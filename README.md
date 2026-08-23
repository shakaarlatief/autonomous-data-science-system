# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

```text
checkpoint            154
active branch         v1-disposition-semantics-diagnostic
active PR             #15 -> v1-frontend-spike
promoted V1 head      10aa3f59bedc5ee45a38f0ae05c68da901d9adff
current boundary      Specification 016 provider-free gate passed; exact live-ready boundary frozen
```

The current progression is:

```text
Prototype V0
    strong falsification of the original P0 design

Specification 013
    accepted selective exact-revision MethodologicalContextPack

Specification 014
    real-model selective context preserved frozen reasoning quality
    while reducing provider input tokens by 66.56%

Specification 015
    first recommendation/action-value experiment
    frozen result FAIL
    failed implementation rejected
    negative evidence preserved separately

Specification 016 [active]
    DEFER-vs-NOT_NOW construct-validity diagnostic
    preregistered before implementation
    provider-free implementation green on Ubuntu and Windows
    secret-gated live boundary frozen
    no live Specification 016 call yet
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
```

---

## Durable post-V0 constraint

Prototype V0 strongly falsified the current P0 design. The broader ADS vision survived, but the original orchestration machinery did not earn its complexity.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore large always-on project/methodological context, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current V1 architecture

### Project semantics

Foundation 018 distinguishes:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

### Methodological navigation

Foundation 019 establishes:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The accepted bounded path now reaches through real reasoning:

```text
large reusable methodological knowledge universe
    -> retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

The transition from reasoning to recommendation/action semantics remains unresolved after Specification 015 and is the active diagnostic boundary.

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## Accepted V1 infrastructure and interaction boundaries

```text
D-028
    SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030
    pyproject.toml + uv + committed uv.lock + uv_build

D-031
    deterministic governed JSON / JSON Schema knowledge interchange

D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port

Specification 008
    promoted Project Cockpit interaction architecture
```

The governed reusable-knowledge persistence/interchange seam is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

The Project Cockpit remains the promoted primary immersive active-work model. Final frontend/chart/canvas choices, visual identity, semantic zoom, auto-layout, minimap, final stage taxonomy, and production backend/API architecture remain open.

---

## Retrieval, Horizon, and selective-context evidence

The first bounded methodological-navigation program progressed through:

```text
Checkpoint 135
    lexical retrieval Recall@3 = 1.00, MRR = 1.00

Checkpoint 137
    dense semantic comparator showed complementary signal

Checkpoint 139
    hybrid comparator preserved semantic top-three coverage

Specification 012 / Checkpoint 141
    first explained MethodologicalHorizon
    TRUE / FALSE / UNKNOWN applicability
    unknown != false

Specification 013 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack
```

On a deliberately wide ten-asset Horizon, Specification 013 selected only 2-3 exact revisions per case and reduced methodology-only context by approximately 65% to 84% while preserving required revision coverage.

---

## Accepted real-model reasoning-context seam

Specification 014 / Checkpoint 146 compared the accepted SELECTIVE pack with a compact FULL_HORIZON control under identical task evidence and model/runtime treatment.

```text
24 reasoner outputs
24 blinded judge outputs
0 retries

SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
critical regressions    none
```

Supported conclusion:

> The bounded selective exact-revision context preserved all frozen reasoning obligations while materially reducing real provider input burden.

This does not establish a universal context budget, final provider/model, or recommendation policy.

Primary evidence:

```text
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
```

---

## Failed first recommendation/action-value experiment

Specification 015 tested GENERIC, SELECTIVE, and FULL_HORIZON on four frozen project microstates using:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

The live workflow completed successfully as an execution:

```text
run                   32642733784
reasoner outputs      36 / 36
blinded judge outputs 36 / 36
provider attempts     72
retries               0
```

but the frozen advancement outcome was **FAIL**.

Fourteen of fifteen gates passed. The sole failed gate was `RA-G05`, because `RA-02 MODEL_CHOICE` SELECTIVE exact disposition accuracy was `0.666667` rather than at least `0.80`.

The repeated mismatch was:

```text
expected  DEFER
observed  NOT_NOW
```

for two noncritical expansion actions. SELECTIVE and FULL_HORIZON behaved identically, GENERIC almost identically, and every RA-02 semantic judge output scored `1.000000`.

The result remains a genuine failed gate. PR #13 containing the failed implementation was closed without merge. The negative evidence was preserved separately through PR #14 and merged into `v1-frontend-spike` at:

```text
10aa3f59bedc5ee45a38f0ae05c68da901d9adff
```

Primary evidence:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Active diagnostic: DEFER versus NOT_NOW

Specification 016 is deliberately not another GENERIC-vs-SELECTIVE value test. It first asks whether the exact-label boundary that failed Specification 015 can be made operational enough to evaluate reliably.

Experimental semantics:

```text
DEFER
    action already justified in the represented plan
    + exact unresolved supplied trigger
    + action becomes current next work once that trigger is satisfied
    + defer_until_id must identify the trigger

NOT_NOW
    current state/objective does not materially justify prioritizing the action
    + no supplied trigger is represented to activate it as current next work
    + defer_until_id must be null
```

Frozen benchmark:

```text
6 contrastive pairs
2 variants per pair
3 repetitions per variant
36 planned successful reasoner calls
45 maximum provider attempts
randomization seed 2026082302
```

No methodological assets, retrieval, Horizon, SELECTIVE treatment, semantic judge, tools, or authoritative project mutation participate.

Hard gates require:

```text
aggregate exact disposition accuracy >= 0.95
every variant >= 2/3 correct
every pair correct on both contrastive sides
all expected-DEFER trigger pointers exact
all expected-NOT_NOW pointers null
```

Frozen outcomes:

```text
DISPOSITION_BOUNDARY_SUPPORTED
DISPOSITION_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

### Provider-free implementation result

Checkpoint 153 records the exact implementation head:

```text
6e7af25fd96d79673a59845e1c608c752970f658
```

Cross-platform workflow `32646969810` passed:

```text
Ubuntu targeted       15 passed
Windows targeted      15 passed
Ubuntu full suite     62 passed, 2 skipped
Windows full suite    62 passed, 2 skipped
```

The same head also passed Checkpoint metadata and the existing V1 reasoning-context regression workflow.

The provider-free historical audit found that the two RA-02 expected-DEFER actions from Specification 015 do not satisfy the stronger Specification 016 construction rule for an unambiguous dependency-backed DEFER example. That is diagnostic evidence only and does not rescore Specification 015.

### Live boundary

Checkpoint 154 freezes the secret-gated live workflow:

```text
.github/workflows/v1-disposition-semantics-live.yml
manual confirmation: RUN_SPEC_016_FROZEN
branch: v1-disposition-semantics-diagnostic
```

No Specification 016 live provider call has occurred.

A pass would show only that this stronger dependency-backed distinction is representable and reliably classifiable on deliberately unambiguous cases. A failure would mean the taxonomy should be collapsed or redesigned before another recommendation-value comparison.

Primary active sources:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
tests/fixtures/reasoning/disposition_semantics_v1.json
docs/checkpoints/152_disposition_semantics_failure_attribution_contract_frozen.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
```

---

## Exact continuation

```text
1. validate the exact final PR #15 head under ordinary provider-free CI
2. require V1 disposition semantics diagnostic, V1 reasoning context value, and Checkpoint metadata to pass
3. after that exact head is green, make no further experiment-branch commits
4. copy only the identical live workflow to main for workflow_dispatch visibility
5. manually run V1 disposition semantics live from v1-disposition-semantics-diagnostic
6. enter RUN_SPEC_016_FROZEN
7. preserve the complete live artifact before interpretation or design changes
```

Do not modify Specification 015 in place. Do not change Specification 016's fixture, definitions, thresholds, repetitions, randomization, retry policy, or concrete experiment treatment after live results are observed.

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means when possible, preserve failures as evidence, and promote only what earns its complexity.
