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

**Prototype V0 is complete. The project is now in the first serious methodological knowledge-universe construction stage of bounded V1.**

```text
checkpoint            193
active branch         v1-methodological-knowledge-universe
active PR             #73
promoted V1 head      bb5d0640fff633e87a6a8c024b1a842fadd85a9d
current boundary      knowledge-universe construction framework frozen;
                      six-slice representation pressure test next
latest specification  Specification 022
latest experiment     Specification 022
outcome               INCOMPLETE
```

The active construction sources are:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

The next step is not another small provider benchmark and not bulk generation of thousands of method summaries.

It is:

```text
register source bundles
    -> pressure-test the representation deeply across six heterogeneous areas
    -> record representation defects
    -> revise where warranted
    -> then begin broader accepted-core construction
```

The first six deep slices are:

```text
Validation
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

---

## Why the project changed emphasis

Earlier V1 work deliberately used small controlled knowledge universes to isolate retrieval, Horizon construction, selective context, reasoning, and recommendation seams.

That produced important evidence, but the balance has now changed.

The project has already established enough substrate around:

```text
project state
reusable knowledge representation
exact revisions and provenance
governed persistence / interchange
retrieval
applicability / missing context
MethodologicalHorizon construction
selective context
real reasoning
```

that keeping the methodological universe artificially tiny would now hide important architectural problems.

The current strategy is therefore:

```text
current architecture
    -> build serious source-backed knowledge
    -> discover where the representation breaks or strains
    -> refine it
    -> continue construction
    -> test on real projects
    -> govern knowledge evolution
```

Checkpoint 191 established the chronological direction:

```text
1. serious governed methodological knowledge universe
2. navigation / selection over that universe
3. project-specific concern / question / option generation
4. prioritization / disposition
5. execution and project-state update
6. real end-to-end project trials
7. governed knowledge evolution
```

The arrows are intentionally reversible when later stages expose missing or badly represented knowledge.

---

## Durable post-V0 constraint

Prototype V0 strongly falsified the original P0 implementation strategy.

The broader ADS vision survived, but the original always-on orchestration machinery did not earn its cost.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The serious knowledge universe is therefore system memory and methodological structure. It must not become one giant prompt.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current architectural core

Foundation 018 separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

and preserves distinctions including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
```

Foundation 019 defines the methodological-navigation progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Foundation 020 provides the current reusable-knowledge representation direction:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
exact revision identity
provenance
```

Foundation 008 governs reuse, generalization, challenge, maturity, and enforcement.

The current representation is deliberately not treated as final. Serious content construction is expected to pressure-test it.

---

## Accepted infrastructure and interaction boundaries

Accepted V1 decisions include:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime
```

The governed reusable-knowledge round-trip is closed across SQLite/Linux, SQLite/Windows, and PostgreSQL 18.

Specification 008 promotes the Project Cockpit interaction architecture.

Specification 018 promotes the bounded governed live-experiment launcher.

Candidate or benchmark knowledge cannot silently create accepted methodological authority through the accepted interchange boundary.

---

## Retrieval and selective-context evidence

The bounded accepted chain is:

```text
lexical retrieval
    -> dense complementarity
    -> hybrid comparator
    -> explained MethodologicalHorizon
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

Specification 014 showed:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
```

This supports selective context economy on the bounded benchmark. It does not establish the final navigation strategy for a serious knowledge universe.

---

## Recommendation/action evidence remains bounded

Later experiments produced several distinct results:

```text
Specification 015  FAIL
Specification 016  dependency-backed DEFER-vs-NOT_NOW boundary supported
Specification 017  INCOMPLETE
Specification 019  FAIL after provenance repair
Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED boundary supported
Specification 021  FAIL on supplied-action recommendation value
Specification 022  INCOMPLETE / EXECUTION INTEGRITY FAILED
```

The important guardrail from Research 030 remains:

```text
methodological navigation / coverage
    !=
downstream disposition calibration over an already supplied action set
```

The recent recommendation experiments therefore do not replace the need to build a real methodological option space.

---

## Specification 022 boundary

Specification 022 moved evaluation upstream from an already supplied action menu to evolving project state and a controlled methodological universe.

Its live run used exact source:

```text
cf5893d74fefa699296842b0a48326a9cb50161c
```

Observed execution:

```text
planned reasoner observations     108
valid reasoner observations         0
planned judge observations        108
valid judge observations            0
provider attempts                 216
execution_complete                false
execution_integrity               false
advancement_outcome               none
```

The frozen schema accepted only:

```text
CURRENT
MISSING_CONTEXT
```

while the live model repeatedly returned semantically natural alternative state labels. Every structured result was rejected before judge execution.

The preserved scientific classification is:

```text
INCOMPLETE / EXECUTION INTEGRITY FAILED
```

There is no legitimate comparative conclusion for `GENERIC`, `ADS_HORIZON`, or `ORACLE_HORIZON`.

The incomplete implementation was not promoted. Its durable evidence/history was preserved through Checkpoints 191-192 and PR #72.

No immediate Specification 022 rerun is planned.

---

## Serious knowledge-universe construction framework

Research 033 establishes the first construction-cycle rules.

### Coverage map is not authority

`docs/methodological_knowledge/COVERAGE_MAP.md` is a planning and gap-visibility view, not a methodological truth store.

### Coverage depth is not maturity

The first construction-depth ladder is:

```text
C0  MAPPED
C1  SOURCED
C2  DECOMPOSED
C3  OPERATIONALIZED
C4  CONNECTED
C5  BEHAVIORALLY_TESTED
C6  PROJECT_EXPOSED
```

These levels do not mean confidence, truth, freshness, or enforcement authority.

### Knowledge target is operational

Useful reusable knowledge may include:

```text
question templates
evidence requirements
hard invariants
decision principles
strategies and alternatives
investigation templates
assumptions
failure modes and detection hooks
diagnostics
claim constraints
human / authority hooks
relations
conditional rules
resolution / reopen criteria
limitations and counterexamples
provenance
revision / governance state
```

### Source authority is proposition-sensitive

There is no universal source-ranking rule. Mathematical definitions, empirical methodology, software behavior, standards, and local project facts require different appropriate source classes.

### LLMs assist, but do not self-authorize

LLMs may extract, decompose, propose relations, find duplicate candidates, challenge scope, and draft behavioral cases. Model output alone is not independent support for accepted reusable knowledge.

### Existing governance remains authoritative

Candidate knowledge must pass through the accepted interchange/governance boundary rather than bypassing it through informal files or model output.

---

## First pressure-test program

Before broad accepted-asset authoring, each of the six slices should produce a packet containing:

```text
slice boundary and purpose
source bundle / source-register candidates
coverage decomposition
canonical concept candidates
candidate asset/component boundaries
question templates
evidence requirements
alternatives / strategies / methods
failure modes and claim constraints
relation candidates
conditional-rule candidates
provenance-granularity examples
duplicate / contradiction examples
behavioral cases
representation problems discovered
```

The point is to learn where the current representation succeeds and fails under real methodological depth.

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

Stable project knowledge is separated across canonical documents, foundations, research memos, specifications, checkpoints, experiment evidence, routing indexes, and Git history.

The project continues to follow the empirical rule that explicit mechanisms and promoted authority must earn their place through evidence.

---

## Start here

For the current stage:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

For the governing reusable-knowledge architecture:

```text
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```

For the transition out of Specification 022:

```text
docs/checkpoints/191_specification_022_live_execution_incomplete_knowledge_universe_next.md
docs/checkpoints/192_specification_022_incomplete_result_preservation_promotion_candidate.md
experiments/methodological_navigation_coverage/V1_METHODOLOGICAL_NAVIGATION_COVERAGE_RESULT.md
```

## Exact next step

```text
1. validate the Checkpoint 193 / Research 033 / coverage-map framework head
2. design the source-register and source-bundle candidate contract
3. build one coordinated six-slice representation pressure-test packet
4. use existing controlled source material only after source registration
5. add stronger external/authoritative sources where proposition support requires them
6. preserve every representation defect instead of forcing content into the current schema
7. revise the representation only where content pressure warrants it
8. then begin broader accepted-core knowledge construction
9. resume navigation/selection evaluation against the serious universe
10. begin real project trials before the universe is complete
```
