# V1 System-Owned Provenance Recommendation and Action Value Result

**Specification:** 019 v0.1  
**Date:** 2026-08-24  
**Frozen advancement outcome:** `FAIL`  
**Experiment source:** `6b5e6237b738250458550f95c9f3a6b0d51e86ec`  
**Live workflow run:** `32664534864`  
**Artifact ID:** `9499756280`  
**Preserved raw bundle commit:** `f5fbef4d6384ee08e873cb1ef9ccb3ed8ec31f2f`

## Result in one sentence

Specification 019 successfully repaired the provenance instrumentation boundary exposed by Specification 017, completed the full matched live design with exact system-owned context provenance, and then **failed the preregistered recommendation/action advancement contract** because SELECTIVE was not sufficiently accurate on RB-02, was not semantically adequate on RB-04, was not per-case non-inferior to either control on RB-02, and produced more blocking-scope false positives than FULL_HORIZON.

The recommendation/action seam is therefore **not promoted**.

---

## Frozen execution integrity

The frozen run completed exactly as planned:

```text
reasoner outputs          36 / 36
judge outputs             36 / 36
scored outputs            36 / 36
provider attempts         72 / 90
retries                    0
complete scored design     true
execution integrity        true
```

The live source matched the provider-free validated source exactly. The locked Specification 017 base fixture retained Git blob:

```text
eac949c47a01878dcc47dcca1116493a02ba9805
```

The Specification 019 overlay SHA-256 was:

```text
c4e7f567ea24c96efa3c20a61e9ca66cd30f1b0bb2ee47d0ddc57eaafc28d08
```

All deterministic provenance invariants evaluated by the runner passed. GENERIC carried an empty revision list, SELECTIVE carried the exact inherited selected revisions, FULL_HORIZON carried all ten accepted revisions, payload hashes and byte counts recomputed exactly, and the model-owned result had no `methodological_basis` field or path capable of mutating system provenance.

This closes the Specification 017 instrumentation defect. It does not by itself establish recommendation value.

---

## Aggregate frozen metrics

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           0.944444       0.916667        0.944444
semantic score           0.950000       0.950000        0.950000
critical omissions       0              0               0
under-recommendations    0              0               0
over-recommendations     0              0               0
blocking false negatives 0              0               0
blocking false positives 4              6               4
clarification FN         0              0               0
clarification FP         0              0               0
defer-pointer errors     0              0               0
unnecessary cost         0              0               0
```

Descriptive methodology-context size remained strongly selective:

```text
GENERIC mean bytes          2.0
SELECTIVE mean bytes     2691.5
FULL_HORIZON mean bytes 10772.0
SELECTIVE / FULL ratio      0.249861
```

That compactness is descriptive instrumentation only. Specification 019 preregistered recommendation/action quality and expansion behavior as the advancement criteria.

---

## Per-case frozen quality

Exact disposition accuracy:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
RB-01                    1.000000       1.000000        1.000000
RB-02                    0.777778       0.666667        0.777778
RB-03                    1.000000       1.000000        1.000000
RB-04                    1.000000       1.000000        1.000000
```

Blinded semantic score:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
RB-01                    1.000000       1.000000        1.000000
RB-02                    1.000000       1.000000        1.000000
RB-03                    1.000000       1.000000        1.000000
RB-04                    0.800000       0.800000        0.800000
```

---

## Failed preregistered gates

The mechanically evaluated gate result was:

```text
absolute gates           FAIL
relative gates           FAIL
expansion gates          FAIL
positive value signals   0
advancement outcome      FAIL
```

The failed named gates were:

```text
SPRA-G06  SELECTIVE every-case exact disposition accuracy >= 0.85
SPRA-G08  SELECTIVE every-case semantic score >= 0.85
SPRA-G09  SELECTIVE per-case exact accuracy vs GENERIC >= -0.10
SPRA-G10  SELECTIVE per-case exact accuracy vs FULL_HORIZON >= -0.10
SPRA-G20  SELECTIVE blocking-scope false positives <= FULL_HORIZON
```

RB-02 drove G06, G09, and G10:

```text
SELECTIVE RB-02 exact       0.666667
GENERIC RB-02 exact         0.777778
difference                 -0.111111
FULL RB-02 exact            0.777778
difference                 -0.111111
```

RB-04 drove G08:

```text
SELECTIVE RB-04 semantic    0.800000
required floor              0.850000
```

The expansion failure was:

```text
SELECTIVE blocking-scope false positives    6
FULL_HORIZON blocking-scope false positives 4
```

No inherited positive value signal passed.

---

## Failure anatomy

### RB-02: recommendation versus blocking calibration

The frozen truth required the two compact nonlinear model comparisons to be `RECOMMENDED`, with tuning `DEFER`red until `model-family-selected`.

Across all three SELECTIVE repetitions, both model-comparison actions were instead elevated to `BLOCKING_REQUIRED`, and both supplied blocked scopes were emitted. This produced:

```text
SELECTIVE RB-02 exact accuracy        0.666667 in all 3 repetitions
SELECTIVE RB-02 blocking FP           2 in all 3 repetitions
```

GENERIC and FULL_HORIZON showed the same over-blocking pattern in repetitions 1 and 2 but were correct in repetition 3, producing `0.777778` per-case exact accuracy and four aggregate blocking false positives each. SELECTIVE was therefore both below the frozen per-case floor and more expansion-prone than FULL_HORIZON.

The error is not a DEFER-pointer failure. The model correctly deferred tuning behind `model-family-selected`. The failed boundary is the calibration between useful model comparison and work that truly blocks a defended downstream scope.

### RB-04: treatment-invariant semantic omission

All conditions achieved perfect deterministic disposition accuracy on RB-04, but every condition received semantic score `0.800000`.

The blinded judge consistently found one frozen obligation absent: the response did not explicitly state that preprocessing/resampling must be fit on training data only and then applied consistently to validation/test/production data to prevent held-out leakage.

Because this semantic shortfall was treatment-invariant, it is not evidence against SELECTIVE specifically. It nevertheless fails the preregistered absolute SELECTIVE case floor, and the frozen contract contains no post-hoc exemption for a common ceiling effect.

---

## What Specification 019 establishes

Specification 019 provides strong bounded evidence for the **instrumentation architecture**:

```text
SYSTEM-OWNED PROVENANCE
    exact supplied stable_key@revision_id
    methodology payload digest
    methodology byte count
    treatment identity

MODEL-OWNED CONTENT
    dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales
```

The entire 36-output reasoner design completed without provenance-induced structured-output failures and without retries. Exact context provenance should therefore remain a deterministic system trace rather than a mandatory model-authored result field.

This positive instrumentation result is distinct from the failed scientific value claim.

---

## What Specification 019 does not establish

The result does **not** justify any of the following:

```text
production recommendation/action seam promotion
production REQUIRED/BLOCKING semantics
production DEFER/NOT_NOW enums
claim that SELECTIVE methodological context improves recommendation quality
claim that SELECTIVE context is generally harmful
final recommendation ranking or prioritization policy
final provider/model selection
multi-agent recommendation architecture
automatic project mutation or execution
```

The observed failure is bounded to this exact prospective benchmark, treatment, model/runtime configuration, and frozen advancement contract.

---

## Architectural consequence

The next experiment should not spend effort repairing provenance instrumentation again. That boundary is now clean.

The unresolved scientific problem is narrower:

```text
methodological context
    -> recommendation calibration
    -> RECOMMENDED versus truly BLOCKING_REQUIRED
    -> defended downstream scope
```

A subsequent design should prospectively test whether blocking status requires a more explicit system-owned dependency/claim-scope representation or another bounded calibration mechanism. It must preserve strong GENERIC and FULL_HORIZON controls, avoid tuning from Specification 019 repetitions, and freeze any changed semantics before another provider call.

No new provider-backed recommendation experiment is authorized by this result.

---

## Durable evidence

Raw bundle:

```text
experiments/system_owned_provenance_recommendation_action_value/results/
    spec019-live-20260824-run-32664534864/
```

The bundle contains the exact reasoning plan, system provenance plan, reasoner attempt ledger, blinded judge plan, judge attempt ledger, result JSON, SQLite evidence store, generated result summary, and a manifest with exact contained-file hashes.

The outer artifact came from GitHub Actions artifact ID `9499756280`. GitHub may repackage the outer ZIP between downloads, so durable preservation authority is the exact run/artifact/source identity plus the verified hashes of every contained experiment file recorded in `ARTIFACT_MANIFEST.md`.
