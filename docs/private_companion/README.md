# Private Companion Knowledge Repository

**Status:** Accepted and operational  
**Last reviewed:** 2026-09-01  
**Scope:** Define the role, authority, content boundary, and continuity contract for the private companion repository used to preserve private ADS knowledge that should survive chat rotation but must not be committed to the public development repository.

## Core authority boundary

The public `autonomous-data-science-system` repository remains the sole ADS project-development repository and the sole authority for:

```text
code / tests / schemas / migrations
architecture / specifications / decisions
foundations / research / checkpoints
public current state and routing
verification / promotion / development history
public-safe Source Universe evidence
```

The private companion repository is a **knowledge-preservation complement only**. It is not a private development fork, not a competing `CURRENT_STATE`, and not an alternate source of implementation truth.

The operational companion repository is:

```text
shakaarlatief/autonomous-data-science-system-private
visibility: private
default branch: main
```

## What belongs where

```text
PUBLIC ADS REPOSITORY
    project-development authority
    public-safe state, evidence, contracts and chronology

PRIVATE COMPANION KNOWLEDGE REPOSITORY
    exact private paths and machine/storage coordinates
    private operational observations
    private source-location mappings
    other durable private continuity knowledge

LOCAL .ads-private STATE
    execution-ready machine-local configuration
    direct runtime inputs

PRIVATE SOURCE VAULT / BACKUP STORAGE
    source binaries
    datasets / PDFs / books / slides
    registry snapshots and backup payloads

SECRET STORAGE
    passwords / API keys / tokens / credentials / encryption secrets
```

The private companion must never be used for ordinary secrets or as bulk source/backup storage merely because it is private.

## Single-owner rule

Each fact should have one primary authority layer.

Example:

```text
public CURRENT_STATE
    ORIGINAL_SOURCE_ROOT = RESOLVED_PRIVATE
    source ingestion = NOT STARTED

private companion
    exact ORIGINAL_SOURCE_ROOT path
    exact private storage topology
```

A private record may reference a public commit, checkpoint, specification, or stable identifier, but it cannot silently redefine public project-development state. If a conflict is discovered, resolve it explicitly and preserve the disposition in the appropriate authority layer.

## Relationship to `.ads-private/`

The Git-ignored local directory:

```text
.ads-private/
```

is machine-local execution configuration. The companion repository instead provides durable private knowledge across chats and machines.

Normal direction:

```text
private companion knowledge
    -> materialize or verify local .ads-private execution state
    -> execute under public ADS contracts
```

Synchronizing a private value into local operational state does not make the companion repository a development repository.

## Current private continuity surface

The primary private routing surface is:

```text
CURRENT_PRIVATE_STATE.md
```

It carries the public-safe synchronization anchor:

```text
Public continuity checkpoint
Public continuity commit
```

and points to the private records relevant to the current ADS boundary.

For Source Vault bootstrap continuity, the current detailed private topology/evidence is routed from `CURRENT_PRIVATE_STATE.md`. Historical or superseded private observations remain provenance and must not override the latest routed private record.

Do not copy volatile Source Vault status into this contract. Live public project state belongs in `docs/CURRENT_STATE.md`; live private routing belongs in the companion `CURRENT_PRIVATE_STATE.md`.

## Cross-chat reconstruction

Repository-first reconstruction remains public-first:

```text
1. reconstruct ADS from the public repository using docs/CONTINUITY.md
2. determine whether the public active state references private knowledge
3. when relevant and accessible, read private CURRENT_PRIVATE_STATE.md
4. follow its routed private records only as a complement
5. use local .ads-private state only when concrete local execution requires it
```

A collaborator must not ask the project owner to repeat a value already marked `RESOLVED_PRIVATE` merely because the public repository intentionally withholds its exact value.

If the companion is inaccessible, preserve `RESOLVED_PRIVATE`; do not silently downgrade it to `UNRESOLVED`.

## Private continuity integrity

When deliberate chat rotation or another continuity transition requires private verification, compare the companion's public continuity anchor against the exact public target.

The governed result is:

```text
PRIVATE_CONTINUITY_INTEGRITY=PASS
PRIVATE_CONTINUITY_INTEGRITY=FAIL
PRIVATE_CONTINUITY_INTEGRITY=NOT_VERIFIED
```

The public checker is:

```text
scripts/check_private_continuity.py
```

`NOT_VERIFIED` means the current surface did not prove private freshness. It is not public repository failure.

## Security boundary

Never store in ordinary Git, public or private:

```text
passwords
API keys
access tokens
private keys
service-account credentials
recovery codes
encryption passwords or keys
```

Do not use the companion for Source Vault object bytes, source binaries, registry databases, backup archives, or other bulk private payloads.

The companion may preserve private paths, remote destination references, non-secret machine observations, and private reports when they are genuinely useful for continuity.

## Bootstrap classification

The private companion bootstrap is complete and operational. Future work should update private knowledge only when the active public ADS boundary creates or changes a private continuity fact.

The repository, not prior chat memory, owns the public/private authority boundary.
