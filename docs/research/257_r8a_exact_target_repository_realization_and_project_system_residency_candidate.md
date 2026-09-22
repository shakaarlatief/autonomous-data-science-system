# Research 257: R8-A Exact Target Repository Realization and Project-System Residency Candidate

**Date:** 2026-09-22
**Status:** R8-A EXACT TARGET REALIZATION RECOMMENDED / OWNER DECISION REQUIRED / REPRESENTATION AND FILE-LEVEL MIGRATION HELD / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Accepted architecture basis:** Research 248-256
**Repository base:** 1d91d0dbed289cad7cc0ce06a4268a685910ff87
**Scope:** Convert the accepted Product/Project, bounded-context, Project-system and Project-information architecture into an exact target repository/workspace layout before any current-file disposition or physical migration. Reconcile the accepted activation/orchestration architecture into the target Project Development System without changing its semantic contracts.

## 1. R8-A design rule

R8-A selects physical ownership and workspace boundaries.

It does not yet select every persistence representation.

Choosing project/system/ as the owner of Project-control state does not imply that every logical control record becomes one JSON file, one Markdown file, one SQLite row, one graph node, or one event-store event.

AO-3 deliberately left those representation questions open.

The next R8 representation stage must select persistence form per responsibility before migration.

## 2. Recommended exact tracked repository root

Target root:

    .github/
    .gitignore
    .python-version
    README.md
    project_anchor.json
    pyproject.toml
    uv.lock
    product/
    project/

Tracked first-level target count:

    9

Preregistered review bound from Research 249:

    12

Result:

    ROOT_PRESSURE=PASS

No named A1 root integration contract is required.

### 2.1 Root responsibilities

    .github/
        repository-host integration only

    .gitignore
        repository/tool-required ignore contract

    .python-version
        repository-wide Python toolchain anchor while Product runtime and
        Project system share the same supported Python line

    README.md
        human cold-start entry

    project_anchor.json
        stable machine-readable Project cold-start anchor
        contains locators, not unique substantive Project truth

    pyproject.toml
        repository-level Python workspace orchestration only

    uv.lock
        repository-level shared Python workspace lock while one lock remains
        operationally justified

    product/
        accepted Product plane

    project/
        accepted Project plane

If future tooling requires an additional true-root anchor, adding it must be justified against the accepted root contract and 12-entry review bound.

## 3. Python workspace topology

R8-A recommends one repository-level uv workspace with two Python package workspaces:

    product/runtime/
    project/system/

The root pyproject owns workspace orchestration.

Package metadata moves to the owning workspace.

The root does not remain the Product Python package merely because it is one today.

### 3.1 Product runtime package

Target:

    product/runtime/
        pyproject.toml
        alembic.ini
        migrations/
        src/
            ads_system/
        tests/

The Python import/package name ads_system is retained unless later evidence independently justifies a package rename.

Reason:

The package name still describes the ADS Product system and renaming it would create broad import churn without improving the accepted bounded-context architecture.

### 3.2 Project Development System package

Target:

    project/system/
        README.md
        pyproject.toml
        src/
            ads_project_system/
        contracts/
            schemas/
        instance/
            policy/
            control/
            captures/
        generated/
        tests/

Package/import target:

    ads_project_system

The local README is a workspace bootstrap/command surface only.

Durable rationale, normative architecture and operating procedures remain under Project knowledge according to R7 A3.

## 4. Product plane target

Recommended target:

    product/
        README.md

        runtime/
            pyproject.toml
            alembic.ini
            migrations/
            src/
                ads_system/
                    project_intelligence/
                    methodological_knowledge/
                    evidence_provenance/
                    reasoning/
                    execution/
                    runtime_platform/
            tests/

        interaction/
            README.md
            web/
                package.json
                package-lock.json
                <tool configuration>
                src/
                e2e/

## 4.1 Product runtime internal contexts

The Product runtime becomes a modular monolith organized primarily by accepted bounded context rather than by one repository-wide application/domain/infrastructure split.

Target modules:

    project_intelligence/
        PC1

    methodological_knowledge/
        PC2

    evidence_provenance/
        PC3

    reasoning/
        PC4

    execution/
        PC5

    runtime_platform/
        PC7

Each context may internally use domain/application/ports/adapters where that improves the context.

The repository does not impose one global domain/, one global application/, or one global infrastructure/ as the primary architecture.

Provider/storage/framework dependencies must remain outward from the semantic contexts.

## 4.2 Product Interaction workspace family

Current strong member:

    product/interaction/web/

Future client surfaces may become siblings only when independently justified.

No empty future workspace is created merely to reserve a name.

A backend API transport does not automatically become a separate interaction workspace. It remains with the runtime unless independent build/deploy/lifecycle evidence justifies extraction.

## 5. Project plane target

Recommended target:

    project/
        README.md

        system/
            <JW1 Project Development System workspace>

        engineering/
            checks/
            tests/
            tooling/

        research/
            README.md
            <active bounded research execution workspaces>

        reproductions/
            README.md
            <preserved executable reproduction packages>

        knowledge/
            README.md

            governance/
                direction/
                architecture/
                    rationale/
                    specifications/
                decisions/
                planning/

            evidence/
                research/
                qualification/
                provenance/

            operations/
                engineering/
                    repository/
                    environments/
                    verification/
                    security/
                    release/
                    recovery/
                collaboration/

            history/
                milestones/

## 5.1 project/engineering/

This is the executable JC4 repository-engineering surface.

It is not a Python package by default.

    checks/
        repository-wide deterministic validators/check entrypoints

    tests/
        cross-workspace integration/system/repository qualification

    tooling/
        bounded repository/build/release engineering helpers that do not
        belong to Product or JW1

If reusable executable engineering code becomes substantial, a dedicated workspace/package requires a later architecture decision.

A generic scripts/ bucket is not retained.

## 5.2 project/research/

This is active JC3 execution, not durable research evidence.

It may contain bounded program workspaces with code, fixtures, harnesses, local manifests and reproducibility assets.

Durable results/protocols that constitute Project information belong under project/knowledge/evidence/research/, project/knowledge/evidence/qualification/ or project/knowledge/evidence/provenance/.

The universal current experiments/ root is not retained.

## 5.3 project/reproductions/

Purpose:

    preserved executable artifacts whose continuing value is exact
    reproducibility/reconstruction

Examples may include a retained historical prototype or an experiment reproduction package.

This is deliberately narrower than archive/, old/ or legacy/.

It must not become a dumping ground for stale code.

Human historical records remain under project/knowledge/history/.

## 6. Operations/engineering subarea freeze

Research 255 A4 requires the first-level Operations/engineering model and a review bound before population.

Accepted candidate subareas:

    repository/
        workspace/build/toolchain/CI/repository operation

    environments/
        local development/test/research environment operation,
        bridges and environment diagnostics

    verification/
        how project/product qualification is executed and interpreted

    security/
        secure development, dependency/supply-chain, secrets and
        vulnerability-response procedures

    release/
        release/version/change/configuration/promotion procedures

    recovery/
        break-glass, incident, backup/recovery and development-continuity
        procedures

Preregistered direct-subarea review bound:

    OPERATIONS_ENGINEERING_DIRECT_SUBAREA_REVIEW_BOUND = 8

Frozen initial direct-subarea count:

    6

Rule:

    7th or 8th direct subarea
        requires explicit justification and proof that it does not fit an
        existing stable responsibility

    >8
        triggers AO-4 architecture review before authoring

This is a review bound, not a requirement to fill unused slots.

## 7. Machine and human cold-start realization

### 7.1 Human

Root README.md must link directly to:

    current Project orientation
    project/README.md
    project/knowledge/README.md

Recommended generated human orientation:

    project/system/generated/orientation/current.md

This is derived and contains no unique accepted truth.

### 7.2 Machine

Root project_anchor.json is the one stable machine-readable cold-start anchor.

It should locate at minimum:

    Project-system workspace
    current Project routing/control source
    generated machine orientation
    current authority regime / authority locator
    schema/version needed to interpret the anchor

Recommended generated machine orientation:

    project/system/generated/orientation/current.json

Recommended canonical Project control/routing area:

    project/system/instance/control/

The exact internal control record schema remains a representation-stage decision.

### 7.3 Accepted hop gate realization

The target paths can satisfy Research 255 A5:

    root README -> current orientation
        1 direct link

    root README -> Project knowledge root
        1 direct link

    root README -> primary knowledge class
        root README -> knowledge README -> class
        2 links

    root README -> governing architecture/current authority
        <=3 links through explicit curated/generated navigation

    project_anchor.json -> routing/authority locator
        same anchor read

    project_anchor.json -> current generated orientation
        <=1 additional repository read

Exact link qualification must be executed before path freeze/cutover.

## 8. Project Development System internal architecture

The target package ads_project_system must reflect accepted semantic/control responsibilities rather than the historical project_knowledge package name.

Recommended source modules:

    semantics/
        declarations
        identity
        authority
        scope
        typed relations
        revision/provenance semantics

    reconstruction/
        task classification
        reconstruction planning
        governing-source closure
        freshness/availability receipts

    activation/
        project-event interpretation
        Progressive Control Closure
        risk/reopen-trigger activation
        action/output-shape re-entry
        activation-miss observability

    orchestration/
        workstreams
        process routing
        collaboration routing
        obligation realization
        Git lifecycle policy integration

    evolution/
        AO-4 EvolutionCase classification
        KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN control

    continuity/
        interaction continuity
        interruption/resume
        independent recovery
        break-glass routing

    preservation/
        capture
        review
        promotion
        provenance retention

    views/
        deterministic generated indexes
        current orientation
        subject/navigation projection
        freshness/manifest logic

    migration/
        compatibility shadows
        successor bridge support
        migration audit
        cutover/rollback support

    adapters/
        Git
        filesystem
        collaboration/provider
        local-runtime/tool integration

These are module-responsibility boundaries, not mandatory one-file-per-concept rules.

## 9. Activation/orchestration reconciliation

The whole-repository redesign does not supersede the AO conceptual architecture.

The following remain accepted design inputs to JW1:

    AO-3 Progressive Control Closure
    AO-4 governed architecture evolution
    AO-5 anchored interaction continuity / independent recovery
    AO-6 purpose-bound Git lifecycle
    AO-7 Authority-Preserving Successor Bridge
    AO-8 reconciled independent review findings
    AO-9 historical regression evidence
    P7-D01 consequential output/action-shape re-entry
    KA-R51 control-miss / owner-reminder observability
    KA-R52 accepted-MUST realization traceability

The new architecture changes their residency and representation problem, not their accepted semantics.

Conceptual mapping:

    AO-3
        -> activation/ + reconstruction/ + orchestration/

    AO-4
        -> evolution/

    AO-5
        -> continuity/

    AO-6
        -> orchestration/ + adapters/git

    AO-7
        -> migration/ + activation/orchestration boundary

    KA-R51
        -> activation observability + qualification evidence

    KA-R52
        -> orchestration obligation-realization traceability

## 10. AO-10 sequencing

AO-10 remains held at this R8-A boundary.

Reason:

AO-10 must implement and qualify a chosen control-evidence representation.

R8-A selects the target workspace and module ownership but deliberately does not yet decide file-backed versus database-backed Project control state, exact EventInterpretation persistence, exact AuthorityReceipt representation, exact ActionContract representation, exact BridgeReceipt representation, exact interaction-envelope persistence, exact obligation-realization ledger/index representation, or exact activation-miss evidence representation.

Therefore R8 representation architecture must precede AO-10 implementation.

AO-10 should resume only after Project-system representation classes are selected, Specification 028 deltas are known, compatibility/shadow paths are defined and current authority fallback paths are explicit.

## 11. Representation boundary

R8-A preserves the following already accepted constraints:

    Git remains durable Project-development authority unless explicitly
    superseded later

    Project knowledge may use rich human-reviewable carriers

    declaration instances remain carrier-resident

    generated views contain no unique accepted truth

    optional graph/vector/SQL indexes may be derived caches

    no graph/vector/SQL store gains authority merely because it improves
    retrieval or traversal

But R8-A does not freeze one universal representation for Project knowledge, Project-system control state, generated views, receipts, indexes or research evidence.

The next R8 stage must perform that responsibility-by-responsibility decision.

## 12. Current root disposition implied by target

Prospective mapping only:

    current src/
        -> product/runtime/src/

    current migrations/ + alembic.ini
        -> product/runtime/

    current frontend/
        -> product/interaction/web/ for promoted Product implementation,
           with design/research/history split later

    current tools/project_knowledge/
        -> project/system/src/ads_project_system/ after detailed mapping

    current schemas/project_knowledge/
        -> project/system/contracts/schemas/

    current scripts/
        -> split among project/engineering, project/system, project/research,
           or retire

    current tests/
        -> split among Product runtime, Product interaction, Project system,
           project/engineering and active research

    current experiments/
        -> project/research while active, then promote/reproduce/retire

    current prototype_v0/
        -> project/reproductions only if executable preservation remains
           justified

    current docs/
        -> Project knowledge/system mapping under R7/R8; no wholesale move

No file is moved by this research.

## 13. Root workspace tooling rationale

Root pyproject.toml remains only because repository-wide Python workspace orchestration is a legitimate A2 true-root responsibility.

Target intent:

    root pyproject
        uv workspace orchestration
        repository-wide Python toolchain constraints only

    product/runtime/pyproject
        Product package metadata/dependencies/build

    project/system/pyproject
        Project Development System package metadata/dependencies/build

    uv.lock
        shared repository Python dependency resolution while justified

The exact uv syntax/configuration must be validated before migration.

The Node web workspace remains independently package-managed under product/interaction/web/.

No repository-root npm workspace is created for a single current JS workspace.

## 14. Dependency invariants

Enforce:

    product/runtime
        MUST NOT import project/system

    product/interaction
        MUST NOT import project/system

    project/system
        MAY inspect/use Product contracts for development governance but must
        not become a Product runtime dependency

    project/engineering
        MAY invoke/qualify both Product and Project workspaces

    project/research
        MAY depend on bounded Product/Project targets for experiments

    project/knowledge
        is information, not an importable runtime dependency

Repository tests must eventually encode the first two as fail-closed architecture checks.

## 15. Exact-target falsifiers

R8-A must reopen/amend if detailed migration discovers:

    a Product runtime dependency that genuinely requires Project-system state

    more than 12 justified tracked true-root entries

    Project-system code that cannot be separated from Product runtime without
    semantic distortion

    a persistent cross-plane contract that cannot resolve by split or
    asymmetric ownership

    operations/engineering repeatedly exceeding its 8-subarea bound

    cold-start hop gates cannot be met without duplicating authority

    the proposed Python workspace split requires circular package dependencies

    the representation stage proves one of the selected physical areas is the
    wrong ownership boundary

## 16. Recommended owner disposition

Recommended:

    ACCEPT

Meaning:

    accept the exact root/product/project/workspace layout in this research
    as the R8 target realization baseline

    accept ads_project_system as the target local JW1 package identity

    accept the Product modular-runtime module map

    accept project/engineering, project/research and project/reproductions
    as non-knowledge Project execution areas

    accept the six operations/engineering subareas and review bound 8

    accept the cold-start target paths

    accept activation/orchestration residency under JW1

    do NOT yet select universal persistence/storage representation

    do NOT authorize physical migration

If accepted, the next R8 stage must decide the authoritative/derived persistence representation per information/control class and produce the Specification 028 representation/path delta before file-level migration planning.

## 17. Current state

    R8A_EXACT_TARGET=RECOMMENDED
    TARGET_ROOT_ENTRIES=9
    ROOT_BOUND=12
    ROOT_PRESSURE=PASS

    PRODUCT_RUNTIME=product/runtime
    PRODUCT_INTERACTION_WEB=product/interaction/web

    PROJECT_SYSTEM=project/system
    PROJECT_SYSTEM_PACKAGE=ads_project_system
    PROJECT_ENGINEERING=project/engineering
    PROJECT_RESEARCH_EXECUTION=project/research
    PROJECT_REPRODUCTIONS=project/reproductions
    PROJECT_KNOWLEDGE=project/knowledge

    OPERATIONS_ENGINEERING_SUBAREAS=6
    OPERATIONS_ENGINEERING_REVIEW_BOUND=8

    AO3_AO9_SEMANTICS=RETAINED
    AO10=HELD_PENDING_R8_REPRESENTATION_RECONCILIATION

    REPRESENTATION_ARCHITECTURE=UNRESOLVED_NEXT
    FILE_LEVEL_MIGRATION=HELD
    SPECIFICATION028=UNCHANGED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    OWNER_DECISION=PENDING
    NEXT=OWNER_R8A_EXACT_TARGET_DECISION
