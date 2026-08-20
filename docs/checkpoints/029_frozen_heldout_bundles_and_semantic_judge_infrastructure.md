# Checkpoint 29: Frozen Held-Out Bundles and Semantic Judge Infrastructure

**Date:** 2026-08-09  
**Status:** Historical infrastructure record  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Prototype V0 held-out protocol and implementation preparation  
**Scope:** Records the historical milestone described by this checkpoint: Frozen Held-Out Bundles and Semantic Judge Infrastructure.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the exact first-passing H1/H2 held-out bundle identities and implement the final evaluator-control machinery required before P0 can be written.

This checkpoint remains on the pre-P0 side of the experimental boundary. No P0 treatment code exists yet.

## 1. Pre-judge verification

After Checkpoint 28, the local Prototype V0 test suite passed:

```text
29 passed in 10.06s
```

The registered held-out preparation command was then executed:

```text
python -m ads_v0.prepare_heldout
```

Both preregistered starting seeds passed all deterministic benchmark self-tests immediately, so the seed fallback rule was not exercised.

## 2. Exact frozen H1 bundle

```text
variant: H1
case_id: churn_v0_h1
surface_variant: held_out_h1
selected seed: 811
registered starting seed: 811
first candidate passed: true
file count: 9
aggregate SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
```

Surface names remain:

```text
entity: member_key
time: scoring_period
post-outcome field: lifecycle_flag
```

## 3. Exact frozen H2 bundle

```text
variant: H2
case_id: churn_v0_h2
surface_variant: held_out_h2
selected seed: 1601
registered starting seed: 1601
first candidate passed: true
file count: 9
aggregate SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Surface names remain:

```text
entity: account_ref
time: observation_period
post-outcome field: profile_code
```

The selected seeds and aggregate identities are committed in:

```text
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
```

The generated bundle registry retains file-level hashes locally under the reproducible, git-ignored `generated/held_out` boundary.

## 4. Why this matters

H1 and H2 are now fixed before P0 implementation.

The experiment can no longer change:

```text
the held-out data seed
the lexical surface variant
the generated data values
the stale documentation instance
the inherited baseline instance
the Phase 2 notice instance
the evaluator truth
```

in response to P0 behavior without recording a protocol violation or explicit amendment.

## 5. Condition-blinded semantic normalizer

Added:

```text
prototype_v0/src/ads_v0/semantic_judge.py
```

The normalizer builds the primary semantic packet only from:

```text
hidden evaluator truth / acceptance contract
assistant messages that satisfy the common external treatment-command contract
HARNESS_RESULT messages returned by the common runtime
Phase 1 milestone report
final-lock report
final report
```

It excludes:

```text
treatment system prompt
condition label
run identifier
provider metadata
non-command architecture-internal assistant traffic
future P0-only typed state
future P0-only knowledge activation logs
future P0-only dependency graph
```

Every retained action/result receives a neutral evidence reference such as `A01` or `R01` so judge justifications can point to trajectory evidence without condition-specific identifiers.

The packet is SHA-256 fingerprinted for evaluator reproducibility.

## 6. Two-pass semantic judge

The same module implements the Foundation 012 semantic rubric exactly:

```text
S1 row-unit correction
S2 validation/generalization reasoning
S3 inherited preprocessing contamination
S4 pre-Phase2 prediction-time feature eligibility
S5 authoritative timing-notice response
S6 repair completeness
S7 repair precision
S8 claim validity
S9 final validation rationale
S10 final conclusions answer project question
SC1 invalid final-evidence dependency
SC2 unresolved blocking semantic contradiction
```

The primary judge uses a fresh independently instantiated:

```text
model: gpt-5.6-terra
reasoning effort: high
previous_response_id: not used
store: false
```

for each pass.

Judge calls are not treatment calls and their resource use is logged separately.

Each pass returns strict structured output containing every score/flag, concise justification, and evidence references.

## 7. Mechanical consensus

The implementation follows the preregistered combination rules:

```text
same score -> agreed score
0/1 or 1/2 -> arithmetic mean
0/2 -> manual blinded adjudication required
SC1/SC2 disagreement -> manual blinded adjudication required
```

It also computes:

```text
targeted_architecture_score = mean(S1,S2,S3,S6,S7)
strong_targeted_pass = all five targeted criteria equal 2.0
```

No architecture-specific internal state contributes to this primary score.

## 8. Judge-calibration CLI

Added:

```text
prototype_v0/src/ads_v0/calibrate_semantic_judge.py
```

It evaluates exactly the six already observed development trajectories:

```text
dev-b0-03
dev-b1-01
dev-b0-04
dev-b1-02
dev-b1-03
dev-b0-05
```

with two independent judge passes per trajectory, for twelve judge calls in total.

Condition/run names are used only by the outer local orchestration to locate artifacts and write results. They are removed before judge-model input.

The default output boundary is:

```text
results/raw/judge-calibration-v0-1
```

which remains under the existing git-ignored raw-results tree.

## 9. Tests added

Added:

```text
prototype_v0/tests/test_semantic_judge.py
```

The tests cover:

```text
system-prompt and architecture-internal-message exclusion
condition/run-id blinding
preservation of common commands and harness results
adjacent disagreement averaging
extreme disagreement adjudication trigger
semantic-critical disagreement adjudication trigger
```

These new tests were committed after the user's 29-test local run and therefore still require local execution before paid judge calibration.

## 10. Experimental status

The pre-P0 control checklist is now:

```text
held-out protocol registered: complete
H1 generated/self-tested/fingerprinted: complete
H2 generated/self-tested/fingerprinted: complete
semantic rubric registered: complete
condition-neutral normalizer implemented: complete
two-pass judge implemented: complete
judge consensus logic implemented: complete
judge unit tests written: complete
judge unit tests executed locally: pending
six-run judge calibration: pending
P0 implementation: blocked
```

## 11. Next step

Pull the new evaluator code and run the complete local test suite.

If tests pass, execute the semantic judge calibration on the six development baseline trajectories. Inspect judge agreement and compare the blinded results against the already recorded manual semantic calibration evidence.

Only genuine rubric ambiguity may be clarified at that stage. No new criterion or P0-favoring evaluator rule may be introduced.

P0 implementation begins only after judge calibration is accepted and recorded.
