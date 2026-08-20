# Specification 003: V1 Python Project and Dependency Tooling

**Date:** 2026-08-20  
**Status:** Accepted V1 technical specification v1.0  
**Scope:** Python project metadata, dependency resolution/locking, package build, source layout, and reproducible development/CI environment for the V1 application package  
**Authority:** Current V1 technical contract for Python project/dependency/build tooling. Subordinate to current project architecture and Specifications 001-002.  
**Validated:** 2026-08-20 through the committed Linux/Windows and Python 3.12/3.13/3.14 project-tooling gate  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Decision

V1 will use:

```text
pyproject.toml
    standards-based project metadata and dependency declarations

uv 0.12 stable series
    project environment management
    dependency resolution
    reproducible lockfile management
    command execution
    build frontend

uv.lock
    committed cross-platform resolved environment

uv_build
    PEP 517 build backend for the current pure-Python V1 package

src layout
    src/ads_system/
```

The current validated uv version is:

```text
0.12.5
```

and `pyproject.toml` currently enforces that exact project-tool version through `tool.uv.required-version` so developer and CI behavior do not drift silently.

The build backend is constrained to the compatible current minor family:

```text
uv_build >=0.12.5,<0.13
```

This is a V1 tooling decision, not a claim that uv or uv_build must remain forever. Project metadata and package semantics remain standards-based so a later tooling change is a bounded developer-infrastructure migration.

---

## 2. Why uv

The current Python Packaging User Guide deliberately does not impose one universal workflow tool, but lists uv among modern tools that cover project management, dependency management, packaging, and publishing.

For this repository, uv fits the actual requirements especially well:

```text
single cross-platform project lockfile
exact/reproducible environment synchronization
standard pyproject.toml dependency declarations
PEP 735 dependency-group support
managed or system Python support
Linux and Windows developer workflows
project command execution through uv run
package building through uv build
lock export for interoperability
```

The accepted architecture needs repeatable SQLite/PostgreSQL test environments and reproducible dependency upgrades. A committed lockfile is therefore operationally valuable rather than cosmetic.

---

## 3. Standards boundary and anti-lock-in policy

The authoritative human-authored dependency intent remains in standard project metadata:

```text
[project]
[project.optional-dependencies]
[dependency-groups]
[build-system]
```

`uv.lock` records the concrete reproducible resolution and is committed to Git.

The lockfile is tool-managed and must not be hand-edited.

For interoperability, uv can export the resolution to formats including the standardized PEP 751 `pylock.toml` format. The CI gate verifies that this export succeeds.

Therefore:

```text
project dependency semantics
    !=
permanent dependence on one proprietary lockfile format
```

A future package-manager change may regenerate a different lock representation from standards-based dependency declarations. Such a change must not affect the ADS domain/application architecture.

---

## 4. Distribution and import-package naming

Current names are intentionally distinct:

```text
Python distribution:
    autonomous-data-science-system

Python import package:
    ads_system
```

The distribution name matches the repository/product identity.

The import package is shorter while remaining specific enough to avoid making the core application package a generic `ads` namespace.

Prototype V0 remains isolated under its historical package and is not merged into the production V1 package merely for naming convenience.

---

## 5. Source layout

V1 uses the standard source layout:

```text
pyproject.toml
src/
    ads_system/
        __init__.py
tests/
```

The source layout reduces accidental imports from the repository working directory and makes tests exercise the installed project structure more faithfully.

As the vertical slice grows, internal modules may be organized around domain/application/infrastructure boundaries, but Specification 003 does not freeze a large package tree before the first production slice proves what is actually needed.

---

## 6. Python-version policy

The package currently declares:

```text
requires-python = ">=3.12"
```

The project-tooling gate verifies the package on:

```text
Python 3.12
Python 3.13
Python 3.14
```

on:

```text
Linux
Windows
```

This gives the project modern Python semantics without needlessly requiring the newest interpreter for architecture features that do not depend on it.

The UUIDv7 domain preference in Specification 001 must remain behind an ID-generation abstraction rather than forcing the entire application to require a particular Python release merely because one standard-library version adds a convenience function.

---

## 7. Dependency groups

Runtime dependencies belong in `project.dependencies`.

Optional runtime capabilities belong in `project.optional-dependencies`, for example the future PostgreSQL adapter dependency.

Development/test-only tooling belongs in standard dependency groups.

Current initial distinction:

```text
runtime:
    SQLAlchemy
    Alembic

optional postgres runtime:
    psycopg

dev/test:
    pytest
    psycopg for portability CI
```

Do not put every development tool into the runtime package merely to simplify installation.

---

## 8. Locking and synchronization policy

Normal developer workflow:

```text
uv sync --locked
uv run --locked <command>
```

Dependency changes intentionally update both:

```text
pyproject.toml
uv.lock
```

CI must fail rather than silently re-resolve when the committed lockfile and project metadata disagree.

Dependency upgrades should be explicit and reviewable rather than occurring merely because a newer package was published.

---

## 9. Build policy

The V1 package is currently pure Python, so `uv_build` is sufficient and intentionally simple.

Build validation uses:

```text
uv build --no-sources
```

so the package is verified without depending on local source overrides that would not exist for an external installer.

The build backend is a replaceable packaging concern. If future requirements add extension modules, complex build scripts, or another package topology, the project may switch build backend without changing application/domain semantics.

---

## 10. CI policy

The project-tooling gate is preserved at:

```text
.github/workflows/v1-python-project-tooling.yml
```

It verifies:

```text
uv lock succeeds
lock consistency
package imports through the src layout
pytest passes
Python 3.12/3.13/3.14 compatibility
Linux and Windows compatibility
package build succeeds
PEP 751 pylock.toml export succeeds
```

Successful evidence is persisted at:

```text
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

This tooling CI is not a substitute for the later production persistence integration suite.

---

## 11. Dependency upgrade discipline

Core persistence dependencies are architecture-relevant and should not float across major API lines silently.

Current intent:

```text
SQLAlchemy >=2.0.52,<2.1
Alembic >=1.19,<2
psycopg >=3.2,<4 where PostgreSQL support is installed
```

The committed lockfile pins concrete transitive versions.

A deliberate dependency upgrade should run at minimum:

```text
project-tooling gate
persistence-tooling gate
V1 architecture/persistence integration tests affected by the change
```

SQLAlchemy 2.1 remains outside the accepted range while it is beta. A later stable 2.1 adoption requires explicit review rather than an accidental resolver upgrade.

---

## 12. What is intentionally not selected here

```text
full production package/module hierarchy
static type checker
formatter/linter stack
release/publishing workflow
public PyPI publishing
workspace/monorepo structure
Docker production image
frontend dependency tooling
```

These should be added when concrete needs justify them.

The repository is not converted into a uv workspace merely because uv supports workspaces. One production package is currently enough.

---

## 13. Validation evidence

Reproducible artifacts:

```text
pyproject.toml
uv.lock
src/ads_system/__init__.py
tests/test_package_smoke.py
.github/workflows/v1-python-project-tooling.yml
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

The gate passed across Linux and Windows on Python 3.12, 3.13, and 3.14.

This establishes that the packaging/dependency foundation is sufficiently stable to support the first production persistence vertical slice.

---

## 14. Next step

Use this project foundation with Specifications 001 and 002 to implement the first production-quality V1 persistence vertical slice.

The slice should remain small and architecture-revealing rather than attempting to materialize every future product object at once.
