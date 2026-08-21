# V1 Governed Knowledge Roundtrip Result

**Status:** PASS  
**Date:** 2026-08-21  
**Validation workflow:** `V1 governed knowledge roundtrip closure gate`  
**Final workflow run:** `32496856945`  
**Validation PR:** `#7`  
**Validated source commit:** `5e04f399153a9a05cdd436cbd62097d000b89044`  
**Permanent clean migration-fix commit:** `e83ae3bd87bbf8f2ecf383b4fd743798ab7a8ed4`  
**Permanent portability-guard commit:** `a3f5caad4ed7cf6dc2997f6fc94fad2aab147bd2`  
**Scope:** Candidate import, explicit acceptance, accepted snapshot export, migration compatibility, relation governance, historical revision pinning, and Alembic revision-ID portability

Validated against the current V1 code on:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

The final gate also ran the deterministic migration revision-identifier portability guard on all three jobs and passed.

The governed persistence/interchange integration gate validates:

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

Two PostgreSQL-specific portability defects were exposed and corrected before closure.

### 1. Overlong manually named constraint

PostgreSQL limits identifiers to 63 bytes. A manually named migration constraint exceeded that limit. The constraint identifier was shortened without changing schema semantics.

### 2. Overlong Alembic revision identifier

Alembic's default `alembic_version.version_num` column is `VARCHAR(32)`. The migration revision identifier:

```text
0002_reusable_knowledge_interchange
```

exceeded that limit. SQLite did not expose the problem because it does not enforce declared `VARCHAR(n)` length in the same way.

The revision identifier was shortened to:

```text
0002_knowledge_interchange
```

while retaining:

```text
down_revision = 0001_v1_persistence_core
```

No migration payload, governance semantics, or application/domain behavior changed as part of that revision-identity fix.

## Portability regression guard

The second defect exposed a cheap deterministic invariant that should remain enforced independently of PostgreSQL execution:

```text
every Alembic revision identifier
    -> unique
    -> length <= 32 characters
```

`tests/test_migration_revision_ids.py` parses the migration files and enforces both properties against Alembic's default version-table envelope. The final closure gate ran this test together with the governed round-trip on Ubuntu/SQLite, Windows/SQLite, and PostgreSQL 18.

## Validation provenance

The final successful gate ran from temporary PR `#7` so the current V1 branch could be validated without prematurely merging the full active V1/frontend branch into `main` and without letting the legacy main-only status-persistence workflow write misleading project state.

Final validation source:

```text
commit  5e04f399153a9a05cdd436cbd62097d000b89044
run     32496856945
result  success
```

The permanent clean finalization branch preserves the substantive fixes and regression guard while excluding the temporary closure workflow itself.

The earlier failed validation remains useful evidence. It demonstrated that the first PostgreSQL constraint-name repair was insufficient and exposed the separate Alembic `VARCHAR(32)` revision-value limit.

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
