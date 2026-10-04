# Research 513: R0 physical-architecture decision-probe preregistration V0.1

**Date:** 2026-10-04
**Status:** R0-P01 / R0-P02 / R0-P03 PROTOCOL FAMILY FROZEN / NO PROBE RESULT OBSERVED / P02 FIXTURE-HARNESS FREEZE NEXT
**Parent:** Research 503-512
**Candidate under test:** GOVERNED_LEDGER_KERNEL_V02
**Logical target:** THIN_CENTRED_HYBRID_V03
**Collaboration thread:** MC-0030
**Scope:** Freeze the questions, arms, metrics, hard controls, decision rules, attempt-integrity rules, dependencies and execution order for the three remaining R0 architecture-decision probes before any probe fixture is executed or result is observed.
**Authority:** Preregistration only. No physical target selection, probe result, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction, or authority switch is authorized.

## 1. Why only three probes remain

Research 512 closes the architecture discussion far enough that most remaining questions are realization/qualification questions rather than architecture-family questions.

The remaining choices that can still materially change the physical target are:

    R0-P01
        can owner-exclusive governing acceptance be both independently verifiable and usable at realistic volume?

    R0-P02
        can deterministic semantic admission/order/tamper evidence be realized over Git without making Git topology itself authority or requiring disproportionate infrastructure?

    R0-P03
        which semantic-navigation additions, if any, materially outperform the V03-native relation substrate plus lexical retrieval?

Everything else remains required downstream qualification unless evidence from one of these probes promotes it back into architecture selection.

## 2. Global preregistration rules

### 2.1 No result before freeze

For each probe:

    protocol family
        this Research 513

    exact fixture/corpus/harness boundary
        must be frozen prospectively in a later Research record

    execution
        only after that exact boundary is committed

No observed probe result may be used to alter its decision thresholds, fixture-selection rule, or hard negative controls.

A protocol defect discovered before result observation may be corrected prospectively with an explicit superseding freeze.

After result observation, tuning-to-green is prohibited.

### 2.2 Result classes

Each probe returns exactly one primary class:

    PASS
        candidate mechanism survives all architecture-changing hard gates

    PASS_WITH_SELECTION
        probe passes and selects one bounded variant/arm inside the candidate family

    AMEND
        architecture family survives but one material interface/mechanism must change before target selection

    REOPEN
        evidence falsifies a load-bearing architecture-family assumption or requires a materially different finalist

    INVALID
        attempt integrity fails; no architecture inference permitted

A probe may also return bounded secondary observations, but they cannot rescue a failed hard gate.

### 2.3 Evidence discipline

Probe harnesses and fixtures are experimental evidence only.

They must not:

    become production authority
    alter Specification 028 authority
    modify current migration state
    switch Project-system authority
    silently create new governing semantics
    mutate hidden/private evidence outside the probe contract

Every generated result binds:

    exact repository head
    exact fixture/harness digests
    exact protocol revision
    exact tool/runtime versions materially affecting the result

### 2.4 No home-field advantage

A compared arm may not receive privileged source information, extra retrieval surfaces, a larger context budget, or post-result manual repair that another arm lacks unless that difference is itself the preregistered feature under test.

Where a baseline already has historical authoring investment, that cost must be reported rather than treated as zero.

### 2.5 Attempt integrity

An attempt is INVALID if:

    fixture/corpus changes after result observation
    hidden expected outputs leak to a blinded evaluator
    an arm is repaired after seeing its scored failure
    result-affecting code changes without a new prospectively frozen attempt
    a required negative control is removed or weakened
    a provider/tool failure is silently retried in a way that changes the semantic attempt
    user/operator intervention supplies answer content forbidden by the protocol

Infrastructure interruption may be resumed only when the frozen protocol defines recovery and exact prior state remains verifiable.

## 3. Execution order

Preferred order:

    1. R0-P02 authority admission / ordering / concurrency
    2. R0-P01 owner authenticity / acceptance burden
    3. R0-P03 semantic navigation / fresh-agent reconstruction

Rationale:

    P02 can falsify the Git-based governing substrate without consuming owner signing effort.
    P01 then tests the human/authentication boundary before the larger navigation experiment.
    P03 is the broadest and most expensive fresh-agent comparison and therefore runs last.

The order may change only before any affected probe result is observed and only through an explicit preregistration amendment.

## 4. R0-P02: authority admission, semantic staleness, ordering and tamper evidence

### 4.1 Architecture question

Can GOVERNED_LEDGER_KERNEL_V02 realize:

    detached owner-authenticated acceptances
    semantic rather than repository-global stale binding
    deterministic in-ledger order
    exact conflict rejection
    interruption recovery
    host-independent authority
    proportionate tamper/rollback evidence

over Git as the durable carrier without relying on Git branch topology as the semantic trust root?

### 4.2 Fixture family

The exact later fixture must include at least:

    GENESIS
        synthetic project identity
        synthetic owner signer set
        genesis chain entry

    BASE ACCEPTANCE
        one accepted effect with explicit identity/currentness

    CONCURRENT CONFLICT A
        governing proposal that changes the same semantic predecessor/state

    CONCURRENT CONFLICT B
        incompatible governing proposal against the same semantic base

    UNRELATED GOVERNING ACCEPTANCE
        semantically independent of the conflict

    UNRELATED NON-GOVERNING LANDING
        knowledge/implementation change outside the semantic base

    INVALID UNSIGNED ENTRY
        structurally plausible but not owner-authenticated

    DUPLICATE ACCEPTANCE
        reuses an already-folded acceptance_id

    HISTORY-MUTATION COPY
        middle-chain mutation / replacement

    TRUNCATED COPY
        valid earlier chain/checkpoint presented as though current

The fixture uses synthetic keys and synthetic governing content. It does not require the project owner's production credential.

### 4.3 Required positive cases

The harness must demonstrate:

    deterministic canonical envelope digest
    deterministic semantic_base_digest
    valid detached signature verification
    contiguous in-ledger sequence and prev-entry chain
    exact full rebuild equals incremental fold
    unrelated non-governing landing does not stale a governing acceptance
    unrelated governing acceptance does not stale another unless the declared semantic dependency changes
    one of two conflicting concurrent acceptances may admit
    the incompatible proposal becomes STALE_SEMANTIC_BASE or exact logical conflict
    host merge/squash/rebase transformation does not alter acceptance validity
    interrupted admission can be recovered without double admission
    connector-only work-branch -> PR -> serialized admission path is representable

### 4.4 Required negative cases

The harness must reject or detect:

    forged signature
    unsigned acceptance
    changed envelope under valid old signature
    decision substitution
    cross-project replay
    acceptance-ID replay
    duplicate ledger sequence
    broken prev-entry digest
    middle-chain rewrite
    logical lineage/currentness conflict
    semantic-base mismatch

A verifier holding a trusted prior checkpoint must detect rollback/truncation below that checkpoint.

### 4.5 Fresh-verifier rollback classification

The probe must separately test/report:

    PRIOR-WITNESS VERIFIER
        possesses a trusted earlier LedgerCheckpoint

    FRESH VERIFIER
        receives only the presented repository snapshot and configured genesis trust

The expected theoretical distinction is preregistered:

    a same-repository chain can prove integrity of the chain presented
    a prior witness can detect rollback below its remembered checkpoint
    a completely fresh verifier cannot prove that a newer valid checkpoint was not suppressed unless an independent freshness/witness mechanism exists

The experiment must not falsely score same-repository hashing as solving that information problem.

### 4.6 Witness variants

If the target threat model requires fresh-verifier anti-rollback beyond "valid as presented", the fixture/harness must compare at least one bounded witness mechanism against same-repository-only baseline.

Eligible mechanisms include:

    owner/device remembered checkpoint
    independently persisted checkpoint witness
    bounded transparency/witness service

The mechanism must not become a second semantic authority. It witnesses chain head/currentness only.

No external transparency product is preselected.

### 4.7 Hard pass gates

R0-P02 is viable only if:

    all required positive cases behave exactly as specified
    all required negative controls are detected
    full rebuild and incremental fold produce the same semantic state/digests
    unrelated repository changes create zero false stale failures
    logical conflict produces zero double-current governing outcomes
    interrupted admission produces zero duplicate accepted entries
    Git merge/rebase/squash changes no detached acceptance proof
    host serialization mechanism can be replaced without changing semantic validity/order rules
    any selected witness mechanism adds no independent semantic ownership

### 4.8 Operational-burden gate

The selected admission/witness design must require:

    zero manual owner editing of sequence/hash metadata
    zero manual duplication of acceptance records between authority stores
    ordinary admission automation after the owner's already-required semantic decision/proof
    explicit owner action only where the accepted checkpoint policy itself requires it

If satisfying the required threat model needs a permanently running authoritative service or a second semantic ledger, classify REOPEN unless a smaller bounded mechanism has been falsified.

### 4.9 Decision rule

    PASS
        all hard gates pass and same-repository chain/checkpoint semantics meet the accepted threat model

    PASS_WITH_SELECTION
        all hard gates pass and one bounded witness/promotion variant is selected

    AMEND
        Git family survives but checkpoint/witness/promotion mechanics need a bounded redesign

    REOPEN
        deterministic trustworthy admission/order cannot be realized over Git proportionately, or requires a second semantic authority / correctness-critical service

    INVALID
        attempt-integrity failure

## 5. R0-P01: owner authenticity and acceptance burden

### 5.1 Architecture question

Can consequential governing acceptance use an owner-exclusive cryptographic proof that:

    binds exactly what the owner saw and decided
    survives repository/host transformations
    is independently verifiable without chat history
    works on the owner's realistic devices/workflow
    remains practical at estimated migration and steady-state volume?

### 5.2 Frozen semantic statement

Every credential arm signs the same logical SignedAcceptanceStatement fields from Research 512:

    context
    project_id
    acceptance_id
    envelope_digest
    shown_digest
    decision
    semantic_base_digest
    signer_set_version
    issued_at

Credential arms may differ only in how they prove owner-exclusive control over that exact statement.

### 5.3 Required credential arms

Fixture freeze must attempt to realize at least:

    A DESKTOP CRYPTOGRAPHIC
        SSH-signature, OS/hardware-backed key, minisign-compatible key, or equivalent
        must require owner-exclusive credential use

    B PASSKEY / WEBAUTHN / MOBILE-CAPABLE
        only qualifies if the assertion can verifiably bind the exact statement digest
        if the available platform cannot expose such binding, record NOT_REALIZABLE rather than pretending ordinary login approval is equivalent

    C PLATFORM-SEPARATED OWNER IDENTITY
        weaker comparator
        a dedicated account/review identity distinct from agent execution identity
        explicitly not assumed cryptographically equivalent to A/B

The exact implementation choices are frozen before owner trials.

### 5.4 Sign-what-you-see requirement

The qualified signing surface itself must:

    load the exact envelope
    validate the semantic base
    render the owner-visible view
    display that view
    digest the exact displayed bytes
    construct the canonical SignedAcceptanceStatement
    invoke the credential proof

Chat/model prose may explain the acceptance but is not the cryptographically bound display.

### 5.5 Required security controls

Each realizable cryptographic arm must demonstrate:

    valid acceptance verifies
    forged/agent-prepared proof rejects
    changed envelope rejects
    changed shown view rejects
    ACCEPT -> REJECT/AMEND substitution rejects
    cross-project replay rejects
    acceptance-ID replay rejects
    semantic-base mismatch rejects
    unrelated repository landing does not invalidate
    signer-set mismatch rejects
    trust-root rotation dry-run
    recovery credential dry-run
    compromise-boundary handling dry-run

Zero security-control misses are permitted.

### 5.6 Owner trials

For each realizable owner-exclusive arm:

    3 small low-consequence signing trials
    1 larger approximately 30-effect envelope trial

Measure separately:

    semantic review time
    mechanical signing/authentication time after the owner has decided
    interaction count
    device switches
    manual file/terminal editing required
    failure/recovery events
    subjective friction note from owner

The owner is not asked to reveal private keys, recovery secrets, or credential material.

### 5.7 Mechanical burden thresholds

At least one owner-exclusive cryptographic arm is operationally viable only if:

    zero manual TOML/JSON/Git metadata editing by owner
    3/3 small trials complete successfully
    median mechanical signing/authentication overhead after decision <= 60 seconds
    no single small-trial mechanical overhead > 120 seconds absent an infrastructure interruption
    large-envelope mechanical signing overhead after semantic decision <= 120 seconds
    no credential secret is exposed to ChatGPT, Claude, Codex, Runtime Bridge logs, repository, or probe result

Semantic reading/review time is measured and reported but does not use the same 60/120-second gate because it scales with actual governing content and should not be optimized away.

### 5.8 Legacy-volume desk estimate

Before classifying R0-P01, freeze a mechanical inventory rule estimating:

    projected number of migration/reconciliation governing acceptances
    projected distribution of effects per acceptance
    expected repeated-signing count under the chosen semantic boundaries

Compute:

    projected_owner_mechanical_minutes
        = projected_acceptance_count * measured median small-acceptance mechanical minutes

If either:

    projected acceptance count > 100
    projected owner mechanical signing burden > 90 minutes

then a governed batch/class-acceptance variant must be designed and bounded before physical-target selection.

That variant must preserve independent acceptability and cannot silently batch unrelated semantics merely to reduce clicks.

### 5.9 Decision rule

    PASS_WITH_SELECTION
        at least one owner-exclusive cryptographic arm passes every security control and burden gate, and projected volume stays within the gate

    AMEND
        cryptographic acceptance is viable but needs a bounded batch/class mechanism, different signing UX, or trust-root workflow

    REOPEN
        no owner-exclusive exact-statement proof is usable on realistic devices/workflow, or only shared agent/platform identity remains feasible

    INVALID
        credential/control leakage, result-affecting post-observation tuning, or attempt-integrity failure

The weaker platform-separated identity arm cannot by itself produce PASS_WITH_SELECTION for the owner-cryptographic architecture. It is a fallback comparator if A/B fail.

## 6. R0-P03: semantic navigation and fresh-agent reconstruction

### 6.1 Architecture question

Given the V03-native deterministic relation substrate, which additional semantic-organization/navigation architecture provides the best whole-system discovery and reconstruction benefit without duplicating authority or imposing unjustified authoring/maintenance burden?

### 6.2 Common substrate for every arm

Every arm receives exactly the same:

    information-role / natural-owner positions
    accepted-effect identities and subjects
    lineage/currentness
    completion relations
    J2 coverage
    evidence/receipt relations
    authority-class labels
    lexical full-text retrieval
    mandatory connector-readable derived orientation surface

These are not scored as an advantage for any arm.

### 6.3 Compared additions

    B0 SUBSTRATE_LEXICAL
        common substrate only

    B1 RESEARCH217_FACETS
        B0 + Research-217-derived controlled subject/facet catalog,
        source-owned membership, polyhierarchy and default/preferred navigation route where applicable

    B2 CARRIER_LINKS
        B0 + source-owned carrier-to-governing links

    B3 SELECTIVE_CONCERNS
        B0 + bounded governed cross-cutting concern/facet vocabulary

    B4 SEMANTIC_RETRIEVAL
        best justified structured arm from B1-B3 + embedding/semantic retrieval
        only if implementation effort can be equalized and authority labelling remains explicit

B4 may be omitted prospectively at exact fixture freeze if equalized implementation cannot be achieved without materially larger engineering investment. That omission must occur before any arm score is observed.

### 6.4 Research 217 historical evidence

Research 217 remains a serious comparator.

Historical evidence includes:

    18 assignable semantic subjects
    6 non-assignable navigation parents
    source-owned memberships
    polyhierarchy
    optional preferred_subject
    65-carrier V0.2 corpus
    94 memberships
    1.446 mean memberships/artifact
    23/65 multi-subject artifacts
    9/9 candidate navigation scenarios PASS
    4/9 legacy comparator scenarios PASS
    blind 24-carrier calibration:
        exact full sets 66.7%
        mean Jaccard 0.852
        micro membership F1 0.867
        preferred-route agreement 91.7%

Those results are evidence, not automatic credit on new whole-system tasks.

### 6.5 Primary task packet

Before constructing/scoring B1-B4 for this probe, freeze 12 primary tasks:

    3 cold-start/current-orientation tasks
    3 cross-plane discovery tasks
    3 impact-analysis / architecture-evolution tasks
    3 exact-source / authority / recovery tasks

Task selection must use either:

    a fresh scenario author who has not designed the compared arms

or:

    a mechanical historical owner-query/event selection rule frozen before arm construction

The second method is preferred if independence of a fresh author cannot be demonstrated cleanly.

### 6.6 Legacy regression packet

The 9 Research 217 navigation scenarios are retained as a separate legacy regression packet.

They cannot substitute for the 12 new primary tasks.

Any scenario that is genuinely inapplicable to a new architecture must have N/A criteria frozen before scoring.

### 6.7 Corpus and maintenance split

Freeze a representative carrier corpus before arm scoring.

Preferred target:

    60 build carriers
    20 held-out/maintenance carriers

If fewer than 80 current relevant carriers qualify under the frozen sampling rule, use all qualifying carriers with a deterministic 3:1 build/held-out split.

Path SHA-256 ordering or another deterministic rule must freeze the split.

Historical metadata investment for B1 is reported as prior authoring cost; it is not treated as free.

### 6.8 Evaluators

At least two fresh evaluators should score task success where model judgment is required.

Requirements:

    no evaluator authors an arm it scores
    no evaluator sees other-arm outputs before producing its own task result
    all arms receive equal task wording and context/tool budget
    source citations/provenance are required for successful answers
    false authority claims are scored as hard failures

Where a task can be mechanically scored, use the mechanical score rather than model preference.

### 6.9 Metrics

Per arm:

    primary tasks PASS / 12
    legacy scenarios PASS / 9
    exact-authority correctness
    relevant-source recall
    missed relevant source count
    irrelevant-source/context burden
    context characters/tokens read
    tool/read count
    provenance correctness
    false-authority errors
    default-route usefulness where applicable
    human browseability result
    authoring effort
    generated-versus-authored metadata fraction
    held-out maintenance agreement
    pre-existing metadata changed solely because corpus grew
    degradation after deletion of generated indexes
    rebuild success of derived navigation

### 6.10 Hard viability gates

An arm is viable only if:

    >= 10/12 primary tasks PASS
    >= 8/9 legacy scenarios PASS or prospectively frozen N/A
    zero false-authority/safety failures
    exact source/revision preserved on every authority-sensitive answer
    no physical path is treated as semantic identity/authority
    no generated index/ranking becomes governing truth
    no unique central membership registry becomes semantic authority
    held-out maintenance agreement >= 0.80 F1 where authored assignment exists
    adding held-out carriers changes <= 10% of pre-existing authored carrier metadata solely because the corpus grew
    deletion of generated indexes causes degraded discovery at worst, never false governing state

### 6.11 Complexity preference rule

Among viable arms, prefer the structurally simpler arm unless a more complex arm achieves at least one preregistered material advantage:

    >= 2 additional primary task PASS results
    >= 0.10 held-out maintenance-agreement improvement
    removes a material authority/navigation failure
    >= 20% reduction in median context/tool burden with no correctness loss

and recurring authored-maintenance burden is <= 25% higher than the simpler arm.

If several arms remain non-dominated, return PASS_WITH_SELECTION only when the rule selects one. Otherwise return PASS with MULTIPLE_VIABLE_ARMS and carry the smallest bounded choice to the owner/target decision.

Research 217/B1 may win.

### 6.12 Decision rule

    PASS_WITH_SELECTION
        one arm is viable and selected by the preregistered dominance/complexity rule

    PASS
        multiple viable arms remain non-dominated; architecture family survives and owner receives the bounded unresolved choice

    AMEND
        all arms require one bounded navigation-interface change but V03-native substrate remains viable

    REOPEN
        no arm meets whole-system navigation/reconstruction requirements without changing authority/semantic substrate assumptions

    INVALID
        contamination, unequal arm treatment, post-result task/threshold changes, or attempt-integrity failure

## 7. Cross-probe architecture decision

After all three valid results:

    any REOPEN
        -> physical-target decision is blocked
        -> reopen only the falsified architecture boundary

    any AMEND
        -> freeze the amendment
        -> determine prospectively whether the affected probe must be rerun
        -> no owner target decision until the amendment has adequate evidence

    P02 PASS/PASS_WITH_SELECTION
    + P01 PASS_WITH_SELECTION
    + P03 PASS/PASS_WITH_SELECTION
        -> architecture evidence is sufficient to prepare an explicit owner physical-target decision package

No numeric score is averaged across probes.

Security/authority failure cannot be offset by navigation quality.

## 8. Downstream qualification preserved

Even after successful target selection, the following remain required during R1/R2 and migration qualification:

    exact source serialization
    canonicalization conformance vectors
    J2 authoring/scaffolding burden
    executor-provider portability
    receipt redaction
    full/incremental rebuild equivalence at scale
    private degraded rebuild
    connector publication freshness
    migration-slice semantic parity
    rollback drills
    CI/provider/runner choice
    deployment/observability
    Runtime Bridge extraction qualification if later authorized

Passing R0-P01..P03 does not waive them.

## 9. Next exact step

R0-P02 executes first.

Before any R0-P02 result is observed, freeze:

    exact fixture records
    exact synthetic key material handling
    exact canonical schemas used by the probe
    exact positive/negative case list
    exact harness implementation boundary
    exact witness variants actually compared
    exact output schema
    exact deterministic decision evaluator

Implementation of the probe harness may begin only after that fixture/harness boundary is frozen.

## 10. Current boundary

    MC0030=OPEN
    PHASE=R0_P02_FIXTURE_HARNESS_FREEZE
    NEXT_ACTOR=chatgpt

    RECONCILED_CANDIDATE=GOVERNED_LEDGER_KERNEL_V02
    PROBE_PROTOCOL=RESEARCH_513_V01

    R0_P01_PROTOCOL=FROZEN_FAMILY
    R0_P02_PROTOCOL=FROZEN_FAMILY
    R0_P03_PROTOCOL=FROZEN_FAMILY

    R0_P01=NOT_RUN
    R0_P02=NOT_RUN
    R0_P03=NOT_RUN

    PHYSICAL_ARCHITECTURE_SELECTED=false
    OWNER_DECISION=NOT_READY
    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    RUNTIME_BRIDGE_EXTRACTION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED
    AUTHORITY_SWITCH_AUTHORIZED=false

    NEXT=R0_P02_EXACT_FIXTURE_HARNESS_FREEZE
