# Research 242: Whole-Repository R2 Lifecycle, Dependency and Co-Change Analysis

**Date:** 2026-09-22
**Status:** R2 COMPLETE / NATURAL BOUNDARIES AND AGGREGATION SURFACES IDENTIFIED / NO TARGET TREE SELECTED / R3 ARCHETYPE SYNTHESIS NEXT
**Parent program:** Research 240
**Inventory/classification basis:** Research 241
**Repository base:** 470a3b4070b7fb72ae474e85696ec6f13bf4b3af
**Scope:** Determine which current ADS concerns genuinely share lifecycle, dependency, build/qualification and co-change boundaries, while avoiding the false inference that current paths or commit habits define the future architecture.

## 1. Evidence model

R2 uses four kinds of repository evidence:

    package/workspace boundaries
        pyproject.toml
        package.json
        lockfiles
        build configuration
        working-directory boundaries

    static dependency evidence
        Python imports
        schema-path consumers
        Alembic/persistence consumers
        frontend runtime/network references

    qualification boundaries
        GitHub Actions path triggers
        test commands
        integration gates
        repository-integrity gates

    Git history / co-change evidence
        root touch frequency
        single-root versus multi-root changes
        pairwise co-change
        first/last observed change windows

No one evidence type is sufficient by itself.

In particular:

> low co-change does not prove architectural independence when the repository deliberately uses small focused commits.

Likewise:

> frequent co-change does not prove one subsystem when a central validation surface intentionally observes many owners.

## 2. Historical activity windows

Observed path-history windows at the R2 base:

| Root | First observed change | Last observed change | Commits touching root |
|---|---:|---:|---:|
| prototype_v0/ | 2026-08-08 | 2026-08-19 | 95 |
| .github/ | 2026-08-08 | 2026-09-19 | 115 |
| docs/ | 2026-08-07 | 2026-09-22 | 1798 |
| scripts/ | 2026-08-19 | 2026-09-19 | 57 |
| src/ | 2026-08-20 | 2026-08-30 | 37 |
| frontend/ | 2026-08-20 | 2026-08-29 | 416 |
| migrations/ | 2026-08-20 | 2026-08-25 | 8 |
| experiments/ | 2026-08-20 | 2026-09-20 | 86 |
| tests/ | 2026-08-20 | 2026-09-20 | 92 |
| schemas/ | 2026-08-20 | 2026-09-18 | 5 |
| tools/ | 2026-09-15 | 2026-09-20 | 17 |

This exposes strong temporal staging.

Most importantly:

    prototype_v0/
        completed before the V1 product work began

    frontend/ and src/
        concentrated in the late-August V1 build/spike period

    tools/project_knowledge/
        appears only in the later mid-September project-control program

    docs/
        remains continuously active across all phases

Therefore several current top-level roots are at least partly products of **development era**, not necessarily timeless architectural categories.

This is directly relevant to the owner's prototype_v0 clarification: its historical existence does not establish a future prototype architecture.

## 3. Root co-change profile

Across the parsed Git history, the major tracked roots show:

| Root | Commits touching root | Root-only commits | Root-only share |
|---|---:|---:|---:|
| .github/ | 122 | 104 | 85.2% |
| docs/ | 1798 | 1726 | 96.0% |
| experiments/ | 86 | 69 | 80.2% |
| frontend/ | 416 | 415 | 99.8% |
| migrations/ | 8 | 7 | 87.5% |
| prototype_v0/ | 95 | 95 | 100.0% |
| schemas/ | 5 | 0 | 0.0% |
| scripts/ | 61 | 22 | 36.1% |
| src/ | 37 | 33 | 89.2% |
| tests/ | 92 | 34 | 37.0% |
| tools/ | 17 | 0 | 0.0% |

The strongest cross-root pairs by observed commit co-change include:

    docs + tests          42
    docs + scripts        33
    scripts + tests       19
    tests + tools         17
    docs + experiments    14
    docs + tools          10
    .github + scripts     10
    experiments + tests    7
    schemas + tests        5
    src + tests            4
    schemas + tools        3

These counts are descriptive rather than normative.

The key interpretation is that **tests, scripts and schemas behave much more like cross-cutting support/qualification surfaces**, whereas frontend and prototype_v0 behave like strongly bounded workspaces in the historical record.

## 4. Project-development subsystem lifecycle boundary

The current subsystem historically named project_knowledge provides the clearest vertical-boundary evidence.

Current implementation footprint:

    tools/project_knowledge/
    schemas/project_knowledge/
    tests/unit/test_project_knowledge_*.py
    docs/project_knowledge/
    experiments/project_knowledge_*/
    scripts/research/project_knowledge_*.py

Observed implementation behavior:

    tools/project_knowledge touched in 17 commits

    every one of those 17 commits also touched
    project-knowledge tests

    3 of 17 also touched project-knowledge schemas

    the project-development implementation has no observed import
    dependency on src/ads_system

    src/ads_system has no observed import dependency on
    tools/project_knowledge

This strongly supports a **real lifecycle and dependency boundary** between:

    ADS product/runtime
        and
    project-development control/knowledge mechanism

It does not yet decide physical placement.

It does show that tools/project_knowledge is not merely a miscellaneous helper collection.

Its schemas and tests are qualification-coupled to it even though they live under repository-wide artifact roots.

This is evidence in favor of treating the project-development mechanism as a first-class subsystem during R3.

## 5. Product/runtime Python boundary

The root Python workspace is coherent at the package/build level:

    pyproject.toml
    uv.lock
    src/ads_system/
    tests/
    alembic.ini
    migrations/

Static imports show that:

    experiments import ads_system
    migrations/env.py imports ads_system
    integration/unit tests import ads_system

The current package itself is organized internally as:

    application/
    domain/
    infrastructure/

This is a strong current package boundary.

However, the physical root around it is not equally cohesive.

tests/ contains tests for many owners beyond ads_system.

schemas/ contains contracts for several unrelated concerns.

scripts/ contains repository governance and research utilities unrelated to product runtime.

Therefore:

> root Python workspace coherence does not imply that every current Python-adjacent root belongs to one product subsystem.

## 6. Persistence and migrations

migrations/ appears historically independent by commit count, but dependency and qualification evidence contradicts any simple "independent subsystem" reading.

alembic.ini explicitly binds:

    script_location = migrations

migrations/env.py imports ads_system.

Multiple integration tests instantiate Alembic using the root migrations directory.

CI workflows bind migrations together with:

    src/ads_system/application
    src/ads_system/infrastructure/persistence
    retrieval
    Source Universe
    reusable-knowledge interchange
    integration tests

Therefore the natural owner of migrations is **the persistence/data-model capability of the current ADS runtime**, even though the folder is physically at repository root.

This is a good example of why path and co-change alone are insufficient.

R3 must consider at least two possibilities:

    keep root migrations/ because Alembic convention/tooling makes it valuable

    or
    co-locate persistence evolution more closely with its owning subsystem

The current root location is not self-justifying.

## 7. Schema ownership

schemas/ is a particularly clear aggregation surface.

It currently contains at least three semantically different owners:

    schemas/project_knowledge/
        consumed directly by tools/project_knowledge
        and project-knowledge tests

    schemas/reusable_knowledge_bundle_v1.schema.json
        part of ADS product knowledge-interchange workflows

    schemas/model_collaboration_thread_state_v1.schema.json
        consumed by model-collaboration validation/tests

The project-knowledge implementation hard-codes exact repository-relative schema paths.

The reusable-knowledge and model-collaboration schemas have completely different consumers and lifecycles.

Therefore:

> schemas/ is an artifact-type namespace, not one architectural owner.

This does not make a centralized schemas/ directory unprofessional.

It means R3 must compare its discoverability/tooling benefits against the ownership clarity of co-located schemas.

## 8. Central tests as qualification aggregation

tests/ is also clearly multi-owner.

It contains:

    ADS application/runtime tests
    persistence integration tests
    Source Universe tests
    experiment harness tests
    repository-governance tests
    model-collaboration tests
    project-development-system tests

Static imports demonstrate that tests qualify both:

    ads_system
    and
    tools.project_knowledge

Co-change demonstrates that tests frequently move with scripts/tools/schemas.

This supports the interpretation:

> tests/ is currently a repository-wide qualification aggregation surface.

Whether that is the best long-term physical structure remains open.

The future design must distinguish:

    repository-wide integration/acceptance tests
        from
    subsystem-local unit/contract tests

R3 should therefore test a **hybrid test topology**, not only all-centralized versus all-co-located extremes.

## 9. scripts/ as a non-domain bucket

scripts/ has one of the highest multi-root co-change rates:

    61 commits touching scripts
    39 also touch another tracked root
    only 36.1% are scripts-only

Its contents span:

    repository integrity
    routing/continuity validation
    checkpoint/Knowledge Map validation
    model-collaboration validation
    release auditing
    GitHub checks
    frontend verification selection
    live experiment launching
    research/probe scripts

Therefore scripts/ is primarily an **execution-form bucket**.

The fact that something is a script says little about its architectural owner.

This is a strong R3 challenge to a permanent undifferentiated scripts/ root.

Some scripts may remain legitimately repository-wide tooling.

Others may belong with the subsystem they operate.

Others may be historical research evidence and should not be treated as permanent tooling at all.

## 10. experiments/ as a lifecycle family

experiments/ is similarly cross-domain.

It contains experiments for:

    architecture/persistence
    runtime/reasoning
    retrieval
    methodological navigation
    recommendation action value
    project-development information architecture

Its history is mostly root-local:

    80.2% of experiment-touching commits touch experiments without
    another tracked top-level root in the same commit

But CI frequently binds individual experiment directories to selected src/ads_system modules.

This indicates that experiments/ is best understood as:

> a development/evidence lifecycle family containing experiments about multiple owners.

That is a different concept from a subsystem.

R3 should therefore separately consider:

    experiment execution workspace
    durable experiment evidence
    historical completed experiments

They do not necessarily need identical physical treatment.

## 11. frontend/ boundary

frontend/ has unusually strong workspace independence:

    own package.json
    own package-lock.json
    own TypeScript/Vite/Playwright configuration
    CI working-directory = frontend
    416 historical commits
    415 of 416 root-local
    no observed application API/network call in frontend/src

The absence of API calls is significant for current status:

> today's frontend is still primarily an independently qualified product/design surface rather than a tightly integrated production client of src/ads_system.

The directory also mixes:

    product frontend source
    unit tests
    e2e tests
    extensive design-lab artifacts

Therefore two questions are distinct:

    Should a frontend application remain an independent workspace?
        evidence currently says this is plausible

    Should all current frontend design-lab/evidence artifacts remain
    inside the future production frontend application?
        not established

R3 must not confuse workspace independence with permanent internal structure.

## 12. prototype_v0/ boundary and future disposition

prototype_v0/ is the strongest historical-workspace boundary in the repository:

    own pyproject.toml
    own source package
    own tests/configs
    dedicated CI
    95 commits
    100% of those commits root-local
    activity ends before V1 product work
    no observed dependency on current ads_system
    no observed dependency on project-development mechanism

This supports a precise conclusion:

> prototype_v0 is a historically self-contained falsification program.

It does **not** support:

> future prototypes should be top-level self-contained folders named prototype_vN.

R3 should treat its future structural disposition independently from its historical preservation requirement.

Strong candidate dispositions to compare later include:

    preserve current prototype_v0 as frozen historical evidence
    while adopting a different architecture for future prototypes

    archive/move the historical workspace under a dedicated history or
    experiments program during a governed migration

    retain it at root only if cold-clone reproducibility/tooling value
    outweighs root conceptual cost

No disposition is selected in R2.

## 13. docs/ lifecycle

docs/ has 1798 observed commits and remains active throughout the complete recorded project period.

96.0% of docs-touching commits are docs-root-only at the coarse root level.

This does not mean all documentation is independent.

It reflects that the repository deliberately commits:

    research
    decisions
    checkpoints
    state
    evidence
    architecture
    operational knowledge

as first-class durable project work.

docs/ is therefore not merely "documentation about code."

It is an authority/evidence/project-memory layer.

That is why its internal architecture cannot be treated as a normal software-docs afterthought.

At the same time, its current internal root mixes several different conceptual dimensions.

Research 218 remains a child design problem to be revisited after Level-1 architecture selection.

## 14. CI as ownership evidence

The workflow graph reinforces several natural units.

### Independent workspace gates

    frontend/
        self-contained Node build/unit/browser gate

    prototype_v0/
        self-contained Python install/test/benchmark gate

### Product vertical-slice gates

    src/ads_system/
    migrations/
    tests/integration/
    selected schemas/
    selected experiments/

These bind multiple artifact roots into one product capability.

### Repository/project-control gate

    docs/**
    tools/project_knowledge/**
    schemas/project_knowledge/**
    repository governance scripts
    repository governance tests

This binds one conceptual project-development/control plane across several physical roots.

Therefore CI already behaves more **capability-first** than the repository root.

That is important evidence for R3.

## 15. Natural units emerging from R2

Without selecting paths, the evidence supports at least these distinct architectural units or roles:

    A. ADS product/runtime Python system
        strong package/runtime boundary

    B. frontend product/application workspace
        strong build/toolchain boundary
        current internal production-vs-design split unresolved

    C. persistence evolution capability
        strongly owned by ADS product/runtime persistence
        root location conventional rather than conceptually independent

    D. project-development control/knowledge mechanism
        strong independent lifecycle/dependency boundary
        currently artifact-scattered

    E. repository governance / validation
        cross-cutting repository concern
        not identical to D

    F. experimental execution/evidence
        lifecycle family spanning many owners

    G. durable project knowledge / authority / history
        repository-wide memory layer
        not simply product docs

    H. historical prototype programs
        historical evidence/workspaces
        not automatically future architecture

    I. host/CI integration
        repository-host-specific operational layer

    J. schemas and tests
        currently aggregation surfaces rather than natural owners

## 16. Structural implications carried into R3

R2 does not select a tree, but it narrows the candidate space.

Any serious R3 architecture should explain all of the following:

    why frontend is or is not a first-class workspace/application

    why project-development mechanism is distributed or co-located

    how subsystem-local tests differ from repository-wide integration tests

    how subsystem-local schemas differ from repository-wide exchange contracts

    where persistence migrations belong conceptually and physically

    how experiments transition from active executable work to durable evidence

    how historical prototypes are preserved without defining future practice

    how repository-governance tooling differs from subsystem tooling

    how docs/project memory remain first-class without a random flat hierarchy

    how PSMF materialization fits without external runtime authority

## 17. R2 conclusion

The current repository's strongest problem is not merely "too many root folders."

It is:

> several different ownership and lifecycle models are projected into one physical level.

Some current roots are real workspace boundaries.

Some are artifact aggregators.

Some are lifecycle/evidence families.

Some are historical programs.

Some are broad authority/memory layers.

Treating all of them as equivalent peers produces conceptual ambiguity.

The strongest positive finding is that ADS already contains enough lifecycle/dependency evidence to derive better boundaries rather than designing from aesthetics.

R3 should now construct candidate repository architectures around those **natural units and roles**, not around the current folder names.

## 18. Current state

    R0=COMPLETE
    R1=COMPLETE_FOR_CANDIDATE_SYNTHESIS
    R2=COMPLETE
    ROOT_ARCHITECTURE=UNRESOLVED
    NATURAL_BOUNDARIES=IDENTIFIED
    CURRENT_TREE=EVIDENCE_ONLY
    PSMF=INPUT
    PROJECT_DEVELOPMENT_SYSTEM=STRONG_BOUNDARY_CANDIDATE
    FRONTEND_WORKSPACE=STRONG_BOUNDARY_CANDIDATE
    ADS_RUNTIME_PACKAGE=STRONG_BOUNDARY_CANDIDATE
    PERSISTENCE=ADS_RUNTIME_OWNED_CAPABILITY
    TESTS=CROSS_CUTTING_AGGREGATION_SURFACE
    SCHEMAS=CROSS_CUTTING_AGGREGATION_SURFACE
    SCRIPTS=MIXED_EXECUTION_FORM_BUCKET
    EXPERIMENTS=MULTI_OWNER_LIFECYCLE_FAMILY
    PROTOTYPE_V0=HISTORICAL_BOUNDED_PROGRAM
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R3_REPOSITORY_ARCHETYPE_SYNTHESIS
