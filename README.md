# Family OS

A privacy-first household operating system for AI agents.

Family OS helps an AI assistant initialize and maintain a local household workspace for family facts, projects, decisions, risks, reminders, reviews, and long-term development plans. It is designed for sensitive household information: the reusable skill stays generic, while private family data remains in the user's local workspace.

## Why

Most families already have scattered notes, screenshots, contracts, bills, parenting plans, financial ideas, and unfinished decisions. AI assistants can help, but they need a stable local structure and clear privacy boundaries.

Family OS provides that structure:

- Local-first household data.
- Agent-readable workspace rules.
- Conversation-triggered updates.
- Projects, areas, decisions, memory, reviews, and archive.
- Multilingual workspace templates.
- Privacy rules for sensitive family information.

## What It Can Manage

- Parenting and birth preparation.
- Household finance and long-term planning.
- Health and care logistics.
- Career and income resilience.
- Housing, insurance, education, documents, and admin tasks.
- Household vendors, services, and recurring operations.
- Major decisions and family development paths.

## Repository Structure

```text
family-os/
  skill/       # The installable Codex skill package
  examples/    # Privacy-safe demo workspaces
  tests/       # Basic script tests
```

## Install

Clone this repository, then link the skill into your Codex skills directory:

```bash
git clone https://github.com/living-hi/family-os.git
ln -s "$(pwd)/family-os/skill" "$HOME/.codex/skills/family-os"
```

Or copy `skill/` into your skills directory:

```bash
cp -a family-os/skill "$HOME/.codex/skills/family-os"
```

## Initialize A Workspace

Create a private household workspace:

```bash
family-os/skill/scripts/family_os_init.py \
  --workspace "$HOME/family-os-workspace" \
  --language auto
```

To force a language:

```bash
family-os/skill/scripts/family_os_init.py \
  --workspace "$HOME/family-os-workspace" \
  --language zh-CN
```

The initializer supports Chinese, English, Japanese, Korean, Spanish, French, German, and Portuguese templates. Unknown languages fall back to English; an AI agent can then localize generated headings and template text.

## Typical Agent Prompts

```text
Use $family-os to initialize my household workspace in Chinese.
```

```text
Use $family-os. Record this family update and update the relevant dashboard, project, and reminders.
```

```text
Use $family-os to review my current household priorities and suggest this week's next actions.
```

## Privacy Model

Family OS separates reusable instructions from private household data:

- `skill/`: generic, publishable, no private data.
- your workspace: private local household facts, plans, contracts, notes, and decisions.

Do not commit your real workspace. Only commit sanitized examples.

## Workspace Layout

```text
family-workspace/
  00-inbox/
  01-dashboard/
  02-areas/
  03-projects/
  04-decisions/
  05-memory/
  90-reviews/
  99-archive/
```

Directory names stay stable by default so scripts can rely on them. Human-facing file headings and content should use the user's language.

## Run Checks

```bash
python3 -m unittest discover -s tests
```

You can also check a workspace manually:

```bash
skill/scripts/family_os_check.py --workspace "$HOME/family-os-workspace"
skill/scripts/family_os_status.py --workspace "$HOME/family-os-workspace"
```

## Status

Early but usable. The skill can initialize workspaces, check structure, summarize dashboard state, and guide AI agents through privacy-aware household updates.

## License

MIT
