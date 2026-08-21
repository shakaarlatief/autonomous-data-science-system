# Specification 002: V1 Persistence Tooling Standard

**Date:** 2026-08-20  
**Status:** Accepted V1 technical specification v1.1 after governed-roundtrip portability closure  
**Scope:** Python persistence toolkit and schema-migration tooling for Specification 001's SQLite-centered architecture and its PostgreSQL migration seam  
**Authority:** Current V1 technical contract for persistence-tool implementation. Subordinate to D-028, Specification 001, and Foundations 017-020.  
**Validated:** Initial tooling selection validated 2026-08-20; migration portability strengthened and revalidated 2026-08-21 through Checkpoint 127  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Decision

V1 will use:

```text
SQLAlchemy Core 2.0 stable series
    schema metadata
    SQL expression construction
    engine / connection / transaction abstraction
    SQLite and PostgreSQL dialect boundary
    explicit custom types where Specification 001 requires them

Alembic 1.x
    ordered schema migration history
    SQLite batch migrations where necessary
    PostgreSQL-compatible migration path
```

SQLAlchemy ORM is **not** the primary V1 persistence/domain mapping.

Raw `sqlite3` / direct DBAPI access is **not** the normal repository implementation style. Direct driver SQL remains allowed only inside narrowly scoped persistence-adapter or maintenance code for capabilities that are deliberately database-specific, such as SQLite PRAGMAs and FTS5 DDL/query details.

The tested baseline pair was:

```text
SQLAlchemy 2.0.52
Alembic 1.19.0
Python 3.13
SQLite via Python sqlite3
PostgreSQL 18 via psycopg 3.x
```

The architecture selects the stable SQLAlchemy 2.0 API line rather than the SQLAlchemy 2.1 beta line. Exact dependency versions must be locked by the project dependency-management tooling.

---

## 2. Why SQLAlchemy Core

Specification 001 deliberately defines an explicit relational architecture and application-owned persistence ports.

SQLAlchemy Core fits that design because it is schema-centric and provides:

```text
MetaData / Table / Column / constraint definitions
composable SQL expressions
explicit Engine / Connection transactions
DBAPI integration
SQLite and PostgreSQL dialects
custom type adaptation
conditional/custom DDL hooks
runtime inspection
```

The application/domain model remains separate from SQLAlchemy table objects.

Repository adapters may translate between domain/application values and Core row mappings. The persistence toolkit does not become the methodological object model.

---

## 3. Why not raw DBAPI as the primary layer

Python's `sqlite3` module is capable and remains the underlying SQLite DBAPI, but using raw DBAPI/SQL as the primary repository layer would force V1 to own too much infrastructure manually:

```text
SQLite/PostgreSQL SQL-dialect branching
type adaptation
portable schema metadata
constraint naming
query construction
transaction boilerplate
migration integration
schema inspection
future driver substitution
```

Specification 001 already requires a credible PostgreSQL migration seam. Rebuilding SQLAlchemy-like portability abstractions in application code would add maintenance burden without a demonstrated benefit.

Raw driver calls are therefore restricted to adapter-local behavior where abstraction would obscure a genuinely backend-specific capability.

---

## 4. Why not SQLAlchemy ORM as the primary model

The ORM is mature and capable, but its principal value is object-relational mapping, identity-map/session behavior, relationship management, and state-oriented unit-of-work persistence.

V1 already has explicit domain semantics and application UnitOfWork boundaries, including:

```text
immutable accepted knowledge revisions
append-only evidence/findings in many cases
typed project lifecycles
exact project -> knowledge revision references
explicit rule traces
separation of current state from event history
```

Making ORM-mapped objects the central domain representation would create an unnecessary second lifecycle/identity abstraction and could blur the required boundary:

```text
domain semantics != persistence representation
```

The ORM is not prohibited forever. A later subsystem may use it if a concrete workload demonstrates clear value, but any use must remain behind the same application ports and must not redefine the core domain model.

---

## 5. SQLAlchemy metadata conventions

### 5.1 One canonical Core metadata model

Production relational schema definitions should be expressed through SQLAlchemy Core `MetaData` and `Table` constructs, with explicit database-independent domain semantics.

The metadata is the current schema model, while **Alembic migration history is the authoritative schema-evolution path**.

### 5.2 Constraint naming is mandatory

Use a deterministic naming convention for:

```text
primary keys
foreign keys
unique constraints
check constraints
indexes
```

This is especially important because Alembic's SQLite batch migration workflow cannot reliably address unnamed constraints.

Manual names must also remain inside the portability envelope of supported backends. PostgreSQL identifiers are limited to 63 bytes, so migration/schema identifiers must not rely on silent PostgreSQL truncation.

### 5.3 SQLite STRICT discipline

Specification 001 requires authoritative SQLite tables to use `STRICT` mode where practical.

SQLAlchemy's SQLite dialect supports `sqlite_strict=True`.

STRICT SQLite tables accept only SQLite's strict storage type names, so portable Core metadata must avoid allowing generic types such as `VARCHAR`/`CHAR` to leak into STRICT SQLite DDL. Textual authoritative fields should compile to SQLite `TEXT`, numeric fields to the appropriate strict primitive, and portable custom types must deliberately select compatible SQLite implementations.

---

## 6. Durable UUID mapping

Specification 001 requires:

```text
SQLite: canonical lowercase hyphenated UUID text
PostgreSQL: native UUID
```

SQLAlchemy's built-in backend-agnostic `Uuid` type uses a 32-character non-hyphenated representation on non-native backends, which does not exactly match the accepted SQLite contract.

V1 should therefore use a small explicit SQLAlchemy `TypeDecorator` or equivalent adapter type that maps:

```text
SQLite      -> TEXT containing canonical 36-character UUID string
PostgreSQL  -> native UUID
Python/app  -> storage-neutral UUID/string contract
```

The tooling spike validated this pattern on both databases.

---

## 7. SQLite connection contract through SQLAlchemy

Every SQLite engine/connection path must enforce Specification 001's operational contract.

At minimum:

```text
PRAGMA foreign_keys = ON       on every connection
PRAGMA busy_timeout            bounded policy
journal_mode = WAL             database initialization/maintenance
synchronous = FULL             default V1 durability profile
```

SQLAlchemy connection events are an appropriate adapter-local mechanism for per-connection PRAGMAs.

Application/domain services must not know about these PRAGMAs.

---

## 8. Transaction policy

Use SQLAlchemy Core's explicit connection/transaction APIs under the application's UnitOfWork abstraction.

Rules remain:

```text
short semantic transactions
no network/LLM/embedding/human wait inside a DB transaction
one application-owned authoritative write path
rollback must leave no partially published semantic unit
```

SQLAlchemy's transaction abstraction is an implementation mechanism, not the domain UnitOfWork itself.

---

## 9. Alembic is the schema-evolution authority

All production schema creation/evolution must be representable as ordered Alembic revisions.

Professional migration policy:

```text
1. production databases are upgraded through Alembic revisions;
2. migration files are committed and code-reviewed;
3. destructive/high-risk migrations require a verified backup first;
4. schema version compatibility is checked at application startup;
5. migrations are tested from an empty/base database and from representative prior versions;
6. SQLite and PostgreSQL portability tests cover the core durable schema;
7. migration logic must not hide methodological/business semantics in database code;
8. revision identifiers are unique and fit the configured Alembic version-table envelope.
```

`MetaData.create_all()` may be used in narrow tests/spikes, but it must not replace the production migration history.

### 9.1 Alembic revision-identifier portability

The current Alembic version table uses the default revision-value envelope:

```text
alembic_version.version_num VARCHAR(32)
```

The governed reusable-knowledge round-trip exposed that a descriptive revision identity longer than 32 characters can appear harmless under SQLite yet fail on PostgreSQL when Alembic records the migration version.

Therefore, while the default version table remains in use:

```text
every Alembic revision identifier
    -> must be unique
    -> must have length <= 32 characters
```

Migration filenames may remain more descriptive than the revision identity.

If a future project deliberately changes the Alembic version-table schema, that change must itself be migration-safe and validated across SQLite and PostgreSQL before this invariant is relaxed.

The deterministic regression guard is:

```text
tests/test_migration_revision_ids.py
```

---

## 10. Alembic autogenerate policy

Alembic autogenerate is an **assistant**, not an authority.

Generated candidate revisions must always be manually reviewed and corrected before acceptance.

Reasons include known limitations around constraint changes, renames, backend-specific constructs, and SQLite table-recreation behavior.

The CI/tooling layer should use Alembic's schema-drift checking capabilities where useful to detect when model metadata and migration history diverge, but no generated migration should be silently applied merely because autogenerate produced it.

---

## 11. SQLite batch migration policy

SQLite's limited `ALTER TABLE` support requires Alembic batch migrations for relevant structural changes.

V1 migrations must:

```text
use deterministic constraint names
preserve STRICT table behavior
preserve named CHECK/UNIQUE/FK constraints
preserve data during table recreation
explicitly review batch operations that recreate tables
```

The tooling spike forced a real Alembic table recreation and verified that:

```text
data survived
STRICT survived
named CHECK constraint survived
new column existed
constraint enforcement still worked
```

The validated spike uses `table_kwargs={"sqlite_strict": True}` for the SQLite batch recreation.

---

## 12. Backend-specific DDL remains isolated

SQLite FTS5 is intentionally a SQLite implementation of the `LexicalIndex` boundary.

SQLAlchemy supports dialect-conditional/custom DDL, and the tooling spike verified that SQLite-only FTS DDL did not leak into PostgreSQL.

For production schema history, backend-specific structures should normally be created/dropped explicitly in reviewed Alembic migrations rather than hidden behind surprising runtime metadata side effects.

Backend-specific SQL may live inside:

```text
SQLite persistence/index adapter
Alembic migration implementation
maintenance tooling
```

It must not leak into methodological/domain services.

---

## 13. PostgreSQL portability requirement

All core relational metadata and migrations must continue to preserve Specification 001's PostgreSQL migration seam.

Initial tooling validation verified:

```text
native UUID mapping
foreign-key integrity
named constraints
project -> knowledge revision references
application transaction semantics
Alembic migration execution
SQLite-specific FTS DDL isolation
```

The richer governed reusable-knowledge round-trip later added direct PostgreSQL 18 evidence for migration 0002 and the governed import/accept/export/pinning seam.

That gate exposed two portability classes worth preserving:

```text
schema/migration object identifiers
    -> respect PostgreSQL's 63-byte identifier limit

Alembic revision values
    -> respect the current 32-character version-table limit
```

New core persistence features should receive PostgreSQL compile/execution coverage when they materially affect the migration seam.

---

## 14. Dependency/version policy

The accepted API family is:

```text
SQLAlchemy >= 2.0 stable, < 2.1 until 2.1 is stable and explicitly reviewed
Alembic 1.x compatible with the selected SQLAlchemy line
psycopg 3.x for PostgreSQL validation/migration work
```

The current validated versions are evidence, not an instruction to float dependencies in production.

The implementation environment locks transitive dependencies reproducibly through the accepted V1 Python project tooling. Updating SQLAlchemy/Alembic requires normal dependency review and CI, including SQLite and PostgreSQL persistence gates.

---

## 15. Acceptance evidence

Initial tooling-selection evidence:

```text
experiments/architecture_spikes/tooling_sqlalchemy_core_alembic_spike.py
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
.github/workflows/v1-persistence-tooling-spike.yml
```

The initial CI spike passed on SQLite and PostgreSQL:

```text
SQLALCHEMY_CORE=PASS
ALEMBIC_MIGRATION=PASS
PORTABLE_UUID=PASS
TRANSACTION_BOUNDARY=PASS
DIALECT_SPECIFIC_DDL_ISOLATION=PASS
TOOLING_SPIKE_RESULT=PASS
```

Later portability/production-seam evidence:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
tests/test_migration_revision_ids.py
```

Checkpoint 127 records the final governed-roundtrip gate:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS on all three jobs
```

---

## 16. Explicit non-decisions

This specification does **not** select:

```text
full physical production DDL
async database access
connection-pool tuning beyond current local-first needs
complete PostgreSQL deployment configuration
frontend/API framework
embedding model or reranker
```

Async persistence is not required for the current V1 architecture. It should not be introduced merely because SQLAlchemy supports it.

---

## 17. Current implementation status

The first production persistence slice and the richer governed reusable-knowledge persistence/interchange seam are now implemented and cross-backend validated.

Current persistence evidence therefore covers:

```text
production migration foundation
exact historical project -> knowledge revision references
candidate-versus-accepted governance
accepted-current pointers
trusted deterministic accepted snapshot export/reload
provenance and relation governance
collections
SQLite/Linux
SQLite/Windows
PostgreSQL 18
migration identifier portability regression guard
```

The next major methodological-knowledge work is outside this tooling specification's scope: production retrieval/MethodologicalHorizon evaluation and selective reasoning-context construction.
