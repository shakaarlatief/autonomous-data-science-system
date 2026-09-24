# Research 275: MC-0028 FACET versus WARRANT Comparative Reconciliation and WARRANT-F V0.1 Candidate

**Date:** 2026-09-24
**Status:** INDEPENDENT CANDIDATES COMPARED / SYNTHESIZED ASSURANCE CANDIDATE FROZEN / CLAUDE COMPARATIVE CRITIQUE NEXT / NO OWNER DECISION / NO PHYSICAL MIGRATION
**Parent requirements:** Research 273
**ChatGPT independent candidate:** Research 274 / FACET
**Claude independent candidate:** MC-0028 Message 001 / WARRANT
**Independent base:** cac7a699eb012c5a02e1c5fab349ebc9e5726145
**Claude independent commit:** 76138e29ed4125bda21f1d9f8e46b34c89bfeef2
**Synthesized candidate:** WARRANT-F V0.1
**Expansion:** Warranted Federated Assurance
**Scope:** Compare the independently derived FACET and WARRANT assurance architectures, disposition their material differences, freeze a synthesis candidate, and define the bounded questions for comparative Claude review before empirical qualification or owner decision.
**Authority:** Comparative architecture candidate only. Nothing in this record accepts the final assurance architecture, changes Specification 028, implements AO-10, retires current assurance oracles, changes host protection, or authorizes physical migration.

## 1. Independence result

The independent-design protocol succeeded.

ChatGPT froze FACET in Research 274 before reading Claude Message 001.

Claude Message 001 states that the new Claude conversation read only the MC-0028 routing/contract material at branch head, which revealed FACET's name and existence but not its design, and used the frozen base for substantive design evidence.

Therefore the useful comparison is not between a proposal and a response to that proposal.

It is between two independently derived architectures sharing only:

    Research 273 requirements
    accepted upstream architecture
    accepted R8-B representation architecture
    current mechanism evidence
    prior MC-0027 assurance failure lessons
    professional standards cross-checks

## 2. High-level convergence

The convergence is unusually strong.

Both candidates independently select:

    claims as semantic units
    versioned verifiers
    exact subject/evidence binding
    federated semantic ownership
    Project Engineering as cross-workspace coordinator
    one deterministic adjudication/gate layer
    Product runtime independence from Project assurance
    JW1 ownership of its semantic validators
    provider configuration as adapter/integration rather than semantic authority
    local and hosted execution from the same logical assurance semantics
    consequence-proportional evidence retention
    explicit trust distinctions
    deterministic versus stochastic assurance separation
    preregistered AI/model evaluation campaigns
    no retry-to-green
    build-once / identify / qualify / promote
    guarded deployment with exact artifact/target identity
    migration-oracle extraction before replacing current checks
    old/new shadow comparison at invariant/claim level
    no canonical assurance SQL or graph database
    AO as consumer of assurance decisions rather than owner of verifier logic
    empirical qualification before owner acceptance

Neither candidate requires reopening the accepted Product/Project, JW1, R7 or WMR-H architecture.

The comparison is therefore a synthesis problem, not a competing-archetype selection.

## 3. Central difference: FACET stops one abstraction too early

FACET's primitive is:

    CLAIM
    VERIFIER
    PROFILE
    EVIDENCE
    DECISION

WARRANT adds:

    WARRANT
        why the verifier's evidence supports the claim
        plus executable sensitivity/specificity witnesses

This addition is materially justified by the strongest recent negative evidence in the project.

MC-0027 did not primarily fail because claims were missing.

It failed because checks bearing the right claim labels could not actually detect the defect class they claimed to test.

FACET partially addresses this in its "strong assurance of assurance" section through negative controls, property testing and mutation testing.

WARRANT makes that relationship explicit and governable.

Disposition:

    ADOPT WARRANT AS FIRST-CLASS

The synthesized primitive becomes:

    CLAIM
    VERIFIER
    WARRANT
    GATE POLICY / PROFILE
    EVIDENCE
    DECISION

The planner remains an execution mechanism, not semantic authority.

## 4. Warrant contract

WARRANT-F adopts the rule:

> A blocking or quarantining claim binding requires an active warrant. An active warrant must state why the verifier is relevant, what it does not cover, and executable evidence that the verifier can reject representative violations.

Default requirement:

    sensitivity witness
        seeded invalid case the verifier must reject

Where false positives are plausible:

    specificity witness
        near-miss valid case the verifier must accept

A verifier implementation, its declared inputs or its witness corpus changing invalidates the prior active warrant until re-witnessed.

An advisory/observational verifier may exist without a blocking-grade warrant, but it must be explicitly classified as unwarranted for blocking use.

This is deliberately strict at V0.1.

The later empirical program must test whether the warrant burden remains proportional across real ADS claims.

If it does not, the architecture must amend the rule rather than quietly accumulating ceremonial witnesses.

## 5. Claim semantics versus gate consequence

FACET uses profiles to determine which claims matter at a lifecycle transition.

WARRANT distinguishes:

    claim consequence floor
    gate-specific actual consequence

This is stronger because a durable property can carry a minimum seriousness while still becoming more stringent at a consequential transition.

Disposition:

    ADOPT WARRANT FLOOR + GATE BINDING
    RETAIN FACET PROFILE COMPOSITION

Therefore:

    CLAIM
        owns property meaning and consequence floor

    PROFILE / GATE POLICY
        selects claims
        chooses actual consequence >= floor
        chooses minimum trust tier
        chooses freshness requirements

This preserves Research 273's consequence classes without forcing one global consequence onto a claim.

## 6. Base-revision assurance ratchet

FACET did not make self-weakening prevention first-class.

WARRANT does.

This is accepted into the synthesis candidate.

For a candidate proposed against a protected target base:

    base rules
        remain effective

    candidate strengthening
        may apply immediately

    candidate weakening
        does not become effective merely because the candidate contains it

Weakening includes at least:

    removing a blocking claim
    lowering consequence
    relaxing threshold
    narrowing governed scope
    removing witness coverage
    lowering trust requirement
    disabling a required verifier
    widening waiver authority

A weakening requires a governed owner decision bound to the exact semantic policy diff.

Unknown/unclassifiable assurance-policy change fails closed as potential weakening.

This protects AC14 against the change weakening the mechanism used to judge itself.

The ratchet does not solve host-admin bypass.

That is a separate trust-boundary problem.

## 7. Trust model reconciliation

FACET proposed:

    SELF
    REPOSITORY_CI
    RELEASE_BUILDER
    TARGET_ENVIRONMENT

WARRANT proposed:

    T0 LOCAL_UNATTESTED
    T1 LOCAL_RECORDED
    T2 HOSTED_EPHEMERAL
    T3 HOSTED_ATTESTED

The WARRANT tier model is more operationally discriminating for current ADS.

Disposition:

    ADOPT WARRANT T0-T3 AS THE BASE TRUST MODEL

with one clarification:

> T2 means execution independent of the author's mutable local runtime state. Under the current shared Git-host identity/admin-capable integration model, it must not be described as authenticated independent human review or complete author-independent governance.

Thus:

    T0
        local feedback / observational

    T1
        exact clean recorded local execution
        useful for review and hosted-infeasible evidence

    T2
        fresh controlled hosted/ephemeral execution of exact subject
        minimum target tier for ordinary blocking promotion evidence

    T3
        T2 plus artifact/evidence provenance suitable for external consumption
        or live activation

Current host identity separation remains an open implementation/governance decision.

No SLSA source-review or two-party-review claim may be inferred from model-to-model review while all actors share the same underlying owner authority.

## 8. Federated ownership plus one adjudication kernel

FACET and WARRANT converge.

WARRANT-F freezes:

    semantic owners
        own claims
        own verifier meaning
        own verifier implementation
        own fixtures/witnesses whose semantics they own

    Project Engineering
        owns gate bindings
        assurance catalog
        planning
        adapters
        evidence normalization
        witness execution orchestration
        gate evaluation
        provider adapters
        cross-workspace qualification
        build/release/deploy engineering

    JW1
        owns Project-system semantic validation

    Product
        owns Product-local validation/evaluation

    Project Research
        owns research protocol/harness integrity and research campaign semantics

    root host integration
        contains provider triggers/adapters only
        no unique assurance semantics

One evaluator decides ADMIT / REFUSE / REVIEW_REQUIRED for governed gates.

Individual owners do not define incompatible meanings of "gate pass".

## 9. Adapter-at-consumer rule

FACET assumed stable logical verifier interfaces.

WARRANT makes the dependency seam more precise:

    owners may emit native result formats
    Project Engineering adapts those results into the common evidence model

This avoids Product or JW1 importing assurance-kernel code merely to satisfy Project Engineering.

Disposition:

    ADOPT CONSUMER-SIDE ADAPTER AS DEFAULT

A verifier may voluntarily emit the neutral evidence shape directly if doing so creates no forbidden dependency.

Direct emission is an optimization, not an ownership requirement.

## 10. Engineering Python environment

Claude correctly identifies that assurance architecture resolves a deferred R8-A question.

A real assurance kernel includes:

    catalog/policy loading
    planner
    adapters
    witness runner
    evaluator
    evidence handling
    provider integration

That is substantial executable Project Engineering code.

Three placements were considered:

    inside project/system
        rejected
        would couple JW1/PSMF to ADS-specific engineering dependencies

    root environment
        rejected
        would recreate root dependency coupling

    project/engineering independent Python project
        recommended

WARRANT-F therefore includes the prospective amendment:

    project/engineering/
        independently resolved Python project
        own pyproject
        own lock
        may invoke Product/JW1 through declared process/contract boundaries
        never a dependency of Product or JW1

This is:

    R8A_AMENDMENT_CANDIDATE=YES
    R8A_REOPEN=NO

It is not silently accepted by this research.

It must be part of the eventual owner assurance-architecture disposition.

## 11. Lifecycle shape

FACET's profiles and WARRANT's gates cover the same Research 273 lifecycle responsibilities.

WARRANT provides the cleaner semantic distinction between feedback, transitions and maintenance.

WARRANT-F adopts:

    F0 AUTHOR FEEDBACK
        no governed transition

    G1 CHANGE
        early hosted candidate feedback
        affected-scope/cached optimization allowed
        not sufficient to admit protected promotion

    G2 PROMOTE
        only blocking source-tree admission gate
        evaluates the exact tree that becomes protected head

    G3 ARTIFACT
        built bytes become qualified

    G4 RELEASE
        qualified artifact becomes releasable

    G5 ACTIVATE
        release enters target environment

    G6 LIVE
        activation becomes accepted or rollback is initiated

    G7 CUTOVER
        authority moves from old representation/mechanism to successor

    M1 DRILLS
        recovery/reconstruction evidence maintenance

    M2 REVALIDATE
        drift, security/dependency, expiry, hermeticity and selection audits

FACET profile names remain useful user-facing command/policy bundles.

They map onto this lifecycle rather than replacing it.

## 12. Exact-result promotion

Research 273 separated pre-merge and integrated-mainline qualification.

WARRANT's exact-result model is stronger if the enforcement mechanism can actually ensure the exact candidate tree is the protected-head result.

WARRANT-F adopts the semantic invariant:

> Blocking promotion evidence must qualify the exact tree that is proposed to become the protected head.

A check on a different pre-merge tree is not admissible for the promoted result.

After promotion, a bounded postflight must confirm:

    protected head == admitted subject

This preserves exact-result semantics for:

    fast-forward promotion
    precomputed merge results
    merge queues
    other future provider mechanisms

The implementation mechanism remains open.

If the host cannot enforce this invariant under the chosen promotion model, the architecture must retain a separate integrated qualification barrier rather than pretending the trees are equivalent.

## 13. Outcome model

FACET distinguishes PASS, FAIL, INCOMPLETE, HARNESS_ERROR, INFRASTRUCTURE_ERROR and MUTATION_UNCERTAIN.

WARRANT refines the same idea into attempt outcomes plus claim-at-gate states.

WARRANT-F adopts the two-level model.

Attempt outcomes:

    PASS
    FAIL
    HARNESS_INVALID
    INFRA_ERROR
    INCOMPLETE
    MUTATION_UNCERTAIN

Derived claim states:

    SATISFIED
    VIOLATED
    UNVERIFIED
    STALE
    UNWARRANTED
    NONDETERMINISTIC
    INCONCLUSIVE
    WAIVED

Only:

    SATISFIED
    WAIVED

can satisfy a BLOCK binding.

WAIVER must be:

    explicit
    owner-authorized
    scope-bound
    subject-bound
    time/expiry-bound where applicable

## 14. Stochastic / AI assurance

The candidates strongly converge.

WARRANT-F uses the more explicit three-layer model:

    L-A HARNESS CORRECTNESS
        deterministic
        blocking where the campaign depends on it

    L-B REPLAY REGRESSION
        deterministic recorded interactions
        validates orchestration/parsing
        does not prove live model quality

    L-C LIVE CAMPAIGN
        stochastic/live
        preregistered
        budgeted
        non-retry-to-green
        bound to model/provider/config/corpus/harness/judge identities

Campaigns record:

    sample design
    metrics
    uncertainty
    acceptance rule
    stopping rule
    budget
    negative controls

INCONCLUSIVE never rounds to PASS.

An LLM-as-judge is itself a verifier and must have a warrant/calibration basis appropriate to the claim.

Live campaigns do not run blindly on every source commit.

## 15. Architecture-boundary assurance

WARRANT adds a useful technique missing from FACET:

    absence execution

Static import checks cannot establish runtime independence by themselves.

The synthesis retains representative claims such as:

    Product succeeds when project/ is absent
    JW1 succeeds when project/engineering/ is absent
    PSMF framework works with an alternate fixture instance
    Product and Project resolve without one root lock

Each must have a negative witness proving the check notices a deliberately seeded forbidden dependency.

This is a strong direct test of accepted R6/R8 dependency semantics.

## 16. CI logical topology

FACET's small logical pipeline family and WARRANT's gate-specific job graph are compatible.

WARRANT-F freezes semantics, not workflow file count.

For a governed gate:

    PLAN
        resolve exact subject, effective policy, claims, trust and reuse

    EXECUTE
        owner verifiers in their own environments

    WITNESS
        re-witness changed blocking verifiers/warrants

    ADJUDICATE
        derive claim states and gate decision

    PUBLISH
        stable gate status
        human-readable detail
        bounded evidence/decision material

Provider configuration contains:

    triggers
    runner/resource choice
    checkout/bootstrap
    kernel invocation
    artifact/status transport

Provider configuration must not be the only home of:

    claim lists
    thresholds
    semantic scope
    gate consequence
    path-selection policy
    stochastic acceptance rules

The exact provider remains open.

GitHub Actions is currently plausible but not architecturally required.

## 17. Stable host interface

FACET and WARRANT converge on a stable host-facing status surface.

WARRANT-F rejects:

    one required host status per individual verifier

and rejects:

    one opaque repository-integrity PASS with no inspectable claim states

Target:

    a small stable status set at gate granularity
    with structured claim-level detail underneath

For example, a future host might require:

    assure/promote

while the underlying decision reports every required claim.

Exact status names/count are realization choices.

## 18. Evidence model and storage

Both candidates select exact subject-bound structured evidence.

WARRANT-F requires every decision-grade record to bind as relevant:

    claim
    warrant
    verifier/version/digest
    subject identity
    source/tree/blob basis
    lock/toolchain inputs
    artifact/environment/model identity
    fixture/corpus
    producer/trust tier
    attempt
    outcome
    raw-bundle digest
    freshness
    visibility

WMR-H remains the representation basis for durable JSON receipts.

One new constraint is accepted into the synthesis:

> Recording a decision-grade receipt must not mutate the source tree whose qualification the receipt is meant to establish.

Therefore decision-grade evidence storage must be outside the exact qualified tree or otherwise avoid recursive subject mutation.

Possible realizations:

    separate append-only Git ref
    release-attached immutable evidence
    external durable evidence store

No storage mechanism is selected yet.

Public/private evidence remains separated by visibility and authority.

## 19. Migration-oracle release

FACET defines mechanism dispositions and old/new shadow comparison.

WARRANT adds the measurable kill-set criterion.

WARRANT-F adopts both.

For every current mechanism:

    extract actual enforced invariant by reading AND falsification/mutation
    identify historical evidence depending on it
    map to successor claims or retirement reason
    build known-bad corpus
    shadow old and successor
    classify divergences

An old mechanism may lose oracle duty only when:

    successor rejects every known-bad case the old mechanism rejects
        or differences are explicit accepted amendments

    no unexplained successor-weaker divergence remains across a
    preregistered qualification window

    successor blocking claims have active warrants

    explicit owner release decision exists for the mechanism/group

This is stronger than output parity and avoids permanent dual assurance.

Claude's classification of the current 34 workflows is retained as:

    PRELIMINARY HYPOTHESIS ONLY

because Claude explicitly did not fully extract every mechanism.

The formal extraction ledger still covers all current workflows, scripts and tests.

## 20. Security and supply chain

The candidates converge substantially.

WARRANT-F retains:

    least privilege
    no unnecessary secrets for untrusted change execution
    protected environments for secret-bearing/cost-bearing operations
    digest-pinned third-party execution dependencies where supported
    independent Product/Project/Engineering locks
    dependency/security drift revalidation
    public/private leak claims with seeded witnesses
    release/artifact source binding
    provenance verification at consumption

A specific SLSA level is not an architecture claim.

Provenance strength scales with present consequence.

The first externally consumed artifact triggers stronger artifact provenance requirements.

## 21. Shared author identity risk

Claude's strongest operational finding is retained.

Current authors/models/automation ultimately share owner-level Git-host authority, and current infrastructure includes admin-capable integration.

Therefore:

    hosted ephemeral execution improves runtime isolation

but:

    it does not create authenticated two-party governance by itself

and:

    host-settings mutation can bypass repository-content ratchets
    unless separately governed and monitored

WARRANT-F therefore requires later design/owner disposition for:

    role/identity separation where practical
    host protection/ruleset authority
    status publisher authority
    deployment authority
    scheduled live host-policy drift verification

This is:

    ASSURANCE_TRUST_GAP=OPEN

It does not force reopening R8-A/R8-B.

It is an implementation/cutover precondition for stronger trusted-evidence claims.

## 22. Delivery and recovery

The candidates converge on:

    build once
    immutable artifact identity
    qualify built bytes
    promote exact digest
    environment/config validation
    exact mutation target
    uncertain mutation -> reconcile by read
    semantic readiness rather than liveness-only checks
    rollback path qualified
    recovery as exercised evidence, not document-only confidence

Product deployment topology remains open.

Existing Project tooling delivery is legitimate evidence for this architecture even though Product production deployment is not yet fixed.

## 23. Assurance self-validation

The kernel is a trusted computing base and must be smaller than the system it evaluates.

Its critical claims include:

    FAIL never admits
    stale evidence never admits
    missing required evidence never admits
    unwarranted BLOCK evidence never admits
    policy weakening cannot self-authorize
    evidence reuse cannot cross digest mismatch
    every attempt used in decision remains visible
    candidate kernel change is judged using base kernel/policy

High-consequence kernel behavior requires:

    positive tests
    negative controls
    mutation tests
    malformed/stale/missing evidence fixtures

This is the architectural lesson of MC-0027 applied to the successor assurance system itself.

## 24. Cost and proportionality

WARRANT-F retains FACET's tiered cost model and WARRANT's explicit ceremony falsifiers.

The architecture must measure:

    local latency
    promotion latency
    verifier cost
    stochastic campaign cost
    witness maintenance cost
    flake rate
    evidence reuse rate
    stale-evidence rate
    selection false-negative rate
    assurance-policy change effort

No numeric target is frozen yet except that future probe thresholds must be preregistered before measurement.

If warrants/claims become a bureaucracy that materially impedes Product development without increasing defect detection, simplify.

## 25. Material amendments relative to FACET

The synthesis changes FACET by adding:

    A1 first-class warrants
    A2 sensitivity/specificity witnesses for blocking use
    A3 claim consequence floors
    A4 base-revision policy ratchet
    A5 two-level attempt/claim outcome model
    A6 trust tiers T0-T3
    A7 exact-result promotion invariant
    A8 consumer-side result adapters
    A9 absence-execution architecture claims
    A10 kill-set oracle retirement
    A11 non-self-mutating decision evidence storage requirement
    A12 explicit host identity/authority trust gap

These are supported by independent evidence rather than stylistic preference.

## 26. Material amendments relative to WARRANT

The synthesis changes/clarifies WARRANT by:

    B1 retaining FACET profiles as user-facing claim bundles over the
       feedback/gate/maintenance lifecycle

    B2 explicitly adding post-promotion subject-equality confirmation to
       exact-result promotion

    B3 clarifying that hosted ephemeral means isolation from author runtime
       state, not authenticated independent governance under the current host
       identity model

    B4 allowing direct neutral evidence emission as an optimization while
       consumer-side adaptation remains the default dependency-safe rule

    B5 keeping exact evidence-store technology open while requiring
       non-self-mutating decision storage

    B6 carrying FACET's mechanism disposition vocabulary alongside WARRANT's
       kill-set release criterion

    B7 retaining FACET's consequence-proportional evidence retention rather
       than implying every normalized evidence record is durable

    B8 retaining FACET's empirical-probe requirement before owner acceptance

## 27. Prospective R8-A amendment

The only current higher-level structural amendment recommended by WARRANT-F is:

    project/engineering becomes an independently resolved Python project

Reason:

    the selected target now contains substantial executable engineering
    machinery with dependencies that should not enter JW1, Product or root
    resolution

This is a completion of a previously deferred decision, not a contradiction of the Product/Project architecture.

Final acceptance requires explicit owner disposition.

No other R5/R6/R7/R8-A/R8-B reopen is currently indicated.

## 28. Comparative critique required before probe freeze

The independent convergence is high, but the synthesis introduces enough consequential mechanisms that one bounded comparative Claude pass is justified.

Claude may now read:

    Research 274 / FACET
    Research 275 / WARRANT-F V0.1
    its own Message 001 / WARRANT

The comparative critique should focus on whether the synthesis over- or under-corrected the independent candidates.

Required challenge questions:

    C1  Is first-class warrant + mandatory witness the correct blocking bar,
        or is it disproportionate / gameable?

    C2  Does the base-revision ratchet actually prevent self-weakening without
        freezing legitimate architecture evolution?

    C3  Is T2 hosted-ephemeral correctly scoped under shared Git-host identity?

    C4  Does the F0/G1-G7/M1-M2 lifecycle preserve any necessary separate
        integrated-mainline assurance?

    C5  Is consumer-side adaptation the correct dependency seam?

    C6  Is project/engineering independent resolution actually justified,
        or does it create an unnecessary third Python island?

    C7  Is non-self-mutating decision evidence a real invariant, and what
        storage options should remain open?

    C8  Is the kill-set retirement rule sufficient and practical?

    C9  Are the AI/stochastic campaign rules statistically and operationally
        sound for ADS?

    C10 Does the assurance kernel absorb responsibilities that belong in AO,
        JW1, Product or repository host integration?

    C11 Which parts require empirical probes before an owner decision?

Claude should return:

    ACCEPT
    AMEND
    REOPEN

for WARRANT-F V0.1, where REOPEN means an accepted upstream architecture must be revisited.

## 29. Candidate empirical program after comparative reconciliation

No probe thresholds are frozen yet.

Current candidate set:

    P-A1
        catalog / warrant / gate evaluator
        missing, stale, contradictory, unwarranted, waived evidence

    P-A2
        base-revision policy weakening attempts
        plus legitimate strengthening/amendment

    P-A3
        verifier sensitivity/specificity witness mutation
        including an intentionally always-pass verifier

    P-A4
        affected-scope selection
        uncertainty fallback
        hermeticity/undeclared-input detection

    P-A5
        Product + JW1 + Engineering verifiers
        owner-native results adapted through one kernel
        local versus hosted plan parity

    P-A6
        stochastic campaign
        preregistered threshold/stopping rule
        INCONCLUSIVE path
        no retry-to-green

    P-A7
        current repository-integrity oracle versus successor claim/warrant
        known-bad kill-set shadow comparison

    P-A8
        exact-result promotion subject binding
        stale pre-merge evidence rejected

    P-A9
        artifact build/digest/provenance/release decision
        no rebuild during promotion

    P-A10
        decision receipt storage does not mutate the qualified subject

    P-A11
        host/provider adapter contains triggers only while semantic policy
        remains provider-independent

    P-A12
        kernel mutation tests proving FAIL/STALE/UNWARRANTED cannot admit

The comparative review may amend this set before preregistration.

## 30. Current state

    MC0028_INDEPENDENT_CANDIDATES=COMPLETE

    CHATGPT_CANDIDATE=FACET
    CLAUDE_CANDIDATE=WARRANT

    SYNTHESIS=WARRANT_F_V0_1

    PRIMITIVE=CLAIM_VERIFIER_WARRANT_GATE_POLICY_EVIDENCE_DECISION
    WARRANT_REQUIRED_FOR_BLOCKING=true
    POLICY_RATCHET=BASE_REVISION
    TRUST_MODEL=T0_T3
    EXACT_RESULT_PROMOTION=true
    FEDERATED_OWNERSHIP=true
    SINGLE_ADJUDICATION=true
    CONSUMER_SIDE_ADAPTER_DEFAULT=true
    STOCHASTIC_CAMPAIGNS=PREREGISTERED_NON_RETRYABLE
    CURRENT_ORACLE_RETIREMENT=KILL_SET_PLUS_OWNER_RELEASE

    R8A_ENGINEERING_PYTHON_PROJECT=AMENDMENT_CANDIDATE
    SHARED_HOST_IDENTITY_TRUST_GAP=OPEN

    OWNER_ASSURANCE_DECISION=NOT_READY
    EMPIRICAL_PROBES=NOT_FROZEN
    SPECIFICATION028=UNCHANGED
    AO10=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false

    NEXT=CLAUDE_COMPARATIVE_WARRANT_F_CRITIQUE
