# Checkpoint 30: Semantic Judge Calibration and P0 Boundary

**Date:** 2026-08-09  
**Status:** Historical mixed checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Prototype V0 held-out protocol and implementation preparation  
**Scope:** Records the historical milestone described by this checkpoint: Semantic Judge Calibration and P0 Boundary.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the final pre-P0 evaluator calibration after the held-out protocol and exact H1/H2 bundles were frozen.

The condition-blinded semantic judge was run twice independently on each of the six already-observed development baseline trajectories:

```text
dev-b0-03
dev-b0-04
dev-b0-05
dev-b1-01
dev-b1-02
dev-b1-03
```

This calibration occurred before any P0 implementation.

## Infrastructure verification

After the semantic-judge infrastructure was added, the full local test suite passed:

```text
34 passed in 8.68s
```

The exact held-out bundles had already been frozen before this judge calibration:

```text
H1 seed: 811
H1 aggregate SHA-256:
7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed: 1601
H2 aggregate SHA-256:
44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Both preregistered starting seeds passed immediately, so no fallback seed search occurred.

## Judge-calibration result

| Run | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | Targeted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dev-b0-03` | 1.0 | 1.5 | 1.0 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 1.5 |
| `dev-b0-04` | 1.0 | 1.0 | 1.0 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 1.4 |
| `dev-b0-05` | 1.0 | 2.0 | 1.0 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 1.6 |
| `dev-b1-01` | 1.0 | 2.0 | 2.0 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 1.8 |
| `dev-b1-02` | 1.0 | 2.0 | 1.0 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 1.6 |
| `dev-b1-03` | 1.0 | 2.0 | 2.0 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 1.8 |

No run required manual adjudication.

## Inter-pass consistency

Across the two fresh judge passes there were 60 ordinary semantic criterion comparisons:

```text
exact criterion agreement: 59 / 60 = 98.3%
adjacent disagreements: 1 / 60
extreme 0-versus-2 disagreements: 0 / 60
```

The only ordinary disagreement was `dev-b0-03` on S2:

```text
pass 1: 1
pass 2: 2
registered consensus: 1.5
```

The disagreement was substantively understandable. One pass treated the deployment mixture as only partially characterized, while the other treated the explicit later-snapshot/repeated-customer reasoning as sufficient for a strong score. The preregistered adjacent-disagreement rule resolves this mechanically without adjudication.

Across the twelve semantic-critical comparisons:

```text
SC1 exact agreement: 6 / 6
SC2 exact agreement: 6 / 6
critical-flag disagreements: 0
all flags: false
```

Therefore the calibration produced no trigger for manual blinded adjudication.

## Agreement with the prior manual semantic review

The automated judge reproduces the most important condition-neutral findings from the full six-run manual review.

Most importantly, inherited learned-preprocessing contamination is scored strongly only when it was explicitly diagnosed:

```text
B0 S3=2: 0 / 3
B1 S3=2: 2 / 3
```

This exactly matches the prior manual finding that B1 improved explicit activation of K-INFO-002 but did not make it perfectly reliable.

The judge also reproduces the broader pattern that:

```text
all six runs repaired the Phase 2 timing change strongly;
all six kept final claims legitimate and bounded;
B1 was more consistently explicit about the deployment/generalization regime;
important semantics could remain operationally correct but insufficiently explicit.
```

## Deliberately stricter rubric effects

The judge assigns S1=1 to all six development trajectories, including `dev-b1-01`.

This is consistent with the preregistered S1 anchor. `dev-b1-01` explicitly stated that rows are monthly customer snapshots, but did not also explicitly retire the stale README one-row-per-customer statement as a durable project conclusion. The earlier manual narrative described this as a strong semantic correction, but Foundation 012 subsequently froze a stricter score-2 requirement before P0 existed.

No rubric change is justified merely to make the automated score match the earlier narrative wording.

Similarly, S4=1 for all six trajectories reflects the registered distinction between defensible provisional feature use and a stronger explicit evidence-qualified feature-availability assumption/question.

These results provide useful headroom for testing whether typed state and activation produce more explicit project semantics rather than merely correct behavior.

## Development targeted-score summary

Descriptively, on the development case:

```text
B0 targeted scores: 1.5, 1.4, 1.6
B0 mean: 1.50

B1 targeted scores: 1.8, 1.6, 1.8
B1 mean: 1.73

development mean difference B1 - B0: approximately +0.23
```

This is calibration evidence only. It is not held-out evidence and must not be compared mechanically with the preregistered +0.30 P0 continuation threshold as if it were a confirmatory result.

No development baseline achieved a `strong_targeted_pass`, primarily because S1 remained 1.0 in every run.

## Judge resource diagnostics

The twelve judge calls consumed, separately from treatment budgets:

```text
total judge tokens: 243,898
mean total tokens per judge pass: approximately 20,325
minimum: 17,352
maximum: 23,296
```

Judge-resource usage is evaluation overhead only and is not charged to B0, B1, or P0 treatment envelopes, as preregistered.

## Calibration decision

The semantic judge is accepted for Prototype V0 held-out use without substantive rubric modification.

Reasons:

```text
very high two-pass criterion agreement;
no extreme disagreements;
no critical-flag disagreements;
no manual-adjudication cases;
strong agreement with the important prior manual findings;
no evidence that condition labels or run IDs affected the primary score;
no need to add or remove semantic criteria.
```

The preregistered evaluator, held-out bundle identities, treatment budgets, continuation thresholds, and falsification rules therefore remain unchanged.

## P0 boundary

The final pre-P0 controls are now complete:

```text
B0/B1 calibration complete and analyzed;
held-out protocol preregistered;
H1/H2 exact bundles frozen and fingerprinted;
semantic rubric frozen;
condition-blinded two-pass judge implemented;
judge calibration completed successfully;
no substantive evaluator amendment required.
```

P0 implementation may now begin.

The implementation must remain inside the pre-specified Version 0 scope. It may operationalize only:

```text
minimal typed project state;
the same four methodological knowledge components;
dynamic activation/applicability;
prospective protected-test safeguard;
dependency-aware reopening/repair;
minimal state-derived runnable frontier;
append-only state-change history.
```

It must not add a specialist reviewer, new privileged methodological knowledge, held-out-specific rules, or uncounted model calls.
