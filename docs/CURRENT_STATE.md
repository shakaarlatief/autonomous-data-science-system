# Current State

**Checkpoint:** 145  
**Date:** 2026-08-22  
**Active development branch:** `v1-reasoning-context-value`  
**Active promotion PR:** #12 into `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #11 merge commit `fd33184fbff588c6737d77af751bc5def0e31954`  
**Development stage:** Prototype V0 complete; bounded V1 implementation now connects governed methodological knowledge, the first explained MethodologicalHorizon, accepted selective model-facing context, and an ADS-owned reasoning runtime seam to the first real-model reasoning-value experiment  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** finish pre-live reconciliation for PR #12, validate its exact reconciled head cross-platform, then execute the frozen Specification 014 live workflow without changing model, prompt, rubric, thresholds, repetition count, or context conditions.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails current V1 work until an explicit later promotion.

---

## 1. Durable post-V0 constraint

ADS remains a wider professional data-science system in which the LLM is one reasoning component rather than the whole system.

Prototype V0 strongly falsified the tested pattern of repeatedly carrying large structured project/frontier state through every reasoning call. The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore P0's large always-on state/context, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

---

## 2. Governing methodological architecture

Foundation 018 keeps project representation separated into:

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

Foundation 020 governs reusable methodological knowledge around stable/revision identity, components, narrative facets, relations, conditional rules, context requirements, provenance/governance, collections, and separation from execution capability.

The current scaling path is:

```text
large reusable knowledge universe
    -> high-recall retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> relevance / prioritization
    -> selective task-specific MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> reasoning / recommendation evidence
```

---

## 3. Accepted V1 architecture already promoted

Current accepted boundaries include:

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture
    rebuildable retrieval projections
    application-level rule evaluation
    selective context assembly

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030 + Specification 003
    pyproject.toml + uv + committed uv.lock + uv_build
    Python >=3.12

D-031 + Specification 004
    JSON + JSON Schema Draft 2020-12
    semantic validation
    deterministic reusable-knowledge interchange

D-032 + completed Specification 005
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4

Specification 008
    Project Cockpit as the promoted V1 primary immersive active-work interaction architecture
```

Checkpoint 127 closes the governed reusable-knowledge persistence/interchange seam across SQLite/Linux, SQLite/Windows, and PostgreSQL 18.

Checkpoint 133 closes the first runtime-framework selection question. Direct model calls remain the fallback/reference path. LangGraph remains a possible future stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

---

## 4. Retrieval, Horizon, and selective-context chain is complete for the first bounded slice

The first executable methodological-navigation chain now has evidence through:

```text
Checkpoint 135
    production lexical retrieval
    RH-L Recall@3 = 1.00
    RH-L MRR      = 1.00

Checkpoint 137
    exact dense semantic comparator
    complementary success/failure pattern versus lexical

Checkpoint 139
    equal-weight RRF comparator
    RH-S Recall@3 = 1.00
    RH-S MRR      = 0.875

Specification 012 v1.0 / Checkpoint 141
    one-hop accepted relation expansion
    TRUE / FALSE / UNKNOWN applicability
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    explained MethodologicalHorizon

Specification 013 v1.0 / Checkpoint 143
    explicit task reasoning functions
    -> primary Horizon matches
    -> bounded REQUIRES_CONCEPT support
    -> hard asset budget
    -> exact accepted-current selected-content reads
    -> MethodologicalContextPack
```

The accepted selective-context seam demonstrated approximately 65% to 84% methodology-only canonical-context reduction on the deliberately adversarial ten-asset Horizon while preserving all frozen required stable keys and exact revisions, selecting zero frozen irrelevant assets, retaining missing-context signals, and keeping selection/omission audit state outside the model-facing pack.

This result is mechanical context-construction evidence only. It does not prove downstream reasoning value.

---

## 5. First real reasoning-value experiment is frozen

Research 021, Specification 014 v0.1, `context_value_v1.json`, and Checkpoint 144 freeze the first downstream reasoning experiment before live model calls.

Frozen question:

> With identical project/task evidence and one concrete model/runtime configuration, does the accepted selective `MethodologicalContextPack` preserve reasoning quality relative to a strong compact full-Horizon control while materially reducing provider-reported input-token burden?

Conditions:

```text
SELECTIVE
    accepted Specification 013 selection
    2-3 exact task-specific revisions

FULL_HORIZON
    all 10 exact Horizon revisions
    same compact reasoning projection
    same task envelope
```

Frozen task classes:

```text
RV-01 MODEL_OPTION
RV-02 EVIDENCE_OPTION
RV-03 VALIDITY_CONSTRAINT
RV-04 DECISION_FRAMEWORK
```

Frozen live design:

```text
4 cases
2 conditions
3 repetitions
24 reasoner outputs
24 blinded judge outputs
48 planned successful provider calls
maximum 60 provider attempts
```

Reasoner treatment constant:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents==0.19.4
gpt-5.6-sol
reasoning effort medium
verbosity low
max output tokens 4000
no tools
no previous-response state
```

Judge treatment constant:

```text
gpt-5.6-sol
reasoning effort high
verbosity low
max output tokens 4000
condition hidden
```

The model configuration is experiment evidence, not a final ADS model selection.

---

## 6. Provider-free implementation is complete and green

Checkpoint 145 preserves the completed pre-live implementation boundary.

Production-facing runtime seam:

```text
src/ads_system/application/reasoning.py
src/ads_system/application/ports.py
src/ads_system/infrastructure/runtime/openai_agents.py
```

Experiment infrastructure:

```text
experiments/reasoning_context_value/environment.py
experiments/reasoning_context_value/harness.py
experiments/reasoning_context_value/judge.py
experiments/reasoning_context_value/runner.py
```

Provider-free coverage validates deterministic condition construction, exact context identities, frozen plan generation/digests, judge blinding, rubric recomputation, provider-neutral trace/usage contracts, unsupported-basis rejection, authoritative-state isolation, result-ledger generation, retry/attempt boundaries, and the full fake-runtime end-to-end path.

Exact first implementation gate before Checkpoint 145:

```text
aadf425fdb24db2512e2171f4a99be3c87d8cb80
V1 reasoning context value
run 32568052820
Ubuntu PASS
Windows PASS
```

At that head, inherited selective-context and Horizon workflows also passed.

No live reasoner or judge call has occurred yet.

---

## 7. Frozen quality and efficiency gates

Quality:

```text
aggregate SELECTIVE mean >= FULL_HORIZON mean - 0.05

for every case:
SELECTIVE mean >= FULL_HORIZON mean - 0.10
```

For every critical obligation, if FULL_HORIZON scores at least 1 in at least two of three repetitions, SELECTIVE must do so in at least two of three repetitions.

Efficiency:

```text
for every matched pair:
SELECTIVE input_tokens < FULL_HORIZON input_tokens

per-case mean SELECTIVE/FULL_HORIZON input-token ratio <= 0.80
aggregate mean SELECTIVE/FULL_HORIZON input-token ratio <= 0.80
```

Latency, cached tokens, reasoning tokens, output tokens, total tokens, service tier, and any explicitly sourced monetary-cost calculation are descriptive rather than hard gates.

No formal statistical non-inferiority claim is permitted from this small experiment.

---

## 8. Current major non-selections

Still deliberately unselected:

```text
final LLM provider/model
multi-agent collaboration architecture
production durable runtime-state persistence schema
production MCP server/tool catalog
A2A
AG-UI final role
frontend final stack promotion
chart library
Cockpit graph/canvas/gesture/auto-layout/minimap/semantic-zoom implementation
backend HTTP/API framework
production embedding model/provider
vector database / ANN infrastructure
permanent production fusion implementation
reranker
natural-language task -> reasoning-function mapper
final semantic relevance mechanism
final MethodologicalHorizon budget
final selective context budget
recommendation / REQUIRED-BLOCKING policy
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

Do not add retrieval/relevance complexity before the frozen reasoning experiment exposes a concrete downstream deficiency.

---

## 9. Exact next execution order

### A. PRE-LIVE RECONCILIATION

```text
1. reconcile README / KNOWLEDGE_MAP / OPEN_QUESTIONS with Checkpoint 145 and PR #12
2. update PR #12 with provider-free implementation and cross-platform evidence
3. validate the exact reconciled PR head again
```

### B. EXECUTE THE FROZEN LIVE EXPERIMENT

The only intended repository path is:

```text
.github/workflows/v1-reasoning-context-value-live.yml
```

Manual confirmation required:

```text
RUN_SPEC_014_FROZEN
```

The workflow must run from `v1-reasoning-context-value` with repository secret `OPENAI_API_KEY` available.

Do not change the model, prompt, fixture, rubric, thresholds, repetitions, retry policy, SELECTIVE construction, or FULL_HORIZON construction before the live result is preserved.

### C. PRESERVE BEFORE INTERPRETING OR TUNING

After the live workflow:

```text
1. download/read the complete workflow artifact
2. preserve raw and aggregate result in the repository
3. create the live-result checkpoint
4. classify pass/failure under the frozen advancement rule
5. only then decide promotion or the next experiment
```

---

## 10. Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/OPEN_QUESTIONS.md
docs/DECISIONS.md
docs/PRINCIPLES.md

docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md

docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/research/021_first_reasoning_context_value_vertical_slice_design.md

experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md

docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
docs/checkpoints/145_reasoning_context_value_implementation_gate_cross_platform_passed.md
```