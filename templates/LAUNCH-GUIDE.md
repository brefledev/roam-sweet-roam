# Launch {{Display Name}}

Operating system: {{OS and architecture}}
Source: {{existing definition or optional AGENT.md}}
Launch folder or profile: {{actual path or native profile name}}

Replace every placeholder and retain only the user's selected routes.

## Open in your desktop app

1. Open {{app}}.
2. Select {{actual named project, saved folder, or Hermes bot}}.
3. Choose {{agent selection when required}}, {{provider and model}},
   {{effort when supported}}, and {{effective permission mode}}.
4. Start a new chat. It loads {{agent identity and context}}.

Repeat these steps for each installed desktop app. Include initial
add-folder or create-profile steps only when the user still needs them.

## Launch from a terminal

Open {{Terminal, Windows Terminal, or the app's terminal}} using
{{zsh, bash, PowerShell, or the selected shell}}.

Working directory: {{actual folder, or explain the explicit selector}}

```text
{{one actual copyable launch command for this user's OS}}
```

Successful startup shows {{expected identity or profile}}. Include one
command for each installed CLI and its required agent or profile selector.

## Configuration and access

| Route | Native files or profile | Provider, model, effort | Effective access |
|---|---|---|---|
| {{app and desktop/main/subagent/CLI route}} | {{actual paths}} | {{actual selection or inherited default}} | {{file, shell, MCP rules and inherited tools}} |

Required MCPs: {{server names and agent-private data locations}}.
Skills and context: {{installed skills and resolved context}}.
Credentials: {{variable names or native login location, with values omitted}}.

## Installation results

| Selected route and OS | Identity and context | Each required MCP and skill | Permissions | Reopen result |
|---|---|---|---|---|
| {{route}} | {{passed/failed/untested with evidence}} | {{per-capability result}} | {{runtime denial, write, refusal, or untested reason}} | {{observed result or exact remaining step}} |

Incomplete capabilities and next action: {{specific failures, owners,
and shortest resolving steps, or all selected checks passed}}.

## Update

Ask your assistant to update from {{recorded source}} using `SETUP.md`.
Existing native instructions and settings are merged and preserved.
