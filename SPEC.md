# Agent sources and native configuration

Keep a selected agent's existing source definition and translate it into the chosen apps' native configuration. A source can be an existing native agent, a folder of instructions and context, or the optional portable format below. Record the source path and generated destinations in `LAUNCH.md`.

Preserve detailed permissions, native hooks, MCP scope, context imports, provider, model, and effort from that source. Resolve unsupported settings explicitly. A translation that omits a required capability remains incomplete.

## Agent files

```text
<agent>/
  AGENT.md
  skills/<skill>/SKILL.md
  context/<file>
```

`AGENT.md` has YAML frontmatter and a Markdown instruction body. `skills/` and `context/` are optional.

```markdown
---
name: researcher
display_name: Researcher
description: Read primary sources and report findings with citations.
access: read-only
mcp_servers: {}
skills: []
context: []
models: {}
---

You are Researcher. Answer from sources and cite your evidence.
```

| Field | Meaning |
|---|---|
| `name` | Required stable slug using lowercase letters, digits, and hyphens. Used in native filenames, profiles, and CLI flags. |
| `display_name` | Optional human-readable name. Defaults to `name`. |
| `description` | Required description of the agent's purpose. |
| `access` | Required shorthand for this optional format: `read-only`, `edit`, or `full`. Preserve detailed access rules in the body and native source. |
| `mcp_servers` | Optional map of server names to stdio or remote definitions. |
| `skills` | Optional relative paths to [Agent Skills](https://agentskills.io) folders containing `SKILL.md`. |
| `context` | Optional relative paths to files the agent should read at startup. |
| `models` | Optional per-app model selections, using `claude`, `codex`, `cursor`, `grok`, or `hermes` keys. A value can be a model ID string or a map containing `provider`, `model`, and `effort`. T3 uses its selected provider and runtime options. Preserve existing defaults when omitted. |
| Markdown body | Required agent instructions. |

Relative paths in a shared portable package resolve inside its agent folder. Copy redistributable dependencies when sharing. During a local installation, preserve intentional references to the user's existing context and skills. Record their resolved paths. Report missing files before activating the affected capability.

For example, preserve a supported Codex model and effort selection with the following optional metadata. The installer checks the actual account's available models before applying it.

```yaml
models:
  codex:
    model: gpt-6.1-sol
    effort: high
```

Translate effort through the installed app's native setting. A Cursor subscription model identifier, a direct Grok model identifier, and a T3 provider selection describe distinct routes. Keep each selected route explicit in `LAUNCH.md`.

## MCP definitions

A stdio server has `command`, optional `args`, and optional `env`. A remote server has `url` and its supported authentication references. For example:

```yaml
mcp_servers:
  time:
    command: uvx
    args: ["mcp-server-time"]
```

Represent a required credential as `${VARIABLE_NAME}`. The installing assistant translates that reference into the app's environment syntax and reports how the variable is supplied. Never serialize the secret value into an agent or launch file.

Server commands require their runtimes on the recipient's machine. Resolve launchers, environment references, and executable paths for Windows, macOS, or Linux using [platform preparation](PLATFORMS.md) and the native guide. Agent-private storage also needs an agent-owned backing-data path. Enable a server after its connection and applicable permission checks pass.

## Requested access

| Level | Required behavior |
|---|---|
| `read-only` | Read and research. Block agent-initiated file edits, state-changing shell commands, and mutating MCP tools. |
| `edit` | Edit within the agreed project or launch folder. Require approval for destructive commands. |
| `full` | Use the app's full-access mode within the person's authorization. |

Each app determines effective access. The installer checks native tools, shell execution, and MCP tools separately, including inherited tools. When a requirement cannot be enforced, the affected launch method or capability stays disabled and the launch guide records the limitation. App-maintained sessions and caches follow the app's own behavior.

## Native output

Retain the chosen source. Folder-based installations add the selected apps' native entrypoints and a personal `LAUNCH.md`. A Hermes-only or user-level-subagent installation can keep the launch guide beside its source. Generate files required by the selected routes. Reuse existing working folders and native profile names.

| App | Native output |
|---|---|
| [Claude Code](surfaces/claude-code.md) | `CLAUDE.md`, `.claude/agents/<name>.md`, `.claude/settings.json`, `.claude/skills/` |
| [Codex](surfaces/codex.md) | `.codex/config.toml`, `.agents/skills/`; `AGENTS.md` supplies the main-session instructions |
| [Cursor](surfaces/cursor.md) | `.cursor/agents/<name>.md`, `.cursor/mcp.json`, `.cursor/cli.json`, `.agents/skills/` |
| [Grok Build](surfaces/grok.md) | `.grok/agents/<name>.md`, `.grok/config.toml`, `.grok/skills/` |
| [Hermes](surfaces/hermes.md) | A native profile containing `SOUL.md`, `config.yaml`, and `skills/`; the launch guide points to it |
| [T3 Code](surfaces/t3-code.md) | A project pointing at the launch folder, with the chosen provider's native files |

Names in native files and commands come from the selected agent's `name`. The [fictional example](examples/bob/) supplies a sample definition and test fixture.

## Verification and scope

[VERIFICATION.md](VERIFICATION.md) records historical setups, native fixture checks, and remaining gaps. Grade each agent, OS, app version, and launch route separately. Record every required MCP call, declared skill, context input, and permission check. Existing history establishes its recorded setup; a new installation needs its own applicable checks.

This version covers local desktop apps and CLIs. Cloud environments, multi-machine sync recipes, and a configuration-generator CLI remain future work.
