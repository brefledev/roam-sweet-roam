# Native verification

This guide draws on existing native agent deployments, current vendor documentation, and later disposable fixture checks. Each record establishes its own operating system, app version, agent configuration, and launch method. The installing assistant verifies the recipient's selected routes.

## Existing deployment evidence

Historical deployment records were recovered during the November 17 repair. Their generic mechanisms now inform the setup guides. Detailed source paths and session receipts remain in the private project report.

| Route | Recorded evidence | Scope |
|---|---|---|
| Codex desktop, Windows, October 9 | Three user-launched primary-agent chats opened existing agent folders and loaded their canonical instructions. Runtime model, effort, and access selections were inspected. | Establishes the folder-as-primary-project mechanism. The observed chats used Full Access; their intended restricted profiles retained separate failures. |
| Claude Code, Windows, October 9 | Existing agent folders imported canonical role/context files and selected native primary-agent settings. CLI checks verified identity, loaded hooks, and specific tool restrictions. | The dated report records an initial Desktop worktree-selection failure and leaves corrected GUI acceptance pending. |
| Hermes, Windows, October 9 | Native profile creation, separate runtime home, canonical identity loading, model/effort readback, local skill operations, MCP calls, and a pinned Bot Chat were recorded. | Establishes the native-profile and named-bot mechanism for that deployment. Current installations resolve their own profile names and paths. |

The repository owner's supplied screenshots and current report show existing named desktop-agent entries and everyday use. Those observations supplement the dated records. Full current permission and tool parity across every route requires its own evidence.

## Disposable fixture checks

Checks ran on Windows 11 in November 2026 using a fictional research agent. These results describe those fixture versions and launch methods. The fixture's failures retain their actual scope alongside the established deployments above.

| App | Tested version | Observed result | Remaining gaps |
|---|---|---|---|
| Claude Code | 2.1.326 | Headless identity, instructions, skill use, four MCP calls, and restricted native tools passed. A memory read-tool allowlist removed mutation tools. | Interactive trust flow, desktop, restart, and extra context files. |
| Codex | 0.169.0 | CLI identity, instructions, context, and skill checks passed. An independent Windows sandbox denied a file write; an unrestricted control succeeded. | Live MCP startup failed. MCP write filtering and desktop checks remain untested. |
| Cursor | Desktop 3.30.14 detected | Folder files were installed. A separate T3 SDK run loaded instructions and skills. | Standalone CLI absent. A local hook timeout blocked remaining native checks. Desktop and native subagent enforcement remain untested. |
| Grok Build | 1.0.88 | Named-agent identity, source precedence, skill inlining, fetch/time connection, time call, and native edit/shell denials passed. | Memory and sequential-thinking startup failed. MCP mutation filtering, upstream schema parity, and edit/full mappings remain untested. |
| Hermes | 0.23.1 | Skill reads and selected dispatcher denials passed in an isolated profile. | Live chat startup and four MCP connections failed. Live-session enforcement and desktop remain untested. |
| T3 Code | 0.1.10 | Project binding and four provider checks ran. Full-access Codex, Cursor, and Grok threads wrote disposable files. Claude loaded restricted native tools and a skill. | Provider-specific MCP loading gaps, main-agent selection for Grok, GUI, restart, and complete read-only enforcement. |

## What the checks establish

Configuration discovery, tool availability, successful invocation, instruction refusal, and runtime denial are separate observations. The setup guides preserve those distinctions.

Filesystem sandbox settings require their own checks. MCP servers can expose state-changing tools independently of filesystem controls. A read-only installation enables read tools through supported controls and leaves unsupported capabilities disabled.

T3 launches require their own verification. In the tested Full-access sessions, folder-level Codex and Cursor settings failed to prevent native writes. Approval prompts also require the user's judgment; they provide a different control from a read-only tool policy.

## macOS and Linux coverage

The [platform guide](PLATFORMS.md) and native pages include macOS and Linux installation sources, configuration-home resolution, terminal launches, desktop setup, and platform limits. Those procedures were reviewed against current primary documentation. Native macOS and Linux execution remains unverified in this project. Windows fixture results establish the listed Windows behavior.

Required capability failures remain incomplete installation outcomes. Disabling a failed MCP preserves a restricted configuration and leaves that MCP requirement open. Static syntax and link checks establish document structure. Historical receipts, current source review, and live execution retain separate statuses.

## Fresh installer check

A fresh assistant generated renamed `sample-agent` installations for Claude Code and Codex from the fictional example. Names, native files, and skill references passed static checks. Codex recognized the disabled project MCP entries; Claude's diagnostic command recognized its configuration.

The isolated configuration homes had fresh authentication state. The single Codex identity attempt returned HTTP 401; Claude returned "Not logged in." Live identity, skill use, MCP calls, and mutation denial remain untested in this fresh run. MCP servers stayed disabled. These outcomes supplement the earlier native checks above.

Existing settings, trust entries, and credentials remained unchanged. A shared Claude feature/usage cache refresh had uncertain ownership and was preserved. Test output and isolated homes remained in the approved test directory.

## Test cleanup

Test profiles, temporary trust entries, and authentication copies were removed or restored according to the native workers' receipts. Shared application caches were preserved. A Cursor test database remained locked by the active T3 desktop process; scoped disposal requires that application to release it. Detailed machine paths and raw test traces remain in local audit material outside the published files.
