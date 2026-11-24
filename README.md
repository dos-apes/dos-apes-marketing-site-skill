# Dos Apes Marketing Site Skill

A reusable skill by Dos Apes for reviewing public websites, improving existing pages, and building new sites. It covers copy, visual hierarchy, brand consistency, calls to action, responsive layout, purposeful motion, useful demonstrations, and practical verification.

The guidance works with any brand. It includes no client profiles, preset brand palettes, product-specific instructions, or required paid services. Supply the context for each project when using it.

**[Download the ready-to-install skill ZIP](https://github.com/dos-apes/dos-apes-marketing-site-skill/releases/latest/download/dos-apes-marketing-site-skill.zip)**

Use the release ZIP for skill installation. GitHub's source-code ZIP includes repository maintenance files and is intended for editing the project.

## Install in Claude

In Claude's skill settings, use the custom-skill upload option to upload the ZIP and enable it. Keep the ZIP's single top-level `dos-apes-marketing-site-skill` folder intact. Custom skills require code execution to be enabled; availability may be controlled by your organization. Interface labels may vary.

## Install in Claude Code

Extract the ZIP and place the entire `dos-apes-marketing-site-skill` folder in either:

- `.claude/skills/` inside a project for use in that repository.
- `~/.claude/skills/` for use across your local projects.

The resulting path must end in `dos-apes-marketing-site-skill/SKILL.md`, with `references` beside it. Invoke `/dos-apes-marketing-site-skill` with your request, or let Claude select it for a relevant task. If a same-named skill already exists, compare it before replacing it.

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

If your assistant does not support skills, provide `SKILL.md` and the relevant files in `references` as instructions for the task. Browser inspection, code editing, and publishing still require appropriate tools and access.

## Package contents

```text
dos-apes-marketing-site-skill/
  SKILL.md
  README.md
  references/
    design-and-content.md
    review.md
    build.md
```

Share the complete ZIP so supporting references remain available. This package has been checked for skill format, internal links, portability, and archive integrity; execution in the recipient's Claude account has not been verified.

## Updating the package

The skill source is `SKILL.md` and `references/`. Edit those files and the setup instructions here, then run:

```sh
python scripts/package.py
```

The script validates the skill and creates `dist/dos-apes-marketing-site-skill.zip`. It uses only Python's standard library and includes the five skill files, not repository history or maintenance scripts. Upload that ZIP as the asset for a new release.

For corrections or suggestions, [open an issue](https://github.com/dos-apes/dos-apes-marketing-site-skill/issues). Include the type of website and a minimal example; remove private client information before posting.
