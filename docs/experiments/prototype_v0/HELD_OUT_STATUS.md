# Prototype V0 Held-Out Status

**Status:** Current detailed experiment ledger  
**Experiment authority:** Descriptive execution status only. Frozen experimental rules are governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.  
**Last reviewed:** 2026-08-18  
**Resolved treatment slots:** 8 / 30  
**Next frozen slot:** `h1-r03-b1-a01`

## Purpose

This file holds the detailed current execution ledger for the preregistered Prototype V0 held-out experiment.

It exists so `docs/CURRENT_STATE.md` can remain concise while the experiment continues to accumulate run-level mechanical details.

Individual checkpoints remain the detailed historical provenance for each milestone. This ledger is the current consolidated execution view.

No S1-S10 or SC1-SC2 semantic judging has begun.

---

## Frozen experiment summary

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out slots each
30 treatment slots total

provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed total tokens: 250,000
max Python execution attempts: 12
max output tokens per provider call: 30,000
max additional generation retries per semantic turn: 2
Python timeout: 60 s
provider request timeout: 300 s
```

Frozen bundle identities:

```text
H1 seed 811
SHA-256 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed 1601
SHA-256 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Preregistered order:

```text
H1
r1: B0, B1, P0
r2: B1, P0, B0
r3: P0, B0, B1
r4: B0, B1, P0
r5: B1, P0, B0

H2
r1: P0, B0, B1
r2: B0, B1, P0
r3: B1, P0, B0
r4: P0, B0, B1
r5: B0, B1, P0
```

Replacement policy:

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/interface generation failure
=> replacement eligible inside same slot
```

Maximum attempts per slot are `a01`, `a02`, and `a03`.

---

## Current counts

```text
resolved treatment slots: 8 / 30
behavior-evaluable retained attempts: 8
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

No semantic cross-condition conclusion is drawn from mechanical inspection.

---

## H1 replicate 1

### B0: `h1-r01-b0-a01`

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
model calls: 15
Python attempts: 5
total tokens: 108,891
A0-A4: PASS
```

The run completed the intended three-phase trajectory and retained the legal six-feature final model.

Detailed record:

```text
docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md
```

### B1: `h1-r01-b1-a01`

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
model calls: 14
Python attempts: 6
total tokens: 120,424
A0-A4: PASS
```

The trajectory explicitly identified inherited preprocessing contamination, reasoned about repeated longitudinal observations, used temporal development, removed `lifecycle_flag` after the timing notice, and completed protected final evaluation.

Detailed record:

```text
docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md
```

### P0: `h1-r01-p0-a01`

```text
behavior_evaluable: true
completed: true
budget_exhausted: true
model calls: 14
Python attempts: 6
total tokens: 294,267
A0-A4: PASS
```

The token ceiling was crossed on the terminal final-report call after cumulative usage had been below the ceiling before that call. The completed report was retained and no later treatment call occurred.

Detailed record:

```text
docs/checkpoints/058_h1_r01_p0_full_mechanical_verification_and_terminal_budget_crossing.md
```

---

## H1 replicate 2

### B1: `h1-r02-b1-a01`

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
model calls: 15
Python attempts: 7
total tokens: 139,150
A0-A4: PASS
```

Detailed record:

```text
docs/checkpoints/060_h1_r02_b1_full_mechanical_verification.md
```

### P0: `h1-r02-p0-a01`

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
model calls: 12
Python attempts: 5
total tokens: 226,926
A0-A4: PASS
```

`K-INFO-003` did not activate in this held-out trajectory. The model independently raised the timing concern and completed the Phase 2 repair. This remains frozen behavioral evidence and does not authorize P0 changes.

Detailed record:

```text
docs/checkpoints/062_h1_r02_p0_full_mechanical_verification.md
```

### B0 slot replacement sequence

```text
h1-r02-b0-a01
    non-behavior-evaluable
    ambiguous_structured_output

h1-r02-b0-a02
    non-behavior-evaluable
    ambiguous_structured_output

h1-r02-b0-a03
    behavior-evaluable retained trajectory
```

Both A01 and A02 failed at the provider/interface structured-output boundary before a usable treatment command entered the runtime. Frozen replacement semantics therefore applied.

Retained A03:

```text
completed: true
completed_within_budget: true
model calls: 16
Python attempts: 7
total tokens: 131,563
A0-A4: PASS
```

One model-authored Phase 1 Python bootstrap attempt timed out and the model later used a successful computational rewrite. This is behavioral runtime evidence, not a provider failure.

Detailed records include:

```text
docs/checkpoints/066_h1_r02_b0_a02_provider_ambiguity_verified_and_final_replacement_authorized.md
docs/checkpoints/068_h1_r02_b0_a03_full_mechanical_verification.md
```

---

## H1 replicate 3

### P0: `h1-r03-p0-a01`

```text
behavior_evaluable: true
completed: false
completed_within_budget: false
budget_exhausted: true
model calls: 13
generation attempts: 13
generation failures: 0
Python attempts: 6
input tokens: 247,734
output tokens: 10,751
total tokens: 258,485
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
```

All 13 provider generations and six Python executions completed normally.

Cumulative usage was 217,919 after call 12, so the protected final-evaluation call was legitimately admitted. Call 13 raised cumulative usage to 258,485. The resource gate then stopped later reasoning, so the run reached protected final evidence but did not receive a final-report call.

All four P0 knowledge components activated.

Phase 2 repair invalidated the provisional `lifecycle_flag` evidence and decision, preserved unrelated validation decisions, established eligible replacement evidence, and locked the legal six-feature model.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Protected H1 test evidence:

```text
n: 4,126
events: 460
AUROC: 0.696277
AP: 0.235698
log loss: 0.324630
Brier: 0.093547
mean prediction: 0.103040
AUROC bootstrap 95% interval: [0.669924, 0.721935]
```

Detailed record:

```text
docs/checkpoints/070_h1_r03_p0_full_mechanical_verification_and_second_budget_exhaustion.md
```

### B0 administrative pre-provider interruption

Before the genuine B0 treatment attempt, one invocation failed during OpenAI client construction because a newly opened local terminal did not contain `OPENAI_API_KEY`.

Only `attempt_started.json` had been written. No provider request, model output, trace, Python execution, summary, or treatment command had occurred.

The false-start directory was moved out of the active attempt ledger to:

```text
results/held_out/pre_provider_interruptions/h1-r03-b0-a01_missing_api_key_20260818T1133/
```

After the credential was restored, status returned `READY_INITIAL` for the same genuine `h1-r03-b0-a01`.

This event:

```text
did not consume a01;
did not count as a provider/interface treatment failure;
did not launch inference;
did not change the frozen experiment.
```

Detailed record:

```text
docs/checkpoints/071_h1_r03_b0_pre_provider_interruption_recovery_and_relaunch_authorization.md
```

### B0: `h1-r03-b0-a01`

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 14
generation attempts: 14
generation failures: 0
Python attempts: 6
input tokens: 99,925
output tokens: 8,583
total tokens: 108,508
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
```

All provider generations and Python executions completed successfully.

Generation 1 contained two identical structured output-text blocks that the frozen normalizer correctly collapsed to one distinct command. There was no ambiguous provider failure.

Trajectory:

```text
read README, project brief, inherited baseline
-> inspect chronological and repeated-member development structure
-> leakage-safe Phase 1 temporal model comparison
-> logistic stability, feature-contribution, uncertainty, and calibration analysis
-> Phase 1 complete
-> authoritative lifecycle_flag timing notice
-> eligible-feature Phase 2 redevelopment
-> final model lock
-> exactly one protected final evaluation
-> final report
```

The model explicitly identified inherited validation-preprocessing contamination.

Phase 1 provisionally selected seven features including `lifecycle_flag`. After the authoritative timing notice, the provisional model was treated as invalid and development was repeated without that feature.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Phase 2 validation evidence:

```text
AUROC: 0.6832
AP: 0.2588
Brier: 0.0889
```

Protected H1 test evidence:

```text
n: 4,126
events: 460
prevalence: 0.1115
AUROC: 0.6961
AP: 0.2358
Brier: 0.0935
AUROC bootstrap 95% interval: [0.6684, 0.7234]
AP bootstrap 95% interval: [0.2038, 0.2762]
```

All milestone objects are present and no development followed protected-test access.

Detailed record:

```text
docs/checkpoints/073_h1_r03_b0_full_mechanical_verification.md
```

---

## Preregistered resource consequence

P0 budget-exhausted retained runs currently equal two:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria require no more than one P0 budget-exhausted run.

Therefore that specific continuation condition can no longer be satisfied regardless of later outcomes.

This is an objective resource-envelope result, not a semantic or overall architectural verdict. The frozen experiment continues so reliability, semantic quality, repair precision, completion, false blocking, and comparative resource distributions can still be evaluated without selective stopping.

---

## Next frozen slot

```text
variant: H1
replicate: 3
condition: B1
slot: h1-r03-b1
attempt: h1-r03-b1-a01
```

The next `run-next` invocation must advance at most this one attempt and then stop for terminal classification and mechanical inspection before any H1 R4 execution.

For the exact current authorization, consult `docs/CURRENT_STATE.md` before executing.
