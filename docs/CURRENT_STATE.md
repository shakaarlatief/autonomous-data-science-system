# Current State

**Checkpoint:** 144  
**Date:** 2026-08-22  
**Active development branch:** `v1-reasoning-context-value`  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #11 merge commit `fd33184fbff588c6737d77af751bc5def0e31954`  
**Development stage:** Prototype V0 complete; bounded V1 implementation now connects governed methodological knowledge, retrieval/Horizon construction, selective context, and the selected reasoning-runtime boundary  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** implement and validate the frozen Specification 014 reasoning-context-value vertical slice without live model calls first; only after the exact implementation head is green should the preregistered live SELECTIVE versus FULL_HORIZON experiment run.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` intentionally trails current V1 work.

---

## 1. Durable architectural constraint

Prototype V0 strongly falsified the tested P0 pattern of repeatedly carrying large structured state and frontier machinery through reasoning calls.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The post-V0 architecture therefore keeps persistent project/methodological state separate from bounded task-specific model context.

---

## 2. Governing methodological architecture

Foundation 018 separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Foundation 019 governs methodological navigation through:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Foundation 020 governs reusable knowledge around:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
conditional KnowledgeRule
KnowledgeCollection
exact revisions
ExecutionCapability
```

The current scaling path is:

```text
large global methodological knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> task-specific relevance selection
    -> selective MethodologicalContextPack
    -> real reasoning
```

---

## 3. Accepted V1 implementation boundaries

Accepted decisions include:

```text
D-028
    SQLite-centered local-first operational architecture

D-029
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030
    pyproject.toml + uv + committed uv.lock + uv_build

D-031
    JSON + JSON Schema Draft 2020-12
    + semantic validation
    + deterministic knowledge interchange

D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

Checkpoint 127 closes the governed reusable-knowledge persistence/interchange seam across SQLite/Linux, SQLite/Windows, and PostgreSQL 18.

Checkpoint 133 closes the initial runtime bakeoff. Direct model calls remain the fallback/reference path. LangGraph remains a future stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

Specification 008 remains the promoted Project Cockpit interaction contract.

---

## 4. Retrieval/Horizon sequence already validated

The first bounded retrieval/Horizon progression is complete:

```text
Checkpoint 135
    production lexical retrieval PASS

Checkpoint 137
    dense-only semantic comparator preserved
    complementary rather than dominant

Checkpoint 139
    bounded lexical+dense RRF comparator PASS

Checkpoint 141 / Specification 012 v1.0
    accepted-current one-hop relation expansion
    TRUE / FALSE / UNKNOWN applicability
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    explained MethodologicalHorizon PASS
```

Key semantic invariant:

```text
unknown != false
```

PR #10 containing the later retrieval/Horizon slice was merged into `v1-frontend-spike` at:

```text
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

Do not keep tuning retrieval because it can be tuned. FastEmbed, BGE, RRF `k=60`, vector persistence, ANN, a vector database, and reranking remain unselected production details.

---

## 5. Selective methodological context is accepted for the first bounded seam

Research 020 / Specification 013 tested:

```text
explicit requested reasoning functions
    -> PRIMARY_FUNCTION_MATCH
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets
    -> exact accepted-current compact context reads
    -> ContextSelectionResult
    -> MethodologicalContextPack
```

The frozen RH-C gate passed on Ubuntu and Windows without changing targets or thresholds.

Observed on the deliberately wide ten-asset Horizon:

```text
RH-C01  2 selected  ratio 0.20020477  reduction 79.98%
RH-C02  2 selected  ratio 0.16462054  reduction 83.54%
RH-C03  3 selected  ratio 0.34635417  reduction 65.36%
RH-C04  2 selected  ratio 0.28222057  reduction 71.78%
```

Across all cases:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected assets         0
unexplained omissions              0
```

Additional validated behavior includes stale-revision fail-closed reads, explicit `BUDGET_LIMIT`, post-budget full-content materialization, deterministic serialization, cross-platform identical digests, preserved `MISSING_CONTEXT`, and omission of retrieval metadata from the model-facing pack.

Checkpoint 143 promoted Specification 013 to accepted bounded v1.0.

PR #11 was validated at exact head:

```text
517a12d14b6bb639258931f5c3c451d35ccd7ec0
```

with all relevant workflows green, then merged exactly into `v1-frontend-spike` at:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

---

## 6. The first real reasoning vertical slice is now preregistered

Research 021, Specification 014 v0.1, the frozen reasoning fixture, and Checkpoint 144 define the next experiment before implementation or live model calls.

Frozen conditions:

```text
SELECTIVE
    accepted Specification 013 pack
    2-3 task-specific exact revisions

FULL_HORIZON
    all ten included Horizon revisions
    same compact reasoning projection
    same task envelope
```

Both conditions receive identical:

```text
project evidence
user task
requested reasoning functions
system instructions
structured output schema
runtime adapter
reasoner model configuration
```

Frozen task classes:

```text
RV-01 MODEL_OPTION
RV-02 EVIDENCE_OPTION
RV-03 VALIDITY_CONSTRAINT
RV-04 DECISION_FRAMEWORK
```

Frozen reasoner configuration:

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

Frozen blinded judge configuration:

```text
gpt-5.6-sol
reasoning effort = high
text verbosity = low
max output tokens = 4000
one judge call per reasoner output
```

The explicit model is an experiment constant, not a final provider/model decision.

---

## 7. Frozen reasoning-quality and token gates

Each case has preregistered semantic obligations scored `0/1/2` by a condition-blinded judge.

Quality gates:

```text
aggregate selective mean >= full-Horizon mean - 0.05

for every case:
selective mean >= full-Horizon mean - 0.10
```

Critical-obligation regression rule:

```text
if FULL_HORIZON satisfies a critical obligation
in at least 2/3 repetitions,
SELECTIVE must also satisfy it in at least 2/3 repetitions
```

Provider-token gates:

```text
SELECTIVE input_tokens < FULL_HORIZON input_tokens
for every matched pair

per-case mean selective/full input-token ratio <= 0.80
aggregate mean selective/full input-token ratio <= 0.80
```

This is a bounded falsification gate, not a formal statistical non-inferiority study.

---

## 8. Frozen call and runtime architecture

Planned live result:

```text
4 cases
2 conditions
3 reasoner repetitions
24 reasoner outputs
24 blinded judge outputs
48 planned successful provider calls
```

Randomization seed:

```text
20260822
```

Maximum provider attempts, including one permitted transport/provider/invalid-response retry per planned call:

```text
60
```

Semantic quality is never a retry reason.

The implementation must create the first production-facing runtime seam under `src/ads_system`:

```text
ADS application
    -> ReasoningRuntime port
    -> infrastructure OpenAI Agents SDK adapter
```

The first experiment intentionally uses no tools, MCP, approvals, previous-response state, or multi-agent behavior so methodological context remains the treatment difference.

Ordinary CI must remain live-API-free. Live calls must run only through an explicit secret-gated workflow after the implementation head is green.

---

## 9. Current major non-selections

Still deliberately unselected:

```text
final LLM provider/model
final reasoning effort / pro mode
multi-agent collaboration architecture
production durable runtime-state persistence schema
production MCP server/tool catalog
natural-language task -> reasoning-function mapper
final semantic relevance mechanism
recommendation / REQUIRED-BLOCKING policy
final MethodologicalHorizon budget
final selective context budget
production embedding provider
vector database / ANN infrastructure
permanent fusion implementation / reranker
frontend final stack promotion
chart library
Cockpit canvas/gesture/auto-layout/minimap/semantic-zoom implementation
complete Foundation 018 production schema
artifact storage
job queue / cloud deployment
```

---

## 10. Exact next execution order

### A. IMPLEMENT WITHOUT LIVE MODEL CALLS

```text
1. add ADS-owned reasoning request/outcome/result models
2. add ReasoningRuntime port
3. add no-tool OpenAI Agents SDK infrastructure adapter
4. add deterministic SELECTIVE/FULL_HORIZON condition construction
5. add deterministic call-plan generation from seed 20260822
6. add blinded judge contract and result validation
7. add fake-model unit/integration tests
8. add secret-gated live workflow
```

### B. VALIDATE THE EXACT IMPLEMENTATION HEAD

```text
1. Ubuntu CI green
2. Windows CI green
3. existing V1 regression suite green
4. frozen selective sets reproduced exactly
5. full control contains all ten Horizon revisions
6. no live provider calls required by ordinary CI
```

### C. ONLY THEN EXECUTE THE LIVE PREREGISTERED PLAN

```text
24 reasoner calls
24 blinded judge calls
no result-driven threshold/configuration changes
preserve all failed attempts/retries
preserve raw outputs and complete aggregate result before tuning
```

If the reasoning result exposes a selective-context failure, classify whether the defect is task-profile expressiveness, knowledge metadata, support closure, budget, or semantic relevance before adding new machinery.

---

## 11. Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/OPEN_QUESTIONS.md
docs/DECISIONS.md
docs/PRINCIPLES.md

docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md

docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/research/021_first_reasoning_context_value_vertical_slice_design.md

experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md

tests/fixtures/reasoning/context_value_v1.json

docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
```
