# Checkpoint 112: V1 Persistence Tooling Selected and Validated

**Date:** 2026-08-20  
**Status:** Historical design and tooling-selection checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 technical architecture; persistence implementation tooling selection  
**Scope:** Compares raw DBAPI, SQLAlchemy Core, and SQLAlchemy ORM approaches; records current official-tooling research and a dual-backend spike; selects SQLAlchemy Core + Alembic for V1 persistence implementation.  
**Authority:** Historical rationale and evidence. D-029 and Specification 002 are the current accepted sources for this tooling scope.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Why this checkpoint exists

Specification 001 intentionally left the SQL toolkit and migration framework unselected until the accepted architecture had survived its own falsification gate.

The next question was therefore narrower than database selection:

> **What persistence implementation tooling gives the accepted SQLite-centered architecture the strongest combination of explicit relational control, professional migration discipline, PostgreSQL portability, and low accidental complexity?**

The serious candidates were:

```text
A. raw DBAPI/sqlite3 + hand-written SQL + hand migration machinery
B. SQLAlchemy Core + Alembic
C. SQLAlchemy ORM + Alembic
```

The goal was not to choose the most feature-rich library. It was to choose the implementation style that best preserves Specification 001's already-accepted architectural boundaries.

---

## 2. Current external research

Research used current official documentation as of 2026-08-20.

### SQLAlchemy Core

SQLAlchemy's documentation describes Core as the schema-centric layer providing SQL rendering, DBAPI integration, transaction integration, schema description, custom types, engine/connection management, events, and multiple database dialects.

Relevant current facts:

```text
SQLAlchemy 2.0.52 is in the stable 2.0 line.
SQLAlchemy 2.1.0b3 is still a beta release.
SQLite and PostgreSQL are built-in dialects.
SQLite STRICT tables are supported through sqlite_strict=True.
SQLite foreign-key PRAGMAs can be installed through connection events.
TypeDecorator can select different physical types by dialect.
conditional/custom DDL is supported.
```

Official references used during the review:

```text
https://docs.sqlalchemy.org/en/20/core/
https://docs.sqlalchemy.org/en/20/intro.html
https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
https://docs.sqlalchemy.org/en/20/dialects/postgresql.html
https://docs.sqlalchemy.org/en/20/core/custom_types.html
https://docs.sqlalchemy.org/en/20/core/ddl.html
https://docs.sqlalchemy.org/en/21/
```

### Alembic

Alembic is the SQLAlchemy migration tool.

Important current behavior:

```text
SQLite structural migrations can use batch move-and-copy operations.
constraint naming is important because unnamed SQLite constraints are hard to target.
batch autogenerate can be enabled with render_as_batch.
autogenerate is explicitly not guaranteed to be perfect and requires review.
named CHECK constraints can be preserved through batch migrations.
```

Official references:

```text
https://alembic.sqlalchemy.org/en/latest/
https://alembic.sqlalchemy.org/en/latest/batch.html
https://alembic.sqlalchemy.org/en/latest/autogenerate.html
https://alembic.sqlalchemy.org/en/latest/ops.html
```

### Python sqlite3 / raw DBAPI

Python's `sqlite3` module is a capable DB-API 2.0 SQLite interface and explicitly supports SQLite's lightweight embedded-database use case.

The issue for this project is not capability. It is whether raw driver usage should become the primary application persistence abstraction when PostgreSQL portability, schema metadata, migrations, named constraints, custom type mapping, and dialect isolation are already requirements.

---

## 3. Candidate A: raw DBAPI + hand migrations

### Strengths

```text
minimal external dependency surface
maximum direct SQLite control
simple for small isolated queries
no ORM/session semantics
```

### Why it loses

The accepted architecture already requires capabilities that raw DBAPI would force the project to reimplement or manually coordinate:

```text
portable SQLite/PostgreSQL DDL/query differences
custom UUID physical mapping
schema metadata and inspection
constraint naming
transaction boilerplate
migration ordering/history
SQLite batch-recreate migrations
PostgreSQL driver substitution
query construction and parameterization discipline
```

The application would effectively build a partial custom database toolkit around the ports.

### Result

```text
NOT SELECTED AS PRIMARY V1 PERSISTENCE STYLE
```

Direct driver SQL remains legitimate inside a narrow adapter when the capability is intentionally backend-specific.

---

## 4. Candidate B: SQLAlchemy Core + Alembic

### Fit with Specification 001

```text
schema-centric rather than domain-object-centric
explicit relational metadata
explicit transaction boundaries
SQLite + PostgreSQL dialect abstraction
custom type adaptation
constraint naming
conditional DDL
migration tooling designed for SQLite batch operations
no requirement to make persisted rows the domain object model
```

This directly preserves:

```text
domain/application semantics
        -> persistence ports
        -> SQLAlchemy Core adapter
        -> SQLite now / PostgreSQL later
```

### Result

```text
SELECTED
```

---

## 5. Candidate C: SQLAlchemy ORM + Alembic

### Strengths

```text
mature mapping system
identity map / Session
relationship management
object-oriented persistence
unit-of-work automation
same underlying Core/dialect ecosystem
```

### Why it does not win as the primary V1 model

The project's domain already has explicit, non-uniform lifecycle semantics:

```text
immutable accepted knowledge revisions
append-only evidence/findings in many cases
type-specific project-object lifecycles
current state != event history
explicit application UnitOfWork boundaries
exact historical knowledge-revision pinning
```

Using ORM-mapped objects as the central domain representation would introduce another state/identity/lifecycle abstraction where the project currently benefits from keeping persistence representation explicit and subordinate.

The ORM could be used later inside a bounded subsystem if it clearly reduces complexity, but it must not redefine the domain model or leak beyond the accepted persistence ports.

### Result

```text
NOT SELECTED AS PRIMARY V1 DOMAIN/PERSISTENCE MODEL
NOT PERMANENTLY PROHIBITED
```

---

## 6. Targeted dual-backend spike

The leading candidate was tested rather than accepted from documentation alone.

Artifacts:

```text
experiments/architecture_spikes/tooling_sqlalchemy_core_alembic_spike.py
.github/workflows/v1-persistence-tooling-spike.yml
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
```

The workflow installed:

```text
Python 3.13
SQLAlchemy 2.0.52
Alembic 1.19.0
psycopg 3.x
PostgreSQL 18 service
```

and executed the same Core schema/application test against SQLite and PostgreSQL.

### SQLite result

```text
TOOLING_BACKEND=sqlite
SQLALCHEMY_CORE=PASS
ALEMBIC_MIGRATION=PASS
PORTABLE_UUID=PASS
TRANSACTION_BOUNDARY=PASS
DIALECT_SPECIFIC_DDL_ISOLATION=PASS
TOOLING_SPIKE_RESULT=PASS
```

### PostgreSQL result

```text
TOOLING_BACKEND=postgresql
SQLALCHEMY_CORE=PASS
ALEMBIC_MIGRATION=PASS
PORTABLE_UUID=PASS
TRANSACTION_BOUNDARY=PASS
DIALECT_SPECIFIC_DDL_ISOLATION=PASS
TOOLING_SPIKE_RESULT=PASS
```

The spike verified:

```text
SQLite STRICT Core tables
foreign_keys PRAGMA installed through SQLAlchemy connection event
short application transaction rollback
real FK failure handling
SQLite FTS5 DDL isolated from PostgreSQL
canonical hyphenated UUID text on SQLite
native PostgreSQL UUID
same Core metadata model executing on PostgreSQL
Alembic migration on both backends
forced SQLite batch table recreation
preservation of STRICT during batch recreation
preservation and continued enforcement of a named CHECK constraint
preservation of existing row data through migration
```

---

## 7. Important implementation lessons discovered

### 7.1 STRICT changes type choices

SQLite STRICT tables accept only SQLite's strict storage-class type names.

A naive portable schema that emits `VARCHAR`, `CHAR(36)`, or similar names can therefore fail even though those declarations are fine in ordinary SQLite tables.

The production Core metadata should deliberately use SQLite-compatible physical types such as `TEXT`, with dialect-aware custom types where necessary.

### 7.2 Built-in SQLAlchemy Uuid does not exactly match the accepted SQLite contract

SQLAlchemy's generic `Uuid` uses a non-hyphenated 32-character representation on backends without native UUID support.

Specification 001 requires canonical lowercase hyphenated UUID text on SQLite and native UUID on PostgreSQL.

The spike therefore used an explicit `TypeDecorator` mapping:

```text
SQLite      -> TEXT, canonical 36-character UUID
PostgreSQL  -> native UUID
```

This preserved the domain contract on both backends.

### 7.3 Constraint naming is not cosmetic

Alembic's batch migration documentation shows that unnamed constraints are problematic in SQLite migrations.

The production schema must therefore use deterministic names for PK/FK/UNIQUE/CHECK/index structures.

### 7.4 Batch migrations need deliberate STRICT preservation

The forced SQLite recreation in the spike explicitly passed:

```python
table_kwargs={"sqlite_strict": True}
```

and verified the recreated table remained STRICT.

This should become migration-review discipline rather than an incidental implementation detail.

### 7.5 Autogenerate cannot be trusted blindly

Alembic itself states that generated migrations require manual review.

Therefore:

```text
autogenerate = candidate migration assistant
reviewed Alembic revision = accepted migration artifact
```

not:

```text
autogenerate output = authoritative schema change
```

---

## 8. Selected tooling contract

Promoted into Specification 002:

```text
SQLAlchemy Core 2.0 stable series
Alembic 1.x
no SQLAlchemy ORM as the primary domain/persistence model
raw DBAPI only for narrow adapter-specific behavior
```

The stable SQLAlchemy 2.0 line is selected because SQLAlchemy 2.1 remains beta at this checkpoint.

Exact package versions must ultimately be locked reproducibly. The dependency-manager/lockfile tool is still unselected.

---

## 9. Migration policy strengthened

The tooling decision also clarifies the production schema lifecycle:

```text
Core MetaData
    describes current schema

Alembic revisions
    authoritative ordered schema-evolution history
```

Production database creation/upgrades must be reproducible from migration history.

`MetaData.create_all()` remains useful for narrow tests and tooling spikes but should not bypass the migration history in deployed/real V1 workspaces.

SQLite-specific structures such as FTS5 should normally be managed explicitly through reviewed migrations/adapters rather than hidden runtime schema side effects.

---

## 10. Promotion audit

### Promoted

```text
docs/specifications/002_v1_persistence_tooling_standard.md
    accepted persistence-tooling contract

docs/DECISIONS.md
    D-029 tooling decision
```

### Not promoted to a new foundation

No new methodological or product-level theory was discovered. This is an implementation-standard decision under the already-promoted architecture.

### Evidence retained

```text
experiments/architecture_spikes/tooling_sqlalchemy_core_alembic_spike.py
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
.github/workflows/v1-persistence-tooling-spike.yml
```

---

## 11. Next legitimate step

The persistence infrastructure is now constrained enough to begin the first production-quality V1 persistence foundation without gambling on an untested implementation stack.

Next:

> **Define the first production relational schema and Alembic base migration behind Specification 001/002's ports, then validate an actual vertical slice through knowledge revisioning, project revision pinning, relations/rules, and migration history on SQLite with PostgreSQL portability CI.**

Do not implement the entire product schema at once. The first production schema should be the smallest coherent core that exercises the architecture under real application interfaces.
