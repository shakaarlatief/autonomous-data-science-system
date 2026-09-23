# Research 273: R8-C0 From-Scratch Assurance Requirements, Claim Model, Failure Model, and Design Protocol

**Date:** 2026-09-23
**Status:** ASSURANCE REQUIREMENTS FROZEN / MECHANISM SELECTION NOT STARTED / CURRENT TEST-CI-CD TOPOLOGY HAS NO PRESERVATION RIGHT / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**R8-A:** Research 259, accepted as amended
**R8-B:** Research 272, WMR-H V0.3 accepted
**Assurance freedom clarification:** Research 262
**Scope:** Derive the future verification / assurance / testing / CI-CD / delivery requirements from required system behavior and failure modes before selecting frameworks, directories, providers, workflow topology, branch controls, release tooling, deployment tooling or aggregate commands.
**Authority:** Requirements and design-protocol freeze only. This research does not select the final assurance architecture or authorize migration.

## 1. Why this stage exists

The project owner explicitly clarified that every current assurance mechanism is redesignable:

    tests
    validators
    repository checks
    integrity aggregators
    CI workflows
    CD/deployment machinery
    pytest topology
    GitHub Actions topology
    required-check shape
    current PASS labels

Research 262 froze the corresponding anti-anchoring rule:

> Verification requirements and accepted historical evidence may survive; verification mechanisms do not survive by inertia.

Research 272 made this a downstream requirement of accepted R8-B.

The representation probe itself then supplied strong negative evidence for mechanism-first assurance:

    a check can have the correct name
    a check can return PASS
    a check can contain expected concepts
    and the check can still fail to exercise the claimed invariant

Therefore the target assurance architecture must be claim-driven and evidence-driven.

## 2. Current mechanism inventory is evidence only

At this checkpoint the tracked repository contains:

    GitHub Actions workflow YAML files      34
    check/integrity/normalization scripts   17
    tracked Python tests                     65
        unit                                 54
        integration                          11

The workflow inventory includes permanent-looking repository checks together with many experiment-, prototype-, spike-, calibration- and V1-specific workflows.

The Python test inventory similarly mixes:

    Product reasoning/context behavior
    Source Universe substrate/recovery
    Project-knowledge semantic/control behavior
    migration/shadow qualification
    repository integrity
    collaboration/routing/continuity
    experiment harnesses and live runners

This is useful historical and invariant-discovery evidence.

It is not a target decomposition.

## 3. Current invariant examples extracted before replacement

The current aggregate repository-integrity path demonstrates that the project presently protects behaviors such as:

    numbered identity uniqueness
    family/header consistency
    selected metadata presence
    declared-reference validity
    legacy validation-evidence preservation
    Project-knowledge semantic validation
    checkpoint metadata integrity
    Knowledge Map integrity
    model-collaboration state validity
    current-routing consistency

Current tests additionally protect behaviors such as:

    Project-knowledge authority resolution
    identity transition behavior
    capture/promotion behavior
    generated-view behavior
    compatibility/shadow behavior
    state/core reconstruction behavior
    privacy/public-boundary behavior
    Source Universe persistence/recovery
    Product reasoning/context selection
    live-experiment launcher safety
    repository-integrity aggregation

These are candidate invariants.

Each must still be re-evaluated against the accepted future architecture.

The extraction obligation is:

    current mechanism
        ->
    actual enforced invariant
        ->
    future relevance classification
        ->
    successor claim
        or explicit retirement reason

No current implementation receives survival rights from this extraction.

## 4. Assurance objective

The future assurance system must answer:

> What evidence is sufficient to justify a specific claim about a specific version of ADS, at a specific lifecycle boundary, under explicit trust and failure assumptions?

The primitive unit is therefore not:

    test file
    workflow
    CI job
    check script

It is:

    ASSURANCE CLAIM

with at least:

    subject
        what object/version/environment is being claimed about

    invariant or property
        what must hold

    evidence class
        what kind of observation can support the claim

    evidence binding
        which source/artifact/state/version the evidence applies to

    trust boundary
        which actors/systems are trusted to produce/verify it

    lifecycle gate
        where the claim matters

    failure semantics
        block / quarantine / review / advisory / observe

    freshness
        when evidence expires or becomes stale

    owner
        Product / Project System / Project Engineering / root host integration

## 5. Assurance claim families

The target architecture must be able to represent and execute at least the following claim families.

### AC1 Product functional correctness

Examples:

    deterministic domain logic
    public APIs and contracts
    orchestration behavior
    analytical execution behavior
    interaction/client behavior

### AC2 Product quality and AI/data-science behavior

Examples:

    stochastic or model-dependent behavior
    retrieval/reasoning quality
    methodological quality
    calibration
    statistical properties
    representative task performance
    regression against accepted baselines

Software unit tests alone are insufficient for this class.

### AC3 Project Development System semantic correctness

Examples:

    authority resolution
    identity
    lifecycle
    transition semantics
    routing
    orchestration/control behavior
    generated-view correctness
    declaration/metadata interpretation
    revision/concurrency rules

JW1 owns the semantic mechanisms being validated.

### AC4 Repository/workspace architecture integrity

Examples:

    Product does not depend on Project for runtime correctness
    independent Product/Project dependency resolution
    allowed dependency direction
    root-entry bound
    workspace boundaries
    no accidental cross-plane coupling
    no forbidden generated/canonical inversion

### AC5 Representation and information integrity

Examples:

    governed-carrier recognition
    source/state pairing
    reference integrity
    provenance preservation
    generated-view rebuildability
    derived-state freshness
    no unique accepted truth in caches
    rule-based/loss-accounted migration

### AC6 Compatibility and migration integrity

Examples:

    old/new behavioral equivalence where required
    intentional divergence explicitly dispositioned
    shadow-read equivalence
    identity preservation
    reference/path integrity
    reversible transition steps
    cutover readiness

### AC7 Build and dependency integrity

Examples:

    reproducible dependency resolution
    source-to-artifact traceability
    dependency-policy conformance
    build inputs identified
    generated artifacts attributable to exact source/configuration

### AC8 Security, privacy, and public/private boundary

Examples:

    secret/private-data non-disclosure
    least-privilege mutation surfaces
    dependency/supply-chain risk
    insecure configuration
    unsafe parsing/deserialization
    permission-manifest correctness
    public/private companion separation

### AC9 Artifact and release provenance

Examples:

    artifact bound to source revision
    qualification evidence bound to artifact
    release content integrity
    immutable release identity
    promotion does not silently rebuild a different artifact

### AC10 Mutation and live-operation safety

Examples:

    stale-write rejection
    exact-target mutation
    idempotency where required
    no uncertain duplicate mutation
    preflight/postflight consistency
    safe retry classification
    bounded rollback/recovery

### AC11 Runtime reliability and observability

Examples:

    health/readiness
    error-rate and latency expectations
    failure visibility
    dependency degradation
    recovery behavior
    evidence that runtime state matches deployed version

Exact SLOs remain future Product/runtime decisions.

### AC12 Recovery and continuity

Examples:

    cold start from stable anchor
    derivative-free reconstruction
    backup/restore
    rollback
    disaster/recovery drill
    collaboration handoff distinct from operational recovery

### AC13 Research and experiment integrity

Examples:

    preregistration where confirmatory claims require it
    immutable fixture/boundary binding
    no threshold change after observation
    negative controls
    harness validity
    result provenance
    explicit INCOMPLETE / INVALID classifications

### AC14 Human-review and governance integrity

Examples:

    material architecture decisions receive required owner disposition
    review requirements cannot be silently bypassed
    evidence and decision event remain distinguishable
    acceptance applies to named scope/version only

### AC15 Delivery and deployment integrity

Examples:

    release promotion gates
    environment-specific configuration validation
    deployment identity
    post-deployment verification
    rollback availability
    no implicit production mutation from unrelated repository activity

Deployment provider and environment topology remain open.

## 6. Lifecycle gates

Assurance must be designed across lifecycle boundaries rather than as one undifferentiated CI run.

### LG0 Authoring / local feedback

Purpose:

    fast defect discovery
    deterministic formatting/static/schema/contract feedback
    focused Product or Project-system tests

No provider assumption.

### LG1 Change / pre-merge qualification

Purpose:

    establish that a proposed repository change satisfies the claims
    required before integration

Must support affected-scope selection without allowing unsafe under-testing.

### LG2 Integrated mainline qualification

Purpose:

    validate properties that require the integrated repository state

Must catch cross-workspace and cross-change interactions.

### LG3 Build / artifact qualification

Purpose:

    bind build outputs to exact source, dependency and build inputs
    and produce artifact-specific evidence

### LG4 Release-candidate / promotion gate

Purpose:

    determine whether an immutable candidate is releasable

Must distinguish:

    source qualification
    artifact qualification
    release authorization

### LG5 Deployment / activation gate

Purpose:

    verify exact target, environment, configuration and mutation authority
    before changing a live environment

### LG6 Post-deployment / live qualification

Purpose:

    confirm deployed identity and bounded runtime behavior

Must support rollback/escalation on failure.

### LG7 Migration / authority-cutover gate

Purpose:

    prove migration-specific equivalence, intentional divergence,
    reference integrity, reconstruction and rollback before authority switch

This gate is required before W5 physical cutover.

### LG8 Recovery / rollback gate

Purpose:

    verify that recovery mechanisms actually restore usable authority/system state

A documented recovery procedure without exercised evidence is insufficient
for claims that depend on recoverability.

### LG9 Scheduled / continuous assurance

Purpose:

    detect drift, dependency/security changes, stale evidence,
    expired credentials/permissions, recovery decay and other conditions
    that can become false without a source commit

Exact cadence remains mechanism-specific.

## 7. Evidence classes

Mechanism selection must be able to compose multiple evidence classes.

    EC1 static/source analysis
    EC2 schema/contract validation
    EC3 deterministic unit/component behavior
    EC4 integration behavior
    EC5 end-to-end/system behavior
    EC6 property/invariant and negative-control testing
    EC7 differential/shadow/equivalence testing
    EC8 migration/reconstruction/recovery drills
    EC9 empirical/statistical/AI evaluation
    EC10 adversarial/security testing
    EC11 live/canary/post-deployment observation
    EC12 artifact/provenance/attestation evidence
    EC13 human review/approval
    EC14 historical/audit evidence

A claim may require more than one class.

No evidence class is globally superior.

## 8. Failure semantics

Every assurance claim must predeclare its consequence class.

### FS1 BLOCK

Failure prevents the governed transition.

Use where proceeding would violate a required invariant or create unacceptable uncertainty.

Typical domains:

    authority
    identity
    unsafe mutation
    release integrity
    migration cutover
    public/private leakage
    critical architecture boundary

### FS2 QUARANTINE

The output/change may exist but cannot be promoted or treated as accepted.

Useful for:

    experimental artifacts
    suspect build outputs
    incomplete migration evidence

### FS3 REVIEW_REQUIRED

Automated evidence is ambiguous or a bounded threshold has been crossed.

A human or governed decision path is required.

### FS4 ADVISORY

Evidence informs quality improvement but does not currently block.

An advisory claim must not masquerade as a blocking guarantee.

### FS5 OBSERVATIONAL

Evidence is collected for diagnosis/research only.

It creates no acceptance claim by itself.

## 9. Flakiness, nondeterminism, and retries

A blocking check must not become green merely because it was retried until it passed.

Rules:

    deterministic claims
        repeated disagreement is a defect in the system or harness

    stochastic/AI claims
        must specify sampling, uncertainty and acceptance criteria appropriate
        to the claim before observation

    retry
        may diagnose infrastructure/transient failure
        but must not erase the original failure classification

    mutation
        uncertain completion must never be blindly retried if duplication
        is possible

The project must distinguish:

    CLAIM FAILURE
    HARNESS FAILURE
    INFRASTRUCTURE FAILURE
    MUTATION UNCERTAINTY
    INCOMPLETE EVIDENCE

This distinction is already supported by the representation-probe history.

## 10. Evidence binding and freshness

Every blocking or release-relevant result must be bound to the subject it qualifies.

Depending on claim type, binding may include:

    source commit
    tree/content digest
    dependency lock
    build/artifact digest
    schema/profile version
    fixture/corpus digest
    environment/configuration identity
    migration manifest version
    provider/runtime identity

Evidence must fail stale rather than silently apply to changed inputs.

Derived evidence must identify:

    authoritative inputs
    generator/assurance mechanism version
    freshness boundary

## 11. Ownership model

Accepted R6/R8-A boundaries remain the starting point.

### Product workspaces

Own:

    Product-local functional tests
    Product-local contract tests
    Product-local quality/evaluation fixtures where the Product owns them
    Product implementation-specific build behavior

### JW1 / project/system

Owns:

    semantic validation mechanisms for Project-system semantics
    representation/control-state semantics
    reconstruction/activation/orchestration semantic validation

### project/engineering

Owns:

    repository architecture validation
    cross-workspace qualification
    assurance orchestration
    test/build tooling that is Project-owned
    CI execution architecture
    release/delivery engineering
    security/supply-chain engineering
    migration qualification orchestration

Engineering may invoke JW1 semantic validators.

JW1 must not depend on engineering.

### true root / host integration

May own only provider/host-required integration anchors.

Provider-specific workflow configuration at root-host scope does not make the provider the semantic owner of assurance.

## 12. Product/Project dependency rule for assurance

The operational Product must remain independently runnable without Project-plane assurance machinery.

Therefore:

    Product runtime
        must not import or require project/system or project/engineering

while:

    Project assurance
        may build, test, inspect, qualify and release Product

Product-local test utilities that are required for Product development may remain Product-owned.

Cross-repository orchestration remains Project-owned.

## 13. Migration-oracle protocol

Before a current validator/check/workflow is removed or replaced:

    1. identify the actual invariant(s) it enforces
    2. identify historical evidence that depends on it
    3. classify each invariant:
           RETAIN
           AMEND
           SUPERSEDE
           RETIRE
    4. map retained/amended invariants to successor claims
    5. run old and successor mechanisms in shadow where comparison is meaningful
    6. reconcile divergences
    7. release the old mechanism only after explicit cutover qualification

No requirement exists for output-text parity or workflow-name parity.

The required parity target is the accepted invariant/claim, unless an explicit amendment intentionally changes it.

## 14. Mechanism-selection criteria

Later candidate architectures must be compared on:

    semantic coverage
    falsifiability
    failure isolation
    local feedback speed
    CI scalability
    determinism
    stochastic-evaluation correctness
    trust-boundary clarity
    evidence binding
    provenance
    cross-platform behavior
    Product/Project separation
    secure secret/permission handling
    migration compatibility
    debuggability
    flake resistance
    artifact/report retention
    recovery
    provider portability where valuable
    operational complexity
    cost/time efficiency

Prestige or popularity is not a decision criterion by itself.

## 15. External professional cross-checks

These sources are evidence and vocabulary cross-checks, not imported target architecture.

### NIST SSDF

NIST SP 800-218 Version 1.1 is the current final SSDF publication.

It frames secure software development as practices integrated across the SDLC and includes release-integrity verification.

Official source:

    https://csrc.nist.gov/pubs/sp/800/218/final

NIST published an initial public draft of SSDF Version 1.2 in December 2025 covering secure and reliable development, delivery and improvement.

Because it is a draft, it is directional evidence only.

    https://csrc.nist.gov/pubs/sp/800/218/r1/ipd

### SLSA

SLSA Version 1.2 is the current approved specification.

Its Build and Source tracks reinforce explicit provenance, expected-process verification and artifact/source traceability.

    https://slsa.dev/spec/v1.2/

This supports the requirement for source/artifact/evidence binding without requiring ADS to claim a particular SLSA level.

### NIST AI RMF / TEVV

NIST AI RMF 1.0 remains published while revision work is ongoing.

The NIST AI Resource Center explicitly treats testing, evaluation, verification and validation as part of operationalizing AI risk management.

    https://www.nist.gov/itl/ai-risk-management-framework
    https://airc.nist.gov/

NIST's 2026 TEVV-Athlon draft is relevant directional evidence because it explicitly targets customizable evaluation across statistical ML, LLMs, multimodal and agentic systems.

Because it is an initial public draft, it is not adopted as authority.

## 16. What remains deliberately open

This research does NOT select:

    pytest versus another test framework
    test directory topology
    coverage tooling
    linter/type checker/static analyzer
    GitHub Actions versus another CI provider
    workflow count
    reusable-workflow topology
    branch protection configuration
    required status-check names
    cache provider
    artifact store
    SBOM format
    attestation implementation
    signing mechanism
    secret manager
    deployment provider
    environment model
    release versioning scheme
    observability vendor
    container technology
    Kubernetes
    cloud platform
    monorepo tooling
    CD product
    exact time/cost budgets

These are downstream realization choices.

## 17. Required next design step

The next step is independent assurance-architecture candidate design against this frozen requirement model.

To reduce anchoring:

    ChatGPT and Claude should independently derive target assurance architectures
    before seeing each other's proposed topology.

Each candidate must cover:

    claim representation
    lifecycle gates
    local feedback architecture
    Product test ownership
    JW1 semantic validation
    project/engineering orchestration
    cross-workspace qualification
    migration/shadow qualification
    security/supply-chain assurance
    build/release provenance
    CI logical topology
    CD/deployment logical topology
    failure/retry/flaky policy
    evidence publication/retention
    migration from current mechanisms
    provider-specific integration boundary

Only after independent candidates are frozen should a comparative synthesis select exact mechanisms/topology.

## 18. Current state

    R8A=ACCEPTED_AS_AMENDED
    R8B=WMR_H_V0_3_ACCEPTED

    R8C0_ASSURANCE_REQUIREMENTS=FROZEN
    ASSURANCE_PRIMITIVE=CLAIM_PLUS_BOUND_EVIDENCE
    ASSURANCE_CLAIM_FAMILIES=15
    LIFECYCLE_GATES=10
    EVIDENCE_CLASSES=14
    FAILURE_SEMANTICS=5

    CURRENT_WORKFLOWS=34_EVIDENCE_ONLY
    CURRENT_CHECK_SCRIPTS=17_EVIDENCE_ONLY
    CURRENT_PYTHON_TESTS=65_EVIDENCE_ONLY

    CURRENT_ASSURANCE_TARGET_PRESERVATION_RIGHT=false
    CURRENT_ASSURANCE_MIGRATION_ORACLE_OBLIGATION=true
    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

    ASSURANCE_MECHANISM_SELECTION=NOT_STARTED
    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=INDEPENDENT_ASSURANCE_ARCHITECTURE_CANDIDATES
