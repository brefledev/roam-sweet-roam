# T3 Code as a desktop host

Add the agent's launch folder as a T3 project, then choose the provider, model, and permission mode for its thread.

## Check the app, provider, and environment

T3 Code provides desktop releases for Windows, macOS, and Linux. Follow the current [installation guide](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md) for your OS and architecture. The desktop app is available on Intel Macs; the current released `t3` executable has a separate architecture limit there. Detect the installed app through its **About** page. Run `t3 --version` when the command exists. [verified — official installation guide]

Install and authenticate the selected provider in the environment where T3 executes it. Open **Settings > Providers**, select that environment, and check the provider status. A local Windows project and a WSL project use their respective binaries, homes, and paths. Set the provider's binary path when required by its integration. [verified — [provider setup and WSL](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md)]

T3's state and each provider's native configuration have separate homes. Preserve the installed T3 home, its projects, and the provider's existing custom-home settings. Inventory `T3CODE_HOME` or a configured `--home-dir` before creating another T3 state directory. Use native settings/provider-instance controls for supported environment overrides. [verified — [T3 state configuration](https://github.com/pingdotgg/t3code/blob/main/apps/server/src/config.ts), [project settings](https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md)]

## Configure the selected agent

1. Follow [SETUP.md](../SETUP.md) and the selected provider guide: [Codex](codex.md), [Claude Code](claude-code.md), [Cursor](cursor.md), or [Grok Build](grok.md). Keep the launch folder's `AGENTS.md`, context, skills, and provider-specific files together.
2. In T3, choose **Add project** and select that exact folder. A desktop file-manager folder drop onto the sidebar also adds it. Give the project the agent's display name.
3. In **Settings > Threads**, select the intended project/environment scope and set defaults for new threads. Choose the provider and an available model, then select supported effort/model parameters. Confirm those values in the new thread. [verified — [project settings](https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md)]
4. Select the permission mode explicitly. Check the effective provider tools and requested restrictions in this thread. T3 settings can override a provider's folder defaults. [verified — [permission modes](https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md), [fixture evidence](../VERIFICATION.md)]

T3 uses provider-native instructions. Folder role loading, provider main-agent selection, and native subagent delegation have separate mechanisms. Verify each requested one. In the November Grok fixture, a project `[agent] name` entry failed to select the main persona. Current Grok configuration reserves that section for user configuration. Keep the folder role complete and record unsupported named-agent selection for that T3 version. [verified — [Grok configuration scope](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md), repository fixture]

## Open and reopen the project

Select the agent's project in the sidebar and start a new thread in the project folder. Choose its provider, model, effort, and permission mode. Ask for the role and a context marker. To return later, select the same project and reopen its thread, or start another thread with the intended defaults. Use a new/restarted provider session after native configuration changes. [verified — [working with threads](https://github.com/pingdotgg/t3code/blob/main/docs/user/thread-sidebar.md)]

With the desktop app already running, this command works in PowerShell and POSIX shells:

```sh
t3 app "<folder>"
```

It opens a new desktop thread and adds the project when needed. The `t3` command can also start a server/web app. For a one-shot agent task, use the selected provider's CLI. Resolve paths and custom-home environment settings through [PLATFORMS.md](../PLATFORMS.md). [verified — [command-line and desktop entrypoints](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md)]

## Check the provider's effective permissions

**Supervised** requests supported approvals. A strict read-only requirement needs verified filesystem, shell, and MCP mutation restrictions in the actual provider session. In November Full-access fixtures, Codex and Cursor wrote test files despite their folder-level read-only/deny settings. [verified — [permission modes](https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md), [VERIFICATION.md](../VERIFICATION.md)]

T3's Cursor integration uses the local Cursor SDK. Current docs say Windows Auto/Supervised with Auto-review can run without filesystem isolation, while restrictive sandbox requests can fail startup. The SDK route and standalone CLI route need separate evidence. After changing Cursor skills, plugins, MCP servers, or CLI OAuth, use **Restart agent session**. MCP OAuth may require a project-scoped CLI login first. [verified — [Cursor provider](https://github.com/pingdotgg/t3code/blob/main/docs/user/cursor.md)]

Review inherited MCP tools for every provider. Keep mutating capabilities disabled when the requested restriction lacks a supported control. Record the effective mode and any omitted capability in `LAUNCH.md`.

## Record the result

Follow [the verification steps](../SETUP.md#4-verify-the-actual-launch-routes) through this T3 provider. November checks covered project binding and selected provider calls. GUI/reopen behavior, complete read-only enforcement, several MCP loading paths, and Grok main-agent selection retained gaps. Historical desktop observations and these fixture results are recorded separately in [VERIFICATION.md](../VERIFICATION.md). [verified — repository verification record]
