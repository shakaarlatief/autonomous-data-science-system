# Research 450: OPERATIVE SP-4 recital-leak detector protocol and blinded packet freeze

**Date:** 2026-10-02
**Status:** SP-4 PROTOCOL + SEEDED PACKET FROZEN / CLAUDE DETECTOR ANNOTATION NEXT / NO RESULT OBSERVED
**Parent:** Research 449 / Research 442 / Claude Message 011
**Fixed evidence base:** e74d60e9651952dbaa8bc050bc9ca1d4e1a55d30
**Implementation manifest:** experiments/ao10_operative_sp4_v01/implementation_manifest.json
**Implementation manifest SHA-256:** e71230be96ca101800e6f460f1736d0ea74ed05d7fb4b50f8355f6b0d55d39a2
**Scope:** Prospectively freeze the SP-4 seeded recital-leak corpus, blindness boundary, detector contract, scoring rules, lexical baseline and development result classes before any detector annotation is observed.
**Authority:** Development-probe protocol only. This record does not select OPERATIVE for production, amend Specification 028, authorize production implementation, expose hidden R2 material, resume dependent DRPs, migrate repository state, authorize SP-5, or switch authority.

## 1. Question

SP-4 asks:

> Can a bounded inferential detector identify machine-binding consequences that have accidentally leaked into human recital text, while avoiding excessive false alarms on rationale, history, examples, quotations, hypotheses and human-only governing principles?

The detector is advisory only.

A LEAK prediction produces review attention.

It does not itself create, amend, delete or reinterpret governing authority.

## 2. Why SP-4 exists

OPERATIVE reduces authoritative semantic inference by making machine consequences explicit at acceptance.

That creates a residual safety risk:

    consequential machine meaning may accidentally remain only in recital text

If that happens silently, the system may under-track a real governing consequence.

The leak detector is therefore a boundary guard.

It is not a substitute for explicit authoring.

## 3. Frozen corpus

The corpus contains:

    24 recital excerpts

with hidden evaluator composition:

    12 LEAK
    12 NO_LEAK

The items are derived only from public SP-2 development cases and the accepted OPERATIVE development direction.

No hidden R2 item-level material is used.

The order is deterministically shuffled from the fixed evidence-base commit so label/source grouping is not exposed in the reviewer packet.

Reviewer-facing artifact:

    experiments/ao10_operative_sp4_v01/reviewer_packet.json

Hidden scoring key:

    experiments/ao10_operative_sp4_v01/evaluator_key.json

## 4. Frozen LEAK definition

Classify LEAK when the recital sentence itself asserts a current binding machine-relevant consequence that would require an accepted operative clause or exact domain-contract/control reference for deterministic Project-system use.

Examples of machine consequence classes include:

    authorization
    prohibition
    gate
    required effect
    consequential sequencing
    lifecycle condition
    machine-validity rule

Classify NO_LEAK when the sentence is:

    rationale
    evidence
    history
    quotation
    description of an already-existing authoritative rule
    rejected option
    hypothetical possibility
    illustrative syntax
    prediction
    open research question
    human-governing principle with deliberately no direct deterministic machine consequence

Normative-looking vocabulary is not sufficient for LEAK.

Importance to humans is not sufficient for LEAK.

## 5. Detector contract

SP-4 tests a:

    QUALIFIED_PROJECT_DETECTOR

not a zero-context fresh-model claim.

Detector:

    Claude interaction claude-04

Execution contract:

    one pass
    current Claude-04 model/configuration
    reviewer-facing packet only for item classification
    no evaluator key
    no lexical baseline
    no scorer
    no result-derived material
    no hidden R2 item semantics
    no external research required

Claude may rely on the frozen detector definition and its existing project context, but may not inspect the hidden labels before committing the annotation.

This tests whether a project-qualified semantic detector can protect the recital boundary.

It does not establish cross-model generalization.

## 6. Reviewer-facing files

Claude may read:

    experiments/ao10_operative_sp4_v01/DETECTOR_PACKET.md
    experiments/ao10_operative_sp4_v01/reviewer_packet.json
    experiments/ao10_operative_sp4_v01/annotation_schema.json

Claude may also read current MC-0029 routing/state only to verify that this obligation is current.

Before committing the annotation Claude must not inspect:

    experiments/ao10_operative_sp4_v01/evaluator_key.json
    experiments/ao10_operative_sp4_v01/lexical_baseline.py
    experiments/ao10_operative_sp4_v01/score_sp4.py
    any future SP-4 result/scoring artifact
    hidden R2 semantic material

## 7. Required annotation artifact

Claude writes exactly one artifact under the existing MC-0029 Claude write boundary:

    docs/model_collaboration/threads/MC-0029/messages/013_claude_sp4_recital_leak_annotation.json

Schema:

    experiments/ao10_operative_sp4_v01/annotation_schema.json

Every one of the 24 item IDs must appear exactly once.

Allowed labels:

    LEAK
    NO_LEAK

Confidence and a short reason are required but do not alter scoring.

## 8. Frozen scoring

Primary metrics:

    recall
    precision
    specificity

Positive class:

    LEAK

Development result classes:

### SP4_DETECTOR_PLAUSIBLE

    recall >= 0.90
    AND
    precision >= 0.75

### SP4_AMEND

    recall >= 0.80
    AND
    precision >= 0.60
    but SP4_DETECTOR_PLAUSIBLE is not reached

### SP4_STRUCTURAL_FALLBACK_REQUIRED

    recall < 0.80
    OR
    precision < 0.60

These are development-routing guards, not scientific universal thresholds.

The 0.90 recall target follows Message 011's proposed boundary.

The precision guards operationalize a small review burden for this 24-item micro-probe.

No threshold tuning is permitted after annotation.

## 9. Frozen lexical baseline

A simple keyword detector is frozen before Claude annotation.

It is intentionally crude.

It flags recital text containing phrases such as:

    must
    shall
    required / requires
    may not
    cannot
    only after / only if
    remain(s) blocked
    prohibited / prohibit
    invalid
    before

Its result is descriptive and non-gating.

Purpose:

    determine whether a semantic detector adds value over trivial structural lint
    or whether a simpler boundary guard may already be competitive

The lexical baseline is scored only after Claude annotation is committed.

## 10. Interpretation rules

If Claude is plausible and materially more precise/recall-capable than the lexical baseline:

    retain an advisory semantic leak detector as a candidate OPERATIVE safeguard

If Claude is plausible but the lexical baseline is comparable:

    do not assume an LLM is necessary;
    prefer the simpler mechanism unless later evidence justifies semantic-model cost

If Claude is AMEND:

    inspect development errors
    refine detector contract or combine structural lint + semantic review
    do not promote detector authority

If structural fallback is required:

    OPERATIVE's recital/operative boundary cannot rely on semantic detection alone

    strengthen structural authoring/lint constraints
    then re-test whether the boundary remains usable

If both semantic and structural detection are impractical:

    reopen the O1 expressiveness/boundary architecture

## 11. Blindness and development burn

The evaluator key is public-repository material but blinded from Claude until annotation commit.

After annotation/scoring:

    all 24 items are development-burned

They may be inspected and used to improve the detector.

They cannot later serve as untouched confirmation for a tuned descendant.

## 12. Execution integrity

Pre-annotation manifest binds exactly:

    reviewer_packet.json
    evaluator_key.json
    DETECTOR_PACKET.md
    annotation_schema.json
    lexical_baseline.py
    score_sp4.py

Manifest SHA-256:

    e71230be96ca101800e6f460f1736d0ea74ed05d7fb4b50f8355f6b0d55d39a2

Observed before freeze:

    reviewer items = 24
    hidden LEAK labels = 12
    hidden NO_LEAK labels = 12
    Python scorer/baseline syntax = valid
    manifest file hashes = valid

No detector annotation exists at this freeze boundary.

## 13. Current boundary

    SP4_PROTOCOL=FROZEN
    SP4_PACKET=FROZEN
    SP4_LABELS=12_LEAK_12_NO_LEAK
    SP4_DETECTOR_CONTRACT=QUALIFIED_PROJECT_DETECTOR
    SP4_ANNOTATION_OBSERVED=false
    HIDDEN_R2_DETAILS=SEALED
    OWNER_NORMATIVE_JUDGMENT_REQUIRED=false
    NEXT=CLAUDE_MESSAGE013_SP4_RECITAL_LEAK_ANNOTATION
