# Checkpoint 109: V1 Technical Architecture Specified and Falsification Gate Defined

**Date:** 2026-08-20  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 technical architecture specification  
**Scope:** Records the first migration-safe technical specification for the accepted SQLite-centered V1 architecture and defines the narrow falsification gate required before broad implementation.  
**Authority:** Historical provenance. Specification 001 is the active technical contract for the architecture spike; D-028 and Foundations 017-020 remain authoritative for accepted architectural/conceptual scope.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## What changed

The architecture-family decision in Checkpoint 108 selected SQLite for V1, but that alone did not guarantee a professional implementation.

A new specification now defines how to use SQLite without embedding avoidable SQLite-specific assumptions throughout the system:

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
```

The specification is deliberately marked candidate v0.1 and frozen for a narrow architecture falsification spike rather than being treated as proven merely because it is detailed.

## Central anti-regret objective

The implementation should be simple enough for V1 while preserving bounded migration seams for future needs.

The design explicitly aims for:

```text
SQLite -> PostgreSQL
exact semantic search -> pgvector/ANN/dedicated provider
bounded relational traversal -> specialized graph projection if later justified
```

without rewriting:

```text
methodological knowledge semantics
project object meaning
rule semantics
methodological-horizon logic
context-assembly logic
human-facing workflow concepts
```

This is not a promise that no future infrastructure change will ever occur. It is a requirement that expected infrastructure evolution be localized rather than architectural rework.

## Important technical directions in Specification 001

The candidate specification now establishes for the spike:

```text
one SQLite operational database for knowledge + project metadata/state
logical table prefixes: sys_ / kg_ / prj_ / exec_ / idx_
domain/application persistence ports around SQLite
application-generated UUID durable identities, UUIDv7 preferred
UTC timestamp semantics independent of SQLite date functions
STRICT authoritative SQLite tables where practical
relational structure for important identities/relationships/history
bounded, validated JSON for flexible role-specific payloads
immutable accepted knowledge content revisions
separate governance state/history from immutable revision content
technical kg_node identity supertype for Asset/Component relation FKs
typed project-state lifecycles rather than one universal project JSON/revision model
exact project references to knowledge revisions
minimal declarative rule AST with TRUE/FALSE/UNKNOWN
no raw SQL or executable code in stored methodological rules
FTS5 as rebuildable lexical state
semantic vectors as rebuildable derived cache behind SemanticIndex
HorizonBuilder and ContextAssembler as application services
one application-owned write path
short transactions with no LLM/network work inside them
foreign_keys=ON on every SQLite connection
WAL mode
synchronous=FULL as the default V1 durability profile
ordered schema migrations
online backup / verified restore
human-readable deterministic knowledge export
explicit PostgreSQL portability contract
```

## Why the project-state schema is not one generic table

A major design risk was implementation convenience overriding the semantic distinctions established in Foundation 018.

The specification explicitly rejects forcing all project objects into one generic JSON document or one universal revision lifecycle.

Examples remain lifecycle-specific:

```text
Definition
    semantic revisions

Question
    open/resolved/deferred lifecycle

Evidence
    normally immutable

Finding
    immutable assertion + supersession/challenge

Decision
    decision revisions/history

Run
    immutable config + mutable execution status + run events
```

A lightweight technical identity registry may still provide common FK targets without claiming identical object semantics.

## Why knowledge governance is separated from revision content

Accepted knowledge content should be historically immutable.

But governance state can change:

```text
candidate -> reviewed -> accepted -> superseded
```

Therefore the candidate architecture separates:

```text
immutable content revision
        !=
current governance state
        !=
append-only governance transition history
```

This avoids mutating the very revision that historical project reasoning is supposed to pin.

## Why no external rule engine is needed

The stored rule form remains intentionally small:

```text
Predicate(name, arguments)
ALL
ANY
NOT
TRUE / FALSE / UNKNOWN
force
unknown behavior
consequence category
```

Predicates are registered application semantics querying project state through typed interfaces.

Rules contain no SQL, Python, shell, JavaScript, or general eval code.

This preserves portability, auditability, and the hybrid LLM + explicit-constraint architecture.

## Why the search/index boundary remains replaceable

Lexical and semantic indexes are derived state.

The authoritative knowledge model does not depend on:

```text
FTS5 ranking semantics
one embedding model
one vector serialization
one nearest-neighbor implementation
```

This enables later retrieval upgrades without database-semantic migration.

## Current technical research incorporated

Current official SQLite documentation confirms the technical basis used by the specification:

```text
STRICT tables for stronger typing
foreign-key enforcement requiring explicit enablement per connection
WAL reader/writer behavior
FTS5 full-text search
online backup / VACUUM INTO backup options
integrity_check / foreign_key_check
PRAGMA optimize guidance
```

PostgreSQL 18 natively supports RFC 9562 UUID values and UUIDv7 generation, strengthening the UUID portability path.

These sources informed implementation details; they do not change the repository authority hierarchy.

## Falsification gate

Specification 001 defines twelve tests that must be addressed before broad implementation:

```text
FT-01 identity/revision historical integrity
FT-02 component/relation integrity
FT-03 Missing Data conditional-rule reconstruction
FT-04 criterion-Finding chain
FT-05 retrieval/horizon coverage fixture
FT-06 missing/stale embedding behavior
FT-07 context-budget enforcement
FT-08 transaction atomicity/failure injection
FT-09 WAL reader/writer behavior
FT-10 backup/restore/integrity
FT-11 derived-index rebuild
FT-12 PostgreSQL portability review/spike
```

The spike should use representative current methodological examples rather than toy database rows only.

## Promotion audit

### Promote to current technical specification?

**Not yet.**

Specification 001 is intentionally candidate v0.1 until the architecture spike tests the design.

### New principle?

**Not yet.**

The migration-safe implementation directions are strong but should first survive the technical gate.

### New project decision?

**No additional architecture-family decision.**

D-028 already selects SQLite-centered V1. The current work specifies how to implement that decision safely.

### Knowledge-map/current-state update?

**Yes.**

Future sessions should route to Specification 001 and this checkpoint before implementing V1 persistence/retrieval.

## Exact next step

Implement the narrow V1 architecture falsification spike.

Do not build the frontend or broad autonomous workflow yet.

The first implementation work should exist specifically to answer:

> Does this technical design preserve the promoted semantics, historical integrity, retrieval/context boundaries, operational reliability, and PostgreSQL migration seam under representative workloads?

Only after that gate should the technical specification be promoted and broader V1 subsystem implementation begin.