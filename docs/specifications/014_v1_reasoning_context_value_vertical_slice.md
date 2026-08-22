# Specification 014: V1 Reasoning Context Value Vertical Slice

**Version:** 0.1  
**Date:** 2026-08-22  
**Status:** Frozen bounded implementation/evaluation contract before reasoning-runtime implementation and live model calls  
**Scope:** First real-model comparison of the accepted selective `MethodologicalContextPack` against a compact full-Horizon control under the same ADS-owned runtime/model configuration, with frozen semantic quality and provider-token efficiency gates.  
**Authority:** Governs the first reasoning-context-value implementation and live experiment until its result is preserved. It does not select the final LLM provider/model, final context budget, final semantic relevance mechanism, recommendation policy, or multi-agent architecture.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

PR #11 was merged into `v1-frontend-spike` at:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

This specification starts from a branch created exactly at that promoted merge:

```text
v1-reasoning-context-value
```

Prerequisite accepted evidence:

```text
D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime selected

Specification 012 v1.0 / Checkpoint 141
    first explained MethodologicalHorizon accepted

Specification 013 v1.0 / Checkpoint 143
    first deterministic selective MethodologicalContextPack accepted
```

Frozen benchmark fixture:

```text
tests/fixtures/reasoning/context_value_v1.json
```

Research rationale:

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
```

The frozen question is:

> With the same project/task evidence and the same concrete model/runtime configuration, does the accepted selective methodological context preserve reasoning quality relative to a strong compact full-Horizon control while reducing provider-reported input-token burden?

---

## 2. Experimental treatment

Two conditions are compared.

### SELECTIVE

Construct the accepted Specification 013 pack through:

```text
select_methodological_context(...)
```

using the frozen RH-C task profile and `max_assets = 3` inherited from the accepted selective-context fixture.

### FULL_HORIZON

Materialize every included candidate from the same ten-asset explained wide Horizon using the same exact compact reasoning projection as Specification 013.

The control must use:

```text
schema_version = 1
same task_id
same requested_reasoning_functions
all exact included Horizon revisions
same applicability/missing-context projection
selection_reason = CONTROL_INCLUDED
```

The full control must not serialize:

```text
retrieval terms
aliases
semantic cues
retrieval scores
global export metadata
system omission decisions
governance event prose
```

The existing RH-C integration-test control shape is the reference implementation.

No third context condition is introduced in this first experiment.

---

## 3. Frozen wide Horizon and task context

Reuse:

```text
tests/fixtures/knowledge/reusable_knowledge_stress_v1.json
tests/fixtures/retrieval/selective_context_v1.json
```

Build the same wide Horizon from the six direct seeds:

```text
class-imbalance
histogram
missing-data
prediction-time-feature-eligibility
random-forest
temporal-validation
```

Accepted one-hop expansion must yield:

```text
bagging
ecdf
gradient-boosted-trees
prediction-moment
```

Required included count:

```text
10
```

The benchmark fixture defines additional reasoning-time project evidence per case. That project evidence is identical across conditions.

---

## 4. Frozen reasoning cases

The four cases are defined exactly in:

```text
tests/fixtures/reasoning/context_value_v1.json
```

They correspond to the preceding RH-C classes:

```text
RV-01  MODEL_OPTION
RV-02  EVIDENCE_OPTION
RV-03  VALIDITY_CONSTRAINT
RV-04  DECISION_FRAMEWORK
```

Required SELECTIVE stable-key sets remain:

```text
RV-01
    gradient-boosted-trees
    random-forest

RV-02
    ecdf
    histogram

RV-03
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

RV-04
    class-imbalance
    missing-data
```

The implementation must verify these exact sets before any live reasoner call.

---

## 5. Frozen semantic obligations

Every case contains a preregistered list of semantic obligations in the benchmark fixture.

Judge scores are restricted to:

```text
0  absent, materially wrong, or contradicted
1  partially or implicitly satisfied
2  explicitly and correctly satisfied
```

Each obligation is marked `critical` or non-critical.

Normalized output quality:

```text
sum(scores)
/
(2 * number_of_obligations)
```

The judge may not add, remove, or reinterpret required obligations after observing outputs.

No live result may cause the fixture rubric to be edited before the failed/passed result is preserved.

---

## 6. Concrete reasoner configuration

Use:

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

Do not use the `gpt-5.6` alias. Use the explicit tier identifier:

```text
gpt-5.6-sol
```

Current external model evidence checked before freeze:

```text
https://developers.openai.com/api/docs/models/gpt-5.6-sol
https://developers.openai.com/api/docs/guides/latest-model
```

The public tier identifier is not treated as a date-frozen model snapshot. Every live result must therefore preserve:

```text
requested model identifier
provider-returned model identifier
run timestamp
OpenAI Agents SDK version
OpenAI client/provider package versions where available
reasoning effort
verbosity
max-output setting
```

This concrete model configuration is an experiment treatment constant, not a project-level final model selection.

---

## 7. Concrete judge configuration

Use one condition-blinded semantic judge call per successful reasoner output.

Judge configuration:

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
case user task
case project evidence
frozen obligation rubric
candidate structured reasoning result
```

The judge must not receive:

```text
SELECTIVE / FULL_HORIZON label
methodological context payload
context digest
input-token usage
latency
cost
paired alternate-condition output
```

Judge result structure must include:

```text
output_id
obligation_scores[{obligation_id, score, rationale}]
normalized_score
critical_failure: bool
judge_summary
```

The harness recomputes `normalized_score` from obligation scores and rejects inconsistent judge output.

---

## 8. ADS-owned reasoner result schema

The principal reasoner returns an ADS-owned structured result:

```text
ReasoningContextValueResult
    answer: str
    proposed_actions: tuple[str, ...]
    required_clarifications: tuple[str, ...]
    warnings: tuple[str, ...]
    methodological_basis: tuple[str, ...]
```

The common instruction is frozen in the benchmark fixture.

Deterministic provenance rule:

```text
set(methodological_basis)
    <=
set(stable keys supplied in that condition)
```

An unsupported basis key is an experiment failure independent of semantic judging.

Duplicate basis keys should be rejected by structured-result validation or normalized deterministically according to the implementation contract frozen before live runs.

---

## 9. ADS-owned ReasoningRuntime boundary

This slice must establish a production-facing runtime seam under `src/ads_system`, not only reuse experiment-local Specification 005 classes.

The application layer requires an ADS-owned port conceptually equivalent to:

```text
ReasoningRuntime
    async run(request: ReasoningRequest) -> ReasoningOutcome
```

ADS-owned request must contain at least:

```text
run_id
model_configuration
system_instruction
user_task
project_evidence
methodological_context_payload
methodological_context_sha256
knowledge_revisions
structured_output_kind
```

ADS-owned outcome must contain at least:

```text
run_id
structured_result
requested_model
provider_model
input_tokens
cached_input_tokens when available
output_tokens
reasoning_tokens when available
total_tokens
latency_seconds
provider_service_tier when available
raw usage details needed for audit
```

The OpenAI Agents SDK adapter remains infrastructure.

Forbidden leakage into ADS domain/application contracts:

```text
Agent
RunState
Runner result types
provider Response objects
framework trace types
```

No runtime tool definitions are needed in this experiment.

---

## 10. Runtime input construction

Every reasoner request contains exactly one condition-neutral input envelope with:

```text
experiment run nonce
user task
project evidence
methodological context payload
```

The unique nonce must occur before the methodological payload so treatment content is not systematically reused from a prior condition through prefix caching.

The runtime must not append:

```text
prior project transcript
prior experiment output
previous_response_id
hidden full Horizon in SELECTIVE
retrieval result lists
judge rubric
condition label
```

The system prompt and structured output schema must be identical across the two conditions.

---

## 11. Replication and deterministic randomization

Frozen design:

```text
4 cases
2 conditions
3 reasoner repetitions per condition
24 planned reasoner outputs
24 planned judge outputs
48 planned successful provider calls
```

Randomization seed:

```text
20260822
```

The harness must generate a deterministic call plan from that seed before any live call.

Requirements:

```text
condition order randomized within each case/repetition pair
all call-plan entries assigned condition-neutral opaque run IDs
judge order independently deterministically shuffled
call plan serialized and hashed before live execution
```

No result-dependent reordering is permitted.

---

## 12. Failure and retry policy

A planned call may be retried once only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

The retry must preserve:

```text
case
condition
repetition
prompt/configuration
context digest
model configuration
```

The failed attempt remains in the raw result ledger.

Maximum attempts across reasoner and judge phases:

```text
60
```

A second failure for the same planned call remains a failed observation. Do not repeatedly sample until success.

Semantic quality is never a retry reason.

---

## 13. Frozen quality gates

Let:

```text
Q_S = mean normalized judge score across successful SELECTIVE outputs
Q_F = mean normalized judge score across successful FULL_HORIZON outputs
```

### RQ-01 Aggregate preservation

Require:

```text
Q_S >= Q_F - 0.05
```

### RQ-02 Per-case preservation

For every case:

```text
mean_case(Q_S) >= mean_case(Q_F) - 0.10
```

### RQ-03 Critical-obligation regression

For every frozen critical obligation:

```text
if FULL_HORIZON scores >= 1
in at least 2 of its 3 repetitions,
then SELECTIVE must also score >= 1
in at least 2 of its 3 repetitions.
```

This detects a selective-context omission that creates a reproducible critical reasoning loss.

### RQ-04 No unsupported methodological basis

For every reasoner output:

```text
methodological_basis subset of supplied stable keys
```

### RQ-05 Exact context identity

The context digest and exact supplied knowledge revisions must match the pre-call constructed condition and remain current accepted at assembly time.

No claim of formal statistical non-inferiority is permitted from these small frozen repetitions.

---

## 14. Frozen efficiency gates

Use provider-reported **total input tokens** as the primary model-specific context-cost measure.

### RE-01 Matched-pair reduction

For every case/repetition pair:

```text
SELECTIVE input_tokens < FULL_HORIZON input_tokens
```

### RE-02 Per-case reduction

For every case:

```text
mean SELECTIVE input_tokens
/
mean FULL_HORIZON input_tokens
<= 0.80
```

### RE-03 Aggregate reduction

Across all reasoner calls:

```text
mean SELECTIVE input_tokens
/
mean FULL_HORIZON input_tokens
<= 0.80
```

The threshold is intentionally looser than methodology-only byte ratios because fixed runtime instructions, project evidence, and output-schema tokens remain in both conditions.

Record but do not gate on:

```text
cached input tokens
output tokens
reasoning tokens
total tokens
latency
monetary cost
```

Any cost calculation must record the pricing source/date used and remain descriptive.

---

## 15. Context-distraction diagnostics

Each frozen case defines:

```text
required_selective_keys
allowed_additional_basis_keys
```

Compute:

```text
unexpected_basis_keys =
    methodological_basis
    - required_selective_keys
    - allowed_additional_basis_keys
```

Record:

```text
count per output
keys per output
condition-level mean
case-level mean
```

This is diagnostic only for the first experiment, not a hard quality gate.

A semantic judge may still score an answer highly if an additional basis is genuinely useful.

---

## 16. Non-quality technical invariants

### RV-INV-01 Frozen selective sets
Before live calls, SELECTIVE sets exactly equal the fixture's required sets.

### RV-INV-02 Full control contains all included Horizon revisions
FULL_HORIZON contains exactly ten current accepted revisions from the built Horizon.

### RV-INV-03 Same task evidence
Matched conditions receive byte-equivalent canonical project evidence and user task text.

### RV-INV-04 Same model configuration
Matched conditions use identical reasoner model/runtime settings.

### RV-INV-05 No tools
Reasoner and judge runtime expose zero callable tools.

### RV-INV-06 No cross-call state
No previous response ID, conversation state, framework session history, or prior reasoning item is reused.

### RV-INV-07 Runtime isolation
ADS application/domain modules import no OpenAI Agents SDK type.

### RV-INV-08 Structured-output validation
Reasoner and judge outputs validate into ADS-owned types before use.

### RV-INV-09 Context transparency
Every reasoner trace records context SHA-256 and exact stable-key/revision pairs.

### RV-INV-10 Provider usage transparency
Every successful reasoner call records provider model identity and token usage fields made available by the provider/runtime.

### RV-INV-11 Judge blinding
Judge payload contains no condition or context identity.

### RV-INV-12 Deterministic plan
Repeated plan generation from unchanged fixture/seed produces identical serialized plan bytes and digest.

### RV-INV-13 Authoritative isolation
Experiment execution performs no authoritative project or reusable-knowledge mutation.

### RV-INV-14 CI isolation
Ordinary CI passes without a live OpenAI API key; live calls require explicit secret-gated execution.

### RV-INV-15 Cross-platform infrastructure
All non-live implementation/unit/integration gates pass on Ubuntu and Windows under the existing V1 Python workflow environment.

---

## 17. Result ledger requirements

Preserve a machine-readable result bundle and human-readable result report.

For every reasoner attempt record at least:

```text
opaque run_id
case_id
condition
repetition
attempt
context_sha256
context_utf8_bytes
context_stable_key/revision pairs
requested model
provider model
reasoning effort
input tokens
cached input tokens if available
output tokens
reasoning tokens if available
total tokens
latency
service tier if available
structured result or failure
unexpected basis keys
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
usage
latency
failure if any
```

Aggregate report must include:

```text
quality gates RQ-01 through RQ-05
efficiency gates RE-01 through RE-03
all technical invariants
per-case condition summaries
raw-failure/retry counts
context/token ratios
unexpected-basis diagnostics
exact workflow/source head
```

Raw outputs must be retained for audit.

---

## 18. Live execution boundary

No live model call may occur before all of the following are committed on the experiment branch:

```text
Research 021
Specification 014 v0.1
context_value_v1.json
Checkpoint 144 freeze record
```

The implementation may then proceed against this frozen contract.

If the implementation reveals a specification defect before live calls, revise the specification explicitly and create a new freeze checkpoint before calling the model.

Do not silently mutate the fixture.

---

## 19. Advancement rule

### If all frozen gates pass

```text
1. preserve complete result before tuning
2. classify selective context as earning continuation at the real reasoning layer
3. promote the production-facing ReasoningRuntime adapter seam used by the test if its technical gates pass
4. retain gpt-5.6-sol/medium as experiment evidence, not a universal model decision
5. advance to a harder real-project recommendation/action slice
```

### If quality fails but efficiency passes

```text
1. preserve the failure
2. identify which critical obligation/regression caused it
3. classify whether the defect is task-profile expressiveness,
   selected knowledge metadata, relation support, budget, or semantic relevance
4. only then consider a richer relevance stage
```

### If both conditions fail similarly

```text
do not blame selective context by default
investigate task/rubric/model/prompt/runtime adequacy first
```

### If FULL_HORIZON performs worse

```text
preserve the distraction evidence
more context must not be treated as automatically safer
```

---

## 20. Explicit non-goals

Do not select or implement merely for this slice:

```text
final LLM provider/model
model-family bakeoff
reasoning-effort bakeoff
pro mode
fast/priority processing
multi-agent collaboration
reasoner tools or MCP
human approval workflow
natural-language task classifier
LLM relevance selector
embedding reranker
final recommendation policy
REQUIRED/BLOCKING policy
final Horizon size
final context budget
production vector database / ANN
permanent RRF implementation
formal statistical significance/non-inferiority framework
```

---

## 21. Primary sources

```text
docs/DECISIONS.md, D-032
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md

docs/research/021_first_reasoning_context_value_vertical_slice_design.md

docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md

tests/fixtures/reasoning/context_value_v1.json
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```
