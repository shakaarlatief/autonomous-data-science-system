# Research 021: First Reasoning Context Value Vertical Slice Design

**Date:** 2026-08-22  
**Status:** Current bounded design research for the first real reasoning experiment after selective-context promotion  
**Scope:** Defines the smallest meaningful experiment that connects the accepted selective `MethodologicalContextPack` seam to the selected ADS-owned `ReasoningRuntime` boundary and tests downstream reasoning quality and model-specific context cost.  
**Authority:** Research rationale only. Specification 014 freezes the executable experiment contract before implementation or live model calls.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting evidence boundary

PR #11 promoted the first selective methodological-context seam into `v1-frontend-spike` at merge commit:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

The new experiment branch begins exactly from that promoted boundary:

```text
v1-reasoning-context-value
```

The accepted upstream path now has executable evidence for:

```text
accepted-current methodological knowledge
    -> lexical retrieval
    -> measured lexical/dense complementarity
    -> bounded hybrid comparator
    -> explained MethodologicalHorizon
    -> TRUE / FALSE / UNKNOWN applicability
    -> task-profile relevance selection
    -> bounded REQUIRES_CONCEPT support
    -> exact MethodologicalContextPack
```

Specification 013 v1.0 demonstrated, on the frozen ten-asset stress corpus:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected assets         0
selected assets                    <= 3
unexplained omissions              0
canonical-context reduction        approximately 65% to 84%
```

That result is mechanical. It does not establish that the smaller pack preserves or improves actual LLM reasoning.

The next question is therefore downstream:

> When the same project/task evidence is reasoned over by the same concrete model/runtime configuration, does the accepted selective `MethodologicalContextPack` preserve methodological reasoning quality relative to a strong full-Horizon control while materially reducing actual provider input-token burden?

---

## 2. Why this experiment comes before more retrieval or relevance tuning

The project could continue tuning:

```text
embedding models
fusion constants
reranking
semantic relevance judges
larger relation expansion
context budgets
```

but none of those mechanisms is currently justified by a demonstrated downstream reasoning failure.

The first RH-C gate already showed that the simple policy can preserve the frozen exact target revisions. The missing evidence is whether the omitted knowledge is actually harmless at reasoning time and whether fuller context causes measurable cost or distraction.

The correct empirical sequence is therefore:

```text
mechanical context compression
    -> real reasoning value test
    -> classify failures if any
    -> only then escalate retrieval/relevance complexity
```

This follows P-004 and P-019: empirically test a mechanism before adding machinery intended to repair a failure that has not been observed.

---

## 3. Isolate context construction, not runtime tooling

Specification 005 already tested runtime capabilities including tools, MCP, approval interruption, resume, structured output, cancellation/timeout behavior, and framework isolation.

Those features should not be activated in the first context-value experiment because they create additional causal paths:

```text
model context
    -> tool choice
    -> tool output
    -> later reasoning
```

The first reasoning vertical slice should therefore use:

```text
one principal reasoner
single-turn reasoning
no tools
no MCP
no approval action
no multi-agent delegation
ADS-owned structured output
ADS-owned RuntimeTrace
```

This still exercises the selected runtime boundary while keeping the treatment difference concentrated in methodological context.

A later experiment can combine selected context with execution tools after the reasoning-only effect is understood.

---

## 4. Experimental conditions

Every matched reasoning task receives the same:

```text
project evidence
user task
requested reasoning functions
model configuration
runtime adapter
system instructions
structured output schema
```

Only the methodological context condition changes.

### Condition S: SELECTIVE

Use the accepted Specification 013 selector exactly:

```text
MethodologicalHorizon
    + MethodologicalContextRequest
    -> select_methodological_context(...)
    -> MethodologicalContextPack
```

Expected selected set remains the frozen RH-C target set for each task.

### Condition F: FULL_HORIZON

Use all ten included candidates from the same explained wide Horizon and materialize them through the **same compact reasoning projection** used by Specification 013.

The control retains:

```text
same schema_version
same task_id
same requested_reasoning_functions
same exact accepted-current revisions
same compact asset/component/rule/narrative projection
same applicability and missing-context metadata
```

Each full-Horizon item receives the neutral experimental reason:

```text
CONTROL_INCLUDED
```

This is the same full-Horizon control shape already used by the RH-C integration gate for canonical size comparison.

The control does not receive the global accepted snapshot export, retrieval terms, aliases, scores, provenance clutter, or system omission decisions. It is therefore a strong compact control rather than a deliberately bloated raw-catalog prompt.

---

## 5. Reuse the four frozen RH-C task classes

Changing both the context mechanism and the task corpus would weaken continuity with the previous result.

The first reasoning experiment should therefore reuse the four heterogeneous RH-C classes:

```text
RV-01  MODEL_OPTION
RV-02  EVIDENCE_OPTION
RV-03  VALIDITY_CONSTRAINT
RV-04  DECISION_FRAMEWORK
```

The tasks are rewritten as natural reasoning requests rather than key-selection tests, but their methodological obligations are derived only from the accepted knowledge fixture used by RH-C.

### RV-01: supervised tree-model comparison

Relevant selective knowledge:

```text
random-forest
gradient-boosted-trees
```

The task asks for a choice-oriented comparison of the supplied tree-ensemble options.

Core obligations supported by the fixture:

```text
identify both model options
explain randomized-tree aggregation for Random Forest
explain sequential boosting for Gradient-Boosted Trees
do not equate technical applicability with automatic model selection
```

`bagging` is allowed as additional supporting basis in the full-Horizon condition because it is a governed concept used by Random Forest, but it is not required for a passing answer.

### RV-02: quantitative-distribution evidence

Relevant selective knowledge:

```text
histogram
ecdf
```

Core obligations:

```text
use both Histogram and ECDF as evidence options
recognize that Histogram depends on binning
recognize that ECDF describes the empirical distribution without bins
avoid treating an extreme value as automatically invalid
```

### RV-03: predictive-validity boundary

Relevant selective knowledge:

```text
prediction-time-feature-eligibility
temporal-validation
prediction-moment
```

The project is future-facing but its prediction moment is unresolved.

Core obligations:

```text
identify prediction moment as unresolved and requiring clarification
require temporal cutoffs/design to represent the intended prediction regime
require features to use only information available by prediction time
recognize source/transformation lineage as part of eligibility
never convert the unknown prediction moment into a false/inapplicable conclusion
```

This is the strongest test of `MISSING_CONTEXT` preservation.

### RV-04: data-quality decision frameworks

Relevant selective knowledge:

```text
class-imbalance
missing-data
```

The project has not yet established class prevalence or whether missingness occurs in production.

Core obligations:

```text
request/identify class prevalence as unresolved
request/identify production missingness as unresolved
recognize that accuracy can conceal minority-class behavior
avoid choosing a missing-data strategy before production missingness is represented
never convert unknown context into a negative fact
```

---

## 6. Freeze task-specific semantic rubrics before model calls

The reasoner should not be judged by exact string matching.

Each frozen case therefore contains a small set of semantic obligations. Each obligation is scored:

```text
0 = absent, materially wrong, or contradicted
1 = partially or implicitly satisfied
2 = explicitly and correctly satisfied
```

Each obligation is marked:

```text
critical = true / false
```

The normalized quality score for one output is:

```text
sum(obligation_scores) / (2 * number_of_obligations)
```

The rubric must be frozen in the fixture before implementation/live runs.

The rubric may only require claims supported by the accepted knowledge fixture and frozen project evidence. General model knowledge may appear in outputs, but it must not be silently promoted into a required scoring obligation after results are observed.

---

## 7. Use a blinded semantic judge, but keep its authority narrow

A semantic judge is justified here because the evaluated object is open-ended methodological reasoning rather than retrieval identity.

The judge receives:

```text
case task
project evidence
frozen rubric obligations
candidate structured reasoning result
```

The judge does **not** receive:

```text
condition label
selective/full context payload
context byte/token counts
runtime latency/cost
matched paired output
```

The judge returns structured scores for the frozen obligations plus a concise rationale.

The judge is not allowed to invent new obligations after reading an answer.

Condition-neutral opaque output IDs are used for judging and preserved with the result.

One judge pass per reasoning output is sufficient for this first bounded slice. Raw reasoning outputs and judge results must be preserved so a later human audit can challenge the judge if needed.

---

## 8. Concrete model choice for the first bounded experiment

D-032 selected the runtime framework boundary but intentionally did not select a final LLM provider/model.

This experiment now needs one concrete model configuration so exact provider token use can be measured.

Current official OpenAI model guidance checked on 2026-08-22 states:

```text
gpt-5.6-sol
    frontier GPT-5.6 model for complex professional work
    1.05M context window
    128K max output
    reasoning efforts: none, low, medium, high, xhigh, max

gpt-5.6
    alias that routes to gpt-5.6-sol

medium
    balanced/default starting reasoning effort
```

Primary external evidence:

```text
https://developers.openai.com/api/docs/models/gpt-5.6-sol
https://developers.openai.com/api/docs/guides/latest-model
```

Use the explicit tier identifier rather than the unsuffixed alias:

```text
gpt-5.6-sol
```

Reasoner configuration:

```text
model                 gpt-5.6-sol
reasoning.effort      medium
text.verbosity        low
max_output_tokens     4000
processing            standard/default, no fast/priority request
state                 single-turn; no previous_response_id
store                 false where exposed
```

Why Sol rather than a smaller model:

The first question is whether ADS context construction harms or preserves reasoning under a strong reasoner. A weaker model would introduce an avoidable model-capability confound. Model-family/cost optimization can be tested later if the context boundary itself survives.

Why medium rather than maximum effort:

Official guidance identifies medium as the balanced/default starting point. The task is bounded methodological synthesis, not a maximum-effort benchmark. If medium proves too weak on both conditions, that should be preserved as evidence before changing the model configuration.

The judge uses the same explicit model tier with:

```text
reasoning.effort      high
text.verbosity        low
max_output_tokens     4000
```

The higher judge effort is intended to reduce scoring error without changing the reasoner treatment.

The experiment must record the provider-returned model identity and relevant SDK/client versions because the public model identifier is a durable tier, not a date-frozen snapshot identifier.

---

## 9. ADS-owned structured reasoning output

The reasoner should return an ADS-owned structure conceptually equivalent to:

```text
ReasoningContextValueResult
    answer: str
    proposed_actions: list[str]
    required_clarifications: list[str]
    warnings: list[str]
    methodological_basis: list[str]
```

`methodological_basis` contains stable keys from the supplied methodological context that materially support the answer.

Deterministic provenance invariant:

```text
set(methodological_basis) <= set(supplied_context_stable_keys)
```

A basis key not present in the supplied exact context is a runtime/provenance failure, not a semantic-judge disagreement.

The model is not required to repeat revision UUIDs. The runtime trace already owns the exact supplied stable-key/revision pairs and context digest.

---

## 10. Replication and call ordering

A single model response is too sensitive to sampling variance for a reasoning-quality conclusion.

Use:

```text
4 cases
2 conditions
3 independent reasoner repetitions
= 24 reasoner outputs
```

Each reasoner output receives one blinded judge call:

```text
24 judge outputs
```

Planned successful model calls:

```text
48
```

The run plan is generated deterministically from seed:

```text
20260822
```

For each case/repetition pair, condition order is randomized. The complete set of reasoner calls is then executed in the frozen generated order.

Judge order is independently deterministically shuffled after reasoner outputs exist.

Every provider request receives a unique condition-neutral run nonce before the methodological payload. This reduces cross-condition prompt-cache reuse for the treatment content. Cached-token counts are still recorded explicitly.

No result-driven rerun is allowed.

Replacement policy:

```text
one retry only for a transport/provider/incomplete-response failure
same case, condition, repetition, model config, and prompt
preserve the failed attempt
```

Maximum provider attempts across reasoner and judge phases:

```text
60
```

A second failure for the same planned call remains a failed/missing observation rather than being repeatedly resampled until a favorable answer appears.

---

## 11. Primary quality gates

This first slice is a bounded falsification gate, not a formal statistical non-inferiority trial.

Let:

```text
Q_S = mean normalized semantic-rubric score for SELECTIVE
Q_F = mean normalized semantic-rubric score for FULL_HORIZON
```

Primary aggregate preservation gate:

```text
Q_S >= Q_F - 0.05
```

Per-case preservation gate:

```text
mean_case(Q_S) >= mean_case(Q_F) - 0.10
for every frozen case
```

Critical-obligation regression gate:

For every frozen critical obligation:

```text
if FULL_HORIZON satisfies the obligation
(score >= 1) in at least 2 of 3 repetitions,
then SELECTIVE must also satisfy it
in at least 2 of 3 repetitions.
```

This explicitly detects a methodological omission that becomes harmful only at reasoning time.

The gate does not require SELECTIVE to outperform FULL_HORIZON.

---

## 12. Primary efficiency gates

The principal efficiency measure is provider-reported **total input tokens**, not UTF-8 bytes.

For every matched case/repetition pair require:

```text
SELECTIVE input_tokens < FULL_HORIZON input_tokens
```

For every case require:

```text
mean(SELECTIVE input_tokens)
    /
mean(FULL_HORIZON input_tokens)
    <= 0.80
```

Also require the aggregate ratio across all planned reasoner calls to be:

```text
<= 0.80
```

The 0.80 threshold is deliberately weaker than the prior 0.16-0.35 methodology-only byte ratios because provider input includes fixed system instructions, structured-output schema, task evidence, and runtime framing that do not shrink with methodological context.

Record separately:

```text
cached input tokens where exposed
reasoning tokens where exposed
output tokens
total tokens
context canonical bytes
context SHA-256
latency
provider service tier
```

No hard latency or monetary-cost gate is frozen in this first experiment. Those quantities are provider/time dependent and are secondary observations.

---

## 13. Context-use and distraction diagnostics

Each case freezes:

```text
required_basis_keys
allowed_additional_basis_keys
```

For a reasoning output compute:

```text
unexpected_basis_keys =
    methodological_basis
    - required_basis_keys
    - allowed_additional_basis_keys
```

This is a diagnostic for fuller-context distraction.

It is not a primary pass/fail criterion in the first experiment because an additional knowledge reference can be semantically useful even when not expected by the small fixture.

The raw answer and semantic judge remain authoritative for quality interpretation.

---

## 14. Runtime and provenance invariants

The vertical slice should establish a real production-facing boundary rather than call the provider directly from an ad hoc script.

Required architecture:

```text
ADS application experiment service
    -> ReasoningRuntime port
    -> OpenAI Agents SDK adapter
    -> concrete provider model
```

The adapter owns framework/provider mechanics. ADS owns:

```text
reasoning request identity
project evidence
condition-neutral run identity
context payload/digest
exact supplied knowledge revision references
structured result schema
normalized usage and latency record
normalized RuntimeTrace
experiment result persistence
```

Required invariants:

```text
framework-specific Agent types do not enter ADS domain models
no global project history/session is silently appended
no tools are available to the reasoner in this experiment
no previous response/reasoning state is reused across planned calls
exact methodological context digest is recorded
exact stable-key/revision pairs are recorded
structured output validates before scoring
methodological_basis is a subset of supplied keys
raw provider/model identity and token usage are retained
```

---

## 15. CI and live-model separation

Ordinary repository CI must not require paid live model calls or an API secret.

Implementation should therefore provide:

```text
unit tests
    fake deterministic ReasoningRuntime / provider model

integration tests
    context condition construction
    prompt/output-schema normalization
    trace/usage normalization
    randomization-plan determinism
    judge-rubric validation

live experiment workflow
    explicit/manual or secret-gated
    OpenAI API key required
    frozen fixture/config required
```

A fake-model gate proves infrastructure determinism. It does not count as the reasoning-quality result.

---

## 16. Failure classes enabled by the vertical slice

The project can now distinguish:

```text
CATALOG_FAILURE
    required knowledge absent

RETRIEVAL_FAILURE
    known knowledge not in Horizon

APPLICABILITY_FAILURE
    candidate incorrectly excluded or unknown treated as false

SELECTION_FAILURE
    relevant Horizon knowledge omitted by relevance/budget policy

CONTEXT_PROVENANCE_FAILURE
    wrong/stale revision or unsupported methodological_basis reference

REASONING_FAILURE_WITH_CONTEXT_PRESENT
    correct context supplied but reasoner misses the obligation

FULL_CONTEXT_DISTRACTION
    fuller context causes extra irrelevant basis or lower reasoning quality

MODEL_CONFIGURATION_FAILURE
    both conditions perform poorly under the frozen model/effort setting

JUDGE_FAILURE
    scoring output invalid/inconsistent with frozen rubric contract
```

This separation is more useful than simply observing one final answer score.

---

## 17. Advancement rule

If the frozen experiment passes the quality and efficiency gates:

```text
1. preserve the complete live result
2. promote the production-facing ReasoningRuntime context boundary used by the slice
3. preserve exact model/provider/configuration as experiment evidence, not universal selection
4. advance to a harder real-project reasoning or recommendation/action slice
5. do not add semantic relevance machinery without a demonstrated need
```

If the experiment fails:

```text
1. preserve the failed result before tuning
2. classify the failure using the stages above
3. if selective context caused a real omission, diagnose task-profile metadata,
   relation support, budget, or semantic relevance before adding a generic LLM judge
4. if both conditions fail, diagnose the task/model/prompt/runtime rather than blaming selection
5. if FULL_HORIZON is worse, preserve the distraction evidence rather than treating more context as safer by default
```

---

## 18. Explicit non-selections

Do not infer or select from this first vertical slice:

```text
final LLM provider/model for ADS
final reasoning effort
pro mode
fast/priority processing
multi-agent architecture
runtime tools/MCP policy
final natural-language task classifier
final semantic relevance judge
final recommendation ranking
REQUIRED/BLOCKING policy
final Horizon/context budget
production FastEmbed/BGE dependency
permanent RRF implementation
ANN/vector database
provider pricing as a durable architectural constant
formal statistical non-inferiority claims
```

The purpose is narrower: determine whether the already-promoted selective context seam earns value when a strong real reasoner actually consumes it.
