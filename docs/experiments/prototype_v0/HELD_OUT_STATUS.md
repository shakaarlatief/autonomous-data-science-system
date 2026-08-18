# Prototype V0 Held-Out Status

**Status:** Current detailed experiment ledger  
**Experiment authority:** Descriptive execution status only. Frozen experimental rules are governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.  
**Last reviewed:** 2026-08-18  
**Resolved treatment slots:** 9 / 30  
**Next frozen slot:** `h1-r04-b0-a01`

## Purpose

This file is the consolidated execution ledger for the preregistered Prototype V0 held-out experiment.

`docs/CURRENT_STATE.md` remains the concise project-navigation layer. Individual checkpoints preserve full run-level provenance. This ledger keeps the current experiment state, retained-run resource summaries, exceptional attempts, and the next frozen slot in one place.

No H1/H2 S1-S10 or SC1-SC2 semantic judging has begun.

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

## Current counts

```text
resolved treatment slots: 9 / 30
remaining treatment slots: 21 / 30
behavior-evaluable retained attempts: 9
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

H1 replicate 3 is fully resolved across P0, B0, and B1.

## Mechanically verified retained runs

| Variant | Replicate | Condition | Retained attempt | Completed | Budget exhausted | Model calls | Python | Total tokens | A0-A4 |
|---|---:|---|---|---|---|---:|---:|---:|---|
| H1 | 1 | B0 | `h1-r01-b0-a01` | yes | no | 15 | 5 | 108,891 | PASS |
| H1 | 1 | B1 | `h1-r01-b1-a01` | yes | no | 14 | 6 | 120,424 | PASS |
| H1 | 1 | P0 | `h1-r01-p0-a01` | yes | yes | 14 | 6 | 294,267 | PASS |
| H1 | 2 | B1 | `h1-r02-b1-a01` | yes | no | 15 | 7 | 139,150 | PASS |
| H1 | 2 | P0 | `h1-r02-p0-a01` | yes | no | 12 | 5 | 226,926 | PASS |
| H1 | 2 | B0 | `h1-r02-b0-a03` | yes | no | 16 | 7 | 131,563 | PASS |
| H1 | 3 | P0 | `h1-r03-p0-a01` | no | yes | 13 | 6 | 258,485 | PASS |
| H1 | 3 | B0 | `h1-r03-b0-a01` | yes | no | 14 | 6 | 108,508 | PASS |
| H1 | 3 | B1 | `h1-r03-b1-a01` | yes | no | 16 | 5 | 113,234 | PASS |

The table is mechanical execution evidence only and must not be used as an unblinded semantic condition comparison.

## Notable attempt-level events

### H1 R2 B0 provider/interface replacements

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

The first two failures occurred before a usable treatment command entered the runtime. Frozen replacement semantics therefore applied. The retained A03 trajectory included one model-authored Phase 1 Python timeout followed by a successful computational rewrite; that timeout is behavioral evidence, not provider failure.

Detailed records:

```text
docs/checkpoints/066_h1_r02_b0_a02_provider_ambiguity_verified_and_final_replacement_authorized.md
docs/checkpoints/068_h1_r02_b0_a03_full_mechanical_verification.md
```

### H1 R3 B0 administrative pre-provider interruption

A local `run-next` invocation failed during OpenAI client construction because `OPENAI_API_KEY` was absent in a newly opened terminal. Only `attempt_started.json` had been written and no provider inference occurred.

The false-start directory was moved outside the active treatment ledger. The genuine `h1-r03-b0-a01` was then launched and retained without consuming a replacement attempt.

Detailed record:

```text
docs/checkpoints/071_h1_r03_b0_pre_provider_interruption_recovery_and_relaunch_authorization.md
```

## H1 replicate 3 mechanical summaries

### P0: `h1-r03-p0-a01`

The run crossed the 250,000-token ceiling on the legitimately admitted protected final-evaluation call. It reached protected final evidence but did not receive a later final-report call.

```text
completed: false
budget_exhausted: true
model calls: 13
Python attempts: 6
total tokens: 258,485
A0-A4: PASS
```

Detailed record:

```text
docs/checkpoints/070_h1_r03_p0_full_mechanical_verification_and_second_budget_exhaustion.md
```

### B0: `h1-r03-b0-a01`

```text
completed: true
budget_exhausted: false
model calls: 14
Python attempts: 6
total tokens: 108,508
A0-A4: PASS
```

The final legal six-feature model excluded `lifecycle_flag`; protected test access occurred only after final lock and the final report was present.

Detailed record:

```text
docs/checkpoints/073_h1_r03_b0_full_mechanical_verification.md
```

### B1: `h1-r03-b1-a01`

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 16
generation attempts: 16
generation failures: 0
Python attempts: 5
input tokens: 105,787
output tokens: 7,447
total tokens: 113,234
A0-A4: PASS
critical failures: none
```

All 16 provider generations completed with one distinct structured-output block each, no retries, and no generation errors. All five Python executions returned code 0 with no timeout or stderr failure.

The trace followed:

```text
artifact/document inspection
-> temporal/repeated-member inspection
-> Phase 1 chronological development
-> Phase 1 complete
-> authoritative lifecycle_flag timing notice
-> lifecycle-free Phase 2 redevelopment
-> future development validation
-> final model lock
-> one protected final evaluation
-> final report
```

Phase 1 provisionally used `lifecycle_flag`. Phase 2 removed it after the authoritative notice and regenerated development evidence.

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
n: 5,375
positives: 572
AUROC: 0.6833
log loss: 0.3142
Brier: 0.0889
AUROC bootstrap 95% interval: [0.6601, 0.7059]
```

The only value-level `test.csv` access occurred at trace sequence 33 after final lock at sequence 30 and final-evaluation authorization at sequence 31. No development followed protected-test feedback.

Protected H1 test evidence:

```text
n: 4,126
positives: 460
prevalence: 0.1115
AUROC: 0.6963
log loss: 0.3246
Brier: 0.0935
mean prediction: 0.1030
AUROC bootstrap 95% interval: [0.6718, 0.7211]
```

All three milestone reports are present.

Detailed record:

```text
docs/checkpoints/078_h1_r03_b1_full_mechanical_verification.md
```

## Preregistered P0 resource consequence

P0 budget-exhausted retained runs currently equal two:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria permit no more than one P0 budget-exhausted run. That specific criterion can no longer be satisfied regardless of later outcomes.

This is an objective resource-envelope result, not a semantic or overall architectural verdict. The frozen experiment continues so the remaining reliability, semantic quality, repair precision, completion, false-blocking, and comparative-resource questions can be evaluated without selective stopping.

## Next frozen slot

The next preregistered treatment slot is:

```text
variant: H1
replicate: 4
condition: B0
slot: h1-r04-b0
attempt: h1-r04-b0-a01
```

Exactly one next `run-next` invocation may be authorized at a time. After its executor result, stop again for classification before any later slot.

For exact current authorization, consult `docs/CURRENT_STATE.md`.
