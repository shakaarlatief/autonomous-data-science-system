# Checkpoint 156: Relation-Backed Recommendation and Action Value Contract Frozen

**Date:** 2026-08-23  
**Status:** Historical preregistration checkpoint; Specification 017 contract frozen before implementation or live provider calls  
**Checkpoint class:** EXPERIMENT CONTRACT FREEZE  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the next recommendation/action-value experiment after the promoted Specification 016 dependency-backed disposition result.  
**Authority:** Historical preregistration provenance. Specification 017 and its frozen fixture govern implementation/evaluation for this slice.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Starting promoted merge:** `6bda0c1efcf078476859b2c2c64fb0586964899d`  
**Associated branch:** `v1-recommendation-action-value-relation-backed`

## 1. Starting evidence

The starting merge contains both:

```text
Specification 015
    immutable frozen FAIL

Specification 016
    immutable frozen live outcome
    DISPOSITION_BOUNDARY_SUPPORTED
```

Specification 016 observed:

```text
36 / 36 exact disposition classifications correct
18 / 18 expected-DEFER trigger pointers exact
18 / 18 expected-NOT_NOW pointers null
```

The supported bounded design/evaluation constraint is:

```text
DEFER-like sequencing
    requires a concrete represented activating dependency/trigger
    if deterministic distinction from NOT_NOW-like absence of current justification is expected.
```

This checkpoint does not promote those labels as production enums.

---

## 2. Frozen Specification 017 question

> Given the same project microstate, explicit task profile, candidate action menu, relation-backed sequencing evidence, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control?

This is a new experiment, not a rescore or repaired rerun of Specification 015.

---

## 3. Frozen conditions

```text
GENERIC
    no reusable methodological assets

SELECTIVE
    accepted Specification 013 task-specific exact revisions

FULL_HORIZON
    all ten exact current accepted Horizon revisions
```

All conditions receive identical:

```text
project evidence
user task
explicit reasoning-function profile
candidate actions
blocked-scope menu
clarification menu
defer-trigger menu
structured result contract
```

---

## 4. Frozen benchmark

Machine-readable authority:

```text
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
```

Four cases:

```text
RB-01  VALIDITY_GATE_AND_SEQUENCE
RB-02  COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE
RB-03  DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION
RB-04  MISSINGNESS_IMBALANCE_DECISION_SEQUENCE
```

Accepted selective sets remain unchanged:

```text
RB-01  prediction-moment + prediction-time-feature-eligibility + temporal-validation
RB-02  random-forest + gradient-boosted-trees
RB-03  histogram + ecdf
RB-04  class-imbalance + missing-data
```

No retrieval, Horizon, or selector redesign is included in this experiment.

---

## 5. Relation-backed disposition contract

Exactly four experiment labels remain:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

The new structured action decision adds:

```text
defer_until_id: string | null
```

Frozen invariants:

```text
DEFER
    action already justified/planned
    + exact supplied unresolved trigger
    + trigger must occur first
    + trigger completion makes action current next work
    + exact defer_until_id required

BLOCKING_REQUIRED / RECOMMENDED / NOT_NOW
    defer_until_id must be null

unknown trigger IDs
    invalid structured response
```

Every Specification 017 expected-DEFER action satisfies this construction prospectively. No ambiguous Specification 015 expected-DEFER action is copied into the new fixture.

---

## 6. Frozen evaluation

Deterministic metrics include:

```text
exact disposition accuracy
critical omissions
under-recommendations
over-recommendations
unnecessary recommended cost
blocking-scope false negatives/positives
required-clarification false negatives/positives
defer-pointer errors
unsupported methodological basis
```

A condition-blinded semantic judge scores only the frozen rubric and may not add obligations.

SELECTIVE absolute gates require:

```text
critical omissions                         0
blocking-scope false negatives             0
unsupported basis failures                 0
defer-pointer errors                        0
required-clarification false negatives     0
aggregate exact disposition accuracy       >= 0.90
every case exact disposition accuracy      >= 0.85
aggregate semantic score                   >= 0.90
every case semantic score                  >= 0.85
```

Relative non-inferiority margins remain:

```text
aggregate exact/semantic vs each control    >= -0.05
per-case exact/semantic vs each control     >= -0.10
```

SELECTIVE may not exceed GENERIC on frozen critical/downside metrics and may not exceed FULL_HORIZON on frozen expansion metrics, as specified in Specification 017 and the fixture.

---

## 7. Frozen positive value signals

At least one preregistered signal is required to claim additional recommendation/action value.

Signals include:

```text
SELECTIVE exact accuracy >= GENERIC + 0.05
SELECTIVE semantic score >= GENERIC + 0.05
fewer critical omissions than GENERIC
fewer blocking false negatives than GENERIC
fewer under-recommendations than GENERIC
fewer clarification false negatives than GENERIC
fewer defer-pointer errors than GENERIC
lower unnecessary recommended cost than FULL_HORIZON
fewer over-recommendations than FULL_HORIZON
fewer blocking false positives than FULL_HORIZON
```

No signal may be added after observing live outputs.

---

## 8. Frozen advancement outcomes

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
    all absolute, relative, and expansion gates pass
    + at least one preregistered positive value signal

SAFE_BUT_NOT_DIFFERENTIATED
    all absolute, relative, and expansion gates pass
    + zero preregistered positive value signals

FAIL
    any frozen absolute, relative, or expansion gate fails
```

A strong GENERIC result that leaves no differentiation is explicitly allowed.

---

## 9. Frozen live treatment and call plan

Reasoner:

```text
OpenAI
OpenAI Agents SDK 0.19.4 behind ADS-owned ReasoningRuntime
gpt-5.6-sol
medium reasoning effort
low verbosity
4000 max output tokens
no tools
no previous-response state
store false where exposed
```

Judge:

```text
same provider/runtime/model
high reasoning effort
low verbosity
4000 max output tokens
condition blinded
```

Call plan:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 judge outputs
72 planned successful provider calls
90 maximum provider attempts
randomization seed 2026082303
one retry per planned call only for frozen infrastructure/structured-output classes
```

The concrete runtime/model treatment remains an experiment constant only.

---

## 10. No live call authorization yet

At this checkpoint:

```text
Specification 017 implementation   NOT YET STARTED
provider-free implementation gate  NOT YET RUN
live workflow                      NOT YET AUTHORIZED
live provider calls                0
```

The exact next task is implementation under the frozen contract.

No live provider call may occur until the exact provider-free implementation head passes ordinary Ubuntu and Windows CI and is preserved in a later pre-live checkpoint.

---

## 11. Promotion audit at freeze

### Research 024

**Decision:** preserve as bounded design rationale.

### Specification 017 v0.1

**Decision:** freeze as experiment authority only.

### `relation_backed_recommendation_action_v1.json`

**Decision:** freeze as evaluator/call-plan truth before implementation.

### Existing Specification 013-016 architecture/results

**Decision:** unchanged.

### Specification 015

**Decision:** unchanged; remains immutable `FAIL` evidence.

### Foundation 018 / 019 / 020

**Decision:** no new Foundation revision at this freeze. Specification 017 tests a bounded downstream consequence of existing relation-oriented and methodological-navigation architecture.

### `DECISIONS.md` / `PRINCIPLES.md`

**Decision:** no new project-level decision or principle yet. Promotion depends on observed Specification 017 evidence.

### Current routing documents

**Decision:** reconcile `README.md`, `CURRENT_STATE.md`, `KNOWLEDGE_MAP.md`, and `OPEN_QUESTIONS.md` to make Specification 017 the active implementation boundary.

---

## 12. Exact continuation

```text
1. implement the experiment-owned relation-backed recommendation result and validator
2. implement frozen fixture/condition construction without modifying evaluator truth
3. implement deterministic action/pointer metrics and blinded judge mechanics
4. implement complete fake-runtime reasoner + judge coverage
5. implement real-persistence provider-free integration coverage
6. add dedicated ordinary Ubuntu/Windows CI with no provider credential
7. preserve the exact green implementation head in the next checkpoint
8. only then expose an explicit secret-gated live workflow
9. make no new live model call before that boundary
```
