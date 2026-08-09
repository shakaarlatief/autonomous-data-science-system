# Current State

## Checkpoint

**Checkpoint:** 28  
**Date:** 2026-08-09  
**Development stage:** Held-out protocol preregistered; final pre-P0 controls pending  
**Implementation status:** B0/B1 development calibration is complete and fully analyzed. The held-out evaluation contract, resource envelope, semantic rubric, run ordering, and continuation/falsification criteria are now registered independently of P0. P0 remains intentionally unimplemented until H1/H2 are generated and fingerprinted and the blinded semantic judge is calibrated on the six development baseline trajectories.

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## System-level vision

Checkpoint 22 distinguishes:

```text
1. Human-executed data-science project
2. Human + interactive LLM project
3. System-mediated data-science project
```

The long-term goal is not merely better prompting. The intended system should operationalize reusable process intelligence that otherwise remains in human methodological memory and project navigation.

The LLM is a reasoning component inside the intended system, not the system itself.

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

B1 remains the primary architectural control because it isolates the value of static methodological prompting from the value of operational state/activation machinery.

## Development calibration complete

The six behavior-evaluable baseline trajectories are:

| Run | Condition | Calls | Total tokens | Python actions | Critical deterministic assertions |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 103,240 | 4 | Pass |
| `dev-b0-04` | B0 | 18 | 147,482 | 7 | Pass |
| `dev-b0-05` | B0 | 19 | 182,271 | 8 | Pass |
| `dev-b1-01` | B1 | 15 | 117,606 | 5 | Pass |
| `dev-b1-02` | B1 | 16 | 112,683 | 5 | Pass |
| `dev-b1-03` | B1 | 17 | 143,014 | 6 | Pass |

Every run completed with zero provider-generation failures and passed the current critical deterministic assertions.

### Resource summary

```text
B0 mean calls: 17.33
B0 mean tokens: 144,331
B0 call range: 15-19
B0 token range: 103,240-182,271

B1 mean calls: 16.00
B1 mean tokens: 124,434
B1 call range: 15-17
B1 token range: 112,683-143,014
```

The first matched pair made B1 appear more expensive, while the three-run mean reversed. This confirms that stochastic trajectory choice materially affects resource use.

## Main baseline semantic findings

Across all six runs, both baseline conditions strongly handled:

```text
protected final-test discipline
legitimate preprocessing in their own evaluation pipelines
future-facing temporal validation
non-mechanical treatment of repeated entities
provisional use of the opaque field under initial documentation
Phase 2 removal of the newly invalid feature
fresh legitimate development evidence before lock
one final protected evaluation
bounded non-causal claims
```

The strongest repeatable B1 advantage was explicit diagnosis of inherited learned-preprocessing contamination:

```text
B0: 0 / 3 explicit diagnoses
B1: 2 / 3 explicit diagnoses
```

This is important because B1 had the relevant concept statically available yet still failed to activate it explicitly in one run. Calibration therefore provides a concrete empirical target for P0's knowledge-activation hypothesis.

Row-unit semantics were operationally understood in all runs but not consistently captured as an explicit durable project conclusion.

Both conditions showed a ceiling effect on Phase 2 repair:

```text
B0: 3 / 3 strong repair
B1: 3 / 3 strong repair
```

P0 therefore cannot justify dependency machinery merely by reproducing that repair on this case family.

Optional methodological coverage remained stochastic. Only `dev-b0-05` independently used customer-cluster bootstrap uncertainty; the other five runs used row-level resampling despite repeated customers.

## Registered held-out protocol

The authoritative protocol is:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

Checkpoint 28 records the registration boundary.

### Held-out variants

H1:

```text
case_id: churn_v0_h1
surface: held_out_h1
seed search starts: 811
customer field: member_key
time field: scoring_period
post-outcome field: lifecycle_flag
```

H2:

```text
case_id: churn_v0_h2
surface: held_out_h2
seed search starts: 1601
customer field: account_ref
time field: observation_period
post-outcome field: profile_code
```

For each variant, the first seed at or above the registered start value that passes all deterministic benchmark self-tests is selected. Treatment performance cannot influence seed selection.

### Held-out run count

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out runs each
30 treatment runs total
```

Condition order is pre-registered and interleaved across replicate blocks.

### Common treatment resource envelope

```text
maximum successful model calls: 24
maximum observed total treatment tokens: 250,000
maximum Python execution attempts: 12
maximum output tokens per provider call: 30,000
maximum additional generation retries: 2
Python timeout: 60 seconds
provider request timeout: 300 seconds
```

Every P0 LLM call, including state/repair reasoning, counts inside the same model-call and token envelope. Deterministic state operations do not create hidden reasoning budget.

Wall-clock time is recorded but remains diagnostic rather than a hard failure criterion in V0.

## Registered semantic evaluator

Ten condition-neutral semantic criteria are scored on an anchored 0/1/2 scale:

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
S10 final conclusions answer the project question
```

Interpretation:

```text
0 = materially wrong/absent/invalid
1 = acceptable but incomplete/implicit/weakly justified
2 = explicit, correct, scoped, and methodologically strong
```

Each behavior-evaluable run receives two fresh condition-blinded judge passes. Primary judge input excludes treatment condition labels, treatment prompts, and P0-only internal state. P0 internal state is diagnostic evidence, not automatic primary-score credit.

Adjacent judge disagreement is averaged. A 0-versus-2 disagreement or disagreement on a semantic critical flag requires blinded manual adjudication.

The targeted architecture score is the mean of:

```text
S1 row-unit correction
S2 validation/generalization
S3 inherited preprocessing integrity
S6 repair completeness
S7 repair precision
```

A strong targeted pass requires all five consensus scores to equal 2.0.

## Registered continuation boundary

P0 provides a continuation signal only if all safety, completion, robustness, and cost requirements hold and it shows a material reliability advantage over B1.

Material reliability is pre-registered as either:

```text
A. at least 2 fewer critical integrity failures than B1 across 10 held-out runs

OR

B. at least +0.30 pooled targeted-architecture mean over B1
   AND at least 2 additional strong targeted-pass runs
```

Additional requirements include:

```text
no more critical failures than B1 overall
no critical architecture-induced false block/over-invalidation
no >0.10 targeted-score deficit versus B1 on either H1 or H2
at least 9/10 P0 completions within budget
median tokens/calls/Python attempts each <=1.50 times B1
at most one P0 budget-exhausted run
architecture-induced noncritical friction in at most 1/10 P0 runs
```

Strong falsification includes P0 having more critical failures than B1, critical false blocking/over-invalidation, architecture friction in at least 2/10 runs, held-out-specific hard coding, or B1 matching/exceeding reliability while P0 is at least 25 percent more expensive in median calls or tokens.

If neither continuation nor strong falsification thresholds are met, the result is classified as inconclusive/no demonstrated need for the architecture on this case family. The default response is not automatic architectural expansion.

## Infrastructure-versus-behavior rule

Terminal provider/infrastructure failure after registered retries is non-behavior-evaluable and may be replaced in the same replicate slot.

Behavioral failures are not replaced, including:

```text
Python exceptions/timeouts
poor methodology
budget exhaustion
semantic failure
failure to finish
critical integrity failure
```

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

with relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

and only the four pre-specified knowledge components.

## Relevant latest checkpoints/foundations

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md

docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
docs/checkpoints/027_full_six_run_baseline_calibration_analysis.md
docs/checkpoints/028_preregistered_held_out_protocol.md
```

## Current priority

**Q-042 is substantively answered for B0/B1 calibration and resource/rubric registration.**

The project is now at the final pre-P0 control boundary.

## Next step

Before P0 implementation:

```text
1. Generate and self-test H1 and H2 according to the registered first-passing-seed rule.
2. Fingerprint the exact first-passing bundles and record their hashes.
3. Implement the condition-neutral semantic trajectory normalizer and two-pass judge.
4. Calibrate that judge on the six already observed B0/B1 development trajectories.
5. Resolve only genuine evaluator ambiguity before P0 exists.
```

After those controls are frozen, P0 implementation can begin.
