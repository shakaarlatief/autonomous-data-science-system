# Research 252: R6-B Current-to-Target Mapping and Structural Disposition Matrix

**Date:** 2026-09-22
**Status:** R6-B FAMILY-LEVEL MAPPING COMPLETE / R7 INFORMATION-ARCHITECTURE DESIGN UNBLOCKED / FILE-LEVEL MIGRATION MANIFEST DEFERRED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Accepted architecture basis:** Research 248-251
**Repository base:** 39a5f8f66d78a1c355c3300d110d24121f796deb
**Scope:** Map the present repository into the accepted from-scratch Product/Project bounded-context architecture after, not before, that target architecture was derived. This mapping classifies current material by future responsibility and disposition without preserving current folders as architectural units.

## 1. Method

R6-B follows the accepted derive-before-map rule.

The target responsibility/context model was frozen in Research 249-250 and owner-accepted in Research 251 before this mapping began.

Therefore this document may now inspect current folders, but only to answer:

    What responsibility does this existing material actually serve?
    Does the current container correspond to one target owner?
    Must the current container split?
    Is it active product implementation, project infrastructure,
    research/evidence, or historical material?
    Should its current representation survive at all?

It may not infer:

    current folder exists -> future folder must exist

## 2. Mapping dispositions

R6-B uses these descriptive dispositions:

    DIRECT_FIT
        current material largely corresponds to one accepted target owner

    INTERNAL_RESTRUCTURE
        same higher-order owner, but current internal boundaries should be
        redesigned

    SPLIT
        current container mixes multiple accepted owners/lifecycles

    MERGE
        current material is better absorbed with another target owner

    PROMOTE_TO_FIRST_CLASS_WORKSPACE
        current material is currently treated as helper/support code but
        belongs to an accepted workspace

    PROJECT_EVIDENCE
        material documents/researches/qualifies the product/project rather
        than being runtime product content

    HISTORICAL_ONLY
        preserve historical truth/reproducibility without active-peer status

    RETIRE_OR_REPLACE
        current representation has no presumed future role

    TOOL_ROOT_CANDIDATE
        current root placement may remain only if accepted true-root rules
        require it

    R7_REQUIRED
        final project information placement depends on R7

    R8_REQUIRED
        exact path/file migration mechanics depend on R8

These are target-mapping classifications, not filesystem operations.

## 3. Current repository root mapping

### 3.1 .github/

Current role:

    GitHub workflows and repository-host integration

Target:

    TRUE ROOT / repository-host integration
    semantics primarily JC4 Engineering/Verification/Delivery
    contribution surfaces may also implement JC5 Collaboration

Disposition:

    DIRECT_FIT at true root because GitHub assigns path semantics

Internal workflow ownership should still be classified by the workspace/context they qualify.

### 3.2 src/ads_system/

Current role:

    active Python Product implementation

Target:

    PW1 Core Product Runtime Workspace

Disposition:

    PROMOTE/ABSORB INTO PW1
    INTERNAL_RESTRUCTURE by PC1-PC5/PC7 boundaries

The current package name and internal application/domain/infrastructure layering are not automatically preserved.

### 3.3 frontend/

Current role:

    TypeScript/Vite Product interface plus extensive design-lab evidence

Target split:

    production/client implementation
        -> PC6 / PW2 Product Interaction workspace family

    product-interface unit/e2e qualification
        -> PW2-local verification plus JC4 for cross-workspace acceptance

    design-lab studies and unpromoted candidates
        -> JC3 Research/Qualification

    superseded/important visual implementations
        -> JC6 Historical Preservation when long-term retention is justified

Disposition:

    SPLIT

The current frontend container must not be migrated wholesale as one future workspace.

### 3.4 migrations/

Current role:

    Alembic schema evolution for Product persistence

Target:

    PC7 inside PW1 persistence realization

Disposition:

    DIRECT_FIT in responsibility
    RELOCATE/INTERNAL_RESTRUCTURE physically later

Root placement has no independent architectural claim.

### 3.5 tools/project_knowledge/

Current role:

    executable project-development control/knowledge machinery

Target:

    JC2 / JW1 Project Development System Workspace

Disposition:

    PROMOTE_TO_FIRST_CLASS_WORKSPACE
    INTERNAL_RESTRUCTURE

The generic tools/ parent has no future presumption.

The current project_knowledge name has no future presumption.

Within JW1, later PSMF work must distinguish:

    materialized generic mechanism
    ADS instance policy/extensions
    project-local control state
    compatibility/migration adapters
    generated views
    framework lineage

### 3.6 schemas/

Current role:

    artifact-type aggregation of unrelated machine contracts

Target split:

    schemas/project_knowledge/**
        -> JW1 / JC2 contracts

    reusable_knowledge_bundle_v1.schema.json
        -> PC2 Methodological Knowledge product contract

    model_collaboration_thread_state_v1.schema.json
        -> JC5 collaboration semantic contract
           implementation/validation may be provided by JW1 or JC4

Disposition:

    SPLIT

No universal repository schemas/ owner is retained.

### 3.7 tests/

Current role:

    repository-wide aggregation of tests for Product, Project system,
    experiments and repository governance

Target split:

    Product context unit/contract tests
        -> PW1 alongside owning Product modules

    Product interaction unit/e2e tests
        -> PW2

    Project-development-system unit/contract tests
        -> JW1

    cross-workspace Product integration/system tests
        -> JC4 qualification surface

    repository-integrity/project-governance tests
        -> JC4

    experiment harness tests
        -> JC3 active research workspaces while active

Disposition:

    SPLIT

One universal target tests/ directory is not retained by default.

### 3.8 scripts/

Current role:

    mixed executable helper bucket

Target split:

    repository integrity/routing/checkpoint validators
        -> JC4 Engineering/Verification/Delivery

    project-development-system operations
        -> JW1 where they operate JC2

    collaboration validators
        -> JC5 semantics / JC4 or JW1 implementation

    experiment launch/research utilities
        -> JC3 active research workspace or historical evidence

    Cockpit verification selectors
        -> JC3/JC4 depending whether design-study or release qualification

    obsolete one-off migration/probe utilities
        -> JC6 historical or RETIRE_OR_REPLACE after evidence retention review

Disposition:

    SPLIT / RETIRE_OR_REPLACE

"Script" ceases to be an ownership category.

### 3.9 experiments/

Current role:

    active and completed experimental programs spanning Product and
    Project-system questions

Target:

    JC3 Research and Qualification during active experiment lifecycle

Upon completion:

    promoted mechanism
        -> owning Product/Project workspace

    load-bearing executable reproduction
        -> JC3/JC6 preserved reproduction unit

    accepted durable result/provenance
        -> R7 project evidence architecture

    obsolete/non-load-bearing execution shell
        -> retire after preservation review

Disposition:

    SPLIT BY LIFECYCLE
    RETIRE universal permanent experiments/ root as target assumption

### 3.10 prototype_v0/

Current role:

    historically self-contained falsification program

Target:

    JC6 Historical Preservation
    with accepted quantitative evidence linked through JC3

Disposition:

    HISTORICAL_ONLY as an active-architecture classification

The current workspace may remain byte-preserved/reproducible during migration if required, but future prototypes do not inherit this root pattern.

### 3.11 docs/

Current role:

    broad aggregation of project authority, product architecture,
    research/evidence, implementation provenance, operations, generated
    project-control state and historical material

Target:

    SPLIT BY SEMANTIC OWNER and lifecycle

Disposition:

    SPLIT / R7_REQUIRED

The current docs/ tree is not retained as the future information architecture by default.

## 4. Current Product implementation mapping

### 4.1 src/ads_system/application/

Current files include context selection, methodological horizon, knowledge interchange, reasoning, retrieval and Source Universe application services.

Target mapping:

    horizon/context_selection/context_models/horizon_models
        -> primarily PC1 Project Intelligence
           consuming PC2 Methodological Knowledge

    retrieval
        -> PC2 query/application behavior
           with PC7 retrieval mechanism adapters where technical

    knowledge_interchange
        -> PC2-owned interchange contract/application behavior

    reasoning
        -> PC4 Reasoning Orchestration

    source_manifest/source_universe
        -> PC3 Evidence/Artifact Provenance

    ports
        -> split by owning PC contract

Disposition:

    INTERNAL_RESTRUCTURE

The present application layer is useful implementation evidence, not the final context decomposition.

### 4.2 src/ads_system/domain/

Current:

    general models
    source_universe models

Target:

    general project/intelligence models
        -> PC1

    source/evidence models
        -> PC3

Disposition:

    SPLIT INTERNALLY BY CONTEXT

A single generic domain/models.py should not become a future catch-all.

### 4.3 src/ads_system/infrastructure/

Current:

    interchange/
    persistence/
    retrieval/
    runtime/
    source_store.py

Target:

    technical mechanisms primarily -> PC7

with adapters implementing inward contracts owned by:

    PC2 knowledge
    PC3 provenance
    PC4 reasoning
    PC1 state/persistence

Disposition:

    INTERNAL_RESTRUCTURE

"Infrastructure" may remain a code-layer concept inside PW1, but it is not a semantic bounded context and must not absorb product meaning.

### 4.4 source_cli.py

Target:

    PC6 Product Interaction and Access if it is a user/operator product CLI

or:

    JC4 if it proves to be only a development/admin command

Disposition:

    CONTESTED / contract test required during detailed mapping

The command's intended external contract, not its current location, decides ownership.

## 5. Current Product Interaction mapping

### 5.1 frontend/src/

Target:

    PC6 / PW2

Disposition:

    DIRECT_FIT at responsibility level
    INTERNAL_RESTRUCTURE allowed from scratch

No current component/page/cockpit concept is protected.

### 5.2 frontend/e2e/

Target:

    PW2-local interface qualification
    plus JC4 cross-workspace acceptance where backend/runtime behavior is involved

Disposition:

    SPLIT BY TEST SCOPE

### 5.3 frontend/design-lab/

Target:

    JC3 for active/unpromoted design research
    JC6 for selected historical fidelity sources
    PC6/PW2 only for mechanisms explicitly promoted into product implementation

Disposition:

    SPLIT

The design-lab is not production Product merely because it is under frontend/.

## 6. Current Project Development System mapping

### 6.1 tools/project_knowledge core

Target:

    JC2 / JW1

Likely generic-framework candidates, still subject to PSMF qualification:

    semantic identity/transitions
    declaration validation
    authority resolution
    workstream graph
    normalized scope
    capture/promotion mechanics
    deterministic view/provenance mechanics

Likely ADS-instance/project-specific material:

    current ADS profiles
    repository path/discovery policy
    current authority vocabulary
    current view set
    project-specific lifecycle states
    ADS repository integration

Likely migration/compatibility adapters:

    current routing / CURRENT_STATE / KNOWLEDGE_MAP compatibility
    W0-W8 migration support
    temporary old/new carrier support

Disposition:

    INTERNAL_RESTRUCTURE inside JW1
    PSMF genericity split remains future governed work

### 6.2 schemas/project_knowledge/

Target:

    JW1 local contracts

Disposition:

    DIRECT_FIT responsibility
    future generic versus ADS-instance schema split remains open

### 6.3 project-knowledge tests

Target:

    JW1 local tests for core/system contracts
    JC4 only for repository-wide integration/acceptance gates

Disposition:

    SPLIT BY TEST SCOPE

### 6.4 docs/project_knowledge/

Current structure includes:

    architecture/
    captures/
    generated/
    project_integration_boundary.md
    selected_architecture_workstream.md

Target split:

    architecture rationale/accepted project architecture
        -> JC1 / R7

    executable/generated project-control views
        -> JC2/JW1 generated-state boundary

    live captures/control state
        -> JC2/JW1

    historical captures/transitions if inactive
        -> JC6 / R7 historical evidence

    migration evidence
        -> JC3/JC6 depending role

Disposition:

    SPLIT

The current project_knowledge folder does not survive as one required target container.

## 7. Current Project information mapping

This section maps current information families to responsibility contexts only. R7 determines the future hierarchy.

### Root project documents

    VISION.md
    PRINCIPLES.md
    DEVELOPMENT_METHOD.md
    DECISIONS.md
    OPEN_QUESTIONS.md
    OPEN_ARCHITECTURE_BACKLOG.md
    CURRENT_STATE.md
    CONTINUITY.md
    KNOWLEDGE_MAP.md
    MAJOR_CHANGES.md
    current_routing.json

Primary target:

    JC1 Project Direction, Architecture and Memory

Special case:

    current_routing semantic state may also be produced/validated by JC2;
    its future root cold-start anchor is governed by Research 248 A2.

Disposition:

    R7_REQUIRED
    current filenames/root placement not preserved automatically

### foundations/

Primary target:

    JC1 accepted/foundational architecture knowledge

Disposition:

    R7_REQUIRED

The artifact family may or may not survive as a physical family.

### specifications/

Primary target:

    JC1 architecture/contract authority

Some executable contract representations may live with Product/Project workspaces, while the accepted project record remains JC1.

Disposition:

    R7_REQUIRED / possible split between normative record and executable contract

### research/

Primary target:

    JC3 Research and Qualification

Promoted conclusions may update JC1 or Product artifacts.

Historical studies may transition to JC6.

Disposition:

    R7_REQUIRED / lifecycle split

### checkpoints/

Current role spans:

    project continuity
    milestone evidence
    experimental results
    architecture transitions
    operational handoffs

Target:

    JC1 / JC3 / JC4 / JC6 depending checkpoint role

Disposition:

    SPLIT SEMANTICALLY in R7

The current "checkpoint" type is not guaranteed to remain one permanent physical family.

## 8. Current domain-named docs directories

### docs/cockpit/

Observed role:

    paused design workstream control
    accepted/provisional implementation provenance
    decision ledger
    exact fidelity/resume evidence

Target:

    product behavior that was actually promoted
        -> PC6 normative/product implementation contracts

    design research and unpromoted candidates
        -> JC3

    implementation provenance needed for accepted behavior
        -> JC3/JC1 depending normative role

    frozen/superseded visual sources retained for recovery
        -> JC6

Disposition:

    SPLIT

No future cockpit/ container is implied.

### docs/source_universe/

Observed role:

    Source Vault bootstrap workstream
    reviewed ingestion procedures
    local/private operational state examples
    validation/intake/manifests

Target split:

    stable Product source/evidence semantics
        -> PC3

    development research/qualification/bootstrap evidence
        -> JC3

    development/local operations
        -> JC4

    current private operational integration notes
        -> JC4 / external Level-0 companion relation

Disposition:

    SPLIT

No future source_universe docs folder is required.

### docs/methodological_knowledge/

Current COVERAGE_MAP is explicitly a planning/coverage-routing artifact rather than accepted methodological authority.

Target:

    current planning record
        -> JC3 / JC1 planning history

    future accepted reusable methodological assets
        -> PC2 Product-owned knowledge

Disposition:

    SPLIT BY MATURITY/AUTHORITY

### docs/local_execution/

Observed role:

    local runtime operations
    authority/bootstrap
    Git investigation lessons
    ACL/integrity
    pull/semantic acceptance
    validation

Target split:

    repository/development environment operations
        -> JC4

    mechanized project-control bootstrap/authority
        -> JC2/JW1 where appropriate

    historical operational lessons
        -> JC6 or JC1 if promoted into durable engineering policy

Disposition:

    SPLIT

The current local_execution concept is not retained automatically.

### docs/model_collaboration/

Target:

    collaboration semantics/current active review state
        -> JC5

    mechanized validation/routing
        -> JC2/JW1 or JC4 implementation

    completed historical threads
        -> JC6/R7 historical project evidence

Disposition:

    SPLIT

### docs/private_companion/

Current role:

    public-safe description of an external/private companion boundary

Target:

    Level-0 external-system relationship knowledge
    under JC1/JC4 depending architecture versus operations

Disposition:

    R7_REQUIRED

No private_companion folder is automatically retained.

### docs/experiments/

Current:

    prototype_v0 result/evidence records

Target:

    JC3 accepted experiment evidence
    JC6 historical record where inactive

Disposition:

    SPLIT BY LIFECYCLE

## 9. Current research/experiment code families

### experiments/* Product-behavior experiments

Examples:

    blocking_calibration
    methodological_navigation_coverage
    reasoning_context_value
    recommendation_action_value
    retrieval
    runtime_bakeoff
    relation/provenance recommendation experiments

Target while active:

    JC3 bounded experiment execution

After completion:

    accepted runtime mechanism -> relevant Product context
    durable result -> R7 evidence
    preserved reproduction -> JC3/JC6
    obsolete shell -> retire

### experiments/project_knowledge_*

Target:

    JC3 research evaluating JC2/JW1

Disposition after completion:

    durable evidence/historical reproduction, not permanent Project-system code

### scripts/research/*

Target:

    JC3 when active/reproducibility-bearing
    JC6 or retire when historical and non-load-bearing

## 10. Root configuration and bootstrap mapping

### README.md

Target:

    TRUE ROOT human cold-start entry

Disposition:

    DIRECT_FIT in responsibility

Future content should route a cold-start reader into:

    Product overview
    Project development/authority entry
    build/run/contribute entry

without becoming the full project manual.

### .gitignore

Target:

    TRUE ROOT repository-host/tooling anchor

Disposition:

    DIRECT_FIT

### .python-version

Candidate:

    TRUE ROOT only if Python version is a repository/workspace-wide
    developer/tooling contract

otherwise:

    move to owning Python workspace(s)

Disposition:

    TOOL_ROOT_CANDIDATE

### pyproject.toml

Current:

    Product Python package/build configuration at root

Target possibilities:

    PW1-local pyproject if only Product runtime owns it

or:

    true-root workspace orchestrator pyproject if a future uv multi-workspace
    design genuinely requires repository-level Python orchestration

Disposition:

    SPLIT ROLE / R8_REQUIRED

Current root location has no automatic preservation claim.

### uv.lock

Target:

    root only if shared workspace orchestration selects one repository-wide
    Python lock

otherwise:

    owning workspace

Disposition:

    TOOL_ROOT_CANDIDATE / R8_REQUIRED

### alembic.ini

Target:

    PC7/PW1 persistence

Disposition:

    move under Product runtime unless proven root-required by chosen tooling

### frontend package files

    package.json
    package-lock.json
    Vite/TS/Playwright configuration

Target:

    PW2 Product interaction workspace

Disposition:

    DIRECT_FIT responsibility
    exact future client workspace name/layout open

## 11. Test/cache/generated cleanup observations

The current working tree exposes local/generated directories such as:

    __pycache__
    .pytest_cache
    .g014_compilecache*
    frontend/node_modules
    prototype_v0/.venv

These are not target architecture entries.

R8 should ensure:

    ignore policies
    deterministic regeneration where applicable
    no accidental authority
    no migration of local caches as project knowledge

This is housekeeping, not an architecture category.

## 12. Cross-plane residue check

R6-B found no current artifact family that requires a new third Level-1 plane.

No named root integration contract is yet required.

Current outcome-3 count remains:

    A1_NAMED_ROOT_INTEGRATION_CONTRACTS = 0

Ambiguous examples such as build provenance, product version metadata and shared provider integration can be resolved through split or asymmetric ownership under the accepted A1 rule.

## 13. Target-root pressure check

A plausible future root remains within the preregistered bound.

Likely true-root classes currently justified:

    product/
    project/
    .github/
    README.md
    .gitignore

Conditional tooling anchors may include:

    repository workspace orchestrator config
    repository-wide lockfile
    repository-wide runtime-version anchor

This implies a likely target in the 5-8 entry range before legal/community files, comfortably below:

    ROOT_ENTRY_REVIEW_BOUND = 12

No amendment is required.

## 14. R6-B completion criterion

Family-level current-to-target mapping is sufficient to unblock R7 because:

    every current top-level tracked family has a target responsibility
    current mixed artifact roots have explicit split logic
    major current Product implementation families have context mapping
    major Project-control implementation families have context mapping
    current docs/domain directories have lifecycle/owner mapping
    current experiments/prototype have lifecycle mapping
    root bootstrap/tooling has target responsibility mapping
    no unresolved third-plane requirement exists

R6-B deliberately does **not** produce the eventual file-by-file move manifest.

That belongs in R8 after R7 defines the future Project information architecture and after downstream contract impacts are reconciled.

## 15. Consequence for R7

R7 is now unblocked.

R7 must design the Project-plane information architecture for:

    JC1 Project Direction, Architecture and Memory
    JC3 Research and Qualification evidence
    JC4 engineering/governance knowledge where durable
    JC5 collaboration records where durable
    JC6 historical preservation

while keeping executable JC2/JW1 control state and generated machinery distinct from ordinary durable project knowledge.

R7 must not begin from today's docs/ tree.

It must derive:

    information classes
    authority/maturity model
    lifecycle
    navigation
    human/agent cold-start
    operational versus historical separation
    executable/generated control-state boundary
    evidence/provenance boundary

and only then map current documents/families.

## 16. Current state

    R6B_FAMILY_MAPPING=COMPLETE
    CURRENT_TOP_LEVEL_FAMILIES_MAPPED=YES
    CURRENT_DOCS_FAMILIES_MAPPED=YES_AT_RESPONSIBILITY_LEVEL
    CURRENT_PRODUCT_IMPLEMENTATION_MAPPED=YES_AT_CONTEXT_LEVEL
    CURRENT_PROJECT_SYSTEM_MAPPED=YES_AT_CONTEXT_LEVEL
    FILE_LEVEL_MOVE_MANIFEST=DEFERRED_TO_R8
    A1_ROOT_INTEGRATION_CONTRACTS=0
    ROOT_BOUND_PRESSURE=PASS
    R7=UNBLOCKED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R7_FROM_SCRATCH_PROJECT_INFORMATION_ARCHITECTURE
