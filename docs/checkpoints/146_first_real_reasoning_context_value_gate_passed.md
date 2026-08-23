# Checkpoint 146: First Real Reasoning Context Value Gate Passed

**Date:** 2026-08-23  
**Status:** Historical live-experiment result checkpoint; all frozen Specification 014 quality and provider-token gates passed and promotion authorized  
**Checkpoint class:** EXPERIMENT RESULT  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the first real-model downstream test of the accepted selective `MethodologicalContextPack` against a compact full-Horizon control and records the resulting bounded promotion decision.  
**Authority:** Historical result provenance and promotion record. The accepted bounded interpretation is promoted through Specification 014 v1.0 and current canonical routing; the complete raw result remains in the experiment result bundle.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-reasoning-context-value`  
**Associated PR:** #12 into `v1-frontend-spike`

## 1. Frozen source and execution provenance

The live treatment was executed from the exact preregistered and provider-free validated source head:

```text
3592cc3bd91e0aae7e5c667fa0c762ae4acd5395
```

Live workflow:

```text
V1 reasoning context value live
run 32635061634
successful workflow attempt 2
```

The first manual workflow attempt stopped before any provider call because the repository secret `OPENAI_API_KEY` had not yet been configured. The unchanged workflow was rerun after the secret was added. Attempt 2 passed the credential boundary and executed the frozen treatment. No model, prompt, context condition, rubric, threshold, repetition count, randomization seed, or retry policy changed between preregistration and the successful live execution.

Frozen design:

```text
4 cases
2 conditions
3 repetitions
24 reasoner outputs
24 blinded judge outputs
48 planned successful provider calls
maximum provider attempts 60
```

Observed:

```text
reasoner outputs              24 / 24
judge outputs                 24 / 24
scored outputs                24 / 24
successful provider calls     48 / 48
provider attempts used        48 / 60
retries                       0
complete scored design        true
overall frozen gate           PASS
```

---

## 2. Frozen comparison

```text
SELECTIVE
    Specification 013 v1.0 selection
    2-3 exact task-specific accepted-current revisions

FULL_HORIZON
    all 10 exact included Horizon revisions
    same compact reasoning projection
    same task/project evidence
    same system instruction
    same structured output schema
    same runtime/model configuration
```

Reasoner:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents 0.19.4
OpenAI Python client 2.54.0
gpt-5.6-sol
reasoning effort medium
verbosity low
max output tokens 4000
no tools
no previous-response state
```

Blinded judge:

```text
gpt-5.6-sol
reasoning effort high
verbosity low
max output tokens 4000
condition hidden
one judge call per reasoner output
```

The concrete model/runtime configuration is experiment evidence, not a final ADS provider/model selection.

---

## 3. Quality gates passed

Frozen requirements:

```text
aggregate SELECTIVE mean >= FULL_HORIZON mean - 0.05
per-case SELECTIVE mean >= FULL_HORIZON mean - 0.10
no reproducible selective-only critical-obligation regression
no unsupported methodological-basis references
exact context identity preserved
```

Observed:

```text
                     SELECTIVE     FULL_HORIZON     difference
RV-01 MODEL_OPTION      1.000000       1.000000       0.000000
RV-02 EVIDENCE_OPTION   1.000000       1.000000       0.000000
RV-03 VALIDITY          1.000000       1.000000       0.000000
RV-04 DECISION          1.000000       1.000000       0.000000
aggregate               1.000000       1.000000       0.000000
```

Critical-obligation regressions:

```text
none
```

Unsupported methodological-basis failures:

```text
none
```

Both conditions reached the frozen judge ceiling. The result therefore demonstrates bounded quality preservation, not a positive SELECTIVE quality advantage and not formal statistical non-inferiority.

---

## 4. Provider-token gates passed

Frozen requirements:

```text
SELECTIVE input_tokens < FULL_HORIZON input_tokens
for every matched case/repetition pair

per-case mean SELECTIVE/FULL_HORIZON ratio <= 0.80
aggregate mean SELECTIVE/FULL_HORIZON ratio <= 0.80
```

Observed:

```text
case    SELECTIVE mean   FULL mean    ratio       reduction
RV-01       911.33       3039.00      0.299879      70.01%
RV-02       786.67       3015.00      0.260918      73.91%
RV-03      1258.00       3027.33      0.415547      58.45%
RV-04      1096.00       3036.67      0.360922      63.91%
aggregate  1013.00       3029.50      0.334379      66.56%
```

Matched-pair token failures:

```text
none
```

Every one of the twelve matched SELECTIVE reasoner calls used fewer provider-reported input tokens than the corresponding FULL_HORIZON call.

---

## 5. Descriptive downstream observations

These were not hard gates:

```text
metric                         SELECTIVE mean   FULL_HORIZON mean
input tokens                     1013.00            3029.50
output tokens                     230.75             441.75
reasoning tokens                   36.42             216.08
total tokens                     1243.75            3471.25
latency seconds                     5.11               8.86
unexpected basis keys               0.00               1.67
```

No cached input tokens were observed in successful reasoner calls.

The context-distraction diagnostic found zero unexpected methodological-basis keys in every SELECTIVE output. FULL_HORIZON produced additional methodological basis in RV-01 and RV-04, with condition-level mean 1.666667 unexpected keys per output. Because both conditions still scored 1.0 on every frozen obligation, the supported conclusion is narrow:

> On this bounded benchmark, fuller context caused measurable methodological expansion without measured frozen-rubric quality loss.

Do not generalize this into a claim that fuller context always distracts or harms a model.

---

## 6. Determinism and technical evidence

Frozen plan identities:

```text
reasoning plan SHA-256
    ef2d604453232487b4259b15f947063ef165f059be3d28bac9d5e93c0583858a

judge plan SHA-256
    939c464190348d860b4459dfadfd732fce1ee7f7802525d582e3a1aeb0da20bd

accepted snapshot digest
    d896eecd45745ca951ea01c81f81d313a8cb49dbd54fa6f9b713f4f9c1904933
```

Runner invariants `RV-INV-01` through `RV-INV-14` passed. `RV-INV-15` is external cross-platform CI evidence by design.

The exact frozen source head had already passed:

```text
V1 reasoning context value
run 32568506881
Ubuntu PASS
Windows PASS
```

and the relevant checkpoint, selective-context, first-Horizon-builder, and MethodologicalHorizon workflows were green at the same source head.

---

## 7. Complete raw result preserved

Stable human-readable result:

```text
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
```

Complete durable raw bundle:

```text
experiments/reasoning_context_value/results/spec014-live-20260823-run-32635061634/
```

Artifact provenance:

```text
workflow run             32635061634
successful run attempt   2
artifact id              9492191878
artifact name            v1-reasoning-context-value-3592cc3bd91e0aae7e5c667fa0c762ae4acd5395-2
artifact ZIP SHA-256     e2fa6b70915b96b2978c4b2c78c5d16207b09cf7bd1e0bb79a2ea027bba5a30a
```

The raw bundle contains the full reasoner/judge attempt ledgers, deterministic plans, aggregate `result.json`, generated report, and isolated experiment SQLite database. `MANIFEST.md` records SHA-256 values for every extracted artifact file.

---

## 8. Bounded interpretation

Specification 014 answers its frozen question positively on the tested benchmark:

```text
selective exact-revision methodological context
    preserved all measured semantic obligations
    while reducing actual provider-reported input tokens by about two thirds
```

This is the first downstream real-model evidence supporting the post-V0 distinction:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The result supports continued use of the architecture:

```text
explained MethodologicalHorizon
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
```

It does not prove general semantic relevance, a universal context budget, or universal model/provider superiority.

---

## 9. Promotion audit

### Promote Specification 014 to bounded accepted v1.0

**Decision:** promote.

Accepted seam:

```text
same task/project evidence
    + accepted selective MethodologicalContextPack
    + exact context/revision trace
    + ADS-owned ReasoningRuntime
    + provider-neutral usage/trace normalization
```

The frozen first real-model comparison passed every preregistered quality and provider-token gate. Specification 014 may therefore move from frozen v0.1 evaluation contract to accepted bounded v1.0 result-backed seam.

### Promote the production-facing ReasoningRuntime seam

**Decision:** promote the seam used by this test as the initial V1 production-facing reasoning boundary.

This includes the ADS-owned request/outcome/result/usage/trace contracts and the no-tool OpenAI Agents SDK infrastructure adapter behind the existing D-032 decision.

This does **not** select `gpt-5.6-sol` as the final model or OpenAI as an irreversible provider dependency. Provider/framework types remain outside ADS application/domain contracts.

### Promote current routing and structural history

**Decision:** update `README.md`, `CURRENT_STATE.md`, `KNOWLEDGE_MAP.md`, `OPEN_QUESTIONS.md`, `VISION.md` where current-boundary wording is stale, and `MAJOR_CHANGES.md`.

### No promotion to final relevance/recommendation policy

Do not promote:

```text
max_assets = 3 as a universal budget
reasoning_functions as a complete semantic relevance solution
FULL_HORIZON as universally harmful
an LLM relevance judge
embedding reranker
final production semantic retrieval stack
recommendation / REQUIRED-BLOCKING policy
multi-agent architecture
formal statistical non-inferiority
```

---

## 10. Exact continuation

```text
1. promote Specification 014 to bounded accepted v1.0
2. reconcile canonical/routing documents with the live result
3. update PR #12 with the measured result and bounded interpretation
4. validate the exact reconciled PR head through provider-free cross-platform and inherited gates
5. merge exactly that green PR #12 head into v1-frontend-spike
6. branch from the promoted merge boundary
7. design and preregister the next harder real-project recommendation/action slice before any new live model calls
```

The next justified experiment should exercise recommendation strength, required/blocking concerns, project-level consequences, and measurable costs of omission or unnecessary methodological expansion. It should not return to retrieval or relevance tuning merely because more tuning is possible.
