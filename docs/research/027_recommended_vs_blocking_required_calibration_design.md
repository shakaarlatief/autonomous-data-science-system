# Research 027: RECOMMENDED versus BLOCKING_REQUIRED Calibration Design

**Date:** 2026-08-24  
**Status:** Design rationale for a separately versioned post-Specification-019 diagnostic  
**Scope:** Isolate whether `RECOMMENDED` versus `BLOCKING_REQUIRED` can be represented as an explicit dependency-backed distinction and classified reliably before any further recommendation-value experiment.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Trigger

Specification 019 completed the full matched recommendation/action experiment after moving exact supplied-context provenance into deterministic system ownership.

The instrumentation repair worked, but the scientific advancement result remained:

```text
FAIL
```

The central local failure was RB-02. SELECTIVE repeatedly labeled two useful nonlinear model-comparison actions:

```text
BLOCKING_REQUIRED
```

when the frozen truth was:

```text
RECOMMENDED
```

GENERIC and FULL_HORIZON showed the same over-blocking tendency less consistently. The result therefore does not support a simple explanation that selective methodological context alone caused the semantic problem.

The immediate question is narrower:

> What exact project-state relation makes worthwhile work merely recommended versus genuinely blocking for a defended downstream scope?

## 2. Why another recommendation-value comparison is premature

Specifications 015, 017, and 019 progressively separated several concerns:

```text
recommendation taxonomy
sequencing semantics
methodological context treatment
reasoner calibration
context provenance
semantic judging
system-value comparison
```

Specification 016 already showed that one ambiguous disposition boundary became reliably classifiable after it was represented relationally:

```text
DEFER
    action already justified
    + exact unresolved activating dependency
    + exact trigger pointer

NOT_NOW
    no represented activating dependency
```

Specification 019 suggests the remaining calibration problem may have the same structural character. `BLOCKING_REQUIRED` may be too easy to interpret as "important" or "should happen before later work" unless the system represents what exact downstream scope is blocked and why.

Therefore the next slice should isolate the construct before reintroducing GENERIC versus SELECTIVE versus FULL_HORIZON.

## 3. Foundational alignment

Foundation 019 distinguishes:

```text
RECOMMENDED
    work judged worth doing now or soon

REQUIRED / BLOCKING
    a downstream action, claim, or deliverable cannot be defended
    until the issue is resolved or explicitly bounded
```

It explicitly states that required is not merely a stronger recommendation.

Foundation 018 separately provides the project semantics needed to represent the distinction:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

and candidate relations such as:

```text
DEPENDS_ON
SUPPORTS
ANSWERS
MOTIVATES
```

A blocking recommendation should therefore be representable as a relation between:

```text
candidate action
    -> unresolved requirement
    -> active defended downstream scope
```

rather than as a high-priority adjective attached to an action.

## 4. Failure hypotheses

The Specification 019 result leaves several explanations open:

```text
A. semantic-taxonomy problem
    RECOMMENDED and BLOCKING_REQUIRED are not operationally explicit enough.

B. benchmark-construction problem
    the frozen examples may not encode necessity strongly enough to make
    blocking uniquely implied by supplied state.

C. reasoner-calibration problem
    the distinction can be represented clearly but the fixed reasoner
    still over-escalates useful work into blocking work.

D. system-value problem
    even after the distinction is operationally stable, explicit
    methodological context may add no recommendation value beyond a
    strong generic reasoner.
```

A new recommendation-value comparison would again mix A/C/D. The diagnostic order should be:

```text
first
    define a structurally explicit blocking relation

then
    test whether one fixed reasoner applies it reliably

only later
    reintroduce methodological-context treatment comparison
```

## 5. Stronger operational distinction

The diagnostic uses only two dispositions.

### BLOCKING_REQUIRED

An action may be classified `BLOCKING_REQUIRED` only when the supplied state establishes all of:

```text
B1. the candidate action is currently justified work;
B2. one exact supplied requirement is unresolved;
B3. one exact supplied downstream scope is active and intended to be defended;
B4. the supplied state explicitly represents that downstream scope as
    depending on resolution of the requirement;
B5. the candidate action is the represented work that resolves or
    establishes the requirement for that scope.
```

A valid result must identify:

```text
blocking_requirement_id = exact supplied requirement ID
blocked_scope_id        = exact supplied downstream scope ID
```

The following are insufficient on their own:

```text
high expected value
high priority
common best practice
possible future usefulness
"do this before modeling"
"this would strengthen confidence"
```

### RECOMMENDED

An action is `RECOMMENDED` when:

```text
R1. the supplied state materially justifies doing the action now or soon;
R2. the action is not represented as a prerequisite for defending any
    exact currently active supplied downstream scope.
```

A valid result must use:

```text
blocking_requirement_id = null
blocked_scope_id        = null
```

The action may still improve evidence, robustness, performance, understanding, or decision quality. It is simply not a represented prerequisite for defending an active downstream scope.

### Diagnostic distinction

```text
BLOCKING_REQUIRED
    this exact defended scope depends on this exact unresolved requirement,
    and this action resolves that requirement

RECOMMENDED
    worthwhile current work, but no exact active defended scope is blocked on it
```

These are experiment semantics only. They do not promote final production enums.

## 6. Why exact blocked-scope pointers matter

A bare blocking label cannot distinguish:

```text
important work
urgent work
prerequisite work
validity-critical work
project-constraint-required work
```

The diagnostic therefore requires the model to identify both the unresolved requirement and the downstream scope that is blocked.

This makes the claim falsifiable:

```text
BLOCKING_REQUIRED
    must point to a supplied requirement
    and a supplied defended scope

RECOMMENDED
    must point to neither
```

The system, not the model, owns the supplied object identities and verifies pointer membership.

## 7. Contrastive benchmark design

Use six heterogeneous action pairs.

Each pair contains:

```text
same candidate action
same requirement menu
same downstream-scope menu
same common instruction
same output schema
same model/runtime treatment
same shared project evidence
```

Only `variant_evidence` differs.

Each pair has:

```text
BLOCKING_REQUIRED variant
    explicit unresolved requirement
    explicit active defended scope
    explicit scope DEPENDS_ON requirement relation
    candidate action explicitly resolves requirement

RECOMMENDED variant
    action explicitly worthwhile
    same requirement/scope identifiers remain visible for contrast
    supplied state explicitly states no current blocking dependency
```

Expected truth is evaluator-only and must never enter the reasoner payload.

## 8. Proposed domains

The six pairs should cover different reasons an action can look important without necessarily being blocking:

```text
BC-01  prediction-time feature availability
BC-02  temporal validation sensitivity
BC-03  missing-data treatment sensitivity
BC-04  subgroup error analysis
BC-05  probability calibration assessment
BC-06  nonlinear model-family comparison
```

These are deliberately controlled microstates rather than attempts to maximize realism. The purpose is construct validity.

## 9. Pair construction sketches

### BC-01 Prediction-time feature availability

Candidate action:

```text
verify whether feature X is available at prediction time
```

Blocking variant:

```text
current deployment candidate uses feature X
active scope: defend model validity for live scoring
requirement: prediction-time availability confirmed
scope explicitly depends on requirement
verification action resolves requirement
```

Recommended variant:

```text
current deployment candidate does not use feature X
verification remains worthwhile for a planned alternative feature set
no active defended scope currently depends on the requirement
```

### BC-02 Temporal validation sensitivity

Candidate action:

```text
run a temporal holdout sensitivity analysis
```

Blocking variant:

```text
active scope: defend future-period performance claim
requirement: temporal representativeness established
current evidence leaves requirement unresolved
sensitivity analysis is the represented work that resolves it
```

Recommended variant:

```text
accepted primary validation already represents the stated deployment regime
sensitivity analysis would strengthen robustness evidence
no active defended scope is blocked on it
```

### BC-03 Missing-data treatment sensitivity

Candidate action:

```text
compare plausible missing-data treatments
```

Blocking variant:

```text
selected pipeline relies on unresolved treatment choice
active scope: defend final preprocessing decision
requirement: treatment robustness established
comparison resolves requirement
```

Recommended variant:

```text
current selected pipeline uses complete primary variables
sensitivity analysis remains useful for optional secondary-variable expansion
no current defended scope depends on it
```

### BC-04 Subgroup error analysis

Candidate action:

```text
run subgroup-specific error analysis
```

Blocking variant:

```text
active deliverable includes a defended subgroup-performance conclusion
requirement: subgroup error behavior characterized
scope explicitly depends on requirement
analysis resolves requirement
```

Recommended variant:

```text
subgroup analysis is useful diagnostic work
current deliverable makes no subgroup-specific defended claim
no active supplied scope depends on it
```

### BC-05 Probability calibration assessment

Candidate action:

```text
assess probability calibration
```

Blocking variant:

```text
active downstream decision interprets predicted probabilities as risk estimates
requirement: probability calibration characterized
scope explicitly depends on requirement
assessment resolves requirement
```

Recommended variant:

```text
current downstream use is ranking only
calibration remains useful diagnostic evidence
no active defended scope depends on calibration quality
```

### BC-06 Nonlinear model-family comparison

Candidate action:

```text
compare one compact nonlinear model family against the accepted linear baseline
```

Blocking variant:

```text
project constitution explicitly requires a defended model-selection decision
only after at least one nonlinear comparator is evaluated
requirement remains unresolved
comparison resolves requirement for the model-selection scope
```

Recommended variant:

```text
accepted linear baseline already satisfies the current deliverable
nonlinear comparison is worthwhile for possible improvement
no current defended scope is blocked on it
```

## 10. Model treatment

Use one reasoner condition only.

Remove:

```text
GENERIC vs SELECTIVE vs FULL_HORIZON
reusable methodological assets
retrieval
MethodologicalHorizon construction
selective context
semantic judge
open-world action discovery
tools
previous response state
project mutation
```

Keep the same concrete reasoner treatment family used in adjacent experiments to avoid introducing a model/runtime change as another confound:

```text
provider                OpenAI
runtime                 OpenAI Agents SDK behind ADS-owned ReasoningRuntime
runtime package         openai-agents==0.19.4
model                   gpt-5.6-sol
reasoning effort        medium
text verbosity          low
max output tokens       2000
fast/priority request   no
previous response       none
runtime tools           none
multi-agent             no
```

This remains an experiment constant only.

## 11. Planned observations

```text
6 pairs
2 variants per pair
3 repetitions per variant

12 variants
36 planned successful reasoner calls
45 maximum provider attempts
```

Use a new deterministic seed frozen before live execution.

Each call receives an opaque deterministic run ID and a unique condition-neutral nonce.

At most one retry is allowed for one planned call, and only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

## 12. Structured output

The minimum diagnostic output is:

```text
BlockingCalibrationResult
    disposition: BLOCKING_REQUIRED | RECOMMENDED
    blocking_requirement_id: string | null
    blocked_scope_id: string | null
    rationale: string
```

Validation rules:

```text
BLOCKING_REQUIRED
    requires one exact supplied blocking_requirement_id
    requires one exact supplied blocked_scope_id

RECOMMENDED
    requires blocking_requirement_id == null
    requires blocked_scope_id == null

unknown requirement/scope IDs
    invalid structured response

empty rationale
    invalid structured response
```

## 13. Deterministic evaluation

Primary metrics:

```text
exact disposition accuracy
exact blocking requirement-pointer accuracy
exact blocked-scope pointer accuracy
joint blocking-pointer accuracy
RECOMMENDED null-pointer correctness
per-variant repetition success
per-pair polarity success
invalid structured-response count
```

No LLM judge is needed for the primary result because benchmark truth is intentionally structural.

## 14. Proposed hard-gate philosophy

The diagnostic should be deliberately strict.

A useful candidate gate set is:

```text
zero unresolved invalid successful outputs
aggregate exact disposition accuracy >= 0.95
every variant >= 2 / 3 correct
every pair both sides >= 2 / 3 correct
all expected BLOCKING_REQUIRED observations identify exact requirement and scope
all expected RECOMMENDED observations return both pointers null
```

The exact gates belong in the frozen Specification 020 contract, not in post-result interpretation.

## 15. Allowed outcomes

A successor specification should permit exactly:

```text
BLOCKING_BOUNDARY_SUPPORTED
BLOCKING_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

If supported, the only justified conclusion is:

> A dependency-backed `BLOCKING_REQUIRED` definition is operationally representable and the fixed reasoner can distinguish it from `RECOMMENDED` on deliberately unambiguous contrastive microstates.

It would not establish:

```text
recommendation-system value
SELECTIVE methodological-context value
production recommendation taxonomy
production dependency schema
automatic project mutation or execution
final provider/model choice
```

If not supported, another recommendation-value comparison using the same blocking distinction should not proceed unchanged.

## 16. Relationship to Specification 019

Specification 019 remains immutable `FAIL` evidence.

This diagnostic must not:

```text
rescore RB-02
rewrite its frozen truth
relax its gates
reinterpret repeated outputs as new benchmark cases
```

It may explain prospectively why the old distinction was difficult to calibrate, but it cannot retroactively change the result.

## 17. Promotion boundary

Research 027 is design rationale only.

The next legitimate repository step is a separately versioned Specification 020 that freezes:

```text
operational semantics
contrastive fixture
reasoner treatment
call plan
retry policy
structured output
hard gates
allowed outcomes
historical-integrity rule
no-project-mutation rule
```

No new provider call is authorized by this research memo.