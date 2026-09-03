# Checkpoint 278: Flexible Multi-Repository Authority and Authenticated Private Git Qualified

**Date:** 2026-09-03
**Status:** ACCEPTED INFRASTRUCTURE / RESEARCH 116 CORE CLOSED
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Codex/Codexless upstream research with stable multi-repository local authority qualified
**Scope:** Preserves the live 51-tool flexible workspace-authority surface, explicit admission of the private local-runtime repository, reviewed runtime-repository bootstrap, private-network Git transport correction, and end-to-end authenticated-private semantic Git qualification.
**Authority:** Historical infrastructure/continuity checkpoint. Research 116 is accepted for its core multi-repository authority scope; Research 113 remains the broader active upstream-research program.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-16`
**Conversation title:** `16 - Codex Live Task Viewer Publication and Source Vault Continuation`
**Primary collaborator:** ChatGPT
**Branch:** `v1-source-vault-bootstrap-resume`

## Stable live surface

Codexless `0.1.1-preview.8` now exposes 51 MCP tools. Fresh disposable-chat discovery qualified `codex.workspace_authority` and the generalized semantic Git schemas while preserving Call Profile, Rich Card/handoff, Browser, and model-free project actions.

Workspace authority is no longer coupled to per-repository MCP schema publication. Registered roots can be explicitly added, updated, or removed with optimistic revision/hash protection. Supported workspace capabilities remain server-defined.

## Runtime workspace admission

The private runtime repository is admitted as:

```text
workspaceId     ads-local-runtime
root            C:\Projects_Data\autonomous-data-science-system-local-runtime
allowed remote  origin
integrity       runtime-private-bootstrap
browser         not granted
```

Registry state after admission:

```text
revision     2
contentHash  588cd49a5f4cc57386781b2c5432996df9ba391d711e551df453570078f8e2d8
```

Codex trust and Codexless registry admission were both independently verified.

## Reviewed private runtime repository bootstrap

The first import selected 173 reviewed non-secret `.ads-private/codexless` files. Two transient backup files and `.ads-private/source_vault_bootstrap.json` were excluded. The completed 176-file private worktree passed the deterministic secret-like path/content scan with zero flagged files.

The root commit is:

```text
0ce61ba794929ee71c555d480a936fdced28ef2e
Bootstrap reviewed local runtime evidence
```

The one-time host bootstrap push created `origin/main`, after which local `HEAD` and `origin/main` were equal at that commit.

## Private authenticated Git transport correction

The first generalized private push localized an authentication boundary: Codex App Server `command/exec` could not use the user's Windows Git credential-manager/askpass state for a private HTTPS remote. No push occurred.

The candidate was corrected without changing MCP input schemas. Network Git operations now use the already-bounded internal host-process substrate while workspace selection, branch/upstream derivation, integrity policy, ancestry checks, commit staging, and postconditions remain server-owned and fail-closed.

The published live `semantic-git.mjs` hash is:

```text
F9B65E6245BEB903AFE9805EB9091DCED907CAC5BC49FCB9E41EC299CAFEC96F
```

## Decisive authenticated-private qualification

After restart and tunnel readiness, generalized private fetch succeeded:

```text
codex.git_fetch_origin(workspaceId=ads-local-runtime)
exitCode=0
hostProcess=true
branch=main
upstream=origin/main
```

The subsequent semantic push against the already-equal branch returned up to date and proved:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
retried=false
headBefore=0ce61ba794929ee71c555d480a936fdced28ef2e
remoteTrackingHeadBefore=0ce61ba794929ee71c555d480a936fdced28ef2e
headAfter=0ce61ba794929ee71c555d480a936fdced28ef2e
remoteTrackingHeadAfter=0ce61ba794929ee71c555d480a936fdced28ef2e
trackedWorkingTreeCleanAfter=true
remoteRefreshAfterExitCode=0
postflightOk=true
```

This closes the core Research 116 question for ordinary filesystem/project workspaces and both public and authenticated-private Git repositories.

## Scope boundary

The accepted architecture is flexible for registered filesystem/project roots and the supported capability set. It is not yet a universal arbitrary-host authority system. Codexless self-maintenance, process lifecycle, Windows services/registry, credential stores, and similar host capabilities remain separate future authority classes if deliberately pursued.

Validation 035 remains open: ChatGPT autonomous supervision/wakeup after its response ends and cooperative active-turn writer transfer are still unresolved architecture questions.

## Exact continuation

```text
1. synchronize corrected `.ads-private` runtime implementation into the private local-runtime repository through normal semantic commit/push
2. publish this Research 116/Checkpoint 278 public preservation through bounded semantic commit/push
3. update MC-0010 to route Claude to both public ADS and private runtime evidence
4. rotate deliberately to chatgpt-17 with the stable 51-tool schema
5. resume broader Research 113 upstream ecosystem research
6. keep Validation 035 supervision/writer-transfer research open
7. resume Source Vault only after deliberate closure of the broader Level-2 research route
```
