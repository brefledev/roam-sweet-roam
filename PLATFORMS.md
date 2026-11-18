# Prepare Windows, macOS, or Linux

The installing assistant detects your OS, architecture, shell, installed versions, and configuration homes before writing files. Choose the apps you use. Desktop and CLI installations can have separate executables, environment variables, and authentication.

## Install the selected apps

Use each vendor's download or installation instructions for your OS. The following sources were checked on November 17, 2026. Their availability describes vendor support. The [verification record](VERIFICATION.md) identifies execution evidence.

| App | Windows | macOS | Linux | Official installation source |
|---|---|---|---|---|
| Codex in the ChatGPT desktop app | Native app | Native app | Native app; check distribution and architecture | [Desktop app](https://learn.chatgpt.com/docs/app), [Linux](https://learn.chatgpt.com/docs/linux/linux-app) |
| Codex CLI | Native Windows or WSL, with different sandbox environments | Native CLI | Native CLI | [Codex source and installation](https://github.com/openai/codex), [Windows](https://developers.openai.com/codex/windows/) |
| Claude Desktop Code tab | Native app | Native app | Linux beta; check supported distributions | [Desktop installation and Code tab](https://code.claude.com/docs/en/desktop) |
| Claude Code CLI | Native Windows or WSL | Native CLI | Native CLI | [Claude Code setup](https://code.claude.com/docs/en/setup) |
| Cursor desktop | Native app | Native app | Native app | [Cursor download and install](https://cursor.com/docs/get-started/installation) |
| Cursor Agent CLI | Native PowerShell installer or WSL | Native CLI | Native CLI | [Current CLI overview](https://cursor.com/docs/cli/overview) |
| Hermes | Native CLI; MSIX desktop requires Windows 11 22H2+ | Apple Silicon desktop bundle; Intel uses CLI and `hermes desktop` | Native CLI; desktop release packaging disabled, local builds available | [Platform support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support), [quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) |
| T3 Code | Native desktop | Native desktop | Native desktop | [T3 installation](https://github.com/pingdotgg/t3code#install) |
| Grok Build CLI | Resolve the package's Windows requirements | Resolve the package's macOS requirements | Resolve the package's Linux requirements | [Grok Build](https://github.com/xai-org/grok-build), [native guide](surfaces/grok.md) |

Check CPU architecture and minimum OS versions on the linked installer page. Use the app's ordinary login. A subscription-backed route and an API-key route can have different billing and model availability. Preserve the user's chosen route.

## Resolve the native configuration homes

Start with the installed app's settings and supported environment overrides. The native guides identify agent, skill, MCP, and project paths inside these homes.

| Configuration | macOS and Linux convention | Windows convention |
|---|---|---|
| Codex user files | `$CODEX_HOME`, normally `~/.codex` | `CODEX_HOME`, normally `%USERPROFILE%\.codex` |
| Claude Code user files | `CLAUDE_CONFIG_DIR`, normally `~/.claude` | `CLAUDE_CONFIG_DIR`, normally `%USERPROFILE%\.claude` |
| Cursor agent definitions | `~/.cursor/agents` | `%USERPROFILE%\.cursor\agents` |
| Grok definitions | `~/.grok`, subject to installed CLI configuration | `%USERPROFILE%\.grok`, subject to installed CLI configuration |
| Hermes profiles | Resolve `HERMES_HOME` and `hermes profile list`; commonly `~/.hermes/profiles` | Resolve `HERMES_HOME` and `hermes profile list`; desktop installations commonly use `%LOCALAPPDATA%\hermes\profiles` |

A desktop project's folder is the user's agent or work folder. Its native configuration files live inside that folder where the app supports project configuration. Reuse an existing folder. Choose a new folder according to the user's organization. Vendor configuration homes and desktop launch folders serve different purposes.

Preserve existing home overrides. Creating a new configuration home also creates a separate trust or authentication context in some apps. Keep the original account and settings intact while resolving that new context.

## Use commands for the selected shell

The assistant writes actual paths into your `LAUNCH.md`. These examples show how to enter an already chosen agent folder. Replace the sample path with that folder.

macOS Terminal, zsh or bash:

```sh
cd "/Users/you/Work/Researcher"
```

Linux terminal, bash or zsh:

```sh
cd "/home/you/Work/Researcher"
```

Windows Terminal, PowerShell:

```powershell
Set-Location -LiteralPath 'C:\Users\you\Work\Researcher'
```

Then use the command in the selected [native guide](README.md#choose-your-apps). Quote paths containing spaces. Windows Git Bash and WSL need their own path syntax. WSL also has a Linux home, installed tools, and authentication state separate from native Windows.

## Connect MCP dependencies and credentials

Install the dependencies required by the agent's actual MCP definitions. A Python server may need `uvx`; a Node server may need `node` and `npx`. Resolve executable paths in the environment that launches the agent. Preserve package versions from a working definition and verify them against the recipient's runtime.

On macOS and Linux, a desktop launched through Finder or the application menu can have a different PATH from a terminal. Windows desktop processes also retain the environment present at startup. Use the vendor's environment configuration or an actual resolved executable path, then verify discovery from the desktop app itself.

Translate environment references into the client's supported syntax. Authenticate remote MCPs separately for each client when required. For private agent memory or databases, use an agent-owned data path in addition to agent-scoped server configuration.

## Verify permissions on the target OS

Use the selected app's native permission controls and inspect their effective runtime values. Codex's Windows sandbox and its macOS or Linux sandbox have different implementations. Cursor main chat, Cursor subagents, and T3-hosted providers have distinct controls. An MCP's remote mutations require their own policy.

Record OS-specific outcomes in the personal launch guide. A Windows result establishes the exercised Windows route. Documentation review establishes documented macOS and Linux procedures. Actual launches on those systems establish their native behavior.
