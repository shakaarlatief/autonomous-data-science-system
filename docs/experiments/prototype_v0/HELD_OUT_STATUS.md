# Prototype V0 Held-Out Status

**Status:** Current detailed experiment ledger  
**Experiment authority:** Descriptive execution status only. Frozen experimental rules are governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.  
**Last reviewed:** 2026-08-18  
**Resolved treatment slots:** 10 / 30  
**Next frozen slot:** `h1-r04-b1-a01`  
**Current gate:** validate automated supervisor before any new paid attempt

## Purpose

This file is the consolidated execution ledger for the preregistered Prototype V0 held-out experiment.

`docs/CURRENT_STATE.md` remains the concise project-navigation layer. Individual checkpoints preserve full run-level provenance. This ledger keeps current experiment counts, retained-run resource summaries, exceptional attempt mechanics, and the execution gate in one place.

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
resolved treatment slots: 10 / 30
remaining treatment slots: 20 / 30
behavior-evaluable retained attempts: 10
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
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

This table is mechanical execution evidence only and must not be used as an unblinded semantic condition comparison.

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

The first two failures occurred before a usable treatment command entered the runtime. Frozen replacement semantics applied. The retained A03 trajectory included one model-authored Phase 1 Python timeout followed by a successful computational rewrite; that timeout is behavioral evidence, not provider failure.

Detailed records:

```text
docs/checkpoints/066_h1_r02_b0_a02_provider_ambiguity_verified_and_final_replacement_authorized.md
docs/checkpoints/068_h1_r02_b0_a03_full_mechanical_verification.md
```

### H1 R3 B0 administrative pre-provider interruption

A local `run-next` invocation failed during OpenAI client construction because `OPENAI_API_KEY` was absent in a newly opened terminal. No provider inference occurred. The false-start directory was moved outside the active treatment ledger and the genuine `h1-r03-b0-a01` was later run normally.

Detailed record:

```text
docs/checkpoints/071_h1_r03_b0_pre_provider_interruption_recovery_and_relaunch_authorization.md
```

### H1 R4 B0 model-authored Python recovery

`h1-r04-b0-a01` made six Python attempts. The first inspection script returned code 1 because it accessed `pairs.diff` instead of the created `diff` column. The model corrected the computation on the next attempt. There were no Python timeouts.

Detailed record:

```text
docs/checkpoints/080_h1_r04_b0_full_mechanical_verification.md
```

## Preregistered P0 resource consequence

P0 budget-exhausted retained runs currently equal two:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria permit no more than one P0 budget-exhausted run. That specific condition can no longer be satisfied regardless of later outcomes.

This is an objective resource-envelope result, not a semantic or overall architectural verdict. The remaining frozen experiment continues.

## Automated supervision architecture introduced after slot 10

The first ten slots established that repeated manual transport and mechanical inspection were no longer adding enough value to justify their cost.

New external infrastructure:

```text
prototype_v0/src/ads_v0/heldout_verifier.py
prototype_v0/src/ads_v0/heldout_supervisor.py
```

Detailed design:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

Implementation checkpoint:

```text
docs/checkpoints/081_automated_held_out_supervision_implemented_pending_retroactive_validation.md
```

The new layer does not alter the frozen treatment runner. It automates read-only mechanical verification and bounded sequential calls to the existing `execute_next_attempt()` function.

### Required validation before prospective use

No paid supervisor batch is currently authorized.

First run:

```bash
pytest
python -m ads_v0.heldout_supervisor verify-existing
python -m ads_v0.heldout_supervisor export
```

The full existing ledger, including both H1 R2 B0 non-behavior-evaluable provider attempts, must pass verifier integrity checks. The compact export must then be compared with the manual records already preserved for the first ten resolved slots.

Only after that parity check may the supervisor be frozen for the remaining V0 execution.

## Next frozen slot

The next treatment identity remains unchanged:

```text
variant: H1
replicate: 4
condition: B1
slot: h1-r04-b1
attempt: h1-r04-b1-a01
```

It is currently held behind the no-inference supervisor-validation gate. Do not run `heldout_runner run-next` or a paid supervisor batch until `docs/CURRENT_STATE.md` explicitly authorizes prospective execution.
