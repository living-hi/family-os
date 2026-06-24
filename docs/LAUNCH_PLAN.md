# Launch Plan

## Positioning

Family OS is a privacy-first household operating system for AI agents.

Short pitch:

> A local-first workspace and Codex skill that helps AI agents organize household facts, projects, decisions, risks, reminders, and long-term family plans.

Chinese pitch:

> Family OS 是一个面向 AI 智能体的本地隐私优先家庭操作系统，用来管理家庭事实、项目、决策、风险、提醒和长期规划。

## Primary Audience

- New parents and expecting families.
- Dual-income households with many logistics.
- People who already use AI agents, Obsidian, Notion, Logseq, or local Markdown notes.
- FIRE, personal finance, and long-term planning communities.
- Privacy-conscious users who do not want to upload household records to SaaS tools.

## Launch Checklist

1. Create a clean GitHub repository named `family-os`.
2. Confirm the repository contains no real household data.
3. Run `python3 -m unittest discover -s tests`.
4. Run the Codex skill validator on `skill/`.
5. Add repository topics:
   - `ai-agent`
   - `codex-skill`
   - `family`
   - `household`
   - `local-first`
   - `privacy`
   - `markdown`
   - `personal-os`
6. Add screenshots or terminal GIFs:
   - initialize Chinese workspace
   - record a household update
   - show dashboard/status output
7. Publish a short demo post in Chinese and English.

## Demo Script

Prompt:

```text
Use $family-os to initialize a Chinese household workspace for a new parent family.
```

Then:

```text
Use $family-os. Record this update: next Tuesday is a prenatal checkup, the doula contract still needs refund terms checked, and we need a hospital bag checklist this week.
```

Expected outcome:

- Dashboard priority updates.
- Risk/reminder update.
- Parenting or logistics project update.
- Sensitive details remain local.

## Content Ideas

- "I built a local-first Family OS for AI agents."
- "家庭资料太散？我做了一个给 AI 用的 Family OS."
- "How to use AI without uploading your family life to a SaaS database."
- "From scattered screenshots to household decisions: a local-first AI workflow."

## Distribution

Chinese:

- 即刻
- 少数派
- 知乎
- V2EX
- 小红书
- Bilibili

English:

- GitHub
- Hacker News
- Reddit: r/selfhosted, r/LocalLLaMA, r/productivity, r/ObsidianMD
- X / Twitter
- LinkedIn

## What Not To Claim

- Do not claim background automation unless a scheduler is added.
- Do not claim medical, legal, or financial advice.
- Do not imply private data is safe if users upload their workspace to a public repository.
- Do not present examples as real family records.

## Improvement Roadmap

- Add screenshots and GIFs.
- Add more localized templates.
- Add an Obsidian vault mode.
- Add project templates for newborn prep, move, insurance review, school selection, and elder care.
- Add optional reminder integration.
- Add a migration assistant for existing family folders.
- Add a privacy scanner that warns before committing sensitive files.
