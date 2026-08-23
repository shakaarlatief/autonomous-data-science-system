# Specification 016: V1 Disposition Semantics Failure-Attribution Diagnostic

**Version:** 0.1  
**Date:** 2026-08-23  
**Status:** Frozen bounded diagnostic contract before implementation or new live model calls  
**Scope:** Determine whether a stronger dependency-backed `DEFER` definition is operationally separable from `NOT_NOW` and reliably classifiable on deliberately unambiguous contrastive project microstates.  
**Authority:** Governs the first post-Specification-015 disposition-semantics diagnostic until its result is preserved. It does not modify Specification 015, promote a production recommendation taxonomy, establish recommendation-system value, authorize project mutation, or select a final provider/model.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

Specification 015 completed under its unchanged frozen contract and returned advancement outcome:

```text
FAIL
```

The failed implementation PR #13 was closed without merge. Its exact negative evidence was preserved separately through PR #14, merged into `v1-frontend-spike` at:

```text
10aa3f59bedc5ee45a38f0ae05c68da901d9adff
```

This diagnostic branch starts exactly from that preserved accepted integration boundary:

```text
v1-disposition-semantics-diagnostic
```

Primary prerequisite evidence:

```text
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Research rationale:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
```

Frozen benchmark fixture:

```text
tests/fixtures/reasoning/disposition_semantics_v1.json
```

The frozen question is:

> When `DEFER` is defined as an explicit dependency-backed sequencing relation and `NOT_NOW` as absence of current justification plus absence of such an activating relation, can the distinction be represented deterministically and applied reliably by the fixed reasoner on deliberately unambiguous contrastive states?

---

## 2. Why this is not another recommendation-value experiment

Specification 015 simultaneously exercised:

```text
recommendation taxonomy
project-state interpretation
methodological context treatment
reasoner calibration
deterministic exact-label evaluation
```

Its only failed hard gate was concentrated in `DEFER` versus `NOT_NOW`, with nearly identical behavior across GENERIC, SELECTIVE, and FULL_HORIZON.

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

If the label boundary itself is not operationally stable, another system-value comparison would be premature.

---

## 3. Historical Specification 015 remains immutable

Nothing in Specification 016 changes:

```text
Specification 015 fixture
Specification 015 expected dispositions
Specification 015 thresholds
Specification 015 live outputs
Specification 015 frozen FAIL result
```

In particular, the two historical RA-02 actions remain historical `DEFER` labels under the original contract.

Specification 016 introduces a **new, stricter construction rule** for future diagnostic cases. It may show that the historical examples would not qualify as unambiguous DEFER examples under the new rule, but it cannot retroactively rescore them.

---

## 4. Frozen operational semantics

Only two dispositions exist in this diagnostic.

### DEFER

An action may be classified `DEFER` only when the supplied state establishes all of:

```text
D1. the action is already justified for the represented project plan;
D2. a specific supplied prerequisite/trigger is currently unresolved;
D3. the prerequisite/trigger has an exact allowed trigger ID;
D4. once that trigger is satisfied, the supplied state represents the action
    as current next work under the otherwise relevant plan.
```

A valid DEFER result must include:

```text
defer_until_id = exact supplied activating trigger ID
```

The possibility that an action could become useful someday is insufficient.

### NOT_NOW

An action is `NOT_NOW` when:

```text
N1. the current objective/state does not materially justify prioritizing it; and
N2. no represented supplied prerequisite/trigger establishes that satisfying
    one current dependency makes the action current next work.
```

A valid NOT_NOW result must include:

```text
defer_until_id = null
```

### Diagnostic distinction

```text
DEFER
    later because this represented trigger must occur first

NOT_NOW
    not in the current represented plan; no activating trigger relation exists
```

These are experiment semantics, not production enums.

---

## 5. Frozen contrastive benchmark

The fixture contains exactly six pairs:

```text
DS-01  model-tuning
DS-02  subgroup-error-analysis
DS-03  feature-interaction-engineering
DS-04  missingness-sensitivity
DS-05  probability-calibration
DS-06  distribution-evidence
```

Every pair has exactly two variants:

```text
DEFER variant
NOT_NOW variant
```

Within one pair, the following are shared:

```text
candidate action ID and label
available trigger menu
shared project evidence
output schema
reasoner instruction
model/runtime treatment
```

Only `variant_evidence` differs.

The DEFER variant must explicitly represent one unresolved activating trigger and the action as current next work after that trigger.

The NOT_NOW variant must explicitly state that the supplied trigger is not an activator for the action and that no represented current dependency makes the action next work.

Expected truth is evaluator-only and must never enter the reasoner payload.

---

## 6. Provider-free construction audit

Before any live model call, implementation must mechanically validate the fixture.

Required checks:

```text
exactly 6 pairs
exactly 2 variants per pair
one expected DEFER and one expected NOT_NOW variant per pair
pair action identical across variants
pair trigger menu identical across variants
shared project evidence identical across variants
DEFER expected_defer_until_id is one supplied trigger
NOT_NOW expected_defer_until_id is null
no expected label/pointer enters the reasoner input
all variant IDs unique
all pair IDs unique
```

The provider-free audit must also verify that the canonical reasoner input is deterministic for the same plan entry and that evaluator truth is absent.

If any construction check fails, the live diagnostic is not permitted to run.

---

## 7. Frozen reasoner input

For each planned call, the reasoner receives only:

```text
condition-neutral run nonce
common instruction
user task
candidate action ID + label
available trigger IDs + descriptions
shared project evidence
variant project evidence
structured output schema
```

The reasoner does not receive:

```text
pair expected disposition
expected defer_until_id
hard-gate thresholds
aggregate result state
other repetitions
other pair variants
Specification 015 observed outputs
methodological knowledge assets
retrieval/Horizon/context metadata
```

The run nonce must occur before any evaluator-neutral payload that could otherwise be shared across repetitions.

---

## 8. Experiment-only structured result

Use an ADS-owned experiment result conceptually equivalent to:

```text
DispositionSemanticsResult
    disposition: DEFER | NOT_NOW
    defer_until_id: str | None
    rationale: str
```

Validation:

```text
DEFER
    defer_until_id must be exactly one supplied trigger ID

NOT_NOW
    defer_until_id must be null

unknown disposition
    invalid structured response

unknown trigger ID
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
```

and must not emit authoritative acceptance/execution events.

The experiment may use temporary isolated persistence only where needed for harness consistency, but authoritative project/knowledge state must remain unchanged.

---

## 10. Frozen reasoner treatment

Use the same concrete treatment family as Specifications 014-015 to avoid introducing a model/runtime change during failure attribution:

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
for the primary classification.
```

Rationales are preserved for post-result inspection only.

No rationale interpretation may override the deterministic frozen classification after seeing results.

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
2026082302
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

### DS-M01 Exact disposition accuracy

For every successful observation:

```text
predicted disposition == expected disposition
```

Aggregate accuracy:

```text
correct observations / 36
```

### DS-M02 Variant repetition success

For each of 12 variants:

```text
number of repetitions with exact expected disposition
```

### DS-M03 Pair polarity success

For each pair, evaluate the two sides separately:

```text
DEFER side correct repetitions
NOT_NOW side correct repetitions
```

### DS-M04 Exact DEFER trigger-pointer accuracy

Across all 18 expected-DEFER observations:

```text
predicted disposition == DEFER
and
predicted defer_until_id == expected_defer_until_id
```

### DS-M05 NOT_NOW null-pointer correctness

Across all 18 expected-NOT_NOW observations:

```text
predicted disposition == NOT_NOW
and
defer_until_id is null
```

### DS-M06 Invalid successful-output count

Count successful runtime responses that fail the experiment result contract after structured materialization.

Such attempts are retryable once under the frozen retry rule and must remain in the attempt ledger.

---

## 14. Frozen hard gates

A completed diagnostic earns `DISPOSITION_BOUNDARY_SUPPORTED` only if **all** gates pass.

### DS-G01 Structured validity

```text
invalid successful outputs after final planned-call resolution == 0
```

### DS-G02 Aggregate disposition accuracy

```text
aggregate exact disposition accuracy >= 0.95
```

With 36 observations this permits at most one exact-label miss.

### DS-G03 Every variant is majority-correct

For every one of the 12 variants:

```text
correct repetitions >= 2 / 3
```

### DS-G04 Every contrastive pair has both sides majority-correct

For every pair:

```text
DEFER side correct repetitions    >= 2 / 3
NOT_NOW side correct repetitions  >= 2 / 3
```

This is intentionally redundant with DS-G03 at the implementation level because the pair is the conceptual unit of separability and must appear explicitly in the result.

### DS-G05 Exact DEFER pointer

Across all expected-DEFER observations:

```text
exact trigger-pointer accuracy == 1.00
```

All 18 expected-DEFER outputs must both classify DEFER and identify the exact activating trigger.

### DS-G06 NOT_NOW pointer absence

Across all expected-NOT_NOW observations:

```text
null-pointer correctness == 1.00
```

All 18 expected-NOT_NOW outputs must both classify NOT_NOW and return no defer pointer.

---

## 15. Frozen outcomes

Exactly one result is allowed.

### DISPOSITION_BOUNDARY_SUPPORTED

Requirements:

```text
all 36 planned successful observations obtained
all DS-G01 through DS-G06 pass
```

Supported conclusion:

> A dependency-backed `DEFER` definition is operationally representable and the fixed reasoner can distinguish it from `NOT_NOW` on the frozen deliberately unambiguous contrastive microstates.

This does not establish recommendation-system value or production taxonomy promotion.

### DISPOSITION_BOUNDARY_NOT_SUPPORTED

Requirements:

```text
all 36 planned successful observations obtained
at least one DS-G01 through DS-G06 fails
```

Required next interpretation:

```text
do not run another recommendation-value comparison with the same distinction;
consider collapsing the labels or representing sequencing as an explicit dependency relation.
```

### INCOMPLETE

Use only when the complete planned successful observation set cannot be obtained under the frozen attempt/retry cap or when execution integrity cannot be verified.

No semantic-boundary conclusion is permitted.

---

## 16. Failure-attribution interpretation matrix

This diagnostic is intended to narrow the Specification 015 failure source.

### If boundary is supported

Evidence supports:

```text
A is less likely under explicit relational semantics:
    DEFER and NOT_NOW can be operationally separated.

C is less likely for deliberately unambiguous cases:
    the reasoner can apply the distinction when evidence is explicit.
```

The historical RA-02 discrepancy then remains consistent with:

```text
B: the original benchmark did not encode a uniquely activating DEFER relation strongly enough.
```

That is still not a retroactive rescore.

A later recommendation-value experiment may test D using newly frozen cases that satisfy the stronger construction rule.

### If boundary is not supported

Evidence supports either:

```text
A: the taxonomy remains operationally unstable;
or
C: the fixed reasoner cannot reliably apply even an explicit version of the distinction.
```

In either case, another SELECTIVE-vs-control recommendation-value experiment using the same four labels is not justified.

---

## 17. Historical RA-02 admissibility diagnostic

Under Specification 016, an expected DEFER benchmark example is admissible only if it contains an explicit activating trigger relation satisfying D1-D4.

The two historical RA-02 DEFER examples from Specification 015 are not rewritten and are not part of the new hard benchmark.

The implementation may include a provider-free historical construction audit that reports:

```text
RA-02 historical examples
    NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER
```

if they lack the new explicit trigger relation.

This report is descriptive failure attribution only and does not modify their original Specification 015 truth.

---

## 18. Provider-free implementation requirements

Before live execution, ordinary CI must validate at minimum:

```text
fixture construction rules
reasoner input excludes evaluator truth
exact output contract
DEFER/NOT_NOW pointer invariants
deterministic randomized plan and plan digest
36-call fake-runtime completeness
retry/attempt accounting
45-attempt hard cap
outcome calculation
historical RA-02 admissibility diagnostic
no provider credential in ordinary CI
no authoritative project/knowledge mutation
no application/domain import of provider SDK types
```

The provider-free fake runtime must cover at least:

```text
perfect pass -> DISPOSITION_BOUNDARY_SUPPORTED
one allowed aggregate miss but all other gates -> result according to exact frozen gates
variant majority failure -> DISPOSITION_BOUNDARY_NOT_SUPPORTED
pointer failure -> DISPOSITION_BOUNDARY_NOT_SUPPORTED
incomplete attempt budget -> INCOMPLETE
```

---

## 19. Live workflow boundary

No live workflow may be executed until:

```text
Specification 016 and fixture are committed and frozen
provider-free implementation is complete
dedicated ordinary CI is green on Ubuntu and Windows where applicable
exact source head is preserved in a pre-live checkpoint
```

The live workflow must be:

```text
manual only
secret-gated
branch-guarded
explicit confirmation-gated
```

Suggested confirmation literal:

```text
RUN_SPEC_016_FROZEN
```

The complete result directory must be uploaded even when the internal diagnostic result is non-supporting.

GitHub workflow success must remain distinct from diagnostic-gate success.

---

## 20. Result preservation

Before any tuning or next-experiment design, preserve:

```text
frozen source head
fixture and specification digests
randomized plan + digest
all raw provider attempts
all successful structured observations
usage/trace data
aggregate/per-pair/per-variant metrics
hard-gate evaluation
final frozen outcome
human-readable result report
```

No threshold, expected disposition, expected trigger pointer, prompt, model, repetition count, or retry policy may change after the first live result is observed.

---

## 21. Explicit non-selections

Specification 016 does not select or establish:

```text
production DEFER / NOT_NOW enums
production recommendation ranking
production REQUIRED/BLOCKING policy
open-world action generation
SELECTIVE recommendation value
project-state -> reasoning-function derivation
automatic Proposal/Question/Investigation/Decision mutation
automatic execution
human approval/escalation policy
final LLM provider/model or reasoning effort
multi-agent recommendation architecture
new retrieval/reranking/vector infrastructure
```

---

## 22. Exact implementation continuation

After this contract and fixture are frozen:

```text
1. create the experiment-only result type and validator
2. implement fixture construction/admissibility audit
3. implement deterministic call-plan and gate evaluator
4. implement fake runtime and complete provider-free integration test
5. add dedicated ordinary CI with no provider credential
6. preserve exact green implementation head in the next checkpoint
7. only then add/expose the manual secret-gated live workflow
8. make no live call before that pre-live checkpoint is green
```
