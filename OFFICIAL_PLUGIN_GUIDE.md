# 官方 Plugin 提交指南

> 本指南面向 OKX 内部开发者，用于向 `okx/plugin-store` 仓库提交或更新官方 plugin。所有变更必须通过 Pull Request 提交，经过静态检查和 AI 代码审查后由维护者合并。

---

## 规则

1. **禁止直接 push 到 main 分支** — 所有 skills/ 目录的变更必须通过 PR
2. **每个 PR 只改一个 plugin** — 不要在同一个 PR 里修改多个 plugin
3. **不要修改其他 plugin 的文件** — 只改你自己 plugin 目录下的内容
4. **不要修改 registry.json** — PR 合并后由维护者更新 registry

---

## 目录结构

每个官方 plugin 放在 `skills/<plugin-name>/` 下：

```
skills/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json           # Plugin 清单（name, version, description, author）
├── SKILL.md                  # Skill 定义（YAML frontmatter + 操作指南）
├── scripts/                  # Python/Shell 脚本（如有）
│   ├── main.py
│   └── config.py
├── assets/                   # 静态资源（dashboard.html, 图片等）
└── references/               # 参考文档
```

---

## 新增 Plugin

### Step 1: 创建分支

```bash
git clone git@github.com:okx/plugin-store.git
cd plugin-store
git checkout -b plugin/<your-plugin-name>
```

### Step 2: 创建目录和文件

```bash
mkdir -p skills/<your-plugin-name>/.claude-plugin
mkdir -p skills/<your-plugin-name>/scripts
mkdir -p skills/<your-plugin-name>/assets
```

### Step 3: 编写 plugin.json

```json
{
  "name": "<your-plugin-name>",
  "description": "一句话描述",
  "version": "1.0.0",
  "author": { "name": "OKX" },
  "license": "Apache-2.0"
}
```

### Step 4: 编写 SKILL.md

必须包含 YAML frontmatter：

```markdown
---
name: <your-plugin-name>
description: >
  触发关键词和功能描述...
version: 1.0.0
updated: 2026-xx-xx
---

# Plugin 标题

## Disclaimer
...

## Pre-flight Checks
...

## Commands
...

## Error Handling
...
```

### Step 5: 放入脚本和资源

- Python 脚本放 `scripts/`
- HTML/图片放 `assets/`
- 参考文档放 `references/`

### Step 6: 提交 PR

```bash
git add skills/<your-plugin-name>/
git commit -m "[new-plugin] <your-plugin-name> v1.0.0"
git push origin plugin/<your-plugin-name>
```

在 GitHub 上创建 Pull Request，目标分支 `main`。

### Step 7: 等待审查

PR 会自动触发：

```
✅ 静态检查 — 文件结构、版本一致性、URL 验证、命令准确性
📋 AI 代码审查 — Claude 审查 SKILL.md 逻辑、安全性、Python 代码质量
```

审查通过后维护者合并，并更新 registry.json 和 marketplace.json。

---

## 更新 Plugin

### Step 1: 创建分支

```bash
git checkout main && git pull
git checkout -b update/<your-plugin-name>
```

### Step 2: 修改文件

修改 `skills/<your-plugin-name>/` 下的文件。

**必须同步更新版本号：**
- `plugin.json` 的 `version` 字段
- `SKILL.md` frontmatter 的 `version` 字段

### Step 3: 提交 PR

```bash
git add skills/<your-plugin-name>/
git commit -m "[update] <your-plugin-name> v1.1.0"
git push origin update/<your-plugin-name>
```

---

## 审查标准

### 静态检查

| 检查项 | 说明 |
|--------|------|
| plugin.json 存在 | `.claude-plugin/plugin.json` 必须存在 |
| SKILL.md 存在 | 大写，必须有 YAML frontmatter |
| 版本一致 | plugin.json 和 SKILL.md 的 version 必须一致 |
| URL 可达 | SKILL.md 中引用的 URL 必须可访问 |
| Python 语法 | scripts/ 下的 .py 文件必须语法正确 |

### AI 代码审查

| 维度 | 说明 |
|------|------|
| SKILL.md 结构 | 是否有 Pre-flight、Commands、Error Handling 等必要章节 |
| onchainos 合规 | 链上写操作是否通过 onchainos CLI |
| 安全性 | 有无硬编码密钥、prompt injection、危险操作 |
| Python 代码 | 有无安全漏洞、未声明的网络请求、动态代码执行 |
| 逻辑一致性 | SKILL.md 描述是否与脚本实际行为一致 |

---

## 注意事项

- Plugin name 允许使用 `okx-` 前缀（仅限 OKX 组织成员）
- Python 脚本只依赖标准库 + onchainos CLI，不要引入第三方包
- Dashboard HTML 放在 `assets/` 目录
- config.py 中的参数必须有注释说明
- 默认值必须安全：`PAUSED = True`、`PAPER_TRADE = True` 或 `DRY_RUN = True`
