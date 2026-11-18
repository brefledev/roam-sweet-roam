# Claude Code in the desktop app or CLI

Use a launch folder for a dedicated main-session role. A native Claude agent file also lets another session delegate to that agent.

## Check the app and its home

The CLI supports native Windows, macOS, and Linux. Windows can also use WSL. Native Windows uses PowerShell and can use Git Bash when Git for Windows is installed. Follow [CLI setup](https://code.claude.com/docs/en/setup), sign in, and run `claude --version`. [verified — official setup docs]

Claude Desktop includes the **Code** tab on macOS, Windows, and Linux beta. It requires an eligible subscription. The Code tab includes its runtime. Install the CLI separately when you want terminal launches. [verified — [desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart)]

Resolve `CLAUDE_CONFIG_DIR` before user-level edits. The default is `~/.claude`, or `%USERPROFILE%\.claude` on Windows. Preserve an existing custom home. [verified — [settings files](https://code.claude.com/docs/en/settings)]

| Purpose | Native location |
|---|---|
| Folder instructions | `<folder>/CLAUDE.md`, importing `@AGENTS.md` |
| Project agent and skills | `<folder>/.claude/agents/<name>.md`, `.claude/skills/<skill>/SKILL.md` |
| User agent and skills | `<CLAUDE_CONFIG_DIR>/agents/<name>.md`, `skills/<skill>/SKILL.md` |
| Default main agent and permissions | `<folder>/.claude/settings.json` |
| Shared project MCP connections | `<folder>/.mcp.json` |

## Configure the selected agent

Follow [SETUP.md](../SETUP.md). Preserve existing files and merge the agent's instructions and context reads. A main-session role can live in `CLAUDE.md` through existing imports such as `@SOUL.md` and `@CHARTER.md`. For a shared `AGENTS.md` source, add `@AGENTS.md` once to `CLAUDE.md`.

For a named delegated agent, create `.claude/agents/<name>.md`:

```markdown
---
name: <name>
description: <when to use this agent>
tools: Read, Grep, Glob, WebFetch, WebSearch, Skill
skills:
  - <declared-skill>
---

<portable role body and explicit context paths>
```

The example requests native read tools. Choose tools for the actual access request. Add supported `model` and `effort` frontmatter only when selected. Copy each declared skill to `.claude/skills/<skill>/`. The `skills` list preloads skills. Review the complete inherited catalog. [verified — [agent fields and capabilities](https://code.claude.com/docs/en/sub-agents), [skills](https://code.claude.com/docs/en/skills)]

For dedicated main-session settings, create `.claude/agents/<name>-primary.md` with the selected native frontmatter and keep the role instructions in the folder's `CLAUDE.md` imports. An empty agent body preserves the default system prompt on the historically tested route. Merge the main selector into `.claude/settings.json`:

```json
{ "agent": "<name>-primary" }
```

Keep the delegated `<name>` definition's full role body and context paths. Ask another main session to use that agent. A user-level installation makes it discoverable across folders. Give that definition absolute context paths, since the calling session can use a different working directory. [verified — [agent invocation](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly)]

Configure the declared MCP servers through `.mcp.json` or the agent's supported `mcpServers` frontmatter. Trust the folder interactively. Add permission approvals for the exact read tools you intend to auto-approve. Native tool availability and permission approval are distinct settings. Memory and other mutating MCP servers require per-tool restrictions. [verified — [MCP](https://code.claude.com/docs/en/mcp), [permissions](https://code.claude.com/docs/en/permissions)]

For read-only access, use an explicit native and MCP read-tool allowlist. Edit and full access require the person's selected tools and approval mode. Native Windows provides tool permission controls; OS shell sandboxing is available on supported macOS/Linux and WSL2 environments. Check shell, MCP, and connector mutation separately. [verified — [sandboxing](https://code.claude.com/docs/en/sandboxing), [setup platform comparison](https://code.claude.com/docs/en/setup#set-up-on-windows)]

## Open and reopen the desktop session

Open Claude Desktop's **Code** tab, start a **New session**, select **Local**, and choose the launch folder. Choose the intended model and permission mode. Leave **Worktree** off when opening the established agent folder directly. Git worktree sessions need the native configuration and context in their selected working tree. [verified — [start a desktop session](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session), historical folder-launch record in VERIFICATION]

The folder's `agent` setting selects its main role. Ask the agent to read its context and name its role. To return, select the saved local environment or folder and start a new session, or reopen the earlier session in the sidebar. For a custom `CLAUDE_CONFIG_DIR`, follow Desktop's environment setup and quit/reopen the app so it receives that value. [verified — [desktop environments](https://code.claude.com/docs/en/desktop#environment-configuration)]

## Launch in a terminal

POSIX shell:

```sh
cd "<folder>"
claude
```

PowerShell:

```powershell
Set-Location -LiteralPath "<folder>"
claude
```

From that folder, `claude` uses its configured primary agent. `claude --agent <name>` selects the full-body named agent explicitly. `claude --agent <name> -p "Name and role?"` runs a headless check. Native agent selection persists when resuming its session. [verified — [agent invocation](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly)]

Resolve home variables, dependencies, and shell quoting through [PLATFORMS.md](../PLATFORMS.md). Record the real path and launch command in `LAUNCH.md`.

## Record the result

Follow [the verification steps](../SETUP.md#4-verify-the-actual-launch-routes). November fixture checks passed main-agent identity, a declared skill, MCP calls, and restricted native tools. A fresh isolated home lacked authentication. Keep that fixture outcome and historical desktop evidence separate in [VERIFICATION.md](../VERIFICATION.md). Check the selected desktop environment, new-session loading, and actual permissions for this installation. [verified — repository verification record]
