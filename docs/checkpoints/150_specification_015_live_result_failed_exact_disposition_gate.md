# Checkpoint 150: Specification 015 Live Result Failed Exact Disposition Gate

**Date:** 2026-08-23  
**Status:** Live frozen-result checkpoint; complete Specification 015 execution preserved; frozen advancement outcome `FAIL`; recommendation/action seam not promoted  
**Checkpoint class:** LIVE EVALUATION RESULT  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the first real recommendation/action-value experiment, its exact artifact, frozen gate classification, failure localization, and the resulting diagnostic boundary.  
**Authority:** Historical experiment result plus current routing consequence. Specification 015 v0.1 remains the immutable authority for how this completed experiment was evaluated. This checkpoint does not rewrite its frozen thresholds or promote its benchmark dispositions into production semantics.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-recommendation-action-value`  
**Associated PR:** #13 -> `v1-frontend-spike`  
**Live workflow run:** `32642733784`  
**Frozen source head:** `d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4`

## 1. Complete live execution

The manual workflow:

```text
V1 recommendation action value live
run 32642733784
job frozen-live-experiment / 97202216781
```

completed successfully as an execution workflow.

It checked out exactly:

```text
d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
```

and reran the frozen provider-free gate before making live calls.

Observed live execution:

```text
reasoner outputs       36 / 36
judge outputs          36 / 36
scored observations    36 / 36
provider attempts      72 / 90 maximum
retries                0
complete scored design true
```

The successful GitHub workflow conclusion means the experiment ran to completion and uploaded its audit bundle. It is distinct from the internal experimental advancement result.

---

## 2. Raw result preserved before interpretation

GitHub Actions artifact:

```text
artifact id      9494161645
artifact name    v1-recommendation-action-value-d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4-1
artifact digest  30229c8a7f7a00d4c170ba382dcf1817964ede04f61427c057b27d1ac7a78408
```

The exact downloaded ZIP digest matched the digest reported by GitHub Actions.

Before interpretive or canonical changes, the complete bundle was committed at:

```text
611237d8d412b977a6c66755411dd97bcc22627e
Preserve frozen Specification 015 live artifact
```

Durable path:

```text
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
```

Contents include:

```text
artifact.zip      complete original Actions artifact
MANIFEST.md       run/artifact identity and SHA-256 audit
RESULT.md         mechanically generated runner report
result.json       mechanically generated aggregate result
```

The ZIP contains the original:

```text
reasoning_plan.json
judge_plan.json
reasoner_attempts.jsonl
judge_attempts.jsonl
result.json
RESULT.md
recommendation_action_value.sqlite3
```

This satisfies the preserve-before-tuning boundary.

---

## 3. Frozen advancement classification

The mechanically generated result is:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0

advancement       FAIL
```

Fourteen of fifteen named gates passed.

The single failed gate was:

```text
RA-G05
For every case:
SELECTIVE mean exact disposition accuracy >= 0.80
```

`RA-02 MODEL_CHOICE` observed:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
```

Therefore Specification 015 **fails** its frozen advancement contract.

The outcome is not eligible for post-hoc relabeling as `SAFE_BUT_NOT_DIFFERENTIATED` or `PROMOTE_BOUNDED_RECOMMENDATION_SEAM`.

---

## 4. Aggregate results

```text
                         GENERIC      SELECTIVE      FULL_HORIZON
exact accuracy           0.916667     0.916667       0.916667
semantic score           0.960417     0.991667       0.991667
critical omissions       0            0              0
blocking false negatives 0            0              0
blocking false positives 1            0              0
under-recommendations    0            0              0
over-recommendations     0            0              0
unnecessary cost         0            0              0
clarification false neg. 0            0              0
unsupported basis        0            0              0
```

Per-case SELECTIVE result:

```text
          exact accuracy   semantic score
RA-01     1.000000         0.966667
RA-02     0.666667         1.000000
RA-03     1.000000         1.000000
RA-04     1.000000         1.000000
```

No critical SELECTIVE methodological omission, blocking-scope false negative, unsupported basis reference, under-recommendation, over-recommendation, unnecessary recommended cost, or required-clarification miss was observed.

---

## 5. Failure localization

The RA-02 action truth contained two noncritical `DEFER` actions:

```text
add-generic-bagging-baseline
plot-all-feature-histograms-before-shortlist
```

All three SELECTIVE repetitions classified both as:

```text
NOT_NOW
```

rather than the frozen expected:

```text
DEFER
```

All three FULL_HORIZON repetitions produced the same two-label mismatch.

GENERIC produced essentially the same pattern: two repetitions returned `NOT_NOW` for both; one repetition returned `DEFER` for bagging but `NOT_NOW` for broad histogram plotting.

Consequently:

```text
SELECTIVE RA-02 exact mean      0.666667
FULL_HORIZON RA-02 exact mean   0.666667
GENERIC RA-02 exact mean        0.722222
```

The condition-blinded semantic judge nevertheless scored all nine RA-02 outputs at `1.000000` and found the requested compact model-shortlist behavior correct.

This localizes the measured failure to exact disposition calibration, especially the operational `DEFER` versus `NOT_NOW` boundary, rather than to a critical methodological omission.

That diagnosis does not override the frozen gate.

---

## 6. Secondary evidence

`RA-03 EVIDENCE_PLAN` produced one GENERIC repetition that incorrectly promoted histogram inspection to `BLOCKING_REQUIRED` and emitted one blocking-scope false positive.

Observed RA-03 means:

```text
GENERIC exact      0.944444
GENERIC semantic   0.875000

SELECTIVE exact    1.000000
SELECTIVE semantic 1.000000

FULL exact         1.000000
FULL semantic      1.000000
```

These differences remain descriptive because the preregistered value-signal set did not include semantic superiority or fewer blocking false positives versus GENERIC.

The frozen promotion-value result remains:

```text
value signals = []
```

Even without the RA-G05 failure, Specification 015 therefore would not have earned `PROMOTE_BOUNDED_RECOMMENDATION_SEAM` under its frozen value rule.

---

## 7. Context-efficiency diagnostic

Efficiency was not a hard Specification 015 gate, but SELECTIVE again carried materially less provider input than FULL_HORIZON:

```text
mean reasoner input tokens
SELECTIVE       1609.25
FULL_HORIZON    3625.42
ratio           0.443880
reduction       55.61%
```

This is consistent with accepted Specification 014 context-economy evidence. It does not rescue the failed downstream recommendation gate.

---

## 8. Supported interpretation

Supported:

```text
Specification 015 fails its frozen recommendation/action advancement contract.
The failure is narrow and concentrated in RA-02 exact disposition calibration.
The same discrepancy appears in all three conditions, so it is not attributable specifically to SELECTIVE context.
Critical blocking/recommendation behavior remained strong on this benchmark.
SELECTIVE did not demonstrate a preregistered positive value signal over the strong controls.
```

Not supported:

```text
that the bounded recommendation seam should be promoted
that the four experimental dispositions are production-ready
that automatic Proposal/Question/Decision mutation should begin
that SELECTIVE methodological context caused the failure
that reusable methodological knowledge is harmful
that the RA-02 evaluator truth should simply be changed after observing the outputs
```

---

## 9. Promotion audit

### Promote Specification 015 recommendation/action seam

**Decision:** no.

Reason: frozen outcome `FAIL`.

### Promote benchmark dispositions into production semantics

**Decision:** no.

Reason: the first live gate exposed a measurable ambiguity/calibration problem around `DEFER` versus `NOT_NOW`.

### Promote automatic project mutation or execution

**Decision:** no.

Reason: recommendation behavior has not earned the prerequisite seam.

### Preserve failure as durable project evidence

**Decision:** yes.

Promote routing to:

```text
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
CURRENT_STATE.md
KNOWLEDGE_MAP.md
README.md
OPEN_QUESTIONS.md
```

### Add project-level decision

**Decision:** no new permanent architecture decision yet.

The current result motivates diagnosis before design commitment.

### Record major change

**Decision:** yes.

The first live recommendation/action gate failed and changes the immediate development direction from promotion/project-state coupling to failure attribution and disposition-semantics diagnosis.

---

## 10. Exact continuation

Do not repair Specification 015 in place.

Do not merge PR #13 into `v1-frontend-spike` as an accepted recommendation seam.

Next:

```text
1. reconcile canonical routing around the preserved FAIL result
2. validate the exact result-preservation head
3. close PR #13 without promotion once the failure record is green
4. start a separate diagnostic branch from the last accepted integration boundary
5. preregister a bounded disposition-semantics/failure-attribution diagnostic before new live calls
6. distinguish DEFER-vs-NOT_NOW specification ambiguity from model calibration failure
7. only after that diagnosis decide whether a revised recommendation seam deserves a new experiment
```

The accepted integration branch remains at the Specification 014 promotion boundary until a later recommendation design earns promotion.
