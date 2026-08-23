# Specification 015: V1 Recommendation and Action Value Vertical Slice

**Version:** 0.1  
**Date:** 2026-08-23  
**Status:** Frozen bounded implementation/evaluation contract before recommendation/action implementation and live model calls  
**Scope:** First downstream comparison of recommendation disposition, blocking dependencies, unnecessary action expansion, and bounded action consequences across GENERIC, accepted SELECTIVE, and compact FULL_HORIZON methodological conditions.  
**Authority:** Governs the first recommendation/action-value implementation and live experiment until its result is preserved. It does not finalize production recommendation enums, task-profile derivation, open-world proposal generation, Foundation 018 project-state persistence, human approval policy, automatic execution, risk/admissibility policy, final provider/model, or multi-agent architecture.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

PR #12 was merged into `v1-frontend-spike` at:

```text
bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
```

This specification starts from the branch created exactly at that merge:

```text
v1-recommendation-action-value
```

Associated promotion PR:

```text
#13 -> v1-frontend-spike
```

Prerequisite accepted evidence:

```text
Foundation 018
    Proposal / Investigation / Run / Evidence / Decision distinctions

Foundation 019
    KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING

D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Specification 012 v1.0 / Checkpoint 141
    explained MethodologicalHorizon

Specification 013 v1.0 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack

Specification 014 v1.0 / Checkpoint 146
    first real-model selective-context value gate passed
```

Frozen benchmark fixture:

```text
tests/fixtures/reasoning/recommendation_action_v1.json
```

Research rationale:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
```

The frozen question is:

> Given the same project microstate, explicit task profile, candidate action menu, model/runtime configuration, and evaluation rubric, does the accepted ADS methodological path help a strong reasoner choose and calibrate the right methodological actions, preserve blocking dependencies, and avoid unnecessary work relative to strong simpler controls?

---

## 2. Why this slice is downstream of Specification 014

Specification 014 established bounded real-model evidence that the accepted selective context can preserve the first frozen reasoning obligations while reducing provider input-token burden materially.

It did not establish that ADS can move correctly from:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> PROJECT ACTION
```

The current slice therefore does not modify retrieval, Horizon construction, applicability, or the accepted selective-context algorithm. Those mechanisms remain treatment inputs.

The new observable failure modes are:

```text
critical concern omitted
recommendation too weak
recommendation too strong
blocking dependency missed
blocking scope invented
unnecessary work recommended
important current work deferred
resolved work reopened without evidence
```

No retrieval/reranking/vector mechanism may be introduced merely to improve this benchmark unless a later preserved result identifies that layer as the failure source.

---

## 3. Frozen recommendation dispositions

Every candidate action must receive exactly one benchmark disposition:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

These labels are experimental evaluation labels, not final production enums.

Their meanings are frozen as follows.

### BLOCKING_REQUIRED

The action or resolution is necessary before one or more explicitly named downstream scopes can currently be defended.

This is not merely a stronger recommendation. It must be tied to a validity/dependency boundary represented in the supplied project microstate.

### RECOMMENDED

The action is worth doing now for the stated current objective, but the current project evidence does not make it a validity blocker for a named downstream scope.

### DEFER

The action may be relevant or useful, but should not be done now because a more immediate dependency, sequencing constraint, or current priority should be resolved first.

### NOT_NOW

The current project evidence and stated objective do not provide material justification for prioritizing the action now. This is different from DEFER: there need not be a current dependency after which it automatically becomes worth doing.

---

## 4. Bounded candidate action menu

Each frozen project microstate supplies the same finite candidate action menu to every condition.

The reasoner may not invent additional action IDs for this experiment.

This restriction is intentional. It permits deterministic evaluation of recommendation calibration and blocking behavior while holding action discovery constant.

Open-world proposal generation remains out of scope.

Every candidate action contains:

```text
action_id
label
cost_units
expected_disposition
critical
```

The `expected_disposition` and `critical` fields are evaluator truth and must not be exposed to the reasoner.

The reasoner receives only:

```text
action_id
label
cost_units
```

Cost units are benchmark-relative burden units used only for unnecessary-action diagnostics. They are not monetary cost and are not a production planning scale.

---

## 5. Frozen conditions

Three conditions are compared.

### GENERIC

A strong reasoner receives:

```text
same system instruction
same user task
same project evidence
same requested reasoning functions
same candidate action menu
same blocked-scope menu
same clarification menu
same structured output schema
no reusable methodological knowledge assets
```

`methodological_basis` must therefore be empty.

This is the principal simple control for whether explicit methodological knowledge/navigation adds downstream recommendation value beyond a strong model that already sees the project state and bounded task profile.

### SELECTIVE

The reasoner receives the accepted Specification 013 pack generated from the same explained Horizon and frozen requested reasoning functions.

Required stable-key sets are fixed by the benchmark fixture.

This is the principal ADS treatment.

### FULL_HORIZON

The reasoner receives all ten current accepted revisions from the same explained Horizon using the same compact reasoning projection accepted in the preceding slices.

FULL_HORIZON exists here to test downstream omission/expansion behavior, not to rerun Specification 014's token-compression question.

No raw global export, retrieval scores, aliases, semantic cues, system omission decisions, or governance event prose enters the reasoner payload.

---

## 6. Task-profile derivation is held fixed

Every condition receives the same explicit `requested_reasoning_functions` for the case.

The unresolved production problem:

```text
project state / user language
    -> requested reasoning functions
```

is deliberately excluded from this experiment.

This preserves attribution. A failure in the present slice occurs after a correct task profile is already supplied.

---

## 7. Frozen project microstates

The benchmark contains exactly four cases.

### RA-01 VALIDITY_GATE

Current state includes:

```text
binary churn prediction
future monthly deployment
prediction moment UNKNOWN
candidate feature observed after outcome
feature-availability assessment not completed
random row split across observed months
user wants nonlinear model comparison now
```

Required SELECTIVE keys:

```text
prediction-moment
prediction-time-feature-eligibility
temporal-validation
```

Expected blocked scopes:

```text
model-comparison-claims
model-selection-decision
```

The critical required actions are to establish prediction moment, audit prediction-time feature availability/lineage, and establish future-representative temporal validation. Model-family comparisons are deferred until those gates are resolved.

### RA-02 MODEL_CHOICE

Current state includes:

```text
binary supervised tabular prediction
future-representative temporal validation already locked
prediction-time feature eligibility already verified
moderate data scale
nonlinear interactions plausible
regularized logistic baseline already evaluated
user wants compact nonlinear shortlist
```

Required SELECTIVE keys:

```text
gradient-boosted-trees
random-forest
```

Expected blocked scopes:

```text
none
```

Random Forest and Gradient-Boosted Trees are recommended under the same locked evaluation design. Resolved validity work should not be reopened without new evidence, and broader ensemble/EDA expansion is not automatically current priority.

### RA-03 EVIDENCE_PLAN

Current state includes:

```text
one quantitative variable
strong right skew and extreme observed values
missingness verified absent
current question is distribution understanding before transformation/capping
no model choice requested
no current validation issue
```

Required SELECTIVE keys:

```text
ecdf
histogram
```

Expected blocked scopes:

```text
none
```

Histogram and ECDF are recommended as compact complementary evidence. Modeling, validation redesign, and already-resolved missingness work are NOT_NOW.

### RA-04 MISSINGNESS_IMBALANCE

Current state includes:

```text
binary classification
positive prevalence approximately 6%
valid deployment-representative split already established
two high-value variables have substantial training missingness
production missingness UNKNOWN
proposal to lock median imputation and evaluation plan before model comparison
```

Required SELECTIVE keys:

```text
class-imbalance
missing-data
```

Expected blocked scopes:

```text
preprocessing-lock
model-selection-claims
```

Missingness/production behavior and imbalance-aware evaluation evidence are blocking requirements for the named scopes. Immediate model-family comparison is deferred.

The fixture is authoritative for exact action menus, clarifications, blocked scopes, and semantic obligations.

---

## 8. ADS-owned recommendation result

The slice must introduce an ADS-owned structured result conceptually equivalent to:

```text
RecommendationActionResult
    summary: str
    action_decisions: tuple[RecommendationActionDecision, ...]
    blocked_scopes: tuple[str, ...]
    required_clarification_ids: tuple[str, ...]
    warnings: tuple[str, ...]
    methodological_basis: tuple[str, ...]

RecommendationActionDecision
    action_id: str
    disposition: RecommendationDisposition
    rationale: str
```

Every supplied candidate action ID must occur exactly once in `action_decisions`.

Unknown action IDs, duplicate action IDs, unknown disposition values, blocked scopes outside the supplied menu, or clarification IDs outside the supplied menu are invalid structured responses.

`methodological_basis` must satisfy:

```text
GENERIC
    empty

SELECTIVE / FULL_HORIZON
    set(methodological_basis)
        <= supplied stable keys in that condition
```

The production-facing output type may later evolve. This experiment does not freeze a final persistent Proposal schema.

---

## 9. No authoritative project mutation yet

The recommendation result is an experiment/application result, not a state mutation.

The runner must not create or update authoritative project objects such as:

```text
Proposal
Question
Investigation
Decision
```

and must not emit authoritative domain events such as:

```text
ProposalCreated
ProposalAccepted
InvestigationStarted
DecisionChanged
```

The purpose of this gate is to establish recommendation/action behavior before coupling it to durable project mutation.

A later slice may map accepted recommendation results into the Foundation 018 object/event model if this seam earns continuation.

---

## 10. Frozen reasoner configuration

Use the same concrete reasoner treatment as Specification 014:

```text
provider                OpenAI
runtime                 OpenAI Agents SDK behind ADS-owned ReasoningRuntime
runtime package         openai-agents==0.19.4
model                   gpt-5.6-sol
reasoning effort        medium
text verbosity          low
max output tokens       4000
fast/priority request   no
previous response       none
runtime tools           none
multi-agent             no
```

The public model identifier is an experiment treatment constant, not a final provider/model selection.

Every successful live attempt must preserve requested/provider model identity, timestamp, package versions where available, reasoning effort, verbosity, output limit, token usage, latency, service tier where available, and exact context/revision identity.

---

## 11. Frozen blinded judge configuration

Use one condition-blinded semantic judge call for every successful reasoner output.

```text
provider                OpenAI
runtime                 OpenAI Agents SDK / compatible ADS runtime path
runtime package         openai-agents==0.19.4
model                   gpt-5.6-sol
reasoning effort        high
text verbosity          low
max output tokens       4000
runtime tools           none
condition identity      hidden
```

The judge receives only:

```text
opaque output_id
user task
project evidence
candidate action labels and IDs
blocked-scope / clarification menus
frozen semantic obligation rubric
candidate RecommendationActionResult
```

The judge must not receive:

```text
GENERIC / SELECTIVE / FULL_HORIZON label
methodological context payload
context digest
expected action dispositions
expected blocked scopes
expected clarification IDs
provider token usage
latency
paired outputs from other conditions
```

Judge scores remain:

```text
0 absent, materially wrong, or contradicted
1 partially or implicitly satisfied
2 explicitly and correctly satisfied
```

Normalized semantic score:

```text
sum(scores) / (2 * number_of_obligations)
```

The harness recomputes the normalized score and rejects inconsistent judge output.

---

## 12. Deterministic recommendation evaluator

Deterministic action evaluation is primary in this slice.

### RM-01 Exact disposition accuracy

For one reasoner output:

```text
number of candidate actions with predicted == expected disposition
/
number of candidate actions
```

### RM-02 Critical action omission

A critical omission occurs when:

```text
expected disposition == BLOCKING_REQUIRED
and
predicted disposition != BLOCKING_REQUIRED
```

### RM-03 Under-recommendation

An under-recommendation occurs when:

```text
expected disposition == RECOMMENDED
and
predicted disposition in {DEFER, NOT_NOW}
```

A `BLOCKING_REQUIRED` prediction for an expected `RECOMMENDED` action is an exact-class error but not counted as under-recommendation.

### RM-04 Over-recommendation

An over-recommendation occurs when:

```text
expected disposition in {DEFER, NOT_NOW}
and
predicted disposition in {RECOMMENDED, BLOCKING_REQUIRED}
```

### RM-05 Unnecessary recommended cost

For one output:

```text
sum(cost_units)
for actions expected in {DEFER, NOT_NOW}
but predicted in {RECOMMENDED, BLOCKING_REQUIRED}
```

### RM-06 Blocking-scope false negative

An expected blocked scope is missing from the result.

### RM-07 Blocking-scope false positive

A predicted blocked scope is not in the expected blocked-scope set.

### RM-08 Required-clarification false negative

An expected required clarification ID is absent from the result.

This metric is recorded deterministically. The current hard gates rely on the frozen semantic obligations for the critical meaning of unresolved clarifications rather than introducing an additional independent threshold after the fixture was frozen.

### RM-09 Unsupported methodological basis

A basis key is present that was not supplied to that condition.

For GENERIC, any basis key is unsupported.

---

## 13. Frozen absolute SELECTIVE gates

The accepted ADS treatment must satisfy every absolute gate.

### RA-G01 Critical omission

```text
SELECTIVE total critical action omissions == 0
```

### RA-G02 Blocking false negatives

```text
SELECTIVE total blocking-scope false negatives == 0
```

### RA-G03 Basis provenance

```text
SELECTIVE unsupported methodological-basis failures == 0
```

### RA-G04 Aggregate exact recommendation calibration

```text
SELECTIVE aggregate exact disposition accuracy >= 0.90
```

### RA-G05 Per-case exact recommendation calibration

For every case:

```text
SELECTIVE mean exact disposition accuracy >= 0.80
```

### RA-G06 Aggregate semantic correctness

```text
SELECTIVE aggregate normalized judge score >= 0.90
```

### RA-G07 Per-case semantic correctness

For every case:

```text
SELECTIVE mean normalized judge score >= 0.85
```

These thresholds are benchmark gates, not production service-level targets.

---

## 14. Frozen relative quality gates

The ADS treatment must not materially regress relative to either strong control.

### RA-G08 Exact disposition versus GENERIC

```text
aggregate SELECTIVE accuracy >= aggregate GENERIC accuracy - 0.05
```

For every case:

```text
SELECTIVE accuracy >= GENERIC accuracy - 0.10
```

### RA-G09 Exact disposition versus FULL_HORIZON

```text
aggregate SELECTIVE accuracy >= aggregate FULL_HORIZON accuracy - 0.05
```

For every case:

```text
SELECTIVE accuracy >= FULL_HORIZON accuracy - 0.10
```

### RA-G10 Semantic score versus GENERIC

```text
aggregate SELECTIVE semantic >= aggregate GENERIC semantic - 0.05
```

For every case:

```text
SELECTIVE semantic >= GENERIC semantic - 0.10
```

### RA-G11 Semantic score versus FULL_HORIZON

```text
aggregate SELECTIVE semantic >= aggregate FULL_HORIZON semantic - 0.05
```

For every case:

```text
SELECTIVE semantic >= FULL_HORIZON semantic - 0.10
```

### RA-G12 Critical/under-recommendation versus GENERIC

```text
SELECTIVE total critical omissions <= GENERIC total critical omissions
SELECTIVE total under-recommendations <= GENERIC total under-recommendations
```

No formal statistical non-inferiority claim may be made from these small repetitions.

---

## 15. Frozen expansion gates against FULL_HORIZON

The SELECTIVE treatment must not be more expansion-prone than the wider context control on the preregistered exact measures.

### RA-G13 Unnecessary action cost

```text
SELECTIVE total unnecessary recommended cost
    <=
FULL_HORIZON total unnecessary recommended cost
```

### RA-G14 Over-recommendations

```text
SELECTIVE total over-recommendations
    <=
FULL_HORIZON total over-recommendations
```

### RA-G15 Blocking false positives

```text
SELECTIVE total blocking-scope false positives
    <=
FULL_HORIZON total blocking-scope false positives
```

These gates do not assume that FULL_HORIZON must be worse. Equality is allowed.

---

## 16. Promotion requires a preregistered positive value signal

Passing safety/non-regression gates alone is not sufficient to claim that the explicit ADS methodological treatment added recommendation/action value on this benchmark.

At least one of the following signals must occur:

```text
1. SELECTIVE aggregate exact disposition accuracy
       >= GENERIC + 0.05

2. SELECTIVE total critical omissions
       < GENERIC total critical omissions

3. SELECTIVE total under-recommendations
       < GENERIC total under-recommendations

4. SELECTIVE total unnecessary recommended cost
       < FULL_HORIZON total unnecessary recommended cost

5. SELECTIVE total over-recommendations
       < FULL_HORIZON total over-recommendations

6. SELECTIVE total blocking-scope false positives
       < FULL_HORIZON total blocking-scope false positives
```

A signal is interpreted only inside this frozen benchmark. It is not a universal claim about explicit methodology or larger context.

---

## 17. Frozen advancement classification

The result must be classified into exactly one of three outcomes.

### PROMOTE_BOUNDED_RECOMMENDATION_SEAM

Require:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
at least one preregistered positive value signal occurs
all technical invariants pass
complete scored design is obtained
```

This outcome would authorize continued development of the bounded recommendation/action result seam and a later project-state mutation slice.

### SAFE_BUT_NOT_DIFFERENTIATED

Require:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
no preregistered positive value signal occurs
all technical invariants pass
complete scored design is obtained
```

This outcome means the mechanism is safe enough on the benchmark but the experiment does not demonstrate additional recommendation/action value over the controls. Do not invent a promotion claim.

### FAIL

Any failure of an absolute, relative, expansion, technical, or completeness gate yields FAIL.

A failed result must be preserved before any model, prompt, context, fixture, threshold, or evaluator is changed.

---

## 18. Provider usage and latency are descriptive

Record for every successful reasoner and judge attempt:

```text
input tokens
cached input tokens when available
output tokens
reasoning tokens when available
total tokens
latency
service tier when available
```

Provider input-token differences are expected across conditions, but Specification 015 does not use token ratio as an advancement gate.

If monetary cost is calculated, preserve the pricing source/date and treat the value as descriptive.

---

## 19. Frozen replication and randomization

Design:

```text
4 cases
3 conditions
3 reasoner repetitions per condition
36 planned reasoner outputs
36 planned blinded judge outputs
72 planned successful provider calls
```

Randomization seed:

```text
20260823
```

The harness must construct and serialize the complete reasoner plan before the first provider call.

Requirements:

```text
condition order randomized within each case/repetition block
all reasoner entries receive condition-neutral opaque output IDs
judge order independently deterministically shuffled
reasoner plan serialized and SHA-256 hashed before calls
judge plan serialized and SHA-256 hashed before judge calls
```

No result-dependent call ordering is permitted.

---

## 20. Frozen failure and retry policy

A planned call may be retried once only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

The retry must preserve case, condition, repetition, task, menus, prompt/configuration, context digest, and model configuration.

Every failed attempt remains in the raw ledger.

Maximum total provider attempts:

```text
90
```

Semantic quality, incorrect recommendation, or a failed evaluation gate is never a retry reason.

---

## 21. Technical invariants

### RA-INV-01 Frozen candidate menus

All three conditions receive byte-equivalent user task, project evidence, requested reasoning functions, candidate action IDs/labels/costs, blocked-scope menu, and clarification menu for a matched case/repetition.

Evaluator-only expected dispositions, expected blocked scopes, expected clarifications, critical flags, and rubric metadata are absent from reasoner input.

### RA-INV-02 Frozen SELECTIVE sets

SELECTIVE stable-key sets exactly equal the fixture's required sets before live calls.

### RA-INV-03 FULL_HORIZON identity

FULL_HORIZON contains exactly ten current accepted revisions from the same explained Horizon.

### RA-INV-04 GENERIC contains no reusable methodological assets

No hidden Horizon, MethodologicalContextPack, knowledge summary, or methodological basis hint enters GENERIC.

### RA-INV-05 Same model configuration

All reasoner conditions use identical model/runtime settings.

### RA-INV-06 No tools

Reasoner and judge expose zero callable tools.

### RA-INV-07 No cross-call state

No previous response ID, framework session history, conversation state, or prior output is reused.

### RA-INV-08 Condition identity hidden from reasoner content

The treatment label is used by the harness but is not serialized into the model-facing task envelope.

### RA-INV-09 Structured output exactness

Every candidate action appears exactly once and only allowed menu IDs/enum values/scopes/clarifications are returned.

### RA-INV-10 Basis provenance

`methodological_basis` is empty for GENERIC and a subset of supplied stable keys for SELECTIVE/FULL_HORIZON.

### RA-INV-11 Judge blinding

The judge payload contains no condition label, methodological context, context digest, expected evaluator labels, provider usage, latency, or alternate-condition output.

### RA-INV-12 Deterministic evaluator

All exact recommendation metrics are recomputed from fixture truth and structured reasoner output, not accepted from model self-report.

### RA-INV-13 Deterministic plan

Repeated plan generation from unchanged fixture/seed produces identical canonical bytes and SHA-256 digests.

### RA-INV-14 Exact context transparency

SELECTIVE/FULL_HORIZON reasoner traces preserve exact context SHA-256 and stable-key/revision pairs. GENERIC explicitly records the empty/no-methodology context identity.

### RA-INV-15 Authoritative isolation

Experiment execution performs no authoritative project or reusable-knowledge mutation.

### RA-INV-16 Runtime isolation

ADS application/domain modules import no OpenAI Agents SDK/provider type.

### RA-INV-17 Ordinary CI isolation

Provider-free CI must pass without a live OpenAI key and must not execute paid/provider calls.

### RA-INV-18 Cross-platform provider-free infrastructure

All non-live unit/integration gates for the slice must pass on Ubuntu and Windows under the existing V1 project environment before live execution.

---

## 22. Result ledger requirements

Preserve a complete machine-readable and human-readable result bundle.

For every reasoner attempt record at least:

```text
opaque output_id
case_id
condition
repetition
attempt
candidate action menu digest
project evidence digest
context SHA-256 / explicit GENERIC empty identity
context stable-key/revision pairs
requested/provider model
reasoning effort
structured RecommendationActionResult or failure
all deterministic recommendation metrics
unexpected / unsupported basis diagnostics
provider usage
latency
service tier when available
```

For every judge attempt record at least:

```text
opaque judge_id
opaque reasoner output_id
attempt
requested/provider model
obligation scores
recomputed normalized score
critical failure
provider usage
latency
failure if any
```

Aggregate result must include:

```text
all RA-G01 through RA-G15 gate results
all preregistered value-signal results
final three-way advancement classification
per-case and per-condition exact accuracy
critical omissions
under-recommendations
over-recommendations
unnecessary recommended cost
blocking false negatives / positives
required-clarification false negatives
semantic judge quality
basis-provenance failures
technical invariants
provider usage and latency summaries
```

Preserve raw ledgers before interpretation or tuning.

---

## 23. Explicit non-goals and non-selections

This specification does not select or solve:

```text
natural-language/project-state -> reasoning-function derivation
open-world free-form proposal discovery
final production recommendation enum
final recommendation ranking/priority model
complete Foundation 018 persistence schema
mapping recommendation output to authoritative Proposal/Question/Decision events
automatic execution of accepted proposals
human approval/escalation policy
admissibility or risk-sensitive assurance policy
final provider/model or reasoning effort
multi-agent recommendation review
production semantic retrieval/fusion/reranking/vector infrastructure
frontend or Project Cockpit wiring
```

Do not infer these decisions from a future pass of this bounded benchmark.

---

## 24. Implementation order after freeze

After the freeze checkpoint is committed:

```text
1. add ADS-owned RecommendationActionResult / disposition types
2. implement deterministic recommendation evaluator
3. implement GENERIC / SELECTIVE / FULL_HORIZON condition construction
4. add deterministic plan and blinded judge contracts
5. add fake-runtime unit/integration tests for all 36 + 36 planned observations
6. add ordinary Ubuntu/Windows provider-free workflow coverage
7. add a separate explicit secret-gated live workflow
8. validate the exact pre-live head
9. execute the frozen live plan once
10. preserve raw and aggregate result before changing anything
```

No live provider call may occur before the implementation is provider-free validated and the exact pre-live boundary is preserved.

---

## 25. Promotion audit at freeze

### Promote this experiment into the active V1 route

**Decision:** yes.

The research rationale and this frozen specification justify testing recommendation/action behavior as the next downstream architectural question.

### Promote any recommendation/action result now

**Decision:** no.

No live or provider-free implementation result exists yet.

### Promote the four disposition labels as permanent product state

**Decision:** no.

They are benchmark semantics for the first evaluation slice.

### Promote bounded candidate menus as the long-term product model

**Decision:** no.

Open-world proposal discovery remains a long-term requirement.

### Promote automatic project mutation or execution

**Decision:** no.

The current slice is read/reason/evaluate only.

### Promote a final model/provider, multi-agent design, or richer retrieval stack

**Decision:** no.

The existing concrete runtime/model is held fixed for attribution only.

---

## 26. Exact continuation

After the freeze checkpoint and routing reconciliation:

```text
implement provider-free only
validate deterministic evaluator and 3-condition plan
prove no authoritative project mutation
prove no live-key leakage into ordinary CI
validate Ubuntu + Windows
then create the explicit live boundary
```

Do not make a live Specification 015 model call before these conditions are met.
