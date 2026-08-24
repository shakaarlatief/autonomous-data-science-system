# Specification 020: V1 RECOMMENDED versus BLOCKING_REQUIRED Calibration Diagnostic

**Version:** 0.1  
**Date:** 2026-08-24  
**Status:** Frozen bounded diagnostic contract before implementation or new live model calls  
**Scope:** Determine whether a stronger dependency-backed `BLOCKING_REQUIRED` definition is operationally separable from `RECOMMENDED` and reliably classifiable on deliberately unambiguous contrastive project microstates.  
**Authority:** Governs the first post-Specification-019 recommendation/blocking calibration diagnostic until its result is preserved. It does not modify Specification 019, promote a production recommendation taxonomy, establish recommendation-system value, authorize project mutation, or select a final provider/model.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

Specification 019 completed under its frozen contract and returned:

```text
FAIL
```

The failed recommendation/action implementation was closed without merge. Its frozen contract, raw result, interpreted report, and checkpoints were preserved separately into `v1-frontend-spike`.

The accepted integration branch was then reconciled through Checkpoint 166 and validated at:

```text
b9c9c3a38935983075a9ca88632177980bb20ede
```

Provider-free integration validation observed:

```text
Checkpoint metadata       run 32695017695   success
V1 frontend spike         run 32695017696   success
Ubuntu build/unit                              success
Windows build/unit                             success
Chromium browser/accessibility/visual gate     success
```

This diagnostic branch starts exactly from that integration boundary:

```text
v1-blocking-calibration-diagnostic
```

Research rationale:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
```

Frozen benchmark fixture:

```text
tests/fixtures/reasoning/blocking_calibration_v1.json
```

The frozen question is:

> When `BLOCKING_REQUIRED` is defined as an explicit relation from a currently justified action to one unresolved requirement that blocks one exact active defended downstream scope, can the fixed reasoner distinguish it reliably from worthwhile but non-blocking `RECOMMENDED` work on deliberately unambiguous contrastive states?

---

## 2. Why this is not another recommendation-value experiment

Specification 019 simultaneously exercised:

```text
recommendation taxonomy
project-state interpretation
methodological context treatment
reasoner calibration
semantic judging
relative system-value comparison
```

The central RB-02 discrepancy involved repeated escalation from:

```text
RECOMMENDED
```

into:

```text
BLOCKING_REQUIRED
```

while GENERIC and FULL_HORIZON showed a similar tendency less consistently.

Therefore this diagnostic deliberately removes:

```text
GENERIC vs SELECTIVE vs FULL_HORIZON comparison
reusable methodological assets
retrieval
MethodologicalHorizon construction
selective context
recommendation-value signals
semantic judge
open-world action discovery
```

If the blocking boundary itself is not operationally stable, another system-value comparison would be premature.

---

## 3. Historical Specification 019 remains immutable

Nothing in Specification 020 changes:

```text
Specification 019 fixture
Specification 019 expected dispositions
Specification 019 expected scopes or dependency pointers
Specification 019 thresholds
Specification 019 live outputs
Specification 019 frozen FAIL result
```

In particular, RB-02 remains historical evidence under its original contract.

Specification 020 introduces a new, stricter construction rule for future diagnostic cases. It may show that stronger explicit blocked-scope relations improve calibration, but it cannot retroactively rescore or reinterpret Specification 019.

---

## 4. Frozen operational semantics

Only two dispositions exist in this diagnostic.

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

A valid BLOCKING_REQUIRED result must include:

```text
blocking_requirement_id = exact supplied unresolved requirement ID
blocked_scope_id        = exact supplied active downstream scope ID
```

The following are insufficient by themselves:

```text
high priority
high expected value
common best practice
possible future usefulness
generic sequencing preference
"should happen before later work"
"would improve confidence"
```

### RECOMMENDED

An action is `RECOMMENDED` when:

```text
R1. the current supplied state materially justifies doing the action now or soon; and
R2. no exact currently active supplied downstream scope is represented as
    depending on completion of this action through an unresolved requirement.
```

A valid RECOMMENDED result must include:

```text
blocking_requirement_id = null
blocked_scope_id        = null
```

The action may still improve evidence, robustness, performance, understanding, or decision quality.

### Diagnostic distinction

```text
BLOCKING_REQUIRED
    this exact defended scope depends on this exact unresolved requirement,
    and this action resolves that requirement

RECOMMENDED
    worthwhile current work, but no exact active defended scope is blocked on it
```

These are experiment semantics, not production enums.

---

## 5. Frozen contrastive benchmark

The fixture contains exactly six pairs:

```text
BC-01  prediction-time feature availability
BC-02  temporal validation sensitivity
BC-03  missing-data treatment sensitivity
BC-04  subgroup error analysis
BC-05  probability calibration assessment
BC-06  nonlinear model-family comparison
```

Every pair has exactly two variants:

```text
BLOCKING_REQUIRED variant
RECOMMENDED variant
```

Within one pair, the following are shared:

```text
candidate action ID and label
available requirement menu
available downstream-scope menu
shared project evidence
output schema
reasoner instruction
model/runtime treatment
```

Only `variant_evidence` differs.

The BLOCKING_REQUIRED variant must explicitly represent:

```text
one unresolved supplied requirement
one active defended supplied downstream scope
one explicit scope DEPENDS_ON requirement relation
the candidate action as the represented resolver of that requirement
```

The RECOMMENDED variant must explicitly represent the action as worthwhile while also representing that no current active supplied scope is blocked on it.

Expected truth is evaluator-only and must never enter the reasoner payload.

---

## 6. Provider-free construction audit

Before any live model call, implementation must mechanically validate the fixture.

Required checks:

```text
exactly 6 pairs
exactly 2 variants per pair
one expected BLOCKING_REQUIRED and one expected RECOMMENDED variant per pair
pair action identical across variants
pair requirement menu identical across variants
pair downstream-scope menu identical across variants
shared project evidence identical across variants
BLOCKING_REQUIRED expected requirement is one supplied requirement
BLOCKING_REQUIRED expected scope is one supplied downstream scope
RECOMMENDED expected requirement is null
RECOMMENDED expected scope is null
all variant IDs unique
all pair IDs unique
expected truth never enters reasoner input
```

The provider-free audit must also verify that the canonical reasoner input is deterministic for the same plan entry.

If any construction check fails, the live diagnostic is not permitted to run.

---

## 7. Frozen reasoner input

For each planned call, the reasoner receives only:

```text
condition-neutral run nonce
common instruction
user task
candidate action ID + label
available requirement IDs + descriptions
available downstream-scope IDs + descriptions
shared project evidence
variant project evidence
structured output schema
```

The reasoner does not receive:

```text
pair expected disposition
expected blocking requirement pointer
expected blocked-scope pointer
hard-gate thresholds
aggregate result state
other repetitions
other pair variants
Specification 019 observed outputs
methodological knowledge assets
retrieval/Horizon/context metadata
```

The run nonce must occur before any evaluator-neutral payload that could otherwise be shared across repetitions.

---

## 8. Experiment-only structured result

Use an ADS-owned experiment result conceptually equivalent to:

```text
BlockingCalibrationResult
    disposition: BLOCKING_REQUIRED | RECOMMENDED
    blocking_requirement_id: str | None
    blocked_scope_id: str | None
    rationale: str
```

Validation:

```text
BLOCKING_REQUIRED
    blocking_requirement_id must be exactly one supplied requirement ID
    blocked_scope_id must be exactly one supplied downstream-scope ID

RECOMMENDED
    blocking_requirement_id must be null
    blocked_scope_id must be null

unknown disposition
    invalid structured response

unknown requirement ID
    invalid structured response

unknown downstream-scope ID
    invalid structured response

empty rationale
    invalid structured response
```

This type is not a production Proposal/Recommendation object and must not be persisted as authoritative project state.

---

## 9. No authoritative project mutation

The diagnostic is read/reason/evaluate only.

It must not create or update:

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

and must not emit authoritative acceptance/execution events.

The experiment may use temporary isolated persistence only where needed for harness consistency, but authoritative project/knowledge state must remain unchanged.

---

## 10. Frozen reasoner treatment

Use the same concrete treatment family as adjacent V1 reasoning experiments so a new model/runtime change does not become another confound:

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

This is a diagnostic constant only. It does not select a final production model/provider or reasoning effort.

Every successful live call must preserve where available:

```text
requested model
provider model identity
runtime/package identity
reasoning effort
verbosity
output limit
input/output/total token usage
cached input token usage
reasoning token usage
latency
service tier
provider response/request identifiers
```

---

## 11. No semantic judge

No LLM judge is used in the hard result.

Reason:

```text
the diagnostic is specifically testing whether evaluator truth
can be made structural enough not to require another semantic model
for the primary classification
```

Rationales are preserved for post-result inspection only.

No rationale interpretation may override deterministic frozen classification after seeing results.

---

## 12. Frozen call plan

```text
6 pairs
2 variants per pair
3 repetitions per variant

12 variants
36 planned successful reasoner calls
45 maximum total provider attempts
```

Randomization seed:

```text
2026082401
```

The complete plan must be generated and hashed before the first provider call.

Each planned call receives an opaque deterministic run ID and a unique condition-neutral nonce.

### Retry policy

At most one retry for one planned call, and only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

Every failed attempt must be preserved in the raw attempt ledger.

Maximum attempts are hard-capped at `45`.

If all 36 successful observations cannot be obtained within that cap, outcome is `INCOMPLETE` and no semantic-boundary conclusion is permitted.

---

## 13. Frozen deterministic metrics

### BC-M01 Exact disposition accuracy

For every successful observation:

```text
predicted disposition == expected disposition
```

Aggregate accuracy:

```text
correct observations / 36
```

### BC-M02 Variant repetition success

For each of 12 variants:

```text
number of repetitions with exact expected disposition
```

### BC-M03 Pair polarity success

For each pair, evaluate the two sides separately:

```text
BLOCKING_REQUIRED side correct repetitions
RECOMMENDED side correct repetitions
```

### BC-M04 Exact blocking requirement-pointer accuracy

Across all 18 expected-BLOCKING_REQUIRED observations:

```text
predicted disposition == BLOCKING_REQUIRED
and
predicted blocking_requirement_id == expected_blocking_requirement_id
```

### BC-M05 Exact blocked-scope pointer accuracy

Across all 18 expected-BLOCKING_REQUIRED observations:

```text
predicted disposition == BLOCKING_REQUIRED
and
predicted blocked_scope_id == expected_blocked_scope_id
```

### BC-M06 Joint blocking-pointer accuracy

Across all 18 expected-BLOCKING_REQUIRED observations:

```text
predicted disposition == BLOCKING_REQUIRED
and
predicted blocking_requirement_id == expected_blocking_requirement_id
and
predicted blocked_scope_id == expected_blocked_scope_id
```

### BC-M07 RECOMMENDED null-pointer correctness

Across all 18 expected-RECOMMENDED observations:

```text
predicted disposition == RECOMMENDED
and
blocking_requirement_id is null
and
blocked_scope_id is null
```

### BC-M08 Invalid successful-output count

Count successful runtime responses that fail the experiment result contract after structured materialization.

Such attempts are retryable once under the frozen retry rule and must remain in the attempt ledger.

---

## 14. Frozen hard gates

A completed diagnostic earns `BLOCKING_BOUNDARY_SUPPORTED` only if all gates pass.

### BC-G01 Structured validity

```text
invalid successful outputs after final planned-call resolution == 0
```

### BC-G02 Aggregate disposition accuracy

```text
aggregate exact disposition accuracy >= 0.95
```

With 36 observations this permits at most one exact-label miss before the stricter pointer gates are considered.

### BC-G03 Every variant is majority-correct

For every one of the 12 variants:

```text
correct repetitions >= 2 / 3
```

### BC-G04 Every contrastive pair has both sides majority-correct

For every pair:

```text
BLOCKING_REQUIRED side correct repetitions >= 2 / 3
RECOMMENDED side correct repetitions         >= 2 / 3
```

This is intentionally explicit even though it overlaps BC-G03 because pair polarity is the conceptual unit of separability.

### BC-G05 Exact joint blocking pointers

Across all expected-BLOCKING_REQUIRED observations:

```text
joint blocking-pointer accuracy == 1.00
```

All 18 expected-BLOCKING_REQUIRED outputs must classify the action as blocking and identify both the exact unresolved requirement and exact blocked scope.

### BC-G06 RECOMMENDED pointer absence

Across all expected-RECOMMENDED observations:

```text
RECOMMENDED null-pointer correctness == 1.00
```

All 18 expected-RECOMMENDED outputs must classify the action as recommended and return both pointer fields null.

### Strictness note

BC-G05 and BC-G06 intentionally make support effectively require exact side correctness across all 36 observations. This is deliberate because the benchmark is designed as a construct-validity diagnostic with explicit unambiguous relations, not a noisy production benchmark. This strictness is frozen before implementation and must not be weakened after results are observed.

---

## 15. Frozen outcomes

Exactly one result is allowed.

### BLOCKING_BOUNDARY_SUPPORTED

Requirements:

```text
all 36 planned successful observations obtained
all BC-G01 through BC-G06 pass
```

Supported conclusion:

> A dependency-backed `BLOCKING_REQUIRED` definition is operationally representable and the fixed reasoner can distinguish it from `RECOMMENDED` on the frozen deliberately unambiguous contrastive microstates.

This does not establish recommendation-system value or production taxonomy promotion.

### BLOCKING_BOUNDARY_NOT_SUPPORTED

Requirements:

```text
all 36 planned successful observations obtained
at least one BC-G01 through BC-G06 fails
```

Required next interpretation:

```text
do not run another recommendation-value comparison with the same blocking distinction unchanged;
consider whether blocking must be represented deterministically from project relations rather than classified by the reasoner,
or whether the production taxonomy should avoid a separate blocking disposition.
```

### INCOMPLETE

Use only when the complete planned successful observation set cannot be obtained under the frozen attempt/retry cap or when execution integrity cannot be verified.

No semantic-boundary conclusion is permitted.

---

## 16. Failure-attribution interpretation matrix

### If boundary is supported

Evidence supports:

```text
A is less likely under explicit relational semantics:
    RECOMMENDED and BLOCKING_REQUIRED can be operationally separated.

C is less likely for deliberately unambiguous cases:
    the reasoner can apply the distinction when requirement and blocked-scope
    relations are explicit.
```

Specification 019's RB-02 behavior then remains consistent with benchmark/state construction that did not make the blocked-scope relation uniquely explicit enough for deterministic calibration.

That is not a retroactive rescore.

A later recommendation-value experiment may test system value using newly frozen cases that satisfy the stronger construction rule.

### If boundary is not supported

Evidence supports either:

```text
A: the taxonomy remains operationally unstable;
or
C: the fixed reasoner cannot reliably apply even an explicit version of the distinction.
```

In either case, another SELECTIVE-versus-control recommendation-value experiment using the same blocking label is not justified.

---

## 17. System-owned provenance boundary

Specification 019 established a durable instrumentation lesson:

```text
SYSTEM
    owns exact supplied context identities and payload provenance

MODEL
    owns recommendation content
```

Specification 020 preserves that separation.

For this diagnostic, the system additionally owns the supplied stable IDs for:

```text
requirements
downstream scopes
candidate action
```

The model may select only from those supplied identities. It must not manufacture authoritative project relations.

---

## 18. Implementation boundary

Only after this contract and fixture are committed and checkpointed may provider-free implementation begin.

Implementation may add:

```text
experiment-only BlockingCalibrationResult
fixture loader and construction audit
deterministic randomized plan builder
truth-blinded reasoner request builder
pointer validation
attempt ledger
deterministic gate evaluator
fake-runtime integration path
provider-free CI
```

Implementation must not add a live workflow or provider credential path until an exact implementation head passes all provider-free gates and a later checkpoint explicitly freezes the live boundary.

---

## 19. Promotion boundary

Specification 020 v0.1 is diagnostic authority only.

It does not promote:

```text
production BLOCKING_REQUIRED semantics
production RECOMMENDED semantics
production recommendation ranking
production dependency persistence schema
SELECTIVE recommendation value
automatic project mutation or execution
final provider/model policy
multi-agent recommendation architecture
```

Historical Specifications 015-019 remain immutable.

No new provider call is authorized by this specification.