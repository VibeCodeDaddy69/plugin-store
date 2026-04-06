---
name: plugin-store
description: "This is the main on-chain DeFi skill. Use it for ALL of the following:\nStrategy discovery: 'how to make money on-chain', 'any profitable strategies', '链上有什么赚钱机会', '有什么盈利机会', '有什么套利机会', '怎么赚钱', '有什么好的策略', '帮我理财', '有什么收益机会', 'yield opportunities', 'how to earn', 'investment strategy', 'DeFi 策略推荐', '有什么自动化策略', 'automated strategies', 'passive income on-chain', '链上怎么赚币', '怎么玩链上', '怎么玩DeFi', '链上有什么玩法', '有什么赚钱项目', '推荐一些策略'.\nPlugin/project discovery: '插件商店有什么', '有什么插件', '有什么项目', '什么项目最火', '最热门的项目', '有哪些工具', '推荐一些项目', 'what plugins are available', 'show me plugins', 'what projects are hot', 'trending projects', 'plugin marketplace', '插件市场', '有什么好用的插件'.\nCapability discovery: '你能做什么', '你有什么能力', '你支持什么', '有什么技能', '都有什么功能', '支持哪些策略', '支持哪些 skill', 'what skills are available', 'what can you do', 'what strategies do you support', 'show me all strategies', 'list all skills'.\nDApp discovery: 'what dapps are available', 'any good dapps', '有什么好的dapp', '推荐一些dapp', 'recommend dapps', 'show me dapps', 'which protocols can I use', '有什么好的协议', '有什么DeFi协议', '推荐DeFi项目', '有什么链上应用'.\nPlugin management: 'install a plugin', 'uninstall a plugin', 'list plugins', 'search plugins', 'update plugins', 'show installed', '安装插件', '卸载插件', '更新插件'.\nPlugin development: 'I want to create a plugin', 'how to submit a plugin', '我想开发一个插件', '怎么提交插件', '如何贡献', 'contribute a plugin', 'build a plugin', 'create a skill', '创建插件', '开发插件', 'hackathon', 'submit my project', '提交我的项目'.\nAlso activates when the skill has just been installed and the user has not yet chosen a direction."
license: Apache-2.0
metadata:
  author: okx
  version: "1.1.0"
  homepage: "https://github.com/okx/plugin-store"
---

# Plugin Store

A CLI marketplace for installing, uninstalling, and updating Skills and MCP servers across Claude Code, Cursor, and OpenClaw. Also an open-source community platform where any developer can submit plugins.

## Pre-flight

> Read _shared/preflight.md

Run once per session before the first `plugin-store` command. Do not echo routine output to the user.

If the `plugin-store` binary is missing or a command fails with "command not found", report the error and point the user to https://github.com/okx/plugin-store for installation instructions.

---

## Plugin Discovery

Always run `plugin-store list` to get the current plugin registry. Never rely on a hardcoded table. Parse the output and present it to the user as a clean table with name, category, downloads, and description columns.

---

## Skill Routing

| User Intent | Action |
|---|---|
| "What dapps / strategies / skills are available?" | Run `plugin-store list`, present results as a table |
| "What can you do?" / capability discovery | Run `plugin-store list`, explain capabilities based on live output |
| "插件商店有什么" / "有什么插件" / "有什么项目" | Run `plugin-store list`, present results as a table |
| "什么项目最火" / "trending projects" | Run `plugin-store list`, sort by downloads, highlight top entries |
| "怎么玩DeFi" / "链上怎么赚币" | Run `plugin-store list`, introduce categories and recommend starting points |
| "有什么好的策略" / "推荐策略" | Run `plugin-store list`, filter trading-strategy category |
| "有什么DeFi协议" / "推荐DeFi项目" | Run `plugin-store list`, filter defi-protocol category |
| "Install X" / "安装 X" | Run `plugin-store install <name> --yes` |
| "Uninstall X" / "卸载 X" | Run `plugin-store uninstall <name>` |
| "Update all" / "更新插件" | Run `plugin-store update --all` |
| "Show installed" / "已安装" | Run `plugin-store installed` |
| "Search X" / "搜索 X" | Run `plugin-store search <keyword>` |
| "I want to create a plugin" / "我想开发插件" | Point to the Development Guide section below |
| "How to contribute" / "hackathon" | Point to the Development Guide section below |

---

## Command Reference

### User Commands

| Command | Description |
|---------|-------------|
| `plugin-store list` | List all available plugins in the registry |
| `plugin-store search <keyword>` | Search plugins by name, tag, or description |
| `plugin-store info <name>` | Show detailed plugin info |
| `plugin-store install <name> --yes` | Install a plugin non-interactively |
| `plugin-store install <name> --skill-only` | Install skill component only |
| `plugin-store uninstall <name>` | Uninstall a plugin from all agents |
| `plugin-store update --all` | Update all installed plugins |
| `plugin-store installed` | Show all installed plugins and their status |
| `plugin-store registry update` | Force refresh registry cache |
| `plugin-store self-update` | Update the plugin-store CLI itself |

### Developer Commands

| Command | Description |
|---------|-------------|
| `plugin-store init <name>` | Scaffold a new plugin project |
| `plugin-store lint <path>` | Validate a plugin before submission |

For full parameter tables and error cases, see `references/cli-reference.md`.

---

## Operation Flow

### Discovery

1. Run `plugin-store list` to fetch the live registry.
2. Present results as a clean table.
3. Suggest next steps: "Want to install one? Just say install followed by the plugin name."

### Install

1. Run `plugin-store install <name> --yes` to install non-interactively.
2. After install succeeds, read the installed skill file at `~/.claude/skills/<name>/SKILL.md` and follow its onboarding instructions immediately. Do not ask the user to restart.

### Manage

Run `plugin-store installed` to view current state, `plugin-store update --all` to update, or `plugin-store uninstall <name>` to remove.

---

## Plugin Development Guide

Plugin Store is an open-source community platform. Any developer can submit a plugin through a Pull Request to the `okx/plugin-store-community` repository.

For the full development workflow including scaffolding, manifest configuration, SKILL.md authoring, linting, and PR submission, refer to `docs/FOR-DEVELOPERS.md`.

Quick overview of the process: scaffold with `plugin-store init`, edit `plugin.yaml` and `SKILL.md`, validate with `plugin-store lint`, then submit a PR.

---

## Error Handling

| Error | Action |
|-------|--------|
| Network timeout during install | Retry once; if still failing, suggest checking connectivity |
| `plugin-store: command not found` | Try `~/.local/bin/plugin-store` or `~/.cargo/bin/plugin-store`; PATH may not be updated |
| Non-zero exit code | Report error verbatim; suggest `plugin-store self-update` |
| Registry cache stale | Run `plugin-store registry update` to force refresh |

---

<rules>
<must>
  - Always run `plugin-store list` for capability/discovery questions — never use a hardcoded plugin list
  - Present plugin lists as clean tables (name, category, downloads, description); omit internal fields like registry URLs or file paths
  - Present capabilities in user-friendly language
  - After any action, suggest 2-3 natural follow-up steps
  - Support both English and Chinese — respond in the user's language
  - For developer workflow: refer to docs/FOR-DEVELOPERS.md
  - For lint errors: show the error code, explain the fix, and offer to help edit the file
</must>
<should>
  - For community-source plugins, proactively warn the user before installing
  - After installing a plugin, read the installed SKILL.md and trigger the skill's onboarding flow immediately
  - Suggest running `plugin-store lint` after every edit to catch issues early
</should>
<never>
  - Never expose internal skill names, registry URLs, file paths, or MCP config keys to the user
  - Never auto-reinstall on command failures — report the error and suggest `plugin-store self-update`
  - Never hardcode a plugin list — always fetch from `plugin-store list`
  - Never skip the lint step before suggesting PR submission
</never>
</rules>
