# Research 026: System-Owned Provenance Recommendation and Action Value Design

**Date:** 2026-08-23  
**Status:** Bounded design rationale after Specification 017 incomplete execution and Specification 018 promotion, before Specification 019 freeze, implementation, or live model calls  
**Scope:** Define the smallest prospective recommendation/action-value experiment that preserves Specification 017's scientific question and evaluator truth while correcting only the identified provenance instrumentation boundary.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

The active branch starts from the canonical Specification 018 integration state:

```text
v1-recommendation-action-value-system-provenance
base integration head  ecf37585f576a3c4fd84a884dee4650b52ab1519
Specification 018 merge 9fd2243c38a8f0f010396847f519e115d30b8f58
```

The immediately relevant evidence is deliberately asymmetric.

Specification 016 established a bounded construct result:

```text
DEFER-like sequencing
    requires a concrete represented activating dependency
    when deterministic separation from NOT_NOW is expected
```

Specification 017 then prospectively rebuilt its four recommendation/action microstates around that stronger relation-backed construction. Its first live run did not complete the matched comparison:

```text
planned reasoner outputs     36
successful reasoner outputs  29
successful judge outputs     29
SELECTIVE completed          12 / 12
FULL_HORIZON completed       12 / 12
GENERIC completed             5 / 12
complete scored design       false
advancement outcome          none
```

All 19 failed reasoner attempts were GENERIC `INVALID_STRUCTURED_RESPONSE` events. They repeatedly placed the requested reasoning-function label into `methodological_basis` even though GENERIC supplied no reusable methodological revisions.

The stable observed boundary was:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

Specification 017 remains immutable incomplete evidence. Its partial condition scores are not advancement evidence and must not be used to alter case truth, thresholds, value signals, or treatment semantics.

Specification 018 now supplies the separate governed control plane needed to launch a future frozen live experiment without a manual Actions UI step. That capability changes experiment transport, not scientific treatment.

---

## 2. The next question should remain the Specification 017 system-value question

The unresolved scientific question is still:

> Given the same project microstate, explicit task profile, candidate action menu, relation-backed sequencing evidence, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control?

A new experiment is justified because Specification 017 never produced the complete matched design required to answer that question.

The next experiment must not quietly become a different benchmark merely because an instrumentation flaw was found.

Therefore the default rule is:

```text
preserve scientific truth
change only provenance ownership and the structured-output dependency on it
```

---

## 3. Preserve the Specification 017 benchmark by reference, not by rewriting it

The strongest protection against accidental post-hoc tuning is to make the next machine-readable fixture an explicit overlay on the immutable Specification 017 fixture rather than copying and editing all four cases.

Immutable base:

```text
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
Git blob SHA eac949c47a01878dcc47dcca1116493a02ba9805
```

The new fixture should fail closed unless the base file still has that exact Git blob identity.

The following Specification 017 elements should be inherited without change:

```text
four case project microstates
candidate action menus
expected disposition truth
expected defer-trigger pointers
blocked-scope menus and truth
clarification menus and truth
cost units
semantic judge obligations
GENERIC / SELECTIVE / FULL_HORIZON conditions
SELECTIVE exact stable-key sets
FULL_HORIZON ten-asset construction
absolute accuracy / omission / pointer / clarification gates
relative non-inferiority margins
expansion gates
positive value signals
allowed advancement outcomes
reasoner model/runtime treatment
judge model/runtime treatment
3 repetitions per case/condition
72 planned successful provider calls
90 maximum provider attempts
retry failure classes
```

No partial Specification 017 output may influence any inherited value.

---

## 4. Change provenance ownership, not methodological treatment

The next experiment should make exact supplied methodological provenance a deterministic system trace.

Before a reasoner request is sent, the harness already knows:

```text
condition
exact supplied methodological payload
exact stable_key@revision_id identities
serialized compact context bytes
accepted-current knowledge snapshot
```

Those facts should be recorded by the system rather than requested back from the model.

Proposed system-owned trace:

```text
SystemContextProvenance
    condition
    supplied_revisions[]
        stable_key
        revision_id
    methodology_payload_sha256
    methodology_payload_bytes
```

For GENERIC:

```text
supplied_revisions = []
methodology payload = canonical empty-methodology payload
```

For SELECTIVE and FULL_HORIZON, the revision pointers must be derived from the exact payload actually supplied to the reasoner, never from the model result.

The trace must be frozen before provider execution and preserved with every attempt/outcome record.

---

## 5. Remove authoritative provenance from the model-owned result

The next experiment-owned model result should contain recommendation content only:

```text
SystemProvenanceRecommendationActionResult
    summary
    action_decisions[]
        action_id
        disposition
        defer_until_id
        rationale
    blocked_scopes[]
    required_clarification_ids[]
    warnings[]
```

It should not contain `methodological_basis`.

This is not a relaxation of scientific reasoning quality. The blinded judge still evaluates whether the reasoning is methodologically correct against the frozen project evidence and rubric.

It is a correction of ownership:

```text
SYSTEM owns what context was supplied.
MODEL owns what recommendation it makes from the supplied situation.
```

If a future product needs model-authored knowledge citations, that should be a separate optional capability with an explicit supplied-ID menu and an independent value test. It should not be the authoritative provenance channel and should not determine whether a recommendation output is structurally valid.

---

## 6. Preserve GENERIC as a genuinely strong control

GENERIC must continue to receive:

```text
same system instruction
same user task
same project evidence
same requested reasoning functions
same candidate action menu
same blocked-scope menu
same clarification menu
same defer-trigger menu
same recommendation result schema
no reusable methodological assets
```

The requested reasoning-function label remains part of the task profile. It must not be interpreted as reusable-knowledge provenance.

GENERIC system-owned methodological provenance is deterministically empty.

A strong model is still allowed to solve the benchmark from general reasoning. The experiment must not manufacture an advantage for SELECTIVE.

---

## 7. Preserve SELECTIVE and FULL_HORIZON unchanged

SELECTIVE should receive the exact accepted Specification 013 context sets inherited from Specification 017:

```text
RB-01  prediction-moment, prediction-time-feature-eligibility, temporal-validation
RB-02  gradient-boosted-trees, random-forest
RB-03  histogram, ecdf
RB-04  class-imbalance, missing-data
```

FULL_HORIZON should receive all ten exact accepted-current revisions using the same compact reasoning projection.

No retrieval, dense model, fusion, Horizon, selector, max-assets, or context-rendering change is justified by the Specification 017 failure.

---

## 8. Keep recommendation evaluation unchanged except for the obsolete provenance metric

The deterministic recommendation metrics should remain:

```text
exact disposition accuracy
critical action omissions
under-recommendations
over-recommendations
unnecessary recommended cost
blocking-scope false negatives
blocking-scope false positives
required-clarification false negatives
required-clarification false positives
defer-pointer errors
```

Specification 017's `unsupported_methodological_basis_failures` is no longer a recommendation metric because the model no longer owns that field.

It should be replaced by technical provenance invariants that are evaluated before or independently of semantic recommendation scoring:

```text
system provenance exactly matches supplied payload
GENERIC provenance has zero supplied revisions
SELECTIVE provenance matches the selected exact revisions
FULL_HORIZON provenance contains all ten exact revisions
payload digest recomputes exactly
provenance is unchanged by model output
```

A provenance-integrity failure should invalidate the experiment execution rather than count as a model recommendation error.

---

## 9. Preserve the judge and promotion logic

The condition-blinded semantic judge should receive the same project/task/action/trigger/rubric evidence and candidate recommendation content as Specification 017, but no system provenance or condition identity.

The judge still scores each frozen obligation 0/1/2 and may not add obligations.

The Specification 017 positive value signals should be inherited unchanged. In particular, do not add a new signal merely because the provenance repair is expected to improve structured-output completion.

Allowed complete-design outcomes should remain semantically equivalent:

```text
PROMOTE_SYSTEM_PROVENANCE_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

The promotion name may change to identify the new experiment, but its gate logic should remain the Specification 017 logic after removal of the obsolete model-authored-basis gate.

An incomplete scored design should again produce no advancement classification.

---

## 10. Preserve the runtime treatment and call budget

For clean attribution, retain:

```text
reasoner
    OpenAI
    OpenAI Agents SDK 0.19.4 behind ADS-owned ReasoningRuntime
    gpt-5.6-sol
    reasoning effort medium
    text verbosity low
    max output tokens 4000
    no tools
    no previous response state

judge
    same provider/runtime/model
    reasoning effort high
    text verbosity low
    max output tokens 4000
    no tools
    condition blinded
```

Use a new deterministic randomization seed because this is a new prospective experiment.

Proposed frozen seed:

```text
2026082304
```

Call plan should remain:

```text
4 cases
3 conditions
3 repetitions
36 planned successful reasoner calls
36 planned successful judge calls
72 planned successful provider calls
90 maximum provider attempts
one retry per planned call only for the same frozen transport/provider/incomplete/invalid-structured failure classes
```

Semantic disagreement remains non-retryable.

---

## 11. Make completion itself an explicit instrumentation diagnostic

Specification 017 failed before its scientific comparison because model-owned provenance made GENERIC structurally fragile.

The next experiment should report, but not use as a promotion value signal:

```text
structured-output completion by condition
retry count by condition
invalid-structured-response count by condition
```

A complete design is required before any scientific advancement outcome is evaluated.

If the provenance repair still fails to produce a complete design, that is new control/instrumentation evidence and should be preserved before further changes.

---

## 12. Provider plan serialization and trace integrity

Before the first provider call, the runner should persist and hash:

```text
reasoner plan
judge plan
accepted knowledge snapshot
all 36 system-owned provenance records
```

The plan must bind each reasoner output ID to:

```text
case
condition
repetition
nonce
exact context payload digest
exact supplied revision pointers
```

The judge plan remains independently shuffled and condition blinded.

Provider attempts must never be able to alter the frozen plan or provenance record for a planned output.

---

## 13. Governed launch through Specification 018

The new live experiment should be the first provider-backed experiment intentionally launched through the accepted Specification 018 control plane.

The launch authorization must be added only after:

```text
Research 026 frozen
Specification 019 frozen
new fixture frozen
contract checkpoint frozen
implementation complete
exact Ubuntu/Windows provider-free CI green
exact live source SHA frozen
```

The repository-controlled authorization must contain the exact live workflow, branch, source SHA, confirmation token, and required successful CI run IDs.

The launcher still receives no provider credential. The target live workflow remains the only workflow allowed to consume the provider secret and must independently verify its exact source SHA and confirmation.

---

## 14. What would count as a legitimate result

### Complete design and all gates pass with at least one inherited positive value signal

This may support a bounded production-facing recommendation result seam whose provenance is system-owned.

### Complete design and all gates pass with no positive signal

This is informative `SAFE_BUT_NOT_DIFFERENTIATED` evidence. It would suggest that the explicit methodological treatment is safe on this benchmark but has not demonstrated marginal recommendation value over the strong generic reasoner.

### Complete design and a gate fails

This is `FAIL`. Preserve the result and attribute the failure before another attempt.

### Incomplete design

No advancement classification. Preserve the evidence and diagnose the instrumentation or provider boundary prospectively.

---

## 15. Explicit non-goals

This experiment does not establish:

```text
final production disposition enums
final recommendation ranking or priority policy
natural-language/project-state -> reasoning-function derivation
open-world action generation
complete dependency persistence
mapping recommendations into authoritative Foundation 018 objects/events
automatic project execution
human approval/escalation policy
final provider/model
multi-agent recommendation architecture
final frontend/Cockpit wiring
```

It also does not test whether model-authored methodological citations are valuable. That is a separate possible future question.

---

## 16. Recommended next freeze

Freeze a new Specification 019 and overlay fixture with the following exact design rule:

```text
Specification 017 scientific benchmark truth is inherited unchanged.
Only provenance ownership and model-output schema dependence are changed.
```

Then record the frozen boundary in Checkpoint 163 before any implementation work or provider call.
