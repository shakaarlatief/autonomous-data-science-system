# Research 328: DRP-03 R2 Exact Preregistration Candidate

**Date:** 2026-09-25
**Status:** R2 PROTOCOL CANDIDATE / BIRTH-LEGACY-STATE SPLIT / CORPUS AND THRESHOLDS PROPOSED / ADVERSARIAL PROTOCOL REVIEW NEXT / NO HARNESS OR HIDDEN KEY FROZEN
**Parent:** Research 327
**Program:** Research 316 / DRP-03
**Scope:** Define the exact candidate design for a second DRP-03 attempt that tests V0.5 obligation birth rather than repeating the R1 construct error, while preserving blind held-out evidence and separating future acceptance birth, legacy candidate extraction, and realization-state attribution.
**Authority:** Preregistration candidate only. This record does not freeze R2, expose a hidden evaluator key, accept V0.5, authorize implementation/migration, or change current authority.

## 1. Why R2 requires a new protocol rather than a repaired R1 matcher

R1 established a real failure:

    free-form retrospective obligation reconstruction
        -> insufficiently reproducible

R2 must not convert that failure into a PASS merely by changing the string matcher.

R2 therefore tests three distinct questions:

    R2-BIRTH
        target future mechanism

    R2-LEGACY
        migration/reconciliation support only

    R2-STATE
        realization-fact validity and derived-state reproducibility

Each component has its own corpus, metrics and decision rule.

A PASS requires all decision-relevant semantic components to pass.

## 2. R2-BIRTH event universe

The candidate event universe is mechanically bounded to six explicit owner/governance acceptance records used in the R7-R8/AO transition program for which a pre-acceptance proposal snapshot exists.

Events are ordered by acceptance commit time.

### E235

    acceptance
        Research 235
        commit 6c1a51c490c863c34486a1bcb186939675b25071

    pre-acceptance snapshot
        02847e6a608d0c0fa2bc3cb8a2a3d93fef981df5

    proposal source
        Research 234

    decision input
        P7-D01 AMEND
        P7-D02 ACCEPT_REQUIREMENT
        P7-D03 ACCEPT_REQUIREMENT

### E248

    acceptance
        Research 248
        commit 8c85be872f11b9a09b2a3f2cef8b52add2072a56

    pre-acceptance snapshot
        3aebde8aca9e0daf69ddcf5cdac073a7eea13eb8

    proposal source
        Research 247

    decision input
        owner amendment acceptance

### E256

    acceptance
        Research 256
        commit 1d91d0dbed289cad7cc0ce06a4268a685910ff87

    pre-acceptance snapshot
        66996189ed772df0cc32038fdb63d232e05bfde5

    proposal source
        Research 255

    decision input
        AMEND

### E259

    acceptance
        Research 259
        commit 181991476bb7091f30235674acf6bfb2b065df59

    pre-acceptance snapshot
        7e9dafd675611632769a482cffca69661567a00e

    proposal source
        Research 258

    decision input
        AMEND
        plus the acceptance-time owner clarification about from-scratch
        representation freedom

    special case
        explicit decision-time delta not fully present in the proposal carrier

### E272

    acceptance
        Research 272
        commit 6e627e539e44b2619de7893cd64b47bc5cb3d422

    pre-acceptance snapshot
        aa0eda73685f6f91d107db99db2d1d7f7f560a1e

    proposal sources
        Research 266
        Research 271

    decision input
        ACCEPT WMR-H V0.3

### E311

    acceptance
        Research 311
        commit 0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

    pre-acceptance snapshot
        78b3e7f2d88e1ab6b51a9dfb85cfdc604d6c074c

    proposal sources
        Research 276
        Research 308
        Research 309
        Research 310

    decision input
        ACCEPT WARRANT-F V0.2 and the R8-A Engineering amendment

No acceptance record itself is reviewer-visible during the declaration-authoring phase.

## 3. Development versus held-out split

The split is fixed without semantic judgment.

Rule:

    split_bit = first_32_bits(SHA256(event_id)) mod 2

    split_bit == 0
        DEVELOPMENT

    split_bit == 1
        HELD_OUT

Frozen result:

    DEVELOPMENT
        E256
        E311

    HELD_OUT
        E235
        E248
        E259
        E272

The event IDs and rule are frozen before any R2 hidden key is authored.

Development events may be used to validate schemas, reviewer instructions and metric implementations.

Held-out labels, obligation keys and acceptance audits must remain unavailable to decision reviewers.

## 4. Proposal-source scope

R2-BIRTH does not dump arbitrary repository history into the reviewer.

Each event packet exposes only:

    exact pre-acceptance snapshot commit
    bounded proposal carrier(s)
    exact decision input
    explicit owner decision-time text when such text itself adds a delta
    V0.5 public taxonomy and realization-boundary rules

The harness-freeze stage must list exact allowed headings for every proposal source before segmentation.

Allowed headings may be selected only to capture the explicit decision package and its directly required semantics.

They must not be tuned after item labels or reviewer results are observed.

## 5. Mechanical segmentation

Segmentation is frozen before any evaluator key.

The candidate deterministic segmentation rule is:

    headings
        context only, never normative items by themselves

    Markdown list item
        one item per list item after removing the list marker

    fenced or indented structured/code line
        one item per non-empty semantic line/row

    prose paragraph
        mechanically split into sentences by a frozen punctuation rule

    blockquote prose
        treated as prose after removing the quote marker

No judgment-based merge occurs during segmentation.

Each item receives:

    event_id
    source_path
    source_revision
    source_heading
    local ordinal
    SHA-256 of exact normalized item text

A stable public item ID is derived from those fields.

Segmentation output is reviewer-visible.

Normative labels are not.

## 6. R2-BIRTH reviewer task

For each event, a declaration reviewer receives the pre-acceptance packet plus decision input and must produce:

    accepted_delta_item_ids

    normative_kind per selected item
        OBLIGATION
        CONSTRAINT
        DISPOSITION
        SEQUENCING
        PRINCIPLE

    realization-requiring item IDs

    ObligationUnit groups
        groups may span headings/files

    responsible semantic owner

    realization boundary

    expected evidence path

    activation/effective boundary

    ambiguity flags
        REVIEW_REQUIRED only where the reviewer can identify the exact ambiguity

    explicit CREATES_NO_REALIZATION_UNITS when applicable

For E259, the owner decision-time clarification is part of the acceptance-time input.

The reviewer is not penalized for content that did not exist in the proposal/decision input.

Instead, the harness separately checks whether acceptance-time added content is incorporated before persistence.

## 7. R2-BIRTH hidden audit

The hidden key is authored only after public mechanical segmentation and the development/held-out split are frozen.

For each held-out event it records:

    accepted normative item IDs
    normative kind
    realization-requiring subset
    canonical or allowed-equivalent unit grouping
    materiality class
    accepted owner-added delta items, if any
    allowed ambiguity set

A material item is one whose omission could change:

    authority
    admissibility
    required realization
    migration/cutover behavior
    protection/hold semantics
    accepted architecture boundary
    owner-approved sequence

The key may allow more than one equivalent grouping when the V0.5 four-part realization-boundary test proves the alternatives semantically equivalent.

The key must never encode reviewer wording.

## 8. R2-BIRTH metrics and candidate thresholds

Held-out decision metrics:

    material omission count
        required = 0

    realization-requiring item precision
        required >= 0.90

    realization-requiring item recall
        required >= 0.90

    realization-requiring item F1
        required >= 0.90

    binary normative/non-normative Cohen kappa between reviewers
        required >= 0.75

    multiclass normative-kind agreement
        required Cohen kappa >= 0.70

    unit grouping
        pairwise same-unit F1 >= 0.80

    acceptance-time owner-added delta incorporation
        required = 100%

    false realization-unit rate
        required <= 0.10

    avoidable REVIEW_REQUIRED event rate
        required <= 0.25 across held-out events

Rationale:

    future acceptance birth is authority-adjacent,
    stable item IDs remove the R1 paraphrase burden,
    therefore R2-BIRTH requires materially stronger precision/recall
    than candidate-only legacy extraction.

The exact threshold set remains a protocol candidate until the adversarial protocol review closes.

No held-out result may be observed before final threshold freeze.

## 9. R2-LEGACY question

R2-LEGACY does not test authority birth.

It asks whether candidate extraction is reliable enough to support:

    migration
    lineage reconciliation
    control observations
    human review

without pretending the extracted units are authoritative.

Reviewer output must carry:

    LEGACY_CANDIDATE=true

and the schema must forbid an authoritative/admission-ready designation.

## 10. R2-LEGACY corpus

Development sources may use previously exposed semantic material.

Held-out decision corpus must contain:

    Specification 028 bounded obligation/gate sections
    Research 311 bounded Engineering/assurance sections
    Research 225 bounded AO-6 branch-execution section
    bounded accepted AO/representation sources
    two non-governing research/candidate negative controls

The harness-freeze record must publish exact paths, revisions, headings and item catalogs.

It must not publish:

    which items are material witness items
    which items are false-gap controls
    evaluator labels
    expected derived states

At least three hidden material-gap witnesses and ten already-realized false-gap controls are required.

The hidden controls bind item IDs and semantic gate/obligation identity, never reviewer wording.

## 11. R2-LEGACY metrics and candidate thresholds

For the fresh blind reviewer:

    realization-requiring item precision >= 0.85
    realization-requiring item recall >= 0.85
    F1 >= 0.85

    binary normative/non-normative kappa >= 0.70
    normative-kind kappa >= 0.65

Across the two independent reviewers:

    pairwise same-unit grouping F1 >= 0.75

Hidden sensitivity/specificity:

    material hidden witness detection
        100%

    already-realized false-gap rate
        <= 0.10

    negative-control realization units
        0

Witness detection is based on the reviewer's derived candidate gap state or explicit candidate gap flag.

It is not based on the presence of a provided witness tag.

## 12. R2-STATE fixture model

R2-STATE freezes accepted unit identities independently of the reviewer.

Reviewers receive source-owned candidate facts and must:

    validate the facts
    identify valid realization/deferral/evidence/qualification/activation facts
    derive the resulting state using V0.5

Development examples may cover the simple lifecycle.

Held-out fixtures must include at least:

    no facts
        -> UNLINKED

    valid realization only
        -> LINKED

    valid realization + evidence
        -> EVIDENCED

    valid realization + evidence + qualification
        -> QUALIFIED

    complete valid realization
        -> OPERATIONAL

    valid governed deferral
        -> DEFERRED

    generic program hold used as deferral
        -> REVIEW_REQUIRED

    deferral missing reactivation condition
        -> REVIEW_REQUIRED

    deferral missing future evidence path
        -> REVIEW_REQUIRED

    stale realization fact
        -> REVIEW_REQUIRED

    contradictory current facts
        -> REVIEW_REQUIRED

    evidence bound to wrong subject/revision
        -> REVIEW_REQUIRED

The final harness may add non-redundant fixtures before freeze.

It may not remove these required failure modes after scoring begins.

## 13. R2-STATE metrics and candidate thresholds

For held-out fixtures:

    fact-validity classification accuracy
        100%

    deterministic state accuracy
        100%

Across independent reviewers on real/candidate source-fact mappings:

    exact derived-state agreement
        >= 0.90

    material DEFERRED versus UNLINKED disagreement
        0

Any failure on the deterministic held-out fact-validity fixtures returns AMEND unless the harness itself is invalid.

## 14. Reviewer roles

ChatGPT in chatgpt-30 is the protocol/key author and therefore is not a decision reviewer.

Claude-04 may serve as:

    protocol critic
    later non-blind comparative reviewer

Claude-04 must not be used as the fresh hidden-witness reviewer because R1 witness identities and the R1 result are already exposed.

R2 requires one new interaction:

    fresh reviewer
        no MC-0029 R1/R2 hidden-key exposure
        no Research 324/325/326/327 result-material exposure
        reviewer-facing packet only

Candidate interaction name:

    Claude-05

The final harness freeze may choose another provider/model instead, but the fresh-blind property is mandatory.

Two independent reviewer annotations must be frozen before comparison.

If ChatGPT or any hidden-key author later becomes an annotator, a third fresh blind reviewer becomes mandatory and key-author results cannot establish blind specificity.

## 15. Reviewer order and exposure

Candidate order:

    1. freeze R2 protocol, public item catalogs, schemas, hidden key and harness

    2. fresh blind reviewer annotation
        first

    3. Claude-04 comparative/non-blind annotation
        without reading fresh reviewer output

    4. freeze both annotations

    5. run the harness

    6. only then expose hidden labels and compare disagreements

Fresh reviewer first prevents current MC-0029 knowledge from shaping the blind packet through response feedback.

Claude-04 may critique the protocol before the hidden key exists, but once the key is frozen Claude-04 must not read it before its annotation.

## 16. Result classes

R2 returns:

    PASS
        all semantic decision gates pass

    AMEND
        harness is valid but one or more semantic gates fail

    HARNESS_INVALID
        evaluator/key/corpus/schema defect prevents the intended construct
        from being measured

A separate non-blocking cost signal is recorded for DRP-08:

    COST_CARRY
        declaration size
        number of units per event
        reviewer ambiguity count
        owner-intervention count
        deferral-authoring burden

Cost does not silently turn an R2 semantic PASS into architecture acceptance.

DRP-08 remains responsible for adoption-economics disposition.

## 17. Falsifier mapping

R2-BIRTH evaluates:

    F-O2 acceptance-birth omission
    F-O4 normative-kind subjectivity
    F-O5 ambiguity burden

R2-STATE evaluates:

    F-O1 state-attribution disagreement

R2 records inputs for:

    F-O3 declaration-authoring burden

R2-LEGACY evaluates whether migration support can detect gaps without creating false authoritative state.

## 18. Downstream holds

Until R2 passes or an explicit later amendment supersedes the dependency:

    DRP-07
        HELD

    DRP-06 obligation-state assertions
        HELD

    DRP-04 detectors consuming obligation state
        HELD

The parts of DRP-04 independent of obligation state may continue later.

DRP-08 must consume R2 cost measurements.

## 19. Adversarial review questions before freeze

The protocol critic must specifically challenge:

    Q1  Is the six-event R2-BIRTH universe representative enough and
        mechanically selected enough?

    Q2  Are the pre-acceptance snapshots and proposal packets temporally fair?

    Q3  Does E259 correctly test decision-time owner-added delta rather than
        unfairly penalizing the proposal author?

    Q4  Can the normative-kind taxonomy be scored without making the hidden key
        merely one reviewer's opinion?

    Q5  Does the four-part realization-boundary rule permit a defensible
        allowed-equivalent grouping key?

    Q6  Are the BIRTH thresholds justified for authority-adjacent use?

    Q7  Are LEGACY thresholds appropriately weaker because outputs are
        candidate-only, without becoming too permissive?

    Q8  Does the STATE component test fact attribution rather than only a
        trivial derivation function?

    Q9  Is one fresh blind reviewer plus one independent non-blind reviewer
        sufficient, given ChatGPT key authorship?

    Q10 Is the split rule or event selection vulnerable to hidden home-field
        advantage?

    Q11 Does the protocol preserve owner authority and avoid recreating a
        universal requirements database?

    Q12 Is any important cross-layer failure mode still absent?

## 20. Current boundary

    RESEARCH327=V05_CANDIDATE
    DRP03_R1=AMEND

    R2_PROTOCOL=PROPOSED_NOT_FROZEN
    R2_HIDDEN_KEY=NOT_CREATED
    R2_HARNESS=NOT_CREATED

    R2_BIRTH_EVENT_COUNT=6
    R2_BIRTH_DEVELOPMENT=E256_E311
    R2_BIRTH_HELD_OUT=E235_E248_E259_E272

    R2_COMPONENTS=BIRTH_LEGACY_STATE
    FRESH_BLIND_REVIEWER_REQUIRED=true
    CHATGPT_DECISION_REVIEWER=false
    CLAUDE04_PROTOCOL_CRITIC=true

    OWNER_DECISION=NOT_READY
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=CLAUDE04_ADVERSARIAL_REVIEW_OF_R2_PROTOCOL_CANDIDATE
