# Research 154: Candidate 01 Zero-Seed Successor-Native Routing Fixture Freeze

**Date:** 2026-09-14
**Status:** ZERO-SEED ROUTING FIXTURE + SUCCESSOR SHADOW SOURCES FROZEN BEFORE IMPLEMENTATION / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Freeze two successor-native shadow canonical sources plus the exact routing fixture/oracle before implementation, so current routing can be regenerated without reading or copying live global-state authority during generation.
**Authority:** Experimental protocol only. The shadow sources are not current project authority. Requirements V0.2 and the current continuity architecture remain authoritative.
**Declared references:** `research:153`, `research:144`, `checkpoint:498`, `path:docs/current_routing.json`

## 1. Exact experiment boundary

The real compatibility target is frozen at commit:

```text
4da4cfecc052b2f339e14dba0e91525662c144b2
```

Frozen experiment artifacts:

```text
ZERO_SEED_ROUTING_FIXTURE_V01.json
    SHA-256  25d302e1fd46afdc1f7e1d363cd8eeedc5881c055aeb2ab79655bae756364594

ZERO_SEED_ROUTING_ORACLE_V01.json
    SHA-256  9687bfe08c32a4bab7718f7f7ace3fb60f6a3d015ff468cbd7431d39c2b38e64

SHADOW_WORKSTREAM_SOURCE.md
    SHA-256  55d95022fef3145aa3ee1e6cddfb9b311f139fcf77ab2772202e1940e0ea298d

SHADOW_PROJECT_INTEGRATION_BOUNDARY.md
    SHA-256  5ef9e53ff021d246c8e46bad8665fa3fd28f9b98ad770327aa57c083930531e1
```

No zero-seed routing implementation exists at this boundary.

## 2. Successor-native shadow source 1: primary active workstream

`SHADOW_WORKSTREAM_SOURCE.md` is a repository-native rich Markdown source with one adjacent machine-readable declaration. It owns only the control facts Research 153 assigned to the primary active workstream:

```text
active development branch
active PR / explicit null state
current checkpoint
current semantic boundary
```

The source is explicitly `shadow_only=true`. Its internal `authority_class=canonical` means canonical **inside the successor shadow model**, not current project authority.

## 3. Successor-native shadow source 2: Project Integration Boundary

`SHADOW_PROJECT_INTEGRATION_BOUNDARY.md` keeps the promoted branch and promoted exact commit adjacent as one semantic fact:

```text
promoted_branch
promoted_commit
promotion_provenance
```

This is the narrow project-wide semantic source added by Research 153. It deliberately does not grow into a general project-control registry.

## 4. Zero-seed generation contract

During generation, the implementation may read:

```text
the two frozen shadow successor sources
Specification 027 at the frozen real base
Checkpoint 192 at the frozen real base
```

It may not read:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

The current routing target may be opened only after the generated object exists, for comparison.

The fixture explicitly records:

```text
global_live_state_generation_fact_count = 0
manual_shadow_source_touch_count = 2
```

This is the distinction Research 153 required. The migration happened **into successor-native sources before generation**; the generator itself receives no global-state seed facts.

## 5. Facts and owners frozen for V0.1

```text
active_development_branch
active_pr
current_checkpoint
current_boundary
    -> primary active workstream execution anchor

promoted_integration_branch
promoted_integration_sha
    -> Project Integration Boundary

latest_specification
    -> computed from real Specification 027

latest_experiment_outcome
    -> computed from real Checkpoint 192 governed outcome
```

The routing compatibility schema remains unchanged for this experiment.

## 6. What this experiment can and cannot prove

A pass would show that Candidate 01 can reproduce the current routing compatibility surface after the relevant live facts have been relocated into narrower successor-native canonical sources. It would also measure the immediate source-touch burden: two shadow canonical sources instead of a broad project-control registry.

A pass would **not** prove that those source files/encodings are final production choices, that automatic migration is solved, or that `CURRENT_STATE.md` is already safely derivable.

## 7. Freeze preflight

Before this record was written, a model-free preflight verified:

```text
fixture/oracle IDs match
forbidden expected-answer keys absent
2 successor shadow sources match frozen bytes/hashes
both structured declarations parse
both are shadow-only canonical-in-candidate-model sources
Specification 027 / Checkpoint 192 / routing target match exact base bytes/hashes
only routing_target is a comparison target
global_live_state_generation_fact_count = 0
manual_shadow_source_touch_count = 2
ZERO_SEED_ROUTING_V01_FREEZE_PREFLIGHT=PASS
```

```text
RESEARCH154=ZERO_SEED_ROUTING_FIXTURE_FROZEN
FIXTURE_SHA256=25d302e1fd46afdc1f7e1d363cd8eeedc5881c055aeb2ab79655bae756364594
ORACLE_SHA256=9687bfe08c32a4bab7718f7f7ace3fb60f6a3d015ff468cbd7431d39c2b38e64
SUCCESSOR_SHADOW_SOURCES=2
GLOBAL_LIVE_STATE_GENERATION_FACTS=0
IMPLEMENTATION=NOT_YET_WRITTEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_ZERO_SEED_ROUTING_V01
```
