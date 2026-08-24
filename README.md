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
checkpoint            187
active branch         v1-methodological-navigation-coverage-diagnostic
active PR             #68
promoted V1 head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
current boundary      Question A diagnostic design choices resolved; Specification 022 not frozen
latest experiment     Specification 021
outcome               FAIL
next                  validate this design boundary, then freeze the exact
                      Specification 022 contract before implementation
```

Current experimental progression:

```text
Prototype V0       strong falsification of original P0 design
Specification 013  selective exact-revision context accepted
Specification 014  equal frozen reasoning quality with 66.56% fewer SELECTIVE input tokens
Specification 015  recommendation/action-value FAIL; implementation rejected
Specification 016  dependency-backed DEFER-vs-NOT_NOW boundary supported
Specification 017  relation-backed recommendation run incomplete; implementation rejected
Specification 018  governed autonomous live-experiment launcher supported/promoted
Specification 019  system-owned-provenance recommendation rerun completed; FAIL preserved
Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED boundary supported/promoted
Specification 021  complete supplied-action recommendation/disposition experiment FAIL; negative evidence preserved without implementation promotion
Checkpoint 183     clarified that supplied-action disposition calibration does not test open-world methodological navigation / coverage
Checkpoint 184     preservation-only promotion candidate for Specification 021 evidence and interpretation
Checkpoint 185     preservation merged, failed implementation closed, Question A architecture/evaluation review ready
Checkpoint 186     methodological-navigation / coverage architecture and evaluation review completed; Specification 022 not frozen
Checkpoint 187     project-state methodological coverage diagnostic design choices resolved; Specification 022 still not frozen
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/186_methodological_navigation_coverage_review_completed.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Durable post-V0 constraint

Prototype V0 strongly falsified the original P0 design. The broader ADS vision survived, but the original orchestration machinery did not earn its complexity.

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

The bounded executable path currently reaches:

```text
reusable methodological knowledge
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

The production-facing recommendation/action layer remains unpromoted because no frozen experiment has yet shown that selective explicit methodological context improves recommendation/action quality beyond the strong generic control.

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## Accepted infrastructure and interaction boundaries

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
```

The governed reusable-knowledge round-trip is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

Specification 008 promotes the **Project Cockpit** as the V1 primary immersive active-work interaction model. It is the intended user-facing environment for chat, project navigation, analytical workspaces, evidence, recommendations, decisions, and project state. Final frontend/chart/canvas choices and production backend/API architecture remain open.

Specification 018 promotes the first bounded governed live-experiment control plane:

```text
owner-created request
    -> repository authorization registry
    -> exact owner/source/green CI/duplicate checks
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

The launcher itself receives no provider credential and does not authorize arbitrary commands, workflows, refs, prompts, models, or secrets from issue text.

---

## Accepted selective-context evidence

Specification 013 accepted a bounded selector that reduces a deliberately wide ten-asset MethodologicalHorizon to 2-3 exact current revisions per task while retaining explicit omission evidence.

Specification 014 tested the downstream real-model consequence:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
retries                 0
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
critical regressions    none
```

Supported conclusion:

> Selective exact-revision methodological context preserved every frozen reasoning obligation while materially reducing real provider input burden on the bounded benchmark.

This does not establish a universal context budget or final provider/model.

---

## Recommendation/action evidence

### Specification 015

The first three-condition recommendation/action-value experiment classified `FAIL`. The failed implementation was not promoted. The main discrepancy was a preregistered `DEFER` versus `NOT_NOW` boundary.

### Specification 016

A prospective construct-validity diagnostic then showed that DEFER-like sequencing can be made reliably distinguishable when it is represented as an already-justified action waiting on one exact activating dependency:

```text
36 / 36 exact dispositions correct
18 / 18 DEFER pointers exact
18 / 18 NOT_NOW pointers null
0 retries
DISPOSITION_BOUNDARY_SUPPORTED
```

The bounded lesson is structural, not a final production-enum decision.

### Specification 017

The relation-backed recommendation/action comparison ended incomplete because model-authored `methodological_basis` duplicated system-known provenance. The durable instrumentation distinction became:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

### Specification 019

Specification 019 prospectively repaired that boundary by keeping exact supplied-context provenance system-owned while leaving recommendation content model-owned.

The governed live run completed the full frozen design:

```text
source                    6b5e6237b738250458550f95c9f3a6b0d51e86ec
reasoner outputs          36 / 36
judge outputs             36 / 36
provider attempts         72 / 90
retries                   0
execution integrity       true
```

Frozen aggregate result:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           0.944444       0.916667        0.944444
semantic score           0.950000       0.950000        0.950000
blocking false positives 4              6               4
```

Frozen outcome:

```text
absolute gates           FAIL
relative gates           FAIL
expansion gates          FAIL
positive value signals   0
advancement outcome      FAIL
```

Specification 019 remains immutable historical `FAIL` evidence and its failed recommendation/action implementation is not promoted.

### Specification 020

Specification 020 prospectively isolated the remaining `RECOMMENDED` versus `BLOCKING_REQUIRED` calibration boundary using explicit requirement/scope relations and no methodological-context treatment.

The governed live design completed exactly as frozen:

```text
frozen source            82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
reasoner outputs         36 / 36
validated observations   36 / 36
provider attempts        36 / 45
failed attempts          0
retries                   0
aggregate exact accuracy 1.000000
all hard gates           PASS
outcome                  BLOCKING_BOUNDARY_SUPPORTED
```

All six contrastive pairs separated perfectly across all three repetitions per side. Every expected `BLOCKING_REQUIRED` output returned the exact unresolved requirement and exact blocked downstream scope. Every expected `RECOMMENDED` output returned both blocking pointers as null.

Supported bounded conclusion:

```text
BLOCKING_REQUIRED-like work
    should identify an exact unresolved requirement
    + an exact active defended downstream scope
    + an explicit scope DEPENDS_ON requirement relation
    + the action that resolves that requirement
```

This makes taxonomy inseparability and fixed-reasoner inability less likely explanations for Specification 019's RB-02 behavior. Specification 019 is not rescored.

Specification 020 does not establish production recommendation enums, final blocking policy, SELECTIVE recommendation value, ranking, open-world action generation, automatic execution, or final provider/model selection.

The cleaned exact PR #44 head passed the Specification 020 Ubuntu/Windows diagnostic plus accepted V1 reasoning-context, disposition-semantics, launcher, and checkpoint-metadata regressions before merge into `v1-frontend-spike` at `a856983172f6436b73e3f7d0e609d208b55a443b`.

Primary evidence:

```text
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
```

---

## System-owned provenance boundary

Specifications 017-020 established a useful separation:

```text
SYSTEM-OWNED PROVENANCE / IDENTITIES
    exact supplied stable_key@revision_id
    methodology payload digest and byte count
    treatment identity
    supplied action / requirement / downstream-scope identities

MODEL-OWNED CONTENT
    dispositions
    dependency pointers among supplied identities
    clarifications
    rationales
```

The model should not be required to reproduce authoritative context provenance that the system already knows exactly.

---

## Preservation and continuity hardening

The Specification 020 stage-boundary review found no substantive preservation failure. It did confirm recurring lag in mutable routing/current-state documents relative to already durable checkpoint/result evidence.

Checkpoint 172 records the first green hardening of that observed consistency seam:

```text
docs/current_routing.json
    machine-readable routing metadata only

scripts/check_current_routing.py
    manifest contract + checkpoint existence + contradiction checks

.github/workflows/current-routing-consistency.yml
    Ubuntu/Windows validation for routing-sensitive changes
```

Exact pre-checkpoint implementation head `5f5dfb81a97f089afc91f20d4632683714a43f60` passed the routing workflow and the accepted V1 blocking-calibration, reasoning-context, disposition-semantics, and autonomous-launcher regression seams.

The final PR #54 head `44d92d73029ad56925bd2c49bb373be5bdef44ce` then passed checkpoint metadata, cross-platform routing consistency, and all applicable accepted V1 regression seams before merge into `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`.

The integration reconciliation is deliberately routing-sensitive so the new push guard must validate the merged branch state itself, not only the pre-merge pull-request head.

Markdown remains the substantive source of project knowledge. The manifest does not become a new repository for rationale, decisions, specifications, experiment interpretation, or historical evidence. Development Method remains v0.4 because its existing rule already permits narrow partial automation once repetitive or inconsistent maintenance is observed.

This hardening is not a justification for graph/vector preservation storage or wholesale machine-generated documentation.

---

## Exact continuation

```text
1. validate the Checkpoint 186 review branch and canonical routing
2. align on Research 031's state-to-methodological-horizon evaluation architecture
3. resolve the still-open benchmark/oracle/condition/metric design questions recorded there
4. only then prospectively freeze Specification 022
5. do not rerun the supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures and incomplete runs as evidence, and promote only what earns its complexity.

## Specification 021 interpretation boundary

The complete Specification 021 result is `FAIL`, but its scope is deliberately narrow. Every condition was already supplied with the explicit reasoning function, candidate action menu, requirements, downstream scopes, dependency/resolver relations, defer triggers, and sequencing relations. The experiment therefore tested downstream disposition calibration over an already-constructed decision space, not whether ADS can discover and surface the methodological option space from raw evolving project state.

Research 030 and Checkpoint 183 preserve the guardrail:

```text
methodological navigation / coverage
    !=
downstream disposition calibration over an already supplied action set
```

GENERIC remains an essential experimental control, not an architectural replacement for the methodological-navigation brain described by Foundations 006, 017, 019, 020 and Research 028.

## Methodological navigation coverage review

Research 031 and Checkpoint 186 move the successor evaluation boundary upstream from supplied-action disposition calibration.

The recommended decomposition is:

```text
UNIVERSE COVERAGE
    -> NAVIGATION / PATH COVERAGE
    -> APPLICABILITY / MISSING CONTEXT
    -> CONCRETE OPTION GENERATION
    -> PRIORITIZATION / DISPOSITION
    -> MODEL-FACING CONTEXT VALUE
```

A methodological-universe gap, a navigation gap, and a downstream reasoning/use gap are separate failure classes. The proposed first successor experiment class is a bounded project-state-to-methodological-horizon coverage diagnostic focused primarily on path discovery and applicability/missing-context handling. Specification 022 is not frozen.
