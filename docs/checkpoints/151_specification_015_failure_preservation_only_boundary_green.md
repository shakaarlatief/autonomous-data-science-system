# Checkpoint 151: Specification 015 Failure Preservation-Only Boundary Green

**Date:** 2026-08-23  
**Status:** Preservation-only boundary checkpoint; failed Specification 015 experiment history and canonical routing are isolated from the rejected implementation and validated before merge  
**Checkpoint class:** FAILURE PRESERVATION / PROMOTION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the branch that carries the frozen Specification 015 design, live artifact/result, failure interpretation, and canonical routing onto the accepted V1 line without carrying the failed recommendation implementation from PR #13.  
**Authority:** Historical preservation and current routing consequence. This checkpoint does not promote the failed recommendation/action seam. Specification 015 v0.1 remains immutable historical experiment authority for its completed run.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-recommendation-action-failure-preservation`  
**Associated PR:** #14 -> `v1-frontend-spike`  
**Rejected implementation PR:** #13 -> `v1-frontend-spike`

## 1. Starting accepted boundary

This preservation branch starts exactly from the last accepted integration commit:

```text
bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
Merge PR #12: validate selective context value in real reasoning
```

That boundary already accepts Specification 014 v1.0 / Checkpoint 146 and the bounded selective-context + ADS-owned `ReasoningRuntime` seam.

The preservation branch does not descend from PR #13's failed implementation head.

---

## 2. What is preserved

The branch carries historical experiment authority and evidence:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json

docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md

experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
```

Canonical routing has been reconciled through:

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/OPEN_QUESTIONS.md
docs/MAJOR_CHANGES.md
```

The structural-history file was deliberately compacted while preserving its major milestones and adding the Specification 014 pass / Specification 015 fail transition. This is navigation/history maintenance only; detailed historical authority remains in decisions, foundations, specifications, checkpoints, experiment reports, and Git history.

---

## 3. What is deliberately not preserved as accepted implementation

A compare against `v1-frontend-spike` confirms this preservation route does not carry the failed production-facing recommendation implementation from PR #13.

Not promoted here:

```text
src/ads_system/application/recommendation.py
experiments/recommendation_action_value/environment.py
experiments/recommendation_action_value/harness.py
experiments/recommendation_action_value/judge.py
experiments/recommendation_action_value/runner.py
recommendation/action production tests and live workflow implementation
```

The experiment fixture and raw result are preserved because they are evidence. The failed implementation is not adopted as an accepted V1 seam.

---

## 4. Frozen live result remains FAIL

Live workflow:

```text
V1 recommendation action value live
run 32642733784
job 97202216781
source head d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
```

Execution completed:

```text
reasoner outputs       36 / 36
judge outputs          36 / 36
provider attempts      72
retries                0
```

Frozen advancement:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0
outcome            FAIL
```

The sole failed gate remains `RA-G05`, localized to `RA-02 MODEL_CHOICE` exact disposition accuracy:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
required floor 0.800000
```

The repeated mismatch was `DEFER` expected versus `NOT_NOW` observed for two noncritical expansion actions. All nine RA-02 outputs scored `1.000000` under the blinded semantic rubric.

No threshold, expected label, treatment, prompt, model, or evaluator has been changed to reinterpret that result.

---

## 5. Exact pre-checkpoint validation

The final preservation/routing head immediately before this checkpoint was:

```text
d843c39a26867c70557b978ff5faf778bda5aaaa
```

That head passed:

```text
Checkpoint metadata
    run 32644994687
    PASS

V1 reasoning context value
    run 32644994598
    PASS
```

No recommendation/action production workflow runs on this preservation branch because the failed implementation/workflow is intentionally absent.

The preservation diff contains historical/frozen design, fixture, result, raw artifact, checkpoints, and routing documents only.

---

## 6. Promotion audit

### Preserve failed experiment evidence on the accepted integration line

**Decision:** yes.

Reason: negative evidence is part of project truth and must not remain stranded on a rejected implementation branch.

### Promote Specification 015 recommendation/action implementation

**Decision:** no.

Reason: frozen advancement outcome `FAIL`.

### Promote benchmark disposition taxonomy

**Decision:** no.

Reason: `DEFER` versus `NOT_NOW` requires a dedicated semantics/failure-attribution diagnostic.

### Promote automatic project mutation or execution

**Decision:** no.

Reason: recommendation behavior has not earned the prerequisite seam.

### Add a permanent architecture decision

**Decision:** no.

The failure motivates diagnosis, not a final taxonomy or orchestration commitment.

### Update structural history

**Decision:** yes, completed in `docs/MAJOR_CHANGES.md`.

---

## 7. Exact continuation

After this checkpoint commit itself is green:

```text
1. merge PR #14 into v1-frontend-spike
2. close PR #13 without merge
3. create a new diagnostic branch from the resulting preserved integration head
4. preregister a bounded DEFER-vs-NOT_NOW / failure-attribution diagnostic
5. isolate recommendation-label semantics from SELECTIVE-vs-control system value
6. make no new live model calls before the diagnostic contract is frozen
7. only after diagnosis decide whether a revised recommendation/action experiment is justified
```

Do not repair Specification 015 in place and do not import the rejected recommendation implementation merely because parts of its live behavior looked strong.
