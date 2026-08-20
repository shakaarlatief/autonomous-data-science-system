from pathlib import Path


def update_decisions() -> None:
    path = Path("docs/DECISIONS.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "**Status:** Superseded for the V1 persistence/retrieval architecture by D-028 and for persistence tooling by D-029; still applicable to implementation subsystems not yet selected",
        "**Status:** Superseded for the V1 persistence/retrieval architecture by D-028, persistence tooling by D-029, and Python project/dependency tooling by D-030; still applicable to implementation subsystems not yet selected",
    )
    if "## D-030. Use uv with standards-based pyproject metadata for the V1 Python project" not in text:
        text = text.rstrip() + """

---

## D-030. Use uv with standards-based pyproject metadata for the V1 Python project

**Status:** Accepted for V1  
**Date:** 2026-08-20

V1 will use `pyproject.toml` as the standards-based Python project/dependency declaration, `uv` as the project/dependency/environment manager, a committed `uv.lock` for reproducible cross-platform resolution, and `uv_build` as the current PEP 517 build backend for the pure-Python `ads_system` package.

The current validated tooling baseline is:

```text
uv 0.12.5
uv_build >=0.12.5,<0.13
Python >=3.12
```

The package is tested on Python 3.12, 3.13, and 3.14 on Linux and Windows.

The distribution/import names are:

```text
distribution: autonomous-data-science-system
import package: ads_system
```

The dependency intent remains in standard `pyproject.toml` metadata. `uv.lock` is committed but tool-managed, and uv's PEP 751 `pylock.toml` export is retained as an interoperability path. The project is not architecturally coupled to uv's lock format.

### Rationale

The first production persistence slice now depends on SQLAlchemy/Alembic and needs repeatable local/CI environments. Ad-hoc package installation would undermine the architecture's reproducibility goals.

uv provides one cross-platform workflow for locking, synchronization, Python selection, command execution, and package building while still consuming standard Python project metadata. A committed universal lockfile supports reproducible development and dependency upgrades. The build backend is replaceable through the standard PEP 517 boundary if future extension-module or packaging requirements change.

A committed project-tooling gate generated the lockfile and passed package import/tests/build plus PEP 751 export on Linux and Windows across Python 3.12-3.14.

See:

```text
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```
""" + "\n"
    path.write_text(text, encoding="utf-8")


def update_spec_001() -> None:
    path = Path("docs/specifications/001_v1_sqlite_technical_architecture.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "**Status:** Accepted V1 technical specification v1.0",
        "**Status:** Accepted V1 technical specification v1.1",
        1,
    )
    text = text.replace(
        "The migration framework/library remains unselected until the bounded implementation/tooling choice clarifies whether a dedicated library is valuable.",
        "Migration tooling is now specified by Specification 002: SQLAlchemy Core 2.0 stable-series APIs implement the relational adapter and Alembic 1.x is the authoritative production schema-migration mechanism. This later tooling decision preserves the migration semantics defined here.",
    )
    old = """First define the **bounded V1 persistence/retrieval implementation contract and tooling**:

```text
1. choose the SQL access / repository implementation approach;
2. choose or deliberately decline a schema migration framework;
3. convert the validated spike schema into reviewed production migrations;
4. define typed domain/repository interfaces and transaction boundaries;
5. define deterministic export/import formats;
6. define the first production retrieval-evaluation fixture before selecting an embedding model;
7. preserve PostgreSQL adapter compatibility in tests.
```

After those boundaries are explicit, implement the first bounded V1 subsystem rather than the entire frontend/autonomous product at once."""
    new = """Persistence and Python project tooling are now specified by:

```text
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
```

The next step is to implement the **first production-quality V1 persistence vertical slice** behind the accepted ports, using SQLAlchemy Core + Alembic inside the reproducible uv-managed project.

The slice should prove stable knowledge identity/revisions, project revision pinning, at least one relation and rule representation, real migration history, SQLite integration, and retained PostgreSQL portability without materializing the whole future product schema."""
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


def update_knowledge_map() -> None:
    path = Path("docs/KNOWLEDGE_MAP.md")
    text = path.read_text(encoding="utf-8")
    marker = "\n---\n\n## Earlier reusable-knowledge theory\n"
    if "## Accepted V1 implementation and Python project tooling" not in text:
        section = """
---

## Accepted V1 implementation and Python project tooling

Persistence tooling:

```text
docs/DECISIONS.md, D-029
docs/specifications/002_v1_persistence_tooling_standard.md
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
```

Accepted direction:

```text
SQLAlchemy Core 2.0 stable series
Alembic 1.x
SQLAlchemy ORM not the primary domain/persistence model
raw DBAPI only for narrow backend-specific adapter behavior
```

Python project/dependency/build tooling:

```text
docs/DECISIONS.md, D-030
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
pyproject.toml
uv.lock
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

Accepted direction:

```text
standards-based pyproject.toml
uv 0.12.5
committed cross-platform uv.lock
uv_build for the current pure-Python package
src/ads_system source layout
Python >=3.12, tested on 3.12/3.13/3.14 on Linux + Windows
```

The persistence and packaging tools are implementation mechanisms behind the already-accepted architecture; they do not redefine the methodological/domain object model.
"""
        if marker not in text:
            raise RuntimeError("KNOWLEDGE_MAP insertion marker not found")
        text = text.replace(marker, "\n" + section + marker, 1)
    start = text.find("## Exact next step")
    if start != -1:
        text = text[:start] + """## Exact next step

Implement the **first production-quality V1 persistence vertical slice** behind Specifications 001-003.

The smallest coherent slice should exercise:

```text
stable knowledge identity + immutable accepted revision
knowledge governance/current pointer
component / relation / conditional-rule storage
project identity and minimal epistemic state
exact project -> knowledge revision reference
repository ports and UnitOfWork
Alembic base migration
SQLite integration tests
PostgreSQL portability CI
```

Do not materialize every Foundation 018 object or build the full frontend/autonomous workflow before this first real persistence path has been validated.
"""
    path.write_text(text, encoding="utf-8")


def update_current_state() -> None:
    path = Path("docs/CURRENT_STATE.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace("**Checkpoint:** 112", "**Checkpoint:** 113", 1)
    text = text.replace(
        "persistence-tooling selection are complete; the first production V1 persistence foundation is the active task",
        "persistence-tooling selection, and reproducible Python project/dependency tooling are complete; the first production V1 persistence foundation is the active task",
        1,
    )
    marker = "\n## Current implementation stage\n"
    if "## Accepted V1 Python project/dependency tooling" not in text:
        section = """
## Accepted V1 Python project/dependency tooling

D-030 and Specification 003 select:

```text
standards-based pyproject.toml
uv 0.12.5
committed cross-platform uv.lock
uv_build for the current pure-Python package
src/ads_system source layout
Python >=3.12
```

The committed CI gate passed on Linux and Windows under Python 3.12, 3.13, and 3.14 and verified locked synchronization, tests, package building, and PEP 751 `pylock.toml` export.

Sources:

```text
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

"""
        if marker not in text:
            raise RuntimeError("CURRENT_STATE insertion marker not found")
        text = text.replace(marker, "\n" + section + marker, 1)
    text = text.replace("project package/build manager and lockfile mechanism\n", "")
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    update_decisions()
    update_spec_001()
    update_knowledge_map()
    update_current_state()
