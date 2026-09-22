# Research 249: R6-A From-Scratch Professional Responsibility Model and Root-Bound Preregistration

**Date:** 2026-09-22
**Status:** R6-A RESPONSIBILITY MODEL FROZEN / TRUE-ROOT REVIEW BOUND PREREGISTERED / CURRENT TREE NOT USED AS TARGET INPUT / WORKSPACE BOUNDARY SYNTHESIS NEXT
**Parent program:** Research 240
**Accepted Level-1 architecture:** Research 248 / G-DUAL accepted as amended
**Repository base:** 8c85be872f11b9a09b2a3f2cef8b52add2072a56
**Scope:** Derive the durable responsibilities of a professional-grade future ADS from first principles before mapping any present folder, package, file family or subsystem into the target architecture.

## 1. Design posture

ADS is not being designed as a small personal utility whose repository only needs to remain convenient for one current implementation.

R6 assumes a serious long-lived technical product and project that may need to support:

    substantial data-science projects
    multiple product surfaces
    multiple model/tool/provider integrations
    multiple execution environments
    larger source and methodological-knowledge corpora
    concurrent human and model contributors
    production-quality security and recovery
    selective CI and release engineering
    long-running background work
    reproducible experiments and evaluations
    future package/service boundaries
    future project/framework reuse
    cold-start reconstruction years later

This does not imply adopting enterprise ceremony for its own sake.

The rule is:

> design responsibilities at professional scale, then implement only the mechanisms whose complexity is justified.

## 2. Derivation method

The responsibility model is derived from:

1. the canonical ADS product vision and constitutional project principles;
2. accepted foundations describing the LLM/system/human boundary, project state, methodological knowledge, evidence provenance, execution and observability;
3. the accepted G-DUAL Product / Project distinction;
4. professional software-system responsibilities that remain important even when no current ADS folder represents them;
5. explicit anti-anchoring probes from Research 248.

Current folders are deliberately not used as the units of derivation.

Only after the responsibility model and later workspace boundaries are frozen may current material be mapped.

## 3. Professional external cross-check

R6 does not copy an external enterprise architecture, but several current professional references confirm responsibilities that a serious software/AI system should not omit merely because ADS has not yet created folders for them.

### NIST Secure Software Development Framework

NIST SP 800-218 treats secure software development as a set of practices integrated into the software development lifecycle, including preparing the organization, protecting software, producing well-secured software and responding to vulnerabilities.

Sources:

    https://csrc.nist.gov/pubs/sp/800/218/final
    https://csrc.nist.gov/projects/ssdf

R6 implication:

    secure development and vulnerability/supply-chain responsibility
    belongs in the project plane even if no current root represents it.

### SLSA

SLSA treats build provenance as verifiable information about how software artifacts were produced and uses progressively stronger build-integrity controls.

Sources:

    https://slsa.dev/spec/v1.2/provenance
    https://slsa.dev/spec/v1.1/levels

R6 implication:

    build/release provenance and artifact-integrity responsibility
    must be represented in professional project engineering.

### OpenTelemetry

OpenTelemetry models observability through vendor-neutral telemetry such as traces, metrics and logs.

Sources:

    https://opentelemetry.io/docs/
    https://opentelemetry.io/docs/concepts/observability-primer/

R6 implication:

    runtime observability is a durable product responsibility;
    development/build/research observability is a distinct project responsibility.

### Well-Architected frameworks

AWS and Azure both treat reliability, security, operational excellence, performance efficiency and cost as architectural qualities of serious workloads.

Sources:

    https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html
    https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework

R6 implication:

    operation, reliability, performance and resource/cost control cannot
    be postponed conceptually until a cloud provider is selected.

These references validate responsibility classes. They do not select ADS technologies, deployment providers or folder names.

## 4. Cross-cutting quality attributes are not top-level owners

The following are architectural qualities that must be designed across relevant responsibilities:

    security
    privacy
    reliability
    recoverability
    observability
    performance
    scalability
    cost/resource efficiency
    accessibility
    usability
    reproducibility
    provenance
    portability
    interoperability
    maintainability
    testability
    auditability
    traceability
    explainability where consequential
    backward/forward compatibility where contracts exist

They are **not** automatically folders, packages or workspaces.

For example:

    product runtime security
        is product responsibility

    secure software development and dependency provenance
        is project responsibility

The same quality attribute may therefore appear in both planes under different authority contracts.

## 5. Product-plane responsibility model

The Product plane owns the operational ADS system and product-owned assets.

The following responsibilities are durable enough to carry into boundary synthesis.

### P01. Project intent, lifecycle and semantic state

Own:

    project creation/open/archive lifecycle
    project intent and goals
    constraints and preferences
    domain/project definitions
    project object identity
    questions, assumptions, findings, claims and decisions
    project events and state transitions
    stale/superseded/invalidated status
    dependency impact on project state

Why durable:

ADS is a persistent project environment, not a one-shot model call.

This responsibility survives changes in UI, model provider, database and agent framework.

### P02. Methodological intelligence and process navigation

Own:

    known/applicable/relevant/recommended/required reasoning
    methodological-horizon construction
    project-specific activation
    next-investigation reasoning support
    missing-context detection
    stopping/defer/reopen logic
    state-triggered methodological reconsideration
    resource-aware analytical prioritization

Why durable:

This is one of the central product-intelligence problems in the canonical vision.

### P03. Reusable methodological knowledge

Own:

    governed reusable methodological assets
    narrative and structured components
    methodological relations and conditional rules
    revisions and provenance
    execution-capability associations
    reusable cross-project lessons
    retrieval/applicability metadata

Why durable:

Reusable methodological reasoning is a first-class long-term product asset independent of one project or one model provider.

### P04. Evidence, source and data-asset provenance

Own product-facing semantics for:

    external source identity
    exact source-artifact identity/integrity
    data/dataset identity and lineage
    derived-artifact lineage
    rights/access classification
    evidence locations and provenance
    artifact verification
    recoverable source/data storage semantics

Why durable:

ADS claims and reusable knowledge require inspectable evidence and exact provenance.

This responsibility is broader than any current Source Universe folder.

### P05. Reasoning and context runtime

Own:

    provider-neutral reasoning boundary
    model invocation semantics
    model/tool capability routing
    context construction
    selective retrieval into model context
    structured reasoning I/O contracts
    tool-call mediation
    reasoning retries/failures
    provider-specific adapters behind ADS-owned semantics

Why durable:

The LLM remains a reasoning component inside ADS, but provider/framework identity must not define product semantics.

### P06. Analytical execution and computational work

Own:

    investigation/run execution
    Python/SQL/tool execution
    reproducible run identity
    compute/environment selection
    run lifecycle
    cancellation/retry semantics
    resource accounting
    analytical artifacts
    deterministic execution controls
    safe execution isolation as requirements grow

Why durable:

ADS must produce empirical evidence, not only recommendations.

### P07. Epistemic assurance, admissibility and human control

Own:

    admissibility boundaries
    semantic validity
    information legitimacy
    evidence validity
    claim validity
    traceability/dependency integrity
    risk-sensitive assurance
    deterministic blockers where rules are precise
    human approval/escalation contracts
    consequence/reversibility-aware intervention
    explanation of why work is required/recommended/deferred

Why durable:

Professional autonomy requires explicit validity and authority boundaries, not only capability.

### P08. Product experience and interaction surfaces

Own product interaction semantics across:

    graphical interface
    conversation/discussion
    project/process navigation
    approvals and interventions
    direct specialist views
    APIs
    CLI/automation surfaces where justified
    accessibility
    user-facing status/recovery states
    explainability and provenance inspection

Why durable:

The exact frontend may change, but ADS needs coherent ways for humans and external clients to interact with the same product state.

No current Cockpit or frontend folder is assumed to survive as the boundary.

### P09. Persistence, state integrity and recovery

Own:

    durable product state
    transactional integrity
    storage abstractions
    schema evolution
    migrations
    backup/restore
    corruption/integrity detection
    retention
    local-first storage where still justified
    future storage-provider substitution behind stable semantics

Why durable:

Persistent state is a defining system responsibility and must remain recoverable.

### P10. Product integration and interoperability

Own product-facing contracts for:

    model providers
    execution/compute providers
    data/source systems
    storage systems
    IDE/developer-workbench integration where product-facing
    external APIs
    connector protocols
    import/export/interchange
    future plugin/extension boundaries where evidence justifies them

Why durable:

ADS must integrate without granting external frameworks authority over ADS semantics.

### P11. Product security, privacy and trust boundaries

Own runtime/product controls for:

    authentication where needed
    authorization
    project/data isolation
    secrets/credential use at runtime
    least-privilege access
    sensitive-data handling
    audit/security events
    privacy policy enforcement
    connector/provider permission boundaries
    secure artifact handling

Why durable:

A professional product cannot treat security as a later deployment wrapper.

### P12. Runtime operations, reliability and resource stewardship

Own product-runtime behavior for:

    health
    telemetry
    logs/metrics/traces/events
    failure isolation
    recovery
    compatibility
    performance
    capacity/scalability
    long-running workflow supervision
    resource/cost accounting
    graceful degradation
    operational diagnostics
    deployment/runtime readiness

Why durable:

ADS is expected to execute long-running consequential work and therefore needs an operable runtime, not only correct code.

## 6. Project-plane responsibility model

The Project plane owns development, governance, evidence and preservation of ADS as a technical project.

### J01. Product direction, requirements and roadmap governance

Own:

    long-term product intent
    scoped requirements
    success criteria
    prioritization
    roadmap/stage decisions
    accepted constraints
    explicit non-goals
    owner decisions about material direction

Why durable:

A serious project requires a maintained distinction between product intent and implementation history.

### J02. Architecture and decision governance

Own:

    architectural principles
    architecture decisions
    specifications/contracts
    evolution cases
    acceptance/supersession
    dependency-impact review
    architecture qualification
    exception governance

Why durable:

Material architectural choices must remain inspectable, challengeable and evolvable.

### J03. Project knowledge, continuity and reconstruction

Own:

    durable development knowledge
    current project state
    authority/maturity distinctions
    continuity/recovery entry
    knowledge navigation
    dependency/supersession awareness
    cold-start reconstruction
    historical reasoning sufficient to resume work correctly

Why durable:

The repository must outlive any chat/model session and remain reconstructable.

This responsibility does not preselect Markdown, docs/, Research/ or any current hierarchy.

### J04. Project-development control system

Own the project-local system that helps govern development itself, including candidate responsibilities such as:

    project-development state
    activation/orchestration
    workstreams
    accepted-obligation tracking
    control/guard semantics
    architecture-evolution activation
    collaboration routing
    Git lifecycle controls
    recovery/continuity support
    deterministic project views
    project-system instance policy

Why durable:

This is the responsibility class investigated by PSMF.

Its exact local boundary and name remain open.

### J05. Research, experimentation and qualification

Own:

    architecture/product research
    hypothesis formation
    experiment protocols
    controlled comparisons
    qualification evidence
    falsification programs
    experiment lifecycle
    result acceptance
    reproducibility of load-bearing evidence

Why durable:

ADS deliberately develops through evidence, not feature accumulation or aesthetic architecture preference.

### J06. Verification and quality engineering

Own project-development assurance for:

    unit/contract/integration/system tests
    acceptance gates
    regression suites
    static analysis
    compatibility checks
    repository integrity
    cross-workspace qualification
    product-behavior evaluation
    release-quality evidence

Why durable:

Verification is not one folder. It is a project responsibility spanning local and cross-system tests.

### J07. Repository, workspace and build engineering

Own:

    repository bootstrap
    workspace orchestration
    package/build configuration
    dependency tooling
    developer commands
    code generation where justified
    build caches/artifacts policy
    CI execution architecture
    repository-wide engineering conventions
    toolchain interoperability

Why durable:

As ADS grows into multiple workspaces, repository engineering becomes explicit infrastructure rather than incidental scripts.

### J08. Secure development and software-supply-chain governance

Own project-development controls for:

    secure development practices
    secret handling in development
    dependency risk
    vulnerability response
    software provenance
    build provenance
    artifact integrity/signing where justified
    third-party license/compliance tracking
    branch/review protections
    security scanning
    incident learning

Why durable:

Professional secure development is a lifecycle responsibility distinct from runtime product security.

### J09. Release, change and configuration management

Own:

    version/release policy
    release qualification
    release notes/change records
    supported-version policy
    compatibility/migration planning
    artifact publication
    deployment promotion policy
    rollback/change control
    configuration baselines

Why durable:

A professional product eventually needs controlled movement from development state into released/operational state.

### J10. Contributor, agent and collaboration workflow

Own:

    human contribution workflow
    model/agent collaboration contracts
    code-review/research-review workflow
    issue/task/workstream collaboration
    permissions and bounded write ownership
    handoffs
    external contribution policy
    professional developer-workbench integration on the development side

Why durable:

ADS is already multi-model and may become multi-contributor. Collaboration semantics should not depend on one chat provider.

### J11. Development environments and project operations

Own:

    local development setup
    reproducible developer environments
    project-specific runtime bridges
    test/research execution infrastructure
    development observability
    CI operational health
    environment diagnostics
    development backup/recovery where needed
    private/public operational separation

Why durable:

The development system itself must be operable and recoverable.

This does not preserve current local_execution or private_companion structures.

### J12. Historical preservation and archival lifecycle

Own:

    retired prototypes
    superseded executable programs worth retaining
    historical evidence
    archival metadata
    preservation/retirement decisions
    ability to distinguish active architecture from historical truth

Why durable:

Long-lived professional projects accumulate valuable but inactive material that should neither disappear nor remain active-peer architecture forever.

## 7. Explicit Product / Project cross-plane splits

The following concerns intentionally appear in both planes and must not be collapsed into one generic folder.

### Security

    product:
        runtime identity, authorization, data protection, provider permissions

    project:
        secure SDLC, dependency/supply-chain controls, developer secrets,
        vulnerability response

### Observability

    product:
        runtime execution and product health telemetry

    project:
        CI/build/research/project-control observability

### Deployment and release

    product:
        deployable/runtime artifacts and runtime configuration semantics

    project:
        release qualification, promotion, versioning, publication and rollback process

### Evaluation

    product:
        methodological validity, claim/evidence assurance and human-control semantics

    project:
        product-quality tests, benchmarks, experiment protocols and release evidence

### Integrations

    product:
        integrations needed by ADS users/projects at runtime

    project:
        integrations used to build, test, govern or collaborate on ADS

### Knowledge

    product:
        knowledge ADS operates on as part of its functionality

    project:
        knowledge about developing/governing ADS itself

### Contracts

    owner follows specified behavior/authority;
    consumption does not create ownership.

Only irreducible cross-plane integration contracts may reach true root under A1.

## 8. Anti-anchoring probe results

Research 248 required testing future responsibilities that current folders may not represent clearly.

### Deployment / release

Represented explicitly by P12/J09.

### Observability

Represented explicitly by P12/J11.

### Security

Represented explicitly by P11/J08.

### Provider integration

Represented by P10 for runtime providers and J07/J10/J11 for development-side providers.

### Cross-plane contracts

Handled by accepted A1 rather than a shared miscellaneous subsystem.

### Environment/runtime orchestration

P06/P12 for product execution; J07/J11 for development execution.

### Benchmark/evaluation assets and verdicts

P07 owns runtime assurance semantics; J05/J06 own product-development evaluations and accepted evidence.

### Product data/model assets

P01/P04/P06/P09 collectively own their semantics, lineage, execution and persistence. A separate top-level "models" responsibility is not yet justified.

### Repository engineering

Explicit J07.

### Cold-start/reconstruction

Explicit J03 plus accepted true-root entry contract.

No anti-anchoring probe requires a third Level-1 plane at this stage.

## 9. True-root inventory bound preregistration

Before any target root inventory is populated, R6 preregisters:

    ROOT_ENTRY_REVIEW_BOUND = 12 tracked first-level entries

Counting rule:

    count every tracked first-level file or directory at repository root
    in the proposed target

    product/ counts
    project/ counts
    host/tool/bootstrap files count
    workspace orchestrator files count
    lockfiles count

Exclude only:

    .git internal state
    untracked local caches
    untracked generated/runtime scratch
    external filesystem material not part of the repository target

Reason for 12:

    the accepted root has only five legitimate responsibility classes;
    a healthy target should therefore remain in the single-digit to
    low-teens range even after real tool anchors are accounted for.

    12 provides room for product/, project/, host integration,
    human/machine cold-start anchors and genuine workspace/tool anchors
    without making "tooling needs it" an unlimited escape hatch.

This is a review bound, not an aesthetic hard failure.

If the future target needs more than 12 tracked first-level entries:

    stop
    classify every excess entry
    determine whether tooling genuinely forces it
    determine whether root classes are incomplete
    determine whether one or more entries should move under product/project
    explicitly amend the bound or architecture if evidence justifies it

Expected healthy target:

    <= 10 entries

but 12 is the preregistered architecture-review trigger.

## 10. What R6-A deliberately does not decide

This responsibility model does not decide:

    folder names below product/ or project/
    package names
    workspace count
    whether frontend remains one workspace
    whether current ads_system remains one workspace
    whether project-development control is one or several workspaces
    where any current document moves
    the future project information hierarchy
    testing folder topology
    schema folder topology
    experiment directory topology
    deployment technology
    cloud provider
    observability stack
    security product
    monorepo tool
    package manager changes

Those are later boundary and realization questions.

## 11. Boundary-synthesis criteria for the next R6 step

A responsibility cluster may become a bounded subsystem/workspace only when enough of the following are true:

    coherent primary responsibility
    stable authority/ownership contract
    high internal semantic cohesion
    meaningful dependency boundary
    independent lifecycle/change pressure
    independent qualification surface
    independent toolchain/build need
    reusable or separately deployable boundary where relevant
    security/permission isolation where relevant
    operational/recovery boundary
    projected future coupling supports separation

A current folder or package is not evidence by itself.

A responsibility need not become a workspace merely because it has a name in this research.

## 12. Current state

    R6_A_RESPONSIBILITY_MODEL=FROZEN
    PRODUCT_RESPONSIBILITIES=12
    PROJECT_RESPONSIBILITIES=12
    THIRD_LEVEL1_PLANE_REQUIRED=NO
    ROOT_ENTRY_REVIEW_BOUND=12
    EXPECTED_HEALTHY_ROOT_ENTRIES=10_OR_FEWER
    CURRENT_TREE_USED_AS_TARGET_INPUT=NO
    CURRENT_TREE_MAPPING_AUTHORIZED=NO
    WORKSPACE_BOUNDARIES=UNRESOLVED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R6_A_RESPONSIBILITY_COUPLING_AND_BOUNDED_CONTEXT_SYNTHESIS
