# Prototype V0 Held-Out Status

**Status:** Current detailed experiment ledger  
**Experiment authority:** Descriptive execution status only. Frozen experimental rules remain governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.  
**Last reviewed:** 2026-08-18  
**Resolved treatment slots:** 13 / 30  
**Remaining treatment slots:** 17 / 30  
**Next frozen slot:** `h1-r05-p0-a01`  
**Execution mode:** prospectively validated sequential supervisor; large bounded batch authorized

## Purpose

This file is the consolidated execution ledger for the preregistered Prototype V0 held-out experiment.

`docs/CURRENT_STATE.md` remains the concise project-navigation layer. Individual checkpoints preserve detailed provenance. This ledger records current counts, retained-run resource summaries, exceptional attempt mechanics, supervisor status, and the exact next frozen execution point.

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

Replacement policy remains:

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/interface generation failure
=> replacement eligible inside same slot
```

Maximum attempts per slot remain `a01`, `a02`, and `a03`.

## Current counts

```text
resolved treatment slots: 13 / 30
remaining treatment slots: 17 / 30
behavior-evaluable retained attempts: 13
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 3
administrative pre-provider interruptions: 1
completed attempt directories mechanically verified: 15
mechanical integrity failures: 0
```

H1 status:

```text
replicate 1: B0, B1, P0 resolved
replicate 2: B1, P0, B0 resolved
replicate 3: P0, B0, B1 resolved
replicate 4: B0, B1, P0 resolved
replicate 5: B1 resolved; P0 then B0 remain
```

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
| H1 | 4 | B0 | `h1-r04-b0-a01` | yes | no | 16 | 6 | 131,266 | PASS |
| H1 | 4 | B1 | `h1-r04-b1-a01` | yes | no | 16 | 6 | 152,391 | PASS |
| H1 | 4 | P0 | `h1-r04-p0-a01` | no | yes | 14 | 5 | 262,255 | PASS |
| H1 | 5 | B1 | `h1-r05-b1-a01` | yes | no | 17 | 7 | 155,299 | PASS |

This table contains mechanical execution evidence only and must not be used as an unblinded semantic condition comparison.

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
    one model-authored Python timeout
```

The first two failures occurred before a usable treatment command entered the runtime. Frozen replacement semantics applied.

### H1 R3 B0 administrative pre-provider interruption

One local invocation failed before provider inference because `OPENAI_API_KEY` was absent. No treatment attempt was consumed. The genuine `h1-r03-b0-a01` later ran normally.

### H1 R4 B0 model-authored Python recovery

`h1-r04-b0-a01` contained one model-authored Python error followed by successful correction. This remains behavioral evidence, not infrastructure failure.

### H1 R4 P0 third retained budget exhaustion

`h1-r04-p0-a01` was behavior-evaluable and mechanically coherent but exhausted the common token envelope:

```text
completed: false
budget exhausted: true
model calls: 14
Python attempts: 5
total tokens: 262,255
final lock sequence: 32
protected test access: 35
final report: absent
A0-A4: PASS
```

It is permanently retained and not replacement-eligible.

### H1 R5 B1 model-authored Python error

`h1-r05-b1-a01` contained one Python execution with return code 1 at trace sequence 28. The trajectory remained behavior-evaluable, recovered, completed, and passed all mechanical integrity checks.

```text
completed: true
model calls: 17
Python attempts: 7
total tokens: 155,299
final lock sequence: 32
protected test access: 35
final report sequence: 37
A0-A4: PASS
```

## P0 resource consequence

P0 budget-exhausted retained runs now equal three:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
H1 R4 P0: budget exhausted
```

The preregistered continuation criteria permit no more than one P0 budget-exhausted run. That criterion became impossible after H1 R3 and remains impossible regardless of later outcomes.

This is an objective resource-envelope result. It is not a substitute for the later blinded semantic evaluation or overall architectural interpretation.

## Automated supervision architecture

The condition-neutral external supervision layer is:

```text
prototype_v0/src/ads_v0/heldout_verifier.py
prototype_v0/src/ads_v0/heldout_supervisor.py
```

Detailed architecture:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

Validated implementation blob identities:

```text
heldout_supervisor.py
    ef6ffbea671d4f177e41002becfd8751e176ddad

heldout_verifier.py
    03fb33280f87d0056a3dbb264a63651df9ffb431
```

### Retrospective validation

Before prospective paid use:

```text
pytest: 77 passed
completed attempt directories verified: 12
integrity passed: 12
integrity failed: 0
```

Checkpoint:

```text
docs/checkpoints/082_held_out_supervisor_retroactively_validated_and_frozen_for_live_use.md
```

### First prospective batch

Batch command:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 3
```

Batch identity:

```text
batch-20260818T170118Z
```

Result:

```text
model attempts launched: 3
stop reason: MAX_MODEL_ATTEMPTS_REACHED
new attempts:
    h1-r04-b1-a01  BEHAVIOR_EVALUABLE  integrity PASS
    h1-r04-p0-a01  BEHAVIOR_EVALUABLE  integrity PASS
    h1-r05-b1-a01  BEHAVIOR_EVALUABLE  integrity PASS
resolved slots after batch: 13 / 30
next attempt: h1-r05-p0-a01
```

Post-batch verification state:

```text
15 completed attempt directories verified
15 integrity PASS
0 integrity FAIL
```

All M01-M11 checks passed for all three prospective attempts. No replacement or order deviation occurred. The supervisor stopped exactly at the explicit paid-attempt bound.

Detailed record:

```text
docs/checkpoints/083_first_live_supervisor_batch_validated_and_unattended_execution_authorized.md
```

## Supervisor execution semantics

The supervisor:

```text
calls the unchanged frozen execute_next_attempt() path;
runs attempts sequentially only;
mechanically verifies each persisted attempt before advancing;
preserves frozen slot order;
preserves frozen replacement semantics;
does not modify B0/B1/P0;
does not expose previous outcomes to later treatments;
does not perform semantic judging;
does not write inside completed attempt directories;
creates one compact batch export for review.
```

Behavioral issues such as Python errors, deterministic failures, incomplete work, or budget exhaustion remain retained outcomes and do not become replacement reasons.

## Next frozen execution

The next treatment identity is:

```text
variant: H1
replicate: 5
condition: P0
slot: h1-r05-p0
attempt: h1-r05-p0-a01
```

The three-attempt prospective smoke test has passed. A large bounded batch is authorized:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

There are 17 unresolved treatment slots. If all resolve on their first attempts, the supervisor will stop at `EXPERIMENT_COMPLETE` after 17 paid attempts. Provider-failure replacements consume additional allowance. Automatic execution must still stop on verifier integrity failure, interrupted attempt, replacement exhaustion, or another existing runner safety state.

After this batch stops, inspect its single compact export before any semantic judging begins.

Do not separately invoke `heldout_runner run-next` while the supervisor workflow is active.