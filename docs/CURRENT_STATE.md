# Current State

**Checkpoint:** 95  
**Date:** 2026-08-19  
**Development stage:** Prototype V0 treatment and semantic inference complete; blinded consensus frozen; condition decoding complete; P0 architecture-specific diagnostics pending  
**Resolved treatment slots:** 30 / 30  
**Semantic logical passes:** 60 / 60  
**Completed semantic cases:** 30 / 30  
**Manual adjudication required:** 0 / 30  
**Execution mode:** no further treatment or semantic-judge inference is authorized for Prototype V0

## Current experiment

Prototype V0 asks:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 is the primary architectural control.

Frozen protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Detailed held-out ledger:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## Fixed treatment evidence

Held-out treatment execution is complete:

```text
resolved treatment slots: 30 / 30
behavior-evaluable retained attempts: 30
B0 retained runs: 10
B1 retained runs: 10
P0 retained runs: 10
non-behavior-evaluable provider/interface attempts: 4
mechanical integrity PASS: 34
mechanical integrity FAIL: 0
```

Pooled mechanical outcomes:

| Condition | Completed within budget | Budget exhausted | Median tokens | Median calls | Median Python |
|---|---:|---:|---:|---:|---:|
| B0 | 10 / 10 | 0 / 10 | 122,544.5 | 16 | 6 |
| B1 | 10 / 10 | 0 / 10 | 120,564.5 | 16 | 6 |
| P0 | 3 / 10 | 7 / 10 | 260,370.0 | 13 | 5 |

P0/B1 median ratios:

```text
total tokens: 2.160
model calls: 0.813
Python attempts: 0.833
```

## Fixed and frozen semantic evidence

The preregistered two-pass judge completed:

```text
provider calls: 60
logical passes: 60 / 60
completed cases: 30 / 30
provider failures: 0
manual-adjudication cases: 0
```

Two-pass agreement:

```text
ordinary comparisons: 300
exact: 288 / 300 = 96.0%
adjacent: 12 / 300 = 4.0%
0-vs-2: 0
SC comparisons: 60 / 60 exact
SC1 consensus flags: 0 / 30
SC2 consensus flags: 0 / 30
```

Frozen blinded semantic aggregate SHA-256:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

The decoder-free frozen ZIP was independently verified with zero file-hash mismatches and an exact aggregate recomputation before unblinding.

## Condition decoding complete

The deterministic decoder re-established the frozen boundary before reading the private condition mapping and produced 30 decoded run rows:

```text
B0: 10
B1: 10
P0: 10
H1: 5 per condition
H2: 5 per condition
```

The uploaded decoded ZIP was independently checked. Its CSV and JSON representations agree on all shared scalar fields, and pooled/variant summaries reproduce from the run-level rows.

### Primary pooled semantic result

| Condition | Targeted architecture mean | Strong targeted pass | Critical-failure runs |
|---|---:|---:|---:|
| B0 | 1.47 | 0 / 10 | 0 / 10 |
| B1 | 1.73 | 0 / 10 | 0 / 10 |
| P0 | 1.78 | 0 / 10 | 0 / 10 |

Primary P0 versus B1 facts:

```text
P0 - B1 targeted mean: +0.05
strong-targeted-pass difference: 0
critical-failure-event difference: 0
```

The preregistered material-reliability improvement is therefore not met.

Criterion-level P0 minus B1 pooled differences:

```text
S1   0.00
S2   0.00
S3  +0.20
S4  -0.05
S5   0.00
S6   0.00
S7  +0.05
S8  -0.05
S9  -0.05
S10 -0.30
```

P0's clearest semantic gain is explicit inherited-preprocessing diagnosis (S3). B1 already captures most of the semantic improvement over B0. P0 does not materially improve the broader targeted reliability vector over B1.

### Cross-variant result

```text
H1 targeted means:
B0 1.44
B1 1.70
P0 1.76
P0 - B1 = +0.06

H2 targeted means:
B0 1.50
B1 1.76
P0 1.80
P0 - B1 = +0.04
```

Cross-variant robustness passes, but the gains over B1 are small on both variants.

Paired P0 minus B1 targeted differences:

```text
H1: +0.10, 0.00, 0.00, 0.00, +0.20
H2:  0.00, +0.20, 0.00, 0.00, 0.00
```

Seven of ten paired comparisons are exact ties.

## Continuation status

The preregistered continuation signal is definitively absent. P0 fails multiple mandatory components:

```text
material reliability improvement: fail
completion: fail
acceptable resource cost: fail
budget-exhaustion limit: fail
```

P0 does pass:

```text
critical failures not worse than B1
cross-variant targeted-score floor
```

Therefore Prototype V0 does not justify continuing the current structured P0 architecture under the preregistered criterion.

## Final classification still pending

Foundation 012 distinguishes between:

```text
strong falsification

and

inconclusive / no demonstrated continuation signal
```

The common semantic/mechanical evidence does not by itself resolve every strong-falsification clause. The remaining P0-internal architecture-specific questions are:

```text
critical architecture-induced false blocking or over-invalidation;
noncritical architecture-induced false blocking or unnecessary broad reopening;
held-out-case-specific hard coding.
```

The resource side of the final B1-versus-P0 strong-falsification clause is already triggered because P0 median tokens are 2.160 times B1. The reliability-match-or-exceed part requires final interpretation of the complete reliability evidence rather than silently treating one scalar as definitive.

## P0 architecture diagnostic export

A read-only diagnostic exporter is implemented:

```text
prototype_v0/src/ads_v0/p0_architecture_diagnostic_export.py
prototype_v0/tests/test_p0_architecture_diagnostic_export.py
```

It selects exactly the ten retained P0 trajectories and exports:

```text
attempt_started.json
attempt_record.json
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
trace.jsonl
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

It also records deterministic structural counts for state-control errors, blocked actions, reopening/invalidation, repair-priority objects, support reassessment, knowledge activation, and relations.

The export launches no model calls, mutates no experiment evidence, includes no B0/B1 trajectory, and does not include the semantic private decoder.

Detailed decoded-result record:

```text
docs/checkpoints/095_decoded_semantic_results_verified_and_p0_diagnostic_export_added.md
```

## Execution and observability architecture

The system-level principle remains:

```text
execution / reasoning
    -> persisted structured state or events
    -> read-only observability
    -> human interface
```

Canonical source:

```text
docs/PRINCIPLES.md, P-022
```

Deep rationale:

```text
docs/foundations/016_execution_observability_separation.md
```

## Next step

Pull the latest diagnostic exporter and run from `prototype_v0/`:

```bash
git pull origin main
pytest
python -m ads_v0.p0_architecture_diagnostic_export verify
python -m ads_v0.p0_architecture_diagnostic_export export
```

Upload the resulting:

```text
p0_architecture_diagnostics_<timestamp>.zip
```

Then inspect the ten P0 trajectories against the remaining architecture-specific clauses and issue the final Prototype V0 classification and architectural decision.

## Current priority

**Validate and export the retained P0 internal diagnostics. No further treatment or semantic-judge inference is allowed.**
