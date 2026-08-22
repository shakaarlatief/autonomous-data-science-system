# Checkpoint 127: Governed Knowledge Roundtrip Closed Across SQLite and PostgreSQL

**Date:** 2026-08-21  
**Status:** Historical verification and implementation-closure record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Closes the richer governed reusable-knowledge persistence/interchange round-trip after successful validation on SQLite/Linux, SQLite/Windows, and PostgreSQL 18, including a new deterministic Alembic revision-ID portability guard.  
**Authority:** Historical verification provenance. `experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md` records the final gate result; Specification 002 v1.1 carries the promoted tooling portability invariant; current canonical routing documents govern current priorities.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this checkpoint exists

The V1 reusable-knowledge subsystem already had two earlier validated layers:

```text
Checkpoint 114
    first production persistence vertical slice
    SQLite/Linux PASS
    SQLite/Windows PASS
    PostgreSQL 18 PASS

Checkpoint 115
    reusable-knowledge interchange contract
    KI-01 through KI-10 PASS
    Linux/Windows
    Python 3.12 through 3.14
```

A later, richer governed round-trip added behavior that was not covered by those earlier gates:

```text
candidate import
explicit acceptance
accepted-current pointers
accepted snapshot export
provenance
relation governance
collections
migration 0002
historical project revision pinning across later knowledge acceptance
```

That richer gate passed SQLite but remained failed on PostgreSQL 18. It therefore could not honestly be called closed.

Checkpoint 127 records the successful closure after fresh validation against the current V1 branch.

---

## 2. Final validation result

Final validation workflow:

```text
V1 governed knowledge roundtrip closure gate
```

Final run:

```text
32496856945
```

Validated source commit on the temporary closure branch:

```text
5e04f399153a9a05cdd436cbd62097d000b89044
```

Result:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

The same jobs also ran the deterministic Alembic migration revision-ID portability guard and passed.

Final authoritative result artifact:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
```

---

## 3. Governed behavior validated

The integration gate validates:

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

The fixture remains benchmark/test material. The gate does not promote the fixture into accepted operational methodological knowledge.

---

## 4. PostgreSQL portability defects discovered and resolved

The closure process exposed two independent portability defects.

### 4.1 Overlong manually named constraint

The first known failure came from a manually named migration constraint whose identifier exceeded PostgreSQL's 63-byte identifier limit.

Resolution:

```text
shorten the constraint identifier
preserve the same schema semantics
```

This repair was necessary but not sufficient.

### 4.2 Overlong Alembic revision identifier

A fresh PostgreSQL 18 closure run then failed after the migration body itself had executed, when Alembic attempted to record the migration revision in its version table.

The failing value was:

```text
0002_reusable_knowledge_interchange
```

Alembic's default version table uses:

```text
alembic_version.version_num VARCHAR(32)
```

PostgreSQL therefore raised a string truncation/data error. SQLite had not exposed the defect because declared `VARCHAR(n)` length is not enforced equivalently there.

Resolution:

```text
revision = "0002_knowledge_interchange"
down_revision = "0001_v1_persistence_core"
```

The migration filename remains descriptive. Only the Alembic revision identity was shortened.

No migration payload, governed-knowledge semantics, domain behavior, or application behavior changed.

Permanent clean migration-fix commit:

```text
e83ae3bd87bbf8f2ecf383b4fd743798ab7a8ed4
```

---

## 5. New deterministic portability guard

The second defect exposed a simple invariant that should not require another PostgreSQL-only failure to rediscover.

The repository now includes:

```text
tests/test_migration_revision_ids.py
```

It enforces:

```text
every Alembic revision identifier is unique
every Alembic revision identifier length <= 32 characters
```

This is intentionally a small deterministic regression guard. It does not introduce a new persistence abstraction or migration framework.

Permanent portability-guard commit:

```text
a3f5caad4ed7cf6dc2997f6fc94fad2aab147bd2
```

The final gate ran this guard together with the governed round-trip on all three validation jobs.

The durable tooling requirement has also been promoted into:

```text
docs/specifications/002_v1_persistence_tooling_standard.md
    Accepted V1 technical specification v1.1
```

Specification 002 now requires unique Alembic revision identifiers that fit the configured version-table envelope and explicitly records the current default `VARCHAR(32)` constraint, while also preserving PostgreSQL's identifier-length portability requirement for manually named schema objects.

---

## 6. Validation-branch strategy and cleanup

The active V1/frontend branch is substantially ahead of `main`.

The pre-existing governed-roundtrip workflow was oriented around `main` and persisted its status there. Running that workflow unchanged would not have been an honest validation of the current V1 branch and could have written misleading current-state evidence to the wrong branch.

A temporary validation branch and PR were therefore used:

```text
branch  v1-knowledge-roundtrip-closure
PR      #7
```

The temporary PR workflow tested the current V1 content without changing ADS domain/application semantics.

The permanent finalization branch intentionally keeps only:

```text
real migration portability fix
final PASS/result artifacts
removal of temporary PostgreSQL diagnostic workflow
Alembic revision-ID regression guard
Specification 002 v1.1 portability amendment
closure checkpoint and routing reconciliation
```

The temporary closure workflow is validation scaffolding and is not part of the permanent active branch.

The old dedicated PostgreSQL diagnostic workflow was removed after closure because its diagnostic purpose is complete.

---

## 7. What this checkpoint closes

The following implementation gate is now closed:

```text
governed reusable-knowledge persistence/interchange round-trip
    SQLite / Linux
    SQLite / Windows
    PostgreSQL 18
```

Q-048 can therefore move from active implementation gate to answered/closed historical implementation question.

This closes the richer governed seam that had remained open after Checkpoints 114 and 115.

---

## 8. What this checkpoint does not establish

Do not infer from this PASS that the following have been validated or selected:

```text
production lexical retrieval quality
FTS ranking quality
semantic retrieval quality
embedding model/provider
lexical/semantic fusion
reranker
ANN/vector service
MethodologicalHorizon construction quality
selective LLM context quality
external-source ingestion workflow
knowledge authoring UX
complete provenance ontology
complete Foundation 018 production schema
agent runtime
```

The persistence/interchange seam is stable enough to stop competing with those next evaluation tracks, but it does not answer them.

---

## 9. Promotion and reconciliation audit

### Promote / reconcile

Required current-layer updates:

```text
V1_KNOWLEDGE_ROUNDTRIP_STATUS
    FAIL -> PASS with final run provenance

V1_KNOWLEDGE_ROUNDTRIP_RESULT
    final cross-backend evidence and portability analysis

Specification 002
    v1.0 -> v1.1
    promote Alembic revision-ID and PostgreSQL identifier portability invariants

CURRENT_STATE
    remove PostgreSQL closure as active blocker
    advance to Checkpoint 127

KNOWLEDGE_MAP
    route governed round-trip as closed evidence

OPEN_QUESTIONS
    mark Q-048 answered/closed
    remove Q-048 from highest-value active execution questions

README
    remove stale statement that governed round-trip remains open

MAJOR_CHANGES
    record governed persistence/interchange portability closure
```

### No new project-level decision required

The closure validates implementation of already accepted D-028 through D-031 and strengthens the technical tooling contract under D-029. It does not introduce a new architectural choice that warrants another D-series decision.

### No new foundation required

The portability defects are implementation constraints rather than new methodological architecture.

---

## 10. Exact continuation after closure

With the governed persistence/interchange seam closed, the next active bounded V1 tracks are:

```text
A. Specification 005 agent-runtime bakeoff
    begin with one principal reasoner
    preserve direct model calls as a valid outcome

B. Retrieval / MethodologicalHorizon benchmark
    build retrieval-quality fixtures
    implement/evaluate production lexical retrieval
    evaluate semantic retrieval candidates empirically
    evaluate fusion only if justified
    measure omission/relevance/context cost
    construct the first real bounded MethodologicalHorizon

C. Future Project Cockpit capability/product work
    build on promoted Specification 008
    do not reopen basic interaction architecture without new evidence
```

Runtime bakeoff and retrieval/horizon work are now the highest-value unresolved implementation/evaluation tracks. The exact ordering between them may be chosen based on dependency and evaluation efficiency rather than by treating either as an already accepted architecture.
