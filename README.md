# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that can own project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

Current execution state:

```text
checkpoint            149
active branch         v1-recommendation-action-value
active PR             #13 -> v1-frontend-spike
promoted V1 head      bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
current boundary      Checkpoint 149 live-ready boundary frozen; manual live dispatch next
```

Specification 014 v1.0 / Checkpoint 146 established the first real-model evidence that selective exact-revision methodological context can preserve frozen reasoning quality while materially reducing provider input-token burden.

Specification 015 moves downstream from context economy to recommendation/action quality: whether ADS helps a strong reasoner distinguish `RECOMMENDED` from `REQUIRED / BLOCKING`, preserve validity dependencies, avoid important omissions, and avoid unnecessary work.

Checkpoint 148 records the complete provider-free Specification 015 implementation. Checkpoint 149 freezes the reconciled live-ready boundary after the checkpoint commit, provider-free recommendation/action workflow, checkpoint metadata, and inherited reasoning-context regression all remained green.

The manual secret-gated live workflow is exposed on the default branch as the dispatcher surface but has not been executed.

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
```

---

## Prototype V0 result and durable constraint

Prototype V0 compared:

```text
B0 = strong LLM + Python + project artifacts + strong generic data-science instructions

B1 = B0 + four methodological concepts supplied statically

P0 = same strong LLM + typed project state + structured knowledge activation
     + prospective safeguards + state-derived action selection
     + dependency-aware repair
```

Final pooled evidence:

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
```

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

The strongest scaling lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

V0 did not reject persistent project memory, reusable methodological knowledge, provenance, or the broader ADS vision. It rejected carrying P0's large always-on state/context, path-sensitive activation, generic recursive reopening, and full frontier machinery forward unchanged.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current V1 architecture

### Project and methodological semantics

The project object model distinguishes:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

with important separations including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

Methodological navigation follows:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The current executable scaling path is:

```text
large reusable methodological knowledge universe
    -> high-recall retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> reasoning evidence
    -> recommendation / REQUIRED-BLOCKING / bounded action evidence
```

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

### Accepted persistence, interchange, runtime, and interaction boundaries

Accepted V1 decisions and promoted contracts include:

```text
D-028
    SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030
    pyproject.toml + uv + committed uv.lock + uv_build

D-031
    JSON + JSON Schema Draft 2020-12
    semantic validation
    deterministic reusable-knowledge normalization/serialization

Specification 008
    promoted Project Cockpit interaction architecture

D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

The governed reusable-knowledge persistence/interchange seam is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

Direct model calls remain the runtime fallback/reference path. LangGraph remains a possible stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

The Project Cockpit remains the promoted primary immersive V1 active-work interaction model, while specialist views remain alternative entry, inspection, and record paths.

---

## Retrieval and MethodologicalHorizon progression

The first bounded methodological-navigation program progressed through:

```text
Checkpoint 135
    production lexical retrieval
    RH-L Recall@3 = 1.00
    RH-L MRR      = 1.00

Checkpoint 137
    exact dense semantic comparator
    recovered class-imbalance but lost ecdf
    dense-only did not replace lexical

Checkpoint 139
    complementary equal-weight RRF comparator
    RH-S Recall@3 = 1.00
    RH-S MRR      = 0.875

Specification 012 v1.0 / Checkpoint 141
    accepted-current one-hop relation expansion
    TRUE / FALSE / UNKNOWN applicability
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    explained MethodologicalHorizon
```

The key semantic invariant is:

```text
unknown != false
```

The hybrid retrieval result is evidence for lexical+dense complementarity. It does not permanently select FastEmbed, BGE, RRF `k=60`, embedding persistence, ANN, reranking, or a vector database.

---

## Accepted selective MethodologicalContextPack seam

Research 020 and Specification 013 tested the first deterministic RH-C policy:

```text
explicit requested reasoning functions
    -> primary Horizon matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current compact context reads
    -> MethodologicalContextPack
```

The system/model boundary is explicit:

```text
SYSTEM
    retains Horizon
    retains selection/omission decisions and reasons

MODEL-FACING PACK
    contains selected methodological knowledge only
```

On the deliberately wide ten-asset Horizon:

```text
              selected     full bytes   selective   ratio
RH-C01        2 / 10         10,744       2,151     0.2002
RH-C02        2 / 10         10,752       1,770     0.1646
RH-C03        3 / 10         10,752       3,724     0.3464
RH-C04        2 / 10         10,754       3,035     0.2822
```

Equivalent methodology-only context reduction was approximately **65% to 84%** while preserving required stable-key/revision coverage and explicit omission reasons. Checkpoint 143 promotes Specification 013 to accepted bounded v1.0.

This does not prove that explicit reasoning functions solve general semantic relevance or that `max_assets = 3` is universal.

---

## Accepted first real reasoning-context-value seam

Specification 014 v1.0 / Checkpoint 146 preserve the first downstream real-model test of the accepted selective `MethodologicalContextPack` against a compact full-Horizon control under the same task evidence and model/runtime configuration.

Observed:

```text
24 / 24 reasoner outputs
24 / 24 blinded judge outputs
0 retries

aggregate quality
    SELECTIVE      1.000000
    FULL_HORIZON   1.000000

aggregate provider input tokens
    SELECTIVE mean 1013.00
    FULL mean      3029.50
    ratio          0.334379
    reduction      66.56%
```

Every matched pair used fewer SELECTIVE input tokens. No critical-obligation regression or unsupported methodological-basis reference occurred.

FULL_HORIZON produced more unexpected methodological-basis expansion, but both conditions reached the frozen quality ceiling. The supported conclusion is bounded quality preservation plus substantial token reduction, not proof that fuller context generally harms reasoning.

Primary evidence:

```text
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
experiments/reasoning_context_value/results/spec014-live-20260823-run-32635061634/
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
```

The result does not select a final provider/model, universal context budget, general relevance solution, or recommendation/REQUIRED-BLOCKING policy.

---

## Active experiment: recommendation and action value

Specification 015 v0.1 / Checkpoints 147-149 govern the first downstream test of:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> bounded project action
```

Three conditions hold the project microstate, explicit reasoning-function profile, candidate action menu, output schema, and concrete model/runtime configuration fixed:

```text
GENERIC
    no reusable methodological assets

SELECTIVE
    accepted exact-revision MethodologicalContextPack

FULL_HORIZON
    all ten exact Horizon revisions
```

The four frozen microstates test:

```text
RA-01  future-prediction validity gate
RA-02  compact nonlinear model choice
RA-03  bounded distribution-evidence plan
RA-04  interacting missingness/class-imbalance decisions
```

Every candidate action must be classified exactly once as:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

Primary evaluation is deterministic, including exact disposition accuracy, critical omissions, under/over-recommendation, unnecessary action cost, blocking-scope errors, clarification misses, and basis provenance. A condition-blinded semantic judge is secondary for rationale/dependency correctness.

The advancement rule deliberately distinguishes:

```text
PROMOTE_BOUNDED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

so a ceiling result against strong controls cannot be post-hoc reinterpreted as additional ADS value.

### Provider-free gate

Checkpoint 148 preserves implementation head:

```text
6ccfd15d194a4205b2f554268ccad05fbd38edda
```

Cross-platform workflow:

```text
V1 recommendation action value
run 32640518712

Ubuntu
    dedicated  12 passed
    full suite 63 passed, 2 skipped

Windows
    dedicated  12 passed
    full suite 63 passed, 2 skipped
```

Both jobs explicitly verified that `OPENAI_API_KEY` was absent. The two skips are the existing PostgreSQL-dependent tests without `ADS_TEST_POSTGRES_URL`.

The complete fake-runtime 36 reasoner + 36 blinded-judge design deliberately returns perfect recommendations in all three conditions. The evaluator correctly returns:

```text
SAFE_BUT_NOT_DIFFERENTIATED
```

This proves the experiment machinery does not manufacture a benefit when strong controls tie. It is not evidence about the real treatment comparison.

The runner also verifies:

```text
GENERIC       no reusable methodological assets
SELECTIVE     exact 2-3 accepted revisions
FULL_HORIZON  exact ten accepted revisions
reasoner      evaluator truth excluded
judge         treatment/evaluator truth blinded
project state unchanged before/after
knowledge authority unchanged before/after
```

### Live-ready boundary

Checkpoint 149 freezes the reconciled pre-live boundary. Its checkpoint commit passed:

```text
Checkpoint metadata                 run 32641146841   PASS
V1 recommendation action value      run 32641146842   PASS
V1 reasoning context value          run 32641146840   PASS
```

The recommendation/action workflow passed on both Ubuntu and Windows and again verified that the ordinary CI environment did not receive the live provider credential.

The manual workflow is exposed on the default branch as a dispatcher but requires the experiment ref:

```text
workflow      V1 recommendation action value live
branch        v1-recommendation-action-value
secret        OPENAI_API_KEY
confirmation  RUN_SPEC_015_FROZEN
```

No live Specification 015 reasoner or judge call has occurred.

Primary active sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
```

---

## Exact continuation

```text
1. keep the frozen Specification 015 treatment unchanged
2. manually dispatch V1 recommendation action value live
3. select branch v1-recommendation-action-value
4. enter confirmation RUN_SPEC_015_FROZEN
5. preserve the complete raw/result bundle before any tuning
6. apply the frozen PROMOTE_BOUNDED_RECOMMENDATION_SEAM / SAFE_BUT_NOT_DIFFERENTIATED / FAIL classification exactly
7. create the live-result checkpoint before merge, repair, or subsequent experiment design
```

The default branch exposes only the manual workflow dispatcher. The live workflow itself refuses any ref other than `v1-recommendation-action-value`.

Do not change the fixture, action menus, model/runtime treatment, prompts, rubric, thresholds, repetitions, randomization, retry policy, context construction, retrieval stack, or recommendation evaluator before the live result is preserved.

---

## Repository role

This repository is the project's durable source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable knowledge is extracted into repository artifacts so the project does not depend on conversational memory or any single chat remaining available.

The core maxim remains:

> **The chat is where we think. The repository is where the system remembers.**

## Development philosophy

The project deliberately resists two opposite mistakes:

```text
Mistake 1:
Assume that because a strong LLM can already do impressive data-science reasoning,
there is no value in system-level process machinery.

Mistake 2:
Assume that because the long-term vision is broader than one LLM conversation,
every piece of orchestration machinery is automatically justified.
```

The current stance is empirical:

> **Build the smallest mechanism that can test the architectural hypothesis, preregister what success means when possible, preserve failures as evidence, and promote only what earns its complexity.**