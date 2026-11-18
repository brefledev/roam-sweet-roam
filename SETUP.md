# Set up the user's chosen agents

You are the installing assistant. Produce native desktop entries or profiles, the requested CLI launch paths, and a short personal `LAUNCH.md`. Read [platform preparation](PLATFORMS.md) and the relevant [native guides](README.md#choose-your-apps).

## 1. Inventory before asking the user to choose

Use the user's supplied locations and choices. Discover installed apps, operating system, architecture, shell, and actual configuration homes. Inspect their native agent directories, existing agent project folders, and Hermes profile list. Each native guide identifies those locations. Read definition metadata first. Keep credentials and unrelated personal files outside the inventory.

Show one compact inventory with agent name, source path, native format, role, access rules, declared MCPs, skills, context, and existing launch methods. Identify duplicate names and competing definitions. Mark uncertain matches for the user to resolve. An empty native directory establishes that directory's contents; ask for custom locations when discovery leaves a gap.

Then ask which agents or subagents to add to which destinations. Offer desktop and CLI separately for each app. Include Hermes profiles and Cursor's main chat or named subagent as distinct choices. Retain choices already supplied. Help define a new agent when requested.

## 2. Choose native locations and preserve the source

Reuse each selected agent's working folder or profile where appropriate. Follow the vendor's native configuration locations. For a new desktop launch folder, choose a location consistent with the user's existing agent or project organization and confirm it in the installation plan. This repository prescribes no universal launch-folder root.

Keep the existing native definition as the source when it already expresses the agent. The optional [portable format](SPEC.md) can collect a new or shared definition. Creating that format is optional. Record which source owns future updates and which native files are generated copies.

Retain instructions, imports, exact permission rules, MCP definitions, skills, context dependencies, provider, model, and effort selections. A broad label such as `read-only` supplements the original rules. Resolve machine-specific paths against the recipient's environment. Copy redistributable context when sharing. Preserve intentional references to existing local context during an installation on the same machine.

Show the agent-by-destination plan: source, desktop project or profile, CLI availability, native files, dependencies, account or subscription route, and requested access. Explain user-level configuration changes. Proceed within the user's existing authorization and resolve substantive choices before the corresponding writes.

## 3. Configure each selected destination natively

Back up existing files before changing them. Merge settings and imports, preserve unrelated instructions, and keep other agents' configuration intact. Have each selected app or CLI perform its supported setup and diagnostics when available.

For each folder-based main agent, connect its instructions through the app's native entrypoint. Codex uses `AGENTS.md`; Claude uses `CLAUDE.md`, which can import an existing `AGENTS.md`. Preserve the full existing contents of either file. Add an import once. Cursor and Grok use the entrypoints described in their guides. A named child-agent definition and a main desktop chat require their own configuration and checks.

For Hermes, create or reuse the selected native profile, apply its identity and settings, and add its desktop Bot Mode presentation when requested. A profile-only installation can keep its launch guide alongside the source definition. Create extra project folders when the user chooses a project workflow.

Configure each declared MCP in the narrowest supported agent, project, or profile scope. Inspect the effective catalog, including inherited global tools. Agent-private servers and backing data require agent-owned configuration and data paths. Authenticate through each client's supported flow. Translate environment references into native syntax and keep secret values in supported credential storage.

Apply exact file, shell, and MCP rules independently. Check host permission modes and inherited policy. A host's Full Access setting can override project intentions. When a selected route cannot enforce a required restriction, explain the specific mismatch and offer the supported alternatives. Record the route as incomplete until the user chooses an acceptable effective policy. An omitted required MCP or an unavailable skill remains an incomplete capability.

Use the selected app's available model list and account. Preserve explicit provider, model, and effort choices. Cursor model names and usage come from Cursor's plan; a direct Grok login is a separate route. T3's selected provider has its own mode and authentication. Resolve unavailable choices with the user before substitution.

## 4. Verify the actual launch routes

Use existing setup receipts as historical evidence, with their dates and scope. Run the changed installation through the selected native app or CLI. Record the operating system, app version, configuration source, provider, model, effort, and effective permission mode.

For every chosen desktop route, add or open its actual project folder or profile, give it the agent's display name, and start a main chat or explicitly selected subagent. Read back the identity, loaded context, declared skills, and effective tool catalog. Reopen that named entry to establish the repeatable launch flow. The guide names the saved entry and exact selection steps.

For every chosen CLI route, run the actual executable from the configured folder or with the explicit profile or agent selector. Repeat the identity, context, skill, and MCP checks. A T3 SDK run proves its own route. A CLI run proves that CLI route.

Invoke one harmless operation from every required MCP. For restricted agents, test disposable file writes, state-changing shell operations, and MCP mutations separately within an agreed test scope. Inspect actual tool results. Record runtime denials and instruction refusals separately. Preserve application-maintained session and cache behavior as a separate observation.

Record each result as passed, failed with its error, or untested with its reason. An existing successful desktop setup remains historical evidence when a later fixture run lacks GUI access. Fresh authentication failures describe that test environment. Native macOS and Linux execution require their own receipts.

Clean up owned disposable artifacts and restore temporary configuration after verification. Preserve shared application processes and other sessions' state. Name any cleanup that needs the app to release a file.

## 5. Deliver the personal launch guide

Write `LAUNCH.md` from [the template](templates/LAUNCH-GUIDE.md), alongside the agent source or in its chosen launch folder. Start with the user's actual desktop clicks and copyable CLI commands for their OS. Include their configured provider, model, effort, permissions, native paths, and update source. Keep verification detail below the launch steps.

Show a completion row for every selected agent and launch route. List required capabilities that failed or remain untested. A partial route stays partial. Give the user a direct link to their launch guide and the shortest supported next action for each incomplete route.

## Update or share

Update from the recorded source, merge into the existing native installation, and repeat the affected checks. A recipient uses their own locations, credentials, installed versions, and app selections. Cloud execution and synchronized configuration management remain optional future work.
