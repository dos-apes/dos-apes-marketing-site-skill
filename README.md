<img src="assets/dos-apes-coding-logo.png" alt="Dos Apes coding logo" width="640">

# Marketing Website Skill

A reusable skill by Dos Apes for reviewing public websites, improving existing pages, and building new sites. It covers copy, visual hierarchy, brand consistency, calls to action, responsive layout, purposeful motion, useful demonstrations, and practical verification.

The guidance works with Claude and ChatGPT, for any brand or website. It includes no client profiles, preset brand palettes, product-specific instructions, or required paid services. Supply the context for each project when using it.

## Choose your assistant

| Where you work | What to use |
| --- | --- |
| Claude | [Skill ZIP](https://github.com/dos-apes/dos-apes-marketing-site-skill/releases/latest/download/dos-apes-marketing-site-skill.zip), uploaded as a custom skill |
| Claude Code | Extract the same ZIP into a local skill folder |
| ChatGPT chat | [Self-contained ChatGPT guide](https://github.com/dos-apes/dos-apes-marketing-site-skill/releases/latest/download/dos-apes-marketing-site-guide.txt), attached to the conversation |
| ChatGPT Project | Add the same guide as a project file and use the [project instructions](https://github.com/dos-apes/dos-apes-marketing-site-skill/releases/latest/download/dos-apes-marketing-site-project-instructions.txt) |

The ZIP includes both editions. The ChatGPT guide is generated from the same workflow and references as the Claude skill, with its supporting material combined into one file. This ChatGPT route uses an attached guide or Project context; it does not depend on a native skill installer or claim to install a plugin.

Use the release downloads for setup. GitHub's source-code ZIP includes repository maintenance files and is intended for editing the project.

## Install in Claude

In Claude's skill settings, use the custom-skill upload option to upload the ZIP and enable it. Keep the ZIP's single top-level `dos-apes-marketing-site-skill` folder intact. Custom skills require code execution to be enabled; availability may be controlled by your organization. Interface labels may vary.

## Install in Claude Code

Extract the ZIP and place the entire `dos-apes-marketing-site-skill` folder in either:

- `.claude/skills/` inside a project for use in that repository.
- `~/.claude/skills/` for use across your local projects.

The resulting path must end in `dos-apes-marketing-site-skill/SKILL.md`, with `references` beside it. Invoke `/dos-apes-marketing-site-skill` with your request, or let Claude select it for a relevant task. If a same-named skill already exists, compare it before replacing it.

## Use in ChatGPT

### One conversation

1. Download `dos-apes-marketing-site-guide.txt` using the link above.
2. Attach the text file to your ChatGPT conversation along with your brief, site address, screenshots, or project files.
3. Explicitly ask ChatGPT to follow the attached guide, then describe the outcome you want. For example:

```text
Use the attached Dos Apes Marketing Site Skill guide as the workflow for this task. Review the website and screenshots I supplied. Prioritize improvements and provide replacement copy where useful. Mark anything you cannot inspect as not verified. Review only; do not edit or publish anything.
```

If file upload is unavailable, paste the guide's text into the conversation. The guide includes all its supporting material; you do not need to upload each reference separately or use a slash command.

### Reuse in a Project

Create or open a ChatGPT Project, add the guide as a project file, and paste the instructions above the license notice in `dos-apes-marketing-site-project-instructions.txt` into the project's instructions. Keep related site materials in that Project and start the task there. Replace the guide file when you want to adopt a newer release.

File upload and Project availability depend on the account and workspace. The guide itself does not add tools. Browsing, visual inspection, repository edits, and publishing require suitable capabilities and authorization in the chat you are using. When those are unavailable, it supports review of supplied material, replacement copy, design specifications, and code handoffs, with inspection limits stated.

## Use it

Provide whatever you have: a site address or screenshots, project files, audience, desired visitor action, approved facts, brand assets, and constraints. You do not need to fill out a long brief before starting.

**Review only**

```text
Use dos-apes-marketing-site-skill to review the website I supplied. Check desktop and phone layouts, copy, navigation, and the main visitor journey. Give me prioritized improvements and replacement copy where useful. Preserve what works. Do not edit or publish the site.
```

**Update an existing site**

```text
Use dos-apes-marketing-site-skill to implement the attached changes in this project. Keep the existing brand and business facts. Verify the affected pages on desktop and phone, and provide a local preview. Do not publish yet.
```

**Build a new site**

```text
Use dos-apes-marketing-site-skill to create a working responsive website from my brief and assets. Write the page copy, choose a clear structure, and implement navigation and the requested interactions. Use the existing project tools. Give me a preview and identify any missing content or integrations.
```

In ChatGPT, start the examples above with "Use the attached Dos Apes Marketing Site Skill guide" rather than assuming the skill is installed. You can also provide the self-contained guide to another assistant that accepts text instructions. Browser inspection, code editing, and publishing still require appropriate tools and access.

## Package contents

```text
dos-apes-marketing-site-skill/
  SKILL.md
  README.md
  LICENSE
  assets/
    dos-apes-coding-logo.png
  chatgpt/
    dos-apes-marketing-site-guide.txt
    project-instructions.txt
  references/
    design-and-content.md
    review.md
    build.md
```

Share the complete ZIP for both editions, or the standalone guide for ChatGPT use. The skill format, generated guide, internal links, portability, and archive integrity have been checked. Installation or execution in a recipient's Claude or ChatGPT account has not been independently verified.

## Updating the package

The shared source is `SKILL.md` and `references/`. Edit those files and the setup instructions here, then run:

```sh
python scripts/package.py
```

The script validates the skill, regenerates `chatgpt/dos-apes-marketing-site-guide.txt`, and creates three release downloads in `dist/`:

- `dos-apes-marketing-site-skill.zip`: nine files covering both editions, including the license and README logo.
- `dos-apes-marketing-site-guide.txt`: the self-contained ChatGPT guide.
- `dos-apes-marketing-site-project-instructions.txt`: short reusable Project instructions.

It uses only Python's standard library. The ZIP excludes repository history and maintenance scripts. Do not edit the generated guide directly; change the shared source and rebuild. Commit the regenerated guide with those changes, then attach all three downloads to the new release so the README's links stay valid.

For corrections or suggestions, [open an issue](https://github.com/dos-apes/dos-apes-marketing-site-skill/issues). Include the type of website and a minimal example; remove private client information before posting.

## License and your own copies

Copyright (c) 2026 Dos Apes. This project is available under the [MIT License](LICENSE).

You may use, copy, customize, and redistribute your own copies, including commercially. Keep the copyright and license notice with copies or substantial portions of this project. The ZIP contains the license, and the standalone ChatGPT downloads include it as well.

This permission does not grant write access to the official Dos Apes repository. Changes there remain controlled by its authorized maintainers. You can suggest improvements through an issue or pull request; suggestions do not automatically change the official version.
