# Contributing

Family OS is designed for private household data. Please keep the project safe to share.

## Rules

- Do not commit real family data, names, addresses, financial details, medical details, contracts, screenshots, or identity information.
- Use only synthetic or heavily sanitized examples.
- Keep the skill package generic and reusable.
- Prefer local-first workflows.
- Add tests when changing scripts.

## Development

Run tests:

```bash
python3 -m unittest discover -s tests
```

Validate the skill with Codex's skill validator when available:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skill
```

## Language Templates

If adding a language to `family_os_init.py`, include enough translated headings to make a first workspace feel native. Keep canonical directory names stable unless a separate localization strategy is added.
