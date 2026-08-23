# Checkpoint 147: First Recommendation and Action Value Contract Frozen

**Date:** 2026-08-23  
**Status:** Historical experiment-design checkpoint; Specification 015 v0.1 and recommendation/action benchmark fixture frozen before implementation or live model calls  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the first downstream experiment testing recommendation disposition, REQUIRED/BLOCKING behavior, unnecessary action expansion, and bounded project-action consequences after the accepted real-model selective-context seam.  
**Authority:** Historical preregistration provenance. Specification 015 v0.1 and `recommendation_action_v1.json` govern the first recommendation/action-value implementation until its result is preserved.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-recommendation-action-value`  
**Associated PR:** #13 into `v1-frontend-spike`

## 1. Promoted starting boundary

PR #12 was merged exactly from the validated head into `v1-frontend-spike` at:

```text
bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
```

The current branch starts exactly from that promoted merge:

```text
v1-recommendation-action-value
```

The first design artifact was then preserved in:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
```

before the benchmark fixture and Specification 015 were frozen.

The promoted prerequisite chain already provides:

```text
governed accepted-current reusable methodological knowledge
explained MethodologicalHorizon
three-valued applicability / missing-context behavior
accepted selective exact-revision MethodologicalContextPack
ADS-owned ReasoningRuntime
first real-model selective-context value evidence
```

Specification 014 / Checkpoint 146 observed:

```text
SELECTIVE aggregate semantic quality      1.000000
FULL_HORIZON aggregate semantic quality   1.000000
SELECTIVE/FULL provider input-token ratio 0.334379
aggregate input-token reduction           66.56%
critical-obligation regressions           none
```

The current experiment moves downstream rather than reopening the already-passed context-compression question.

---

## 2. Frozen next question

The next test is:

> Given the same project microstate, explicit task profile, candidate action menu, model/runtime configuration, and evaluation rubric, does the accepted ADS methodological path help a strong reasoner choose and calibrate the right methodological actions, preserve blocking dependencies, and avoid unnecessary work relative to strong simpler controls?

The methodological progression under test is:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> PROJECT ACTION
```

This is the first explicit test of the Foundation 019 distinction that REQUIRED/BLOCKING is a validity/dependency status rather than simply a stronger recommendation.

---

## 3. Frozen three-condition design

### GENERIC

```text
same project evidence
same user task
same explicit reasoning-function profile
same bounded candidate action menu
same blocked-scope / clarification menus
same structured output contract
no reusable methodological knowledge assets
```

This is the principal simple-control condition for whether explicit ADS methodological knowledge adds recommendation/action value beyond a strong model with the same project evidence and task profile.

### SELECTIVE

```text
accepted Specification 013 exact-revision MethodologicalContextPack
same task/project/action envelope
```

This is the principal ADS treatment.

### FULL_HORIZON

```text
all ten exact current accepted Horizon revisions
same compact reasoning projection
same task/project/action envelope
```

This control tests whether wider context rescues an important concern omitted by SELECTIVE or instead creates unnecessary recommendation/action expansion.

The reasoner does not receive the condition label.

---

## 4. Frozen benchmark disposition semantics

Every candidate action receives exactly one of:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

Frozen meanings:

```text
BLOCKING_REQUIRED
    necessary before one or more named downstream scopes can be defended

RECOMMENDED
    worth doing now for the stated current objective, but not a named blocker

DEFER
    potentially relevant/useful, but should wait for a current dependency or priority

NOT_NOW
    no material current justification from the frozen project evidence/objective
```

These labels are benchmark semantics only. They are not promoted as the final production recommendation enum.

---

## 5. Frozen bounded action menu

The first recommendation experiment freezes a candidate action menu for every project microstate.

Reason:

```text
hold action discovery constant
    -> make recommendation calibration deterministic
    -> measure omission / over-recommendation / blocking directly
```

The reasoner may not invent action IDs in this gate.

The model-facing menu contains only:

```text
action_id
label
cost_units
```

Evaluator truth remains hidden:

```text
expected_disposition
critical
expected blocked scopes
expected clarification IDs
```

Open-world proposal generation remains a later experiment.

---

## 6. Frozen project microstates

Fixture:

```text
tests/fixtures/reasoning/recommendation_action_v1.json
```

Cases:

```text
RA-01 VALIDITY_GATE
    prediction moment unresolved
    post-outcome feature timing
    random-across-time split under future deployment
    model comparison requested prematurely

RA-02 MODEL_CHOICE
    validity gates already resolved
    compact nonlinear shortlist requested
    Random Forest + Gradient-Boosted Trees are current model options

RA-03 EVIDENCE_PLAN
    quantitative right-skewed distribution question
    Histogram + ECDF are current complementary evidence options
    unrelated modeling/validation work is not current priority

RA-04 MISSINGNESS_IMBALANCE
    approximately 6% positive class
    high-value variables with training missingness
    production missingness unresolved
    preprocessing/model-selection claims proposed prematurely
```

Required SELECTIVE sets:

```text
RA-01
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

RA-02
    gradient-boosted-trees
    random-forest

RA-03
    ecdf
    histogram

RA-04
    class-imbalance
    missing-data
```

The fixture is authoritative for exact project evidence, user tasks, action menus, action costs, expected dispositions, blocked scopes, clarification menus, and semantic obligations.

---

## 7. Frozen ADS-owned result direction

The reasoner output is frozen conceptually as:

```text
RecommendationActionResult
    summary
    action_decisions[]
        action_id
        disposition
        rationale
    blocked_scopes[]
    required_clarification_ids[]
    warnings[]
    methodological_basis[]
```

Every candidate action must appear exactly once.

Invalid structured output includes:

```text
unknown action ID
duplicate action ID
missing candidate action
unknown disposition
blocked scope outside supplied menu
clarification ID outside supplied menu
unsupported methodological basis
```

For GENERIC:

```text
methodological_basis == []
```

For SELECTIVE/FULL_HORIZON:

```text
methodological_basis subset of supplied stable keys
```

This is an experiment/application result. It does not yet create authoritative `Proposal`, `Question`, `Investigation`, or `Decision` objects.

---

## 8. Frozen deterministic recommendation metrics

Primary exact metrics:

```text
exact disposition accuracy
critical action omissions
under-recommendations
over-recommendations
unnecessary recommended cost units
blocking-scope false negatives
blocking-scope false positives
required-clarification false negatives
unsupported methodological-basis references
```

Definitions are frozen in Specification 015 and the fixture.

The semantic judge remains secondary and evaluates rationale/dependency correctness, unresolved-context handling, and contradictions with project evidence.

This split follows P-004: exact recommendation behavior is evaluated deterministically rather than delegated to an LLM judge when exact evaluator truth exists.

---

## 9. Frozen absolute SELECTIVE gates

Require:

```text
critical action omissions                   == 0
blocking-scope false negatives              == 0
unsupported methodological-basis failures   == 0
aggregate exact disposition accuracy        >= 0.90
every case mean exact accuracy              >= 0.80
aggregate normalized semantic score         >= 0.90
every case mean semantic score              >= 0.85
```

These are bounded benchmark thresholds, not production service-level targets.

---

## 10. Frozen relative gates

SELECTIVE must remain close to both strong controls.

Exact disposition accuracy:

```text
aggregate SELECTIVE >= GENERIC - 0.05
every case SELECTIVE >= GENERIC - 0.10

aggregate SELECTIVE >= FULL_HORIZON - 0.05
every case SELECTIVE >= FULL_HORIZON - 0.10
```

Semantic quality:

```text
aggregate SELECTIVE >= GENERIC - 0.05
every case SELECTIVE >= GENERIC - 0.10

aggregate SELECTIVE >= FULL_HORIZON - 0.05
every case SELECTIVE >= FULL_HORIZON - 0.10
```

Also require:

```text
SELECTIVE critical omissions <= GENERIC critical omissions
SELECTIVE under-recommendations <= GENERIC under-recommendations
```

No formal statistical non-inferiority claim is permitted.

---

## 11. Frozen expansion gates

Against FULL_HORIZON require:

```text
SELECTIVE unnecessary recommended cost
    <= FULL_HORIZON unnecessary recommended cost

SELECTIVE over-recommendations
    <= FULL_HORIZON over-recommendations

SELECTIVE blocking-scope false positives
    <= FULL_HORIZON blocking-scope false positives
```

Equality passes the safety/expansion gate but does not establish additional SELECTIVE value.

---

## 12. Frozen positive-value requirement

To claim additional recommendation/action value rather than merely safety, at least one preregistered signal must be strictly positive:

```text
SELECTIVE aggregate exact accuracy >= GENERIC + 0.05

or

SELECTIVE total critical omissions < GENERIC

or

SELECTIVE total under-recommendations < GENERIC

or

SELECTIVE total unnecessary recommended cost < FULL_HORIZON

or

SELECTIVE total over-recommendations < FULL_HORIZON

or

SELECTIVE total blocking-scope false positives < FULL_HORIZON
```

This rule is important because a three-way ceiling result must not be reinterpreted after the fact as evidence that the more explicit mechanism added value.

---

## 13. Frozen advancement classification

Exactly one result class must be emitted.

### PROMOTE_BOUNDED_RECOMMENDATION_SEAM

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
>= 1 positive-value signal
all technical invariants pass
complete scored design obtained
```

### SAFE_BUT_NOT_DIFFERENTIATED

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
0 positive-value signals
all technical invariants pass
complete scored design obtained
```

### FAIL

Any absolute, relative, expansion, technical, or completeness gate fails.

The failed result must be preserved before changing the treatment.

---

## 14. Frozen model/runtime treatment

Reasoner:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents==0.19.4
gpt-5.6-sol
reasoning effort = medium
text verbosity = low
max output tokens = 4000
no tools
no previous-response state
no fast/priority request
```

Judge:

```text
gpt-5.6-sol
reasoning effort = high
text verbosity = low
max output tokens = 4000
one condition-blinded judge call per successful reasoner output
no tools
```

The concrete model configuration remains an experiment treatment constant, not a final provider/model decision.

---

## 15. Frozen call plan and retry boundary

```text
4 cases
3 conditions
3 repetitions
= 36 reasoner outputs

1 blinded judge call per successful reasoner output
= 36 judge outputs

planned successful provider calls = 72
```

Randomization seed:

```text
20260823
```

Maximum provider attempts:

```text
90
```

One retry maximum per planned call only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic quality, incorrect recommendation, or failed evaluation gates are never retry reasons.

All attempts are preserved.

---

## 16. Frozen technical boundaries

Before any live call the implementation must prove provider-free:

```text
same case/task/action evidence across conditions
expected evaluator truth absent from model payloads
exact SELECTIVE stable-key sets
exact ten-revision FULL_HORIZON
GENERIC contains no reusable methodological assets
same model/runtime configuration
no tools
no cross-call state
condition label absent from reasoner content
strict structured action coverage
basis provenance
judge blinding
deterministic evaluator
deterministic reasoner/judge plan hashes
exact context/revision transparency
no authoritative project mutation
ADS/provider runtime isolation
ordinary CI contains no live API key
Ubuntu + Windows provider-free passage
```

No live workflow should exist as an automatic PR trigger.

---

## 17. Explicit non-selections

This checkpoint does not select:

```text
natural-language/project-state task-profile derivation
open-world proposal generation
final production recommendation enum
final recommendation ranking model
complete Foundation 018 production schema
authoritative Proposal/Question/Decision mutation
automatic execution
human approval/escalation policy
admissibility/risk policy
final model/provider
multi-agent recommendation review
production semantic retrieval/reranking/vector infrastructure
frontend/Cockpit wiring
```

---

## 18. Exact continuation

```text
1. route the repository to Checkpoint 147 / Specification 015 / PR #13
2. implement ADS-owned recommendation result types provider-free
3. implement exact evaluator and three condition builders
4. implement deterministic reasoner/judge plans and fake-runtime tests
5. add ordinary Ubuntu/Windows provider-free workflow coverage
6. validate the exact implementation head
7. only then create/use the explicit secret-gated live execution boundary
8. preserve the full result before any tuning
```

No live Specification 015 model call has occurred at this checkpoint.

Primary sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
```

---

## 19. Promotion audit

### Promote

The frozen experiment contract itself should become the active V1 evidence route:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
```

Repository routing should identify PR #13 as the active implementation/evaluation branch after the promoted Specification 014 seam.

### Do not promote

No recommendation/action quality conclusion, final recommendation taxonomy, project-state mutation policy, human-control policy, provider/model selection, task-profile derivation mechanism, or richer retrieval mechanism is promoted by this freeze.

Reason: Checkpoint 147 is preregistration only. No provider-free implementation result or live recommendation result exists yet.

### Preserve the distinction between experiment routing and product semantics

The branch is authorized to implement and test the bounded recommendation/action result seam. It is not authorized to silently turn benchmark-specific labels or candidate-menu design into the final Project Cockpit/product model.
