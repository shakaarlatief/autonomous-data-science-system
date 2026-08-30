# Local Private Operational State

**Status:** Accepted Source Universe operational-state contract  
**Date:** 2026-08-30  
**Scope:** Preserve machine-specific and private operational coordinates needed to execute the permanent Source Vault bootstrap without leaking them into the public repository or forcing future conversations to ask the project owner for already-resolved information again.

## Purpose

The public repository is the authority for project state, architecture, accepted decisions, blockers and public-safe evidence. Some execution facts cannot safely live in a public repository, including exact local filesystem paths and other machine-specific coordinates.

Those two needs must not be collapsed.

The Source Vault bootstrap therefore uses a two-layer operational-state model:

```text
PUBLIC REPOSITORY STATE
    what is resolved or unresolved
    what gate passed or failed
    what action is next
    public-safe evidence and rationale

LOCAL PRIVATE OPERATIONAL STATE
    exact local paths
    exact machine/storage measurements when useful
    other machine-specific values required for execution
```

A value being private does not make it unknown to the project.

## Canonical local file

For the current local-first bootstrap, the canonical machine-local state file is:

```text
.ads-private/source_vault_bootstrap.json
```

The entire `.ads-private/` directory is ignored by Git.

A public template is preserved at:

```text
docs/source_universe/local_private_state.example.json
```

The private file is operational input, not a replacement for `CURRENT_STATE.md`, specifications, checkpoints or accepted public evidence.

## Public status vocabulary

Public repository state may use the following statuses without exposing the underlying value:

```text
RESOLVED_PRIVATE
    the project owner has already supplied or confirmed the value
    the exact value is intentionally withheld from public Git

UNRESOLVED
    the value has not yet been chosen or confirmed

FAILED_INSUFFICIENT_FREE_SPACE
    a capacity preflight has already established that cleanup or another
    storage decision is required before execution can continue

RECHECK_REQUIRED
    a prior measurement is no longer sufficient and must be measured again

READY
    the relevant operational prerequisite has been verified
```

Future collaborators must distinguish `RESOLVED_PRIVATE` from `UNRESOLVED`.

## Continuity rule

If `CURRENT_STATE.md` records a value as `RESOLVED_PRIVATE`, a new conversation must not ask the project owner to supply that value again merely during reconstruction.

Instead:

```text
reconstruction surface can access local private state
    -> read the exact value from the private state before execution

reconstruction surface cannot access local private state
    -> preserve the fact that the value is already resolved
    -> do not downgrade it to UNRESOLVED
    -> request or hand off the exact value only when a concrete local
       execution step actually requires it and no local execution surface
       can retrieve it
```

This avoids confusing "not visible to this chat" with "not known to the project".

## Current Source Vault fields

The local state file may contain:

```text
ORIGINAL_SOURCE_ROOT
SOURCE_REGISTRY_DATABASE
SOURCE_VAULT_ROOT
INDEPENDENT_BACKUP_ROOT
CLEAN_RESTORE_ROOT
capacity observations used for the current preflight
```

It must not be used to store source binaries, credentials, registry snapshots or backup payloads.

## Capacity observations

Capacity measurements are operational observations, not timeless facts. Record enough information locally to understand the last preflight, but the public repository should preserve the durable conclusion rather than unnecessary machine detail.

For example:

```text
local private state
    exact volume / bytes / percentages / timestamp

public repository
    capacity preflight failed
    cleanup required
    recheck required before permanent write
```

After cleanup, the local measurement should be refreshed and the public status should be updated if the gate changes.

## Portability and loss

The local private file is deliberately not synchronized through public Git. Losing that file does not invalidate repository knowledge or Source Universe architecture, but it can require re-resolving machine-specific coordinates.

Once the permanent Source Vault exists, private operational state should be included in an appropriate user-controlled private backup strategy if losing those coordinates would create unnecessary recovery work. It should never be added to the public repository merely for convenience.

## Safety boundary

Never commit:

```text
exact private filesystem paths
private credentials or tokens
private registry/database contents
source binaries
backup payloads
other private machine notes not required as public evidence
```

Public Git may safely preserve that a private value is resolved, that a gate failed or passed, and what the next action is.
