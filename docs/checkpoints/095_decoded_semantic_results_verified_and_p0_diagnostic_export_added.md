# Checkpoint 95: Decoded Semantic Results Verified and P0 Diagnostic Export Added

**Date:** 2026-08-19  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: Decoded Semantic Results Verified and P0 Diagnostic Export Added.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the first condition-level semantic result after the preregistered blinded evidence was frozen, independently verify the uploaded decoded export, and define the remaining architecture-specific diagnostic stage required before final Prototype V0 classification.

## Frozen boundary preserved

The decoded export reports the same blinded semantic aggregate that was frozen before condition identity was revealed:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

Its predecode verification records:

```text
prepared cases: 30 / 30
logical passes: 60 / 60
completed cases: 30 / 30
manual-adjudication cases: 0
provider attempts: 60
private decoder read during verification: no
```

The decoder read the condition mapping only after this frozen boundary had been re-established.

## Independent decoded-export verification

The uploaded archive contains exactly:

```text
decoded_results.json
decoded_run_table.csv
```

Independent inspection confirmed:

```text
run rows: 30
B0 rows: 10
B1 rows: 10
P0 rows: 10
H1 per condition: 5
H2 per condition: 5
CSV rows: 30
CSV scalar fields disagreeing with decoded JSON: 0
```

Pooled summaries and registered comparison facts were recomputed from the run rows and agree with the decoded result.

## Primary pooled semantic result

| Condition | Targeted architecture mean | Strong targeted pass | Critical-failure runs |
|---|---:|---:|---:|
| B0 | 1.47 | 0 / 10 | 0 / 10 |
| B1 | 1.73 | 0 / 10 | 0 / 10 |
| P0 | 1.78 | 0 / 10 | 0 / 10 |

Therefore:

```text
P0 - B1 targeted mean difference: +0.05
strong-targeted-pass difference: 0
critical-failure-event difference: 0
```

The preregistered material-reliability criterion is not met:

```text
A: at least two fewer P0 critical failures than B1
observed: false

B: P0 targeted mean at least +0.30 over B1 AND at least two more strong passes
observed: +0.05 and 0 more strong passes
=> false
```

## Criterion-level pooled means

| Criterion | B0 | B1 | P0 | P0 - B1 |
|---|---:|---:|---:|---:|
| S1 | 1.00 | 1.00 | 1.00 | 0.00 |
| S2 | 1.15 | 1.90 | 1.90 | 0.00 |
| S3 | 1.25 | 1.80 | 2.00 | +0.20 |
| S4 | 1.05 | 1.05 | 1.00 | -0.05 |
| S5 | 2.00 | 2.00 | 2.00 | 0.00 |
| S6 | 2.00 | 2.00 | 2.00 | 0.00 |
| S7 | 1.95 | 1.95 | 2.00 | +0.05 |
| S8 | 1.95 | 2.00 | 1.95 | -0.05 |
| S9 | 1.25 | 2.00 | 1.95 | -0.05 |
| S10 | 2.00 | 2.00 | 1.70 | -0.30 |

The most visible structured-P0 semantic gain is S3 inherited-preprocessing diagnosis, where P0 reaches 2.00 versus B1 1.80. B1 had already captured most of the gain over B0. P0 does not improve S1, S2, S5, or S6 relative to B1 and loses ground on final-task completion-related S10 because four P0 runs never produced final reports.

## Variant robustness

Targeted architecture means:

```text
H1:
B0 1.44
B1 1.70
P0 1.76
P0 - B1 = +0.06

H2:
B0 1.50
B1 1.76
P0 1.80
P0 - B1 = +0.04
```

Thus the cross-variant floor passes because P0 is not more than 0.10 below B1 on either variant. The semantic gain over B1 is nevertheless small on both variants and far below the registered +0.30 reliability alternative.

Paired replicate-level P0 minus B1 targeted differences are:

```text
H1: +0.10, 0.00, 0.00, 0.00, +0.20
H2:  0.00, +0.20, 0.00, 0.00, 0.00
```

No paired replicate shows P0 semantically worse than B1 on the targeted score, but seven of ten pairs are exact ties and the three gains are small.

## Resource and completion result remains decisive

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

The structured treatment therefore used fewer successful calls but dramatically more tokens per trajectory. The continuation criterion fails independently on material reliability, completion, budget exhaustion, and token cost.

## Current interpretation boundary

The common semantic/mechanical evidence is now sufficient to conclude:

```text
Prototype V0 does not provide the preregistered continuation signal for P0.
```

It is not yet sufficient to select the final preregistered classification between:

```text
strong falsification

and

inconclusive / no demonstrated continuation signal
```

because Foundation 012 also requires explicit post-unblinding review of P0-internal architecture-specific clauses:

```text
critical architecture-induced false blocking or over-invalidation;
noncritical architecture-induced false blocking or unnecessary broad reopening;
held-out-case-specific hard coding.
```

The resource-trigger part of the final strong-falsification clause is already present because P0 median tokens are at least 1.25 times B1. Whether the registered reliability-match-or-exceed wording is satisfied must be interpreted together with the full reliability evidence rather than silently equated to one scalar score.

## P0 architecture diagnostic export

A read-only post-unblinding exporter has been added:

```text
prototype_v0/src/ads_v0/p0_architecture_diagnostic_export.py
prototype_v0/tests/test_p0_architecture_diagnostic_export.py
```

It selects exactly the ten retained decoded P0 trajectories and exports, for each:

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

It also records compact structural diagnostics such as:

```text
P0 state-control error events;
blocked ACTION-object counts;
reopened and invalidated transitions;
repair-priority objects;
support-reassessment objects;
knowledge activations and reopen counts;
state relation/type/status counts.
```

The exporter:

```text
launches no model calls;
mutates no attempt evidence;
includes no B0/B1 trajectory;
includes no semantic private decoder;
does not itself decide the final architecture classification.
```

The raw P0 conversation is included because determining whether a controller block was false or justified can require seeing the proposed state patch, command, rationale, visible state, and subsequent recovery rather than counting blocked events mechanically.

## Source-level hard-coding precheck

A repository search for held-out surface identifiers such as:

```text
member_key
account_ref
lifecycle_flag
profile_code
held_out_h1
held_out_h2
churn_v0_h1
churn_v0_h2
```

did not find them in the P0 treatment implementation. The frozen P0 controller instead operates through generic state types, tags, relations, knowledge components, project artifacts, and evidence-triggered state synchronization.

This is useful source-level evidence against literal H1/H2 hard coding, but final assessment remains part of the architecture-diagnostic review.

## Promotion audit

No new system-level foundation is required at this checkpoint. The result is specific to Prototype V0 and belongs in the experiment ledger and checkpoint history.

The broader system principle remains unchanged: explicit mechanisms must earn their complexity empirically, and failure to demonstrate value should cause simplification rather than architectural escalation.

## Next step

Run the deterministic diagnostic-export validation and create the P0-only export:

```bash
pytest
python -m ads_v0.p0_architecture_diagnostic_export verify
python -m ads_v0.p0_architecture_diagnostic_export export
```

Then review the resulting:

```text
p0_architecture_diagnostics_<timestamp>.zip
```

against the remaining Foundation 012 architecture-specific falsification clauses before issuing the final Prototype V0 classification.
