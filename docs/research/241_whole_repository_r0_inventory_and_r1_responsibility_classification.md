# Research 241: Whole-Repository R0 Inventory and R1 Responsibility Classification

**Date:** 2026-09-22
**Status:** R0 INVENTORY COMPLETE / R1 INITIAL RESPONSIBILITY CLASSIFICATION COMPLETE / NO TARGET TREE SELECTED / R2 LIFECYCLE-DEPENDENCY-COCHANGE ANALYSIS NEXT
**Parent program:** Research 240 / PKIA-E01 whole-repository physical architecture evolution
**Repository base:** 2d35783da89e14b82b09af9e67247c98fb1eb90a
**Scope:** Inventory the tracked ADS repository as it actually exists and classify each major root by responsibility, lifecycle and build/runtime role without assuming that the current folder name or parent is correct.

## 1. Method

This pass deliberately separates two questions:

    R0
        What actually exists today?

    R1
        What is each major thing, conceptually?

The classification is not a placement decision.

For example, saying that migrations/ is persistence-schema evolution owned by the backend does not yet imply that migrations/ should move beneath src/, packages/, backend/ or any other future path.

Likewise, saying that tests/ is cross-cutting verification does not yet imply centralized or co-located tests.

## 2. Tracked root inventory

The tracked repository root is:

    .github/
    docs/
    experiments/
    frontend/
    migrations/
    prototype_v0/
    schemas/
    scripts/
    src/
    tests/
    tools/

    .gitignore
    .python-version
    README.md
    alembic.ini
    pyproject.toml
    uv.lock

Local-only/cache/generated entries are excluded from target classification unless their existence reveals an operational requirement.

Examples excluded from the tracked logical target:

    .venv/
    .ads-private/
    .tmp/
    .pytest_cache/
    frontend/node_modules/
    frontend/dist/
    generated experiment/runtime outputs ignored by Git

## 3. Root build and workspace boundaries

The current repository contains more than one technical workspace.

### 3.1 Root Python workspace

Root pyproject.toml defines:

    project name      autonomous-data-science-system
    build module      ads_system
    source package    src/ads_system
    test root         tests
    dependency lock   uv.lock
    database tooling  alembic.ini + migrations/

This is one clear executable/product workspace.

### 3.2 Frontend workspace

frontend/ has its own:

    package.json
    package-lock.json
    tsconfig.json
    Vite configuration
    Playwright configuration
    frontend README
    source tree
    e2e tree
    design-lab tree

CI regularly enters frontend/ as its own working directory.

This is a strong application/workspace boundary, not merely an arbitrary artifact folder.

### 3.3 Prototype V0 workspace

prototype_v0/ has its own:

    pyproject.toml
    source tree
    tests
    configs
    README
    generated/results areas
    dedicated CI workflow

It is a self-contained historical experimental project with a separate Python package lifecycle.

It is intentionally retained as falsification evidence rather than being the current product runtime.

## 4. Initial responsibility classification

| Current root | Primary conceptual responsibility | Current lifecycle character | Initial architectural observation |
|---|---|---|---|
| .github/ | repository-host integration, CI/CD and GitHub automation | repository-wide operational infrastructure | Naturally host-specific; central by platform convention, but individual workflows reveal owners elsewhere |
| src/ads_system/ | current ADS Python product/runtime implementation | active product code | Strong package boundary; internally already separates application/domain/infrastructure |
| frontend/ | current user-facing product/application workspace and design-validation surface | active but still partly spike/evaluation | Strong independent technical workspace with own toolchain |
| migrations/ | persistent database schema evolution for root ADS Python runtime | active backend persistence support | Conceptually owned by persistence, despite generic root placement |
| tests/ | Python verification for product code, experiments, repository governance and project-control subsystem | cross-cutting verification | Highly mixed ownership; centralized test discovery is convenient but not proof of ideal physical ownership |
| schemas/ | machine-readable contracts for several concerns | shared contract bucket | Mixed ownership: project-knowledge schemas coexist with model-collaboration and reusable-knowledge schemas |
| scripts/ | repository validators, release/audit tools, launchers, selectors and research utilities | mixed development support | Not one coherent subsystem; name reflects artifact form more than ownership |
| tools/project_knowledge/ | executable project-development knowledge/control support subsystem | active project-development infrastructure | Strong subsystem identity currently placed under generic tools/; the only tracked tools/ child |
| experiments/ | governed experimental implementations, harnesses and durable experiment artifacts | evidence/development lifecycle | Cross-cuts product, methodological and project-architecture concerns |
| prototype_v0/ | completed self-contained falsification prototype | historical experiment/project | Clear bounded historical project, not current runtime |
| docs/ | durable project knowledge, state, contracts, evidence, history, operations and navigation | broad authority/evidence layer | Extremely broad multi-owner space; Research 218 governs only its target information architecture |
| root config files | workspace bootstrap, packaging, dependency, DB-tool and repository conventions | repository-level support | Some are conventional root anchors because external tooling expects them |

## 5. Important mixed roots

Several roots are not conceptually homogeneous.

### 5.1 tests/

The centralized tests directory currently includes, among other things:

    ADS runtime/application tests
    Source Universe integration tests
    experiment harness tests
    repository-integrity tests
    continuity/routing tests
    model-collaboration tests
    project-knowledge/control architecture tests

Therefore:

    tests/
        !=
    one subsystem

It is a verification aggregation surface.

Whether that remains desirable depends on the future architecture and tooling cost of co-location.

### 5.2 schemas/

The root currently contains:

    schemas/project_knowledge/
    model_collaboration_thread_state_v1.schema.json
    reusable_knowledge_bundle_v1.schema.json

Therefore schemas/ is also an artifact-type aggregation surface across multiple owners.

### 5.3 scripts/

The root scripts directory contains:

    repository-integrity validators
    current-routing / Knowledge Map / checkpoint validators
    GitHub integration validators
    frontend verification selectors
    live experiment launchers
    public release audit
    research scripts under scripts/research/

This is a broad repository-support bucket rather than one bounded product capability.

### 5.4 experiments/

Experiments include:

    product/runtime architecture spikes
    retrieval/runtime/reasoning experiments
    methodological-navigation experiments
    project-knowledge architecture T1/T3/T4 experiments
    action-value and calibration work

So experiments/ expresses lifecycle/evidence type rather than one domain owner.

### 5.5 docs/

docs/ combines:

    project constitution/orientation
    current state and continuity
    epistemic/lifecycle records
    product/subsystem operational knowledge
    local execution
    model collaboration
    methodological knowledge
    project-control architecture
    private-companion public-safe knowledge

The earlier Research 218 problem is therefore one instance of a broader repository pattern: artifact/lifecycle and subsystem dimensions coexist physically.

## 6. Current project-development subsystem footprint

The present subsystem historically named project_knowledge spans several roots:

    tools/project_knowledge/
        implementation

    schemas/project_knowledge/
        machine-readable profile contracts

    tests/unit/test_project_knowledge_*.py
        verification

    docs/project_knowledge/
        architecture, generated views, captures and control artifacts

    experiments/project_knowledge_*/
        W5/T1/T3/T4 empirical work

    scripts/research/project_knowledge_*.py
        earlier research/probe utilities

    docs/research/project_knowledge_*/
        research evidence families

This demonstrates a real artifact-first physical organization.

It does not yet establish whether the future subsystem should be consolidated.

The R2/R3 comparison must distinguish:

    permanent subsystem implementation
    project-instance policy
    governed generated state
    subsystem architecture documentation
    research/evidence about the subsystem
    generic repository validation
    historical probes

Those may have different natural homes even if they concern the same topic.

## 7. Current dependency / workflow evidence already visible

CI gives useful ownership evidence.

Examples:

    frontend workflows operate with working-directory frontend

    prototype-v0 workflow installs and tests prototype_v0 independently

    root Python workflows use src/ads_system plus centralized tests

    persistence workflows bind src/ads_system infrastructure together with migrations/

    repository-integrity workflow explicitly binds:
        schemas/project_knowledge/
        tools/project_knowledge/
        scripts/repository_integrity.py
        routing/continuity validators

    many experiments bind selected src/ads_system modules plus one experiment directory

This is early evidence that several current root paths are physically separate even though they form one change/qualification unit.

R2 will measure that more systematically rather than inferring from examples.

## 8. Provisional conceptual concern map

The following concerns appear materially distinct enough to analyze as candidate architectural units:

    ADS product/runtime core
    user-facing frontend/application
    persistence/database evolution
    methodological/reusable knowledge capability
    Source Universe
    project-development control/knowledge system
    repository governance/validation
    model collaboration
    local execution/runtime integration
    governed experiment/evidence system
    documentation/project memory
    historical prototypes
    private companion boundary
    CI/repository-host integration

This is a concern map, not a folder proposal.

Several may later collapse together; several may split further.

## 9. What the inventory suggests so far

The current repository is neither purely artifact-first nor purely subsystem-first.

It is a pragmatic hybrid.

That hybrid has at least three strengths:

    familiar Python root conventions
    simple root-level pytest/package tooling
    clear separate frontend workspace

It also has at least four structural tensions:

    substantial subsystems are horizontally scattered across artifact roots

    generic artifact roots such as schemas/, scripts/ and tests/ contain
    multiple unrelated owners

    some domain/workspace roots such as frontend/ coexist directly with
    artifact roots such as tests/ and schemas/

    docs/ repeats the same dimensional mixing internally at a much larger scale

These tensions justify R2/R3 analysis.

They do not yet justify a migration.

## 10. R1 classification rule going forward

For the next phase, current path names should be ignored when asking what something is.

Each concern should be described along independent dimensions:

    product/application role
    runtime/deployment role
    reuse boundary
    authority role
    lifecycle
    change cadence
    dependency direction
    build/package boundary
    test/qualification boundary
    schema/config ownership
    data/persistence ownership
    knowledge/documentation ownership
    generated-state ownership
    private/public boundary
    historical versus current status

Only after those dimensions are known should physical grouping be proposed.

## 11. R2 next questions

R2 must now determine actual lifecycle, dependency and co-change evidence.

At minimum:

    Which roots or concerns change together repeatedly?

    Which can be built/tested/released independently?

    Which imports or executes which?

    Which configuration/schema files are consumed by which subsystem?

    Which CI gates bind multiple current roots into one qualification unit?

    Which roots are separated only because of ecosystem convention?

    Which roots have independent package managers/build systems?

    Which concerns are current product architecture versus development tooling?

    Which apparent subsystem boundaries exist only because of historical staging?

    Which areas are expected to survive long-term versus become historical evidence?

## 12. Current state

    R0=COMPLETE
    R1=INITIAL_CLASSIFICATION_COMPLETE
    TARGET_ROOT_TREE=NOT_SELECTED
    CURRENT_ROOT_TREE=EVIDENCE_ONLY
    CURRENT_ARCHITECTURE_STYLE=PRAGMATIC_HYBRID
    PSMF=INPUT
    PROJECT_KNOWLEDGE_NAME=OPEN
    TOOLS_ROOT=OPEN
    CENTRAL_TESTS=OPEN
    CENTRAL_SCHEMAS=OPEN
    CENTRAL_SCRIPTS=OPEN
    FRONTEND_ROOT=OPEN
    EXPERIMENTS_ROOT=OPEN
    DOCS_ROOT=OPEN
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R2_LIFECYCLE_DEPENDENCY_COCHANGE_ANALYSIS
