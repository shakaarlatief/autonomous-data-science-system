# Research 029: Dependency-Backed Recommendation-Value Experiment Design

**Date:** 2026-08-24  
**Status:** Prospective experiment-design rationale  
**Authority:** Research only. This memo motivates Specification 021 but does not authorize implementation, live provider calls, project mutation, or production recommendation semantics.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Purpose

The next legitimate scientific question is again the question that Specifications 015, 017, and 019 attempted to answer:

> Does selective explicit methodological knowledge improve downstream recommendation/action quality beyond a strong generic reasoner, while avoiding the expansion cost of supplying the full methodological Horizon?

That question remains unanswered.

The previous experiments produced useful failure-attribution evidence rather than a positive recommendation-value result:

```text
Specification 015   FAIL
    DEFER versus NOT_NOW was not structurally anchored enough

Specification 016   SUPPORTED
    DEFER-like sequencing becomes operationally separable when one exact activating dependency is represented

Specification 017   INCOMPLETE
    model-authored methodological provenance duplicated system-known provenance and prevented a valid complete comparison

Specification 019   FAIL
    system-owned provenance repaired the instrumentation defect, but SELECTIVE repeatedly over-blocked useful model-family comparison actions

Specification 020   SUPPORTED
    RECOMMENDED versus BLOCKING_REQUIRED becomes operationally separable when an exact unresolved requirement, exact active defended downstream scope, explicit scope dependency, and exact resolving action are represented
```

Specification 020 therefore removes one major construct-validity objection to a new recommendation-value experiment. It does not make Specification 019 successful and does not justify changing its historical truth.

The next experiment should be genuinely prospective and should combine the structural lessons from Specifications 016, 019, and 020 without tuning old observed outputs into favorable labels.

---

## 2. What must remain fixed

The successor experiment should preserve the strongest accepted boundaries:

```text
GENERIC / SELECTIVE / FULL_HORIZON comparison
same ADS-owned ReasoningRuntime and fixed model treatment
system-owned exact methodological provenance
same accepted ten-asset methodological universe
same accepted selective exact-revision context path
no retrieval/model/provider change
no tools
no project mutation
blinded semantic judging
complete-design requirement before scientific classification
```

The experiment is not an opportunity to improve the selector, change the knowledge base, choose a more favorable model, or redesign the provider runtime.

Those changes would make failure attribution weaker.

---

## 3. The central correction: relation-backed dispositions must be explicit

Specification 019 asked the reasoner to infer blocking strength from project evidence and a blocked-scope menu. That left room for a strong recommendation to be escalated into `BLOCKING_REQUIRED` even when the state did not contain one exact represented blocked-scope relation.

Specification 020 showed that the stronger construction can be applied reliably:

```text
BLOCKING_REQUIRED
    current justified action
    + exact unresolved requirement
    + exact active defended downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action RESOLVES requirement
```

The successor benchmark should therefore encode those identities and relations directly in the supplied project microstate.

The same principle applies to sequencing:

```text
DEFER
    already-justified or planned action
    + exact unresolved trigger
    + explicit action WAITS_FOR trigger relation
```

The reasoner should not invent either blocking or defer relations.

This creates a cleaner division:

```text
SYSTEM-OWNED STRUCTURE
    action identities
    requirement identities
    downstream-scope identities
    scope -> requirement dependencies
    action -> requirement resolver relations
    defer-trigger identities
    action -> trigger wait relations
    exact methodological provenance

MODEL-OWNED CONTENT
    disposition selection among supplied actions
    relation pointers among supplied identities
    recommendation rationales
    summary / warnings
```

---

## 4. Why blocking should remain in the model result for this experiment

Once blocking relations are explicit, the harness could theoretically derive `BLOCKING_REQUIRED` deterministically.

The successor experiment should not yet make that production architecture decision.

Keeping the disposition in the model result has two advantages:

1. it directly verifies that the reasoner respects the explicit structural semantics inside a mixed recommendation task rather than only in the isolated Specification 020 diagnostic;
2. it preserves comparability with the earlier recommendation experiments while removing the ambiguity that caused the main Specification 019 failure mode.

The experiment can therefore test recommendation value while also treating any renewed over-blocking as a strict calibration regression.

Whether production blocking should eventually be deterministic from relations remains a separate question.

---

## 5. New truth, not a favorable rescore

Specification 021 should use newly authored project microstates and action menus.

It should not overlay or relabel Specification 019 cases.

Permitted design inputs are only durable lessons already established before the new calls:

```text
Specification 016 dependency-backed DEFER construct
Specification 019 system-owned provenance boundary
Specification 020 explicit requirement/scope blocking construct
Specification 013 accepted selective key sets
Specification 014 accepted selective-context reasoning path
```

The new benchmark may reuse the same four methodological neighborhoods because those are the exact neighborhoods whose selector behavior is already accepted:

```text
prediction validity
nonlinear model options
distribution evidence
missingness / class imbalance
```

But project states, action menus, requirement relations, triggers, expected dispositions, and judge obligations must be frozen prospectively before any new provider call.

No individual Specification 019 output may be used to tune a new expected label or gate.

---

## 6. Benchmark architecture

A compact four-case design is preferable to expanding scientific scope.

Each case should contain multiple candidate actions so a single reasoner output tests a structured decision set rather than one binary label.

### Case 1: future-prediction validity and sequencing

Methodological context:

```text
prediction-moment
prediction-time-feature-eligibility
temporal-validation
```

The project state should contain explicit unresolved requirements protecting one active future-facing model-selection scope.

Actions that resolve those requirements are `BLOCKING_REQUIRED` with exact pointers.

Already approved model comparisons wait on one exact `prediction-validity-established` trigger and are `DEFER`.

An unrelated distribution action is `NOT_NOW`.

### Case 2: compact nonlinear model shortlist

Methodological context:

```text
gradient-boosted-trees
random-forest
```

Prediction validity and validation are already established. No active defended scope is represented as blocked on either model-family comparison.

Random Forest and Gradient-Boosted Trees evaluation are therefore worthwhile non-blocking `RECOMMENDED` work.

Tuning actions are `DEFER` behind one exact initial-comparison trigger.

Unrelated or redundant expansion actions are `NOT_NOW`.

This case is intentionally the clean prospective test of the calibration problem that appeared in Specification 019, without changing Specification 019 itself.

### Case 3: distribution evidence before transformation

Methodological context:

```text
histogram
ecdf
```

Histogram and ECDF inspection are current `RECOMMENDED` evidence-gathering actions.

A downstream transformation comparison is `DEFER` until the evidence-review trigger is satisfied.

Premature transformation or unrelated modeling actions are `NOT_NOW`.

No active defended scope is blocked, so `BLOCKING_REQUIRED` must not be used.

### Case 4: missingness and class-imbalance decision framework

Methodological context:

```text
missing-data
class-imbalance
```

Two unresolved requirements protect two exact active downstream scopes:

```text
class prevalence -> evaluation/metric plan
production missingness regime -> preprocessing plan
```

The actions that resolve those requirements are `BLOCKING_REQUIRED` with exact pointers.

Current missingness-pattern analysis can be `RECOMMENDED` without being blocking.

Actions whose legitimacy depends on resolved data-quality facts are `DEFER` behind exact triggers.

A premature accuracy-only or global-imputation action is `NOT_NOW`.

---

## 7. Output contract should bind dispositions to relations locally

The previous global `blocked_scopes` list makes action-to-scope attribution indirect.

A cleaner experiment result is:

```text
DependencyBackedRecommendationActionResult
    summary
    action_decisions[]
        action_id
        disposition
        blocking_requirement_id
        blocked_scope_id
        defer_until_id
        rationale
    warnings
```

Pointer rules:

```text
BLOCKING_REQUIRED
    exact supplied requirement pointer
    exact supplied blocked-scope pointer
    null defer pointer

RECOMMENDED
    null blocking pointers
    null defer pointer

DEFER
    null blocking pointers
    exact supplied defer-trigger pointer

NOT_NOW
    all three pointers null
```

This combines the strongest structural ideas from Specifications 016 and 020 in one mixed recommendation task.

---

## 8. What counts as recommendation value

The experiment should not promote the recommendation seam merely because SELECTIVE is valid.

A strong generic reasoner is the relevant baseline.

The required interpretation remains:

```text
SAFE
    SELECTIVE meets absolute quality requirements
    and is non-inferior to GENERIC and FULL_HORIZON
    and does not expand recommendations more aggressively than FULL_HORIZON

DIFFERENTIATED
    SELECTIVE additionally shows at least one prospectively frozen positive value signal
```

Possible value signals should remain about recommendation quality rather than context cost:

```text
higher exact disposition accuracy than GENERIC
higher blinded semantic score than GENERIC
fewer critical omissions than GENERIC
fewer under-recommendations than GENERIC
fewer blocking false positives than GENERIC
lower unnecessary recommendation cost than FULL_HORIZON
fewer over-recommendations than FULL_HORIZON
```

Input-token or methodology-byte savings remain descriptive evidence only. Specification 014 already established the bounded context-economy result.

---

## 9. A no-difference result is scientifically useful

The current accepted knowledge universe is deliberately small and contains fairly standard methodology.

A strong generic model may already know and apply most of it.

Therefore the successor contract must allow:

```text
SAFE_BUT_NOT_DIFFERENTIATED
```

as a legitimate complete outcome.

That outcome would mean:

```text
clean relation-backed semantics no longer cause the previous calibration failure,
but selective explicit methodological context still does not measurably improve recommendation quality over the generic reasoner on this bounded knowledge set.
```

The correct next step would not be to keep rewriting the same benchmark until SELECTIVE wins.

A more plausible next research direction would then be knowledge coverage, novelty, or broader methodological-universe construction, because the bottleneck may be the content universe rather than the selective-context mechanism.

---

## 10. Failure interpretation

If SELECTIVE still fails strict blocking calibration despite explicit relations, that is a materially stronger negative signal than Specification 019 because Specification 020 already demonstrated the fixed reasoner can apply the construct in isolation.

If SELECTIVE is safe but no better than GENERIC, the recommendation-value hypothesis remains unsupported for the current knowledge universe.

If SELECTIVE is safe, non-inferior, no more expansion-prone than FULL_HORIZON, and shows at least one frozen positive value signal, the bounded recommendation seam earns promotion to the next integration question.

None of these outcomes establish production taxonomy, ranking, state mutation, or automatic execution.

---

## 11. Proposed experiment boundary

Specification 021 should freeze:

```text
4 new cases
3 conditions
3 repetitions per condition
36 reasoner outputs
36 blinded judge outputs
90 maximum provider attempts
fixed gpt-5.6-sol treatment
system-owned methodology provenance
explicit requirement/scope/resolver relations
explicit defer-trigger relations
strict relation-pointer validation
absolute / relative / expansion gates
positive value signals
complete-design outcomes
provider-free construction audits
no live authorization until exact green implementation evidence is checkpointed
```

The experiment should remain read/reason/evaluate only.

---

## 12. Recommendation

Proceed with a frozen Specification 021 under a new branch.

The experiment should be treated as the cleanest prospective test so far of the original downstream value hypothesis:

> **Does the accepted selective methodological-context path improve recommendation/action quality once provenance and disposition semantics are no longer known confounds?**

A positive result would justify bounded recommendation-layer promotion.

A safe-but-undifferentiated result would strongly suggest that the current small methodological universe does not add measurable recommendation value beyond the strong generic reasoner.

A failure would reject promotion of the current recommendation seam.
