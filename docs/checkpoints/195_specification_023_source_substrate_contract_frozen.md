# Checkpoint 195: Specification 023 Source Substrate Contract Frozen

**Date:** 2026-08-25  
**Status:** Prospective provider-free source-substrate implementation contract frozen before implementation  
**Checkpoint class:** Specification freeze / implementation boundary  
**Project stage:** V1 methodological knowledge-universe construction, source-universe prerequisite  
**Scope:** Minimal Source Registry, content-addressed SourceArtifactStore, deterministic registry export, integrity audit, backup/restore, and first VU Machine Learning corpus acceptance gates  
**Authority:** Historical freeze record for Specification 023. Specification 023 is the authoritative contract for its declared implementation scope.  
**Design session:** 06  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 06 - Methodological Knowledge Universe Construction

## 1. Frozen contract

Specification 023 is now frozen prospectively before implementation:

```text
docs/specifications/023_v1_source_universe_substrate.md
```

The implementation target is deliberately bounded and provider-free.

---

## 2. Exact implementation seam

The first source path is frozen as:

```text
filesystem source input
    -> stage + SHA-256 + byte count
    -> immutable local content-addressed SourceArtifactStore
    -> relational Source Registry transaction
    -> deterministic registry export
    -> integrity audit
    -> provider-neutral backup package
    -> clean restore
    -> restored integrity audit
```

No LLM/provider call is part of source-integrity correctness.

---

## 3. Frozen minimum domain identities

Specification 023 freezes V1.0 implementation requirements for:

```text
SourceRecord
SourceArtifact
SourceCollection
SourceCollectionMembership
SourceLocator
SourceIngestionEvent
DerivedSourceArtifact
```

This does not claim that these are the final complete source ontology.

---

## 4. Exact-artifact contract

Frozen:

```text
SHA-256 over exact unmodified source bytes
lowercase hexadecimal digest
content-addressed local storage
```

Frozen object layout:

```text
<root>/objects/sha256/<first-two-hex>/<remaining-62-hex>
```

The source-store root is configuration outside the public Git repository and is not domain identity.

---

## 5. Exact duplicate and variant boundary

Frozen duplicate behavior:

```text
same exact bytes
    -> one SourceArtifact row
    -> one stored object
    -> multiple SourceIngestionEvent rows allowed/required
```

Frozen variant behavior:

```text
different exact bytes
    -> distinct SourceArtifact records
```

No automatic semantic merge is permitted in normal ingestion.

The first chat-intake snapshot already provides real evidence for both cases:

```text
14 renamed uploads are exact byte duplicates of earlier uploads

book-v1.2.0-cropped.pdf
unraveling-pca.pdf
    are byte-distinct apparent variants of related PCA material
```

---

## 6. Rights/access minimum

Frozen conservative defaults for user-supplied educational material:

```text
access_class           PRIVATE_USER_SUPPLIED
redistribution_status UNKNOWN
metadata_visibility   PRIVATE unless explicitly marked public-safe
```

File possession or public course affiliation does not imply redistribution permission.

---

## 7. Public repository boundary

Specification 023 forbids current VU Machine Learning source binaries from entering Git during the source-substrate implementation/acceptance slice.

Git may later contain deterministic public-safe source catalog metadata, schemas, code, tests, and history.

Private observed paths and source-store internal paths are excluded from public-safe export.

---

## 8. Deterministic export boundary

Two export profiles are frozen:

```text
PRIVATE_SNAPSHOT
PUBLIC_SAFE_CATALOG
```

The private snapshot supports trusted restore/bootstrap and excludes source bytes.

The public-safe catalog excludes private metadata/locators and is the only source-registry export profile considered suitable for possible Git preservation.

---

## 9. Backup/recovery boundary

A source store is not accepted merely because local ingestion works.

Specification 023 requires:

```text
clean integrity audit before backup
verified object copy
registry snapshot digest
backup manifest
clean-target restore
full restored integrity audit
```

Backup provider selection remains deferred.

The first implementation may validate against a second filesystem destination so that recovery semantics are tested before cloud-provider complexity is introduced.

---

## 10. First corpus freeze

The first real corpus is:

```text
VU Amsterdam Machine Learning
collection stable key: vu-amsterdam-machine-learning
canonical locator: https://mlvu.github.io/
```

The current chat-observed batch contains 20 exact files and is fingerprinted in:

```text
docs/source_universe/intake_snapshots/001_vu_machine_learning_chat_intake.md
```

That file remains diagnostic historical evidence, not source authority.

---

## 11. Frozen hard gates

Specification 023 freezes:

```text
SU-G01 through SU-G23
```

covering schema/migration, persistence, exact-byte preservation, duplicate behavior, variants, uncertain collection membership, deterministic private/public export, integrity audit, backup/restore, derived-artifact lineage, VU corpus intake, cross-platform behavior, and inherited regressions.

No gate is to be weakened after observing first-corpus behavior without a prospective specification revision.

---

## 12. Frozen advancement outcomes

The real-corpus stage must classify as exactly one of:

```text
SOURCE_SUBSTRATE_ACCEPTED
SOURCE_SUBSTRATE_NEEDS_REVISION
SOURCE_SUBSTRATE_FAILED
```

`NEEDS_REVISION` exists so a methodologically sound but representation-insufficient substrate is not mislabeled as accepted or failed.

---

## 13. D-015 remains active until demonstrated acceptance

The source architecture is now conceptually and prospectively specified, but no accepted source store exists yet.

Therefore:

```text
D-015 remains operationally active
```

until the provider-free implementation and first-corpus recovery gates succeed.

Only a later acceptance checkpoint should supersede D-015 in scope.

---

## 14. Promotion audit

### Specification promotion

Specification 023 is the promoted frozen implementation contract for this bounded slice.

### Foundation promotion

Foundation 021 remains the conceptual source/evidence authority above the specification.

### Decision promotion

No new explicit project decision is added yet because D-015 should not be superseded before operational validation.

### Current-state/routing promotion

Canonical routing should be reconciled to this active source-substrate branch after the frozen contract head passes repository validation.

---

## 15. Exact continuation point

Next:

> **Implement Specification 023 provider-free, validate SU-G01 through SU-G23 on Ubuntu and Windows, then ingest the locally available VU Amsterdam Machine Learning folder as the first real corpus and execute a clean backup/restore before any additional course batch is admitted.**

No additional educational course upload is required before that acceptance boundary.
