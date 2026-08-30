# Permanent Source Vault Bootstrap Runbook

**Status:** Active operational runbook for the first user-controlled Source Universe deployment  
**Date:** 2026-08-25  
**Last reviewed:** 2026-08-30  
**Scope:** Deploy the accepted Specification 023 source substrate on durable user-controlled storage and ingest the original VU Amsterdam Machine Learning folder before any additional course corpus is admitted  
**Authority:** Operational guidance subordinate to Foundation 022, Specification 023, and the current checkpoint. This file does not select a permanent cloud provider, backup provider, or final multi-user deployment topology.

## 1. Purpose

Specification 023 has demonstrated that the provider-free source substrate can preserve exact bytes, maintain source identity and encounter provenance, audit integrity, create a verified backup, and restore into a clean target.

The next step is not another architecture experiment.

The next step is to instantiate that accepted mechanism on storage controlled by the user so the educational source corpus no longer depends on ChatGPT uploads or disposable development storage.

The first permanent corpus remains:

```text
VU Amsterdam Machine Learning
collection stable key: vu-amsterdam-machine-learning
canonical locator: https://mlvu.github.io/
```

---

## 2. Four locations must remain conceptually separate

The deployment uses four distinct locations:

```text
ORIGINAL_SOURCE_ROOT
    the user's existing Machine Learning course folder
    read-only intake source

SOURCE_REGISTRY_DATABASE
    the operational SQLite Source Registry

SOURCE_VAULT_ROOT
    the canonical private content-addressed artifact store

INDEPENDENT_BACKUP_ROOT
    a separate recoverable backup destination
```

A fifth disposable location is used for recovery proof:

```text
CLEAN_RESTORE_ROOT
    temporary clean registry + vault used only to prove recovery
```

The original course folder is not modified by ingestion.

The Source Vault must not live inside the public Git repository.

The independent backup should not be merely another folder inside the same canonical vault tree. Its purpose is to provide a separate recovery copy.

---

## 3. Storage policy for the first permanent deployment

Initial deployment remains local-first and provider-neutral.

Requirements:

```text
source registry and vault are user-controlled
source binaries remain private
paths are supplied through configuration / CLI arguments
no private paths are committed to public Git
no source binary is committed to Git
no source is deleted from the original course folder as part of ingestion
backup is verified before it is considered complete
```

Exact private paths and machine-specific measurements are governed by the layered private-state architecture:

```text
public contract
    docs/source_universe/LOCAL_PRIVATE_OPERATIONAL_STATE.md

private companion knowledge repository
    shakaarlatief/autonomous-data-science-system-private
    durable private cross-chat knowledge

machine-local runtime state
    .ads-private/source_vault_bootstrap.json
    execution-ready local configuration
```

The `.ads-private/` directory is ignored by the public repository's Git configuration. A public placeholder template is preserved at:

```text
docs/source_universe/local_private_state.example.json
```

The public repository records whether a private value is resolved and whether the operational gate passed or failed. The private companion preserves the durable exact private complement. The local `.ads-private` state exists for concrete local command execution.

The private companion is not a second ADS development repository and is not Source Vault or secret storage.

A cloud/object-storage provider may be introduced later if measured requirements justify it. The current deployment should not add provider complexity merely for appearance.

---

## 4. Current preflight boundary and preflight before any permanent write

Public-safe current state as of 2026-08-30:

```text
ORIGINAL_SOURCE_ROOT          RESOLVED_PRIVATE
SOURCE_REGISTRY_DATABASE     UNRESOLVED
SOURCE_VAULT_ROOT             UNRESOLVED
INDEPENDENT_BACKUP_ROOT       UNRESOLVED
CLEAN_RESTORE_ROOT            UNRESOLVED
cleanup stage                 COMPLETED
capacity preflight            READY
capacity recheck required     NO
backup topology               UNRESOLVED
permanent write allowed       NO
private companion             OPERATIONAL
```

The formal capacity recheck used the actual original local first-corpus footprint and the current filesystem capacity after cleanup. The exact source path and exact machine-specific measurements are intentionally not reproduced in public Git. They are durably preserved in the private companion through:

```text
source_universe/source_vault_bootstrap.json
source_universe/capacity_recheck_2026-08-30.json
```

The capacity result is `READY`. It was derived from the measured first corpus and the storage required for the canonical vault, registry overhead, an independent backup-sized copy, and a temporary clean restore. No arbitrary free-space threshold was used.

Capacity is therefore no longer the active blocker. The remaining blocker is storage-topology resolution: all four remaining private locations must be selected, and the independent backup must be genuinely separate and verifiable before permanent writes begin.

The fact that the original source location is already resolved is durable project state. Future conversations must not ask the project owner to provide it again merely during reconstruction.

Before ingestion:

```text
1. confirm the exact promoted V1 source code is locally available
2. free sufficient local storage and rerun the capacity measurement                 COMPLETE
3. update or supersede the durable private capacity observation                    COMPLETE
4. choose SOURCE_REGISTRY_DATABASE                                                  NEXT
5. choose SOURCE_VAULT_ROOT
6. choose INDEPENDENT_BACKUP_ROOT
7. choose CLEAN_RESTORE_ROOT
8. materialize or verify .ads-private/source_vault_bootstrap.json for local execution using the resolved private values
9. verify SOURCE_VAULT_ROOT is outside the public Git repository
10. verify the backup root is a genuinely separate destination
11. verify the original source folder is not being used as the vault
12. verify the resolved topology still has sufficient working capacity
```

Do not proceed to any permanent Source Registry or Source Vault write merely because the capacity gate is `READY`. Permanent writes remain forbidden until the remaining private locations are resolved, local execution state is verified, and genuine backup separation is confirmed.

The earlier approximately 490 MB development-batch observation has now served only as historical evidence. The formal capacity gate is based on the actual local first-corpus measurement preserved privately.

---

## 5. Create a clean migrated Source Registry

Specification 023 uses the accepted Alembic migration history.

Conceptual command:

```text
ADS_DATABASE_URL=<sqlite URL for SOURCE_REGISTRY_DATABASE> \
uv run --python 3.13 --locked alembic upgrade head
```

Platform-specific quoting and path syntax should be resolved from the actual selected local path before execution.

Do not create registry tables by hand.

---

## 6. Prospectively compare the original folder before ingestion

Use the reviewed first-corpus manifest:

```text
docs/source_universe/manifests/001_vu_machine_learning.json
```

Command shape:

```text
uv run --python 3.13 --locked python -m ads_system.source_cli compare \
  --manifest docs/source_universe/manifests/001_vu_machine_learning.json \
  --root <ORIGINAL_SOURCE_ROOT> \
  --output <PRIVATE_COMPARISON_REPORT>
```

The report preserves four outcome classes:

```text
MATCH
DIFFERENT_ARTIFACT
MISSING_LOCAL_SOURCE
ADDITIONAL_LOCAL_SOURCE
```

No mismatch should be normalized away automatically.

A local original that differs from the ChatGPT-observed artifact is not inherently an error. It may be a different version or variant and should be preserved explicitly after review.

A source present locally but absent from the 20-file first chat batch is likewise not inherently an error.

---

## 7. Review the comparison before ingestion

The first permanent intake must account for every mismatch class.

Expected review logic:

```text
MATCH
    safe to ingest under the reviewed manifest identity

DIFFERENT_ARTIFACT
    preserve as distinct exact bytes; review logical-source/version relationship

MISSING_LOCAL_SOURCE
    record explicitly; do not fabricate the missing artifact

ADDITIONAL_LOCAL_SOURCE
    review and extend the intake manifest prospectively before ingestion
```

The goal is not to force the local folder to reproduce the ChatGPT batch exactly.

The goal is to preserve the actual local corpus without losing the pre-existing comparison evidence.

---

## 8. Ingest the reviewed local corpus

Command shape:

```text
uv run --python 3.13 --locked python -m ads_system.source_cli ingest \
  --manifest <REVIEWED_MANIFEST> \
  --root <ORIGINAL_SOURCE_ROOT> \
  --database <SOURCE_REGISTRY_DATABASE> \
  --vault <SOURCE_VAULT_ROOT>
```

Expected semantics:

```text
new exact bytes
    -> NEW_ARTIFACT

exact bytes already present
    -> EXACT_DUPLICATE encounter

same filename but different bytes
    -> distinct SourceArtifact

uncertain course membership
    -> uncertainty preserved exactly
```

The original source files remain untouched.

---

## 9. Run the canonical integrity audit

Command shape:

```text
uv run --python 3.13 --locked python -m ads_system.source_cli audit \
  --database <SOURCE_REGISTRY_DATABASE> \
  --vault <SOURCE_VAULT_ROOT>
```

Acceptance requires only clean registered-artifact results and no unexplained orphan object.

Potential failure classes include:

```text
MISSING_OBJECT
SIZE_MISMATCH
DIGEST_MISMATCH
ORPHAN_OBJECT
```

Do not proceed to backup acceptance if the working store is dirty.

---

## 10. Create an independent verified backup

Command shape:

```text
uv run --python 3.13 --locked python -m ads_system.source_cli backup \
  --database <SOURCE_REGISTRY_DATABASE> \
  --vault <SOURCE_VAULT_ROOT> \
  --target <INDEPENDENT_BACKUP_ROOT>
```

The backup contains a deterministic private registry snapshot, exact object payloads, and a backup manifest. Backup creation verifies the copied payload before reporting success.

The backup destination is private and must not be committed to Git.

---

## 11. Prove disaster recovery into a clean target

Create a clean migrated restore registry and an empty restore vault, then run:

```text
uv run --python 3.13 --locked python -m ads_system.source_cli restore \
  --backup <INDEPENDENT_BACKUP_ROOT> \
  --database <CLEAN_RESTORE_DATABASE> \
  --vault <CLEAN_RESTORE_VAULT>
```

Then run the same integrity audit against the restored target.

Recovery proof requires:

```text
registry semantic state reproduced
all restored artifact sizes correct
all restored artifact SHA-256 values correct
no unexplained orphan objects
full restored audit clean
```

The clean restore location may be deleted after safe non-private recovery evidence has been preserved.

---

## 12. What may be preserved in Git after permanent bootstrap

Safe public-repository evidence may include:

```text
checkpoint / deployment classification
counts
non-sensitive mismatch classifications
SHA-256 values already approved as safe metadata
public-safe source metadata
registry snapshot digest
backup manifest digest
software / migration versions
validation outcomes
resolved / unresolved private-location status
capacity gate classification
```

Do not commit to the public repository:

```text
source PDFs/books/slides
private observed paths
exact machine-specific private operational coordinates
private registry snapshot
backup payload
source-vault object bytes
credentials
private notes
```

The private companion repository may preserve exact private knowledge needed for continuity, but it must not become source-binary, backup-payload, database, or credential storage.

---

## 13. Course 2 admission gate

No additional educational course batch should be admitted until the first permanent Machine Learning deployment satisfies:

```text
original local corpus reviewed
all intended files ingested or explicitly accounted for
working integrity audit clean
independent backup verified
clean restore successful
restored integrity audit clean
safe evidence preserved
```

After this gate, course-sized intake can become the normal workflow:

```text
course context
    -> reviewed manifest
    -> compare / intake review
    -> ingest
    -> audit
    -> backup update
    -> safe registry evidence
```

The source corpus can then grow independently of ChatGPT conversation history.

---

## 14. Reopen conditions

Pause and revise the deployment process if the first permanent local exercise exposes any of the following:

```text
unhandled source variant semantics
unacceptable backup topology
path portability defects
registry/vault placement conflicts
source-rights metadata gaps
performance or storage problems
recovery failure
unexplained mismatch with prospectively frozen fingerprints
private information leaking into public-safe outputs
```

Any material architectural change should be preserved prospectively before bulk intake continues.