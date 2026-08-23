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

Current execution state:

```text
checkpoint            151
active branch         v1-recommendation-action-failure-preservation
active preservation   PR #14 -> v1-frontend-spike
rejected experiment   PR #13, close without merge
promoted V1 head      bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
current boundary      failed Specification 015 evidence isolated from failed implementation; exact preservation-head validation
```

Specification 014 v1.0 / Checkpoint 146 established the first real-model evidence that selective exact-revision methodological context can preserve frozen reasoning quality while materially reducing provider input-token burden.

Specification 015 then tested whether that accepted methodological path adds downstream recommendation/action value beyond strong controls. The live workflow executed completely, but the preregistered advancement outcome is **FAIL** because one per-case exact-disposition gate failed on `RA-02 MODEL_CHOICE`.

The failure is narrow and not treatment-specific. SELECTIVE and FULL_HORIZON repeatedly chose `NOT_NOW` where frozen evaluator truth expected `DEFER` for two noncritical expansion actions; GENERIC behaved almost identically, while the blinded semantic judge scored every RA-02 output perfectly. The failed result is preserved exactly rather than repaired after observation.

Checkpoint 151 now separates the negative experiment evidence from the rejected implementation. PR #14 starts from the last accepted Specification 014 integration boundary and carries only the frozen design/fixture/checkpoints/result/artifact plus current routing. PR #13's failed recommendation implementation is deliberately absent.

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
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

The current executable path is:

```text
large reusable knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> reasoning evidence                         [accepted bounded seam]
    -> recommendation / REQUIRED-BLOCKING/action [first live seam failed]
```

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

### Accepted persistence, interchange, runtime, and interaction boundaries

```text
D-028
    SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030
    pyproject.toml + uv + committed uv.lock + uv_build

D-031
    deterministic governed JSON / JSON Schema 2020-12 knowledge interchange

Specification 008
    promoted Project Cockpit interaction architecture

D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
```

The governed reusable-knowledge persistence/interchange seam is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

Direct model calls remain the runtime fallback/reference path. LangGraph remains a possible stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

The Project Cockpit remains the promoted primary immersive V1 active-work interaction model, while specialist views remain alternative entry, inspection, and record paths.

---

## Retrieval, Horizon, and selective context progression

```text
Checkpoint 135
    production lexical retrieval
    RH-L Recall@3 = 1.00
    RH-L MRR      = 1.00

Checkpoint 137
    dense semantic comparator recovered class-imbalance but lost ecdf
    dense-only did not replace lexical

Checkpoint 139
    complementary equal-weight RRF comparator
    RH-S Recall@3 = 1.00
    RH-S MRR      = 0.875

Specification 012 v1.0 / Checkpoint 141
    accepted-current one-hop relation expansion
    TRUE / FALSE / UNKNOWN applicability
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT

Specification 013 v1.0 / Checkpoint 143
    selective exact-revision MethodologicalContextPack
```

The key semantic invariant is:

```text
unknown != false
```

On the deliberately wide ten-asset Horizon, Specification 013 selected only 2-3 exact revisions per frozen case and reduced methodology-only context by approximately 65% to 84% while preserving required revision coverage and explicit omission reasons.

---

## Accepted first real reasoning-context-value seam

Specification 014 v1.0 / Checkpoint 146 compared SELECTIVE against a compact FULL_HORIZON control under identical task evidence and model/runtime treatment.

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

---

## Failed first recommendation/action-value seam

Specification 015 v0.1 froze the first downstream test of:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> bounded project action
```

Conditions:

```text
GENERIC
    no reusable methodological assets

SELECTIVE
    accepted exact-revision MethodologicalContextPack

FULL_HORIZON
    all ten exact Horizon revisions
```

Live execution:

```text
workflow              V1 recommendation action value live
run                   32642733784
source head            d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
reasoner outputs       36 / 36
blinded judge outputs  36 / 36
provider attempts      72
retries                0
```

Frozen aggregate behavior:

```text
                         GENERIC      SELECTIVE      FULL_HORIZON
exact accuracy           0.916667     0.916667       0.916667
semantic score           0.960417     0.991667       0.991667
critical omissions       0            0              0
blocking false negatives 0            0              0
blocking false positives 1            0              0
under-recommendations    0            0              0
over-recommendations     0            0              0
unnecessary cost         0            0              0
```

The sole failed hard gate was per-case SELECTIVE exact accuracy on `RA-02 MODEL_CHOICE`:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
required floor 0.800000
```

The discrepancy was entirely `DEFER` versus `NOT_NOW` for two noncritical expansion actions. All nine RA-02 outputs scored `1.000000` under the blinded semantic rubric.

Frozen advancement remains:

```text
FAIL
```

No preregistered positive value signal was observed. The seam is not promoted. The correct next move is diagnosis, not threshold repair, evaluator relabeling, retrieval tuning, or project-state coupling.

Primary evidence:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
```

---

## Exact continuation

```text
1. validate the exact Checkpoint 151 / PR #14 preservation head
2. merge PR #14 into v1-frontend-spike only if green
3. close PR #13 without merge
4. create a separate diagnostic branch from the preserved integration head
5. preregister a bounded DEFER-vs-NOT_NOW / failure-attribution diagnostic
6. test disposition semantics independently from SELECTIVE-vs-control system value
7. make no new live calls before that diagnostic contract is frozen
```

Do not return to retrieval or selector tuning without a measured downstream reason. Do not promote the current benchmark disposition labels into production semantics from a failed gate.

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
