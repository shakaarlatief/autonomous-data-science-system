# Research 330: MC-0029 Message 009 Reconciliation, Obligation-Birth V0.7 Candidate, and DRP-03 R2 Protocol V0.3 Freeze Candidate

**Date:** 2026-09-25
**Status:** MESSAGE 009 RECONCILED / RESEARCH 329 AMENDED / V0.7 CANDIDATE / R2 PROTOCOL V0.3 FREEZE CANDIDATE / OWNER M-1 DEFERRAL DECISION REQUIRED / NO HIDDEN KEY OR HARNESS
**Parent:** Research 329 / MC-0029 Message 009
**Machine event universe:** docs/research/project_knowledge_activation_orchestration/ao10/DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V03.json
**M-1 deferral proposal:** docs/research/project_knowledge_activation_orchestration/ao10/M1_OWNER_REVIEW_EFFICACY_DEFERRAL_PROPOSAL_V01.json
**Scope:** Reconcile all F-1 through F-21 requirements, correct the R2 event split without rewriting historical research, strengthen V0.6 into V0.7 where Message 009 exposed architectural gaps, and identify the one remaining owner authority decision before the public R2 protocol can be frozen.
**Authority:** Research/protocol candidate only. This record does not accept V0.7, make the M-1 deferral valid, freeze any hidden key, create an executable scoring harness, authorize production AO-10, authorize physical migration, retire current oracles, or switch authority.

## 1. Disposition

Claude Message 009 is accepted as:

    Research 329
        -> AMEND

Message 009 confirms that Message 008 was faithfully reconciled and that the BIRTH / LEGACY / STATE split remains sound.

The remaining defects are second-order protocol and authority defects.

F-1 through F-20 are resolved by this candidate.

F-21 is structurally resolved but still requires one explicit owner decision because a valid V0.7 DeferralRecord cannot manufacture its own governing authority.

## 2. Research 329 split defect is corrected prospectively

Research 329 section 3 contains a historical prose error.

It listed two event placements inconsistently with its V0.2 machine file.

Research 329 is not edited.

Instead:

    DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V03.json

supersedes V0.2 and is authoritative for:

    event membership
    proposal-source clusters
    development/held-out placement
    decision-input provenance
    decision-time-delta policy
    restatement policy
    known clarification blind spots

The historical Research 329 prose remains evidence of the defect.

## 3. Event split now operates on proposal-source clusters

Event-level splitting is retired.

Reason:

    EV-1435b027
    EV-02847e6a
    EV-6c1a51c4

all consume Research 234.

Placing one event in development and another held-out leaks identical segmented items across the split.

V0.3 builds connected components over events sharing any proposal-source path.

For each cluster:

    canonical payload
        newline-joined sorted event IDs

    cluster digest
        SHA256(canonical payload)

    split_value
        first 32 bits(cluster digest) mod 3

    0
        DEVELOPMENT

    1 or 2
        HELD_OUT

This rule is frozen before any R2 key or label exists.

Observed V0.3 placement:

    DEVELOPMENT
        EV-33af3544
        EV-39a5f8f6

    HELD_OUT
        EV-1435b027
        EV-02847e6a
        EV-6c1a51c4
        EV-8c85be87
        EV-1d91d0db
        EV-18199147
        EV-46bc4eeb
        EV-6e627e53
        EV-0a68787a

EV-46bc4eeb remains:

    SECONDARY_STRESS_ONLY_PREDECISION_PACKAGE_INCOMPLETE

and cannot determine primary BIRTH PASS.

Therefore:

    primary held-out real events
        8

    primary held-out proposal-source clusters
        6

The development side contains two large independent proposal clusters.

If that is later insufficient for schema/instruction debugging, synthetic development fixtures may be added before freeze.

Held-out material may never be mined for development tuning.

## 4. Clarification-event blind spot is explicit

The selection regex remains:

    ^(Accept\b|Apply AO9 P7\b)

The Apply AO9 P7 alternative is deliberately event-specific.

It exists because the owner P7-D01 AMEND was committed as:

    Apply AO9 P7 D01 amendment

rather than under an Accept subject.

The regex is replayable and complete under its own rule.

It is not complete for V0.7 OWNER_NORMATIVE_CLARIFICATION events.

Known clarification/freedom commits in the same window include:

    770ad49c...
        Clarify proactive capability and semantic Git policy

    470a3b40...
        Clarify unconstrained repository redesign freedom

    ca4ceb67...
        Reconcile R8-B candidates and freeze assurance freedom

    a9f7b71a...
        Freeze WARRANT-F V0.2 with total design freedom

They lack an independently qualified proposal-time/verbatim owner evidence chain suitable for historical birth replay.

Therefore:

    HISTORICAL_OWNER_NORMATIVE_CLARIFICATION_BIRTH
        = UNTESTED

Controlled negatives may test over-declaration behavior.

They do not turn historical clarification birth into tested evidence.

External-validity limitation:

    every historical proposal in this corpus was authored through the same
    ChatGPT-led project process

so PASS would establish qualification for this proposal style, not universal author-style independence.

## 5. Decision-time delta policy applies to every event

E259 was not unique.

For every event, key authors inspect the acceptance-time evidence separately from the reviewer packet.

An item is:

    DECISION_TIME_DELTA

when its accepted status or semantic content is determinable only from:

    acceptance-record content
    owner decision-time addition
    acceptance commit diff
    other evidence unavailable in the proposal-time packet

DECISION_TIME_DELTA items:

    are counted per event
    are reported
    are excluded from reviewer precision/recall
    are excluded from reviewer false-positive accounting when the reviewer
        could not have known them

They do not silently disappear from architecture history.

They demonstrate that historical replay cannot test that part of future birth.

## 6. Restatement rule

R2-BIRTH measures new/changed accepted semantic birth.

Historical proposal packets may restate previously governing semantics without exposing the full accepted baseline to the reviewer.

Key authors therefore tag:

    RESTATED

when the semantic item was already governing immediately before the event and the event does not materially amend it.

RESTATED items are neutral for reviewer precision/recall.

Novelty itself is not a reviewer-scored task.

This prevents the historical replay from requiring a blind reviewer to reconstruct the entire previous authority state merely to avoid duplicate births.

Consequence:

    duplicate-rebirth prevention is not independently qualified by historical R2

and must be checked later in prospective shadow birth.

## 7. Decision-input provenance

Each V0.3 event freezes its reviewer-visible minimal decision token and provenance.

Historical tokens are classified:

    HISTORICAL_OWNER_DECISION_TOKEN_AGENT_TRANSCRIPTION

unless a separately provenance-bound platform export proves verbatim owner text.

The token may tell the reviewer the owner's decision class, such as:

    ACCEPT
    AMEND
    ACCEPT_REQUIREMENT

It may not smuggle acceptance-record explanatory semantics into the pre-decision packet.

The event manifest records:

    acceptance commit
    decision token
    provenance class
    whether verbatim owner authorship is proven

## 8. V0.7 verbatim owner-decision evidence contract

Future governed owner decisions must preserve OwnerDecisionEvidence containing:

    exact platform-exported owner-authored decision text
    capture timestamp/provenance where available
    platform/message locator where available
    exact proposal revision presented
    exact candidate declaration revision presented
    exact owner-facing material-summary revision presented

The context binding is mandatory.

A bare:

    ACCEPT
    AMEND

without the object/revision presented to the owner is insufficient.

If exact owner text is private:

    private exact-text bytes
        +
    private random salt
        +
    public/private-safe salted commitment
        +
    safe provenance/reference

may be used.

The public commitment is:

    SHA256(
        canonical context binding
        || private salt
        || exact owner decision bytes
    )

The salt remains private.

This prevents low-entropy owner text such as ACCEPT from being brute-forced from a public digest.

Agent retyping/paraphrase is not verbatim evidence.

The platform export is preferred.

Identity limitation:

    repository evidence can preserve that a platform/account message was
    captured through the configured owner channel

but under shared or weak external identity it cannot cryptographically prove the
human owner's authorship merely because the committed project record says OWNER.

That limit must remain explicit in assurance claims.

## 9. OWNER_NORMATIVE_CLARIFICATION does not constrain normative kind

Research 329's restriction is removed.

OWNER_NORMATIVE_CLARIFICATION may yield any V0.7 normative kind:

    OBLIGATION
    CONSTRAINT
    DISPOSITION
    SEQUENCING
    PRINCIPLE

The event kind describes how authority entered.

It does not determine the consequence kind.

A clarification may legitimately create no realization units.

It may also create realization-requiring items.

## 10. Negative birth controls V0.3

Negative controls remain controlled because no clean historical negative birth chain is available.

Before reviewer packets freeze:

    controls use the same packet schema as real events
    control prose is adapted to realistic ADS proposal length/structure
    controls receive ordinary-looking event identifiers
    controls are interleaved at hash-derived frozen positions
    reviewers are not told controls exist
    no reviewer-facing field marks them as controls

Their expected result is:

    accepted normative semantics
    CREATES_NO_REALIZATION_UNITS

The result separately reports on real historical events:

    false realization-unit rate by normative kind

This tests the more important mixed-event failure where PRINCIPLE or self-executing DISPOSITION content is over-promoted into obligations.

## 11. Hidden-key authorship and independence

There are two independent key-author slots.

Neither key author may be a decision reviewer.

At least one key author must be fresh:

    no MC-0029 exposure
    no R1 annotation/result exposure
    no access to the other key author's output before freeze

If the ChatGPT protocol/proposal author occupies the other slot:

    PROPOSAL_AUTHOR_BIAS_PRESENT=true

must be recorded.

The fresh key author is the required counterweight.

The proposal author may never be the sole, unchecked source of truth.

## 12. Construct-validity gate V0.3

Before any decision reviewer runs, compare the two independently frozen keys.

Report:

    normative prevalence per author
    binary normative/non-normative Cohen kappa
    positive specific agreement on normative items
    normative-kind kappa
    material-item positive specific agreement
    grouping-constraint agreement

Definitions:

    normative union
        items either key author marks normative

    positive specific agreement
        2 * both_positive
        /
        (2 * both_positive + A_only_positive + B_only_positive)

Candidate pre-adjudication gates:

    binary kappa >= 0.80
    normative positive specific agreement >= 0.80
    normative-kind kappa >= 0.75
    material-item positive specific agreement >= 0.90
    grouping-constraint agreement >= 0.80

Normative-kind kappa is reported on items both authors classify as normative.

Grouping-constraint agreement is computed over the union of item pairs either author constrains.

Material disagreement requires explicit owner adjudication or:

    CONSTRUCT_UNDERDETERMINED

Owner adjudication cannot make a failed pre-adjudication construct gate retroactively pass.

## 13. Allowed ambiguity

The ambiguity cap denominator is not all segmented text.

For each event:

    ambiguity denominator
        union of items either key author marks normative

    allowed ambiguity
        <= 10% of that event's denominator

The result reports:

    numerator
    denominator
    fraction

per event and overall.

Allowed ambiguity is for genuinely non-material equivalent interpretation.

A material disagreement is never hidden in the ambiguity allowance.

## 14. Owner adjudication evidence

Every owner adjudication uses the V0.7 OwnerDecisionEvidence rule.

It binds:

    exact disputed item IDs
    exact alternatives presented
    exact owner-authored response
    exact key revisions being adjudicated

Private owner text uses a salted commitment.

Agent paraphrase may explain the result but cannot replace the adjudication evidence.

## 15. Grouping constraints and score

The final hidden grouping key contains:

    MUST_JOIN
    MUST_SPLIT
    UNCONSTRAINED

Reviewer partition scoring:

    TP
        MUST_JOIN pair reviewer joins

    FN
        MUST_JOIN pair reviewer splits

    FP
        MUST_SPLIT pair reviewer joins

    TN
        MUST_SPLIT pair reviewer splits

Grouping precision/recall/F1 uses TP/FP/FN.

Key-author constraint agreement is computed over the union of pairs either author marked MUST_JOIN or MUST_SPLIT.

Held-out grouping floor:

    MUST_JOIN pairs >= 15
    total constrained pairs >= 30

If either floor fails:

    grouping evidence = INCONCLUSIVE

and BIRTH cannot obtain a complete PASS on historical grouping evidence.

## 16. Segmentation V0.3

The public packet generator must implement one frozen mechanical splitter.

Rules:

    normalize line endings

    headings
        context only

    prose / list / blockquote text
        remove presentation markers
        use the same deterministic sentence splitter

    fenced / indented structured blocks
        split at blank lines
        within each sub-block, split at every line having the minimum
        indentation of that sub-block
        attach deeper-indented continuation lines to the preceding
        top-level line

    Markdown tables
        one item per body row
        header retained as context

No semantic merge/split predicate is permitted.

Before key authoring:

    splitter code is frozen
    sentence-splitter test vectors are frozen
    packet generator is frozen
    every public packet is generated
    generator + splitter + packet bytes are SHA-256 committed

Sentence test vectors must cover at least:

    V0.6 / V0.7 version tokens
    decimal numbers
    section symbol references
    e.g.
    i.e.
    identifiers with periods
    Markdown links
    colon-led lists

No key may exist before those commitments.

## 17. BIRTH sample floors, scoring and uncertainty

Primary held-out historical evidence must satisfy:

    primary held-out proposal-source clusters >= 5
    material normative items >= 30
    realization-requiring items >= 20
    MUST_JOIN pairs >= 15
    total constrained pairs >= 30

The machine V0.3 split currently has:

    6 primary held-out proposal-source clusters

The semantic item/pair floors cannot be known before independent key authoring.

If any floor fails:

    BIRTH = INCONCLUSIVE

No historical window widening is allowed.

Remedy:

    preregistered prospective shadow-birth qualification on future
    acceptance events

not retrospective corpus expansion.

Each blind reviewer must individually meet every reviewer-versus-key threshold.

Inter-reviewer kappa does not substitute for reviewer-versus-key failure.

Precision and recall report:

    point estimate
    95% cluster-bootstrap confidence interval

Bootstrap unit:

    proposal-source cluster

Candidate bootstrap procedure:

    10,000 resamples with replacement
    deterministic seed derived from the public protocol-freeze digest

Confidence intervals are mandatory uncertainty reporting.

The preregistered point thresholds remain the hard decision gates after the sample floors are met.

## 18. BIRTH candidate thresholds

Per blind reviewer:

    material omissions
        0, where explicit REVIEW_REQUIRED on the exact material item counts as captured

    realization-requiring precision >= 0.90
    realization-requiring recall    >= 0.90
    realization-requiring F1        >= 0.90

    false realization-unit rate <= 0.10
    avoidable REVIEW rate       <= 0.25

Between the two fresh blind reviewers:

    binary normativity kappa >= 0.75
    normative-kind kappa     >= 0.70

Grouping per reviewer:

    constrained-pair F1 >= 0.80

The final protocol freeze may change a candidate threshold only before held-out labels exist and must record the rationale.

After key authoring starts, thresholds are immutable for that attempt.

## 19. LEGACY evidence contract

LEGACY remains candidate-only even on PASS.

Each hidden material-gap witness and false-gap control must carry independent repository evidence in the private key.

Allowed evidence forms include:

    exact path + revision proving a realized carrier
    exact test/validator evidence
    exact accepted realization record
    deterministic absence-search specification plus frozen search result
    exact successor/retirement evidence showing the old gap is not live

The evidence must be sufficient to audit:

    REALIZED
    or
    NOT_REALIZED

without relying solely on the key author's label.

At least:

    6 hidden material-gap witnesses
    10 already-realized false-gap controls
    2 negative-control sources

remain required.

## 20. STATE expected-output construction

STATE-REF expected outputs are independently derived twice from the public V0.7 state rules.

Authors are blind to each other's expected outputs before freeze.

If they disagree materially:

    STATE-REF = CONSTRUCT_UNDERDETERMINED

If they agree and the frozen reference implementation deviates:

    STATE-REF = HARNESS_INVALID

Required public fixture classes include all Research 329 fixtures plus:

    insufficient deferral authority
    scoped-selector deferral lacking recorded resolution
    deferral renewal/extension chain
    evidence without REALIZES relation
    two independently sufficient REALIZES facts from different artifacts
        on one unit
    explicit owner waiver under T-3

Candidate semantic expectations:

    insufficient authority
        invalid fact -> REVIEW_REQUIRED

    unresolved scoped selector
        invalid fact -> REVIEW_REQUIRED

    valid continuous renewal chain
        latest valid deferral governs -> DEFERRED

    evidence without REALIZES
        orphan/invalid evidence -> REVIEW_REQUIRED

    two independently sufficient realizers that expose independent failure
        grouping conflict -> REVIEW_REQUIRED

    owner waiver
        may permit advancement
        does not change realization state

The exact fixture bytes and final expected outputs are frozen only after the two-author construct stage.

## 21. Reviewer freshness V0.3

Two fresh blind decision reviewers are required.

For a decision-grade PASS they should be from different providers/model families.

Fresh means:

    no ADS Project memory
    no account memory containing ADS material
    no past-chat search
    no repository checkout
    no Git-host connector
    no web access
    reviewer packet only

The owner is the environment configurer and records:

    isolation settings
    plugin/connector state
    memory state where observable
    model/provider identity
    model knowledge/training cutoff where documented
    tool availability

Training-contamination field:

    cutoff_before_2026_09_22
    cutoff_on_or_after_2026_09_22
    cutoff_unknown

The latter two are explicitly reported as contamination risk.

They do not silently become proof that training data contained the repository.

Reviewer result also records complete declared tool use and available tool-log references.

A reviewer environment that violates the packet-only boundary is descriptive only.

## 22. Key concealment and hash basis

Commitment order:

    public protocol / splitter / generator / packets
        ->
    Key A private bytes + public commitment
        ->
    Key B private bytes + public commitment
        ->
    construct-validity gate
        ->
    adjudicated final private key + public commitment
        ->
    reviewer annotations
        ->
    key publication after both annotations freeze

Every commitment states:

    canonical serialization
    byte length
    SHA-256 of exact canonical bytes
    schema version
    freeze timestamp
    provenance role

Private low-entropy owner text additionally uses the salted commitment rule.

No hidden key is stored in a reviewer-accessible repository or connector.

## 23. Attempt accounting and no retry-to-green

Historical R2 permits at most:

    2 attempts

Attempt 1 is the normal frozen run.

Attempt 2 is permitted only when Attempt 1 is:

    HARNESS_INVALID

and the repair is prospective and specifically bound to the invalidating defect.

If reviewer outputs were observed before the defect was discovered:

    Attempt 2 requires fresh reviewer instances

Held-out labels may be reused only when the invalidating defect is demonstrably independent of reviewer outputs and the reuse analysis is recorded before rerun.

Outcomes:

    AMEND
        no same-corpus retry

    INCONCLUSIVE
        prospective shadow birth, not historical window widening

    CONSTRUCT_UNDERDETERMINED
        reopen semantics/construct definition before any new decision attempt

    HARNESS_INVALID
        one bounded repair attempt allowed

Every attempt, invalid or not, is durably recorded.

No failed decision result may be tuned into green through repeated reviewer replacement, threshold change, corpus widening, or selective refreeze.

## 24. Reviewer quality and labeling-fatigue controls

N-1 is accepted as real protocol risk.

Reviewer/key-author work is partitioned into deterministic source-cluster/event batches.

Candidate maximum:

    400 primary items per batch

Attention checks:

    3% exact duplicate items per batch
    minimum 5 where batch size permits
    maximum 20

They are inserted at hidden hash-derived positions and excluded from semantic decision metrics.

Within-rater gates:

    binary normative consistency >= 0.95
    normative-kind consistency >= 0.90
        on duplicate pairs where the item is treated as normative

A reviewer/key-author failing the quality gate cannot silently be retained because its semantic score is favorable.

Before any key comparison/scoring, one replacement is allowed per slot under a preregistered quality-failure rule.

All failed quality annotations are retained and reported.

If the replacement also fails:

    relevant component = INCONCLUSIVE

This pre-score quality replacement does not authorize semantic retry-to-green.

## 25. Component consequences and owner-decision readiness

BIRTH, STATE and LEGACY remain independently classified.

For V0.7 architecture owner-decision readiness:

    BIRTH = PASS
    and
    STATE = PASS

are required.

LEGACY does not gate V0.7 birth/state owner-decision readiness.

LEGACY gates:

    obligation-unit lineage
    legacy migration/reconciliation assistance
    oracle-retirement uses that depend on legacy units

If LEGACY fails:

    clause-level Specification 028 lineage may still proceed
    obligation-unit lineage remains held

Clause-level lineage output may never be reused as ObligationUnit truth unless later bound through R2-qualified obligation semantics.

BIRTH INCONCLUSIVE:

    historical owner decision remains NOT_READY
    prospective shadow-birth program is required

Production activation remains separately held by unresolved adoption/owner-review evidence even after architecture owner-decision readiness.

## 26. COST_CARRY V0.3

Record:

    proposal source item count
    selected normative item count
    realization-unit count
    declaration UTF-8 byte count
    REVIEW_REQUIRED count
    key-author disagreement count
    key-author labeling item count
    key-author batch count
    owner-adjudication count
    owner-adjudication item count
    reviewer intervention count
    reviewer batch count

Tokens/time may be supplementary when reliable.

All values remain labeled:

    EXTRACTION_FROM_EXISTING_PROPOSAL_COST
    or
    QUALIFICATION_GOVERNANCE_COST

They are not target proposal-authoring cost.

DRP-08 must separately measure:

    target declaration authoring cost
    independent completeness-audit cost
    owner material-review cost
    hold-to-deferral conversion cost

## 27. M-1 proposed governed deferral

Historical R2 cannot test owner rubber-stamp resistance.

The correct rule is not to silently carry this forever.

A complete DeferralRecord proposal now exists:

    AO10-M1-OWNER-REVIEW-EFFICACY-DEFERRAL-V01

It contains:

    exact obligation identity
    blocking reason
    reactivation condition
    future evidence path
    temporal binding
    provenance

Required reactivation boundary:

    before V0.7 production activation, authority switch, or operational
    reliance on agent-drafted declaration semantics

Future evidence:

    prospective seeded-error owner-review efficacy trial

However:

    governing authority = OWNER
    owner decision = PENDING

Therefore it is not yet a valid governed deferral.

The protocol key/harness freeze remains blocked on this one owner decision.

## 28. N-1 through N-4

N-1 LABELING FATIGUE

    addressed by deterministic batching, hidden duplicates, within-rater
    consistency gates, bounded pre-score replacement and durable failed-run evidence

N-2 PROPOSAL-AUTHOR KEY BIAS

    proposal-author participation is tagged
    at least one fresh key author is mandatory
    construct-validity gate and owner material adjudication remain independent

N-3 FORKING PATHS

    maximum historical attempts = 2
    second attempt only for HARNESS_INVALID
    no window widening
    pre-score reviewer replacement bounded to one quality replacement per slot

N-4 CLARIFICATION BLIND SPOT

    historical OWNER_NORMATIVE_CLARIFICATION birth = UNTESTED
    controlled negative behavior is not misreported as historical qualification

## 29. F-1 through F-21 disposition

    F-1   ACCEPTED / corrected by authoritative V0.3 machine file
    F-2   ACCEPTED / proposal-source cluster split
    F-3   ACCEPTED
    F-4   ACCEPTED
    F-5   ACCEPTED / RESTATED neutral
    F-6   ACCEPTED
    F-7   ACCEPTED
    F-8   ACCEPTED
    F-9   ACCEPTED
    F-10  ACCEPTED
    F-11  ACCEPTED
    F-12  ACCEPTED
    F-13  ACCEPTED
    F-14  ACCEPTED AS FREEZE PREREQUISITE
    F-15  ACCEPTED
    F-16  ACCEPTED
    F-17  ACCEPTED
    F-18  ACCEPTED
    F-19  ACCEPTED
    F-20  ACCEPTED
    F-21  STRUCTURALLY ACCEPTED / OWNER AUTHORITY PENDING FOR M-1 DEFERRAL

No other Message 009 change is intentionally omitted.

## 30. Current boundary

    DRP03_R1=AMEND

    RESEARCH329=AMENDED_BY_RESEARCH330
    V07=PROSPECTIVE_CANDIDATE
    R2_PROTOCOL_V03=FREEZE_CANDIDATE

    R2_EVENT_UNIVERSE_MACHINE=V03_AUTHORITATIVE
    R2_EVENT_COUNT=11
    R2_EVENT_CLUSTERS=9
    R2_DEVELOPMENT_EVENTS=2
    R2_HELD_OUT_EVENTS=9
    R2_PRIMARY_HELD_OUT_REAL_EVENTS=8
    R2_PRIMARY_HELD_OUT_CLUSTERS=6

    HISTORICAL_OWNER_ADDED_DELTA_CAPTURE=UNTESTED
    HISTORICAL_OWNER_NORMATIVE_CLARIFICATION_BIRTH=UNTESTED
    DUPLICATE_REBIRTH_PREVENTION=PROSPECTIVE_SHADOW_REQUIRED

    KEY_AUTHORS=2
    FRESH_KEY_AUTHOR_MINIMUM=1
    BLIND_DECISION_REVIEWERS=2
    DIFFERENT_PROVIDER_FAMILIES_FOR_PASS=true

    R2_HISTORICAL_MAX_ATTEMPTS=2
    R2_SECOND_ATTEMPT_ONLY_FOR=HARNESS_INVALID

    R2_KEY=NOT_CREATED
    R2_HARNESS=NOT_CREATED
    R2_REVIEWER_ANNOTATIONS=NONE

    M1_DEFERRAL=OWNER_DECISION_REQUIRED
    R2_PROTOCOL_FREEZE_BLOCKED_ON_M1_DEFERRAL=true

    OWNER_DECISION=REQUIRED_FOR_M1_DEFERRAL_ONLY
    V07_ARCHITECTURE_OWNER_DECISION=NOT_READY
    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=OWNER_M1_DEFERRAL_DECISION_THEN_PUBLIC_PROTOCOL_ASSET_FREEZE
