# V1 Reasoning Context Value Result

**Date:** 2026-08-23  
**Status:** Frozen Specification 014 live result preserved; all preregistered quality and provider-token gates passed  
**Experiment:** `v1-reasoning-context-value-v0.1`  
**Specification:** `docs/specifications/014_v1_reasoning_context_value_vertical_slice.md`  
**Frozen source head:** `3592cc3bd91e0aae7e5c667fa0c762ae4acd5395`  
**Workflow:** `V1 reasoning context value live`  
**Workflow run:** `32635061634`  
**Successful workflow attempt:** 2  
**Raw result bundle:** `experiments/reasoning_context_value/results/spec014-live-20260823-run-32635061634/`

## 1. Result summary

The first real-model test of selective methodological context passed every frozen gate without changing the model, prompt, context conditions, semantic obligations, thresholds, repetition count, randomization seed, or retry policy after preregistration.

The frozen comparison was:

```text
SELECTIVE
    Specification 013 v1.0 context selection
    2-3 exact task-specific accepted-current revisions

versus

FULL_HORIZON
    all 10 exact included Horizon revisions
    same compact reasoning projection
    same project/task evidence
    same system instruction
    same structured output schema
    same model/runtime configuration
```

Observed completion:

```text
reasoner outputs                 24 / 24
blinded judge outputs            24 / 24
scored outputs                   24 / 24
successful provider calls        48 / 48 planned
provider attempts used           48 / 60 maximum
retries                           0
complete scored design           true
overall frozen gate              PASS
```

The first manual workflow attempt stopped before any provider call because `OPENAI_API_KEY` was not yet configured as a repository secret. The unchanged workflow was rerun after the secret was added. Attempt 2 executed the frozen experiment successfully. The failed credential-boundary attempt therefore does not constitute an experimental observation and caused no treatment contamination.

---

## 2. Frozen model/runtime environment

Reasoner:

```text
runtime                 OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents           0.19.4
OpenAI Python client    2.54.0
requested model         gpt-5.6-sol
provider model          gpt-5.6-sol
reasoning effort        medium
verbosity               low
max output tokens       4000
tools                   none
previous-response state none
```

Judge:

```text
model                   gpt-5.6-sol
reasoning effort        high
verbosity               low
max output tokens       4000
condition identity      hidden
one judge call          per reasoner output
```

Execution Python:

```text
Python 3.13.15
```

The concrete model/runtime configuration remains experiment evidence rather than a universal ADS model selection.

---

## 3. Quality result

Frozen quality gates:

```text
aggregate SELECTIVE mean >= FULL_HORIZON mean - 0.05

for every case:
SELECTIVE mean >= FULL_HORIZON mean - 0.10

for every critical obligation:
if FULL_HORIZON satisfies it in at least 2/3 repetitions,
SELECTIVE must also satisfy it in at least 2/3 repetitions
```

Observed:

| Case | SELECTIVE mean | FULL_HORIZON mean | Difference | Per-case gate |
|---|---:|---:|---:|---|
| RV-01 MODEL_OPTION | 1.000000 | 1.000000 | 0.000000 | PASS |
| RV-02 EVIDENCE_OPTION | 1.000000 | 1.000000 | 0.000000 | PASS |
| RV-03 VALIDITY_CONSTRAINT | 1.000000 | 1.000000 | 0.000000 | PASS |
| RV-04 DECISION_FRAMEWORK | 1.000000 | 1.000000 | 0.000000 | PASS |
| **Aggregate** | **1.000000** | **1.000000** | **0.000000** | **PASS** |

Critical-obligation regressions:

```text
none
```

Unsupported methodological-basis failures:

```text
none
```

All 24 outputs therefore satisfied every frozen semantic obligation according to the independently ordered, condition-blinded judge.

This is strong bounded evidence of quality preservation on the frozen task set. It is not a formal statistical non-inferiority result, and the ceiling score in both conditions means this experiment cannot estimate a positive quality advantage for SELECTIVE.

---

## 4. Provider input-token result

Frozen efficiency gates:

```text
SELECTIVE input_tokens < FULL_HORIZON input_tokens
for every matched case/repetition pair

per-case mean SELECTIVE/FULL_HORIZON input-token ratio <= 0.80

aggregate mean SELECTIVE/FULL_HORIZON input-token ratio <= 0.80
```

Observed:

| Case | Mean SELECTIVE input tokens | Mean FULL input tokens | S/F ratio | Input-token reduction | Gate |
|---|---:|---:|---:|---:|---|
| RV-01 | 911.33 | 3039.00 | 0.299879 | 70.01% | PASS |
| RV-02 | 786.67 | 3015.00 | 0.260918 | 73.91% | PASS |
| RV-03 | 1258.00 | 3027.33 | 0.415547 | 58.45% | PASS |
| RV-04 | 1096.00 | 3036.67 | 0.360922 | 63.91% | PASS |
| **Aggregate** | **1013.00** | **3029.50** | **0.334379** | **66.56%** | **PASS** |

Matched-pair token failures:

```text
none
```

Every one of the 12 matched SELECTIVE calls used fewer provider-reported input tokens than its FULL_HORIZON counterpart.

This result is materially stronger than the preceding methodology-only byte proxy because it measures the actual provider-reported model input after fixed instructions, project evidence, structured-output machinery, and the methodological context are combined.

---

## 5. Descriptive non-gated runtime observations

The following were preregistered as descriptive rather than hard gates:

| Metric | SELECTIVE mean | FULL_HORIZON mean |
|---|---:|---:|
| Input tokens | 1013.00 | 3029.50 |
| Output tokens | 230.75 | 441.75 |
| Reasoning tokens | 36.42 | 216.08 |
| Total tokens | 1243.75 | 3471.25 |
| Latency, seconds | 5.11 | 8.86 |
| Unexpected methodological-basis keys | 0.00 | 1.67 |

No cached input tokens were observed in the successful reasoner calls.

These observations are not promotion gates and should not be generalized as stable provider-performance ratios from this small experiment. They do, however, motivate preserving context economy as an explicit downstream measurement in later reasoning experiments.

---

## 6. Context-distraction diagnostic

The frozen diagnostic defined:

```text
unexpected_basis_keys =
    methodological_basis
    - required_selective_keys
    - allowed_additional_basis_keys
```

Observed condition-level means:

```text
SELECTIVE     0.000000 unexpected basis keys per output
FULL_HORIZON 1.666667 unexpected basis keys per output
```

Every SELECTIVE output stayed within its required/explicitly allowed methodological basis.

FULL_HORIZON produced additional methodological excursions in two task classes:

```text
RV-01 MODEL_OPTION
    mean unexpected basis count = 4.333333

RV-04 DECISION_FRAMEWORK
    mean unexpected basis count = 2.333333
```

Examples of extra FULL_HORIZON basis keys included concerns such as:

```text
prediction-moment
prediction-time-feature-eligibility
temporal-validation
missing-data
class-imbalance
```

when they were not part of the frozen required/allowed basis for the immediate task.

The blinded judge still gave both conditions perfect frozen obligation scores. The correct interpretation is therefore:

> On this bounded benchmark, fuller context caused measurable methodological expansion without causing measured rubric-quality loss.

It would be an overclaim to state that FULL_HORIZON generally distracts models or that the additional considerations were always harmful. This diagnostic earns further testing on harder tasks where irrelevant methodological expansion can create real decision costs or obligation failures.

---

## 7. Determinism, provenance, and technical invariants

Frozen identities:

```text
reasoning plan SHA-256
    ef2d604453232487b4259b15f947063ef165f059be3d28bac9d5e93c0583858a

judge plan SHA-256
    939c464190348d860b4459dfadfd732fce1ee7f7802525d582e3a1aeb0da20bd

accepted snapshot digest
    d896eecd45745ca951ea01c81f81d313a8cb49dbd54fa6f9b713f4f9c1904933
```

Runner-reported invariants `RV-INV-01` through `RV-INV-14` all passed. `RV-INV-15` is intentionally external CI evidence rather than something the live runner can prove about itself.

The exact frozen source head had already passed the provider-free reasoning-context workflow on both Ubuntu and Windows before the live run:

```text
source head
    3592cc3bd91e0aae7e5c667fa0c762ae4acd5395

V1 reasoning context value
    run 32568506881
    Ubuntu PASS
    Windows PASS
```

The inherited checkpoint, selective-context, first-Horizon-builder, and MethodologicalHorizon workflows were also green on that source head.

---

## 8. Durable raw-result preservation

The complete successful workflow artifact was downloaded and verified before repository preservation.

Artifact provenance:

```text
workflow run             32635061634
successful run attempt   2
artifact id              9492191878
artifact name            v1-reasoning-context-value-3592cc3bd91e0aae7e5c667fa0c762ae4acd5395-2
artifact ZIP SHA-256     e2fa6b70915b96b2978c4b2c78c5d16207b09cf7bd1e0bb79a2ea027bba5a30a
```

Durable repository copy:

```text
experiments/reasoning_context_value/results/spec014-live-20260823-run-32635061634/
```

That directory contains:

```text
MANIFEST.md
RESULT.generated.md
reasoner_attempts.jsonl
judge_attempts.jsonl
reasoning_plan.json
judge_plan.json
result.json
reasoning_context_value.sqlite3
```

The manifest records the SHA-256 of every extracted artifact file. The JSONL ledgers retain every reasoner and judge attempt, including exact structured outputs, context identities, model/runtime identity, usage, latency, and judge rationales. No raw failure or retry observations are absent because the successful live execution required no retries.

---

## 9. Bounded interpretation

Specification 014 answers its frozen question positively on this benchmark:

```text
selective methodological context
    preserved all measured semantic obligations
    while reducing provider input-token burden by about two thirds
    and eliminating unexpected methodological-basis expansion
    in the SELECTIVE condition
```

The accepted interpretation is deliberately narrower than a global architecture claim.

This experiment supports continuation of:

```text
system-retained broad methodological state
    !=
model-facing context on every reasoning call

explained MethodologicalHorizon
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
```

It also provides the first downstream evidence that the post-V0 selective-context direction is not merely mechanically smaller: under one concrete real-model configuration it retained all frozen reasoning obligations while materially lowering actual model input.

---

## 10. What this result does not establish

Do not infer from this result that:

```text
gpt-5.6-sol is the final ADS model
medium reasoning effort is universally optimal
max_assets = 3 is a final context budget
reasoning_functions solve general semantic relevance
FULL_HORIZON context always harms reasoning
SELECTIVE universally improves answer quality
an LLM relevance judge is unnecessary in all future systems
retrieval/reranking/fusion are solved at production scale
multi-agent reasoning is unnecessary in all future stages
recommendation / REQUIRED-BLOCKING policy is solved
formal statistical non-inferiority has been demonstrated
```

The four frozen cases were deliberately bounded and both conditions reached the judge ceiling. Harder project-level tasks are required before stronger claims are justified.

---

## 11. Advancement decision

All frozen gates passed. Under Specification 014's preregistered advancement rule, the result therefore earns:

```text
1. preservation before tuning                                  DONE
2. continuation of selective context at the real reasoning layer PASS
3. promotion of the tested ADS-owned ReasoningRuntime seam     WARRANTED
4. retention of gpt-5.6-sol/medium as experiment evidence      REQUIRED
5. advancement to a harder real-project recommendation/action slice WARRANTED
```

The next experiment should not return to retrieval or relevance tuning merely because more tuning is possible.

The next justified question is whether the accepted methodological-navigation and selective-context machinery can drive a harder project-level reasoning/recommendation/action decision where:

```text
correct recommendation strength matters
important omissions can cause visible downstream failure
unnecessary methodological expansion has a measurable cost
human/system action consequences can be inspected
```

That next slice must be designed and preregistered from the promoted PR #12 boundary before its live model calls begin.
