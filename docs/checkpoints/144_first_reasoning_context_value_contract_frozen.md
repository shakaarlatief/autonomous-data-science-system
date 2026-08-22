# Checkpoint 144: First Reasoning Context Value Contract Frozen

**Date:** 2026-08-22  
**Status:** Historical experiment-design checkpoint; Specification 014 v0.1 and reasoning-context-value fixture frozen before implementation or live model calls  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the first downstream reasoning experiment connecting selective methodological context to the selected ReasoningRuntime boundary.  
**Authority:** Historical preregistration provenance. Specification 014 v0.1 and `context_value_v1.json` govern the first reasoning-context-value implementation until its result is preserved.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-reasoning-context-value`

## 1. Promoted starting boundary

PR #11 was merged into `v1-frontend-spike` at:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

The current branch starts exactly from that merge commit:

```text
v1-reasoning-context-value
```

The promoted prerequisite chain already provides:

```text
accepted-current reusable methodological knowledge
production lexical retrieval
measured lexical/dense complementarity
bounded hybrid retrieval evidence
accepted-current one-hop relation expansion
three-valued applicability / missing-context behavior
explained MethodologicalHorizon
deterministic task-profile relevance selection
bounded REQUIRES_CONCEPT support
exact selective MethodologicalContextPack
```

Specification 013 v1.0 earned promotion after preserving all frozen exact revisions and reducing methodology-only canonical context by approximately 65% to 84% on the ten-asset stress Horizon.

---

## 2. Frozen next question

The next test is no longer whether context can be compressed mechanically.

It is:

> Under the same project/task evidence and the same concrete model/runtime configuration, does the accepted selective methodological context preserve reasoning quality relative to a strong compact full-Horizon control while materially reducing provider-reported input-token burden?

This is the first experiment that directly tests whether the post-V0 selective-context architecture earns value at the LLM reasoning layer.

---

## 3. Frozen conditions

```text
SELECTIVE
    accepted Specification 013 selection
    2-3 task-specific exact revisions

FULL_HORIZON
    all ten included Horizon revisions
    same compact reasoning projection
    same task envelope
    neutral CONTROL_INCLUDED item reason
```

Both conditions receive identical:

```text
project evidence
user task
requested reasoning functions
system instruction
structured output schema
runtime adapter
reasoner model configuration
```

The full control is intentionally strong. It contains compact accepted-current reasoning content rather than a raw catalog/export and still exposes each asset's own reasoning functions.

---

## 4. Frozen task set

Fixture:

```text
tests/fixtures/reasoning/context_value_v1.json
```

Cases:

```text
RV-01 MODEL_OPTION
    supervised tree-model comparison

RV-02 EVIDENCE_OPTION
    quantitative-distribution evidence

RV-03 VALIDITY_CONSTRAINT
    future-facing validation and prediction-time feature legitimacy

RV-04 DECISION_FRAMEWORK
    class-imbalance and missing-data decision context
```

The required SELECTIVE sets remain exactly those validated by RH-C:

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

Each case also freezes project evidence, user task, required/allowed methodological basis keys, and semantic obligations before model calls.

---

## 5. Frozen model/runtime configuration

Reasoner:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents==0.19.4
gpt-5.6-sol
reasoning effort = medium
text verbosity = low
max output tokens = 4000
no tools
no previous-response state
no fast/priority request
```

Judge:

```text
gpt-5.6-sol
reasoning effort = high
text verbosity = low
max output tokens = 4000
one blinded judge call per reasoner output
no tools
```

The explicit model tier is an experiment constant, not a final project-level provider/model selection.

Current official model evidence was checked before freeze from:

```text
https://developers.openai.com/api/docs/models/gpt-5.6-sol
https://developers.openai.com/api/docs/guides/latest-model
```

The live result must preserve the provider-returned model identity and relevant runtime/client versions because the public tier identifier is not treated as a date-frozen snapshot.

---

## 6. Frozen reasoning-output contract

The reasoner returns an ADS-owned structured result containing:

```text
answer
proposed_actions
required_clarifications
warnings
methodological_basis
```

Hard provenance invariant:

```text
methodological_basis
    subset of
stable keys actually supplied to that reasoner call
```

The model does not need to repeat revision UUIDs because the ADS runtime trace owns exact context digest and stable-key/revision references.

---

## 7. Frozen quality scoring

Each case has preregistered semantic obligations scored by a condition-blinded judge:

```text
0 = absent / materially wrong / contradicted
1 = partial or implicit
2 = explicit and correct
```

Normalized score:

```text
sum(scores) / (2 * number_of obligations)
```

Primary gates:

```text
aggregate SELECTIVE mean >= FULL_HORIZON mean - 0.05

for every case:
SELECTIVE mean >= FULL_HORIZON mean - 0.10
```

Critical-obligation regression gate:

```text
if FULL_HORIZON satisfies a critical obligation
in at least 2 of 3 repetitions,
SELECTIVE must also satisfy it
in at least 2 of 3 repetitions
```

This is a bounded falsification threshold, not a formal statistical non-inferiority claim.

---

## 8. Frozen efficiency gate

Primary model-specific efficiency metric:

```text
provider-reported total input tokens
```

Require every matched pair to satisfy:

```text
SELECTIVE input_tokens < FULL_HORIZON input_tokens
```

Require every case and the aggregate to satisfy:

```text
mean SELECTIVE input_tokens
/
mean FULL_HORIZON input_tokens
<= 0.80
```

Record but do not hard-gate:

```text
cached input tokens
reasoning tokens
output tokens
total tokens
latency
monetary cost
service tier
```

The 0.80 threshold deliberately accounts for fixed prompt/runtime/output-schema overhead that did not appear in the prior methodology-only byte ratios.

---

## 9. Frozen repetition and blinding plan

```text
4 cases
2 conditions
3 repetitions
= 24 reasoner outputs

1 blinded judge call per output
= 24 judge outputs

planned successful provider calls = 48
```

Randomization seed:

```text
20260822
```

The harness must generate and hash the deterministic call plan before live execution.

Condition order is randomized within matched case/repetition pairs. Judge order is independently shuffled.

Judge payload excludes:

```text
condition
context payload/digest
usage
latency/cost
paired alternate output
```

---

## 10. Frozen failure/retry policy

One retry only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic quality is never a retry reason.

Maximum provider attempts:

```text
60
```

Failed attempts are preserved. A second failure for the same planned call remains a failed observation rather than being repeatedly resampled.

---

## 11. Runtime implementation boundary

The experiment must create the first production-facing ADS-owned reasoning runtime seam under `src/ads_system` rather than directly depending on the experiment-local Specification 005 adapter.

Required direction:

```text
ADS application
    -> ReasoningRuntime port
    -> infrastructure OpenAI Agents SDK adapter
```

ADS owns:

```text
request identity
project evidence
context digest
exact supplied knowledge revisions
structured result
normalized usage
normalized trace
experiment result
```

Framework/provider types remain infrastructure-only.

No tools or multi-agent behavior participate in this experiment.

---

## 12. CI/live separation

Ordinary CI must not require a paid API call or secret.

Required split:

```text
unit/integration CI
    deterministic fake runtime/model
    condition construction
    prompt/output validation
    plan randomization
    trace/usage normalization
    judge-rubric contract

live experiment
    explicit secret-gated workflow
    frozen fixture/config
    real provider calls
```

A fake-model pass proves infrastructure only. It does not count as the reasoning-quality result.

---

## 13. Explicit non-selections

Do not introduce or conclude merely from this gate:

```text
final LLM provider/model
model-family bakeoff
reasoning-effort bakeoff
pro mode
fast/priority processing
multi-agent architecture
reasoner tools or MCP
natural-language task classifier
LLM relevance selector
embedding reranker
recommendation / REQUIRED-BLOCKING policy
final Horizon/context budget
production vector database / ANN
permanent RRF implementation
formal statistical non-inferiority claims
```

---

## 14. Exact continuation

```text
1. implement ADS-owned reasoning request/outcome/result types and ReasoningRuntime port
2. implement the OpenAI Agents SDK no-tool adapter behind that port
3. implement deterministic SELECTIVE/FULL_HORIZON condition construction
4. implement frozen plan generation and semantic-judge contract
5. add fake-model unit/integration coverage and cross-platform CI
6. add a secret-gated live workflow
7. validate the exact implementation head before live calls
8. execute the frozen 48-call plan without result-driven tuning
9. preserve complete raw and aggregate result before changing thresholds/configuration
```

Primary sources:

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
tests/fixtures/reasoning/context_value_v1.json
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
```
