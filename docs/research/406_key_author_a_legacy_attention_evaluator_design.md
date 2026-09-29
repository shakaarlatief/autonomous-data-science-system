# Research 406: Key Author A LEGACY Attention Evaluator Design

**Date:** 2026-09-29
**Status:** ATTENTION EVALUATOR DESIGN FROZEN BEFORE LIVE METRIC OBSERVATION / IMPLEMENTATION AND QUALIFICATION NEXT
**Parent:** Research 405
**Scope:** Freeze the deterministic mechanical evaluator for the post-P5 Key Author A LEGACY attention-consistency gate before any private classification labels are joined to the frozen attention mapping.
**Authority:** Mechanical evaluator design only. This record does not execute the attention gate, expose attention identities, modify labels, authorize replacement, authorize later LEGACY semantic work, assemble Key A, generate a commitment, authorize Key Author B, score DRP-03, implement the successor architecture, or migrate repository state.

## 1. Preconditions

The evaluator may run only when the private Key Author A progress state proves:

    P5 authorized
    P5 phase version = LEGACY_CLASSIFICATION_V02
    accepted P5 batches = exact L01-L18 order
    accepted batch count = 18
    accepted attempt records = exactly 18
    every accepted artifact still matches its accepted SHA-256
    every accepted artifact still passes exact schema and frozen presentation-ID validation
    all accepted P5 session IDs remain unique
    open_p5_batch = null
    current_phase = P5_LEGACY_CLASSIFICATION_ALL_BATCHES_ACCEPTED_AWAITING_ATTENTION_GATE

No semantic model turn is part of this gate.

## 2. Frozen attention input

The evaluator uses only the fixed private copy of:

    inputs/r2_v03/packets/legacy_attention_provenance.json

The caller cannot select or provide a path, presentation ID, semantic-item ID, label, threshold, denominator, or mapping.

The frozen public packet manifest binds the corresponding source bytes at:

    SHA-256 bfc35235ab1aa0a325018fe66c03b14facf43f9ab710ec587ad3901850b459f6
    bytes 540084

The evaluator must fail closed if the fixed private copy does not match this frozen identity.

It must also validate:

    schema_version = 1
    protocol_id = AO10-DRP03-R2-V03
    component = LEGACY_CLASSIFICATION_ATTENTION_PROVENANCE
    exact 18 record identities and metadata
    exact presentation-ID set per batch
    primary_count + attention_duplicate_count = frozen batch presentation count
    total primary presentations = 3088
    total presentations = 3210
    every attention duplicate maps to exactly one primary presentation with the same semantic_item_id
    no semantic_item_id has more than one primary presentation inside a batch
    no malformed or ambiguous duplicate pair is accepted

The evaluator may internally use the attention mapping. It must not return any presentation ID, semantic-item ID, duplicate identity, source identity, private denominator, or semantic label.

## 3. Pair construction

For each frozen attention-duplicate presentation:

    duplicate presentation
        is paired with
    the unique non-duplicate primary presentation
        from the same frozen batch
        with the same semantic_item_id

The primary presentation is the canonical semantic decision for denominator semantics because attention duplicates were preregistered as quality-control presentations and excluded from semantic decision metrics.

## 4. Frozen consistency definitions

Binary normative consistency is evaluated over every valid attention pair:

    binary_consistency
        =
    number of pairs where primary.normative == duplicate.normative
        /
    number of valid attention pairs

Normative-kind consistency uses the preregistered phrase "duplicate pairs where the item is treated as normative" as follows:

    denominator
        =
    valid attention pairs whose canonical primary presentation has normative = true

For every such pair, the kind comparison passes only when:

    duplicate.normative = true
    and
    duplicate.normative_kind == primary.normative_kind

Therefore a duplicate that changes a canonically normative item to non-normative fails both the binary comparison and, for that same canonical normative item, the normative-kind comparison. A canonically non-normative item is excluded from the normative-kind denominator.

An empty normative-kind denominator fails closed rather than being treated as perfect consistency.

Gate comparisons use exact integer numerator/denominator arithmetic, not rounded displayed values.

## 5. Frozen thresholds and disposition

Thresholds remain exactly:

    binary normative consistency >= 0.95
    normative-kind consistency >= 0.90

PASS requires both gates.

FAIL on either gate:

    does not authorize label repair
    does not authorize selective rerun-to-green
    preserves the accepted L01-L18 artifacts unchanged
    requires the preregistered replacement-governance path before key comparison/scoring

PASS:

    preserves the accepted L01-L18 artifacts unchanged
    makes the unique LEGACY catalog eligible for prospectively designed candidate-gap/evidence/grouping work
    does not itself authorize that later work

## 6. Bounded Runtime Bridge operation

The qualified implementation should extend the purpose-specific P5 private-operation surface with one action:

    evaluate_attention

This action accepts no batch key, attempt, session, path, threshold, ID, mapping, or other caller-selected semantic/control input.

The operation must:

    revalidate the full accepted P5 surface
    validate the frozen attention input and pairing invariants
    compute the two metrics mechanically
    persist only the bounded gate disposition in PROGRESS.json
    return only public-safe aggregate quality information

Allowed return shape:

    ok
    action
    gate = PASS | FAIL
    binaryConsistency
    binaryConsistencyPass
    normativeKindConsistency
    normativeKindConsistencyPass
    replacementRequired
    hiddenSemanticDetailsExposed = false

Metric values may be returned as aggregate decimals, matching the Research 362 precedent. Private denominators, item identities and pair identities remain hidden.

On PASS, progress advances to:

    P5_LEGACY_CLASSIFICATION_COMPLETE_ATTENTION_PASS_AWAITING_POST_CLASSIFICATION_PHASE_DESIGN

On FAIL, progress advances to:

    P5_LEGACY_CLASSIFICATION_COMPLETE_ATTENTION_FAIL_AWAITING_REPLACEMENT_GOVERNANCE

The result must be idempotent: re-reading an already recorded identical gate result returns the same bounded receipt and may not recompute against drifted inputs.

## 7. Qualification before live execution

Before the live Key A gate is run, the implementation must pass staged regression cases covering at minimum:

    valid PASS fixture
    binary threshold failure
    normative-kind threshold failure
    empty normative-kind denominator
    malformed mapping
    ambiguous/missing primary
    attention-file digest drift
    accepted-artifact digest drift
    incomplete accepted prefix
    wrong progress phase
    hidden-detail non-disclosure
    retained P5 classification behavior
    retained P4 behavior
    public-surface registration

No live Key A metric may be observed during implementation or staged qualification.

    ATTENTION_EVALUATOR_DESIGN=FROZEN
    LIVE_ATTENTION_METRIC_OBSERVED=false
    NEXT=IMPLEMENT_QUALIFY_PUBLISH_AND_ACTIVATE_BOUNDED_ATTENTION_EVALUATOR
