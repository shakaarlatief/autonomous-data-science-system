# Research 250: R6-A Responsibility Coupling, Bounded Contexts, and Workspace Candidate Synthesis

**Date:** 2026-09-22
**Status:** R6 BOUNDED-CONTEXT / WORKSPACE CANDIDATE FROZEN / OWNER DECISION REQUIRED BEFORE CURRENT-TO-TARGET MAPPING
**Parent program:** Research 240
**Responsibility basis:** Research 249
**Accepted Level-1 architecture:** Research 248 / amended G-DUAL
**Repository base:** 89d5acdba694d4d8a3132f5bc36fffdd10cd04ec
**Scope:** Derive professional lower-level subsystem and workspace boundaries from the frozen R6-A responsibility model without using current repository folders as target units. Freeze a recommended boundary architecture before any current-to-target mapping.

## 1. Boundary types must not be conflated

A professional repository can have several kinds of boundaries that are related but not identical.

### 1.1 Bounded context

A semantic/authority boundary.

It answers:

    Which responsibility owns this meaning?
    Which concepts and invariants are internally coherent?
    Where must translation occur between different models?

A bounded context does not automatically deserve its own package, process, service or repository.

### 1.2 Workspace

A build/toolchain/qualification boundary.

It answers:

    Does this unit have a coherent dependency graph?
    Does it need its own package manager or build configuration?
    Can it be qualified meaningfully as one technical unit?
    Does its lifecycle justify first-class workspace status?

### 1.3 Deployment unit

An independently deployable/operable runtime boundary.

It answers:

    Does this need independent scaling, fault isolation, security isolation,
    release cadence or operations?

A deployment unit may be extracted from one workspace later.

### 1.4 Information domain

A knowledge/evidence/authority organization boundary.

It answers:

    Where does durable knowledge about this responsibility live?

R7 governs the Project-plane information architecture.

### 1.5 Why the distinction matters

The current repository often lets one folder imply several of these roles at once.

R6 rejects that shortcut.

For example:

    reusable methodological knowledge
        can be a distinct bounded context

without requiring:

    a separate repository
    a separate deployable service
    a separate package manager

Likewise a web client can be a separate workspace because of its toolchain even while it remains one product surface of the same product domain.

## 2. Coupling dimensions

Each responsibility from Research 249 is compared on:

    semantic authority
    shared state/invariants
    transactional consistency
    lifecycle/change pressure
    dependency direction
    build/toolchain
    qualification surface
    deployment/scaling pressure
    security/permission boundary
    failure isolation
    provider volatility
    portability/reuse
    projected future coupling

The design deliberately avoids "one responsibility = one service".

## 3. Product bounded contexts

R6 recommends seven logical Product bounded contexts.

These are responsibility/authority boundaries, not folder names.

### PC1. Project Intelligence

Primary responsibilities:

    P01 Project intent/lifecycle/semantic state
    P02 Methodological intelligence/process navigation
    P07 Epistemic assurance/admissibility/human-control semantics

Owns:

    the evolving analytical project model
    project meaning and state transitions
    questions/assumptions/findings/claims/decisions
    methodological horizon and next-action semantics
    required/blocking/deferred status
    consequence-aware human escalation
    claim/evidence dependency status

Why these belong together:

    methodological navigation is a function of current project state;
    assurance rules constrain which state transitions/claims are legitimate;
    human-control requirements are triggered by project/assurance state.

They share one high-cohesion semantic model.

This is the central product domain.

### PC2. Methodological Knowledge

Primary responsibility:

    P03 Reusable methodological knowledge

Owns:

    reusable methodological assets
    components/facets/rules
    relations
    revisions
    methodological provenance
    applicability/retrieval metadata
    execution-capability references

Boundary rule:

    PC2 may inform PC1 but does not own project-specific state.

    global/reusable methodological knowledge
        !=
    one project's current methodological decision state

Why separate:

Its revision/governance lifecycle is cross-project and different from the lifecycle of any one analytical project.

### PC3. Evidence and Artifact Provenance

Primary responsibility:

    P04 Evidence/source/data-asset provenance

Owns:

    logical source identity
    exact artifact identity
    dataset/artifact lineage
    evidence locations
    rights/access classification
    derived-artifact provenance
    integrity/recovery semantics for evidentiary artifacts

Boundary rule:

    evidence possession/provenance
        !=
    accepted methodological knowledge

    evidence record
        !=
    claim/decision

Why separate:

Evidence has immutable/integrity/rights concerns that differ materially from PC1 project reasoning and PC2 accepted reusable knowledge.

### PC4. Reasoning Orchestration

Primary responsibility:

    P05 Reasoning/context runtime

Owns:

    reasoning-task contracts
    context assembly
    provider-neutral model semantics
    model/tool invocation policy
    structured reasoning I/O
    provider adapter boundary
    retry/failure semantics for reasoning calls

Boundary rule:

The reasoning system proposes/interprets.

It must not silently become the authoritative owner of project state, evidence identity or execution truth.

### PC5. Analytical Execution

Primary responsibility:

    P06 analytical execution/computational work

Owns:

    executable investigation/run lifecycle
    compute/tool invocation
    run identity
    cancellation/retry
    deterministic execution constraints
    resource accounting
    execution artifacts/events

Boundary rule:

    reasoning request
        !=
    execution fact

    execution event/artifact
        !=
    project claim

The execution context produces evidence for PC1/PC3 to interpret and govern.

### PC6. Product Interaction and Access

Primary responsibility:

    P08 product experience/interaction surfaces

Owns:

    human-facing interaction semantics
    project navigation
    approvals/interventions
    conversation surface
    specialist views
    accessibility
    user-facing status/error/recovery behavior
    external client/API/CLI presentation contracts where product-facing

Boundary rule:

The interface projects and commands product state through stable product contracts.

It does not own analytical truth merely because the user sees or edits it there.

### PC7. Runtime Platform and External Boundary

Primary responsibilities:

    P09 Persistence/state integrity/recovery
    P10 Product integration/interoperability
    P11 Product security/privacy/trust
    P12 Runtime operations/reliability/resource stewardship

Owns technical realization concerns such as:

    persistence adapters
    transaction/storage mechanisms
    schema migration mechanics
    runtime provider/connectors
    identity/authz enforcement mechanisms
    runtime secrets integration
    telemetry mechanisms
    health/recovery mechanisms
    deployment/runtime configuration mechanisms
    performance/resource controls

Important boundary rule:

PC7 is **not** a miscellaneous "infrastructure" owner.

Its components implement contracts defined by the product bounded contexts and the accepted product-wide quality policies.

Domain meaning remains inward.

Provider/framework/storage technologies remain outward.

The reason to keep these four responsibilities in one logical platform context at R6 is not that they are semantically identical. It is that, at the current architectural maturity, they are technical realization capabilities serving the same product runtime and do not yet show independent product-domain authority or deployment lifecycles sufficient to justify separate first-class workspaces.

R6 must preserve internal separation among persistence, external integrations, security and operations so they can split later if actual lifecycle/deployment evidence demands it.

## 4. Product dependency direction

Preferred conceptual direction:

    PC6 Interaction
        ->
    PC1 Project Intelligence
        ->
    PC2 Methodological Knowledge
    PC3 Evidence/Provenance
    PC4 Reasoning Orchestration
    PC5 Analytical Execution

    PC1/PC2/PC3/PC4/PC5
        depend on stable ports/contracts
        <-
    PC7 Runtime Platform implements those outward technical ports

More precisely:

    PC2 informs PC1 through explicit knowledge-query/revision contracts.

    PC3 supplies provenance/artifact references to PC1/PC2/PC5.

    PC4 receives bounded reasoning tasks/context from application/domain
    orchestration and returns proposals/results.

    PC5 receives explicit execution jobs and emits execution facts/artifacts.

    PC6 accesses product behavior through application/API contracts.

    PC7 implements persistence/provider/security/operations mechanisms without
    owning the inner semantic model.

Cycles at the semantic-authority level are rejected even if runtime callbacks/events are bidirectional.

## 5. Product workspace candidate

### PW1. Core Product Runtime Workspace

**Recommendation:** STRONG CANDIDATE

Contains the implementation of:

    PC1 Project Intelligence
    PC2 Methodological Knowledge
    PC3 Evidence/Artifact Provenance
    PC4 Reasoning Orchestration
    PC5 Analytical Execution
    PC7 Runtime Platform/External Boundary

Why one workspace initially:

    common backend/runtime language family is plausible
    strong transactional/state coupling exists across project state and evidence
    reasoning/execution are orchestration components of the same product runtime
    provider/storage/runtime adapters benefit from one stable inward domain contract
    no current evidence requires independent deployment of those contexts
    splitting them into services now would add distributed-state and operations cost
    without a demonstrated lifecycle benefit

This is a **modular product runtime**, not permission for a featureless monolith.

Required internal properties:

    explicit module/context boundaries
    dependency direction checks
    narrow public interfaces
    no provider/framework leakage into domain semantics
    independently testable context contracts
    extraction-ready seams for components that later earn separate lifecycle

External professional evidence supports this posture:

    AWS Prescriptive Guidance notes that modular monoliths and microservices
    can coexist and that microservices introduce integration/data-consistency/
    latency/operational complexity.

    Bounded contexts and explicit contracts remain valuable even when contexts
    share one deployment artifact.

Sources:

    https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/introduction.html
    https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/micro-frontend-alternatives.html

This is not a "small project" compromise.

It is a professional choice to delay distributed-system cost until independent deployment, scaling, fault, security or team/lifecycle boundaries justify it.

Extraction triggers for any PC1-PC5/PC7 context include:

    independent scaling requirement
    materially different availability/fault domain
    materially different security boundary
    incompatible dependency/runtime needs
    independent release cadence
    independent team ownership at sustained scale
    operational isolation requirement
    reusable distribution need
    persistent change-coupling evidence showing extraction reduces coordination cost

### PW2. Product Interaction Workspace Family

**Recommendation:** STRONG CANDIDATE

Owns implementation of PC6 interaction surfaces that have independent technical toolchains.

The family may include:

    web client
    desktop shell
    CLI client
    API client libraries

but R6 does not create one workspace for each possibility now.

Why separate from PW1:

    interaction surfaces have distinct build/toolchain/runtime concerns;
    they should consume stable product contracts rather than import backend
    implementation internals;
    UI deployment and release cadence can differ from backend/runtime cadence.

Important:

The current frontend's historical isolation is not the justification.

Even if today's frontend folder disappeared, a serious browser-based product surface would still have a distinct JavaScript/TypeScript build/qualification boundary unless a future technology choice removed that difference.

The exact future client workspaces remain R6-B/R8 realization questions.

## 6. Product contexts not promoted to separate workspaces now

The following remain logical contexts inside PW1 unless future evidence changes the result:

    PC2 Methodological Knowledge
    PC3 Evidence and Artifact Provenance
    PC4 Reasoning Orchestration
    PC5 Analytical Execution
    PC7 Runtime Platform

This is deliberate.

"Important" does not mean "separate package/service/repository".

Each context should still have enforceable internal contracts so later extraction is possible without first inventing boundaries retrospectively.

## 7. Project bounded contexts

R6 recommends six logical Project bounded contexts.

### JC1. Project Direction, Architecture and Memory

Primary responsibilities:

    J01 Product direction/requirements/roadmap
    J02 Architecture/decision governance
    J03 Project knowledge/continuity/reconstruction

Owns:

    why the project exists
    accepted direction
    requirements and non-goals
    architecture decisions/specifications
    current project authority/state
    durable rationale
    knowledge routing
    continuity/reconstruction semantics

Why together:

These are different document/record types but one authority system for understanding what the project currently means and why.

This is an information/authority context, not an executable software package.

R7 will design its information architecture.

### JC2. Project Development Control System

Primary responsibility:

    J04 project-development control system

Owns:

    project-development state/control machinery
    activation/orchestration
    workstream/control semantics
    accepted-obligation traceability
    evolution-trigger handling
    collaboration routing/control where mechanized
    Git lifecycle control where mechanized
    deterministic project views
    project-system instance policy

PSMF maps here.

This is the strongest Project-plane executable workspace candidate.

### JC3. Research and Qualification

Primary responsibilities:

    J05 research/experimentation/qualification
    parts of J06 product-behavior/system evaluation

Owns:

    hypotheses
    preregistered experiments
    controlled evaluations
    falsification programs
    qualification evidence
    review protocols
    accepted experimental verdicts

Boundary rule:

Research execution is a lifecycle, not necessarily a permanent package hierarchy.

Active experimental code may live in bounded temporary/reproducible execution units.

Durable accepted evidence moves into the project information/evidence architecture.

### JC4. Engineering, Verification and Delivery

Primary responsibilities:

    J06 verification/quality engineering
    J07 repository/workspace/build engineering
    J08 secure-development/supply-chain governance
    J09 release/change/configuration management
    J11 development environments/project operations

Owns:

    repository engineering
    build/test orchestration
    integration/acceptance qualification
    CI architecture
    dependency/toolchain governance
    secure-development controls
    release qualification and publication process
    development environment/diagnostics
    project operational health

Why together at R6:

These responsibilities operate the software-development lifecycle of the repository.

They are highly coupled through CI/build/release/verification and do not currently need separate conceptual top-level systems merely because security, testing and release are important.

Internal sub-boundaries must remain explicit.

### JC5. Collaboration and Contribution

Primary responsibility:

    J10 contributor/agent/collaboration workflow

Owns:

    contribution semantics
    human/model handoff
    code/research review workflow
    bounded write authority
    external contribution policy
    collaboration-provider integration contracts

Boundary rule:

Mechanized project-control portions may be implemented by JC2.

Repository-host/workflow portions may be implemented by JC4.

JC5 owns the **collaboration semantics**, not necessarily one executable workspace.

### JC6. Historical Preservation

Primary responsibility:

    J12 historical preservation/archive lifecycle

Owns:

    historical classification
    preservation criteria
    archived executable programs
    superseded-but-important artifacts
    reproducibility retention decisions
    distinction between active architecture and historical truth

This is primarily an information/lifecycle context, not a software workspace.

## 8. Project workspace candidates

### JW1. Project Development System Workspace

**Recommendation:** STRONG CANDIDATE

Implements JC2.

Expected properties:

    complete project-local materialization of the generic framework mechanism
    project-local instance policy/extensions
    project-control implementation
    local contracts/schemas
    local unit/contract tests
    generated control state where appropriate
    lineage for framework materialization/upgrades

It must remain self-contained at project operation/recovery time under PSMF.

The final name is still open.

### JW2. Repository Engineering Workspace

**Recommendation:** NOT YET JUSTIFIED AS AN INDEPENDENT PACKAGE

JC4 is a first-class responsibility context, but a dedicated executable package/workspace should exist only when shared project-engineering code becomes substantial enough to justify one.

Many JC4 artifacts may legitimately remain:

    repository orchestrator configuration
    CI definitions
    validation commands
    development environment configuration
    release configuration

without becoming a package.

If reusable executable engineering code grows, R6/R8 may introduce a bounded project-engineering package rather than recreating a generic scripts/ bucket.

### Research execution workspaces

**Recommendation:** EPHEMERAL / PROGRAM-SCOPED BY DEFAULT

JC3 may create bounded reproducible experiment workspaces while active.

They do not become permanent peers automatically.

After completion each receives an explicit disposition:

    promote implementation
    preserve executable reproduction package
    retain evidence only where independently re-derivable
    archive
    retire

This replaces the assumption of one indefinitely growing universal experiments/ tree.

## 9. Cross-plane dependency invariant

The most important R6 dependency rule is:

> The operational Product plane must not require the Project plane for runtime correctness.

A released/built ADS product must remain operable even if:

    project research records are absent
    project-control machinery is absent
    development collaboration tooling is absent
    repository engineering tools are absent

The Project plane may inspect, build, test, qualify and release the Product plane.

Therefore the dependency is asymmetric:

    project
        -> may depend on / inspect / orchestrate product for development

    product runtime
        -X-> must not depend on project plane

Permitted exception:

    immutable build/version/provenance metadata may be generated by project
    engineering and embedded in product artifacts when the product owns the
    runtime consumption contract.

This is handled as split/asymmetric ownership under A1.

## 10. True-root cross-plane candidates

R6 still does not populate the final root inventory.

It identifies only the classes likely to require later inventory entries:

    product/
    project/
    human cold-start entry
    machine cold-start/routing anchor
    repository-host integration
    repository/workspace orchestrator anchors
    legal/host metadata only when root semantics justify it
    named cross-plane integration contract only if A1 requires one

The preregistered review bound remains:

    12 tracked first-level entries

No root integration contract has yet been proven necessary.

Current count of A1 outcome-3 contracts:

    0

## 11. Architecture stress test

### Future multiple product services

PW1 may split only when extraction triggers fire.

G-DUAL root remains stable.

### Large methodological knowledge base

PC2 can scale internally and later extract without changing the Product/Project Level-1 architecture.

### Large evidence/source substrate

PC3 can acquire specialized storage/runtime without becoming Project-plane knowledge.

### Multiple user surfaces

PW2 becomes a family of client workspaces while product semantic authority remains PC1-PC7.

### Remote/background execution

PC5 can extract into a separate worker/service if fault/security/scaling pressure justifies it.

### Multiple model providers

PC4 retains ADS-owned reasoning semantics while PC7 provider adapters vary.

### Multi-user/security requirements

P11/PC7 can mature into stronger isolation/authn/authz mechanisms without forcing project-security governance into Product.

### Larger engineering organization

JC4 can split internally or gain a workspace; JW1 remains the project-control system rather than swallowing the full engineering organization.

### Many experiments and retired prototypes

JC3/JC6 lifecycle prevents permanent root/workspace accumulation.

### Framework reused in another project

JW1 materialization remains project-local; ADS product-specific contexts are not copied into the generic framework.

## 12. Strongest alternative

The strongest alternative is a more distributed Product architecture:

    PC2 knowledge service
    PC3 evidence service
    PC4 reasoning service
    PC5 execution service
    PC1 project-state service

with independent workspaces/deployments from the beginning.

R6 rejects that as the target **for now**, not because ADS is a small project, but because:

    independent lifecycle/deployment/scaling/security requirements have not
    been demonstrated for each service;

    the distributed design creates transaction, consistency, versioning,
    observability and operational burdens immediately;

    the bounded contexts can be preserved inside a modular runtime and
    extracted later under explicit triggers.

If future scale proves independent deployment valuable, the current recommendation is designed to make that evolution straightforward.

## 13. Recommended R6 boundary architecture

### Product plane

    Product bounded contexts
        PC1 Project Intelligence
        PC2 Methodological Knowledge
        PC3 Evidence and Artifact Provenance
        PC4 Reasoning Orchestration
        PC5 Analytical Execution
        PC6 Product Interaction and Access
        PC7 Runtime Platform and External Boundary

    Strong workspace candidates
        PW1 Core Product Runtime Workspace
        PW2 Product Interaction Workspace Family

### Project plane

    Project bounded contexts
        JC1 Project Direction, Architecture and Memory
        JC2 Project Development Control System
        JC3 Research and Qualification
        JC4 Engineering, Verification and Delivery
        JC5 Collaboration and Contribution
        JC6 Historical Preservation

    Strong workspace candidate
        JW1 Project Development System Workspace

    Not automatically workspaces
        JC1 information/authority corpus
        JC3 research lifecycle
        JC4 repository engineering surface
        JC5 collaboration semantics
        JC6 historical lifecycle

## 14. Why owner decision is required before R6-B

This boundary architecture is materially more specific than the already accepted Level-1 Product / Project split.

If accepted, R6-B may begin mapping current artifacts into these derived responsibilities/contexts.

If amended, mapping must wait.

If rejected, R6 must derive another lower-level boundary model without using the current repository tree as its skeleton.

No current folder has been assigned a target path in this research.

## 15. Recommended owner disposition

Recommended decision:

    ACCEPT

meaning:

    accept the R6 logical bounded-context/workspace architecture as the
    target model for current-to-target mapping and R7 follow-on design;

    preserve extraction/evolution triggers;

    do not authorize physical migration yet.

## 16. Current state

    R6_RESPONSIBILITY_MODEL=FROZEN
    R6_BOUNDARY_CANDIDATE=FROZEN
    RECOMMENDED_OWNER_DECISION=ACCEPT
    OWNER_DECISION=PENDING
    PRODUCT_CONTEXTS=7
    PROJECT_CONTEXTS=6
    STRONG_PRODUCT_WORKSPACE_CANDIDATES=2
    STRONG_PROJECT_WORKSPACE_CANDIDATES=1
    ROOT_INTEGRATION_CONTRACTS=0
    CURRENT_TO_TARGET_MAPPING=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=OWNER_R6_BOUNDARY_DECISION
