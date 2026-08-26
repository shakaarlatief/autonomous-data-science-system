# Research 024: Relation-Backed Recommendation and Action Value Design

**Date:** 2026-08-23  
**Status:** Bounded design rationale after Specification 016 support and before Specification 017 freeze, implementation, or live model calls  
**Scope:** Define the next downstream recommendation/action-value experiment so the system-value question can be tested without repeating Specification 015's ambiguous sequencing construct.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

PR #15 was merged into `v1-frontend-spike` at:

```text
6bda0c1efcf078476859b2c2c64fb0586964899d
```

That merge preserves two adjacent but different pieces of evidence.

Specification 015 remains an immutable failed recommendation/action-value experiment:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0
```

Its only failed named gate was concentrated on two RA-02 actions whose frozen truth expected `DEFER` while all three conditions mostly or always returned `NOT_NOW`.

Specification 016 then isolated that construct question. It replaced a loose sequencing label with an explicit relation-backed definition:

```text
DEFER
    action already justified in the represented plan
    + exact unresolved supplied activating trigger
    + action becomes current next work after the trigger
    + exact defer_until_id

NOT_NOW
    no material current justification
    + no represented supplied activating trigger relation
    + null defer_until_id
```

The live diagnostic returned:

```text
36 / 36 exact disposition classifications correct
18 / 18 expected-DEFER trigger pointers exact
18 / 18 expected-NOT_NOW pointers null
DISPOSITION_BOUNDARY_SUPPORTED
```

The next justified experiment can therefore return to the system-value question, but only under the stronger sequencing construction.

---

## 2. The unresolved question is now system value

The next frozen question should be:

> Given the same project microstate, explicit task profile, candidate action menu, relation-backed sequencing evidence, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control?

This is not a rerun or repair of Specification 015.

Specification 015 answered its own frozen question with `FAIL` and remains unchanged. Specification 017 should be a new benchmark whose evaluator truth is rebuilt around the Specification 016 construct discipline.

The experimental sequence is now:

```text
Specification 014
    selective context preserves reasoning quality efficiently

Specification 015
    first recommendation/action benchmark fails one exact-disposition gate

Specification 016
    stronger dependency-backed DEFER/NOT_NOW construct passes

Specification 017
    test recommendation/action value again under that stronger construct
```

---

## 3. Preserve the three-condition attribution design

The next experiment should retain the strongest useful part of Specification 015:

```text
GENERIC
SELECTIVE
FULL_HORIZON
```

### GENERIC

Receives the same:

```text
project evidence
user task
explicit reasoning-function profile
candidate action menu
blocked-scope menu
clarification menu
defer-trigger menu
structured output contract
```

but no reusable methodological assets.

This remains the main system-value control. A strong model may already know much of the relevant methodology, and the experiment must allow that result rather than manufacture a benefit.

### SELECTIVE

Receives the accepted Specification 013 exact-revision `MethodologicalContextPack` for the frozen task profile.

This is the ADS treatment whose downstream value remains unresolved.

### FULL_HORIZON

Receives the same ten exact current accepted Horizon revisions using the compact reasoning projection.

This remains the expansion/control condition. It asks whether more methodological context creates unnecessary work or rescues something SELECTIVE omitted.

---

## 4. Keep accepted retrieval and selection fixed

There is still no measured downstream reason to retune retrieval, dense fusion, RRF, Horizon construction, or the accepted task-profile selector.

Specification 017 should reuse the same four reasoning-function classes and exact selective sets already validated by Specifications 013-015:

```text
VALIDITY_CONSTRAINT
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

MODEL_OPTION
    random-forest
    gradient-boosted-trees

EVIDENCE_OPTION
    histogram
    ecdf

DECISION_FRAMEWORK
    class-imbalance
    missing-data
```

The benchmark should become harder downstream of context construction, not by changing context selection at the same time.

---

## 5. Strengthen the recommendation result with explicit sequencing pointers

Specification 015 represented disposition as only:

```text
action_id
    + disposition
    + rationale
```

That is no longer enough for `DEFER`.

The next experiment should use an experiment-owned structured result such as:

```text
RelationBackedRecommendationActionResult
    summary
    action_decisions[]
        action_id
        disposition
        defer_until_id: string | null
        rationale
    blocked_scopes[]
    required_clarification_ids[]
    warnings[]
    methodological_basis[]
```

Validation should enforce:

```text
DEFER
    defer_until_id must be exactly one supplied trigger ID

BLOCKING_REQUIRED / RECOMMENDED / NOT_NOW
    defer_until_id must be null

unknown trigger IDs
    invalid structured response
```

The pointer is not decorative metadata. It is the machine-checkable relation that gives DEFER its stronger meaning.

---

## 6. Make the four dispositions mutually interpretable

The benchmark should freeze explicit operational definitions and precedence.

### BLOCKING_REQUIRED

Use only when the action is a current required action and named downstream scope cannot yet be defended without resolving it.

It is not simply a high-priority recommendation.

### RECOMMENDED

Use when the action is currently justified and useful, but the supplied state does not make it a validity blocker for named downstream scope.

### DEFER

Use only when:

```text
the action is already justified/planned
and
an exact supplied unresolved trigger must happen first
and
satisfying that trigger makes this action current next work
```

Return the exact trigger pointer.

### NOT_NOW

Use when the current objective/state does not materially justify the action and no supplied activating dependency relation makes it current next work after one represented trigger.

The mere possibility that an action could become useful later is not DEFER.

### Precedence

When an action cannot legitimately begin until a represented trigger occurs, it is `DEFER`, even if it may become important later. `BLOCKING_REQUIRED` is reserved for a required action that is itself current work needed to unblock a named scope.

This distinction prevents the evaluator from treating every ultimately necessary downstream action as currently blocking.

---

## 7. Four new project microstates

The benchmark should retain the four accepted methodological task classes but replace the old action truth with new relation-backed project states.

### RB-01: VALIDITY_GATE_AND_SEQUENCE

Project situation:

```text
binary churn prediction
future monthly deployment
prediction moment UNKNOWN
one candidate feature appears after the outcome
feature-availability audit not completed
current evaluation randomly mixes months
user wants nonlinear model comparison
```

The project plan explicitly states that nonlinear model comparison is already approved as the immediate next modeling step once a supplied `prediction-validity-established` trigger is satisfied.

Expected behavior:

```text
establish prediction moment                  BLOCKING_REQUIRED
audit prediction-time feature availability   BLOCKING_REQUIRED
replace random split with temporal design     BLOCKING_REQUIRED
compare Random Forest                         DEFER -> prediction-validity-established
compare Gradient-Boosted Trees                DEFER -> prediction-validity-established
unrelated distribution plot                   NOT_NOW
```

This retains the important Specification 015 validity behavior while making model-comparison sequencing objectively relation-backed.

### RB-02: COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE

Project situation:

```text
future-representative validation already locked
prediction-time feature eligibility already verified
regularized logistic baseline already evaluated
nonlinear interactions plausible
user requests a compact nonlinear shortlist
```

Random Forest and Gradient-Boosted Trees are current recommendations. Hyperparameter tuning is already the agreed next modeling step only after a supplied `model-family-selected` trigger resolves.

Expected behavior:

```text
compare Random Forest                         RECOMMENDED
compare Gradient-Boosted Trees                RECOMMENDED
tune selected nonlinear family                DEFER -> model-family-selected
add generic bagging baseline                  NOT_NOW
redesign temporal validation                  NOT_NOW
plot every feature histogram before shortlist NOT_NOW
```

This directly repairs the construct problem without changing Specification 015. Generic bagging and broad histogram expansion are no longer called DEFER merely because they could be done later.

### RB-03: DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION

Project situation:

```text
one continuous variable strongly right-skewed
extreme values are present
missingness has already been verified absent
current question is distribution understanding
transformation/capping decision intentionally follows evidence review
no model choice requested
```

Histogram and ECDF are current complementary evidence actions. A supplied `distribution-evidence-reviewed` trigger activates the already-planned transformation/capping decision step.

Expected behavior:

```text
plot Histogram                                RECOMMENDED
compute ECDF                                  RECOMMENDED
evaluate transformation/capping options       DEFER -> distribution-evidence-reviewed
winsorize extreme values immediately          NOT_NOW
fit nonlinear model now                       NOT_NOW
reopen missingness analysis                   NOT_NOW
```

This tests whether methodological knowledge supports evidence planning without turning extreme values into automatic invalid-data claims or method-first preprocessing.

### RB-04: MISSINGNESS_IMBALANCE_DECISION_SEQUENCE

Project situation:

```text
binary classification
approximately 6% positives
valid evaluation split already established
two high-value variables have substantial training missingness
production/serving missingness behavior UNKNOWN
user proposes median imputation + accuracy-only evaluation + immediate model comparison
```

The project explicitly plans to lock the missing-data strategy after a `production-missingness-characterized` trigger and to begin model comparison after a broader `preprocessing-evaluation-plan-locked` trigger.

Expected behavior:

```text
characterize production missingness           BLOCKING_REQUIRED
define imbalance-aware evaluation plan        BLOCKING_REQUIRED
lock missing-data strategy                     DEFER -> production-missingness-characterized
lock median imputation immediately             NOT_NOW
use accuracy as the only primary metric        NOT_NOW
compare models                                 DEFER -> preprocessing-evaluation-plan-locked
apply automatic oversampling immediately       NOT_NOW
```

The key methodological distinction is that training missingness alone does not justify locking a production strategy. If serving missingness may occur, preprocessing must be trained on training data and consistently applied, while the project still needs to understand the intended production missingness regime before choosing among plausible strategies. Likewise, class imbalance does not mechanically imply one resampling method or make accuracy sufficient by itself.

---

## 8. Why these cases are better than merely relabeling RA-02

The new benchmark is not created by changing the two failed Specification 015 labels from `DEFER` to `NOT_NOW`.

Instead:

```text
old ambiguous actions
    remain historical Specification 015 truth

new DEFER actions
    are deliberately different actions or project states
    with explicit activating triggers

new NOT_NOW actions
    deliberately have no activating trigger relation
```

This is necessary to avoid post-hoc repair.

It also lets the next experiment test a stronger substantive question:

> Once exact sequencing truth is no longer ambiguous, does explicit methodological knowledge improve action calibration or reasoning quality?

---

## 9. Deterministic evaluation remains primary

For every successful reasoner output, compute at least:

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
unsupported methodological-basis references
```

A `defer-pointer error` includes:

```text
expected DEFER but wrong or null pointer
predicted DEFER with an unknown pointer
predicted non-DEFER carrying a pointer
```

The experiment should report disposition and pointer performance separately so a correct label with a wrong dependency cannot hide inside one score.

---

## 10. Keep a condition-blinded semantic judge

Deterministic action truth is not enough to establish that the reasoning is methodologically sound.

A condition-blinded judge should continue to score frozen obligations for:

```text
why the action is required or merely recommended
why an explicit dependency justifies DEFER
why unknown context remains unresolved
why unrelated expansion is not justified
whether the recommendation contradicts supplied project evidence
```

The judge must not see:

```text
condition identity
methodological context
context digest
token usage
selection metadata
paired outputs
```

It scores only the candidate result against the frozen project evidence, action menu, trigger menu, and rubric.

---

## 11. Expand the preregistered value signals slightly

Specification 015 intentionally did not count semantic-score superiority as a promotion signal. That made one observed semantic improvement descriptive only.

For the next experiment, semantic quality is legitimately part of downstream recommendation value and should be preregistered before observation.

Acceptable positive signals should include:

```text
SELECTIVE aggregate exact disposition accuracy >= GENERIC + 0.05
SELECTIVE aggregate semantic score >= GENERIC + 0.05
SELECTIVE fewer critical omissions than GENERIC
SELECTIVE fewer blocking-scope false negatives than GENERIC
SELECTIVE fewer under-recommendations than GENERIC
SELECTIVE fewer required-clarification false negatives than GENERIC
SELECTIVE fewer defer-pointer errors than GENERIC
SELECTIVE lower unnecessary recommended cost than FULL_HORIZON
SELECTIVE fewer over-recommendations than FULL_HORIZON
SELECTIVE fewer blocking-scope false positives than FULL_HORIZON
```

This is not result-driven tuning because the signal set is frozen before Specification 017 implementation or live outputs.

A semantic-score advantage alone should still be substantial enough to matter, hence the proposed `+0.05` margin.

---

## 12. Preserve absolute and non-inferiority gates

SELECTIVE should not be promoted just because one metric beats a control.

Absolute gates should require:

```text
0 critical action omissions
0 blocking-scope false negatives
0 unsupported methodological-basis failures
0 defer-pointer errors
0 required-clarification false negatives
aggregate exact disposition accuracy >= 0.90
every case exact disposition accuracy >= 0.85
aggregate semantic score >= 0.90
every case semantic score >= 0.85
```

Relative non-inferiority should require SELECTIVE not to materially regress against GENERIC or FULL_HORIZON on aggregate/per-case exact accuracy or semantic quality.

Expansion gates should continue to require SELECTIVE to be no worse than FULL_HORIZON on unnecessary recommended cost, over-recommendations, and blocking-scope false positives.

The exact numerical margins belong in Specification 017 and the fixture.

---

## 13. Keep an informative no-differentiation outcome

The benchmark must remain capable of saying that explicit knowledge did not add measurable downstream value.

Frozen outcome classes should be:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
    all absolute, relative, and expansion gates pass
    + at least one preregistered positive value signal

SAFE_BUT_NOT_DIFFERENTIATED
    all absolute, relative, and expansion gates pass
    + no preregistered positive value signal

FAIL
    any frozen safety/quality/non-inferiority/expansion gate fails
```

This is important because a strong GENERIC reasoner may still solve the benchmark nearly perfectly. That would be evidence about marginal system value, not an experiment-design failure.

---

## 14. Runtime and call plan

For attribution, keep the same concrete bounded treatment used in Specifications 014-016:

```text
reasoner
    provider OpenAI
    runtime OpenAI Agents SDK 0.19.4 behind ADS-owned ReasoningRuntime
    model gpt-5.6-sol
    reasoning effort medium
    text verbosity low
    max output tokens 4000
    no tools
    no previous response state

judge
    same model/runtime
    reasoning effort high
    text verbosity low
    max output tokens 4000
    no tools
    condition blinded
```

This remains an experiment constant only.

Call plan:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
90 maximum provider attempts
one retry per planned call only for frozen infrastructure/structured-output failure classes
semantic disagreement is never a retry reason
```

Use a new deterministic randomization seed and freeze both reasoner and judge plans before provider calls.

---

## 15. Provider input and context size remain descriptive

Specification 014 already established a bounded context-efficiency result. Specification 017 should continue recording:

```text
provider input tokens
output tokens
reasoning tokens when exposed
latency
serialized context bytes
SELECTIVE/FULL ratios
```

but these should not replace the recommendation/action gates.

A SELECTIVE treatment that is cheaper but makes worse project recommendations should fail.

---

## 16. Explicit non-goals

Specification 017 should not attempt to solve:

```text
natural-language project state -> reasoning-function derivation
open-world free-form proposal discovery
production DEFER / NOT_NOW enum design
complete Foundation 018 dependency-relation schema
automatic mutation of Proposal / Question / Investigation / Decision state
automatic execution
human approval policy
final recommendation ranking/priority model
risk/admissibility policy
multi-agent recommendation review
production semantic retrieval stack
frontend/Cockpit wiring
final provider/model selection
```

The experiment stops before authoritative project mutation.

---

## 17. Recommended sequence after freeze

```text
1. freeze Specification 017 and a new benchmark fixture
2. freeze the new relation-backed RecommendationActionResult contract
3. implement deterministic disposition/pointer/action evaluators
4. build provider-free GENERIC / SELECTIVE / FULL_HORIZON condition construction
5. add fake-runtime and real-persistence integration coverage
6. add ordinary Ubuntu/Windows CI with no provider credential
7. preserve the exact provider-free implementation head
8. only then expose an explicit secret-gated live workflow
9. execute the frozen live plan once
10. preserve the complete raw artifact before interpretation or design changes
```

No Specification 017 live provider call should occur before the contract is frozen and the exact implementation head is green.
