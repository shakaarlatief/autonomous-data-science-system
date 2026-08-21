# V1 Governed Knowledge Roundtrip Result

**Status:** PASS  
**Date:** 2026-08-21  
**Validation workflow:** `V1 governed knowledge roundtrip closure gate`  
**Workflow run:** `32496496812`  
**Validation PR:** `#7`  
**Validation merge ref:** `249428d97e7013caa65981b59fa894874cf3df2e`  
**Permanent migration-fix commit:** `e83ae3bd87bbf8f2ecf383b4fd743798ab7a8ed4`  
**Scope:** Candidate import, explicit acceptance, accepted snapshot export, migration compatibility, relation governance, and historical revision pinning

Validated against the current V1 code on:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

The integration gate validates the following governed persistence/interchange behavior:

```text
IR-01  PASS  migration 0001 relation/current semantics preserved through migration 0002
IR-02  PASS  candidate import is idempotent and does not advance accepted authority
IR-03  PASS  conflicting reuse of a durable revision identity is rejected
IR-04  PASS  explicit acceptance advances accepted-current pointers
IR-05  PASS  accepted snapshot validates, is trusted-only, deterministic, and reloadable
IR-06  PASS  later candidate revision leaves current accepted revision unchanged
IR-07  PASS  explicit R2 acceptance supersedes R1 while project Finding remains pinned to R1
IR-08  PASS  current accepted snapshot exports R2 without pretending to be full history
```

## PostgreSQL portability defects resolved

Two PostgreSQL-specific portability defects were exposed by the governed round-trip gate and corrected before closure.

### 1. Overlong manually named constraint

PostgreSQL limits identifiers to 63 bytes. A manually named migration constraint exceeded that limit. The constraint identifier was shortened without changing its schema semantics.

### 2. Overlong Alembic revision identifier

Alembic's default `alembic_version.version_num` column is `VARCHAR(32)`. The migration revision identifier:

```text
0002_reusable_knowledge_interchange
```

exceeded that limit. SQLite did not expose this because it does not enforce declared `VARCHAR(n)` length in the same way.

The revision identifier was shortened to:

```text
0002_knowledge_interchange
```

while retaining:

```text
down_revision = 0001_v1_persistence_core
```

No migration payload, governance semantics, or application/domain behavior changed as part of that revision-identity fix.

## Validation provenance

The successful gate ran from temporary PR `#7` so the current V1 branch could be validated without prematurely merging the full frontend/V1 branch into `main` and without letting the old status-persistence workflow write misleading state to `main`.

The PR's successful validation merge ref was:

```text
249428d97e7013caa65981b59fa894874cf3df2e
```

The permanent clean branch preserves the same corrected migration blob in:

```text
e83ae3bd87bbf8f2ecf383b4fd743798ab7a8ed4
```

The temporary closure workflow is validation scaffolding only and is not part of the permanent V1 branch.

## Scope boundary

This gate validates the governed persistence/interchange seam. It does **not** validate:

```text
retrieval quality
FTS ranking
embedding quality
semantic retrieval
lexical/semantic fusion
reranking
MethodologicalHorizon construction
selective LLM context quality
external-source ingestion
knowledge authoring UX
complete production provenance ontology
```

The representative reusable-knowledge fixture remains benchmark/test material. The gate converts a copy to a candidate set inside isolated test databases and does not create accepted operational methodological authority in the repository.
