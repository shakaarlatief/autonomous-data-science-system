# Research 022: First Recommendation and Action Value Vertical Slice Design

**Date:** 2026-08-23  
**Status:** Bounded design rationale before Specification 015 freeze and before recommendation/action implementation or live model calls  
**Scope:** First downstream test of methodological recommendation strength, blocking dependencies, unnecessary action expansion, and bounded project-action consequences after the accepted Specification 014 real-reasoning result  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting point

PR #12 was merged into `v1-frontend-spike` at:

```text
bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
```

That merge promotes the first bounded real-model evidence for:

```text
explained MethodologicalHorizon
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
```

Specification 014 / Checkpoint 146 observed identical frozen semantic quality under SELECTIVE and FULL_HORIZON while SELECTIVE used an aggregate provider input-token ratio of `0.334379`, a `66.56%` reduction.

The next legitimate question is therefore no longer whether the accepted selective pack can be materially smaller while preserving the first simple reasoning obligations. The next missing layer is the one that the product actually needs in order to guide a project:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> PROPOSED PROJECT ACTION
```

Foundation 019 explicitly distinguishes recommendation from applicability/relevance and states that REQUIRED/BLOCKING is not merely a stronger recommendation. Foundation 018 separately defines project-level `Proposal`, `Investigation`, `Run`, `Evidence`, and `Decision` concepts.

The first recommendation/action experiment should test this boundary without prematurely implementing the complete production project-object lifecycle.

---

## 2. Why the next slice should not return to retrieval tuning

The current bounded chain already has evidence for:

```text
lexical retrieval
semantic-channel complementarity
hybrid retrieval comparator
explained one-hop MethodologicalHorizon
three-valued applicability / missing context
selective exact-revision context
real-model selective-context value
```

There are still open retrieval and semantic-relevance questions at production scale, but no current downstream failure requires another retrieval mechanism.

Adding a reranker, LLM relevance judge, ANN index, larger embedding system, or more elaborate selector before observing a recommendation/action deficiency would violate the project's complexity discipline.

The next experiment should make a new failure mode observable instead:

```text
known and relevant concern
    but recommendation too weak

known and relevant concern
    but recommendation too strong

required dependency omitted

required dependency identified
    but downstream action not blocked

low-value action recommended anyway

important action deferred incorrectly
```

These are closer to the behavior a future Project Cockpit must expose to the user.

---

## 3. What exactly should be tested

The frozen question should be:

> Given the same project microstate, explicit task profile, candidate action menu, model/runtime configuration, and evaluation rubric, does the accepted ADS methodological path help a strong reasoner choose and calibrate the right methodological actions, preserve blocking dependencies, and avoid unnecessary work relative to strong simpler controls?

This is deliberately narrower than a full autonomous project.

The experiment should test:

```text
recommendation disposition
    BLOCKING_REQUIRED
    RECOMMENDED
    DEFER
    NOT_NOW

blocking scope
    which downstream claims/decisions cannot yet be defended

required clarification
    when unresolved context must be requested rather than assumed

methodological basis
    which supplied exact knowledge revisions support the recommendation

unnecessary expansion
    whether extra context causes more low-value work to be recommended
```

The four disposition labels are benchmark labels for this slice, not a final production enum.

---

## 4. Why use a bounded candidate action menu

The long-term system should remain open-world. It should be able to propose an important action that was not pre-enumerated.

That is not the right first recommendation experiment.

If the reasoner may invent arbitrary actions while recommendation strength, context condition, project consequences, and semantic scoring all change simultaneously, attribution becomes weak.

The first slice should therefore freeze a candidate action menu per project microstate and ask every condition to classify the same actions.

This gives exact deterministic measures for:

```text
critical omission
under-recommendation
over-recommendation
premature downstream action
unnecessary action cost
blocking-scope false negative
blocking-scope false positive
```

Open-world proposal generation remains an explicit later question.

---

## 5. Three conditions are more informative than another two-condition context test

The next experiment should use three conditions.

### GENERIC

A strong reasoner receives:

```text
same user task
same project evidence
same explicit requested reasoning functions
same candidate action menu
same structured recommendation schema
no reusable methodological knowledge assets
```

This is the strongest simple control for the question:

> Does explicit methodological knowledge/navigation add downstream recommendation value beyond a strong model that already sees the project state and the same bounded task profile?

### SELECTIVE

The reasoner receives the accepted Specification 013 selective exact-revision pack.

This is the main ADS treatment.

### FULL_HORIZON

The reasoner receives all ten exact current accepted assets from the same explained Horizon using the same compact projection.

This is not included to repeat Specification 014's token experiment. It tests the downstream possibility that broader context causes unnecessary recommendation expansion or, conversely, rescues an important concern omitted by SELECTIVE.

The main comparisons are therefore:

```text
SELECTIVE versus GENERIC
    system-value comparison

SELECTIVE versus FULL_HORIZON
    omission / expansion comparison
```

Provider token usage remains recorded but is not the main advancement gate in this slice.

---

## 6. Keep task-profile derivation out of scope for attribution

A major unresolved production question is:

```text
project state / natural language
    -> requested reasoning functions
```

That should not be mixed into the first recommendation-value experiment.

The benchmark should freeze the same explicit reasoning-function profile for all three conditions. This keeps the experiment focused on what happens after the task profile is known.

If SELECTIVE fails under a correct frozen task profile, the failure belongs downstream of task-profile derivation. If it succeeds, a later experiment can test whether ADS can derive the profile robustly from project objects and user intent.

---

## 7. Four project microstates

The benchmark should deliberately reuse the four accepted selective-context classes while making their downstream action consequences harder.

### RA-01: VALIDITY_GATE

Project situation:

```text
binary churn prediction
future monthly deployment
prediction moment not formally established
one candidate feature appears after the outcome
current evaluation uses random row splitting across time
user wants to compare nonlinear models immediately
```

The correct behavior should place prediction timing, feature eligibility, and temporal validation in `BLOCKING_REQUIRED` status and defer model comparison until those validity gates are resolved.

This case tests:

```text
critical omission
blocking scope
premature model action
required clarification
```

### RA-02: MODEL_CHOICE

Project situation:

```text
valid temporal evaluation design already locked
prediction-time feature availability already verified
moderate-size tabular binary classification
nonlinear interactions plausible
simple linear baseline already exists
user wants a compact nonlinear shortlist
```

The correct behavior should recommend Random Forest and Gradient Boosted Trees under the same locked evaluation design while avoiding reopening already-resolved validity work or expanding automatically into every related ensemble method.

This case tests:

```text
useful model recommendations
redundancy / unnecessary expansion
respect for already-resolved project state
```

### RA-03: EVIDENCE_PLAN

Project situation:

```text
one continuous variable is strongly right-skewed with extreme values
missingness has already been verified absent
current question is distribution understanding before deciding transformation/capping
no model choice is requested yet
```

The correct behavior should recommend Histogram and ECDF as complementary evidence and keep unrelated modeling/validation/missingness work out of the current action set.

This case tests:

```text
expected information value
bounded evidence planning
low-cost complementary methods
avoidance of method-first expansion
```

### RA-04: MISSINGNESS_IMBALANCE

Project situation:

```text
binary classification with approximately 6% positives
valid evaluation split already established
two high-value variables have substantial training missingness
production/serving missingness behavior is unknown
current proposal is to lock median imputation and a metric plan before comparing models
```

The correct behavior should block the preprocessing lock until missingness is characterized, require an imbalance-aware evaluation plan before model-selection claims, defer model comparison until those decisions are defensible, and avoid blindly accepting median imputation merely because it is simple.

This case tests:

```text
multiple interacting decision frameworks
missing-context handling
required versus recommended calibration
blocking of premature project decisions
```

---

## 8. Recommendation output should be structured but not yet persisted as full project state

Foundation 018 defines `Proposal` as a candidate action/analysis/clarification/decision and makes it a natural eventual project object.

The first experiment should not yet mutate authoritative project state or claim that the production Proposal schema is finalized.

Instead, establish a provider-neutral application result such as:

```text
RecommendationActionResult
    summary
    action_decisions[]
        action_id
        disposition
        rationale
    blocked_scopes[]
    required_clarifications[]
    warnings[]
    methodological_basis[]
```

The experiment can then deterministically evaluate the recommendation bundle against the frozen project microstate.

If this seam earns continuation, a later production slice can map accepted recommendation results into durable Foundation 018 objects/events such as:

```text
ProposalCreated
QuestionOpened
ProposalAccepted
InvestigationStarted
DecisionChanged
```

This ordering avoids prematurely freezing the full project mutation model before recommendation behavior itself has evidence.

---

## 9. Deterministic action metrics should carry more weight than an LLM judge

The first real reasoning experiment used a blinded semantic judge because its obligations were mostly semantic.

Recommendation/action evaluation has more exact structure.

For every output the harness can deterministically compute:

```text
exact disposition accuracy
critical action omissions
under-recommendation count
over-recommendation count
unnecessary recommended cost units
blocking-scope false negatives
blocking-scope false positives
unsupported methodological-basis references
```

These should be primary.

A condition-blinded semantic judge remains useful for:

```text
whether the rationale is methodologically correct
whether dependencies are explained correctly
whether required clarification is justified
whether the answer contradicts the frozen project evidence
```

This preserves P-004: use deterministic evidence where the question is exactly testable and LLM judgment where genuine semantic interpretation remains.

---

## 10. Avoid one opaque utility score

Foundation 019 already warns against one opaque recommendation score as the product abstraction. The evaluation should follow the same discipline.

Do not collapse everything immediately into one arbitrary scalar.

Report separate metrics for:

```text
critical safety / validity
recommendation calibration
action burden
blocking behavior
semantic rationale quality
provider resource use
```

A weighted disposition-accuracy summary may be useful, but the advancement rule should remain interpretable in terms of the underlying failure modes.

---

## 11. Strong advancement logic should allow an informative no-differentiation result

A strong model may solve the bounded benchmark without explicit methodology. If so, the correct conclusion is not to invent a benefit.

The frozen outcome classes should distinguish:

```text
PROMOTE_BOUNDED_RECOMMENDATION_SEAM
    SELECTIVE meets absolute safety/quality gates,
    is non-inferior to GENERIC on the frozen recommendation metrics,
    is no more expansion-prone than FULL_HORIZON,
    and shows at least one preregistered downstream value signal

SAFE_BUT_NOT_DIFFERENTIATED
    SELECTIVE meets absolute gates and does not materially regress,
    but the benchmark does not show an additional recommendation/action value signal

FAIL
    critical omission, blocking failure, material recommendation regression,
    unsupported basis, or other frozen gate failure
```

This prevents another ceiling result from being overinterpreted.

---

## 12. What should count as a downstream value signal

Before observing live outputs, freeze the acceptable value signals.

Examples:

```text
higher exact disposition accuracy than GENERIC
fewer critical omissions than GENERIC
fewer under-recommendations than GENERIC
lower unnecessary recommended cost than FULL_HORIZON
fewer over-recommendations than FULL_HORIZON
fewer blocking-scope false positives than FULL_HORIZON
```

At least one such signal should be strictly better for a result to claim additional bounded recommendation/action value.

Matching all controls perfectly is still useful evidence of safety, but not evidence that the more explicit recommendation mechanism itself added value on that benchmark.

---

## 13. Reuse the same model/runtime treatment initially

To keep the architectural comparison interpretable, use the same concrete reasoner and judge configuration as Specification 014 unless implementation evidence forces a documented change before freeze:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents==0.19.4
gpt-5.6-sol
reasoner reasoning effort medium
judge reasoning effort high
no tools
no previous-response state
```

This is still not a final provider/model selection.

Changing the model at the same time as changing the task would make it harder to attribute differences to the new recommendation/action layer.

---

## 14. Repetitions and call budget

A reasonable frozen design is:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
```

Use deterministic condition randomization inside each case/repetition block and independently randomized judge order.

Allow at most one retry for infrastructure/structured-output failure classes, never for semantic quality.

A maximum of `90` total provider attempts gives bounded retry room without allowing repeated sampling until success.

---

## 15. Explicit non-goals

This slice should not attempt to solve:

```text
natural-language project state -> reasoning-function derivation
open-world free-form proposal discovery
complete Foundation 018 persistence schema
automatic execution of accepted proposals
human approval policy
final recommendation enum or priority model
final REQUIRED/BLOCKING production policy
risk/admissibility policy
multi-agent recommendation review
production semantic retrieval stack
frontend/Cockpit wiring
```

Those become better-defined after the recommendation behavior itself has measurable evidence.

---

## 16. Recommended implementation sequence after freeze

If Specification 015 accepts this design, implementation should proceed in the following order:

```text
1. freeze benchmark fixture and exact action/consequence expectations
2. freeze RecommendationActionResult and condition construction
3. build deterministic recommendation evaluator
4. add fake-runtime unit/integration tests
5. add GENERIC / SELECTIVE / FULL_HORIZON provider-free harness
6. validate ordinary CI with no live key
7. add explicit secret-gated live workflow
8. validate the exact pre-live head
9. execute the frozen live plan once
10. preserve raw result before any tuning
```

No live provider call should occur before the Specification 015 contract and freeze checkpoint exist.
