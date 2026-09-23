# Research 274: ChatGPT Independent R8-C Assurance Architecture Candidate FACET

**Date:** 2026-09-23
**Status:** CHATGPT INDEPENDENT ASSURANCE CANDIDATE FROZEN / CLAUDE CANDIDATE NOT READ / NO OWNER DECISION / NO PHYSICAL MIGRATION
**Parent requirements:** Research 273
**Independent evidence base:** cac7a699eb012c5a02e1c5fab349ebc9e5726145
**Collaboration protocol:** MC-0028
**Candidate name:** FACET
**Expansion:** Federated Assurance Claims, Evidence, and Transitions
**Scope:** Independently derive a target verification / assurance / testing / CI-CD / delivery architecture before reading Claude's MC-0028 candidate.
**Authority:** Independent architecture candidate only.

## 1. Independence declaration

This candidate was derived from Research 273 and accepted upstream architecture before Claude MC-0028 Message 001 was read.

    CLAUDE_MC0028_MESSAGE001_READ=false

Current mechanisms are evidence only.

## 2. Core conclusion

A claim-first architecture is necessary but not sufficient.

FACET gives five concepts separate identities:

    CLAIM
        what must be true

    VERIFIER
        mechanism that can produce evidence about the claim

    PROFILE
        claims/trust levels required for a lifecycle transition

    EVIDENCE
        version-bound observation produced by a verifier

    DECISION
        deterministic evaluation of a profile over evidence

An execution planner coordinates these objects but is not semantic authority.

This prevents:

    test name = contract
    workflow = policy
    provider = assurance authority
    unbound PASS text = acceptance
    release logic hidden in CI wiring

## 3. Architecture layers

### F1 Assurance contracts

Stable semantics:

    claim ID
    natural owner
    subject type
    required evidence class
    failure semantics
    freshness
    minimum trust class
    dependencies where needed

Claims are selective.

Ordinary unit tests do not each become first-class claim records.

Use first-class claims for blocking, cross-component, release, migration, authority, security or durable governance properties.

### F2 Federated verifiers

Verifier implementation stays with semantic owner.

    Product
        functional/contract/integration tests
        Product-owned AI/statistical evaluation

    project/system / JW1
        authority, identity, routing, lifecycle, representation and
        activation/orchestration semantic validation

    project/engineering
        repository/cross-workspace validation
        build/release
        security/supply chain
        migration/recovery orchestration

A verifier has a stable logical ID/version.

Framework choice remains open.

### F3 Profiles

Initial semantic profile family:

    local-fast
    change
    mainline
    release
    deploy
    migration-cutover
    recovery-drill
    scheduled-drift

Profiles are not workflow names.

### F4 Planner / execution graph

Project Engineering owns planning.

Inputs:

    profile
    exact source revision
    change scope when applicable
    dependency/impact graph
    execution environment
    explicitly reusable fresh evidence

Output:

    verifier DAG

Rule:

> Uncertain affected-scope analysis for a blocking claim expands qualification rather than silently skipping the claim.

Engineering may invoke Product and JW1 verifiers.

JW1 must not depend on Engineering.

### F5 Evidence plane

Meaningful results emit a structured evidence envelope with at least:

    schema/version
    claim ID
    verifier ID/version
    subject identity
    source/tree digest
    relevant dependency/build/fixture digest
    environment/trust class
    outcome classification
    evidence references
    freshness/expiry where relevant

Required outcome classes:

    PASS
    FAIL
    INCOMPLETE
    HARNESS_ERROR
    INFRASTRUCTURE_ERROR
    MUTATION_UNCERTAIN

Storage is consequence-proportional.

Routine logs need not become canonical knowledge.

Release/migration/high-consequence decisions require durable evidence.

### F6 Gate evaluator

A deterministic evaluator consumes:

    profile
    exact subject/version
    bound evidence

and returns:

    PASS
    FAIL
    INCOMPLETE
    REVIEW_REQUIRED

Missing/stale required evidence never becomes PASS.

The gate emits a decision receipt with required claims, evidence selected, stale/missing evidence, trust class and result.

AO later consumes the gate decision as a transition precondition.

Assurance does not own AO workflow authority.

## 4. Ownership/topology direction

Recommended target direction:

    product/
        runtime/
            tests/
                unit/
                contract/
                integration/
                evaluation/

        interaction/
            web/
                tests/

    project/
        system/
            tests/
                semantic/
                reconstruction/
                activation/
                orchestration/

        engineering/
            assurance/
                contracts/
                profiles/
                planner/
                gate/
                evidence/
                providers/
                migration/
                security/
                release/
            tests/
                repository/
                cross_workspace/
                delivery/

        research/
            <research-only harnesses>

        reproductions/
            <admitted reproducible qualification assets>

Exact names remain amendable.

Ownership is the architecture.

## 5. Representation

WMR-H V0.3 supplies the representation model.

    human assurance rationale/policy
        Markdown

    selective machine-consumed claim/profile policy
        human-authored TOML

    verifier/evidence/gate schemas
        versioned JSON Schema

    machine evidence/decision receipts
        JSON

    generated indexes
        JSON and optional derived SQLite/FTS

No canonical assurance SQL database or graph database is required.

## 6. Local feedback

Local assurance must be useful without pretending to be trusted release evidence.

    local-fast
        schema/static/unit/focused contract checks

    local-full
        broader workspace integration/evaluation

Use the same verifier entrypoints as CI where practical.

Direct verifier invocation remains possible for diagnosis.

FACET requires semantic parity, not identical execution environments.

## 7. CI logical topology

Use a small logical profile family rather than one workflow per historical capability.

### Change qualification

PR/proposed change:

    repository architecture
    affected Product/JW1 tests
    contracts/schema
    security/static checks
    affected integration
    bounded stable AI/evaluation smoke evidence

### Mainline qualification

Integrated state:

    cross-workspace regression
    broader integration
    interactions hidden by affected-scope optimization

### Scheduled drift assurance

Time/provider/dependency driven:

    dependency/security drift
    model/provider drift
    stochastic evaluation drift
    recovery freshness
    credential/permission drift where relevant

### Release qualification

Explicit immutable candidate:

    controlled build
    artifact digest
    provenance
    required release claims
    release decision

### Deployment qualification

Explicit promotion of known artifact:

    environment/config validation
    exact target preflight
    deployment
    post-deployment verification
    rollback signal

### Migration/cutover qualification

Explicit transition:

    old/new shadow evidence
    identity/reference integrity
    reconstruction
    rollback
    authority-switch readiness

Physical workflow-file count is not architectural.

## 8. Stable host check interface

Branch protection or equivalent host policy should depend on a small stable gate interface rather than every verifier name.

A stable gate exposes structured subclaim detail so aggregation does not hide failures.

The current monolithic PUBLIC_REPOSITORY_INTEGRITY result may remain a migration oracle, but it does not define the future claim model.

## 9. Deterministic versus stochastic assurance

### Deterministic blocking claims

Must be:

    repeatable on equivalent inputs
    versioned
    bound to exact subject
    negative-control capable where useful
    failure-isolating

A flaky deterministic blocker does not count as satisfied.

### AI/statistical/stochastic claims

Bind:

    corpus/task version and digest
    provider/model/config when relevant
    prompt/system configuration when relevant
    seeds where meaningful
    sample count
    metrics
    threshold/baseline
    uncertainty method
    cost/time boundary

Profile placement is consequence-aware:

    change
        cheap stable smoke evaluation

    mainline
        broader regression evaluation

    scheduled
        drift-sensitive external/provider evaluation

    release
        representative decision-quality evaluation where warranted

No retry-to-green.

Confirmatory thresholds are set before observation.

## 10. Strong assurance of assurance

High-consequence claims should use stronger test forms where practical:

    property/invariant tests
    negative controls
    mutation testing of assurance logic
    corrupted-state fixtures
    differential/shadow checks
    failure-path tests

Especially for:

    authority
    migration
    concurrency
    stale-write protection
    parser recognition
    privacy/security boundary
    gate evaluator

Universal mutation testing is not required.

## 11. Security and supply chain

Integrated claim families include:

    secret/private-data exposure
    least-privilege workflow permissions
    dependency vulnerability/policy
    external action/dependency integrity
    source revision governance
    build provenance
    artifact integrity
    permission-manifest correctness
    unsafe parsing/deserialization

Logical rules:

    untrusted PRs receive no unnecessary secrets
    jobs receive least privilege
    dependency/action versions are policy controlled
    Product and Project locks are validated independently
    release artifact is traceable to exact source/build inputs

Exact scanners, SBOM, signing and attestation tools remain open.

FACET does not claim a SLSA level merely by design.

## 12. Build, release, and CD

FACET selects the logical rule:

> Build a release candidate once, identify it immutably, qualify that artifact, and promote the identified artifact instead of silently rebuilding different bits per environment.

Release evidence binds:

    source/tree
    dependencies
    build recipe
    builder/trust context
    artifact digest
    required test/evaluation evidence

Delivery flow:

    candidate
        -> immutable build
        -> release profile
        -> release decision
        -> exact artifact + environment config
        -> deploy preflight
        -> guarded mutation
        -> post-deploy verification
        -> healthy promotion / rollback / review

Rules:

    PR activity does not implicitly deploy production
    deployment requires exact target identity
    mutation uncertainty blocks blind retry
    environment config is validated separately
    rollback target exists before high-consequence deployment

Provider/environment topology remains open.

## 13. Evidence trust classes

Suggested logical trust classes:

    SELF
        developer/local evidence

    REPOSITORY_CI
        controlled repository CI on exact source revision

    RELEASE_BUILDER
        governed build/provenance context

    TARGET_ENVIRONMENT
        live/deployed target observation

Profiles may require minimum trust by claim.

This prevents local PASS from being treated as equivalent to release evidence.

## 14. Evidence retention

Consequence-proportional retention:

    ephemeral
        ordinary unit logs, caches, intermediate data

    bounded CI retention
        integration/evaluation/security reports

    durable release evidence
        artifact digest/provenance + release gate decision

    durable migration/governance evidence
        cutover, recovery, owner/authority receipts

WMR-H immutable JSON receipts fit the durable class.

Raw logs do not become canonical Project knowledge by default.

## 15. Recovery assurance

Recovery is an exercised capability.

Separate:

    human recovery procedure
    executable recovery verifier/drill
    bound recovery evidence

Claims may cover:

    stable-anchor reconstruction
    generated-layer rebuild
    backup restore
    artifact rollback
    authority-state reconstruction
    environment recovery

## 16. Migration from current assurance

Create a claim-mapping manifest for every current:

    test family
    check script
    integrity validator
    workflow
    live qualification harness

Map:

    current mechanism
    actual invariant
    future claim
    disposition:
        RETAIN_IMPLEMENTATION
        REWRITE
        MERGE
        SPLIT
        REPLACE
        RETIRE
        HISTORICAL_ONLY
    shadow requirement
    retirement gate

Historical experiment workflows should normally become HISTORICAL_ONLY once their live purpose is over.

Old/new shadow comparison targets claims and violations, not output text/job count.

Divergence classifications:

    successor defect
    old mechanism defect
    intentional semantic change
    fixture mismatch
    harness failure

## 17. Provider boundary

FACET is provider-neutral at the semantic layer, without abstracting for abstraction's sake.

GitHub Actions remains a plausible implementation provider because the repository is hosted on GitHub.

But:

    workflow YAML
        host integration

    claim/profile policy
        Project-owned semantics

    verifiers
        natural owner

    gate/evidence schema
        provider-independent

If GitHub Actions survives, .github invokes Project-owned assurance interfaces rather than owning the semantics.

## 18. Cost, caching, and affected scope

Tier work by consequence:

    local-fast
    change
    mainline
    scheduled
    release
    migration

Exact numeric budgets follow measurement, not invention.

Caching is valid only under exact bound-input conditions.

For blockers:

    uncertain cache validity -> rerun

Affected-scope uncertainty similarly expands the run.

## 19. Self-validation

Critical assurance components must themselves be qualified:

    claim/profile parser
    planner
    affected-scope resolver
    gate evaluator
    evidence binding
    stale-evidence rejection
    provider adapters
    retry/mutation classifier

Use malformed, stale, missing, contradictory and mutation-test fixtures where consequence warrants it.

## 20. AO boundary

AO owns:

    project workflow state
    trigger handling
    transition authority

FACET owns:

    claims
    verifier execution
    evidence
    gate decision

Interface:

    AO requests/requires profile
        -> FACET emits exact bound decision
        -> AO checks subject/freshness
        -> transition may proceed

AO-10 can later persist/consume this interface using WMR-H.

## 21. Rejected alternatives

Rejected as core architecture:

    one monolithic repository gate
    one CI workflow per historical subsystem
    canonical central assurance database
    purely co-located tests with no Project coordination
    fully centralized tests divorced from owner
    universal blocking AI evaluation on every PR

Aggregate summary views remain useful.

## 22. Falsifiers

Amend/reopen FACET if:

    claim/profile policy becomes excessive bureaucracy
    first-class claims cannot remain selective
    federated verifier ownership fragments invocation unmanageably
    planner becomes a second build system
    affected-scope cannot fail safe
    evidence envelopes cause unacceptable churn
    stable gates hide critical failures
    local/CI semantic parity cannot be maintained
    provider adapters require large lowest-common-denominator abstractions
    stochastic evaluation cannot produce viable decision-quality evidence
    AO/FACET ownership becomes circular

## 23. Required probes before acceptance

After comparative synthesis, preregister bounded probes such as:

    P-A1 gate evaluator under missing/stale/contradictory evidence
    P-A2 affected-scope optimization plus uncertainty fallback
    P-A3 Product + JW1 + repository verifier locally and in CI
    P-A4 stochastic evaluation with preregistered threshold and no retry-to-green
    P-A5 artifact digest + provenance + release gate receipt
    P-A6 old repository-integrity oracle versus successor claims
    P-A7 infrastructure versus claim-failure classification
    P-A8 mutation test proving missing evidence cannot pass

## 24. Open exact choices

Still open:

    pytest retention/replacement
    lint/type/static security tools
    coverage policy
    GitHub Actions retention
    workflow count
    branch required-status count
    runner mix
    cache/artifact store
    signing/attestation technology
    SBOM format
    versioning
    deployment provider
    secret manager
    environment topology
    observability stack
    numeric latency/cost/coverage/evaluation thresholds

## 25. Candidate state

    CHATGPT_ASSURANCE_CANDIDATE=FACET
    INDEPENDENT_BASE=cac7a699eb012c5a02e1c5fab349ebc9e5726145
    CLAUDE_MC0028_MESSAGE001_READ=false

    ASSURANCE_PRIMITIVE=CLAIM_VERIFIER_PROFILE_EVIDENCE_DECISION
    EXECUTION=FEDERATED_VERIFIERS_THIN_PROJECT_ENGINEERING_PLANNER
    TEST_OWNERSHIP=NATURAL_SEMANTIC_OWNER
    CROSS_WORKSPACE_OWNER=PROJECT_ENGINEERING
    JW1_SEMANTIC_VALIDATION=RETAINED
    GATE_POLICY=PROFILE_DRIVEN
    EVIDENCE=SUBJECT_BOUND_AND_TRUST_CLASSIFIED
    STOCHASTIC_EVAL=SEPARATE_EVIDENCE_DISCIPLINE
    CD=IMMUTABLE_ARTIFACT_PROMOTION_WITH_GUARDED_MUTATION
    PROVIDER_SEMANTIC_AUTHORITY=false

    CURRENT_MECHANISMS=MIGRATION_ORACLES_UNTIL_RELEASED
    SPECIFICATION028=UNCHANGED
    AO10=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=CLAUDE_INDEPENDENT_CANDIDATE_THEN_COMPARATIVE_SYNTHESIS
