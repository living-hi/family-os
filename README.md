# Family OS

Language: [English](#english) | [中文](#中文说明)

## English

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
  skill/       # The installable agent skill package
  examples/    # Privacy-safe demo workspaces
  tests/       # Basic script tests
```

## Install

Install from ClawHub:

```bash
clawhub install family-os
```

Or clone this repository, then link the skill into your local skills directory:

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

## 中文说明

面向 AI 智能体的本地隐私优先家庭操作系统。

Family OS 帮助 AI 助手初始化并维护一个本地家庭工作区，用来管理家庭事实、项目、决策、风险、提醒、复盘和长期发展规划。它适合处理敏感家庭资料：可开源的技能包保持通用，真实家庭数据只保存在用户自己的本地工作区。

### 为什么需要

很多家庭资料分散在聊天记录、截图、合同、账单、育儿计划、财务想法和未完成决策里。AI 可以帮忙整理和推进，但前提是有稳定的本地目录结构和明确的隐私边界。

Family OS 提供：

- 本地优先的家庭资料管理。
- AI 智能体可读取的工作区规则。
- 对话触发式更新。
- 项目、领域、决策、记忆、复盘和归档结构。
- 多语言工作区模板。
- 面向敏感家庭信息的隐私规则。

### 可以管理什么

- 孕产、育儿和新生儿准备。
- 家庭财务、预算、安全垫和长期规划。
- 健康、医疗和照护后勤。
- 职业、收入和风险对冲。
- 住房、保险、教育、证件和行政事务。
- 家政、服务商、采购和家庭日常运营。
- 重大决策记录和家庭发展路径。

### 安装

从 ClawHub 安装：

```bash
clawhub install family-os
```

也可以克隆仓库后，将 `skill/` 软链接到本地 skills 目录：

```bash
git clone https://github.com/living-hi/family-os.git
ln -s "$(pwd)/family-os/skill" "$HOME/.codex/skills/family-os"
```

也可以直接复制：

```bash
cp -a family-os/skill "$HOME/.codex/skills/family-os"
```

### 初始化中文家庭工作区

```bash
family-os/skill/scripts/family_os_init.py \
  --workspace "$HOME/family-os-workspace" \
  --language zh-CN
```

自动按用户环境选择语言：

```bash
family-os/skill/scripts/family_os_init.py \
  --workspace "$HOME/family-os-workspace" \
  --language auto
```

目前内置中文、英文、日文、韩文、西班牙文、法文、德文、葡萄牙文模板。

### 典型提示词

```text
Use $family-os to initialize my household workspace in Chinese.
```

```text
使用 $family-os，记录这条家庭更新，并同步更新相关 dashboard、项目和提醒。
```

```text
使用 $family-os，帮我复盘当前家庭优先级，并给出本周下一步行动。
```

### 隐私模型

Family OS 把通用技能和私有家庭数据分开：

- `skill/`：通用、可发布、不含私密数据。
- 你的家庭工作区：本地私有资料，包括家庭事实、计划、合同、笔记和决策。

不要把真实家庭工作区提交到公开仓库。公开分享时只使用脱敏示例。

### 运行检查

```bash
python3 -m unittest discover -s tests
skill/scripts/family_os_check.py --workspace "$HOME/family-os-workspace"
skill/scripts/family_os_status.py --workspace "$HOME/family-os-workspace"
```

## License

MIT
