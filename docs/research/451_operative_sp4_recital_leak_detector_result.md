# Research 451: OPERATIVE SP-4 recital-leak detector result

**Date:** 2026-10-02
**Status:** SP-4 COMPLETE / SP4_DETECTOR_PLAUSIBLE / SEMANTIC DETECTOR OUTPERFORMS LEXICAL BASELINE / SP-5 AUTHORIZATION BOUNDARY NEXT
**Protocol:** Research 450
**Claude annotation commit:** 692da0f31d47a3c7a226ab80f2d764eff1f936cf
**Claude annotation Git blob:** 03a387e59b2c6c355b72e6aca46e22fe406c80a3
**Claude annotation SHA-256:** 222512102de4b97f6ea2359cafa70d99fdbf5bc204f992a3ba38174f17c39de0
**Result artifact:** experiments/ao10_operative_sp4_v01/SP4_RESULT_V01.json
**Result SHA-256:** 8b9ec84fbfa6ecd9b4dd84a0469d9360a3946c05fc3f0fcaf9234a4442f687df
**Scope:** Record the blinded qualified-project-detector recital-leak result and compare it with the frozen lexical baseline.
**Authority:** Development evidence only. This result does not select OPERATIVE for production, amend Specification 028, authorize production implementation, expose hidden R2 material, resume dependent DRPs, migrate repository state, authorize SP-5, or switch authority.

## 1. Annotation integrity

Claude Message 013 changed exactly one file:

    docs/model_collaboration/threads/MC-0029/messages/013_claude_sp4_recital_leak_annotation.json

The file conforms to the frozen annotation schema.

Observed:

    annotations     24
    LEAK            12
    NO_LEAK         12

Claude reported that it used only:

    DETECTOR_PACKET.md
    reviewer_packet.json
    annotation_schema.json
    current routing/inbox/state

and did not inspect:

    evaluator_key.json
    lexical_baseline.py
    score_sp4.py
    future SP-4 results
    hidden R2 item-level semantics

The commit was fast-forwarded into the coordination branch before scoring.

## 2. Semantic detector result

Frozen truth set:

    LEAK      12
    NO_LEAK   12

Observed confusion matrix:

    TP = 12
    FN = 0
    FP = 0
    TN = 12

Therefore:

    recall       = 1.000000
    precision    = 1.000000
    specificity  = 1.000000

Frozen plausible thresholds:

    recall >= 0.90
    precision >= 0.75

Therefore:

    SP4 = SP4_DETECTOR_PLAUSIBLE

Claude's three lowest-confidence calls were S008, S015 and S024.

All three nevertheless matched the frozen hidden key.

## 3. Frozen lexical baseline

The simple keyword detector was frozen before Claude annotation.

Observed:

    TP = 9
    FN = 3
    FP = 4
    TN = 8

Therefore:

    recall       = 0.750000
    precision    = 0.692307692308
    specificity  = 0.666666666667

The lexical baseline does not reach the frozen SP4_DETECTOR_PLAUSIBLE or SP4_AMEND recall threshold.

## 4. Comparative interpretation

On this seeded 24-item development packet:

    qualified semantic detector:
        12/12 leaks found
        0 false positives

    simple lexical detector:
        9/12 leaks found
        4 false positives

This supports retaining an **advisory semantic recital-leak detector** as a candidate safeguard.

It also rejects the idea that this specific crude lexical rule is already an equivalent substitute.

It does not establish that only a large generative LLM can perform the role.

Future alternatives may include:

    a smaller typed classifier
    a fine-tuned/local classifier
    a stronger structural/static lint
    a hybrid structural + semantic detector

Technology choice remains open.

## 5. Architectural consequence

The result strengthens the V0.2 boundary:

    accepted machine semantics should be explicit
    AND
    recital text can be checked for likely omitted machine consequences

The detector remains detective-only.

A LEAK prediction means:

    review the governing artifact
    determine whether a consequence is missing from the operative/domain-contract surface
    amend through the proper acceptance path if necessary

A LEAK prediction does not mean:

    the detector's inferred interpretation becomes authoritative

This preserves the J1 authority boundary.

## 6. Important limitations

The result is deliberately narrow.

First:

    the 24 items are seeded development cases authored from known Project semantics.

They are now development-burned.

Second:

    Claude was a project-qualified detector with substantial context.

This is not zero-context generalization evidence.

Third:

    all items are short recital excerpts.

The probe does not establish performance on long ambiguous documents, mixed paragraphs, or adversarially subtle omissions.

Fourth:

    the hidden key was authored by ChatGPT.

The perfect detector score therefore does not by itself establish independent objective semantic truth.

It shows agreement with the frozen development target under the qualified-author contract.

Fifth:

    the lexical baseline is intentionally crude.

Its underperformance does not rule out stronger non-LLM structural methods.

## 7. Route consequence

The progressive development sequence now stands:

    SP-0 = MIXED_EXISTING_IDIOM
    SP-1 = OPERATIVE_GRAMMAR_PLAUSIBLE
    SP-2 = V02_MICRO_SURVIVES
    SP-3 = SP3_MECHANISM_PLAUSIBLE
    SP-4 = SP4_DETECTOR_PLAUSIBLE

The next planned probe is SP-5 owner-review efficacy with deliberately seeded material errors.

Research 438 and Research 443 require explicit informed owner authorization before any seeded-error owner-review execution.

Therefore:

    SP-5 may be designed/frozen
    but must not execute
    and no seeded review packet may be presented to the owner
    until the owner explicitly authorizes a knowingly seeded-error experiment.

SP-6 detective-only null-baseline comparison remains mandatory after the owner-review-efficacy question is resolved.

## 8. Current disposition

    SP4=COMPLETE
    SP4_RESULT=SP4_DETECTOR_PLAUSIBLE

    CLAUDE_RECALL=1.0
    CLAUDE_PRECISION=1.0
    CLAUDE_SPECIFICITY=1.0

    LEXICAL_RECALL=0.75
    LEXICAL_PRECISION=0.692307692308
    LEXICAL_SPECIFICITY=0.666666666667

    ADVISORY_SEMANTIC_LEAK_DETECTOR=RETAIN_AS_CANDIDATE
    DETECTOR_AUTHORITY=false
    MODEL_TECHNOLOGY_SELECTED=false

    OPERATIVE_V02=CONTINUE_DEVELOPMENT
    OPERATIVE_V02_TARGET_STATUS=NOT_SELECTED

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED_NOW=false

    NEXT=FREEZE_SP5_OWNER_REVIEW_EFFICACY_PROTOCOL
