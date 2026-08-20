# Checkpoint 111: V1 Technical Architecture Gate Passed and Specification 001 Promoted

**Date:** 2026-08-20  
**Status:** Historical architecture-validation and promotion checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** V1 technical architecture validation and implementation-boundary transition  
**Scope:** Records the reproducible FT-01 through FT-12 gate result, promotion of Specification 001 to accepted V1 technical contract, and the transition from architecture validation to bounded implementation/tooling design.  
**Authority:** Historical provenance. Specification 001 v1.0 governs the accepted V1 technical architecture for its declared scope; D-028 governs the V1 architecture-family decision.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## Validation completed

The committed V1 architecture falsification workflow has now produced a persistent PASS result:

```text
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
```

Results:

```text
FT-01  PASS
FT-02  PASS
FT-03  PASS
FT-04  PASS
FT-05  PASS_ARCHITECTURE_ONLY
FT-06  PASS
FT-07  PASS
FT-08  PASS
FT-09  PASS
FT-10  PASS
FT-11  PASS
FT-12  PASS
```

The SQLite-side tests executed against the committed schema/harness. FT-12 executed against a PostgreSQL 18 service in GitHub Actions.

## What the gate actually establishes

The gate gives direct evidence that the proposed technical seams can support:

```text
stable global knowledge identity
immutable/recoverable knowledge revisions
historical project pinning to an exact old revision
component/relation foreign-key integrity
bounded relation traversal
TRUE/FALSE/UNKNOWN rule evaluation
Missing Data branch reconstruction without hidden action execution
criterion-Finding compatibility with Foundation 018
explicit missing/stale semantic-index behavior
bounded context assembly
atomic semantic write units
WAL reader + controlled writer behavior
online backup/restore/integrity
rebuildable derived indexes
PostgreSQL mapping of core durable semantics
```

FT-12 is especially important for the project's anti-regret objective. Representative durable identities, revisions, component relationships, rule JSON, relation semantics, timestamps, and project-to-knowledge references mapped to PostgreSQL without redesigning their meaning.

This does not prove that a future infrastructure migration will be cost-free. It does show that the migration seam is real rather than merely claimed in prose.

## What the gate does not establish

`FT-05` intentionally used a deterministic toy semantic provider.

Therefore this gate does **not** establish:

```text
which embedding model should be used
production semantic-retrieval recall
lexical/semantic fusion quality
reranker quality
final methodological-horizon ranking quality
LLM provider/model quality
frontend/backend framework suitability
```

Those are separate empirical questions.

The architecture deliberately makes those layers replaceable so a failure there does not imply a database rewrite.

## Defect-driven correction retained

The preliminary spike discovered that an attempted SQLite subquery-based expression index could not represent the desired project-scoped uniqueness rule.

The corrected design carries `project_id` explicitly in the relevant subtype and uses ordinary composite foreign keys and a UNIQUE constraint.

This correction was promoted into Specification 001 because it improves all three properties simultaneously:

```text
clarity
referential integrity
PostgreSQL portability
```

The relation current-revision invariant was also strengthened through a composite foreign key, and derived-index refresh avoids relying on SQLite REPLACE semantics as domain behavior.

## Specification promotion

`docs/specifications/001_v1_sqlite_technical_architecture.md` is now:

```text
Accepted V1 technical specification v1.0
```

The accepted contract includes:

```text
SQLite as an adapter behind domain/application persistence ports
application-generated UUID durable identities, UUIDv7 preferred
UTC domain timestamps
STRICT authoritative tables where practical
relational core + bounded validated JSON
immutable accepted knowledge revisions
separate mutable governance state/history
explicit project-type lifecycles
exact project -> knowledge revision references
minimal declarative rules, no executable stored code
FTS5 as rebuildable lexical state
SemanticIndex / EmbeddingProvider abstraction
HorizonBuilder and ContextAssembler application services
one application-owned write path
short transactions
foreign_keys=ON / WAL / synchronous=FULL baseline
ordered migrations
online backup + integrity verification
human-readable deterministic knowledge export
explicit PostgreSQL portability rules
```

## Anti-regret interpretation

The project should not interpret "professional architecture" as "never change infrastructure."

The stronger goal is:

> foreseeable changes in infrastructure should occur behind stable semantic and application boundaries rather than forcing a redesign of the methodological brain.

Examples:

```text
semantic retrieval underperforms
    -> change embedding/fusion/reranking provider

SQLite becomes write-contention bottleneck
    -> move persistence adapter/schema to PostgreSQL

relation traversal becomes genuinely graph-dominant
    -> add or migrate RelationQuery projection/provider
```

None of those should require changing what a KnowledgeAsset, Finding, Question, rule, or methodological horizon means.

A full architecture reconsideration is warranted only if evidence shows the semantic/domain boundaries themselves are wrong.

## Promotion audit

### Specification 001

**Promoted.** Candidate v0.1 -> accepted V1 technical specification v1.0.

### New project decision

**Not necessary.** D-028 already accepts the SQLite-centered V1 architecture family. Specification 001 now provides the validated current technical contract beneath that accepted decision.

### New principle

**Not necessary yet.** The portability/adapter discipline is enforced by Specification 001. It can be elevated to a global principle if later subsystems demonstrate that the pattern generalizes beyond this V1 persistence/retrieval boundary.

### Routing/current state

**Update warranted.** Future sessions should read Specification 001 and this checkpoint before changing V1 persistence/retrieval architecture.

## Exact next step

Architecture-family selection and architecture-seam validation are now complete.

The next task is **bounded V1 implementation-contract and tooling design**, not broad product construction.

Determine, with the same evidence discipline:

```text
SQL access / repository implementation approach
schema migration implementation approach
production migration/DDL organization
typed domain/repository interfaces
transaction/UnitOfWork implementation
UUIDv7 implementation choice
canonical export/import representation
first real retrieval-quality benchmark before embedding-model selection
PostgreSQL portability tests retained in CI
```

Then implement the first bounded persistence/retrieval subsystem behind the accepted ports.