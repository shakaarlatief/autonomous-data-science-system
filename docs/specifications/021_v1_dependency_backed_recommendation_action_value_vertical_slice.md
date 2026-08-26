# Specification 021: V1 Dependency-Backed Recommendation and Action Value Vertical Slice

**Version:** 0.1  
**Date:** 2026-08-24  
**Status:** Frozen bounded implementation/evaluation contract before Specification 021 implementation or new live provider calls  
**Scope:** Prospectively test whether the accepted SELECTIVE methodological-context path improves downstream recommendation/action quality relative to a strong GENERIC reasoner while remaining no more expansion-prone than FULL_HORIZON, after known provenance, DEFER, and BLOCKING_REQUIRED confounds are removed through system-owned provenance and explicit relation-backed semantics.  
**Authority:** Governs Specification 021 implementation and evaluation until its result is preserved. It does not modify or rescore Specifications 015-020, promote production recommendation/disposition semantics, authorize project mutation or automatic execution, select a final provider/model, or select a multi-agent architecture.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

The experiment branch is:

```text
v1-dependency-backed-recommendation-value
```

It was created from the closed integration boundary:

```text
8f29894667467e6ef58a02eb8f5d580c895968e6
```

Checkpoint 173 records closure of the Level-2 routing-consistency hardening after the required exact integration push validation.

Historical evidence remains immutable:

```text
Specification 015   FAIL
Specification 016   DISPOSITION_BOUNDARY_SUPPORTED
Specification 017   INCOMPLETE
Specification 019   FAIL
Specification 020   BLOCKING_BOUNDARY_SUPPORTED
```

Research rationale:

```text
docs/research/029_dependency_backed_recommendation_value_design.md
```

Frozen benchmark fixture:

```text
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
```

---

## 2. Frozen experiment question

> Given the same project microstate, explicit task profile, candidate action menu, explicit requirement/scope/resolver relations, explicit defer-trigger relations, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE exact-revision methodological-context path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control?

This is a new prospective experiment.

It is not a rescore or relabeling of Specification 019.

---

## 3. Why a new experiment is now justified

Specification 019 completed a matched three-condition comparison with system-owned methodological provenance but failed its frozen gates. The central discrepancy was repeated escalation of worthwhile nonlinear model-family comparison from:

```text
RECOMMENDED
```

into:

```text
BLOCKING_REQUIRED
```

Specification 020 then prospectively isolated that construct and supported the stronger relation-backed boundary:

```text
exact unresolved requirement
+ exact active defended downstream scope
+ explicit scope DEPENDS_ON requirement relation
+ candidate action RESOLVES requirement
```

Specification 016 had already supported the analogous sequencing rule:

```text
DEFER
    -> exact unresolved activating trigger
    -> action explicitly waits for that trigger
```

Specification 021 therefore tests recommendation value only after those structural semantics are made explicit in new benchmark cases.

---

## 4. Historical-integrity rule

Specification 021 MUST NOT:

```text
edit Specification 019 truth
rescore Specification 019 outputs
reinterpret RB-02 as correct under the new contract
use individual Specification 019 outputs to tune new expected labels
weaken Specification 019 gates post hoc
edit or rescore Specification 020
claim that Specification 020 proved recommendation-system value
```

The new cases are prospectively authored from accepted structural lessons, not from desired model behavior.

---

## 5. Frozen methodological universe

Specification 021 reuses the same accepted ten-asset methodological universe used by Specifications 013-019:

```text
bagging
class-imbalance
ecdf
gradient-boosted-trees
histogram
missing-data
prediction-moment
prediction-time-feature-eligibility
random-forest
temporal-validation
```

Knowledge source:

```text
tests/fixtures/knowledge/reusable_knowledge_stress_v1.json
```

No knowledge asset may be added, rewritten, or selectively strengthened for this experiment.

The experiment is not a knowledge-engineering treatment.

---

## 6. Frozen conditions

Exactly three conditions are frozen.

### GENERIC

Receives:

```text
same common instruction
same user task
same project evidence
same explicit requested reasoning functions
same requirement menu
same downstream-scope menu
same scope DEPENDS_ON requirement relations
same candidate action menu
same action RESOLVES requirement relations
same defer-trigger menu
same action WAITS_FOR trigger relations
same structured output schema
no reusable methodological assets
```

System-owned supplied methodology revisions are empty.

### SELECTIVE

Receives the accepted compact exact-revision methodological context for the case.

Frozen selective stable-key sets:

```text
DBRA-01
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

DBRA-02
    gradient-boosted-trees
    random-forest

DBRA-03
    ecdf
    histogram

DBRA-04
    class-imbalance
    missing-data
```

The implementation may reuse the accepted Specification 013 context-construction code path, but the effective supplied set MUST equal the frozen case set exactly.

### FULL_HORIZON

Receives all ten exact accepted-current revisions using the same compact reasoning projection as adjacent V1 recommendation experiments.

No retrieval, embedding, reranking, selector, provider, or model treatment is varied.

---

## 7. Frozen experiment dispositions

Each candidate action appears exactly once and receives exactly one disposition:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

These remain experiment labels only.

### BLOCKING_REQUIRED

Allowed only when the supplied state contains all of:

```text
B1. the action is currently justified;
B2. one exact supplied requirement is unresolved;
B3. one exact supplied downstream scope is active and intended to be defended;
B4. an explicit supplied relation states that the scope DEPENDS_ON the requirement;
B5. an explicit supplied relation states that the candidate action RESOLVES that requirement.
```

Required pointers:

```text
blocking_requirement_id = exact supplied requirement ID
blocked_scope_id        = exact supplied downstream-scope ID
defer_until_id          = null
```

High value, common best practice, priority, or generic sequencing preference is insufficient.

### RECOMMENDED

The current state materially justifies the action now or soon, but no exact active defended supplied scope is represented as blocked on a requirement that this action resolves.

Required pointers:

```text
blocking_requirement_id = null
blocked_scope_id        = null
defer_until_id          = null
```

### DEFER

Allowed only when:

```text
D1. the action is already justified or planned;
D2. one exact supplied trigger is unresolved;
D3. an explicit supplied relation states that the action WAITS_FOR that trigger;
D4. satisfying the trigger makes the action current next work.
```

Required pointers:

```text
blocking_requirement_id = null
blocked_scope_id        = null
defer_until_id          = exact supplied trigger ID
```

### NOT_NOW

The current state does not materially justify the action and no represented exact blocking or defer relation makes it current or next.

Required pointers:

```text
blocking_requirement_id = null
blocked_scope_id        = null
defer_until_id          = null
```

---

## 8. System-owned project relation contract

The benchmark supplies stable experiment identities for:

```text
requirements
downstream scopes
scope DEPENDS_ON requirement relations
defer triggers
candidate actions
action RESOLVES requirement relations
action WAITS_FOR trigger relations
```

The model may select only supplied identities.

The model must not invent authoritative dependencies, blockers, requirements, or triggers.

For every case and every condition, the core project/action/relation payload MUST be byte-equivalent after canonical serialization except for condition-neutral request nonce fields and methodology payload.

---

## 9. Frozen structured result

Use an experiment-owned result conceptually equivalent to:

```text
DependencyBackedRecommendationActionResult
    summary: string
    action_decisions: list[DependencyBackedActionDecision]
        action_id: string
        disposition: BLOCKING_REQUIRED | RECOMMENDED | DEFER | NOT_NOW
        blocking_requirement_id: string | null
        blocked_scope_id: string | null
        defer_until_id: string | null
        rationale: string
    warnings: list[string]
```

No model-authored methodological provenance field exists.

Validation MUST enforce:

```text
every candidate action appears exactly once
no duplicate or unknown action IDs
all requirement pointers are supplied IDs
all scope pointers are supplied IDs
all defer pointers are supplied trigger IDs
BLOCKING_REQUIRED requires non-null requirement and scope pointers and null defer pointer
RECOMMENDED requires all three pointers null
DEFER requires null blocking pointers and one non-null defer pointer
NOT_NOW requires all three pointers null
non-empty rationale for every action
no additional structured-result fields outside the frozen schema
```

Invalid structured responses are retryable only under the frozen retry policy.

---

## 10. Frozen benchmark cases

Exactly four new cases are frozen.

### DBRA-01 FUTURE_VALIDITY_AND_MODEL_SEQUENCE

Requested reasoning function:

```text
VALIDITY_CONSTRAINT
```

Selective context:

```text
prediction-moment
prediction-time-feature-eligibility
temporal-validation
```

The active future-facing model-selection scope explicitly depends on three unresolved requirements. Three actions resolve those requirements and are `BLOCKING_REQUIRED`. Two already approved model comparisons explicitly wait for `prediction-validity-established` and are `DEFER`. One unrelated distribution action is `NOT_NOW`.

### DBRA-02 COMPACT_NONLINEAR_MODEL_SHORTLIST

Requested reasoning function:

```text
MODEL_OPTION
```

Selective context:

```text
gradient-boosted-trees
random-forest
```

Prediction validity and temporal evaluation are already established. No active defended scope is blocked on the model-family comparisons. Random Forest and Gradient-Boosted Trees evaluation are `RECOMMENDED`. Their tuning actions explicitly wait for `initial-nonlinear-comparison-complete` and are `DEFER`. Redundant or unrelated expansion is `NOT_NOW`.

Any `BLOCKING_REQUIRED` output in this case is a blocking false positive.

### DBRA-03 DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION

Requested reasoning function:

```text
EVIDENCE_OPTION
```

Selective context:

```text
ecdf
histogram
```

Histogram and ECDF inspection are `RECOMMENDED`. A transformation comparison explicitly waits for `distribution-evidence-reviewed` and is `DEFER`. Premature transformation and unrelated model-family work are `NOT_NOW`.

No active defended scope is blocked.

### DBRA-04 MISSINGNESS_IMBALANCE_DECISION_FRAMEWORK

Requested reasoning function:

```text
DECISION_FRAMEWORK
```

Selective context:

```text
class-imbalance
missing-data
```

One active evaluation-plan scope explicitly depends on an unresolved class-prevalence requirement, and one active preprocessing-plan scope explicitly depends on an unresolved production-missingness requirement. The two resolver actions are `BLOCKING_REQUIRED` with exact pointers. Missingness-pattern analysis is `RECOMMENDED`. Downstream strategy actions wait on exact supplied triggers and are `DEFER`. Premature accuracy-only/global-imputation actions are `NOT_NOW`.

The machine-readable fixture is the exact truth authority.

---

## 11. Frozen common reasoner instruction

The reasoner instruction MUST communicate the experiment semantics without exposing evaluator truth.

It must include the following meaning:

```text
Use only supplied project facts and supplied project relations for project-specific claims.
General methodological reasoning is allowed.
Unknown project facts remain unknown.
Classify every supplied candidate action exactly once.
Do not invent blockers, requirements, scopes, triggers, or relation identities.
BLOCKING_REQUIRED requires an exact supplied unresolved requirement, an exact active defended scope that depends on it, and an exact supplied action-resolves-requirement relation.
RECOMMENDED is worthwhile current work without such a blocking relation.
DEFER requires an exact supplied unresolved trigger and supplied action-waits-for-trigger relation.
NOT_NOW is neither currently justified nor activated by one of the supplied relations.
Return only supplied IDs in pointer fields.
Do not self-report methodological provenance.
```

Expected labels, gate thresholds, and evaluator rubrics MUST NOT enter the reasoner payload.

---

## 12. System-owned methodological provenance

For every planned reasoner output, construct before provider execution:

```text
SystemContextProvenance
    condition
    supplied_revisions[]
        stable_key
        revision_id
    methodology_payload_sha256
    methodology_payload_bytes
```

Rules:

```text
GENERIC supplied_revisions == []
SELECTIVE supplied revisions equal the exact frozen case set
FULL_HORIZON supplied revisions contain all ten exact revisions
payload SHA-256 recomputes exactly
payload byte count recomputes exactly
attempts/retries reuse the same planned provenance record
model output cannot mutate provenance
```

Methodological provenance is execution integrity, not a recommendation score.

---

## 13. Frozen deterministic recommendation metrics

For every successful reasoner output compute:

```text
exact_disposition_accuracy
critical_action_omissions
under_recommendations
over_recommendations
unnecessary_recommended_cost
blocking_false_positives
blocking_pointer_errors
defer_pointer_errors
```

Definitions:

```text
critical_action_omission
    expected BLOCKING_REQUIRED predicted as any other disposition

under_recommendation
    expected RECOMMENDED predicted as DEFER or NOT_NOW

over_recommendation
    expected DEFER or NOT_NOW predicted as RECOMMENDED or BLOCKING_REQUIRED

unnecessary_recommended_cost
    sum(cost_units) for expected DEFER/NOT_NOW actions predicted RECOMMENDED/BLOCKING_REQUIRED

blocking_false_positive
    any action not expected BLOCKING_REQUIRED predicted BLOCKING_REQUIRED

blocking_pointer_error
    expected BLOCKING_REQUIRED action predicted with wrong/null requirement or scope pointer,
    or any non-BLOCKING_REQUIRED action returning a non-null blocking pointer

defer_pointer_error
    expected DEFER action predicted with wrong/null trigger,
    predicted DEFER with unknown trigger,
    or any non-DEFER action returning a non-null defer pointer
```

---

## 14. Frozen blinded semantic judge

Every successful reasoner output receives exactly one judge call.

The judge receives only:

```text
opaque output ID
user task
project evidence
requirement/scope/trigger/action menus and relations
frozen case rubric
candidate model-owned recommendation result
score definitions
```

The judge MUST NOT receive:

```text
condition identity
methodological context
system provenance
context digests
selection metadata
provider usage or latency
paired outputs
expected deterministic disposition labels outside the rubric
```

Each frozen obligation is scored:

```text
0 absent, materially wrong, or contradicted
1 partial or implicit without material contradiction
2 explicit and correct
```

Normalized score:

```text
sum(scores) / (2 * number_of_obligations)
```

The judge may not add obligations.

---

## 15. Frozen absolute SELECTIVE gates

SELECTIVE MUST satisfy all:

```text
DBRA-G01  critical_action_omissions == 0
DBRA-G02  blocking_false_positives == 0
DBRA-G03  blocking_pointer_errors == 0
DBRA-G04  defer_pointer_errors == 0
DBRA-G05  aggregate exact disposition accuracy >= 0.90
DBRA-G06  every case exact disposition accuracy >= 0.85
DBRA-G07  aggregate semantic score >= 0.90
DBRA-G08  every case semantic score >= 0.85
```

The strict zero-tolerance blocking gates are justified because Specification 020 already demonstrated exact application of the explicit blocking construct in deliberately unambiguous microstates.

---

## 16. Frozen relative non-inferiority gates

SELECTIVE MUST satisfy:

```text
aggregate exact accuracy vs GENERIC       >= -0.05
per-case exact accuracy vs GENERIC        >= -0.10
aggregate exact accuracy vs FULL_HORIZON  >= -0.05
per-case exact accuracy vs FULL_HORIZON   >= -0.10

aggregate semantic score vs GENERIC       >= -0.05
per-case semantic score vs GENERIC        >= -0.10
aggregate semantic score vs FULL_HORIZON  >= -0.05
per-case semantic score vs FULL_HORIZON   >= -0.10

SELECTIVE critical omissions <= GENERIC
SELECTIVE blocking false positives <= GENERIC
SELECTIVE under-recommendations <= GENERIC
SELECTIVE defer-pointer errors <= GENERIC
```

These are bounded experiment gates, not formal statistical non-inferiority claims.

---

## 17. Frozen expansion gates

SELECTIVE MUST be no worse than FULL_HORIZON on:

```text
unnecessary recommended cost
over-recommendations
blocking false positives
```

The purpose is to reject a selective treatment that achieves apparent coverage by becoming more recommendation-expansive than the full compact Horizon.

---

## 18. Frozen positive value signals

Promotion requires at least one prospectively frozen recommendation-quality signal:

```text
S1  SELECTIVE aggregate exact disposition accuracy >= GENERIC + 0.05
S2  SELECTIVE aggregate semantic score >= GENERIC + 0.05
S3  SELECTIVE total critical omissions < GENERIC
S4  SELECTIVE total blocking false positives < GENERIC
S5  SELECTIVE total under-recommendations < GENERIC
S6  SELECTIVE total defer-pointer errors < GENERIC
S7  SELECTIVE unnecessary recommended cost < FULL_HORIZON
S8  SELECTIVE total over-recommendations < FULL_HORIZON
S9  SELECTIVE total blocking false positives < FULL_HORIZON
```

Input tokens, methodology bytes, latency, retries, and structured-output completion are descriptive instrumentation only and are not positive value signals.

---

## 19. Frozen complete-design outcomes

A scientific outcome is allowed only if all 36 reasoner outputs and all 36 corresponding judge outputs are successfully scored and execution integrity passes.

### PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM

Requires:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
at least one positive value signal passes
```

Supported bounded conclusion:

> Under the frozen relation-backed project microstates and fixed reasoner treatment, the accepted SELECTIVE methodological-context path is safe and shows at least one prospectively defined downstream recommendation-quality advantage over GENERIC and/or FULL_HORIZON.

This would justify bounded promotion of the recommendation seam to the next integration question, not production automation.

### SAFE_BUT_NOT_DIFFERENTIATED

Requires:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
zero positive value signals
```

Supported bounded conclusion:

> Clean dependency-backed semantics remove the known calibration confounds, but the current selective methodological context still does not demonstrate measurable recommendation-quality value beyond the strong generic reasoner on this bounded knowledge universe.

Required next interpretation:

```text
do not repeat the same benchmark merely to seek a positive result;
consider whether knowledge coverage/novelty rather than selection is the next limiting factor.
```

### FAIL

Use when the complete scored design has execution integrity but any absolute, relative, or expansion gate fails.

No recommendation-seam promotion is permitted.

### INCOMPLETE OR INTEGRITY-FAILED

If the complete scored design cannot be obtained under the frozen attempt budget, or execution integrity fails:

```text
advancement outcome = none
```

Do not force an incomplete run into a scientific outcome.

---

## 20. Frozen reasoner configuration

```text
provider                     OpenAI
runtime                      OpenAI Agents SDK behind ADS-owned ReasoningRuntime
runtime version              0.19.4
requested model              gpt-5.6-sol
reasoning effort             medium
text verbosity               low
max output tokens            4000
tools                        none
previous response state      none
fast/priority processing     not requested
store                        false where exposed
```

This is an experiment constant only.

---

## 21. Frozen judge configuration

```text
provider                     OpenAI
runtime                      OpenAI Agents SDK 0.19.4
requested model              gpt-5.6-sol
reasoning effort             high
text verbosity               low
max output tokens            4000
tools                        none
condition identity           hidden
one judge call               per successful reasoner output
```

---

## 22. Frozen repetitions, randomization, and provider budget

```text
4 cases
3 conditions
3 repetitions per condition
36 planned successful reasoner calls
36 planned successful judge calls
72 planned successful provider calls
randomization seed 2026082402
maximum total provider attempts 90
maximum retries per planned call 1
```

Retryable failure classes only:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

Every reasoner request receives a unique condition-neutral nonce. Judge order is independently deterministic and condition blinded. Every failed attempt is preserved.

---

## 23. Frozen plan and trace artifacts

Before the first provider call, serialize and hash:

```text
reasoner plan
judge plan
accepted knowledge snapshot
system methodological provenance plan
canonical matched-core project/action/relation payloads
```

The matched-core payload audit MUST establish that GENERIC, SELECTIVE, and FULL_HORIZON receive identical project/action/relation evidence per case apart from methodology payload and condition-neutral nonce.

The plan becomes immutable after the first provider attempt.

---

## 24. Provider-free construction audit

Before any live provider call, ordinary CI MUST prove at least:

```text
DBRA-INV-01 exactly four frozen cases exist
DBRA-INV-02 exactly three conditions exist
DBRA-INV-03 exact 36-call reasoner plan is deterministic under seed 2026082402
DBRA-INV-04 judge plan is deterministic, independently shuffled, and condition blinded
DBRA-INV-05 GENERIC supplies zero methodology revisions
DBRA-INV-06 SELECTIVE exact stable-key sets match Section 6 and the fixture
DBRA-INV-07 FULL_HORIZON supplies all ten accepted-current revisions
DBRA-INV-08 system methodology provenance is generated before provider calls from actual payloads
DBRA-INV-09 methodology payload SHA-256 and byte counts recompute exactly
DBRA-INV-10 no model-authored methodological provenance field exists
DBRA-INV-11 every expected BLOCKING_REQUIRED action has one exact unresolved requirement, one exact active defended scope, one scope DEPENDS_ON requirement relation, and one action RESOLVES requirement relation
DBRA-INV-12 no expected non-BLOCKING action satisfies the complete blocking construction
DBRA-INV-13 every expected DEFER action has one exact unresolved trigger and one action WAITS_FOR trigger relation
DBRA-INV-14 no expected NOT_NOW action has a blocking or defer relation
DBRA-INV-15 matched core project/action/relation payload is identical across conditions per plan entry
DBRA-INV-16 evaluator truth does not enter reasoner input
DBRA-INV-17 structured output validation enforces exact pointer rules
DBRA-INV-18 judge payload is condition/context/provenance/usage/paired-output blinded
DBRA-INV-19 retry accounting obeys the 90-attempt ceiling and semantic disagreement is non-retryable
DBRA-INV-20 complete fake-runtime design evaluates 36 reasoner and 36 judge outputs
DBRA-INV-21 ordinary CI contains no provider credential
DBRA-INV-22 application/domain layers remain free of provider SDK imports
DBRA-INV-23 authoritative project and knowledge state are not mutated
DBRA-INV-24 no live workflow or authorization is introduced before an exact green implementation checkpoint
```

The dedicated provider-free gate MUST run on Ubuntu and Windows.

---

## 25. Descriptive instrumentation

Record per condition and overall:

```text
successful structured outputs
invalid structured outputs
retry counts
input tokens
cached input tokens
output tokens
reasoning tokens
total tokens
latency
serialized methodology bytes
SELECTIVE/FULL methodology byte ratio
provider model/runtime identifiers
provider response/request IDs where exposed
```

These do not override recommendation gates.

---

## 26. No authoritative project mutation

Specification 021 is read/reason/evaluate only.

It must not create, update, accept, reject, execute, or persist authoritative project objects/events such as:

```text
Proposal
Question
Investigation
Decision
Run
Evidence
Finding
Claim
```

Temporary isolated experiment persistence is allowed only where needed for harness consistency.

---

## 27. Governed live launch boundary

This specification does not authorize a provider call.

After implementation, a later checkpoint MUST freeze:

```text
exact implementation source SHA
exact successful Ubuntu/Windows provider-free CI run IDs
exact target live workflow
exact confirmation token
exact Specification 018 authorization evidence
```

Only then may one exact repository-controlled authorization be added on `main` and exercised through the accepted governed launcher.

The launcher itself receives no provider credential. The target workflow independently validates the frozen source and confirmation before execution.

---

## 28. Explicit non-goals

Specification 021 does not establish or implement:

```text
production recommendation enum design
production deterministic blocking policy
production dependency persistence schema
open-world action generation
natural-language/project-state -> reasoning-function derivation
accepted recommendation -> durable project object/event mapping
automatic execution
human approval/escalation policy
final ranking/prioritization policy
risk/admissibility policy
large-scale knowledge-universe construction
multi-agent recommendation architecture
final provider/model policy
frontend/Cockpit wiring
```

---

## 29. Exact implementation sequence

```text
1. freeze Research 029, Specification 021, benchmark fixture, and a checkpoint
2. implement strict fixture loading and provider-free construction audits
3. implement the experiment-owned structured result and relation-pointer validation
4. reuse system-owned methodology provenance semantics from Specification 019
5. reuse the accepted exact-revision context construction for GENERIC / SELECTIVE / FULL_HORIZON
6. implement deterministic recommendation metrics and blinded semantic judging
7. implement complete fake-runtime and persistence-backed provider-free tests
8. add dedicated Ubuntu/Windows provider-free CI with no provider credential
9. freeze and checkpoint the exact green implementation head
10. only then freeze one governed live authorization boundary
11. execute at most the frozen provider-backed run
12. preserve all raw evidence before interpreting any scientific outcome
```

No Specification 021 live provider call is authorized before steps 1-9 are complete and green.
