# Checkpoint 153: Disposition Semantics Provider-Free Gate Passed Cross-Platform

**Date:** 2026-08-23  
**Status:** Provider-free implementation gate passed on Ubuntu and Windows; no Specification 016 live provider call has occurred  
**Checkpoint class:** IMPLEMENTATION / VALIDATION  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the completed provider-free implementation and cross-platform validation of the frozen Specification 016 disposition-semantics diagnostic before any live model call.  
**Authority:** Historical implementation/validation checkpoint. Specification 016 v0.1 and `disposition_semantics_v1.json` remain the frozen experiment authority.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-disposition-semantics-diagnostic`  
**Associated PR:** #15 -> `v1-frontend-spike`  
**Validated implementation head:** `6e7af25fd96d79673a59845e1c608c752970f658`

## 1. Frozen contract remained unchanged

Checkpoint 152 froze Specification 016 before implementation. The provider-free implementation did not change:

```text
operational DEFER / NOT_NOW definitions
six contrastive pairs
12 variants
three repetitions per variant
36 planned successful reasoner calls
45 maximum provider attempts
randomization seed 2026082302
retry policy
model/runtime treatment
hard-gate thresholds
advancement outcome labels
```

No live provider call occurred during this implementation phase.

---

## 2. Implemented provider-free seam

The bounded implementation now contains:

```text
experiment-only DispositionSemanticsResult
    disposition: DEFER | NOT_NOW
    defer_until_id: exact supplied trigger ID | null
    rationale: non-empty string

frozen fixture validation
    exactly six pairs
    exactly one DEFER and one NOT_NOW variant per pair
    exact trigger-pointer truth for DEFER
    null trigger-pointer truth for NOT_NOW
    no shared/variant evidence overwrite

frozen randomized call plan
    36 deterministic entries
    globally shuffled from seed 2026082302
    unique run IDs
    unique condition-neutral nonces

truth-blinded request construction
    evaluator labels/expected pointers absent from model input
    no reusable methodological knowledge
    no Horizon or selective context
    no tools
    no cross-call state

attempt ledger and retry enforcement
    maximum 45 provider attempts
    one retry only for frozen retry categories
    failed attempts preserved

hard-gate evaluator
    exact disposition accuracy
    per-variant majority
    per-pair polarity
    exact DEFER pointer accuracy
    exact NOT_NOW null-pointer correctness
    SUPPORTED / NOT_SUPPORTED / INCOMPLETE outcome
```

The ADS-owned `ReasoningRequest` was generalized only enough to accept a caller-supplied ADS structured-output type. The already accepted `ReasoningContextValueResult` remains the default, and its existing digest behavior is deliberately preserved.

The OpenAI Agents infrastructure adapter now forwards the requested ADS-owned structured-output type while provider SDK types remain outside the application/domain layers.

---

## 3. Provider-free runner closure

`experiments/disposition_semantics/runner.py` now executes the complete frozen experiment shape without requiring a live provider when supplied a fake runtime.

It mechanically preserves:

```text
reasoning_plan.json
reasoner_attempts.jsonl
result.json
RESULT.md
```

The fake runtime integration test classifies from model-visible project evidence only. It does not read frozen evaluator truth.

Provider-free runner validation demonstrates:

```text
36 / 36 successful outputs
all six hard gates pass under the visible-evidence fake runtime
one deliberate transport failure is retried once
failed attempt is preserved
provider-attempt count becomes 37
frozen final classification remains unchanged after the allowed retry
```

This validates experiment mechanics. It is not evidence that the live model will pass the diagnostic.

---

## 4. Historical RA-02 admissibility diagnostic

The provider-free implementation also checks the two historical Specification 015 RA-02 actions under the stronger Specification 016 benchmark-construction rule.

Observed:

```text
add-generic-bagging-baseline
    NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER

plot-all-feature-histograms-before-shortlist
    NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER
```

Reason: the historical fixture does not contain the explicit dependency-backed trigger pointer required for a new Specification 016 unambiguous DEFER example.

This does **not** rescore, relabel, or repair Specification 015. Its frozen FAIL remains unchanged.

---

## 5. Exact cross-platform CI evidence

Validated branch head:

```text
6e7af25fd96d79673a59845e1c608c752970f658
```

Dedicated workflow:

```text
V1 disposition semantics diagnostic
run 32646969810
```

Ubuntu:

```text
provider-free diagnostic tests  15 passed
full V1 Python suite            62 passed, 2 skipped
result                          PASS
```

Windows:

```text
provider-free diagnostic tests  15 passed
full V1 Python suite            62 passed, 2 skipped
result                          PASS
```

The two skipped tests are the existing PostgreSQL-backed integration tests when `ADS_TEST_POSTGRES_URL` is not configured.

The ordinary workflow explicitly verifies that `OPENAI_API_KEY` is absent.

Inherited regression workflows on the same exact head also passed:

```text
Checkpoint metadata
    run 32646969848
    PASS

V1 reasoning context value
    run 32646969808
    PASS
```

This is important because the generalized structured-output request/runtime seam touches the already accepted Specification 014 runtime path.

---

## 6. Promotion audit

### Promote DEFER / NOT_NOW as production semantics

**Decision:** no.

Reason: only provider-free experiment mechanics have passed. The live construct-validity question has not been answered.

### Promote explicit trigger-backed sequencing as a production dependency model

**Decision:** no.

Reason: the relation-backed distinction is still an experiment hypothesis.

### Promote generalized ADS structured-output request capability

**Decision:** continue provisionally through the diagnostic branch, but do not make a new project-level architecture decision yet.

Reason: the change is narrow, provider-neutral, preserves the accepted default behavior, and passed the complete current regression suite. Final promotion belongs after the live diagnostic and PR-level promotion audit.

### Rewrite Specification 015

**Decision:** no.

Its negative result remains immutable historical evidence.

### Make live calls now

**Decision:** not yet.

The explicit secret-gated live workflow and an exact pre-live boundary checkpoint must still be created and validated first.

---

## 7. Exact continuation

```text
1. add the explicit manual secret-gated Specification 016 live workflow
2. keep live execution restricted to v1-disposition-semantics-diagnostic
3. rerun the frozen provider-free gate inside the live workflow before any provider call
4. preserve the exact live-ready source head in the next checkpoint
5. validate that exact head under ordinary provider-free CI
6. expose only the workflow dispatcher on main so GitHub can manually dispatch it
7. make no live provider call until that exact pre-live boundary is green
8. then execute the unchanged 36-call frozen diagnostic once
```
