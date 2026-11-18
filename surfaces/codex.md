# Codex in the desktop app or CLI

Open the agent's launch folder to use its role as the main session. Install a native custom subagent separately when you also want other sessions to delegate to it.

## Check the app and its home

The CLI supports Windows, macOS, and Linux. The current ChatGPT desktop app with Codex also provides all three OS routes. Follow the current [CLI installer](https://learn.chatgpt.com/docs/cli), [desktop setup](https://learn.chatgpt.com/docs/app), or [Linux desktop guide](https://learn.chatgpt.com/docs/linux/linux-app), then sign in. Run `codex --version`. [verified — official installation docs]

Resolve `CODEX_HOME` first. Its default is `~/.codex`, including `%USERPROFILE%\.codex` on native Windows. WSL uses its Linux home. Keep an existing custom home and authentication setup. [verified — [environment variables](https://learn.chatgpt.com/docs/config-file/environment-variables)]

| Purpose | Native location |
|---|---|
| Main-session instructions and context directives | `<folder>/AGENTS.md` |
| Trusted project settings and MCP servers | `<folder>/.codex/config.toml` |
| User settings | `<CODEX_HOME>/config.toml` |
| Native custom subagent | `<folder>/.codex/agents/<name>.toml` or the active user's Codex agents directory |
| Project or user skills | `<folder>/.agents/skills/<skill>/SKILL.md` or `~/.agents/skills/<skill>/SKILL.md` |

User skills have their own discovery locations. Inspect the active skill catalog when a custom Codex home is used. See [instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skills](https://learn.chatgpt.com/docs/build-skills), and [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents). [verified — vendor docs]

## Configure the selected agent

1. Follow [SETUP.md](../SETUP.md). Preserve the existing launch folder and portable definition. Put the role body and explicit context reads in `AGENTS.md`. Copy the declared skills.
2. Merge the requested model, supported `model_reasoning_effort`, and MCP entries into `.codex/config.toml`. Configure provider/authentication choices in the active user configuration. Project configuration supports a narrower set of keys. [verified — [configuration precedence](https://learn.chatgpt.com/docs/config-file/config-advanced)]
3. Trust this folder through Codex's interactive prompt so project settings load. Inspect inherited account connectors, global MCP servers, and user skills.

For a requested read-only CLI session, the documented settings are:

```toml
sandbox_mode = "read-only"
approval_policy = "never"

# Add only the agent's declared servers after resolving dependencies.
# [mcp_servers.fetch]
# command = "uvx"
# args = ["mcp-server-fetch"]
```

`workspace-write` and `danger-full-access` select broader filesystem access. Preserve the person's requested approval policy and verify the selected launch method. Windows sandbox backends have different isolation limits. MCP tools and connectors need separate controls, such as `enabled_tools` for an explicit read-tool list. [verified — [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference), [MCP](https://learn.chatgpt.com/docs/extend/mcp), [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox)]

For optional delegation, create `.codex/agents/<name>.toml`:

```toml
name = "<name>"
description = "<when to delegate to this agent>"
developer_instructions = """
<portable role body and explicit context paths>
"""
# model = "<available model ID>"
# model_reasoning_effort = "<supported effort>"
```

Ask the main agent to delegate to this name. The parent supplies its permissions and MCP configuration. Custom agent files support selected capability reductions and model settings; parent sandbox, approval, and provider settings govern the child. [verified — [custom agent schema](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agent-file-schema)]

## Open and reopen the desktop project

In the desktop app, choose **Add new project**, select the launch folder, and start a local chat in that project. For an existing project with multiple folders, use its folder controls to make the agent's folder primary before starting the chat. Give the project the agent's display name. Check the selected model, effort, and permission control beneath the composer. Later, select the same project in the sidebar and start a new chat or reopen its existing conversation. `codex app "<folder>"` offers a terminal entrypoint on supported desktop systems. [verified — [desktop guide](https://learn.chatgpt.com/docs/app), [developer commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli), historical primary-folder evidence in VERIFICATION]

The main role comes from that folder's instructions. A `.codex/agents/` definition supplies a delegated agent. Confirm the active role and context in the selected chat.

## Launch in a terminal

These commands use the same syntax in PowerShell and POSIX shells. Use paths and any custom-home environment setting for that shell as described in [PLATFORMS.md](../PLATFORMS.md).

```sh
codex -C "<folder>"
codex exec --skip-git-repo-check -C "<folder>" "Name and role?"
```

Use the second command for a headless check outside a Git repository. Complete folder trust interactively first. Record the actual command and custom home in `LAUNCH.md`.

## Record the result

Follow [the verification steps](../SETUP.md#4-verify-the-actual-launch-routes) in each chosen app or CLI. November fixture checks passed CLI identity, context, and skill loading and a Windows sandbox write denial. Fixture MCP startup failed. Historical desktop evidence and fresh fixture outcomes have separate entries in [VERIFICATION.md](../VERIFICATION.md). New installations need their own effective-permission and reopen checks. [verified — repository verification record]
