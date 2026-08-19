# Prototype V0 Held-Out Status

**Status:** Held-out treatment execution complete; blinded semantic consensus frozen; condition decoding pending  
**Experiment authority:** Descriptive execution status only. Frozen experimental rules remain governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.  
**Last reviewed:** 2026-08-19  
**Resolved treatment slots:** 30 / 30  
**Remaining treatment slots:** 0 / 30  
**Next frozen treatment slot:** none  
**Execution mode:** treatment and judge inference complete; post-freeze deterministic decoding pending

## Purpose

This file is the consolidated execution ledger for the preregistered Prototype V0 held-out experiment.

`docs/CURRENT_STATE.md` remains the concise project-navigation layer. Individual checkpoints preserve detailed provenance. This ledger records current counts, retained-run resource summaries, exceptional attempt mechanics, semantic-judge completion, the blinded freeze identity, and the transition to decoded condition comparison.

No further B0/B1/P0 treatment call or semantic-judge call is authorized for Prototype V0.

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

## Final treatment-execution counts

```text
resolved treatment slots: 30 / 30
remaining treatment slots: 0 / 30
behavior-evaluable retained attempts: 30
B0 retained runs: 10
B1 retained runs: 10
P0 retained runs: 10
non-behavior-evaluable provider/interface attempts: 4
replacement attempts launched: 4
administrative pre-provider interruptions: 1
completed attempt directories mechanically verified: 34
mechanical verification integrity PASS: 34
mechanical verification integrity FAIL: 0
```

The four non-behavior-evaluable provider/interface attempts were:

```text
h1-r02-b0-a01
h1-r02-b0-a02
h2-r05-b0-a01
h2-r05-b0-a02
```

Both affected B0 slots resolved on `a03` under the frozen replacement policy.

## Final retained-run table

| Variant | Replicate | Condition | Retained attempt | Completed | Budget exhausted | Model calls | Python | Total tokens | A0-A4 |
|---|---:|---|---|---|---|---:|---:|---:|---|
| H1 | 1 | B0 | `h1-r01-b0-a01` | yes | no | 15 | 5 | 108,891 | PASS |
| H1 | 1 | B1 | `h1-r01-b1-a01` | yes | no | 14 | 6 | 120,424 | PASS |
| H1 | 1 | P0 | `h1-r01-p0-a01` | yes | yes | 14 | 6 | 294,267 | PASS |
| H1 | 2 | B0 | `h1-r02-b0-a03` | yes | no | 16 | 7 | 131,563 | PASS |
| H1 | 2 | B1 | `h1-r02-b1-a01` | yes | no | 15 | 7 | 139,150 | PASS |
| H1 | 2 | P0 | `h1-r02-p0-a01` | yes | no | 12 | 5 | 226,926 | PASS |
| H1 | 3 | B0 | `h1-r03-b0-a01` | yes | no | 14 | 6 | 108,508 | PASS |
| H1 | 3 | B1 | `h1-r03-b1-a01` | yes | no | 16 | 5 | 113,234 | PASS |
| H1 | 3 | P0 | `h1-r03-p0-a01` | no | yes | 13 | 6 | 258,485 | PASS |
| H1 | 4 | B0 | `h1-r04-b0-a01` | yes | no | 16 | 6 | 131,266 | PASS |
| H1 | 4 | B1 | `h1-r04-b1-a01` | yes | no | 16 | 6 | 152,391 | PASS |
| H1 | 4 | P0 | `h1-r04-p0-a01` | no | yes | 14 | 5 | 262,255 | PASS |
| H1 | 5 | B0 | `h1-r05-b0-a01` | yes | no | 14 | 6 | 123,055 | PASS |
| H1 | 5 | B1 | `h1-r05-b1-a01` | yes | no | 17 | 7 | 155,299 | PASS |
| H1 | 5 | P0 | `h1-r05-p0-a01` | no | yes | 14 | 5 | 257,290 | PASS |
| H2 | 1 | B0 | `h2-r01-b0-a01` | yes | no | 16 | 6 | 122,034 | PASS |
| H2 | 1 | B1 | `h2-r01-b1-a01` | yes | no | 13 | 5 | 107,134 | PASS |
| H2 | 1 | P0 | `h2-r01-p0-a01` | yes | no | 13 | 4 | 240,025 | PASS |
| H2 | 2 | B0 | `h2-r02-b0-a01` | yes | no | 16 | 5 | 116,745 | PASS |
| H2 | 2 | B1 | `h2-r02-b1-a01` | yes | no | 16 | 6 | 114,529 | PASS |
| H2 | 2 | P0 | `h2-r02-p0-a01` | no | yes | 14 | 5 | 269,711 | PASS |
| H2 | 3 | B0 | `h2-r03-b0-a01` | yes | no | 17 | 6 | 143,832 | PASS |
| H2 | 3 | B1 | `h2-r03-b1-a01` | yes | no | 15 | 4 | 119,011 | PASS |
| H2 | 3 | P0 | `h2-r03-p0-a01` | yes | yes | 13 | 6 | 285,470 | PASS |
| H2 | 4 | B0 | `h2-r04-b0-a01` | yes | no | 16 | 6 | 112,263 | PASS |
| H2 | 4 | B1 | `h2-r04-b1-a01` | yes | no | 16 | 6 | 120,705 | PASS |
| H2 | 4 | P0 | `h2-r04-p0-a01` | yes | yes | 13 | 4 | 267,296 | PASS |
| H2 | 5 | B0 | `h2-r05-b0-a03` | yes | no | 18 | 8 | 157,554 | PASS |
| H2 | 5 | B1 | `h2-r05-b1-a01` | yes | no | 16 | 8 | 142,948 | PASS |
| H2 | 5 | P0 | `h2-r05-p0-a01` | yes | no | 12 | 4 | 228,549 | PASS |

All 30 retained behavior-evaluable trajectories pass the registered deterministic A0-A4 layer according to the final compact mechanical-verification export.

## Pooled resource and completion summary

| Condition | Completed | Completed within budget | Budget exhausted | Final reports | Median total tokens | Median model calls | Median Python attempts |
|---|---:|---:|---:|---:|---:|---:|---:|
| B0 | 10 / 10 | 10 / 10 | 0 / 10 | 10 / 10 | 122,544.5 | 16 | 6 |
| B1 | 10 / 10 | 10 / 10 | 0 / 10 | 10 / 10 | 120,564.5 | 16 | 6 |
| P0 | 6 / 10 | 3 / 10 | 7 / 10 | 6 / 10 | 260,370.0 | 13 | 5 |

P0/B1 pooled median resource ratios:

```text
total tokens: 2.160
successful model calls: 0.813
Python attempts: 0.833
```

The unusually high P0 token cost despite fewer calls is a central mechanical result to interpret alongside semantic reliability.

## Continuation criterion status from mechanical outcomes

Foundation 012 requires all continuation conditions to hold. Three mechanically observable requirements are already impossible:

```text
required P0 completion within budget: at least 9 / 10
observed: 3 / 10

allowed P0 budget-exhausted runs: at most 1 / 10
observed: 7 / 10

allowed P0/B1 median token ratio: at most 1.50
observed: 2.160
```

Therefore the current P0 design cannot obtain the preregistered V0 continuation signal regardless of S1-S10 outcomes.

The final registered classification still requires decoded semantic reliability plus the P0-specific architecture diagnostic clauses relevant to strong falsification.

## Final unattended treatment batch

Batch:

```text
batch-20260818T212414Z
```

Result:

```text
model attempts launched: 19
behavior-evaluable attempts in batch: 17
non-behavior-evaluable provider failures in batch: 2
stop reason: EXPERIMENT_COMPLETE
resolved treatment slots after batch: 30 / 30
```

The batch started at `h1-r05-p0-a01`, followed the preregistered order, and terminated because no unresolved treatment slot remained.

The two provider failures were both in H2 R5 B0:

```text
h2-r05-b0-a01: NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE
h2-r05-b0-a02: NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE
h2-r05-b0-a03: retained BEHAVIOR_EVALUABLE trajectory
```

This used the full three-attempt allowance for the slot without exceeding it.

Final supervisor snapshot:

```text
status: EXPERIMENT_COMPLETE
resolved slots: 30 / 30
attempts mechanically verified: 34
integrity PASS: 34
integrity FAIL: 0
```

Detailed completion record:

```text
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
```

## Notable behavioral execution events

Model-authored Python execution failures/timeouts remain behavior evidence and were not replaced. Retained runs with at least one such event include:

```text
h1-r02-b0-a03
h1-r04-b0-a01
h1-r05-b1-a01
h2-r01-b0-a01
h2-r03-b0-a01
h2-r05-b1-a01
```

They remain part of the final retained trajectories exactly as executed.

## P0 completion pattern

```text
H1 R1: completed, budget exhausted
H1 R2: completed within budget
H1 R3: incomplete, budget exhausted
H1 R4: incomplete, budget exhausted
H1 R5: incomplete, budget exhausted
H2 R1: completed within budget
H2 R2: incomplete, budget exhausted
H2 R3: completed, budget exhausted
H2 R4: completed, budget exhausted
H2 R5: completed within budget
```

Totals:

```text
completed: 6 / 10
completed within budget: 3 / 10
budget exhausted: 7 / 10
final report present: 6 / 10
```

## Blinded semantic-judge execution

The preregistered two-pass semantic judge completed after all treatment trajectories were fixed.

Observed execution:

```text
semantic batch: semantic-batch-20260819T121018Z
prepared blinded cases: 30 / 30
logical passes persisted: 60 / 60
completed blinded cases: 30 / 30
provider attempts: 60
provider failures: 0
manual-adjudication cases: 0
stop reason: JUDGE_COMPLETE
```

Two-pass agreement across the frozen blinded pool:

```text
ordinary criterion comparisons: 300
exact agreement: 288 / 300 = 96.0%
adjacent disagreements: 12 / 300 = 4.0%
extreme 0-vs-2 disagreements: 0

semantic-critical comparisons: 60
exact agreement: 60 / 60
critical disagreements: 0
SC1 consensus flags: 0 / 30
SC2 consensus flags: 0 / 30
```

The twelve adjacent disagreements were resolved by the already-preregistered arithmetic-mean rule. No manual semantic intervention was required.

Judge resource usage, separate from treatment budgets:

```text
total judge tokens: 1,073,492
mean per pass: approximately 17,891.5
median per pass: 18,668.5
minimum: 12,303
maximum: 23,182
```

Detailed record:

```text
docs/checkpoints/090_blinded_semantic_judge_execution_complete.md
```

## Frozen blinded consensus

The complete blinded semantic evidence was mechanically verified and frozen before condition decoding.

Local freeze validation:

```text
pytest: 95 passed
prepared cases verified: 30 / 30
logical passes verified: 60 / 60
completed cases verified: 30 / 30
manual-adjudication cases: 0
provider attempts: 60
private decoder read: no
```

Frozen aggregate SHA-256:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

The decoder-free frozen ZIP was uploaded and independently checked byte-for-byte against its manifest:

```text
freeze-covered files: 242
file SHA-256 mismatches: 0
recomputed aggregate matches: yes
private decoder present: no
```

Condition-blind aggregate semantic shape at the freeze boundary:

```text
S1 mean: 1.000
S2 mean: 1.650
S3 mean: 1.683
S4 mean: 1.033
S5 mean: 2.000
S6 mean: 2.000
S7 mean: 1.967
S8 mean: 1.967
S9 mean: 1.733
S10 mean: 1.900
blinded targeted-architecture mean: 1.660
strong-targeted-pass cases: 0 / 30
```

Detailed freeze records:

```text
docs/checkpoints/092_blinded_semantic_consensus_freeze_implemented_pending_validation.md
docs/checkpoints/093_blinded_semantic_freeze_independently_verified_and_unblinding_authorized.md
```

## Current post-freeze boundary

The scientific ordering is now:

```text
treatment trajectories fixed
-> deterministic mechanics verified
-> semantic judge completed
-> two-pass consensus completed
-> no manual adjudication required
-> blinded evidence frozen
-> frozen archive independently verified
-> condition decoding authorized
```

The next stage is deterministic condition decoding. The decoder must first re-verify the frozen aggregate without reading the private mapping, then reveal the mapping and compute H1, H2, pooled, and paired B0/B1/P0 comparisons.

After decoded common semantic outcomes are available, P0-specific diagnostics must separately assess the registered architecture-induced false-blocking, over-invalidation/broad-reopening, and held-out-specific hard-coding clauses before the final strong-falsification versus no-demonstrated-continuation classification is recorded.

The primary architectural comparison remains P0 versus B1.