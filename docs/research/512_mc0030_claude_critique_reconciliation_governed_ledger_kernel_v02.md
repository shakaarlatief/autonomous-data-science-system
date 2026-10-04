# Research 512: MC-0030 Claude critique reconciliation and Governed Ledger Kernel V0.2

**Date:** 2026-10-04
**Status:** CLAUDE MESSAGE 003 RECONCILED / GOVERNED LEDGER KERNEL V0.2 FROZEN / THREE-PROBE PROGRAM RETAINED / PROBE PROTOCOL PREREGISTRATION NEXT / OWNER DECISION NOT READY
**Parent:** Research 503-511
**Selected logical target:** THIN_CENTRED_HYBRID_V03
**Compared evidence:** Research 504 + 508, MC-0030 Messages 001-003, Research 511
**Reconciled candidate:** GOVERNED_LEDGER_KERNEL_V02
**Collaboration thread:** MC-0030
**Scope:** Reconcile Claude Message 003 into the first comparative candidate, repair the acceptance/order/J2/publication/executor/private-state interfaces before probe design, and freeze the smallest decision-relevant R0 probe set without executing any probe.
**Authority:** Comparative architecture candidate only. No physical target, implementation, migration, Specification 028 amendment, Runtime Bridge extraction, production activation, or authority switch is authorized.

## 1. Overall disposition

Claude Message 003 is accepted as a material critique with refinements.

It does not reopen THIN_CENTRED_HYBRID_V03 and does not justify a second physical finalist.

The revised candidate remains one architecture family:

    GOVERNED_LEDGER_KERNEL_V02

Disposition:

    MESSAGE003=ACCEPT_WITH_REFINEMENTS
    RESEARCH511=AMEND
    GOVERNED_LEDGER_KERNEL_V01=SUPERSEDED_BY_V02
    COMPETING_PHYSICAL_FINALISTS=NOT_REQUIRED
    V03_REOPEN=NO
    OWNER_DECISION=NOT_READY

The three preselection probes remain sufficient:

    R0-P01 owner authenticity and acceptance burden
    R0-P02 authority admission / ordering / concurrency / tamper evidence
    R0-P03 semantic navigation / fresh-agent reconstruction

No probe is executed by this record.

## 2. What remains unchanged

The following Research 511 decisions survive Claude's critique:

    repository-native immutable governing acceptance family
    detached owner-exclusive proof over consequential Acceptance Envelopes
    natural-owner J2 rather than a duplicated central realization authority
    one deterministic Project-system kernel
    one executable predicate implementation for shared semantics
    deterministic J3
    non-authoritative orientation and retrieval
    disposable SQLite/FTS/local indexes
    one reconciled architecture family
    provider-neutral ADS executor port
    Codexless Runtime Bridge as reusable external infrastructure
    no Runtime Bridge extraction merely to satisfy R0
    Product / Project separation
    semantic shadow before physical migration
    one operational authority until explicit cutover
    Specification 028 remains current operational authority

## 3. Acceptance proof: detached envelope proof retained and strengthened

Claude's F-01 is accepted.

A consequential governing act is not authoritative because a Git commit, PR approval, chat message, connector identity, or shared GitHub identity says so.

It requires an independently verifiable owner-exclusive proof over one canonical acceptance statement.

The proof is transport-independent. Git carries the record; Git does not create the owner's semantic authority.

## 4. Semantic base replaces whole-repository stale binding

Claude F-02 is accepted.

Research 511's whole-repository expected-base wording is retired for governing acceptance validity.

A signed acceptance instead binds:

    semantic_base_digest

The semantic base is the canonical digest of exactly the governing state the proposed acceptance depends on, including as applicable:

    current identity/status/lineage heads of referenced predecessor or subject effects
    pinned accepted domain-contract revisions
    signer-set version
    governing grammar version
    accepted predicate-semantics version
    any explicit governing dependency named by the envelope

Admission recomputes that semantic base against the candidate governing state.

    equal
        -> semantic precondition remains valid

    different
        -> STALE_SEMANTIC_BASE
        -> re-render and re-decide before admission

Unrelated repository changes do not invalidate an owner decision.

Unrelated governing acceptances also do not invalidate it unless they alter a dependency included in the semantic base.

This keeps stale-write protection semantic rather than path/commit-global.

## 5. Canonical signed statement and anti-replay binding

Claude F-03 is accepted with one refinement: timestamps are provenance, not ordering authority.

The logical statement is:

    SignedAcceptanceStatement
        context
        project_id
        acceptance_id
        envelope_digest
        shown_digest
        decision
        semantic_base_digest
        signer_set_version
        issued_at

Required semantics:

    context
        domain separation, for example ADS-GOVERNING-ACCEPTANCE/v1

    project_id
        stable governed project identity
        blocks cross-project replay

    acceptance_id
        stable unique acceptance identity
        folds at most once

    envelope_digest
        canonical semantic digest of the exact Acceptance Envelope

    shown_digest
        digest of the exact rendered bytes displayed by the signing client

    decision
        ACCEPT | AMEND | REJECT
        signed as data, never inferred from transport

    semantic_base_digest
        Section 4

    signer_set_version
        exact trust-root state under which the proof was made

    issued_at
        provenance only
        never ledger order and never a conflict-resolution tiebreaker

The statement uses a standard signature mechanism. ADS does not invent cryptography.

Candidate mechanisms include SSH signature formats, hardware-backed keys, minisign-compatible keys, and WebAuthn/passkey assertions where the assertion can bind the exact statement digest.

Exact credential adapter remains R0-P01 evidence.

## 6. Sign what the owner actually sees

Claude F-04 is accepted.

The authoritative owner-visible rendering is produced by the signing client from the exact envelope using the qualified renderer version.

The signing client:

    loads the exact envelope
    validates the semantic base
    renders the owner-visible view
    displays that exact view
    digests the bytes it displayed
    signs the statement containing shown_digest

A rendering produced by chat, a model, CI, or another tool may assist review but is not the cryptographically bound shown view unless the signing client independently reproduces and displays those exact bytes.

The normal owner workflow does not require hand-editing TOML, JSON, or Git metadata.

## 7. Trust root, rotation, recovery and compromise

Claude F-05 is accepted with a compromise-authority refinement.

Genesis:

    first signer set is established by a GENESIS record
    owner confirms the initial public-key fingerprint through an explicit out-of-band step
    the trust-on-first-use nature of genesis is recorded, not hidden

Rotation:

    ordinary signer-set rotation is authorized by the currently valid signer authority

Recovery:

    at least one offline recovery credential may be pre-registered
    use of the recovery credential creates an explicit governed recovery/rotation event

Revocation:

    ordinary revocation is prospective
    it does not silently invalidate acceptances that were validly admitted before the effective revocation boundary

Compromise:

    a compromise declaration must itself be authorized by a still-trusted current or recovery credential
    it names an explicit compromise boundary
    affected post-boundary acceptances become REVIEW_REQUIRED until re-ratified, retired, or otherwise governed
    when the compromise start cannot be established precisely, policy may conservatively widen the review interval

The exact genesis/recovery UX is part of R0-P01.

## 8. Authority order is in-ledger, not Git-topology authority

Claude F-07 is accepted and supersedes Research 511's branch-admission-order rule.

Git remains the leading durable carrier and collaboration substrate, but Git topology is not the semantic trust anchor.

Every admitted governing entry participates in an in-ledger chain:

    LedgerEntry
        sequence_no
        acceptance_id
        envelope_digest
        prev_entry_digest
        entry_digest

The kernel verifies:

    contiguous sequence
    previous-digest continuity
    referenced acceptance authenticity
    acceptance semantic-base validity at admission
    no duplicate acceptance_id
    no invalid lineage/currentness transition

Host mechanisms such as merge queue or a Runtime-Bridge promotion controller serialize candidate admission. They do not create semantic authority.

### 8.1 Owner checkpoints

Periodic or consequence-triggered owner-signed LedgerCheckpoint statements bind:

    project_id
    sequence_no
    chain_head_digest
    signer_set_version
    checkpoint class
    issued_at

At minimum, checkpoints are required at:

    genesis
    authority switch / rollback boundary
    trust-root rotation
    other high-consequence boundaries defined by accepted policy

R0-P02 determines whether ordinary ledger operation also requires a frequency/size checkpoint policy.

### 8.2 Anti-rollback limitation made explicit

A hash chain proves continuity and detects mutation of a presented chain.

A verifier that already holds a trusted prior checkpoint can also reject rollback below that checkpoint.

A completely fresh verifier presented only with one repository snapshot cannot, from a same-repository hash chain alone, prove that a newer valid checkpoint was not suppressed.

This is an explicit threat-model fact, not hidden by the architecture.

R0-P02 must therefore test the required anti-rollback witness level and decide whether the target needs:

    remembered local trusted checkpoint
    independently persisted witness/checkpoint channel
    another bounded transparency mechanism

or whether authenticated integrity plus fail-visible prior-checkpoint comparison satisfies the actual Project threat model.

An external transparency service is not selected by default.

## 9. J2 fact kinds and one natural carrier

Claude F-08 is accepted with a projection clarification.

J2 fact kinds:

    OBSERVABLE
        existence
        exact revision
        digest
        deterministic CI outcome
        deployment/activation state where the natural owner exposes it exactly
        -> derived from natural-owner records

    RELATIONAL
        realizer/artifact COVERS accepted effect/component
        FULL / PARTIAL
        realization successor/carry relation where not already J1
        -> explicitly declared by the natural owner
        -> never inferred from similarity, naming, model judgment, or heuristic code reading

    EPHEMERAL
        manual procedure result
        external action
        one-time execution fact
        fact that cannot be reproduced later from its natural owner
        -> durable event receipt

For each authoritative/natural-owner J2 fact tuple, exactly one carrier class owns the fact.

Derived projections may repeat that fact for navigation, J3, orientation, search, or reporting, but those projections are not additional carriers of authority.

A validator rejects contradictory duplicate natural-owner declarations.

Missing required coverage is visible as OPEN / UNOWNED / COVERAGE according to V03 orientation semantics.

Colocated REALIZES-style manifests are the leading carrier for repository-local RELATIONAL coverage. They are not required for OBSERVABLE facts that can be derived exactly and are not the only valid carrier for non-repository realizers.

## 10. Semantic organization: substrate selected, navigation architecture open

Claude F-09 is accepted.

The selected substrate is only what V03 already requires plus non-authoritative lexical retrieval:

    accepted-effect identities and subjects
    lineage
    completion relations
    J2 coverage
    evidence/receipt relations
    lifecycle/currentness
    authority-class labels
    lexical full-text retrieval

This substrate is available equally to every R0-P03 arm.

The following are navigation-architecture choices and remain unselected:

    Research 217-derived subject/facet catalog
    carrier-to-governing link metadata
    selective governed concerns/facets
    embedding/semantic retrieval

R0-P03 arms:

    B0 substrate + lexical
    B1 B0 + Research 217-derived subject/facet catalog
    B2 B0 + carrier links
    B3 B0 + selective governed concerns/facets
    B4 best justified structured arm + embeddings/semantic retrieval under equalized effort

B1 may win.

Research 217 is comparator evidence, not a legacy strawman.

## 11. Connector-readable derived orientation is a service-level requirement

Claude F-10 is accepted.

Correctness remains independent of generated publication.

Operability does not.

Every admitted ledger advance must produce, within a bounded service-level latency, a repository/connector-readable derived orientation that includes at least:

    accepted chain head / checkpoint reference
    current governing authority summary
    open REQUIREs and next gaps
    REVIEW_REQUIRED items grouped by resolving owner
    recent governing acceptances
    navigation entry points
    source/input digests
    explicit DERIVED / non-authoritative label

Readers can compare the published source head/checkpoint to the source ledger.

Staleness is visible.

R1 chooses the publication channel.

A dedicated derived Git ref is the leading option because common repository connectors can read it, but it is not selected merely by convention. An equivalent repository-readable channel may win.

CI artifacts alone do not satisfy this service level.

Deletion of the publication never destroys governing truth.

## 12. Project-system and Project-engineering direction rules

Claude F-11 is accepted.

Code dependency:

    project/engineering -> project/system
    project/system never imports project/engineering

Data may flow both ways through typed contracts:

    project/system
        emits compiled ActionContracts / control requirements

    project/engineering
        emits J2 evidence, qualification, execution and assurance receipts

Mutual data exchange is not circular semantic ownership.

AO placement:

    activation
    semantic event interpretation
    route/owner selection
    preflight/postflight decision logic
    admission semantics
    continuation logic

belong in project/system.

Provider mechanics, verifier execution, CI/provider integration, executor adapters and migration execution belong in project/engineering.

Predicate semantics have one implementation in project/system. Engineering consumes a typed batch/library/CLI result interface and may not reimplement registered predicate logic.

## 13. Predicate implementation conformance

Claude F-12 is accepted.

An implementation-only predicate change is conformant only if it preserves accepted semantics.

A change that alters any J3 output on:

    the frozen golden corpus
    the current accepted ledger snapshot
    applicable property/metamorphic conformance tests

is treated as a semantic change unless a governed review explicitly classifies the old behavior as a CONFORMANCE_DEFECT.

The defect classification preserves the old result as historical defective evidence rather than silently rewriting history.

## 14. Executor contract ownership and recovery

Claude F-13 is accepted with one important ownership refinement.

### 14.1 No premature third neutral standard

V0.2 does not create a new independently owned cross-product receipt standard merely to reconcile ADS and Runtime Bridge.

Instead:

    Runtime Bridge
        owns its generic native capability/request/receipt contract

    other providers
        own their native contracts

    ADS Project System
        owns ActionRequest / ExecutionReceipt / EvidenceReceipt / CapabilitySnapshot /
        FailureReceipt as its provider-neutral internal port

    ADS adapters
        translate provider-native contracts into ADS port records

If later multiple independent projects need one shared generic execution standard, extraction can be evaluated then.

The generic Runtime Bridge never imports ADS types.

### 14.2 Idempotency and recoverability are capabilities, not assumptions

Every ADS ActionRequest carries a logical operation/idempotency key.

Each adapter advertises exact guarantees such as:

    AT_MOST_ONCE
    IDEMPOTENT_BY_PLATFORM_PRECONDITION
    RECOVERABLE_OBSERVATION
    BEST_EFFORT
    NON_IDEMPOTENT

A governed action requiring at-most-once execution may route only to an executor qualified for that guarantee.

recover(operation_key) must return only what evidence supports, for example:

    DONE with outputs
    NOT_STARTED
    PARTIAL with known outputs / compensation state
    UNKNOWN

It may never claim DONE merely because a retry would be convenient.

### 14.3 Independent observation

INDEPENDENTLY_OBSERVED means reconstructed from platform-recorded facts that the executor's own self-report did not author, for example:

    commit objects
    branch/ref state
    check runs
    workflow records
    artifact digests

The receipt records residual shared-identity limitations where applicable.

SELF_REPORTED alone remains insufficient for consequential authorization consumption.

### 14.4 Receipt privacy

Public receipts must pass deterministic secret/credential redaction policy before publication.

Sensitive receipt payloads remain private and expose only permitted projections/commitments publicly.

## 15. Private J1 without a second development authority

Claude F-15 is accepted.

A private governing acceptance may keep sensitive semantic bytes in the private companion only if:

    the private payload is content-addressed
    the public ledger alone owns admission and ordering
    the private store cannot create or reorder governing acts
    the public record binds the private payload digest
    owner authenticity remains verifiable from the public acceptance proof

If a private acceptance changes any public effect, the public ledger must expose a minimum public consequence skeleton sufficient to keep public currentness correct:

    affected public effect IDs
    structural relation kind
    resulting public status/currentness
    effective boundary

It does not expose the private successor meaning.

If even that structural disclosure is unacceptable, the affected governing scope cannot simultaneously be treated as public current authority; it must move behind the private boundary or explicitly orient as PRIVATE_UNAVAILABLE / REVIEW_REQUIRED.

Purely private effects with no public consequence remain private.

The private companion remains a knowledge/evidence complement, never a second ADS development repository.

## 16. Explicit owner and developer workflow

Claude F-18 is accepted.

Normal owner workflow:

    open qualified signing/review surface
    inspect rendered acceptance
    choose ACCEPT / AMEND / REJECT
    authenticate/sign
    no hand-edit of TOML, JSON, Git refs, sequence numbers, or signature metadata

Normal developer/model workflow:

    use Project-system scaffolding/API/CLI to draft typed records
    edit ordinary source/artifact content in its natural home
    declare RELATIONAL J2 coverage through the appropriate natural-owner carrier
    validate before review
    never manufacture owner proof
    never hand-maintain J3/orientation state

R1 must include short authoring/recovery guides and machine-enforced scaffolding where useful.

## 17. Substrate choices are explicit, not preservation rights

Claude F-19 is accepted with refinements.

### Git

Git is the current leading durable authority carrier because it provides:

    inspectable immutable objects
    distributed/offline copies
    reviewable diffs
    content addressing
    mature transport
    current project compatibility

Git is not the owner-authenticity root and not the semantic ledger-order root.

Falsifier:

    R0-P02 shows that portable deterministic admission, required anti-rollback evidence, or recovery cannot be achieved over Git without disproportionate burden

### Python

Python is a provisional R1 implementation default, not an R0 semantic invariant.

Reasons:

    existing qualified fixtures/evaluators
    current repository expertise
    good deterministic tooling
    low operational burden

Falsifier:

    another implementation language materially improves correctness, portability, packaging, performance, or verification enough to justify migration cost

No architecture requirement says the successor must remain Python.

### Repository tree

The Product / Project, project/system / project/engineering, governing-ledger / control / knowledge responsibility boundaries are selected conceptually.

The exact R8-A physical tree has no preservation right.

R8-A is evidence and a strong layout starting point. R1 may refine, move, split, merge, rename, or replace physical folders when doing so better realizes the selected boundaries.

## 18. R0-P01 corrected scope

R0-P01 must compare at least:

    desktop cryptographic signing path
        SSH/hardware-backed or equivalent

    passkey/WebAuthn/mobile-capable path
        only if it can bind the exact SignedAcceptanceStatement

    platform-separated owner identity
        weaker comparator class, not presumed equivalent

Controls:

    valid low-consequence acceptance
    forged/agent-prepared acceptance rejected
    cross-project replay rejected
    acceptance-ID replay rejected
    decision substitution rejected
    semantic-base staleness rejected
    unrelated repository landing does not invalidate
    sign-what-you-see verification
    trust-root rotation dry-run
    recovery/compromise dry-run
    one larger envelope of approximately 30 effects

Desk input before result classification:

    estimate expected number and size distribution of governing acceptances needed for legacy reconciliation/migration

This determines whether per-acceptance UX is sufficient or a governed batch/class acceptance mechanism must be designed.

No batch/class mechanism is selected in advance.

## 19. R0-P02 corrected scope

R0-P02 must test:

    two concurrent governing proposals
    one real semantic conflict
    one unrelated governing proposal
    unrelated non-governing repository landing
    semantic-base equality and stale failure
    in-ledger sequence/hash continuity
    duplicate acceptance rejection
    injected unsigned/invalid record
    simulated history rewrite
    rollback/truncation against a prior trusted checkpoint
    fresh-verifier limitation with no prior witness
    actual host merge/squash/rebase transformation
    connector-only work-branch -> PR -> admission path
    interrupted admission and recoverability

R0-P02 must classify whether the target threat model needs an independent anti-rollback witness beyond same-repository checkpoints.

That question remains inside R0-P02. It is not a fourth probe.

## 20. R0-P03 corrected scope

Every navigation arm receives the same selected V03-native relation substrate and lexical retrieval.

The compared additions are Section 10 B0-B4.

The test runs through the mandatory connector-readable orientation publication, not through privileged local kernel execution alone.

Scenarios, scoring, fresh-agent rules, authoring-effort accounting and maintenance/drift additions are frozen before any arm result is observed.

Measures include:

    task correctness
    relevant-source recall
    irrelevant-context burden
    provenance correctness
    false-authority errors
    context/tool cost
    human browseability
    fresh-agent continuation
    what-governs-this
    impact analysis
    AO candidate-context retrieval
    migration reasoning
    cross-cutting architecture evolution
    authoring burden
    maintenance burden
    behavior after deleting generated indexes

Research 217 remains eligible to win.

## 21. Why no fourth preselection probe is added

Claude F-16 and F-17 are retained.

The following questions are important but have bounded adaptation points inside V0.2 and therefore do not currently determine the architecture family:

    executor portability
    rebuild/index scale
    private degraded rebuild
    migration-slice parity
    exact CI provider/runner
    exact derived publication channel
    exact leaf repository topology
    exact source serialization
    exact kernel implementation language

They remain downstream R1/R2 qualification obligations.

If one of R0-P01..P03 exposes evidence that one of those questions actually changes the family, the architecture decision is held and the relevant question is promoted before owner selection.

## 22. R0 completeness after reconciliation

Claude's audit is accepted.

R0-R01 through R0-R62 now have explicit candidate answers.

Important closure points:

    R0-R01/R02
        Sections 3-7

    R0-R13
        Sections 12-13

    R0-R26
        Section 15

    R0-R27
        Sections 4 and 8

    R0-R28
        Section 14

    R0-R39
        Section 16

    R0-R44
        Sections 8 and 17

    R0-R49
        Section 11

    R0-R52
        Section 10

    R0-R60
        Section 14

No R0 requirement is knowingly left without an architecture-level answer.

Some answers remain probe-dependent by design.

## 23. Leading physical/software candidate V0.2

At this boundary the candidate is:

    GOVERNING PLANE
        immutable Acceptance Envelopes
        canonical semantic digests
        owner-exclusive detached proofs
        semantic-base binding
        in-ledger admission chain
        owner checkpoints
        explicit lineage/completion/accounting

    REALIZATION PLANE
        natural-owner J2
        OBSERVABLE / RELATIONAL / EPHEMERAL fact classes
        one natural carrier per fact
        exact source revision/provenance

    DETERMINISTIC KERNEL
        acceptance verification/fold
        chain verification
        lineage/currentness
        completion
        versioned predicates
        J3
        control compilation
        orientation
        navigation substrate
        validation/recovery

    ENGINEERING PLANE
        WARRANT-F
        verifier execution
        executor adapters
        provider/CI mechanics
        migration/shadow/cutover tooling
        qualification

    DERIVED OPERABILITY PLANE
        local SQLite/FTS/search
        generated orientation
        mandatory connector-readable bounded publication
        optional richer disposable projections
        never authority

    EXECUTION PLANE
        ADS-owned executor port
        provider-native adapters
        Runtime Bridge external generic infrastructure
        explicit capability/idempotency/recovery semantics

    PRIVATE COMPLEMENT
        content-addressed private payloads
        public consequence skeleton where public authority changes
        no admission/order authority

    PRODUCT
        independently resolved
        no Project-system runtime dependency

## 24. Material falsifiers retained

V0.2 must be amended or reopened if evidence shows:

    no usable independently verifiable owner-exclusive acceptance path exists
    acceptance volume makes per-acceptance proof structurally impractical without a new governed batching model
    semantic-base computation cannot remain exact and bounded
    Git plus the selected admission/witness design cannot provide required tamper/rollback properties proportionately
    J2 RELATIONAL declarations create unsustainable authoring burden or cannot stay complete
    connector-readable derived orientation cannot remain fresh/rebuildable without becoming de facto authority
    relation-first substrate plus candidate navigation additions cannot match the best Research 217 behavior fairly
    executor adapters require provider-specific semantic branching in AO
    Project-system / Project-engineering boundary causes duplicated semantic implementations
    private/public consequence handling leaks prohibited meaning or yields false public currentness
    operating burden is disproportionate to actual Project scale

## 25. Current boundary

    MC0030=OPEN
    PHASE=R0_PROBE_PROTOCOL_PREREGISTRATION
    NEXT_ACTOR=chatgpt

    CLAUDE_MESSAGE_003=72046958ce4f5c1f79375bb71dfa2291607e1ba9
    MESSAGE003_DISPOSITION=ACCEPT_WITH_REFINEMENTS
    RESEARCH511=AMENDED
    RECONCILED_CANDIDATE=GOVERNED_LEDGER_KERNEL_V02

    COMPETING_FINALISTS=NOT_REQUIRED
    V03_REOPEN=false
    PHYSICAL_ARCHITECTURE_SELECTED=false
    OWNER_DECISION=NOT_READY

    R0_P01=NOT_RUN
    R0_P02=NOT_RUN
    R0_P03=NOT_RUN
    PROBE_PROTOCOLS=NOT_YET_FROZEN

    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    RUNTIME_BRIDGE_EXTRACTION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED
    AUTHORITY_SWITCH_AUTHORIZED=false

    NEXT=R0_P01_TO_P03_PROTOCOL_PREREGISTRATION
