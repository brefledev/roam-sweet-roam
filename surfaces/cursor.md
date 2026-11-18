# Cursor in the editor or CLI

Open the agent's launch folder for its main-session role. Add a native subagent when you also want to delegate a task by name.

## Check the app and its home

Cursor Desktop supports Windows, macOS, and Linux. Current CLI docs provide installers for native Windows PowerShell, macOS, Linux, and WSL. Follow the current [editor quickstart](https://cursor.com/docs/get-started/quickstart) or [CLI setup](https://cursor.com/docs/cli/overview). Authenticate through Cursor. [verified — official installation docs]

Current CLI docs use `agent`. Older releases and some integrations use `cursor-agent`. Resolve the installed executable and run its `--version` and `--help`. Check its publisher/path when another app also supplies `agent`. Keep the working executable's full path in `LAUNCH.md`. [verified — [CLI overview](https://cursor.com/docs/cli/overview), [T3 Cursor integration](https://github.com/pingdotgg/t3code/blob/main/docs/user/cursor.md)]

| Purpose | Native location |
|---|---|
| Main-session instructions | `<folder>/AGENTS.md` or `.cursor/rules/*.mdc` |
| Native subagent | `<folder>/.cursor/agents/<name>.md` or `~/.cursor/agents/<name>.md` |
| Project MCP servers | `<folder>/.cursor/mcp.json` |
| Project skills | `<folder>/.cursor/skills/<skill>/SKILL.md` or `.agents/skills/<skill>/SKILL.md` |
| CLI permissions | `<folder>/.cursor/cli.json` |
| Global CLI settings | `~/.cursor/cli-config.json` |

`CURSOR_CONFIG_DIR` changes the CLI configuration directory. Linux also supports `XDG_CONFIG_HOME`. Resolve these before user-level edits. The editor's user-data directory, CLI settings, and project agent files have separate scopes. See [CLI configuration](https://cursor.com/docs/cli/reference/configuration.md), [rules](https://cursor.com/docs/rules.md), and [skills](https://cursor.com/docs/skills.md). [verified — vendor docs]

## Configure the selected agent

1. Follow [SETUP.md](../SETUP.md). Put the role body and context-read instructions in the launch folder's `AGENTS.md`.
2. Copy declared skills and configure only declared servers in `.cursor/mcp.json`. Cursor MCP configuration supports environment references such as `${env:NAME}`. Resolve each stdio executable in the app's environment. [verified — [MCP configuration](https://cursor.com/docs/mcp.md)]
3. For optional delegation, create `.cursor/agents/<name>.md`:

```markdown
---
name: <name>
description: <when to delegate to this agent>
readonly: true
model: inherit
---

<portable role body and explicit context paths>
```

`readonly: true` requests restricted writes for this subagent. Choose it for a read-only request. Copying the file registers a delegated agent; the main session gets its role from the launch folder's instructions. Cursor also discovers compatible Claude and Codex agent definitions, with native Cursor definitions taking precedence. Inspect duplicates before writing. [verified — [subagents](https://cursor.com/docs/subagents.md)]

For a read-only CLI installation, documented permission tokens support this starting configuration in `.cursor/cli.json`:

```json
{
  "permissions": {
    "allow": ["Read(**)", "WebFetch(*)"],
    "deny": ["Write(**)", "Shell(*)"]
  }
}
```

Verify effective native writes and shell denial in that CLI. Inspect and restrict MCP mutation separately. For edit or full access, configure the selected approval/sandbox mode through the installed app's documented controls. **Ask** mode is a useful main-chat choice for research. A required enforced read-only policy needs its own checks. [verified — [CLI permissions](https://cursor.com/docs/cli/reference/permissions.md), [run modes](https://cursor.com/docs/agent/security/run-modes.md)]

## Choose the model and billing route

Select the parent model in Cursor's picker or with the CLI's `--model` option. A subagent uses `inherit` or a named model. Supported model parameters can include effort, using the documented model-ID options. Confirm the model shown in the task card. [verified — [CLI parameters](https://cursor.com/docs/cli/reference/parameters.md), [subagent model configuration](https://cursor.com/docs/subagents.md#model-configuration)]

Cursor supplies its own model catalog and billing route. Named third-party subagent requests bill to the applicable third-party credit/usage pool even when the parent uses Auto. Account, plan, and team restrictions can change availability or trigger a fallback. Record the actual model and credit route before running a selected vendor model. [verified — [models and pricing](https://cursor.com/docs/models-and-pricing.md), [subagent usage pools](https://cursor.com/docs/subagents.md#parent-model-and-usage-pools)]

## Open and reopen the desktop folder

Choose **File > Open Folder** in Cursor and select the launch folder. Open Agent chat and choose its model and mode. Ask for the role and a context marker. To delegate, type `/<name>` followed by the task, then inspect the resulting subagent card. Reopen the same folder through **File > Open Recent**, or open it again through **Open Folder**. Start a fresh chat after changing native instructions. [verified — [editor quickstart](https://cursor.com/docs/get-started/quickstart), [explicit subagent invocation](https://cursor.com/docs/subagents.md#explicit-invocation)]

## Launch in a terminal

POSIX shell:

```sh
cd "<folder>"
agent
```

PowerShell:

```powershell
Set-Location -LiteralPath "<folder>"
agent
```

Substitute the detected Cursor executable, such as `cursor-agent`, when appropriate. From this folder, `agent --print "Name and role?"` checks the main role. `agent "/<name> Name and role?"` requests the delegated agent. Use [PLATFORMS.md](../PLATFORMS.md) for custom homes, executable paths, and quoting.

## Record the result

Follow [the verification steps](../SETUP.md#4-verify-the-actual-launch-routes). Earlier fixtures installed native files, while a hook timeout blocked the remaining direct native checks. A T3 SDK run is separate evidence. T3 Full access permitted native writes despite the folder's CLI deny rules. Historical desktop setup and fresh-fixture gaps are recorded separately in [VERIFICATION.md](../VERIFICATION.md). [verified — repository verification record]
