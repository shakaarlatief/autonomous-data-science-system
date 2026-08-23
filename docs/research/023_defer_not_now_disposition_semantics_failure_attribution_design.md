# Research 023: DEFER versus NOT_NOW Disposition Semantics and Failure Attribution Design

**Date:** 2026-08-23  
**Status:** Design rationale for a separately versioned post-Specification-015 diagnostic  
**Scope:** Diagnose whether the `DEFER` / `NOT_NOW` distinction can be made operationally explicit and reliably classified before another recommendation/action-value experiment.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Trigger

Specification 015 completed exactly as frozen and returned `FAIL`.

The failure was unusually narrow:

```text
14 / 15 named gates passed
only RA-G05 failed
failure localized to RA-02 MODEL_CHOICE
```

In RA-02 the frozen evaluator expected:

```text
add-generic-bagging-baseline                  DEFER
plot-all-feature-histograms-before-shortlist DEFER
```

but all SELECTIVE and FULL_HORIZON repetitions returned:

```text
NOT_NOW
```

GENERIC produced nearly the same pattern. All nine RA-02 outputs received a condition-blinded semantic score of `1.000000`.

Therefore the next justified question is not whether SELECTIVE beats GENERIC. The immediate question is whether the disposition boundary itself is sufficiently operational to support deterministic project navigation.

## 2. Failure hypotheses

The preserved result leaves four distinct explanations:

```text
A. taxonomy/semantic problem
    DEFER and NOT_NOW are not operationally separable enough.

B. benchmark-truth problem
    the original RA-02 DEFER labels were defensible under the old prose definitions,
    but not uniquely implied by the supplied state.

C. reasoner-calibration problem
    the labels are separable when evidence is explicit,
    but the reasoner still cannot apply the distinction reliably.

D. system-value problem
    even after semantics are made measurable,
    explicit methodological knowledge may still add no recommendation value
    beyond a strong generic reasoner.
```

Specification 015 cannot distinguish these cleanly because it tested B/C/D simultaneously while treating the disposition taxonomy as fixed.

## 3. Diagnostic order

The next slice should isolate semantics before system value:

```text
first
    make DEFER vs NOT_NOW mechanically distinguishable

then
    test whether one strong reasoner applies the distinction reliably

only later
    reintroduce GENERIC vs SELECTIVE vs FULL_HORIZON
```

No reusable methodological knowledge is needed for the semantic diagnostic. Retrieval, Horizon construction, selective context, and recommendation-value comparison are deliberately held out.

This avoids attributing a taxonomy failure to knowledge selection.

## 4. Stronger operational definition

The original definitions were:

```text
DEFER
    relevant/useful, but not now because a more immediate dependency,
    sequencing constraint, or current priority should be resolved first

NOT_NOW
    current evidence/objective does not materially justify prioritizing the action now
```

The practical ambiguity is that almost any `NOT_NOW` action might become useful eventually, while almost any low-priority action can be described as waiting for something else.

The diagnostic therefore makes the distinction relational rather than merely verbal.

### DEFER

An action is `DEFER` only when the supplied project state establishes all of:

```text
1. the action is already justified for the represented project plan;
2. a specific currently unresolved prerequisite/trigger is represented;
3. that prerequisite/trigger has an allowed stable trigger ID;
4. once that trigger is satisfied, the action is represented as current next work
   under the otherwise relevant plan.
```

A DEFER output must therefore include:

```text
defer_until_id = one exact supplied trigger ID
```

### NOT_NOW

An action is `NOT_NOW` when:

```text
1. the current objective/state does not materially justify prioritizing it; and
2. no represented supplied trigger establishes that satisfying one current dependency
   makes the action current next work.
```

A NOT_NOW output must therefore include:

```text
defer_until_id = null
```

The key distinction becomes:

```text
DEFER     = later because this represented prerequisite/trigger must occur first
NOT_NOW   = not in the current represented plan; no such trigger relation exists
```

This is a candidate diagnostic definition, not a promoted production taxonomy.

## 5. Why this is better aligned with ADS semantics

Foundation 018 already distinguishes project objects, relations, and events. A sequencing disposition should therefore have a relation-like justification rather than exist as an isolated label.

Conceptually:

```text
Action A
    DEFER until Trigger T
```

is materially different from:

```text
Action A
    NOT_NOW
    no current activating dependency/trigger represented
```

This also maps more naturally to a future Cockpit:

```text
Deferred
    Hyperparameter tuning
    waiting for: model family selected

Not now
    Broad feature histogram sweep
    not part of current objective
```

The diagnostic does not yet authorize those UI or state semantics.

## 6. Contrastive benchmark design

Use six contrastive action pairs across heterogeneous data-science situations.

Each pair contains:

```text
same candidate action
same output schema
same disposition definitions
same trigger menu shape
same model/runtime treatment

variant A
    explicit unresolved trigger relation
    expected DEFER + exact trigger pointer

variant B
    no represented activating trigger relation
    expected NOT_NOW + null pointer
```

The pairs cover:

```text
DS-01  hyperparameter tuning
DS-02  subgroup error analysis
DS-03  feature-interaction engineering
DS-04  missingness sensitivity analysis
DS-05  probability calibration analysis
DS-06  additional distribution plotting
```

The cases are deliberately clearer than the historical RA-02 examples. The purpose is not realism maximization. It is construct validity: can the proposed semantic boundary be represented and classified reproducibly at all?

## 7. Historical RA-02 interpretation

The two disputed RA-02 actions should remain untouched in Specification 015.

Under the stricter diagnostic construction rule, a DEFER benchmark case is admissible only if the project state contains an explicit named activating prerequisite/trigger and represents the action as current next work once that trigger resolves.

The historical RA-02 examples did not encode that stronger relation explicitly. Therefore:

```text
they remain valid immutable Specification 015 historical cases;

they would not qualify as unambiguous DEFER cases
under the proposed Specification 016 diagnostic construction rule.
```

This does not retroactively prove their original labels were wrong. It explains why they are unsuitable for deciding whether the stronger operational distinction is learnable.

## 8. Model treatment

Use one reasoner condition only.

```text
no reusable methodological assets
no Horizon/context comparison
no semantic judge
no tools
no previous response state
```

Keep the same concrete model/runtime treatment used in Specifications 014-015 so a new model change does not become another confound.

That treatment remains an experiment constant only, not a final model/provider selection.

## 9. Planned observations

```text
6 pairs
2 variants per pair
3 repetitions per variant

12 frozen variants
36 planned successful reasoner calls
45 maximum provider attempts
```

Call order is frozen by a deterministic seed before any live calls.

One retry per planned call is allowed only for transport/provider/incomplete/invalid-structured-response failure. Semantic disagreement is never a retry reason.

## 10. Structured output

The minimum diagnostic output is:

```text
DispositionSemanticsResult
    disposition: DEFER | NOT_NOW
    defer_until_id: string | null
    rationale: string
```

Validation rules:

```text
DEFER
    requires exactly one valid supplied defer_until_id

NOT_NOW
    requires defer_until_id == null

unknown trigger IDs
    invalid structured response
```

Rationale is preserved for inspection but is not judged semantically in the hard gate.

## 11. Deterministic evaluation

Primary metrics:

```text
exact disposition accuracy
exact defer-trigger pointer accuracy
invalid structured-response count
per-variant repetition success
per-pair polarity success
NOT_NOW null-pointer correctness
```

No LLM judge is needed for the main result. The expected distinction is intentionally encoded as a structural benchmark property.

## 12. Proposed advancement rule

A passing result should require all of:

```text
0 invalid successful outputs
aggregate exact disposition accuracy >= 0.95
every frozen variant correct in at least 2 / 3 repetitions
every contrastive pair has both sides correct in at least 2 / 3 repetitions
all expected-DEFER outputs identify the exact trigger pointer
all expected-NOT_NOW outputs return a null trigger pointer
```

Because there are 18 expected-DEFER observations, a `0.95` pointer threshold would effectively require all 18. Making that requirement explicit is clearer.

Outcome:

```text
DISPOSITION_BOUNDARY_SUPPORTED
DISPOSITION_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

## 13. Interpretation boundaries

### If supported

The supported conclusion is only:

```text
A dependency-backed DEFER definition is operationally representable
and the frozen reasoner can distinguish it from NOT_NOW
on deliberately unambiguous contrastive cases.
```

Then a separately preregistered recommendation/action-value experiment may reuse the clarified semantic structure.

It would still need to test whether SELECTIVE adds value beyond GENERIC.

### If not supported

Do not run another recommendation-value comparison with the same four-label taxonomy.

Instead consider:

```text
collapse DEFER and NOT_NOW into a broader NOT_CURRENT state;
or
represent sequencing as an explicit dependency relation
rather than as a mutually exclusive recommendation label.
```

## 14. Explicit non-conclusions

This diagnostic does not establish:

```text
that original RA-02 evaluator truth was wrong
that Specification 015 should be rescored
that SELECTIVE adds recommendation value
that DEFER/NOT_NOW should become production enums
that recommendations may mutate project state
that automatic execution is safe
that current model/provider settings are final
```

## 15. Recommended next implementation boundary

Before any live call:

```text
1. freeze Specification 016 and its fixture
2. implement an ADS-owned experiment-only result validator/harness
3. add a provider-free contrastive-fixture construction audit
4. prove call-plan determinism and retry/attempt accounting
5. validate the complete fake-runtime 36-output shape
6. validate the exact implementation head under ordinary CI
7. only then expose one explicit secret-gated live workflow
```
