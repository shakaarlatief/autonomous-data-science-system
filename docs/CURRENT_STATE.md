# Current State

## Checkpoint

**Checkpoint:** 29  
**Date:** 2026-08-09  
**Development stage:** Exact held-out bundles frozen; blinded semantic judge implemented; judge calibration pending  
**Implementation status:** B0/B1 development calibration is complete and fully analyzed. The held-out evaluation protocol was preregistered before P0. Exact H1/H2 bundles are now generated, self-tested, and cryptographically frozen. The condition-blinded two-pass semantic judge and calibration CLI are implemented. New judge tests still need local execution, followed by the six-run judge calibration. P0 remains intentionally unimplemented until that evaluator-control step is accepted.

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## System-level vision

The long-term project distinguishes three abstraction levels:

```text
1. Human-executed data-science project
2. Human + interactive LLM project
3. System-mediated data-science project
```

The LLM is a reasoning component inside the intended system, not the system itself. The system should operationalize reusable process intelligence that would otherwise remain in human methodological memory and project navigation.

## Prototype V0 conditions

```text
B0
Strong LLM + Python + project artifacts + strong generic data-science instruction.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, prospective gate, or dependency repair.

P0
Same model/tools + typed project state + four structured knowledge components
+ activation/applicability + prospective safeguards
+ dependency-aware repair + minimal state-derived action selection.
```

B1 remains the primary architectural control because it isolates better static prompting from operational state/activation machinery.

## Baseline development calibration

Six behavior-evaluable runs completed under the fixed common development configuration:

| Run | Condition | Calls | Total tokens | Python actions | Critical deterministic assertions |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 103,240 | 4 | Pass |
| `dev-b0-04` | B0 | 18 | 147,482 | 7 | Pass |
| `dev-b0-05` | B0 | 19 | 182,271 | 8 | Pass |
| `dev-b1-01` | B1 | 15 | 117,606 | 5 | Pass |
| `dev-b1-02` | B1 | 16 | 112,683 | 5 | Pass |
| `dev-b1-03` | B1 | 17 | 143,014 | 6 | Pass |

Every run had zero provider-generation failures.

Main semantic findings:

```text
B0 and B1 both strongly protected final test.
B0 and B1 both repaired the Phase 2 invalid feature in 3/3 runs.
B0 and B1 both used legitimate preprocessing in their own models.
B1 explicitly diagnosed inherited learned-preprocessing contamination in 2/3 runs.
B0 explicitly diagnosed that inherited contamination in 0/3 runs.
Row-unit semantics were operationally understood but not always durably stated.
Static knowledge presence did not guarantee activation.
Optional methodological coverage remained stochastic.
```

This gives P0 a meaningful falsification target while preventing credit for merely reproducing baseline ceiling behavior.

## Preregistered held-out protocol

Authoritative files:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

The protocol freezes, before P0:

```text
held-out surface mechanisms and seed-selection rule
5 runs per condition on H1 and H2
30 total held-out treatment runs
interleaved run order
common treatment model
resource envelope
semantic rubric
critical triggers
condition-blinded two-pass judge procedure
consensus/adjudication rules
primary and diagnostic outcomes
continuation thresholds
strong falsification conditions
```

## Exact frozen held-out bundles

The registered preparation code was executed after a clean pre-judge test run:

```text
29 passed in 10.06s
```

Both registered starting seeds passed all benchmark self-tests immediately.

### H1

```text
case_id: churn_v0_h1
surface_variant: held_out_h1
selected seed: 811
entity field: member_key
time field: scoring_period
post-outcome field: lifecycle_flag
file count: 9
aggregate SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
```

### H2

```text
case_id: churn_v0_h2
surface_variant: held_out_h2
selected seed: 1601
entity field: account_ref
time field: observation_period
post-outcome field: profile_code
file count: 9
aggregate SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Committed aggregate identity record:

```text
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
```

Generated bundle files and file-level registry remain reproducible under the git-ignored `generated/held_out` boundary.

## Common held-out treatment resource envelope

```text
maximum successful model calls: 24
maximum observed total treatment tokens: 250,000
maximum Python execution attempts: 12
maximum output tokens per provider call: 30,000
maximum additional generation retries: 2
Python timeout: 60 seconds
provider request timeout: 300 seconds
```

Every P0 LLM call, including state or repair reasoning, must fit inside the same call/token envelope. Deterministic state operations do not create hidden LLM budget.

## Semantic evaluator

Primary criteria:

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
```

Scale:

```text
0 = materially wrong/absent/invalid
1 = acceptable but incomplete/implicit/weakly justified
2 = explicit, correct, scoped, and methodologically strong
```

Semantic critical triggers:

```text
SC1 invalid final-evidence dependency
SC2 unresolved blocking semantic contradiction
```

Targeted architecture score:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted consensus scores to equal 2.0.

## Condition-blinded judge implementation

Added:

```text
prototype_v0/src/ads_v0/semantic_judge.py
prototype_v0/src/ads_v0/calibrate_semantic_judge.py
prototype_v0/tests/test_semantic_judge.py
```

The primary judge packet contains only:

```text
hidden evaluator truth and acceptance contract
common external treatment commands and rationales
common HARNESS_RESULT tool outputs
Phase 1 milestone report
final-lock report
final report
```

It excludes:

```text
condition label
run identifier
treatment system prompt
provider metadata
non-command architecture-internal traffic
P0 typed state
P0 knowledge-activation logs
P0 dependency graph
```

Every external action/result receives a neutral evidence reference. The normalized packet is SHA-256 fingerprinted.

Every run receives two fresh independent `gpt-5.6-terra` judge calls at high reasoning effort, without `previous_response_id` and without shared judge context.

Consensus is mechanical:

```text
exact score agreement -> agreed score
adjacent disagreement -> arithmetic mean
0-versus-2 disagreement -> manual blinded adjudication
SC1/SC2 disagreement -> manual blinded adjudication
```

Judge resource usage is logged separately and is not charged to treatment budgets.

## Registered continuation boundary

P0 provides a continuation signal only if all integrity, completion, cross-variant robustness, architecture-friction, and resource requirements hold, plus either:

```text
A. at least 2 fewer critical integrity failures than B1 across 10 held-out runs

OR

B. at least +0.30 pooled targeted-architecture mean over B1
   AND at least 2 additional strong targeted-pass runs
```

If neither continuation nor strong falsification conditions are met, V0 is classified as inconclusive/no demonstrated need for the architecture on this case family.

## P0 remains intentionally unimplemented

Planned minimal P0 state remains:

```text
ARTIFACT
FACT
ASSUMPTION
QUESTION
EVIDENCE
CLAIM
DECISION
OBLIGATION
ACTION
```

Relations remain:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Only the four pre-specified knowledge components may be used in P0.

## Latest checkpoints/foundations

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md

docs/checkpoints/027_full_six_run_baseline_calibration_analysis.md
docs/checkpoints/028_preregistered_held_out_protocol.md
docs/checkpoints/029_frozen_heldout_bundles_and_semantic_judge_infrastructure.md
```

## Current priority

The final pre-P0 control is now **semantic judge calibration**.

## Next step

```text
1. Pull Checkpoint 29 evaluator code.
2. Run the complete test suite, including the new semantic-judge tests.
3. If green, run the two-pass judge calibration on all six development B0/B1 trajectories.
4. Inspect judge agreement, critical-trigger disagreements, and correspondence with the already documented manual semantic calibration evidence.
5. Resolve only genuine evaluator ambiguity while P0 still does not exist.
6. Freeze the accepted judge calibration record.
7. Begin P0 implementation.
```
