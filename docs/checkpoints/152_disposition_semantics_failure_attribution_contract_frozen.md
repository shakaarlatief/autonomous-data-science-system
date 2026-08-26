# Checkpoint 152: Disposition Semantics Failure-Attribution Contract Frozen

**Date:** 2026-08-23  
**Status:** Pre-implementation diagnostic checkpoint; Specification 016 and its contrastive fixture are frozen before diagnostic implementation or new live provider calls  
**Checkpoint class:** PREREGISTERED DIAGNOSTIC CONTRACT  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the first post-Specification-015 diagnostic of whether dependency-backed `DEFER` is operationally separable from `NOT_NOW` on deliberately unambiguous contrastive project microstates.  
**Authority:** Historical freeze record. Specification 016 v0.1 and `disposition_semantics_v1.json` govern the diagnostic until its result is preserved. This checkpoint does not modify Specification 015 or promote recommendation taxonomy.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-disposition-semantics-diagnostic`

## 1. Starting preserved integration boundary

PR #14 preserved the failed Specification 015 experiment without adopting its failed recommendation implementation.

Promoted preservation merge:

```text
10aa3f59bedc5ee45a38f0ae05c68da901d9adff
```

PR #13 was then closed without merge.

This diagnostic branch was created exactly from `10aa3f59...`.

Therefore the new work begins from:

```text
accepted Specification 014 reasoning-context seam
+
immutable Specification 015 negative evidence
-
failed Specification 015 recommendation implementation
```

---

## 2. Diagnostic rationale frozen

Primary rationale:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
```

Specification 015 failed only `RA-G05`, with the discrepancy concentrated in `RA-02 MODEL_CHOICE`:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
```

The repeated exact-label difference was:

```text
frozen truth   DEFER
observed       NOT_NOW
```

for two noncritical expansion actions, while all nine RA-02 semantic judge outputs scored `1.000000`.

The next experiment therefore does not compare methodological-context treatments. It isolates the disposition boundary itself.

---

## 3. Frozen operational semantics

### DEFER

Use `DEFER` only when the supplied state establishes:

```text
action already justified in represented plan
+
specific unresolved supplied prerequisite/trigger
+
exact trigger ID
+
action becomes current next work once trigger is satisfied
```

A valid DEFER result requires:

```text
defer_until_id = exact activating trigger ID
```

### NOT_NOW

Use `NOT_NOW` when:

```text
current objective/state does not materially justify prioritizing the action
+
no represented supplied trigger makes it current next work after resolution
```

A valid NOT_NOW result requires:

```text
defer_until_id = null
```

The key proposed distinction is therefore relational:

```text
DEFER     = later because this represented trigger must occur first
NOT_NOW   = not in the current represented plan; no activating trigger relation exists
```

These remain diagnostic semantics only.

---

## 4. Frozen fixture

Authoritative fixture:

```text
tests/fixtures/reasoning/disposition_semantics_v1.json
```

Exactly six contrastive pairs:

```text
DS-01  model-tuning
DS-02  subgroup-error-analysis
DS-03  feature-interaction-engineering
DS-04  missingness-sensitivity
DS-05  probability-calibration
DS-06  distribution-evidence
```

Every pair has exactly:

```text
one DEFER variant
one NOT_NOW variant
same action
same trigger menu
same shared project evidence
variant-specific evidence only
```

Expected truth is evaluator-only and must not enter reasoner inputs.

The historical RA-02 examples remain immutable. They are not part of the new hard benchmark and cannot be rescored by this diagnostic.

---

## 5. Frozen treatment

One reasoner condition only:

```text
no reusable methodological assets
no retrieval/Horizon/context treatment
no GENERIC/SELECTIVE/FULL comparison
no semantic judge
no tools
no previous response state
```

Concrete diagnostic model/runtime treatment:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents==0.19.4
gpt-5.6-sol
reasoning effort medium
verbosity low
max output tokens 2000
```

This remains an experiment constant, not a final provider/model decision.

---

## 6. Frozen call plan

```text
6 pairs
2 variants per pair
3 repetitions per variant
12 variants
36 planned successful reasoner calls
45 maximum provider attempts
randomization seed 2026082302
```

At most one retry per planned call, only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

The complete plan and digest must exist before the first provider call.

---

## 7. Frozen structured result

Experiment-only result:

```text
DispositionSemanticsResult
    disposition: DEFER | NOT_NOW
    defer_until_id: str | None
    rationale: str
```

Contract:

```text
DEFER     -> exact supplied trigger required
NOT_NOW   -> null trigger required
unknown trigger/disposition -> invalid
empty rationale -> invalid
```

No authoritative project mutation is permitted.

---

## 8. Frozen hard gates

All must pass for support:

```text
DS-G01  zero unresolved invalid successful outputs
DS-G02  aggregate exact disposition accuracy >= 0.95
DS-G03  every variant correct in at least 2 / 3 repetitions
DS-G04  every pair has both sides correct in at least 2 / 3 repetitions
DS-G05  exact expected-DEFER trigger-pointer accuracy == 1.00
DS-G06  expected-NOT_NOW null-pointer correctness == 1.00
```

Frozen outcomes:

```text
DISPOSITION_BOUNDARY_SUPPORTED
DISPOSITION_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

No post-result threshold tuning is allowed.

---

## 9. Interpretation freeze

### If supported

Supported conclusion is limited to:

```text
dependency-backed DEFER is operationally representable
and the fixed reasoner can distinguish it from NOT_NOW
on the frozen deliberately unambiguous cases
```

It does not establish SELECTIVE recommendation value.

A later separately preregistered recommendation/action experiment may then use the clarified construction rule.

### If not supported

Do not run another SELECTIVE-vs-control recommendation-value experiment using the same disposition distinction.

First consider collapsing `DEFER` and `NOT_NOW` or moving sequencing into an explicit dependency relation rather than an exclusive recommendation label.

---

## 10. Explicit non-decisions

This checkpoint does not:

```text
change Specification 015
rescore RA-02
promote DEFER/NOT_NOW into production
establish recommendation/action value
authorize project-state mutation
authorize automatic execution
select a final provider/model
select a multi-agent architecture
justify retrieval/reranking/vector changes
```

---

## 11. Promotion audit

### Promote Specification 016 as frozen diagnostic contract

**Decision:** yes, at v0.1 preregistration authority only.

### Promote a production recommendation taxonomy

**Decision:** no.

### Add a new project-level decision/principle

**Decision:** no.

The stronger DEFER semantics are a diagnostic hypothesis until evaluated.

### Update current routing

**Decision:** yes.

README, CURRENT_STATE, KNOWLEDGE_MAP, and OPEN_QUESTIONS should route to this diagnostic after the freeze.

### Update MAJOR_CHANGES

**Decision:** not yet.

The Specification 015 failure is already recorded. Add another structural-history entry only after the diagnostic changes the development direction materially.

---

## 12. Exact continuation

```text
1. implement the experiment-only result type and validation
2. implement the provider-free contrastive fixture/admissibility audit
3. implement deterministic plan, attempt ledger, and gate evaluator
4. implement complete 36-output fake-runtime integration coverage
5. add ordinary provider-free CI with no OPENAI_API_KEY
6. preserve and validate the exact implementation head
7. only then create/expose a secret-gated live workflow
8. make no new live model call before that pre-live checkpoint is green
```
