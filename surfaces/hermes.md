# Hermes in a named profile

Use the existing Hermes profile for an established agent. Create a profile for a new agent, then select that same profile from the CLI or desktop.

## Check the runtime and its home

Follow the current [installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation) and [platform support matrix](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/platform-support.md). Native Windows and POSIX CLI installs have different launchers and data homes. Released desktop bundles target Apple Silicon macOS and Windows. Intel Macs can use the CLI and `hermes desktop`; Linux desktop packaging currently requires the documented local-build route. [verified — official platform guide]

Run `hermes --version`, `hermes profile list`, and `hermes profile show <name>`. Inspect `HERMES_HOME` and the selected gateway. Existing profile IDs can differ from an agent's display name or portable name. Preserve the actual native ID. [verified — [profiles](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md)]

| Purpose | Default location |
|---|---|
| Native Windows data root | `%LOCALAPPDATA%\hermes\` |
| macOS/Linux/WSL data root | `~/.hermes/` |
| Named profile | `<resolved data root>/profiles/<native-id>/` |
| Profile identity, settings, and skills | `<profile>/SOUL.md`, `config.yaml`, `skills/<skill>/SKILL.md` |
| Existing source and context | The user's chosen source folder or native profile |

`HERMES_HOME` can select a custom home or a profile home directly. Resolve the effective profile from native command output before editing it. The profile home and tool working directory are separate choices. [verified — [profile homes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md), [Windows paths](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/windows-native.md)]

## Configure the selected agent

1. Follow [SETUP.md](../SETUP.md). For a new profile, inspect `hermes profile create --help`, then use `hermes profile create <name> --no-alias --no-skills` when those flags are supported. Inspect its reported location. Current creation inherits model/credentials by default and offers `--no-credentials`. Choose the intended account arrangement explicitly. [verified — [profile creation](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md)]
2. Put the role body in the profile's `SOUL.md`, or preserve its existing canonical-file read instructions. Add explicit resolved context reads to the profile instructions. Keep the source and context at their existing or chosen location. Add project `AGENTS.md` only for a selected project-folder workflow.
3. Preserve the existing provider, model, and effort. Apply a requested change through `hermes model` or **Settings > Model** for the selected profile. CLI/Desktop session selections can differ from the saved profile default. Read back both. [verified — [configuration](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/configuration.md), [desktop model settings](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/desktop.md)]
4. Copy declared skills into `<profile>/skills/`. Keep existing profile-only skills. Review `skills.external_dirs`, project discovery, and startup loading so inherited skills match the requested setup. [verified — [skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)]
5. Merge declared servers into the profile's `config.yaml`:

```yaml
mcp_servers:
  fetch:
    command: uvx
    args: ["mcp-server-fetch"]
```

Resolve each executable in the runtime's environment. Keep credentials in Hermes's supported secret configuration. Set `terminal.cwd` to the chosen launch folder when that profile needs a persistent working directory. Check each connection with `hermes -p <native-id> mcp test <server>`, followed by a harmless tool call in the selected agent. [verified — [MCP](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/mcp.md)]

Hermes profiles supply whole-agent identity and state. Its delegation tools have their own runtime configuration. Record the chosen profile separately from any delegated-agent role. [verified — [profiles](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md)]

## Apply the requested access

Hermes toolsets can contain reads and writes together. For example, `file` includes mutation tools and `skills` includes skill management. A strict read-only setup needs explicit tool restrictions, MCP read-tool filtering, and checks for every enabled channel. A reviewed fail-closed `pre_tool_call` hook provided selected dispatcher denials in the November fixture. Its live-session startup failed, so that evidence covers the tested dispatcher path. [verified — [security](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/security.md), [hooks](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/hooks.md), [fixture results](../VERIFICATION.md)]

Use installed-version controls and a tested backend boundary for edit/full access. Headless `-z` bypasses approval prompts. Hermes session/log/cache persistence continues in ordinary use. Filter mutating MCP tools independently, using the connected catalog's real tool names. [verified — [MCP filtering reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/mcp-config-reference.md), [security](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/security.md)]

## Open and reopen the desktop profile

Use the same syntax in PowerShell or a POSIX shell, with that OS's real paths:

```sh
hermes -p <native-id> desktop --cwd "<folder>"
```

In Desktop, select the intended gateway, then the agent's profile in the profile rail or **Profiles** control. Open a new chat and inspect its working directory, model, effort, and tools. For later use, select that same gateway/profile and reopen its chat or start a new one. A Bot Mode entry uses the underlying profile and its own persistent Bot Chat. Preserve an existing working Bot/profile setup. [verified — [desktop](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/desktop.md), [profiles and Bot Mode](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md)]

## Launch in a terminal

These commands share syntax across PowerShell and POSIX shells:

```sh
hermes -p <native-id> --in "<folder>" chat
hermes -p <native-id> --in "<folder>" -z "Name and role?"
```

Check `--in` and `-z` in the installed help. Use the second command only with the intended headless permissions. Resolve custom homes and shell paths through [PLATFORMS.md](../PLATFORMS.md). Write the native profile ID and real launch commands in `LAUNCH.md`.

## Record the result

Follow [the verification steps](../SETUP.md#4-verify-the-actual-launch-routes). Historical native profile/Desktop/Bot acceptance and November isolated-fixture failures are distinct evidence in [VERIFICATION.md](../VERIFICATION.md). The later fixture passed skill reads and selected dispatcher denials, while live chat and MCP startup failed. Preserve established working profiles and record any new installation's actual result. [verified — repository verification record]
