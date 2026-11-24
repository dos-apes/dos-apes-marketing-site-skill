"""Validate and package the public skill. Requires only Python's standard library."""

from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import zipfile


NAME = "dos-apes-marketing-site-skill"
FILES = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "references/design-and-content.md",
    "references/review.md",
    "references/build.md",
    "chatgpt/dos-apes-marketing-site-guide.txt",
    "chatgpt/project-instructions.txt",
)
ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/dos-apes/dos-apes-marketing-site-skill"
GUIDE_NAME = "dos-apes-marketing-site-guide.txt"
PROJECT_INSTRUCTIONS_NAME = "dos-apes-marketing-site-project-instructions.txt"
GUIDE_SOURCES = ("SKILL.md", "references/design-and-content.md", "references/review.md", "references/build.md")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def build_chatgpt_guide():
    """Combine the shared instructions without leaving missing file references."""
    headings = {
        "review.md": "Review or update an existing website",
        "build.md": "Build a new site or implement updates",
        "design-and-content.md": "Shared design and content checks",
    }
    sections = []
    source_hash = hashlib.sha256()
    for relative in GUIDE_SOURCES:
        path = ROOT / relative
        require(path.is_file() and not path.is_symlink(), "Missing guide source: " + relative)
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        source_hash.update(relative.encode("utf-8") + b"\0" + text.encode("utf-8"))
        if relative == "SKILL.md":
            text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)
            text = text.replace("# Dos Apes Marketing Site Skill", "# Core workflow", 1)
            text = re.sub(r"^Installation and example requests are in .*README\.md.*\n?", "", text, flags=re.M)

        def embedded_reference(match):
            label, target = match.groups()
            name = PurePosixPath(target.split("#", 1)[0]).name
            require(name in headings, "Unresolved reference in standalone guide: " + target)
            return label + ' (see "' + headings[name] + '" in this guide)'

        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", embedded_reference, text)
        sections.append(text.strip())

    introduction = (
        "DOS APES MARKETING SITE SKILL — CHATGPT GUIDE\n\n"
        "This self-contained edition includes the same workflow, design checks, "
        "review guidance, and build guidance as the native skill package.\n\n"
        "HOW TO USE\n"
        "Attach this file to a ChatGPT conversation and explicitly ask: "
        "'Use the attached Dos Apes Marketing Site Skill guide for this task.' "
        "Then provide your website, screenshots, project files, or brief and say "
        "whether you want a review, updates, a concept, or a new site. "
        "If attaching a file is unavailable, paste its text into the chat.\n\n"
        "For repeated use, add this file to a ChatGPT Project and set that "
        "Project's instructions to use it for relevant website tasks. "
        "This is conversation guidance; it does not install a plugin, enable "
        "tools, grant access, or override the user's specific instructions. "
        "Use only the sections relevant to the requested task.\n\n"
        "MAINTENANCE\n"
        "Generated from the shared skill source. Edit SKILL.md and references/ "
        "in the repository and rebuild rather than editing this copy.\n"
        "Source fingerprint: " + source_hash.hexdigest() + "\n"
    )
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8").strip()
    guide = introduction + "\n\n" + "\n\n---\n\n".join(sections) + "\n\n---\n\nLICENSE\n\n" + license_text + "\n"
    require(not re.search(r"\[[^\]]+\]\([^)]+\.md[^)]*\)", guide), "Standalone guide has unresolved file links.")
    output = ROOT / "chatgpt" / GUIDE_NAME
    output.parent.mkdir(exist_ok=True)
    require(not output.is_symlink() and output.resolve().is_relative_to(ROOT), "Unsafe guide output path.")
    output.write_text(guide, encoding="utf-8", newline="\n")


def package():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    require(frontmatter is not None, "SKILL.md needs YAML frontmatter.")
    # The distributed metadata intentionally uses two plain scalar fields.
    metadata = {}
    for line in frontmatter[1].splitlines():
        key, separator, value = line.partition(":")
        require(bool(separator), "Each metadata field needs a key and value.")
        require(key not in metadata, "Duplicate metadata field: " + key)
        metadata[key] = value.strip()
    require(set(metadata) == {"name", "description"}, "Expected name and description metadata.")
    require(metadata["name"] == NAME, "Skill name does not match the package folder.")
    require(0 < len(metadata["description"]) <= 200, "Description must be 1-200 characters.")
    require(not re.search(r"[<>]|:\s|\s#", metadata["description"]), "Use a plain description scalar.")

    build_chatgpt_guide()

    contents = {}
    link_count = 0
    for relative in FILES:
        path = ROOT / relative
        require(path.is_file() and not path.is_symlink(), "Missing or unsafe file: " + relative)
        require(path.resolve().is_relative_to(ROOT), "File escapes the repository: " + relative)
        text = path.read_text(encoding="utf-8")
        require(bool(text.strip()), "Empty file: " + relative)
        require(not re.search(r"(?i)\b[a-z]:[\\/]|/Users/|/home/|mailto:", text), "Remove machine-specific paths or email addresses: " + relative)
        urls = re.findall(r"https?://[^\s)<>]+", text)
        require(all(url == REPOSITORY or url.startswith(REPOSITORY + "/") for url in urls), "Unexpected external source link: " + relative)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("https://", "#")):
                continue
            linked = (path.parent / target.split("#", 1)[0]).resolve()
            require(linked.is_relative_to(ROOT) and linked.is_file(), "Broken relative link: " + target)
            require(linked.relative_to(ROOT).as_posix() in FILES, "Linked file is not included in the ZIP: " + target)
            link_count += 1
        # Normalize source line endings so output is identical on each platform.
        contents[relative] = text.replace("\r\n", "\n").encode("utf-8")

    destination = ROOT / "dist" / (NAME + ".zip")
    destination.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for relative in sorted(contents):
            info = zipfile.ZipInfo(NAME + "/" + relative, date_time=(2026, 11, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, contents[relative])
    with zipfile.ZipFile(destination) as archive:
        require(archive.testzip() is None, "ZIP integrity check failed.")
        require(set(archive.namelist()) == {NAME + "/" + name for name in FILES}, "Unexpected ZIP contents.")
        for member in archive.infolist():
            name = PurePosixPath(member.filename)
            require(not name.is_absolute() and ".." not in name.parts, "Unsafe ZIP path.")
            relative = name.relative_to(NAME).as_posix()
            require(archive.read(member) == contents[relative], "ZIP content differs from source.")

    standalone_guide = destination.parent / GUIDE_NAME
    standalone_instructions = destination.parent / PROJECT_INSTRUCTIONS_NAME
    standalone_guide.write_bytes(contents["chatgpt/" + GUIDE_NAME])
    standalone_instructions.write_bytes(
        contents["chatgpt/project-instructions.txt"].rstrip()
        + b"\n\n---\n\nLICENSE (reuse notice; not part of the Project instructions)\n\n"
        + contents["LICENSE"]
    )
    print(json.dumps({
        "archive": str(destination),
        "files": len(FILES),
        "relative_links_checked": link_count,
        "bytes": destination.stat().st_size,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "chatgpt_downloads": [
            {"file": str(path), "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in (standalone_guide, standalone_instructions)
        ],
    }, indent=2))


if __name__ == "__main__":
    package()
