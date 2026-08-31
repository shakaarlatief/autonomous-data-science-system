# Local Private Operational State

**Status:** Accepted Source Universe operational-state contract  
**Date:** 2026-08-30  
**Last reviewed:** 2026-08-31  
**Scope:** Preserve machine-specific and private operational coordinates needed to execute the permanent Source Vault bootstrap without leaking them into the public repository or forcing future conversations to ask the project owner for already-resolved information again.

## Purpose

The public repository is the authority for project state, architecture, accepted decisions, blockers and public-safe evidence. Some execution facts cannot safely live in a public repository, including exact local filesystem paths and other machine-specific coordinates.

Those two needs must not be collapsed.

The Source Vault bootstrap therefore uses a layered operational-state model:

```text
PUBLIC ADS REPOSITORY
    sole project-development repository
    what is resolved or unresolved
    what gate passed or failed
    what action is next
    public-safe evidence and rationale

PRIVATE COMPANION KNOWLEDGE REPOSITORY
    durable private knowledge used for continuity across chats
    exact private paths and observations where appropriate
    no ADS product development

LOCAL PRIVATE OPERATIONAL STATE
    execution-ready exact local paths
    exact machine/storage measurements when useful
    remote-backup destination references and transport metadata
    other machine-specific values required for local execution
```

A value being private does not make it unknown to the project.

The governing public-side companion-repository contract is:

```text
docs/private_companion/README.md
```

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

The private file is operational input, not a replacement for `CURRENT_STATE.md`, specifications, checkpoints, accepted public evidence, or the private companion knowledge repository.

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
private companion repository is accessible
    -> retrieve the durable private value there when relevant

local execution surface can access .ads-private state
    -> read the execution-ready local value there

current surface can access neither private layer
    -> preserve the fact that the value is already resolved
    -> do not downgrade it to UNRESOLVED
    -> request or hand off the exact value only when a concrete execution
       step actually requires it and no accessible private layer can supply it
```

This avoids confusing "not visible to this chat" with "not known to the project".

## Current Source Vault fields

The local state file may contain:

```text
ORIGINAL_SOURCE_ROOT
SOURCE_REGISTRY_DATABASE
SOURCE_VAULT_ROOT
BACKUP_STAGING_ROOT
INDEPENDENT_BACKUP_ROOT
INDEPENDENT_BACKUP_TRANSPORT
CLEAN_RESTORE_ROOT
capacity observations used for the current preflight
```

`BACKUP_STAGING_ROOT` is a local temporary surface where ADS may create and verify its canonical backup bundle. When it resides on the same physical device as the canonical vault, it must never be counted as the independent backup.

`INDEPENDENT_BACKUP_ROOT` may identify a genuinely separate remote destination. `INDEPENDENT_BACKUP_TRANSPORT` may record non-secret provider/transport metadata such as provider class, destination reference, whether client-side encryption is required, and the selected encryption tool.

The local state file must not contain passwords, encryption keys, OAuth credentials, access tokens, recovery secrets, source binaries, registry snapshots, or backup payloads. A field such as `credentials_stored_here` should remain false and exists to make that boundary explicit.

## Capacity observations

Capacity measurements are operational observations, not timeless facts. Record enough information locally to understand the last preflight, but the public repository should preserve the durable conclusion rather than unnecessary machine detail.

For example:

```text
private companion / local private state
    exact volume / displayed capacity values / percentages / timestamp

public repository
    capacity preflight failed or passed
    cleanup / recheck status
    next operational boundary
```

After cleanup, the local measurement should be refreshed and the public status should be updated if the gate changes. The durable private companion observation should also be updated or superseded so future chats can recover the latest private state without relying on transient conversation memory.

## Relationship to the private companion repository

The two private layers have different jobs:

```text
private companion repository
    durable private knowledge
    cross-chat reconstruction
    private continuity/provenance

.ads-private/
    machine-local execution configuration
    direct command/runtime input
```

The companion repository must not become a second ADS development repository. Code, tests, architecture, specifications, decisions, checkpoints, and implementation history remain in the public `autonomous-data-science-system` repository.

Where useful, a local `.ads-private` file may be initialized or refreshed from the corresponding private companion knowledge. This is synchronization of operational values, not cross-repository development.

## Portability and loss

The local private file is deliberately not synchronized through public Git. Losing that file does not invalidate repository knowledge or Source Universe architecture, but it can require reconstructing machine-local execution coordinates.

Important private continuity facts should have a durable private copy in the private companion so loss of one machine-local file does not force the project owner to repeat already-known information.

Once the permanent Source Vault exists, private operational state should also be included in an appropriate user-controlled private backup strategy if losing those coordinates would create unnecessary recovery work. It should never be added to the public repository merely for convenience.

## Safety boundary

Never commit to the public repository:

```text
exact private filesystem paths
private remote destination coordinates when they are not public-safe
private credentials or tokens
encryption passwords or keys
private registry/database contents
source binaries
backup payloads
other private machine notes not required as public evidence
```

The private companion repository may store private knowledge such as exact paths, remote destination references, and observations, but it must still not store ordinary secrets or act as bulk binary/source storage.

Public Git may safely preserve that a private value is resolved, that a gate failed or passed, what class of independent backup is selected, and what the next action is.
