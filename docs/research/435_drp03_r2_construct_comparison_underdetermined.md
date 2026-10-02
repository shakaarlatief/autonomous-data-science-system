# Research 435: DRP-03 R2 STATE+BIRTH construct comparison is underdetermined

**Date:** 2026-10-02
**Status:** LIVE COMPARISON COMPLETE / CONSTRUCT_UNDERDETERMINED / GOVERNED STOP
**Parent:** Research 434 / Research 433 / Research 330
**Scope:** Preserve the single authorized public-safe P9 comparison of the already-frozen Key Author A and Key Author B STATE+BIRTH commitments.
**Authority:** Empirical construct-comparison result only. This record does not expose hidden item-level key semantics, adjudicate disagreements, create a final key, run dependent decision reviewers, tune thresholds, retry the comparison, implement production AO-10, migrate repository state, retire an oracle, or switch authority.

## 1. Execution boundary

The purpose-specific P9 status preflight returned:

    comparisonReady               = true
    comparisonFrozen              = false
    keyACommitmentVerified        = true
    keyBCommitmentVerified        = true
    componentScope                = BIRTH + STATE
    legacyStatus                  = INCONCLUSIVE
    hiddenSemanticDetailsExposed  = false
    next                          = RUN_COMPARISON

Research 433 had already authorized exactly one mechanical `run_comparison` after verified deployment. That call was executed once through `codex.p9_construct_comparison_operation`.

The comparison froze successfully under:

    algorithm version = STATE_BIRTH_CONSTRUCT_COMPARISON_V01
    Key A commitment  = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb
    Key B commitment  = fe12b806ff28d81171af87d435172495f51a6f45c2164f2eecbc8b58f2f23e84
    component scope    = BIRTH + STATE
    LEGACY             = INCONCLUSIVE / excluded
    P6C                = NOT_RUN

No hidden semantic detail was exposed to the task-owner surface.

## 2. BIRTH aggregate construct metrics

P9 aligned 2709 BIRTH semantic items.

Descriptive normative prevalence:

    Key A  1195 / 2709 = 0.441122185308
    Key B  1001 / 2709 = 0.369509043928

Preregistered gate results:

| Metric | Result | Threshold | Gate |
|---|---:|---:|---|
| Binary normativity Cohen kappa | 0.774540330104 | >= 0.80 | FAIL |
| Normative positive specific agreement | 0.865209471767 | >= 0.80 | PASS |
| Normative-kind Cohen kappa | 0.502907383797 | >= 0.75 | FAIL |
| Material positive specific agreement | 0.841737393909 | >= 0.90 | FAIL |
| Grouping-constraint agreement | 41 / 600 = 0.068333333333 | >= 0.80 | FAIL |

Aggregate disagreement counts exposed by the public-safe projection are:

    material item disagreements       = 722
    grouping constraint disagreements = 559
    non-gating field disagreements    = 565

These are aggregate counts only. P9 did not expose which items or pairs disagreed.

## 3. Ambiguity cap

The frozen ambiguity rule uses the union of items either author marks normative as denominator and marks an item ambiguous when either author sets ambiguity=true.

Overall:

    numerator   = 130
    denominator = 1246
    fraction    = 0.104333868379
    cap         = 0.10
    result      = FAIL

Four of the 13 public event-level cap checks fail. P9 exposed only the already-public packet event IDs and aggregate numerator/denominator/fraction values, as allowed by Research 433.

## 4. STATE-REF aggregate comparison

The 24 frozen STATE fixtures produce:

    fixture count                             = 24
    exact structural agreement count          = 18
    fact-validity disagreement fixture count  = 1
    final-state disagreement fixture count    = 5
    STATE_REF_AUTHORS_AGREE                   = false

The comparison excludes free-text reason from material equality, as preregistered.

No fixture answer, fact partition, or other hidden STATE semantic content was exposed.

## 5. Frozen overall outcome

P9 returned:

    overallOutcome = CONSTRUCT_UNDERDETERMINED

The private comparison record is frozen as:

    SHA-256 = 156622e2e3790a2f810adb2b9038256706ce9d82861c696c4f4c5e1db34e67b0
    bytes   = 297787

The public-safe response reports:

    comparisonFrozen             = true
    hiddenSemanticDetailsExposed = false
    next                         = STOP_CONSTRUCT_UNDERDETERMINED

This result follows the preregistered rule directly. Multiple required BIRTH agreement gates fail, the ambiguity cap fails overall, and STATE-REF contains material structural disagreement. Any one required construct failure is sufficient to prevent final-key progression.

## 6. Scientific interpretation

This result does not establish that either key author is individually correct or incorrect on the hidden semantic items.

It establishes the narrower preregistered conclusion:

    the two independently produced STATE+BIRTH constructions do not meet
    the frozen agreement requirements needed to treat the construct as
    sufficiently determined for the planned downstream decision sequence.

The result is not a harness failure. P9 was already mechanically qualified and verified, both commitments were verified before comparison, the comparison completed successfully, and a deterministic frozen comparison record now exists.

Historical LEGACY remains exactly as before:

    HISTORICAL_R2_LEGACY_COMPONENT          = INCONCLUSIVE
    HISTORICAL_R2_LEGACY_CONSTRUCT_VALIDITY = NOT_ESTABLISHED
    P6C                                      = NOT_RUN

No inference from STATE+BIRTH may be used to rewrite that historical LEGACY status.

## 7. Governed consequence

Research 433 prospectively requires the following behavior for this outcome:

    stop
    do not retry
    do not relabel hidden outputs
    do not tune thresholds
    do not create a final key
    do not use owner adjudication to rescue a failed construct gate

Therefore:

    DRP03_R2_CONSTRUCT_COMPARISON  = CONSTRUCT_UNDERDETERMINED
    FINAL_KEY_CREATION              = NOT_AUTHORIZED
    OWNER_ADJUDICATION              = NOT_APPLICABLE_AS_RESCUE
    DEPENDENT_DECISION_PROGRESSION  = BLOCKED
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

Any continuation beyond this boundary requires a new explicit scientific/project route that respects the failed preregistered construct gate. It cannot be treated as ordinary continuation of the previous final-key sequence.

## 8. Current boundary

    KEY_A_STATE_BIRTH_COMMITMENT = FROZEN
    KEY_B_STATE_BIRTH_COMMITMENT = FROZEN
    P9_COMPARISON_RECORD         = FROZEN
    P9_COMPARISON_OUTCOME        = CONSTRUCT_UNDERDETERMINED
    LEGACY                       = INCONCLUSIVE / EXCLUDED
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    NEXT = STOP_AND_OWNER_ROUTE_FROM_CONSTRUCT_UNDERDETERMINED
