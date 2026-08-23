# V1 Recommendation and Action Value Result

**Date:** 2026-08-23  
**Benchmark:** `v1-recommendation-action-value-v0.1`  
**Specification:** 015 v0.1  
**Frozen source head:** `d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4`  
**GitHub Actions run:** `32642733784`  
**Job:** `frozen-live-experiment` (`97202216781`)  
**Artifact ID:** `9494161645`  
**Artifact SHA-256:** `30229c8a7f7a00d4c170ba382dcf1817964ede04f61427c057b27d1ac7a78408`  
**Frozen advancement outcome:** **FAIL**

## 1. Execution integrity

The live workflow itself completed successfully. This means the frozen experiment executed and its result bundle was uploaded correctly; it does **not** mean that the experimental promotion gates passed.

Observed execution:

```text
reasoner outputs       36 / 36
judge outputs          36 / 36
scored observations    36 / 36
provider attempts      72 / 90 maximum
retries                0
complete scored design true
```

The workflow checked out the exact frozen source head, reran the provider-free implementation gate before any live call, executed the frozen runner, and uploaded the complete result bundle.

The exact downloaded artifact has been preserved durably at:

```text
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
```

The preserved `artifact.zip` is the complete GitHub Actions bundle. `MANIFEST.md` records the artifact digest and unpacked per-file digests. `RESULT.md` and `result.json` are duplicated outside the ZIP for direct inspection.

## 2. Frozen advancement result

The preregistered evaluator returned:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0

advancement       FAIL
```

Fourteen of the fifteen named frozen gates passed. The only failed gate was:

```text
RA-G05
SELECTIVE mean exact disposition accuracy >= 0.80 for every case
```

The failing case was `RA-02 MODEL_CHOICE`:

```text
RA-02 exact disposition accuracy

GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
```

Therefore the frozen Specification 015 result is **FAIL**. The result must not be relabeled as `SAFE_BUT_NOT_DIFFERENTIATED` or `PROMOTE_BOUNDED_RECOMMENDATION_SEAM` after seeing the outputs.

## 3. Aggregate deterministic and semantic results

```text
                         GENERIC      SELECTIVE      FULL_HORIZON
exact accuracy           0.916667     0.916667       0.916667
semantic score           0.960417     0.991667       0.991667
critical omissions       0            0              0
blocking false neg.      0            0              0
blocking false pos.      1            0              0
under-recommendations    0            0              0
over-recommendations     0            0              0
unnecessary cost         0            0              0
clarification false neg. 0            0              0
unsupported basis        0            0              0
```

Per-case exact accuracy:

```text
          GENERIC      SELECTIVE      FULL_HORIZON
RA-01     1.000000     1.000000       1.000000
RA-02     0.722222     0.666667       0.666667
RA-03     0.944444     1.000000       1.000000
RA-04     1.000000     1.000000       1.000000
```

Per-case semantic judge score:

```text
          GENERIC      SELECTIVE      FULL_HORIZON
RA-01     0.966667     0.966667       0.966667
RA-02     1.000000     1.000000       1.000000
RA-03     0.875000     1.000000       1.000000
RA-04     1.000000     1.000000       1.000000
```

## 4. Exact RA-02 failure pattern

The frozen RA-02 evaluator expected:

```text
compare-random-forest                    RECOMMENDED
compare-gradient-boosted-trees           RECOMMENDED
add-generic-bagging-baseline             DEFER
redesign-temporal-validation             NOT_NOW
reaudit-prediction-time-features         NOT_NOW
plot-all-feature-histograms-before-shortlist  DEFER
```

All three SELECTIVE repetitions returned:

```text
compare-random-forest                    RECOMMENDED
compare-gradient-boosted-trees           RECOMMENDED
add-generic-bagging-baseline             NOT_NOW
redesign-temporal-validation             NOT_NOW
reaudit-prediction-time-features         NOT_NOW
plot-all-feature-histograms-before-shortlist  NOT_NOW
```

So the same two noncritical actions differed from frozen evaluator truth in every SELECTIVE repetition:

```text
add-generic-bagging-baseline
    expected DEFER
    observed NOT_NOW

plot-all-feature-histograms-before-shortlist
    expected DEFER
    observed NOT_NOW
```

FULL_HORIZON produced exactly the same two-label mismatch in all three repetitions. GENERIC produced the same pattern in two repetitions; its first repetition classified the generic bagging baseline as `DEFER` but still classified broad histogram plotting as `NOT_NOW`.

This repeated three-condition convergence is diagnostically important. It does not alter the frozen `FAIL`, but it weakens the hypothesis that the failure was caused specifically by selective methodological context.

## 5. Semantic evidence around RA-02

The condition-blinded semantic judge scored every RA-02 output at:

```text
1.000000
```

for all nine RA-02 reasoner outputs.

The judge explicitly found that the outputs:

```text
recommended Random Forest and Gradient-Boosted Trees
kept both under the locked evaluation design
did not reopen resolved temporal-validation or feature-eligibility work
did not treat generic bagging or exhaustive histogram plotting as necessary expansion
```

Therefore the measured failure is a disagreement in exact disposition calibration, specifically the `DEFER` versus `NOT_NOW` distinction for two noncritical expansion actions, rather than a critical methodological omission or semantic failure in the model-shortlist reasoning.

This is a diagnostic interpretation only. The preregistered exact-label gate remains binding for Specification 015.

## 6. Other observed treatment differences

`RA-03 EVIDENCE_PLAN` produced one GENERIC repetition that elevated `plot-histogram` from expected `RECOMMENDED` to `BLOCKING_REQUIRED` and emitted an unsupported blocked scope relative to frozen truth. This produced:

```text
GENERIC RA-03 exact mean       0.944444
GENERIC RA-03 semantic mean    0.875000
GENERIC total blocking FP      1

SELECTIVE RA-03 exact mean     1.000000
SELECTIVE RA-03 semantic mean  1.000000
SELECTIVE blocking FP          0
```

FULL_HORIZON also scored perfectly on RA-03.

This difference does not satisfy any preregistered promotion-value signal. In particular, the frozen value-signal set did not include semantic-score superiority or fewer blocking false positives versus GENERIC. Those observations therefore remain descriptive and must not be post-hoc converted into promotion evidence.

## 7. No preregistered positive value signal

The frozen promotion rule required at least one explicit value signal after all safety gates passed.

Observed:

```text
value signals = []
```

SELECTIVE aggregate exact accuracy tied both controls at `0.916667`. It had no advantage in critical omissions or under-recommendations versus GENERIC, and no advantage in unnecessary cost, over-recommendations, or blocking false positives versus FULL_HORIZON.

Thus even if RA-G05 had passed, the observed frozen comparison would not have earned `PROMOTE_BOUNDED_RECOMMENDATION_SEAM` under the preregistered positive-value rule.

## 8. Descriptive context-efficiency result

Token efficiency was not a Specification 015 hard gate, but the same context-economy pattern remained visible:

```text
mean reasoner input tokens
GENERIC        950.33
SELECTIVE     1609.25
FULL_HORIZON  3625.42

SELECTIVE / FULL_HORIZON = 0.443880
reduction                  55.61%
```

Mean serialized methodological-context bytes were approximately:

```text
GENERIC            2
SELECTIVE        2683
FULL_HORIZON   10763.5

SELECTIVE / FULL_HORIZON = 0.249268
reduction                  75.07%
```

This is consistent with the previously accepted context-economy seam, but Specification 015 was designed to test downstream recommendation value, not to re-promote token efficiency.

## 9. Supported conclusion

The strongest supported conclusion is:

```text
Specification 015 FAILS its frozen advancement contract.

The failure is narrow:
    one absolute per-case exact-label gate failed
    on RA-02
    because DEFER and NOT_NOW were separated differently
    for two noncritical expansion actions.

The failure is not treatment-specific:
    SELECTIVE and FULL_HORIZON showed the same pattern
    GENERIC showed nearly the same pattern.

Critical methodological behavior remained strong:
    zero SELECTIVE critical omissions
    zero SELECTIVE blocking false negatives
    zero SELECTIVE unsupported basis
    zero SELECTIVE under/over-recommendations
    zero SELECTIVE unnecessary recommended cost
    zero SELECTIVE clarification false negatives
    high semantic scores
```

This result does **not** justify promoting a production recommendation/action seam.

It also does **not** justify concluding that reusable methodological knowledge is harmful. The experiment did not isolate a selective-context-specific failure, and the main discrepancy may involve the operational meaning or benchmark measurability of `DEFER` versus `NOT_NOW`.

## 10. Required next diagnostic boundary

Before another live recommendation experiment or any coupling to authoritative Proposal/Question/Decision mutation, the project should diagnose the failed disposition boundary without editing Specification 015 or its historical result.

The next bounded question should distinguish:

```text
A. recommendation semantics problem
    Are DEFER and NOT_NOW actually separable enough for deterministic project navigation?

B. benchmark-truth problem
    Were the two RA-02 expected DEFER labels defensible under the frozen definitions?

C. model-calibration problem
    Given unambiguous cases, can the reasoner reliably distinguish sequencing-based DEFER from evidence-based NOT_NOW?

D. system-value problem
    After disposition semantics are made measurable, does SELECTIVE add value over GENERIC or merely match a strong reasoner?
```

No result-driven change to the frozen Specification 015 result is permitted. A follow-up must be a separately versioned, preregistered diagnostic or replacement experiment.
