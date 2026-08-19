# Prototype V0 Held-Out Status

**Status:** Complete  
**Final classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Experiment authority:** Descriptive execution ledger. Frozen experimental rules remain governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.  
**Last reviewed:** 2026-08-19  
**Resolved treatment slots:** 30 / 30  
**Remaining treatment slots:** 0 / 30  
**Execution mode:** closed; no further V0 treatment or semantic-judge inference authorized

## Purpose

This file is the compact final execution ledger for the preregistered Prototype V0 held-out experiment.

The complete interpretation is in:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Detailed chronological provenance remains in `docs/checkpoints/`.

## Frozen experiment

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0: 10 retained runs
B1: 10 retained runs
P0: 10 retained runs
30 retained treatment trajectories total

provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed treatment tokens: 250,000
max Python attempts: 12
```

Frozen bundle identities:

```text
H1 seed 811
SHA-256 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed 1601
SHA-256 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

## Treatment execution

Final counts:

```text
resolved preregistered slots: 30 / 30
behavior-evaluable retained trajectories: 30
non-behavior-evaluable provider/interface attempts: 4
mechanically verified attempt directories: 34
mechanical integrity PASS: 34
mechanical integrity FAIL: 0
administrative pre-provider interruptions: 1
```

Provider-failure attempts replaced under the frozen policy:

```text
h1-r02-b0-a01
h1-r02-b0-a02
h2-r05-b0-a01
h2-r05-b0-a02
```

Both affected B0 slots resolved on attempt `a03`.

All 30 retained trajectories passed the registered deterministic A0-A4 layer.

## Retained mechanical table

| Variant | Replicate | Condition | Retained attempt | Completed | Budget exhausted | Calls | Python | Tokens |
|---|---:|---|---|---|---|---:|---:|---:|
| H1 | 1 | B0 | `h1-r01-b0-a01` | yes | no | 15 | 5 | 108,891 |
| H1 | 1 | B1 | `h1-r01-b1-a01` | yes | no | 14 | 6 | 120,424 |
| H1 | 1 | P0 | `h1-r01-p0-a01` | yes | yes | 14 | 6 | 294,267 |
| H1 | 2 | B1 | `h1-r02-b1-a01` | yes | no | 15 | 7 | 139,150 |
| H1 | 2 | P0 | `h1-r02-p0-a01` | yes | no | 12 | 5 | 226,926 |
| H1 | 2 | B0 | `h1-r02-b0-a03` | yes | no | 16 | 7 | 131,563 |
| H1 | 3 | P0 | `h1-r03-p0-a01` | no | yes | 13 | 6 | 258,485 |
| H1 | 3 | B0 | `h1-r03-b0-a01` | yes | no | 14 | 6 | 108,508 |
| H1 | 3 | B1 | `h1-r03-b1-a01` | yes | no | 16 | 5 | 113,234 |
| H1 | 4 | B0 | `h1-r04-b0-a01` | yes | no | 16 | 6 | 131,266 |
| H1 | 4 | B1 | `h1-r04-b1-a01` | yes | no | 16 | 6 | 152,391 |
| H1 | 4 | P0 | `h1-r04-p0-a01` | no | yes | 14 | 5 | 262,255 |
| H1 | 5 | B1 | `h1-r05-b1-a01` | yes | no | 17 | 7 | 155,299 |
| H1 | 5 | P0 | `h1-r05-p0-a01` | no | yes | 14 | 5 | 257,290 |
| H1 | 5 | B0 | `h1-r05-b0-a01` | yes | no | 14 | 6 | 123,055 |
| H2 | 1 | P0 | `h2-r01-p0-a01` | yes | no | 13 | 4 | 240,025 |
| H2 | 1 | B0 | `h2-r01-b0-a01` | yes | no | 16 | 6 | 122,034 |
| H2 | 1 | B1 | `h2-r01-b1-a01` | yes | no | 13 | 5 | 107,134 |
| H2 | 2 | B0 | `h2-r02-b0-a01` | yes | no | 16 | 5 | 116,745 |
| H2 | 2 | B1 | `h2-r02-b1-a01` | yes | no | 16 | 6 | 114,529 |
| H2 | 2 | P0 | `h2-r02-p0-a01` | no | yes | 14 | 5 | 269,711 |
| H2 | 3 | B1 | `h2-r03-b1-a01` | yes | no | 15 | 4 | 119,011 |
| H2 | 3 | P0 | `h2-r03-p0-a01` | yes | yes | 13 | 6 | 285,470 |
| H2 | 3 | B0 | `h2-r03-b0-a01` | yes | no | 17 | 6 | 143,832 |
| H2 | 4 | P0 | `h2-r04-p0-a01` | yes | yes | 13 | 4 | 267,296 |
| H2 | 4 | B0 | `h2-r04-b0-a01` | yes | no | 16 | 6 | 112,263 |
| H2 | 4 | B1 | `h2-r04-b1-a01` | yes | no | 16 | 6 | 120,705 |
| H2 | 5 | B0 | `h2-r05-b0-a03` | yes | no | 18 | 8 | 157,554 |
| H2 | 5 | B1 | `h2-r05-b1-a01` | yes | no | 16 | 8 | 142,948 |
| H2 | 5 | P0 | `h2-r05-p0-a01` | yes | no | 12 | 4 | 228,549 |

## Pooled resource/completion summary

| Condition | Completed | Within budget | Budget exhausted | Final reports | Median tokens | Median calls | Median Python |
|---|---:|---:|---:|---:|---:|---:|---:|
| B0 | 10 / 10 | 10 / 10 | 0 / 10 | 10 / 10 | 122,544.5 | 16 | 6 |
| B1 | 10 / 10 | 10 / 10 | 0 / 10 | 10 / 10 | 120,564.5 | 16 | 6 |
| P0 | 6 / 10 | 3 / 10 | 7 / 10 | 6 / 10 | 260,370.0 | 13 | 5 |

P0/B1 median ratios:

```text
total tokens: 2.160
model calls: 0.813
Python attempts: 0.833
```

## Blinded semantic evaluation

The registered two-pass judge completed after all treatment trajectories were fixed:

```text
prepared blinded cases: 30 / 30
logical judge passes: 60 / 60
provider calls: 60
provider failures: 0
manual-adjudication cases: 0
```

Two-pass agreement:

```text
S1-S10 comparisons: 300
exact: 288 / 300 = 96.0%
adjacent: 12 / 300 = 4.0%
0-vs-2: 0

SC comparisons: 60
exact: 60 / 60
SC1 consensus flags: 0 / 30
SC2 consensus flags: 0 / 30
```

The complete condition-blind evidence was frozen before unblinding.

Frozen aggregate SHA-256:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

The decoder-free freeze export was independently checked against its manifest with zero SHA-256 mismatches before condition decoding.

## Decoded semantic result

| Criterion | B0 | B1 | P0 |
|---|---:|---:|---:|
| S1 | 1.00 | 1.00 | 1.00 |
| S2 | 1.15 | 1.90 | 1.90 |
| S3 | 1.25 | 1.80 | 2.00 |
| S4 | 1.05 | 1.05 | 1.00 |
| S5 | 2.00 | 2.00 | 2.00 |
| S6 | 2.00 | 2.00 | 2.00 |
| S7 | 1.95 | 1.95 | 2.00 |
| S8 | 1.95 | 2.00 | 1.95 |
| S9 | 1.25 | 2.00 | 1.95 |
| S10 | 2.00 | 2.00 | 1.70 |

Targeted score:

```text
B0: 1.47
B1: 1.73
P0: 1.78
```

Strong targeted passes:

```text
B0: 0 / 10
B1: 0 / 10
P0: 0 / 10
```

Critical failure runs:

```text
B0: 0 / 10
B1: 0 / 10
P0: 0 / 10
```

Variant-specific targeted means:

```text
H1: B0 1.44, B1 1.70, P0 1.76
H2: B0 1.50, B1 1.76, P0 1.80
```

P0 minus B1 paired differences:

```text
H1: +0.10, 0.00, 0.00, 0.00, +0.20
H2:  0.00, +0.20, 0.00, 0.00, 0.00
```

## P0 architecture diagnostics

The ten retained P0 internal trajectories were reviewed after unblinding.

Aggregate structural counts:

```text
state objects: 506
relations: 483
invalidated transitions: 14
reopened transitions: 24
repair-priority objects: 32
support-reassessment objects: 30
knowledge reopens: 2
state-control errors: 0
blocked ACTION objects: 0
Python-budget blocks: 0
```

Findings:

```text
false action blocking: none observed
critical over-invalidation: none observed
held-out-specific hard coding: none found
repair invalidations: materially scoped to the post-outcome feature and dependent evidence
knowledge activation: K-INFO-003 activated in 8/10, exposing path-sensitive trigger brittleness
support reassessment: avoidable internal obligation churn observed
broad reopening: one latent noncritical H2 R4 over-propagation artifact, immediately re-resolved without extra external analysis
```

The registered architecture-friction threshold was not exceeded.

## Preregistered decision

Continuation requires all mandatory components to pass.

Observed:

```text
critical failures not worse than B1: PASS
material reliability improvement: FAIL
cross-variant robustness: PASS
completion: FAIL
resource cost: FAIL
architecture-induced friction: PASS
```

Therefore there is no continuation signal.

Foundation 012 also preregistered strong falsification when B1 matches or exceeds P0 reliability while P0 median tokens or calls are at least 25% higher.

B1 and P0 have identical critical-failure counts and strong-targeted-pass counts. P0's targeted-score advantage is only `+0.05`, far below the registered material improvement threshold of `+0.30` plus a strong-pass gain.

P0 median tokens are `2.160x` B1.

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

## Provenance

Key records:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
docs/checkpoints/090_blinded_semantic_judge_execution_complete.md
docs/checkpoints/093_blinded_semantic_freeze_independently_verified_and_unblinding_authorized.md
docs/checkpoints/095_decoded_semantic_results_verified_and_p0_diagnostic_export_added.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Prototype V0 is now immutable experimental evidence. Future architecture work should use it as a constraint rather than tune the completed treatment against this benchmark.
