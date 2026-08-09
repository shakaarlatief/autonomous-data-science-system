# Current State

## Checkpoint

**Checkpoint:** 24  
**Date:** 2026-08-09  
**Development stage:** Real-model baseline calibration and run-to-run variability measurement  
**Implementation status:** Two behavior-evaluable B0 trajectories and two behavior-evaluable B1 trajectories have completed under the fixed common configuration. The first matched pair has been semantically reviewed. All four completed baseline trajectories pass the current critical deterministic assertions. Two final development replicates remain before cross-run comparison, held-out protocol freezing, and P0 implementation.

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## System-level vision

Checkpoint 22 makes an important abstraction explicit:

```text
1. Human-executed data-science project
2. Human + interactive LLM project
3. System-mediated data-science project
```

The long-term goal is not merely a better one-shot prompt or a better single LLM conversation. The system should progressively operationalize process navigation that otherwise remains in the human's head or must be reconstructed in every project conversation:

```text
reusable methodological knowledge
project-state tracking
questions / assumptions / claims / evidence
context-sensitive investigation activation
alternative generation and applicability reasoning
prospective safeguards
dependency-aware repair
resource-aware prioritization
persistent project memory
selective human escalation
cross-project reasoning reuse
```

The LLM is a reasoning component inside the intended system, not the system itself.

B0/B1 remain useful lower-level controls because they test how much of a specific methodological benefit can already be achieved by a strong reasoner and static prompting before system machinery is credited.

## Prototype V0 experimental question

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

B1 is the critical control. If B1 matches P0's reliability at materially lower complexity or cost, P0 should be simplified or rejected for this project scale.

## Benchmark and common harness

The synthetic development benchmark is a 24-month customer-month churn project with:

```text
train months 1-16
validation months 17-20
test months 21-24
repeated customers plus new entrants
stale README row-unit statement
inherited baseline with learned preprocessing fit on train+validation
opaque account_state_code initially documented as scoring-time information
Phase 2 authoritative notice showing account_state_code is post-outcome/backfilled
protected final test
```

The common runtime provides phase-aware artifact visibility, metadata/value access, declared-input Python execution, tracing, milestone transitions, final-model lock semantics, and resource accounting.

The deterministic evaluator checks benchmark validity, premature test access, post-test development, final feature legitimacy, and Phase 2 re-evaluation after material feature invalidation.

## Fixed development-calibration configuration

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max output tokens per call: 30,000
max additional generation retries: 2
request timeout: 300 seconds
strict Structured Outputs
multi-turn previous_response_id continuation
all-turn reasoning context
```

Do not change these settings during the remaining baseline development replicates unless a genuine condition-neutral infrastructure failure makes continuation impossible.

## Calibration history

### Infrastructure diagnostics

`dev-b0-01` was not behavior-evaluable. It exposed the original 10,000-token output ceiling and missing incomplete-response usage accounting. Checkpoint 16 corrected both condition-neutrally.

`dev-b0-02` was not behavior-evaluable. It exposed duplicate-equal structured message blocks whose SDK aggregate was invalid as one JSON document. Checkpoint 17 added conservative duplicate-equal normalization while preserving ambiguity errors for distinct commands.

### `dev-b0-03`: first behavior-evaluable B0

```text
completed: true
successful model calls: 15
generation failures: 0
input tokens: 96,525
output tokens: 6,715
reported reasoning tokens: 1,203
total observed tokens: 103,240
all deterministic assertions passed: true
```

Semantic review found strong final-test discipline, temporal validation reasoning, precise Phase 2 feature invalidation/repair, and bounded claims. Main weaknesses were an implicit rather than explicit row-unit correction, failure to explicitly diagnose the inherited train+validation preprocessing contamination, and row-level bootstrap uncertainty that ignored repeated-customer dependence.

### `dev-b1-01`: first behavior-evaluable B1

```text
completed: true
successful model calls: 15
generation failures: 0
input tokens: 109,884
output tokens: 7,722
reported reasoning tokens: 2,060
total observed tokens: 117,606
all deterministic assertions passed: true
```

The first matched semantic comparison found that B1 improved explicit reasoning on the exact methodological concepts supplied statically:

```text
explicit diagnosis of inherited learned-preprocessing contamination
explicit customer-month observation-unit statement
more explicit deployment/generalization-regime reasoning
known-versus-new customer subgroup analysis
```

B0 already matched B1 on the central critical-integrity outcomes, especially protected-test discipline and Phase 2 repair. Final protected-test AUROC was effectively identical at about 0.660.

Both conditions shared the optional uncertainty weakness: row-level bootstrap resampling did not account for repeated-customer dependence.

B1 used approximately 13.9 percent more total observed tokens than B0 in the first matched pair.

### `dev-b0-04`: second behavior-evaluable B0

```text
completed: true
successful model calls: 18
generation attempts: 18
generation failures: 0
total observed tokens: 147,482
behavior_evaluable: true
critical deterministic assertions passed: true
```

Compared with `dev-b0-03`, the second B0 replicate used three additional model calls and 44,242 more tokens, approximately 42.9 percent more total token usage. The 20-call ceiling remained sufficient but only two calls were unused.

### `dev-b1-02`: second behavior-evaluable B1

```text
completed: true
successful model calls: 16
generation attempts: 16
generation failures: 0
total observed tokens: 112,683
behavior_evaluable: true
critical deterministic assertions passed: true
```

Compared with `dev-b1-01`, the second B1 replicate used one additional successful model turn but 4,923 fewer observed tokens, approximately 4.2 percent less total usage.

This confirms that model-call count and total token usage need not move together. Per-turn output length, accumulated interaction history, and action selection can materially change total resource use.

## Current operational baseline table

| Run | Condition | Calls | Generation failures | Total observed tokens | Critical deterministic assertions |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 0 | 103,240 | Pass |
| `dev-b0-04` | B0 | 18 | 0 | 147,482 | Pass |
| `dev-b1-01` | B1 | 15 | 0 | 117,606 | Pass |
| `dev-b1-02` | B1 | 16 | 0 | 112,683 | Pass |

The first two B0 runs show much larger token variation than the first two B1 runs, but two trajectories per condition are insufficient to infer a stable variance difference.

All four behavior-evaluable runs completed within the 20-call ceiling and all passed the current critical deterministic assertions.

## First-pair semantic conclusions

The first B0/B1 pair supports only preliminary development conclusions:

```text
Both are strong viable baselines.
Static knowledge can improve explicit reasoning on targeted concerns.
B0 already performs strongly on critical-integrity mechanics.
B1's observed benefit was mainly semantic/process quality, not predictive accuracy.
The observed B1 benefit came with higher token cost in the first pair.
Neither condition solved every methodological issue.
One matched pair is insufficient to estimate stable treatment effects.
```

## Common-interface decision

No new shared provider/runtime defect has been identified since Checkpoint 17.

Do not change the command protocol, milestone schema, benchmark, prompts, model, reasoning effort, or resource ceilings during the remaining baseline development replicates.

The observed row-unit reporting omission and repeated-customer bootstrap weakness must not be converted into post-hoc privileged B1/P0 prompt knowledge during V0.

## Automated validation

The latest code-affecting calibration repair remains CI-validated with:

```text
25 passed in 8.30s
```

No code has changed during the empirical-review checkpoints since that repair.

## Relevant checkpoints

```text
docs/checkpoints/016_first_real_model_calibration_output_budget.md
docs/checkpoints/017_duplicate_structured_output_normalization.md
docs/checkpoints/018_first_behavior_evaluable_b0_run.md
docs/checkpoints/019_first_b0_semantic_trajectory_review.md
docs/checkpoints/020_first_behavior_evaluable_b1_run.md
docs/checkpoints/021_first_matched_b0_b1_semantic_comparison.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
docs/checkpoints/023_second_behavior_evaluable_b0_calibration_run.md
docs/checkpoints/024_second_behavior_evaluable_b1_calibration_run.md
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

The experiment still requires three behavior-evaluable development trajectories per baseline condition before the held-out evaluator/resource protocol is frozen and P0 is implemented.

## Current priority

**Q-042 remains highest priority:** characterize real B0/B1 behavior and resource variability well enough to freeze a fair common protocol independently of P0.

Current behavior-evaluable replicate counts:

```text
B0: 2 / 3
B1: 2 / 3
```

## Next step

Continue the fixed alternating development-calibration order:

```text
next: dev-b1-03
then: dev-b0-05
```

After those two runs complete, compare all six baseline trajectories for run-to-run variance, deterministic outcomes, semantic criteria, repair precision, optional methodological errors, action counts, and token distributions. Then freeze the held-out evaluator/resource protocol and only then implement P0.
