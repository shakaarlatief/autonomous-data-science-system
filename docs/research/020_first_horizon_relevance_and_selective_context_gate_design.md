# Research 020: First Horizon Relevance and Selective Context Gate Design

**Date:** 2026-08-22  
**Status:** Current bounded design research for the first RH-C implementation  
**Scope:** Defines the smallest meaningful post-Checkpoint-141 experiment for task-specific relevance filtering and selective methodological context assembly.  
**Authority:** Research rationale only. Specification 013 freezes the executable contract.

## 1. Starting evidence boundary

Checkpoint 141 closes the first explained `MethodologicalHorizon` slice:

```text
accepted-current direct candidates
    -> one-hop governed relation expansion
    -> deterministic applicability/context evaluation
    -> explained included/excluded Horizon
```

Observed cross-platform result:

```text
RH-R  4 / 4 PASS
RH-A  5 / 5 PASS
```

The next unresolved stage in Foundation 019 is no longer candidate retrieval or basic applicability. It is:

```text
APPLICABLE / unresolved Horizon candidates
    -> RELEVANCE / PRIORITIZATION
    -> selective task-specific reasoning context
```

Specification 009 intentionally left RH-C thresholds unfrozen until a real Horizon existed. That prerequisite is now satisfied.

---

## 2. The first RH-C gate should test context reduction before model judgment

Foundation 019 makes relevance semantically rich, and a future LLM may participate in relevance assessment. That does not imply the first relevance implementation should immediately use an LLM judge.

The current ten-asset stress corpus already exposes an explicit, governed signal:

```text
reasoning_functions
```

Examples in the accepted benchmark knowledge include:

```text
MODEL_OPTION
    random-forest
    gradient-boosted-trees

EVIDENCE_OPTION
    histogram
    ecdf

VALIDITY_CONSTRAINT
    temporal-validation
    prediction-time-feature-eligibility

DECISION_FRAMEWORK
    class-imbalance
    missing-data
```

The relation graph also provides explicit support semantics such as:

```text
REQUIRES_CONCEPT
    temporal-validation -> prediction-moment
    prediction-time-feature-eligibility -> prediction-moment
```

This gives a falsifiable minimum-complexity hypothesis:

> Given an already-built Horizon and an explicit task profile naming the reasoning functions needed for the current reasoning step, a deterministic selector can retain primary function matches plus required conceptual support while omitting unrelated Horizon knowledge from the model-facing context.

If this simple policy cannot preserve required revisions while materially shrinking context on the frozen corpus, adding an LLM relevance judge before diagnosing the failure would be premature.

---

## 3. Separate task interpretation from context selection

The first gate should not pretend to solve natural-language task interpretation at the same time.

The selector receives an explicit `MethodologicalContextRequest` containing:

```text
task_id
requested_reasoning_functions
max_assets
```

This profile is an input to the experiment, not a claim that the final system will require humans to supply enum values.

A later system may derive the profile from:

```text
project object semantics
current Question / Investigation / Claim
explicit workflow state
LLM semantic reasoning
a deterministic task mapper
or a hybrid
```

That mapping deserves separate evidence. The first RH-C gate isolates the downstream selection/serialization mechanism.

---

## 4. Deliberately use a wide Horizon stress case

If each RH-C scenario started with only the two relevant assets, selective context assembly would be trivial.

The benchmark should therefore construct the same deliberately wide Horizon from six direct accepted-current seeds:

```text
class-imbalance
histogram
missing-data
prediction-time-feature-eligibility
random-forest
temporal-validation
```

One-hop accepted relation expansion adds:

```text
bagging
ecdf
gradient-boosted-trees
prediction-moment
```

The resulting stress Horizon therefore contains all ten heterogeneous benchmark assets while still preserving the origin distinction between direct candidates and relation-added candidates.

This is intentionally adversarial for context selection. It is **not** a claim that production retrieval should normally return the full catalog.

The point is to test the strongest version of the V0 scaling lesson:

```text
system remembers / Horizon contains 10
    but
current reasoning call receives only 2-3
```

---

## 5. First deterministic relevance policy

### 5.1 Primary task relevance

An included Horizon candidate is a primary match when its accepted-current knowledge revision has at least one `reasoning_function` in the request's `requested_reasoning_functions`.

No fuzzy text score, embedding score, BM25 score, or LLM judgment participates.

### 5.2 Required conceptual support

After primary matches are known, include a relation-added candidate when:

```text
relation_type == REQUIRES_CONCEPT
and
relation_source_key is already selected
```

This is not generic recursive graph expansion. It is bounded support closure over a relation that explicitly declares a required concept and only over candidates already present in the Horizon.

Do not automatically include:

```text
ALTERNATIVE_TO
USES_CONCEPT
COMPLEMENTS
```

unless those candidates independently match the requested reasoning functions.

For example:

```text
MODEL_OPTION
    random-forest
    gradient-boosted-trees

bagging
    stays out unless MECHANISM_EXPLANATION is also requested
```

while:

```text
VALIDITY_CONSTRAINT
    temporal-validation
    prediction-time-feature-eligibility

REQUIRES_CONCEPT support
    prediction-moment
```

### 5.3 No final recommendation claim

A selected item is task-relevant for this bounded context request. It is not thereby `RECOMMENDED`, `REQUIRED`, or `BLOCKING` in the full Foundation 019 sense.

The first gate intentionally stops before recommendation policy.

---

## 6. Preserve relation source provenance

Checkpoint 141 already preserves relation type and relation revision ID, but the first context-support rule also needs to know which direct Horizon candidate produced a relation-added candidate.

The smallest extension is:

```text
HorizonCandidate.relation_source_key
```

For direct candidates it is `None`.

For relation-added candidates it is the stable key of the direct seed whose accepted outbound relation introduced the candidate.

This is an explainability/provenance extension to the accepted one-hop Horizon seam. It does not change relation traversal depth or applicability semantics.

---

## 7. Separate system selection evidence from model-facing context

A critical architectural distinction is:

```text
ContextSelectionResult
    system-facing
    selected candidates
    omitted candidates
    explicit reasons
    budget diagnostics
    size metrics

MethodologicalContextPack
    model-facing methodological context
    selected knowledge only
    exact revisions
    task profile
    aggregate missing-context keys
```

The LLM pack must **not** serialize a list of every omitted global/Horizon candidate merely to explain why each was omitted.

That would recreate the failure mode the selector is intended to prevent.

The system can retain omission explanations for observability/UI without sending them into every reasoning call.

---

## 8. Compact reasoning projection

The context pack should not reuse the retrieval document projection or export the full interchange bundle.

For a selected knowledge revision, a compact reasoning projection may include:

```text
stable_key
revision_id
title
intrinsic_kind
purpose
scope
reasoning_functions
applicability_state
missing_context_keys
context_requirements
semantic_checks
limitations
accepted components
narrative facets
conditional rules
relation provenance when relation-added
```

Traceable accepted component/rule identities should be retained when their content is serialized.

Do not include merely because they exist:

```text
retrieval lexical terms
retrieval aliases
semantic retrieval cues
retrieval scores
asset UUID when stable/revision identity suffices
source locators
provenance source lists
governance event prose
timestamps
collection membership
SQLite / SQLAlchemy details
```

This respects Foundation 020's separation between retrieval signals and reasoning content.

---

## 9. Frozen task classes proposed for RH-C

All four cases use the same wide ten-asset Horizon.

### RH-C01: model-option reasoning

```text
requested function:
    MODEL_OPTION

required exact assets:
    random-forest
    gradient-boosted-trees

expected count:
    2
```

### RH-C02: empirical-distribution evidence

```text
requested function:
    EVIDENCE_OPTION

required exact assets:
    histogram
    ecdf

expected count:
    2
```

### RH-C03: predictive-validity constraints

```text
requested function:
    VALIDITY_CONSTRAINT

primary exact assets:
    temporal-validation
    prediction-time-feature-eligibility

required conceptual support:
    prediction-moment

expected count:
    3
```

This case deliberately leaves `prediction-moment` project context unresolved so the selected pack must preserve the relevant missing-context signal rather than silently dropping the affected validity knowledge.

### RH-C04: data-quality decision frameworks

```text
requested function:
    DECISION_FRAMEWORK

required exact assets:
    class-imbalance
    missing-data

expected count:
    2
```

This case deliberately leaves the framework-specific required project facts unresolved. `MISSING_CONTEXT` is therefore expected to remain visible in the selected methodological context.

---

## 10. Context-size metric should remain provider-neutral

The final LLM model/tokenizer is not selected. A token count from one provider's tokenizer would therefore create false precision and an unnecessary dependency in the first gate.

Use deterministic primary size metrics:

```text
canonical serialized UTF-8 bytes
Unicode character count
selected asset count
```

Compare three conceptual sizes in the benchmark harness:

```text
GLOBAL CONTROL
    compact reasoning projection for all 10 accepted-current assets

FULL HORIZON CONTROL
    compact reasoning projection for all included wide-Horizon assets

SELECTIVE PACK
    only task-selected assets
```

Exact model-token measurement belongs in the later real reasoning vertical slice once a concrete model/tokenizer is part of the evaluated runtime configuration.

---

## 11. Proposed preregistered quality gates

The first selector should have to earn its existence.

Across all RH-C cases require:

```text
exact required-revision coverage     = 1.00
irrelevant selected assets           = 0
selected asset count                 <= 3
selective bytes < full-Horizon bytes for every case
selective/full-Horizon byte ratio    <= 0.65 for every case
```

Also require:

```text
all selected revisions remain current accepted
MISSING_CONTEXT metadata preserved for selected unresolved knowledge
all omitted Horizon candidates receive a system-facing omission reason
omitted candidates absent from the model-facing pack
context retrieval occurs only for exact Horizon candidates, not by global-catalog scan
canonical serialization deterministic
application layer storage-neutral
authoritative knowledge unchanged
Ubuntu + Windows pass
locked V1 regression suite remains green
```

These thresholds are intentionally frozen before implementation/results.

A failure is useful evidence. Do not loosen the byte ratio or expected key sets after observing the first run without preserving the failed result first.

---

## 12. Budget behavior

`max_assets` is a hard upper bound on the model-facing methodological pack.

Deterministic ordering for the first policy should be:

```text
primary function matches before support-only candidates
DIRECT before RELATION within the same relevance class
stable_key ascending as final tie break
```

If relevant candidates exceed the budget, omitted candidates must be reported as:

```text
BUDGET_LIMIT
```

The frozen RH-C quality cases choose `max_assets = 3`, so all required assets should fit if the policy is correct.

Separate unit coverage should still exercise the budget-overflow path.

---

## 13. Failure classes enabled by this gate

The system can now separate:

```text
KNOWN_NOT_RETRIEVED
    upstream retrieval failure

INAPPLICABLE
    explicit applicability failure

MISSING_CONTEXT
    unresolved prerequisite/context

HORIZON_BUT_NOT_TASK_RELEVANT
    selector intentionally omitted candidate

RELEVANT_BUT_BUDGET_OMITTED
    context budget failure

SELECTED_CONTEXT
    exact revision sent to reasoning
```

This is materially more informative than one end-to-end recommendation score.

---

## 14. Non-selections

Do not select from this first RH-C gate:

```text
LLM relevance judge
embedding-based relevance reranker
learned ranker
opaque numeric relevance score
final recommendation policy
REQUIRED/BLOCKING policy
final Horizon size
final context budget for all tasks
provider-specific token budget
production FastEmbed/BGE dependency
permanent production RRF implementation
ANN/vector database
recursive relation expansion
```

The gate tests whether simple explicit task semantics already provide useful context compression.

---

## 15. Advancement rule

If the frozen deterministic selector passes:

```text
1. preserve the result
2. promote the bounded ContextSelectionResult / MethodologicalContextPack seam
3. connect one real reasoning vertical slice through the ADS-owned ReasoningRuntime
4. measure exact model tokens there under the selected concrete model
5. compare reasoning quality with selective context versus a stronger simple control
```

If it fails:

```text
1. preserve the failure
2. classify whether the problem is knowledge metadata, task-profile expressiveness,
   support-closure semantics, budget policy, or serialization
3. only then consider a more flexible semantic/LLM relevance stage
```

Do not add model reasoning merely to hide a deterministic metadata defect.
