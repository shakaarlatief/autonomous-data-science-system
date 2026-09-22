# Research 240: PKIA-E01 Whole-Repository Physical Architecture Scope Reset and First-Principles Design Program

**Date:** 2026-09-22
**Status:** OWNER-SCOPE CLARIFICATION RECORDED / WHOLE-REPOSITORY PHYSICAL ARCHITECTURE NOW ACTIVE DESIGN SCOPE / CURRENT TREE IS EVIDENCE ONLY / NO PHYSICAL MIGRATION AUTHORIZED
**Evolution case:** PKIA-E01
**Prior boundary:** Research 236-239 / Checkpoints 567-569
**Frozen baseline still in force:** Research 218 until explicit AO-4 disposition
**Related contracts:** Research 177, Specification 028, Candidate 01 semantic architecture
**Repository base inspected:** 56fa2a08d187534b9b4302b21373d2cd249b8431
**Interaction:** ChatGPT / chatgpt-29 / 29 - Project Knowledge Information Architecture Evolution
**Scope:** Reset the active investigation to the correct level: design the future physical architecture of the entire ADS repository from first principles, with the present repository tree treated as evidence rather than a constraint. PSMF remains an input to this design; Research 218 becomes a child information-architecture problem rather than the parent frame for the whole repository.

## 1. Owner clarification

The owner has explicitly clarified that the redesign must not be constrained to docs/, to Research 218, or to the current tools/project_knowledge/ implementation boundary.

The current ADS repository may be reorganized materially if evidence supports it.

That includes, without presumption:

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
    root configuration files
    current subsystem names
    current package names
    the name project_knowledge

The goal is not to tidy today's tree.

The goal is to determine what a professional, coherent and scalable ADS repository should look like if designed today for long-term growth.

This freedom is stronger than renaming or relocating existing folders. Every current structural concept is challengeable. A current root, subsystem, package, workspace, artifact family, file type, workflow or representation may ultimately be retained, relocated, reorganized internally, split, merged, absorbed into another owner, replaced by a different mechanism, externalized, retired from the active architecture, or preserved only as historical evidence if that is the professionally stronger design.

For example, `prototype_v0/` is not presumed to be the permanent professional pattern for future prototypes merely because it exists as a self-contained folder today. The redesign may conclude that future prototypes should use a different workspace model, live under a governed experiments/program structure, become independent repositories, or follow another architecture entirely. The current `prototype_v0/` still has historical/provenance value and must not be destructively rewritten merely to make the future tree look uniform.

The governing distinction is therefore:

    current artifact existence
        !=
    future architectural requirement

    preserving historical truth/provenance
        !=
    preserving the current representation forever

A future migration may supersede, archive, redirect or transition current carriers while preserving their accepted history and semantic continuity.

## 2. Why this is a scope correction rather than a contradiction

The original owner-approved reopening at Research 235 / Checkpoint 566 required reconsidering Research 218's physical hierarchy from first principles for:

    long-term ADS scale
    professional organization
    future growth
    expected expansion in projects/subsystems/knowledge

Research 236 then correctly moved one level upward to investigate the residency and reuse boundary of the project-development knowledge/control architecture. Research 237-239 produced useful PSMF evidence.

The investigation subsequently narrowed too quickly toward the project-instance-policy home while implicitly leaving the rest of the ADS repository structure fixed.

That narrowing is now corrected.

The PSMF work remains valid, but it is one architectural input inside a larger repository-design problem.

## 3. The current repository tree has no privileged status

The tracked repository root at the inspected base is:

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

Local-only/generated/cache roots such as .venv/, .ads-private/, .tmp/, .pytest_cache/ and frontend dependency/build outputs are not part of the tracked logical target merely because they appear on disk.

The root README currently describes the major tracked areas by operational role. That description is evidence of today's organization, not a freeze on the future architecture.

## 4. The current root mixes multiple organizing principles

The present tree is a hybrid assembled from several different dimensions.

Examples:

    src/
    tests/
    schemas/
    scripts/
    tools/
    migrations/
        mostly artifact-type / technical-role categories

    frontend/
        application / product-surface boundary

    prototype_v0/
        self-contained historical prototype / experiment project

    experiments/
        evidence / development-lifecycle family

    docs/
        broad durable-knowledge and project-memory family

    .github/
        repository-host / CI integration

A hybrid is not inherently wrong.

The open question is whether this particular hybrid is the best long-term architecture for ADS.

The same issue exists recursively inside docs/: artifact/lifecycle families, subsystem/domain homes, governance records and project-knowledge infrastructure currently coexist at the same level.

## 5. Architecture levels must remain distinct

The redesign will explicitly separate at least five levels.

    LEVEL 0  REPOSITORY / SYSTEM TOPOLOGY

        What repositories or independently versioned systems exist?
        ADS public repository
        possible generic framework source
        private companion
        local runtime
        future independently versioned components

    LEVEL 1  ADS REPOSITORY ROOT ARCHITECTURE

        What are the stable top-level categories inside ADS?
        Which things are peers and why?

    LEVEL 2  SUBSYSTEM INTERNAL ARCHITECTURE

        How should a major bounded subsystem organize its own
        implementation, tests, schemas, configuration, documentation,
        adapters and generated state?

    LEVEL 3  INFORMATION / KNOWLEDGE ARCHITECTURE

        Where should durable project knowledge, research, specifications,
        evidence, operational documentation, decisions and history live?

    LEVEL 4  SEMANTIC ARCHITECTURE

        identity
        authority
        relations
        provenance
        lifecycle
        subjects/navigation
        reconstruction

PSMF mainly informs Levels 0 and 2.

The present whole-repository investigation is primarily Level 1, with consequences for Levels 2 and 3.

Research 218 is primarily a Level-3 physical information architecture and is therefore now a child problem of the broader repository architecture.

Candidate 01's deeper semantic contracts are Level 4 and remain preserved unless independently challenged by evidence.

## 6. The tools/project_knowledge example

The current project-development knowledge/control subsystem is physically distributed.

    tools/project_knowledge/
    schemas/project_knowledge/
    docs/project_knowledge/
    tests/...project_knowledge...
    experiments/project_knowledge_...
    scripts/research/...project_knowledge...

This is an artifact-first organization:

    artifact type
        ->
    subsystem

It is a legitimate professional pattern.

A competing pattern is subsystem-first organization:

    subsystem
        ->
    implementation
    tests
    schemas
    configuration
    documentation
    adapters
    generated state

A third possibility is a conventional monorepo split such as applications/packages/tooling/infrastructure, and a fourth is a deliberate ADS-specific hybrid.

No option is selected yet.

The fact that tools/ currently contains only project_knowledge/ is evidence worth considering; it does not prove that tools/ should disappear.

## 7. Names are also open

The name project_knowledge is not frozen as the permanent name of the subsystem.

Its current responsibility has expanded beyond knowledge storage/navigation into areas such as:

    semantic identity
    authority resolution
    reconstruction
    activation/orchestration
    workstreams
    capture/promotion
    architecture evolution
    Git lifecycle
    interaction continuity/recovery
    collaboration routing
    control obligations

A future name must follow the final responsibility boundary rather than drive it.

Likewise, names such as tools/, schemas/, docs/, experiments/, frontend/ and prospective names such as systems/, packages/, apps/, platform/, knowledge/ or engineering/ are candidates only until their semantics are justified.

## 8. Design families to compare

At minimum, the repository-level study must compare serious architecture families rather than merely prettier folder trees.

### A. Conventional artifact-first repository

    src/
    tests/
    docs/
    tools/
    schemas/
    scripts/
    migrations/
    experiments/
    ...

Subsystems are distributed beneath artifact-type roots.

### B. Subsystem-first / vertical repository

    systems/
        subsystem_a/
            implementation/
            tests/
            schemas/
            docs/
        subsystem_b/
            ...

Major independently evolving systems are physically co-located.

### C. Monorepo-style applications/packages/tooling split

Conceptually:

    apps/
    packages/
    tooling/
    infrastructure/
    research/
    docs/
    ...

Deployable applications, reusable packages and repository support have different roots.

### D. Deliberate ADS-specific hybrid

Stable conceptual categories are derived from ADS responsibilities rather than copied from a generic software-monorepo convention.

### E. Multi-repository boundary variants

Some concerns may ultimately deserve independent repositories or distributions, but repository extraction must be justified by lifecycle/authority/dependency evidence rather than aesthetic separation.

PSMF is one such topology candidate for the generic project-development framework source.

These families are starting points, not an exhaustive frozen taxonomy.

## 9. Evaluation criteria

Each candidate must be evaluated against the actual and future ADS system.

At minimum:

    conceptual coherence
    clear ownership
    clear dependency direction
    lifecycle independence
    co-change locality
    human discoverability
    AI-agent reconstructability
    predictable authoring/placement rules
    tooling/ecosystem compatibility
    Python packaging
    frontend tooling
    test discovery
    schema ownership
    database migration ownership
    CI ergonomics
    generated/local artifact handling
    Git provenance
    authority preservation
    PSMF materialization compatibility
    future extraction/reuse
    project self-containment
    private/public boundaries
    historical preservation
    migration cost
    ability to scale to many future components
    ability to scale to many future projects/workstreams
    ability to explain the repository to a new contributor without hidden conventions

A visually neat tree is insufficient if the ownership model is poor.

A conventional tree is insufficient if it scatters strongly cohesive subsystems without benefit.

A subsystem-first tree is insufficient if it fights language/build tooling or creates duplicated infrastructure.

## 10. Future-growth stress cases

The target must be tested against more than today's repository.

At minimum:

    ADS with many additional product capabilities
    multiple frontend/product surfaces
    larger backend/application/domain/platform layers
    more deployment/runtime integrations
    more methodological knowledge
    more governed experiments
    more substantial project-control machinery
    PSMF local materialization
    multiple project-specific framework extensions
    future private/local companion responsibilities
    historical prototypes that must remain evidence but not active architecture
    possible independent packages/services
    new contributors and AI agents reconstructing the project cold

Temporary project stages must not become the primary physical hierarchy merely because they are visible today.

## 11. Ordered design program

The active work sequence is now:

    PHASE R0  CURRENT REPOSITORY INVENTORY

        inventory tracked root families
        identify logical owners
        separate tracked architecture from local/generated artifacts
        identify packaging/build/test/deployment boundaries

    PHASE R1  RESPONSIBILITY CLASSIFICATION

        ignore current folder names temporarily
        classify major ADS concerns by what they actually are:
            application/product
            reusable library
            platform capability
            development infrastructure
            project-control subsystem
            experiment/evidence
            durable knowledge
            operational infrastructure
            repository tooling
            deployment/configuration
            integration
            historical artifact

    PHASE R2  LIFECYCLE / DEPENDENCY / CO-CHANGE ANALYSIS

        determine which concerns genuinely evolve together
        determine package/runtime/deployment boundaries
        identify accidental versus natural coupling

    PHASE R3  REPOSITORY ARCHETYPE CANDIDATES

        construct serious artifact-first, subsystem-first,
        monorepo-style and ADS-specific candidates

    PHASE R4  STRESS TEST / PROFESSIONAL PATTERN REVIEW

        test against current ADS and future-growth scenarios
        use external professional patterns as evidence where useful
        do not copy a convention merely because it is common

    PHASE R5  ROOT-ARCHITECTURE SELECTION

        determine the target Level-1 repository architecture

    PHASE R6  SUBSYSTEM BOUNDARIES

        place the PSMF materialized project-development system
        decide whether it is self-contained or distributed
        determine project-instance-policy ownership
        decide naming only after responsibility is clear

    PHASE R7  INFORMATION-ARCHITECTURE REDESIGN

        reconsider Research 218 inside the selected repository architecture
        derive the durable knowledge hierarchy
        reconsider current docs root/families/subsystem homes
        preserve semantic natural ownership without assuming flat physical peers

    PHASE R8  GOVERNED DISPOSITION / MIGRATION PROGRAM

        KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN affected contracts
        reconcile Research 177, Research 218, Specification 028 and AO dependencies
        only then design and execute physical migration

The phases may expose dependencies requiring bounded iteration. They are a reasoning order, not permission for premature moves.

## 12. What is explicitly not happening yet

    no root directory moves
    no docs hierarchy moves
    no package renames
    no project_knowledge rename
    no generic framework repository creation
    no PSMF extraction
    no framework/vendor directory
    no Research 218 replacement tree
    no authority switch
    no AO-10 implementation
    no W5-F0 resume

The current repository remains operationally authoritative while its future architecture is investigated.

## 13. Status of PSMF and G1

Research 239 remains valid.

    PSMF
        leading topology hypothesis for generic-source <-> project-instance
        relationship

    G1
        PASS
        lifecycle independence empirically supported

    owner acceptance
        NOT YET

    mechanism extraction
        NOT JUSTIFIED NOW

PSMF must be integrated into the eventual whole-repository design rather than used to pre-decide it.

## 14. EvolutionCase scope

For continuity, the existing case identity PKIA-E01 is retained.

Its active affected-scope investigation is now broader:

    PRIMARY ACTIVE DESIGN SCOPE
        whole ADS repository physical architecture

    CHILD SCOPE
        Research 218 information architecture

    RELATED SCOPE
        Research 177 project-support-code boundary
        Specification 028 physical implementation assumptions
        PSMF local materialization boundary
        repository root conventions documented in README/pyproject/tooling

    PRESERVED UNLESS INDEPENDENTLY CHALLENGED
        deeper Candidate 01 semantic identity/authority/relation principles

If later evidence shows that a root-level concern is genuinely unrelated to this EvolutionCase, it may be split into its own governed case rather than being forced into PKIA-E01.

## 15. Current state

    PKIA_E01=OPEN
    ACTIVE_SCOPE=WHOLE_ADS_REPOSITORY_PHYSICAL_ARCHITECTURE
    CURRENT_TREE=EVIDENCE_NOT_TARGET
    PSMF=LEADING_TOPOLOGY_INPUT
    G1=PASS
    OWNER_ACCEPTED_TARGET=NO
    RESEARCH218=FROZEN_BASELINE_RETAINED
    RESEARCH218_ROLE=CHILD_INFORMATION_ARCHITECTURE_PROBLEM
    RESEARCH177=UNCHANGED
    SPECIFICATION028=UNCHANGED
    INSTANCE_POLICY_HOME=DEFERRED_UNTIL_REPOSITORY_ARCHITECTURE
    ROOT_ARCHITECTURE=UNRESOLVED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    W5_F0=PAUSED
    AO10=HELD
    AUTHORITY_SWITCH_ALLOWED=false
    NEXT=R0_CURRENT_REPOSITORY_INVENTORY_AND_R1_RESPONSIBILITY_CLASSIFICATION
