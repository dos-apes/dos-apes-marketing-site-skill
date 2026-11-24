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
    "references/design-and-content.md",
    "references/review.md",
    "references/build.md",
)
ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/dos-apes/dos-apes-marketing-site-skill"


def require(condition, message):
    if not condition:
        raise ValueError(message)


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
    print(json.dumps({
        "archive": str(destination),
        "files": len(FILES),
        "relative_links_checked": link_count,
        "bytes": destination.stat().st_size,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    }, indent=2))


if __name__ == "__main__":
    package()
