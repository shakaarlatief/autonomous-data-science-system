# Checkpoint 113: V1 Python Project Tooling Validated

**Date:** 2026-08-20  
**Status:** Historical tooling-selection and reproducibility checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 implementation foundation; Python project/dependency/build tooling selection  
**Scope:** Selects and validates the V1 Python project-management, lockfile, build-backend, source-layout, and cross-platform interpreter support contract.  
**Authority:** Historical rationale and validation evidence. D-030 and Specification 003 are the current accepted sources for this scope.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Why this checkpoint exists

After D-029 selected SQLAlchemy Core + Alembic, the repository still lacked a production Python project foundation and reproducible dependency lock.

That gap needed to be closed before the first production persistence slice, because architecture-relevant dependencies and CI should not be installed ad hoc.

The question was:

> **Which project/dependency/build workflow gives V1 a professional, reproducible, cross-platform Python foundation without coupling domain architecture to one packaging tool?**

---

## 2. Research conclusion

The current Python Packaging User Guide treats `pyproject.toml` as the standard project configuration surface and deliberately allows multiple workflow/build tools rather than prescribing one universal choice.

uv is currently a strong fit for this repository because it combines:

```text
project environment management
cross-platform locking
standard pyproject dependency declarations
PEP 735 dependency groups
managed/system Python support
command execution
package building
lock export/interoperability
```

Its project lock is designed to be committed and reused across platforms.

The current uv documentation also provides a pure-Python `uv_build` backend and recommends it for most straightforward Python projects, while keeping the backend replaceable through the standard PEP 517 build-system boundary.

---

## 3. Anti-lock-in reasoning

The accepted direction does not make uv configuration the semantic source of application dependencies.

Instead:

```text
standards-based pyproject.toml
    declares project/dependency intent

uv.lock
    records concrete reproducible resolution

uv
    manages/synchronizes the environment

uv_build
    implements the current pure-Python package build
```

uv can export the resolution to the standardized PEP 751 `pylock.toml` format.

Therefore a future workflow-tool change can replace the project manager/lock representation without redefining the ADS application architecture.

---

## 4. Candidate production foundation introduced

The repository now contains:

```text
pyproject.toml
src/ads_system/__init__.py
tests/test_package_smoke.py
.github/workflows/v1-python-project-tooling.yml
```

Initial package identities:

```text
distribution:
    autonomous-data-science-system

import package:
    ads_system
```

The import package intentionally avoids the overly generic `ads` namespace.

Prototype V0 remains isolated rather than being silently folded into production V1 code.

---

## 5. Python support boundary

The package declares:

```text
requires-python = ">=3.12"
```

The CI gate tested:

```text
Python 3.12
Python 3.13
Python 3.14
```

on:

```text
Ubuntu/Linux
Windows
```

This matters because the user-facing professional developer workflow is explicitly expected to work locally on normal developer machines rather than only in one CI Linux environment.

---

## 6. Reproducible gate

The workflow generated the committed `uv.lock` and passed the following contract:

```text
standard pyproject.toml metadata
uv 0.12.5
cross-platform uv.lock
Python 3.12 / 3.13 / 3.14
Linux + Windows
locked synchronization
pytest execution
uv_build package build
PEP 751 pylock.toml export
src-layout package import
```

Evidence:

```text
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

The gate's success means the project foundation is no longer hypothetical.

---

## 7. Version discipline

The project currently pins its uv workflow tool to:

```text
0.12.5
```

and constrains:

```text
uv_build >=0.12.5,<0.13
SQLAlchemy >=2.0.52,<2.1
Alembic >=1.19,<2
psycopg >=3.2,<4 where installed
```

Concrete resolved/transitive versions are recorded in `uv.lock`.

This separates intentional compatibility ranges from exact reproducible resolution.

---

## 8. Promotion audit

### Promoted

```text
docs/specifications/003_v1_python_project_and_dependency_tooling.md
    accepted V1 project/dependency/build tooling contract

docs/DECISIONS.md
    D-030 project-tooling decision
```

### No new foundation

This does not introduce new product or methodological theory. It is an implementation foundation beneath accepted architecture.

### Reproducible evidence retained

```text
pyproject.toml
uv.lock
.github/workflows/v1-python-project-tooling.yml
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

---

## 9. Next legitimate step

The project now has:

```text
accepted persistence architecture
accepted technical architecture contract
accepted SQL/migration toolkit
accepted reproducible Python project foundation
```

The next task is finally to implement the **first production-quality persistence vertical slice** rather than another infrastructure-selection layer.

That slice should prove a real application path through:

```text
knowledge stable identity
immutable revision publication
project creation
exact project -> knowledge revision pinning
at least one static relation
at least one conditional rule representation
repository ports / UnitOfWork
Alembic base migration
SQLite integration
PostgreSQL portability
```

The slice should remain deliberately bounded. The project should not materialize every Foundation 018 object before the first production architecture path has earned confidence.
