# Specification 017: V1 Relation-Backed Recommendation and Action Value Vertical Slice

**Version:** 0.1  
**Date:** 2026-08-23  
**Status:** Frozen bounded implementation/evaluation contract before Specification 017 implementation or live model calls  
**Scope:** Second recommendation/action-value experiment, built from the promoted Specification 016 dependency-backed sequencing result, comparing GENERIC, accepted SELECTIVE, and compact FULL_HORIZON conditions without mutating authoritative project state.  
**Authority:** Governs Specification 017 implementation and evaluation until its result is preserved. It does not modify or rescore Specification 015, finalize production recommendation/disposition enums, define the complete Foundation 018 dependency schema, authorize project-state mutation or automatic execution, select a final provider/model, or select a multi-agent architecture.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

PR #15 was merged into `v1-frontend-spike` at:

```text
6bda0c1efcf078476859b2c2c64fb0586964899d
```

The active experiment branch begins exactly there:

```text
v1-recommendation-action-value-relation-backed
```

Specification 015 is immutable historical evidence with frozen outcome `FAIL`.

Specification 016 is completed bounded evidence with frozen outcome:

```text
DISPOSITION_BOUNDARY_SUPPORTED
```

Specification 017 is a new experiment. Its evaluator truth is not created by relabeling Specification 015 outputs. Any expected `DEFER` action in this specification must satisfy the stronger dependency-backed construction frozen below.

---

## 2. Frozen experiment question

> Given the same project microstate, explicit task profile, candidate action menu, relation-backed sequencing evidence, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control?

The target is downstream recommendation/action value after the accepted context-selection seam, not retrieval quality and not context-size reduction by itself.

---

## 3. Conditions

Exactly three conditions are frozen.

### GENERIC

Receives:

```text
same system instruction
same user task
same project evidence
same explicit requested reasoning functions
same candidate action menu
same blocked-scope menu
same clarification menu
same defer-trigger menu
same structured result schema
no reusable methodological assets
```

`methodological_basis` must be empty.

### SELECTIVE

Receives the accepted Specification 013 exact-revision `MethodologicalContextPack` for the frozen task profile.

Frozen selective sets:

```text
RB-01
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

RB-02
    random-forest
    gradient-boosted-trees

RB-03
    histogram
    ecdf

RB-04
    class-imbalance
    missing-data
```

### FULL_HORIZON

Receives all ten exact current accepted revisions in the same explained Horizon using the same compact reasoning projection used by the accepted context-value path.

The wider full condition is an expansion/control condition, not a new retrieval treatment.

---

## 4. Frozen disposition semantics

Every candidate action must be classified exactly once using one of:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

These remain experiment labels, not production enums.

### BLOCKING_REQUIRED

Use only when the action is current required work and at least one supplied named downstream scope cannot yet be defended without resolving it.

It is not merely a stronger recommendation.

### RECOMMENDED

Use when the action is currently justified and useful but is not a required blocker for a supplied downstream scope.

### DEFER

Use only when all are true:

```text
1. the action is already justified/planned in the represented project state;
2. one exact supplied trigger is currently unresolved;
3. that trigger must occur before the action can legitimately begin; and
4. satisfying the trigger makes the action current next work under the represented plan.
```

A DEFER decision must return:

```text
defer_until_id = exact supplied trigger ID
```

### NOT_NOW

Use when the current objective/state does not materially justify the action and no represented supplied activating trigger establishes that satisfying one current dependency makes it current next work.

A NOT_NOW decision must return:

```text
defer_until_id = null
```

The mere possibility that an action could become useful later is not sufficient for DEFER.

### Pointer rule for other dispositions

`BLOCKING_REQUIRED` and `RECOMMENDED` must also return `defer_until_id = null`.

Any unknown trigger ID is an invalid structured response.

---

## 5. Frozen structured result

The experiment-owned structured result is:

```text
RelationBackedRecommendationActionResult
    summary: string
    action_decisions: list[RelationBackedActionDecision]
        action_id: string
        disposition: BLOCKING_REQUIRED | RECOMMENDED | DEFER | NOT_NOW
        defer_until_id: string | null
        rationale: string
    blocked_scopes: list[string]
    required_clarification_ids: list[string]
    warnings: list[string]
    methodological_basis: list[string]
```

Validation requirements:

```text
every candidate action appears exactly once
no unknown candidate action IDs
no duplicate candidate action IDs
blocked_scopes subset of supplied blocked-scope menu
required_clarification_ids subset of supplied clarification menu
methodological_basis subset of exact supplied stable keys
DEFER -> exact supplied defer trigger
non-DEFER -> null defer pointer
```

Validation failure is an invalid structured-response failure class. It may be retried only under the frozen retry policy and never because the semantic answer disagrees with benchmark truth.

---

## 6. Frozen benchmark cases

The exact machine-readable benchmark is:

```text
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
```

There are four cases.

### RB-01 VALIDITY_GATE_AND_SEQUENCE

Task profile:

```text
VALIDITY_CONSTRAINT
```

Selective exact keys:

```text
prediction-moment
prediction-time-feature-eligibility
temporal-validation
```

Frozen core truth:

```text
establish-prediction-moment                 BLOCKING_REQUIRED
audit-prediction-time-feature-availability  BLOCKING_REQUIRED
establish-future-temporal-validation        BLOCKING_REQUIRED
compare-random-forest                       DEFER -> prediction-validity-established
compare-gradient-boosted-trees              DEFER -> prediction-validity-established
plot-monthly-spend-histogram                 NOT_NOW
```

Expected blocked scopes:

```text
model-comparison-claims
model-selection-decision
```

Expected required clarification:

```text
prediction-moment
```

### RB-02 COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE

Task profile:

```text
MODEL_OPTION
```

Selective exact keys:

```text
random-forest
gradient-boosted-trees
```

Frozen core truth:

```text
compare-random-forest                        RECOMMENDED
compare-gradient-boosted-trees               RECOMMENDED
tune-selected-nonlinear-family               DEFER -> model-family-selected
add-generic-bagging-baseline                 NOT_NOW
redesign-temporal-validation                 NOT_NOW
plot-all-feature-histograms-before-shortlist NOT_NOW
```

No blocked scopes or required clarifications are expected.

### RB-03 DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION

Task profile:

```text
EVIDENCE_OPTION
```

Selective exact keys:

```text
histogram
ecdf
```

Frozen core truth:

```text
establish-distribution-evidence-before-transformation BLOCKING_REQUIRED
plot-histogram                                      RECOMMENDED
compute-ecdf                                        RECOMMENDED
evaluate-transformation-capping-options             DEFER -> distribution-evidence-reviewed
winsorize-extreme-values-immediately                NOT_NOW
fit-nonlinear-model-now                             NOT_NOW
reopen-missingness-analysis                         NOT_NOW
```

Expected blocked scope:

```text
transformation-capping-decision
```

The generic evidence requirement is the blocker. Histogram and ECDF are complementary methods for satisfying it and are not individually promoted to REQUIRED merely because they are known methods.

### RB-04 MISSINGNESS_IMBALANCE_DECISION_SEQUENCE

Task profile:

```text
DECISION_FRAMEWORK
```

Selective exact keys:

```text
class-imbalance
missing-data
```

Frozen core truth:

```text
characterize-production-missingness          BLOCKING_REQUIRED
define-imbalance-aware-evaluation-plan        BLOCKING_REQUIRED
lock-missing-data-strategy                    DEFER -> production-missingness-characterized
lock-median-imputation-immediately            NOT_NOW
use-accuracy-only-primary-metric              NOT_NOW
compare-models                                DEFER -> preprocessing-evaluation-plan-locked
automatic-minority-oversampling-immediately   NOT_NOW
```

Expected blocked scopes:

```text
preprocessing-lock
model-comparison-claims
model-selection-decision
```

Expected required clarification:

```text
production-missingness
```

The benchmark does not declare median imputation, oversampling, or another single strategy universally wrong. It declares them not currently justified under the supplied unknown production-missingness state and bounded objective.

---

## 7. Deterministic metrics

For each condition and case, the harness must compute:

```text
exact_disposition_accuracy
critical_action_omissions
under_recommendations
over_recommendations
unnecessary_recommended_cost
blocking_scope_false_negatives
blocking_scope_false_positives
required_clarification_false_negatives
required_clarification_false_positives
defer_pointer_errors
unsupported_methodological_basis_failures
```

Definitions:

```text
critical_action_omission
    expected BLOCKING_REQUIRED action predicted as another disposition

under_recommendation
    expected RECOMMENDED action predicted as DEFER or NOT_NOW

over_recommendation
    expected DEFER or NOT_NOW action predicted as RECOMMENDED or BLOCKING_REQUIRED

unnecessary_recommended_cost
    sum(cost_units) for expected DEFER/NOT_NOW actions predicted as RECOMMENDED/BLOCKING_REQUIRED

defer_pointer_error
    any expected-DEFER wrong/null pointer,
    any predicted DEFER unknown pointer,
    or any non-DEFER decision carrying a pointer

unsupported_methodological_basis_failure
    any methodological_basis key not supplied in that condition
```

Exact disposition truth and defer-pointer truth are evaluated separately.

---

## 8. Blinded semantic judge

Every successful reasoner output receives exactly one condition-blinded semantic judge call.

The judge receives only:

```text
opaque output ID
user task
project evidence
candidate action menu
blocked-scope menu
clarification menu
defer-trigger menu
frozen rubric
candidate structured result
score definitions
```

The judge must not receive:

```text
condition identity
methodological context or context digest
selection metadata
provider usage or latency
paired outputs
expected deterministic labels outside the rubric
```

Each frozen obligation is scored:

```text
0 absent, materially wrong, or contradicted
1 partial or implicit without material contradiction
2 explicit and correct
```

Normalized semantic score:

```text
sum(scores) / (2 * number_of_obligations)
```

The judge may not add obligations.

---

## 9. Frozen absolute SELECTIVE gates

SELECTIVE must satisfy all:

```text
RBR-G01  critical_action_omissions == 0
RBR-G02  blocking_scope_false_negatives == 0
RBR-G03  unsupported_methodological_basis_failures == 0
RBR-G04  defer_pointer_errors == 0
RBR-G05  required_clarification_false_negatives == 0
RBR-G06  aggregate exact disposition accuracy >= 0.90
RBR-G07  every case exact disposition accuracy >= 0.85
RBR-G08  aggregate semantic score >= 0.90
RBR-G09  every case semantic score >= 0.85
```

A semantic judge score cannot compensate for a failed deterministic critical/pointer gate.

---

## 10. Frozen relative non-inferiority gates

SELECTIVE must satisfy:

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
SELECTIVE blocking false negatives <= GENERIC
SELECTIVE under-recommendations <= GENERIC
SELECTIVE required-clarification false negatives <= GENERIC
SELECTIVE defer-pointer errors <= GENERIC
```

These are bounded non-inferiority gates, not formal statistical non-inferiority claims.

---

## 11. Frozen expansion gates

SELECTIVE must be no worse than FULL_HORIZON on:

```text
unnecessary recommended cost
over-recommendations
blocking-scope false positives
required-clarification false positives
```

These gates test the hypothesis that wider context may create unnecessary action expansion.

---

## 12. Frozen positive value signals

A result may claim additional bounded recommendation/action value only if at least one of these preregistered signals is observed:

```text
S1  SELECTIVE aggregate exact disposition accuracy >= GENERIC + 0.05
S2  SELECTIVE aggregate semantic score >= GENERIC + 0.05
S3  SELECTIVE total critical omissions < GENERIC
S4  SELECTIVE total blocking-scope false negatives < GENERIC
S5  SELECTIVE total under-recommendations < GENERIC
S6  SELECTIVE total required-clarification false negatives < GENERIC
S7  SELECTIVE total defer-pointer errors < GENERIC
S8  SELECTIVE unnecessary recommended cost < FULL_HORIZON
S9  SELECTIVE total over-recommendations < FULL_HORIZON
S10 SELECTIVE total blocking-scope false positives < FULL_HORIZON
```

At least one signal is required for promotion.

No signal may be added after live outputs are observed.

---

## 13. Frozen advancement outcomes

Exactly three outcomes are allowed.

### PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM

Requires:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
at least one frozen positive value signal
```

### SAFE_BUT_NOT_DIFFERENTIATED

Requires:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
zero frozen positive value signals
```

This is a valid result and must not be rewritten into a promotion claim.

### FAIL

Any frozen absolute, relative, or expansion gate fails.

The complete raw result must be preserved regardless of outcome.

---

## 14. Frozen reasoner configuration

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

The concrete model/runtime configuration is an experiment constant only and is not promoted as the final provider/model choice.

---

## 15. Frozen judge configuration

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

## 16. Frozen repetitions, randomization, and provider budget

```text
4 cases
3 conditions
3 repetitions per condition
36 planned successful reasoner calls
36 planned successful judge calls
72 planned successful provider calls
randomization seed 2026082303
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

Every request receives a unique condition-neutral nonce. Reasoner condition order is deterministic from the frozen seed. Judge order is independently deterministic and condition blinded.

Failed attempts must be preserved.

---

## 17. Technical invariants before any live call

The provider-free implementation must prove at least:

```text
RBR-INV-01 exact frozen fixture parses and validates
RBR-INV-02 exact 36-call reasoner plan is deterministic
RBR-INV-03 judge plan is deterministic and independently shuffled
RBR-INV-04 GENERIC supplies zero methodological revisions
RBR-INV-05 SELECTIVE exact stable-key sets match this specification
RBR-INV-06 FULL_HORIZON supplies all ten exact accepted-current revisions
RBR-INV-07 matched conditions share identical task/project/action/trigger evidence
RBR-INV-08 relation-backed output schema validates defer pointers
RBR-INV-09 methodological basis is limited to actually supplied keys
RBR-INV-10 judge payload is condition/context/usage blinded
RBR-INV-11 retry accounting obeys the frozen 90-attempt ceiling
RBR-INV-12 complete fake-runtime design evaluates all 36 reasoner outputs and 36 judge outputs
RBR-INV-13 normal CI contains no live provider credential
RBR-INV-14 application/domain layers remain free of provider SDK imports
RBR-INV-15 authoritative project state is not mutated by the experiment
```

No live workflow may be executed until the exact implementation head has passed ordinary provider-free Ubuntu and Windows CI and has been preserved in a checkpoint.

---

## 18. Provider resource evidence

Record descriptively for every successful call when exposed:

```text
input tokens
cached input tokens
output tokens
reasoning tokens
total tokens
latency
requested model
provider model
runtime version
provider response/request IDs
```

Also record serialized context bytes and SELECTIVE/FULL context ratios.

No provider-resource metric overrides a failed recommendation/action gate.

---

## 19. Historical integrity requirements

The implementation and result must not:

```text
edit Specification 015 expected labels
rescore Specification 015
claim the old RA-02 evaluator truth was objectively wrong
reuse Specification 015's ambiguous expected-DEFER actions as new unambiguous DEFER truth
change Specification 016 after its observed result
```

The relation-backed construction is applied prospectively to new Specification 017 benchmark states.

---

## 20. Explicit non-goals

This experiment does not establish or implement:

```text
natural-language/project state -> reasoning-function derivation
open-world action generation
production recommendation enum design
complete Foundation 018 dependency-relation persistence
Proposal/Question/Investigation/Decision mutation
automatic execution
human approval/escalation policy
final prioritization/ranking policy
risk/admissibility policy
multi-agent recommendation architecture
production semantic retrieval stack
frontend/Cockpit wiring
final provider/model selection
```

---

## 21. Promotion rule

Before implementation or live calls, this specification and its fixture are frozen as experiment authority only.

After the result:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
    may justify a bounded production-facing recommendation result seam
    and a separate next design for mapping accepted outputs into Foundation 018 objects/relations/events

SAFE_BUT_NOT_DIFFERENTIATED
    preserves safety evidence but does not establish marginal value from explicit methodological knowledge

FAIL
    blocks promotion and requires failure attribution before another recommendation/action-value attempt
```

Production DEFER/NOT_NOW enums remain open under every outcome.

---

## 22. Exact next implementation sequence

```text
1. implement the experiment-owned relation-backed result model and validator
2. implement frozen fixture validation and condition construction
3. implement deterministic action/pointer metrics and blinded judge contract
4. implement fake-runtime unit tests and real-persistence provider-free integration tests
5. add dedicated ordinary Ubuntu/Windows CI with no live key
6. preserve and validate the exact implementation head
7. only then expose one explicit secret-gated live workflow
8. execute the frozen plan once
9. preserve all raw attempts/results before interpretation
```

No Specification 017 live provider call is authorized before steps 1-6 are complete and green.
