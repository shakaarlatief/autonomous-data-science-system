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
checkpoint            156
active branch         v1-recommendation-action-value-relation-backed
active PR             #16 -> v1-frontend-spike
promoted V1 head      6bda0c1efcf078476859b2c2c64fb0586964899d
current boundary      Specification 017 frozen before implementation/live calls
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

Specification 016
    isolated dependency-backed DEFER-vs-NOT_NOW construct validity
    all frozen live gates passed
    outcome DISPOSITION_BOUNDARY_SUPPORTED
    promoted at 6bda0c1efcf078476859b2c2c64fb0586964899d

Specification 017 [active]
    second recommendation/action-value contract frozen
    GENERIC vs SELECTIVE vs FULL_HORIZON
    relation-backed defer pointers
    no implementation or live call yet
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
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

The next active test is whether that explicit methodological path adds downstream recommendation/action value once sequencing truth is represented with exact activating dependency pointers.

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

The live workflow completed all planned reasoner and judge calls with no retries, but the frozen advancement outcome was **FAIL**.

Fourteen of fifteen gates passed. The sole failed gate was `RA-G05`, because `RA-02 MODEL_CHOICE` SELECTIVE exact disposition accuracy was `0.666667` rather than at least `0.80`.

The repeated mismatch was:

```text
expected  DEFER
observed  NOT_NOW
```

for two noncritical expansion actions. SELECTIVE and FULL_HORIZON behaved identically, GENERIC almost identically, and every RA-02 semantic judge output scored `1.000000`.

The result remains a genuine failed gate. PR #13 containing the failed implementation was closed without merge. The negative evidence was preserved separately through PR #14.

Primary evidence:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Supported dependency-backed disposition diagnostic

Specification 016 did not test system value. It isolated whether a stronger `DEFER` versus `NOT_NOW` boundary could be represented and classified reliably.

Relation-backed semantics:

```text
DEFER
    action already justified in represented plan
    + exact unresolved supplied trigger
    + action becomes current next work after the trigger
    + exact defer_until_id

NOT_NOW
    no material current justification
    + no represented supplied activating trigger
    + null defer_until_id
```

Live result:

```text
run                                  32652636943
reasoner outputs                     36 / 36
provider attempts                    36 / 45
failed attempts                      0
retries                              0
aggregate exact disposition accuracy 1.000000
all variants                         3 / 3 correct
all pair sides                       3 / 3 correct
DEFER exact pointer accuracy         1.000000
NOT_NOW null-pointer correctness     1.000000
outcome                              DISPOSITION_BOUNDARY_SUPPORTED
```

Supported bounded conclusion:

> A dependency-backed `DEFER` definition is operationally representable, and the frozen reasoner can distinguish it from `NOT_NOW` on deliberately unambiguous contrastive project microstates.

This is a design/evaluation constraint, not a final production enum or persistence contract.

Primary evidence:

```text
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

---

## Active Specification 017 experiment

Specification 017 returns to the unresolved downstream system-value question under the stronger relation-backed construction.

Frozen question:

> Does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than FULL_HORIZON?

Conditions:

```text
GENERIC
SELECTIVE
FULL_HORIZON
```

Frozen cases:

```text
RB-01  VALIDITY_GATE_AND_SEQUENCE
RB-02  COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE
RB-03  DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION
RB-04  MISSINGNESS_IMBALANCE_DECISION_SEQUENCE
```

Every action decision now includes:

```text
action_id
disposition
defer_until_id
rationale
```

Frozen pointer rule:

```text
DEFER
    exact supplied unresolved activating trigger required

BLOCKING_REQUIRED / RECOMMENDED / NOT_NOW
    null defer pointer required
```

The new benchmark does not relabel the historical Specification 015 cases. It constructs new expected-DEFER states prospectively with explicit triggers.

Advancement outcomes:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

A promotion claim requires all absolute, relative, and expansion gates plus at least one preregistered positive value signal. If all quality gates pass but GENERIC remains equally strong, the result is explicitly `SAFE_BUT_NOT_DIFFERENTIATED`.

Frozen call plan:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 condition-blinded judge outputs
72 planned successful provider calls
90 maximum provider attempts
randomization seed 2026082303
```

No Specification 017 live provider call has occurred.

Primary active sources:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
```

---

## Exact continuation

```text
1. implement the relation-backed recommendation result and validator
2. implement frozen GENERIC / SELECTIVE / FULL_HORIZON condition construction
3. implement deterministic action/scope/clarification/pointer metrics
4. implement blinded semantic judging
5. add complete fake-runtime and real-persistence provider-free tests
6. add ordinary Ubuntu/Windows CI with no live provider key
7. preserve the exact green implementation head
8. only then expose the secret-gated live workflow
9. make no new live model call before that boundary
```

Do not modify or rescore Specifications 015 or 016. Do not change Specification 017's fixture, thresholds, value signals, randomization, call plan, retry policy, or model/runtime treatment after live outputs are observed.

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means when possible, preserve failures as evidence, and promote only what earns its complexity.
