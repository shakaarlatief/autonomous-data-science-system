# Research 329: MC-0029 Message 008 Reconciliation, Obligation-Birth V0.6 Candidate, and DRP-03 R2 Protocol V0.2 Candidate

**Date:** 2026-09-25
**Status:** MESSAGE 008 RECONCILED / RESEARCH 328 AMENDED / V0.6 CANDIDATE / R2 PROTOCOL V0.2 CANDIDATE / FINAL PROTOCOL CRITIQUE NEXT / NO HIDDEN KEY OR HARNESS FROZEN
**Parent:** Research 328 / MC-0029 Message 008
**Architecture parent:** Research 327 V0.5
**Public event-universe candidate:** docs/research/project_knowledge_activation_orchestration/ao10/DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V02.json
**Scope:** Reconcile every R2P-1 through R2P-15 requirement, strengthen the obligation-birth architecture where Message 008 exposed real whole-system risks, and define the amended R2 protocol candidate before any hidden labels, evaluator key, or executable harness are created.
**Authority:** Research/protocol candidate only. This record does not accept V0.6, freeze R2, authorize production AO-10, authorize migration, retire current oracles, or switch authority.

## 1. Disposition

Claude Message 008 is accepted as:

    Research 328
        -> AMEND

Research 327's core architecture direction remains supported:

    proposal-time declaration drafting
    acceptance-bound semantic birth
    candidate-only legacy extraction
    natural-owner realization facts
    fully derived realization state

Message 008 demonstrates that the first R2 protocol would not measure those claims cleanly enough.

All fifteen required protocol changes are incorporated below.

## 2. R2-BIRTH universe is now mechanically replayable

Research 328's six-event set is retired.

The R2 V0.2 candidate uses a fixed first-parent history window:

    start
        1435b02729edaf416c8196f224e1cf49c1dd715b
        Apply AO9 P7 D01 amendment

    end
        0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d
        Accept WARRANT-F V0.2 and close R8-C

Candidate rule:

    first-parent commits only

    commit subject matches:
        ^(Accept\b|Apply AO9 P7\b)

    every match is enumerated

No semantic cherry-picking occurs before enumeration.

The resulting eleven events are preserved in the machine-readable event-universe candidate.

This explicitly includes the events Research 328 omitted:

    G-DUAL initial acceptance
    R6 acceptance
    AO9 D01
    AO9 D02
    AO9 D03
    MC-0027 audit acceptance

Each event records:

    exact acceptance commit
    exact direct-parent pre-acceptance snapshot
    event kind
    whole-document proposal source(s)
    exact decision input
    development/held-out split
    scoring eligibility
    exclusion/stress reason where applicable

## 3. Development/held-out split

The split is mechanical and uses no semantic labels:

    event_id
        EV-<first 8 chars of acceptance commit>

    split_value
        first_32_bits(SHA256(event_id)) mod 3

    0
        DEVELOPMENT

    1 or 2
        HELD_OUT

Observed before any key exists:

    DEVELOPMENT
        EV-33af3544
        EV-39a5f8f6
        EV-6e627e53

    HELD_OUT
        EV-1435b027
        EV-02847e6a
        EV-6c1a51c4
        EV-8c85be87
        EV-1d91d0db
        EV-18199147
        EV-46bc4eeb
        EV-0a68787a

EV-46bc4eeb is retained in the universe but marked:

    SECONDARY_STRESS_ONLY_PREDECISION_PACKAGE_INCOMPLETE

because its final ChatGPT reconciliation did not exist before the acceptance commit.

It cannot determine primary BIRTH PASS.

Primary held-out real events therefore equal seven.

## 4. E235 leakage is removed by event splitting

The old combined E235 fixture is retired.

The three P7 decisions are three events:

    EV-1435b027
        P7-D01 / AO8-E01 = AMEND
        snapshot = b908fe0e...

    EV-02847e6a
        P7-D02 / KA-R51 = ACCEPT_REQUIREMENT
        snapshot = 1435b027...

    EV-6c1a51c4
        P7-D03 / KA-R52 = ACCEPT_REQUIREMENT
        snapshot = 02847e6a...

Earlier accepted P7 decisions are valid prior context for later decisions.

They are no longer leaked as answers to a combined three-decision task.

A temporal-fairness validator becomes mandatory:

    every reviewer-visible packet blob
        MUST exist at the event's pre-acceptance snapshot

    no packet content first introduced in
        the acceptance commit
        or any later commit
        may enter the proposal-time packet

Exception:

    separately provenance-tagged verbatim owner decision-time text
        may enter only through the dedicated owner-decision channel

## 5. Reviewers see bounded packets, not repository snapshots

The phrase "pre-acceptance snapshot" identifies file versions.

It does not grant repository visibility.

Decision reviewers receive only the generated reviewer packet.

They do not receive:

    repository checkout
    Git history
    CURRENT_STATE
    current_routing
    checkpoints
    collaboration inbox/state
    acceptance record
    hidden labels
    evaluator keys
    prior R1/R2 research

Proposal sources are whole documents.

Heading-level curation is prohibited.

Whole-document proposal mapping is frozen in the event manifest before key authoring.

The packet generator must prove each included blob came from the stated pre-acceptance snapshot.

## 6. Owner-added decision-time delta is not falsely claimed as historically tested

Research 328's E259 owner-added-delta metric is removed.

The repository preserves the agent-authored acceptance record, but does not bind a repository-native verbatim owner message strongly enough for an unbiased historical capture test.

Therefore:

    HISTORICAL_OWNER_ADDED_DELTA_CAPTURE
        = UNTESTED

EV-18199147 remains usable for ordinary proposal-time birth scoring against Research 258.

Its extra representation-freedom clarification is excluded from the owner-added-delta metric.

V0.6 adds a prospective rule:

    every governed owner decision persists
        exact owner-authored decision text
        plus source/provenance locator

If the exact text is sensitive or belongs outside the public repository:

    private exact-text carrier
        +
    public/private-safe reference and cryptographic binding

is sufficient.

An agent paraphrase is never the verbatim decision record.

If exact owner text is unavailable:

    VERBATIM_DECISION_UNAVAILABLE

must be explicit and chat-only delta recovery cannot be claimed authoritative.

## 7. V0.6 owner-review and anti-authority-laundering controls

Message 008 M-1 is accepted.

Every agent-drafted declaration item records drafting provenance:

    drafting actor/model/tool
    source item IDs
    proposal revision
    declaration revision

The owner-facing review projection must be material-items-first.

At minimum it surfaces before lower-consequence details:

    material accepted delta
    new realization obligations
    changed constraints
    changed sequencing/holds
    authority/cutover effects
    ambiguities requiring owner review
    agent-drafted provenance

A declaration does not gain independent authority by being machine-generated.

Authority still comes from the owner/governance act.

Post-acceptance agent-drafting corrections obey T-2.

A semantic repair that changes obligations still requires explicit owner acknowledgement, even when the correction is obviously aligning the structure to already-authoritative text.

R2 V0.2 does not claim historical owner-review efficacy.

The seeded-error owner rubber-stamp check is:

    EXPLICITLY UNTESTED IN HISTORICAL R2

and is carried as a required later owner-ergonomics/adoption test.

No claim that "owner review catches declaration errors" may be made from R2.

## 8. V0.6 independent completeness audit

Message 008 M-2 is accepted.

Proposal authors must not be the sole completeness authority for their own declaration.

Target rule:

    consequential governing changes
        -> independent completeness audit required before dependent advancement

Lower-consequence changes may use a preregistered sampled audit policy.

The exact consequence boundary remains a later policy/profile decision and is not selected here.

An explicit owner waiver may allow advancement while preserving the missing-audit fact.

A waiver does not make the declaration complete.

## 9. Acceptance-event vocabulary is extended for owner clarifications

V0.5's event kinds remain.

V0.6 adds:

    OWNER_NORMATIVE_CLARIFICATION

for an owner clarification that changes governing interpretation without necessarily selecting a new realization act.

Such an event may yield only:

    PRINCIPLE
    DISPOSITION

and therefore legitimately produce:

    CREATES_NO_REALIZATION_UNITS

This closes the conceptual gap exposed by chat-only owner clarifications without pretending explanatory research automatically has authority.

The authority event, not the word "clarification", determines whether this kind applies.

## 10. Negative birth controls

R2 V0.2 includes two controlled negative birth fixtures:

    NC-PRINCIPLE-01
        accepted PRINCIPLE only

    NC-DISPOSITION-01
        self-executing DISPOSITION only

Expected architectural behavior:

    accepted normative delta exists
    but
    CREATES_NO_REALIZATION_UNITS

These controls do not count toward historical representativeness or sample-size floors.

They test over-declaration.

The final freeze should additionally include a real OWNER_NORMATIVE_CLARIFICATION negative example if an exact pre-decision/verbatim evidence chain can be qualified without leakage.

If not, the result must state that the negative birth controls are controlled rather than historical.

## 11. Key construction becomes a two-author construct-validity stage

A single hidden key is no longer sufficient.

Before any decision reviewer runs:

    Key Author A
        independent labeling

    Key Author B
        independent labeling
        blind to A

Both operate on the same frozen public segmentation and key-author packet.

Neither may serve as a decision reviewer.

Before reconciliation, compute:

    binary normative/non-normative kappa
    normative-kind kappa
    material-item agreement
    MUST_JOIN / MUST_SPLIT constraint agreement

Candidate construct gate:

    binary kappa >= 0.80
    kind kappa >= 0.75
    constrained-pair agreement >= 0.80

Material disagreements:

    must be explicitly adjudicated by the owner
        OR
    cause CONSTRUCT_UNDERDETERMINED when owner adjudication is not appropriate

Owner adjudication cannot retroactively turn poor pre-adjudication construct agreement into a PASS.

Allowed ambiguity:

    applies only to genuinely non-material equivalent interpretations
    is capped at <= 10% of held-out evaluable statements
    is frozen and reported

If the pre-adjudication construct gate fails materially:

    R2 component = CONSTRUCT_UNDERDETERMINED
    decision reviewers do not run against that contested key

## 12. Grouping truth is constraints, not one canonical partition

The hidden grouping key records:

    MUST_JOIN pairs
    MUST_SPLIT pairs
    unconstrained pairs

MUST_JOIN requires the four-part V0.6 realization-boundary rule to clearly unify the items.

MUST_SPLIT requires at least one clear independent boundary such as:

    different realization owner
    different realization artifact/effect
    different qualifying decision
    independently remediable failure

All other pairs remain unconstrained.

Grouping score is computed only over constrained pairs.

The result reports:

    constrained-pair count
    unconstrained-pair count
    unconstrained fraction

No reviewer is penalized for choosing among unconstrained equivalent groupings.

## 13. Segmentation V0.2

The phrase "semantically addressable line" is removed.

Mechanical procedure:

    1. normalize line endings;

    2. retain heading identity as context but not as an item;

    3. remove Markdown list/blockquote syntax before segmentation;

    4. prose and list text use the same frozen deterministic sentence splitter;

    5. a fenced block, indented structured block, or table body is treated as
       one contiguous structured source item per non-blank block;

    6. no judgment-based merge or split is allowed.

Proposal scope:

    whole proposal documents only
    never selected headings

Decision metrics report:

    micro item-weighted values
    macro event-weighted values

The primary semantic decision uses the uniformly segmented statement/item layer.

Line count does not create extra decision weight inside a structured block.

Cost metrics may separately report bytes/tokens/lines.

## 14. BIRTH capture semantics and sample floor

A material item is counted as captured when the reviewer either:

    makes a definitive declaration about it
        OR
    explicitly flags that exact item REVIEW_REQUIRED

REVIEW_REQUIRED is not automatically correct classification.

For a frozen allowed-ambiguity item:

    REVIEW_REQUIRED may be correct

For an item outside the allowed-ambiguity set:

    REVIEW_REQUIRED contributes to
        avoidable-review rate

Primary historical BIRTH scoring requires at least:

    6 primary held-out real events
    40 evaluable held-out statements/items
    20 realization-requiring held-out statements/items

If any floor is not met:

    BIRTH = INCONCLUSIVE

not PASS.

The result reports 95% confidence intervals for precision and recall.

Candidate BIRTH thresholds remain:

    material omission count = 0
        where explicit REVIEW on the item counts as captured

    realization-requiring precision >= 0.90
    realization-requiring recall    >= 0.90
    realization-requiring F1        >= 0.90

    blind reviewer binary normativity kappa >= 0.75
    blind reviewer kind kappa               >= 0.70

    constrained-pair grouping F1 >= 0.80

    false realization-unit rate <= 0.10

    avoidable REVIEW rate <= 0.25

These remain protocol-candidate thresholds until the final protocol review closes.

## 15. LEGACY is source-disjoint from R1 and BIRTH held-out evidence

R2-LEGACY must not reuse R1 witness/control identities.

Final LEGACY corpus must be:

    source-disjoint from R1 hidden controls/witnesses

and, where feasible:

    source-disjoint from held-out R2-BIRTH proposal carriers

The harness freeze must prove that no hidden witness or false-gap identity appears in:

    R1 evaluator key
    R1 reviewer packet
    R1 annotations
    Research 324-327 summaries

At least:

    6 hidden material-gap witnesses
    10 already-realized false-gap controls
    2 negative-control sources

are required.

Candidate thresholds:

    realization-requiring recall >= 0.90
    precision >= 0.75
    F1 >= 0.82

    binary normativity kappa >= 0.65
    normative-kind kappa >= 0.60
    constrained-pair grouping F1 >= 0.70

    hidden witness detection = 100%
    already-realized false-gap rate <= 0.10
    negative-control realization units = 0

LEGACY output remains:

    CANDIDATE_ONLY

regardless of score.

## 16. STATE V0.2 separates reference correctness from reviewer attribution

R2-STATE has two layers.

### STATE-REF

A reference implementation of V0.6 fact validity and state derivation runs against frozen fixtures.

Required fixture classes include:

    no facts
    realization only
    realization + evidence
    realization + evidence + qualification
    complete operational realization
    valid governed deferral

    generic program hold falsely used as deferral
    missing reactivation condition
    missing future evidence path
    stale realization fact
    contradictory current facts
    evidence bound to wrong subject/revision

    valid deferral + stale irrelevant evidence
    deferral whose reactivation condition has already occurred
    scoped-selector deferral excluding the obligation
    superseded governing parent with realization lifecycle preserved separately

STATE-REF expected accuracy:

    100%

Failure of the reference implementation against the frozen specification is:

    HARNESS_INVALID
        or
    CONSTRUCT_UNDERDETERMINED

depending on whether implementation or specification caused the conflict.

It is not automatically architecture AMEND.

### STATE-ATTRIBUTION

Two fresh blind reviewers receive frozen candidate source facts.

The real mapping corpus must be frozen with the harness.

It includes verbatim real repository holds/distractors of the class that caused R1 DEFERRED/UNLINKED disagreement.

Candidate gates:

    exact derived-state agreement >= 0.90
    material DEFERRED vs UNLINKED disagreement = 0

The result reports fact-validity disagreement separately from final-state disagreement.

## 17. Reviewer independence V0.2

Claude-04 cannot count toward any R2 inter-reviewer threshold.

ChatGPT chatgpt-30 cannot count toward any R2 decision-reviewer threshold.

Two fresh blind decision reviewers are required.

Preferred:

    two different providers

Operational freshness requires:

    no ADS Project memory
    no account memory carrying ADS project content
    no past-chat search
    no repository checkout
    no Git-host connector
    no unrestricted web access to the repository
    reviewer-facing packet only

Each reviewer output retains:

    environment/provider/model identity
    freshness attestation
    packet digest
    declared tool use
    available tool-call evidence/log reference where the platform exposes one

If a reviewer environment cannot satisfy the blindness boundary:

    that annotation is descriptive only

and cannot establish blind thresholds.

## 18. Key concealment

Held-out keys and labels are never committed to reviewer-accessible storage before annotations freeze.

Freeze sequence:

    public corpus/schema/segmentation freeze
        ->
    Key Author A private key + hash commitment
        ->
    Key Author B private key + hash commitment
        ->
    key agreement gate
        ->
    adjudicated final private key + hash commitment
        ->
    reviewer packets
        ->
    Reviewer 1 freeze
        ->
    Reviewer 2 freeze
        ->
    only then publish keys for auditable scoring

Public coordination may store only:

    key digest
    byte length
    schema version
    freeze timestamp
    non-secret provenance

The full key must reside in reviewer-inaccessible storage.

Exact storage technology remains a harness-freeze decision.

## 19. Component result semantics

Each component reports independently:

    PASS
    AMEND
    INCONCLUSIVE
    CONSTRUCT_UNDERDETERMINED
    HARNESS_INVALID

Consequences:

    BIRTH PASS
        supports the target acceptance-birth mechanism only

    BIRTH AMEND
        blocks acceptance-birth qualification

    STATE PASS
        supports V0.6 realization fact/state semantics

    STATE AMEND
        blocks KA-R52 state qualification

    LEGACY PASS
        supports candidate migration/reconciliation assistance

    LEGACY AMEND
        does not negate a BIRTH PASS
        but blocks obligation-unit lineage/migration use

    INCONCLUSIVE
        preserves the relevant hold

    CONSTRUCT_UNDERDETERMINED
        reopens taxonomy/boundary semantics before reviewer scoring

    HARNESS_INVALID
        requires prospective repair/refreeze without architecture inference

No single collapsed R2 label may erase these distinctions.

## 20. COST_CARRY units

R2 records a non-authoritative cost proxy using frozen units:

    proposal source item count
    selected normative item count
    realization-unit count
    declaration UTF-8 byte count
    REVIEW_REQUIRED count
    key-author disagreement count
    owner-adjudication count
    reviewer intervention count

Provider token counts may be recorded when available but are secondary.

Wall-clock time is recorded only when the platform supplies reliable timestamps.

The metric is labeled:

    EXTRACTION_FROM_EXISTING_PROPOSAL_COST

It is not the target cost of authoring declarations while proposals are being written.

DRP-08 must not reuse it without adjustment.

## 21. DRP-07 and other downstream holds

DRP-07 is split:

    clause-level Specification 028 lineage
        MAY PROCEED
        because section -> disposition -> successor mapping does not require
        qualified ObligationUnit semantics

    obligation-unit lineage
        HELD pending R2

DRP-04:

    detectors independent of disputed obligation state may proceed

    obligation-state-consuming detectors remain held

DRP-06:

    obligation-state assertions remain held

DRP-08:

    consumes COST_CARRY only as a bounded proxy
    and must separately measure target authoring/adoption burden

## 22. Whole-system failure modes M-1 through M-6

M-1 OWNER RUBBER-STAMP / AUTHORITY LAUNDERING

    Controls added:
        item-level agent provenance
        material-items-first owner projection
        T-2 owner acknowledgement for semantic declaration repair

    Historical owner-review efficacy:
        UNTESTED

M-2 PROPOSAL-AUTHOR INCENTIVE

    Control added:
        independent completeness audit for consequential governing changes
        plus a later sampled-audit policy for lower consequence

M-3 CHAT-ONLY OWNER DELTAS

    Control added:
        verbatim owner decision evidence with provenance
        public/private-safe exact-text carrier when necessary

M-4 BOOTSTRAP

    First future acceptance of this mechanism uses:

        BOOTSTRAP_DECLARATION

    It is independently audited and revalidated after the mechanism is
    itself accepted/qualified.

    The bootstrap record may not claim the not-yet-accepted mechanism
    already governed its own acceptance.

M-5 HOLD-TO-DEFERRAL MIGRATION BURDEN

    Current historical generic holds are not silently promoted into valid
    DeferralRecords.

    Migration must explicitly classify/convert them.

    DRP-08 must measure that conversion burden.

M-6 ASSURANCE REUSE

    Qualified R2 hidden sensitivity/specificity witnesses become candidate
    WARRANT-F G2 witness material under the same concealment discipline.

    They may not be converted into public named "hidden" controls before
    the assurance campaign that consumes them.

## 23. R2P-1 through R2P-15 disposition

    R2P-1   ACCEPTED
    R2P-2   ACCEPTED
    R2P-3   ACCEPTED
    R2P-4   ACCEPTED / historical metric removed; prospective verbatim rule added
    R2P-5   ACCEPTED
    R2P-6   ACCEPTED
    R2P-7   ACCEPTED
    R2P-8   ACCEPTED
    R2P-9   ACCEPTED
    R2P-10  ACCEPTED
    R2P-11  ACCEPTED / two fresh blind reviewers now mandatory
    R2P-12  ACCEPTED
    R2P-13  ACCEPTED
    R2P-14  ACCEPTED
    R2P-15  ACCEPTED / M-1 historical owner-review efficacy explicitly untested

No R2P requirement is intentionally omitted.

## 24. What remains before freeze

The protocol is not yet frozen.

A final adversarial protocol review should challenge at least:

    event-window and subject-regex construct validity
    proposal-source mapping fairness
    controlled-negative versus historical-negative validity
    sample floors and thresholds
    dual-key-author process
    owner adjudication semantics
    segmentation and structured-block weighting
    reviewer freshness enforceability
    private key-storage feasibility
    component consequence mapping
    bootstrap and verbatim-decision rules
    whether M-1 remaining untested is an acceptable bounded limitation

No hidden key or held-out labels should be created before that review is reconciled.

## 25. Current boundary

    DRP03_R1=AMEND
    RESEARCH327=V05_CANDIDATE
    RESEARCH328=AMENDED_BY_RESEARCH329

    V06=PROSPECTIVE_CANDIDATE
    R2_PROTOCOL_V02=PROSPECTIVE_CANDIDATE

    R2_EVENT_UNIVERSE=11_MECHANICALLY_ENUMERATED_ACCEPT_OR_APPLY_EVENTS
    R2_PRIMARY_HELD_OUT_REAL_EVENTS=7
    R2_NEGATIVE_BIRTH_CONTROLS=2_CONTROLLED
    HISTORICAL_OWNER_ADDED_DELTA_CAPTURE=UNTESTED

    DUAL_KEY_AUTHORS=REQUIRED
    KEY_CONSTRUCT_GATE=REQUIRED
    OWNER_MATERIAL_ADJUDICATION=REQUIRED
    ALLOWED_AMBIGUITY_CAP=0.10

    FRESH_BLIND_DECISION_REVIEWERS=2
    CLAUDE04_DECISION_REVIEWER=false
    CHATGPT30_DECISION_REVIEWER=false

    R2_KEY=NOT_CREATED
    R2_HARNESS=NOT_CREATED
    R2_REVIEWER_ANNOTATIONS=NONE

    CLAUSE_LEVEL_DRP07=MAY_PROCEED
    OBLIGATION_UNIT_DRP07=HELD

    OWNER_DECISION=NOT_READY
    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=CLAUDE04_FINAL_ADVERSARIAL_REVIEW_OF_RESEARCH329_BEFORE_R2_FREEZE
