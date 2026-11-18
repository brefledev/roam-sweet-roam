# Grok Build in the terminal

Open the launch folder in Grok Build to load its main role. Native named agents add explicit selection and delegation where the installed release supports them.

## Check the CLI and its home

Official releases provide Windows, macOS, and Linux binaries. Follow the [official installation instructions](https://github.com/xai-org/grok-build#installing-the-released-binary), then authenticate. Run `grok --version` and `grok --help`. Use the resolved `grok` executable to avoid clashes with another app's `agent` command. [verified — upstream README]

Resolve `GROK_HOME` before user-level edits. Its default is `~/.grok`, or `%USERPROFILE%\.grok` on native Windows. Preserve a configured custom home and its login state. [verified — [configuration](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md)]

| Purpose | Native location |
|---|---|
| Main-session instructions | `<folder>/AGENTS.md` |
| Named project or user agent | `<folder>/.grok/agents/<name>.md` or `<GROK_HOME>/agents/<name>.md` |
| Project MCP, plugins, and permission rules | `<folder>/.grok/config.toml` |
| User configuration and interactive default agent | `<GROK_HOME>/config.toml` |
| Project or user skills | `<folder>/.grok/skills/<skill>/SKILL.md` or `<GROK_HOME>/skills/<skill>/SKILL.md` |

## Configure the selected agent

Follow [SETUP.md](../SETUP.md). Put the role body and context reads in `AGENTS.md`. Copy declared skills to `.grok/skills/`. For a named native agent, write `.grok/agents/<name>.md` using the installed version's supported frontmatter. The November fixture accepted `name`, `description`, `skills`, and inline `mcpServers`. Preserve the selected model and supported effort. [verified — [skills](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md), [subagents](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/16-subagents.md), repository fixture]

Configure the agent's declared MCP connections and permission rules in `.grok/config.toml`, or supported agent-scoped MCP entries. Review folder trust interactively. Inspect actual startup events and tools. In the tested release, `inspect --json` omitted agent-scoped servers even when startup events reported them. [verified — [MCP](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/07-mcp-servers.md), [VERIFICATION.md](../VERIFICATION.md)]

Current project configuration accepts MCP, plugin, and permission sections. Interactive `[agent] name` or `definition` defaults belong in user configuration. An ACP host can supply its own selection and overrides. Keep each agent's folder instructions complete for hosts that launch the default main agent. [verified — [configuration scope](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md), [agent mode](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/15-agent-mode.md)]

For optional native delegation, confirm that the named agent is discoverable and ask the main agent to delegate to it. Grok's subagent personas are an additional behavioral configuration with their own resolution rules. Translate the existing agent into the supported native agent format. [verified — [agents and personas](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/16-subagents.md)]

## Apply the requested access

These rules denied native file edits and shell execution in Grok Build 1.0.88:

```toml
[permission]
rules = [
  { action = "allow", tool = "read" },
  { action = "allow", tool = "grep" },
  { action = "deny", tool = "edit" },
  { action = "deny", tool = "bash" },
]
```

Check the current schema and tool catalog before reuse. Add explicit restrictions for every other mutating native or MCP tool. Select edit/full permissions from the installed release's documented modes and rules, then check actual behavior. Approval modes and OS containment provide different controls. [verified — [permissions](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/22-permissions-and-safety.md), [sandbox](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/18-sandbox.md), repository fixture]

## Launch and return

The main role loads from the launch folder with the same command syntax in PowerShell and POSIX shells:

```sh
grok --cwd "<folder>"
```

For a named-agent headless check, the November release and current headless reference support:

```sh
grok --cwd "<folder>" --agent <name> -p "Name and role?"
```

Interactive agent-file selection is version-sensitive. Current configuration docs describe `--agent-profile <path>` as an override. Check `grok --help` for the installed selector and write its working command in `LAUNCH.md`. Run that command again to start the selected role. Keep a recorded continuation command separate from a new-session command. [verified — [headless reference](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/14-headless-mode.md), [configuration](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md)]

Use [PLATFORMS.md](../PLATFORMS.md) for environment variables, native paths, and shell quoting. For a desktop host, follow [T3 Code](t3-code.md) and verify that host's effective main-agent selection.

## Record the result

Follow [the verification steps](../SETUP.md#4-verify-the-actual-launch-routes). The November fixture passed named-agent identity, skill loading, fetch/time connection, a time call, and native edit/shell denials. Memory and sequential-thinking startup failed. MCP mutation restrictions and host-specific selection retain the gaps in [VERIFICATION.md](../VERIFICATION.md). [verified — repository verification record]
