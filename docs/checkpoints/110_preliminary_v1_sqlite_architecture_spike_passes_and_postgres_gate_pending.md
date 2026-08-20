# Checkpoint 110: Preliminary V1 SQLite Architecture Spike Passes and PostgreSQL Gate Pending

**Date:** 2026-08-20  
**Status:** Historical experimental-design checkpoint; preliminary local spike evidence  
**Checkpoint class:** DESIGN  
**Project stage:** V1 technical architecture falsification  
**Scope:** Records the first executable local falsification pass against Specification 001, including one schema defect discovered and repaired during the spike, 11 SQLite-side gate passes, and the remaining PostgreSQL portability execution gate.  
**Authority:** Historical provenance only. Specification 001 remains candidate v0.1 and is not promoted by this checkpoint. The spike harness must be checked into the repository and the PostgreSQL portability gate must still run before architecture acceptance.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## Why this checkpoint exists

Specification 001 deliberately requires implementation evidence before broad V1 coding.

A first local executable spike was therefore built against the proposed SQLite schema and application boundaries.

The result is encouraging, but this checkpoint intentionally does **not** claim the technical architecture is fully accepted yet.

## Environment

The preliminary spike ran in the current development runtime with:

```text
Python 3.13.5
Python sqlite3 binding
SQLite STRICT tables
foreign_keys=ON
WAL mode for the file-backed concurrency test
synchronous=FULL
standard-library online backup API
```

The spike used synthetic but semantically representative fixtures for:

```text
Histogram
Missing Data
Temporal Validation
Random Forest
Prediction-Time Feature Eligibility
Class Imbalance
plus distractor methodological assets
```

The semantic retrieval provider in this architecture-only spike was deliberately a deterministic toy provider. It validates the `SemanticIndex` / hybrid candidate-union boundary and stale-index behavior, **not** production embedding quality.

## Defect found during the spike

The first schema attempt tried to create a SQLite UNIQUE index over a subquery in the index expression to derive `project_id` from the project-entity registry.

SQLite rejected this:

```text
OperationalError: subqueries prohibited in index expressions
```

This was useful falsification evidence rather than a reason to weaken integrity.

The schema was corrected by making `project_id` explicit in the Definition subtype table and enforcing:

```text
FOREIGN KEY(definition_id, project_id)
    -> prj_entity(entity_id, project_id)

UNIQUE(project_id, key)
```

This is cleaner relationally, easier to query, and more portable to PostgreSQL than the attempted expression-index shortcut.

The corrected design therefore strengthens the specification's preference for explicit queryable relational semantics over clever engine-specific shortcuts.

## Additional schema hardening during the spike

The spike also strengthened relation-current-revision integrity by requiring the stable relation/current-revision pointer to reference a revision belonging to the same relation through a composite foreign key.

Derived lexical-index refresh was changed away from SQLite `INSERT OR REPLACE` style semantics toward explicit delete/insert behavior inside the index adapter, consistent with Specification 001's rule that SQLite-specific replacement semantics must not leak into authoritative domain behavior.

## Gate results

The current local results are:

```text
FT-01  PASS  identity/revision historical integrity
FT-02  PASS  component/relation integrity + bounded traversal
FT-03  PASS  Missing Data TRUE/FALSE/UNKNOWN rule reconstruction
FT-04  PASS  criterion-Finding chain + exact knowledge revision pin
FT-05  PASS* retrieval/horizon architecture fixture
FT-06  PASS  missing/stale embedding detection + fallback/rebuild
FT-07  PASS  context-budget enforcement
FT-08  PASS  transaction failure injection / atomic rollback
FT-09  PASS  WAL reader + controlled writer behavior
FT-10  PASS  online backup / restore / integrity / FK checks
FT-11  PASS  deletion and rebuild of derived search/embedding state
FT-12  NOT RUN YET  executable PostgreSQL portability gate
```

`FT-05 PASS*` means the architecture path and bounded candidate-union semantics passed with the deterministic toy semantic provider. It must not be interpreted as validation of a production embedding model, reranker, or retrieval-quality target. Retrieval-model quality remains a separate empirical selection task.

## Important behaviors demonstrated

### Historical knowledge pinning

A project Question was linked to Missing Data revision R1. After publishing R2:

```text
current asset pointer -> R2
historical project reference -> R1
R1 semantic content hash unchanged
```

This is the central revision-history behavior the architecture must preserve.

### Conditional rule behavior

A Missing Data rule depending on whether missing feature values occur in production produced:

```text
missing Definition -> UNKNOWN -> OPEN_QUESTION consequence
Definition = true -> TRUE -> recommendation consequence
Definition = false -> FALSE -> no consequence
```

A hard training-information safeguard with missing required context produced:

```text
UNKNOWN -> BLOCK_DEPENDENT
```

No rule directly executed a project action.

### Criterion Finding

Prediction-Time Feature Eligibility was represented using:

```text
Question
    -> Evidence
    -> Finding
        criterion revision = exact feature-eligibility knowledge revision
        verdict = INELIGIBLE
    -> Decision
```

No new universal Assessment object was required.

### Derived index failure behavior

Deleting embedding rows produced an explicit missing-index health state while lexical retrieval continued to find the relevant asset.

Rebuilding derived embeddings restored health without changing authoritative knowledge.

Deleting both FTS/search documents and embeddings left authoritative knowledge unchanged and both derived layers could be rebuilt.

### Transaction failure injection

A deliberate exception between revision insertion and current-pointer publication rolled back the entire write unit.

The spike observed:

```text
no partial revision
no moved current pointer
no FK damage
```

### WAL concurrency

A reader held a read transaction while a controlled writer acquired a write transaction and rolled it back successfully. The reader did not fail and the writer did not require waiting for the reader to finish.

This supports the selected initial reader/writer envelope. It does not simulate high-concurrency production workloads.

### Backup/restore

The standard SQLite online backup API produced a restorable snapshot that passed:

```text
PRAGMA integrity_check
PRAGMA foreign_key_check
historical knowledge presence checks
```

## PostgreSQL portability status

An executable PostgreSQL test did not run locally because the current runtime contains neither Docker nor a PostgreSQL server/client.

The planned portability test should therefore run through a small GitHub Actions job using a temporary PostgreSQL service.

It should validate the core migration seam, not attempt to deploy the whole future backend.

Minimum executable checks:

```text
UUID domain IDs -> PostgreSQL UUID
UTC timestamp semantics -> timestamptz
validated JSON payload -> JSONB
asset/current-revision composite FK
project -> exact knowledge-revision FK
relation source/target indexes
stored rule JSON and exact revision ownership
transactional insert/update of representative fixtures
```

## Reproducibility status

The local spike logic has been developed and executed, but the polished reusable harness is not yet committed in this checkpoint.

Before this evidence is used to promote Specification 001, the harness must be checked into:

```text
experiments/architecture_spikes/
```

and the SQLite portion should be rerun from the repository version.

The PostgreSQL CI portability job should then run against that committed contract.

## Promotion audit

### Promote Specification 001?

**No.**

Eleven SQLite-side architecture gates are promising, but the reproducible harness and executable PostgreSQL portability gate remain incomplete.

### Add a principle or decision?

**No.**

D-028 remains the accepted architecture-family decision. The current evidence tests the implementation contract beneath it.

### Update current state?

**Yes.**

The exact next work is now narrower than "begin the architecture spike": preserve the executable harness, rerun it from the repository, and complete FT-12 in CI.

## Exact next step

1. check the architecture falsification harness into `experiments/architecture_spikes/`;
2. rerun the SQLite gates from that committed harness;
3. add a temporary PostgreSQL CI/service portability test;
4. inspect the resulting evidence;
5. only then decide whether Specification 001 can be promoted from candidate v0.1 to the accepted V1 technical contract.