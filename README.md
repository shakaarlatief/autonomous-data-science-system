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
checkpoint            175
active branch         v1-dependency-backed-recommendation-value
active PR             #55 draft
promoted V1 head      a639cfc570290a2169425f43078bbb242fa398e9
current boundary      Specification 021 provider-free implementation green;
                      separate governed live boundary next
latest experiment     Specification 021
outcome               PROVIDER_FREE_IMPLEMENTATION_GREEN
next                  validate this reconciled exact head,
                      freeze the separate pre-live boundary,
                      and only then introduce a live entry path
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
Checkpoint 173     machine-checkable current-routing hardening promoted and closed
Specification 021  dependency-backed recommendation-value contract frozen;
                   provider-free implementation green; not run live
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/174_specification_021_dependency_backed_recommendation_value_contract_frozen.md
docs/checkpoints/175_specification_021_provider_free_implementation_gate_cross_platform_passed.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/research/029_dependency_backed_recommendation_value_design.md
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
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

The accepted bounded executable path currently reaches:

```text
reusable methodological knowledge
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

Foundation 020 separates reusable methodological knowledge from project state, execution implementation, and presentation.

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Research 028 preserves the broader forward architecture:

```text
SYSTEM-OWNED PROJECT STATE
    What is true about this project?

METHODOLOGICAL NAVIGATION
    Given what is true, what matters now?

LLM REASONING
    Given what matters, how should we reason about it?
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

This does not establish a universal context budget, final provider/model, or downstream recommendation value.

---

## Recommendation/action evidence through Specification 020

### Specification 015

The first three-condition recommendation/action-value experiment classified `FAIL`. The failed implementation was not promoted. A central discrepancy was `DEFER` versus `NOT_NOW`.

### Specification 016

A prospective construct-validity diagnostic established the bounded structural lesson:

```text
DEFER-like sequencing
    -> already justified/planned action
    + exact unresolved activating dependency
```

The diagnostic returned 36/36 exact dispositions, 18/18 exact DEFER pointers, and 18/18 NOT_NOW null pointers.

### Specification 017

The relation-backed recommendation/action comparison ended incomplete because model-authored `methodological_basis` duplicated system-known provenance. The durable instrumentation distinction became:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

### Specification 019

Specification 019 moved exact supplied-context provenance to deterministic system ownership and completed the full matched comparison:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           0.944444       0.916667        0.944444
semantic score           0.950000       0.950000        0.950000
blocking false positives 4              6               4
```

Frozen outcome:

```text
FAIL
```

The main discrepancy was repeated escalation of useful nonlinear model-family comparison into `BLOCKING_REQUIRED`, especially under SELECTIVE. Specification 019 remains immutable historical evidence and is not rescored.

### Specification 020

Specification 020 prospectively isolated `RECOMMENDED` versus `BLOCKING_REQUIRED` without methodological-context treatment. It completed 36/36 observations with every frozen hard gate passing:

```text
outcome   BLOCKING_BOUNDARY_SUPPORTED
```

Accepted bounded structural lesson:

```text
BLOCKING_REQUIRED-like work
    exact unresolved requirement
    + exact active defended downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action RESOLVES requirement
```

Specification 020 does not establish production recommendation enums, blocking policy, ranking, automatic execution, or SELECTIVE recommendation value.

Primary evidence:

```text
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
```

---

## System-owned provenance and relation boundary

The strongest current separation is:

```text
SYSTEM-OWNED IDENTITIES / PROVENANCE
    exact supplied stable_key@revision_id
    methodology payload digest and byte count
    treatment identity
    supplied action identities
    supplied requirement identities
    supplied downstream-scope identities
    supplied dependency / resolver / defer-trigger identities

MODEL-OWNED CONTENT
    dispositions
    pointers among supplied identities
    rationales
    summaries / warnings
```

The model should not be required to reproduce authoritative context provenance that the system already knows exactly, and it must not invent authoritative project relations inside a bounded experiment.

---

## Specification 021: provider-free implementation green

Specification 021 is the clean prospective recommendation-value test after the known sequencing, provenance, and blocking-calibration confounds were separately addressed.

It uses four newly authored cases:

```text
DBRA-01  future validity and model sequencing
DBRA-02  compact nonlinear model shortlist
DBRA-03  distribution evidence before transformation
DBRA-04  missingness / class-imbalance decision framework
```

and exactly three matched conditions:

```text
GENERIC
SELECTIVE
FULL_HORIZON
```

The experiment-owned action result carries action-local relation pointers:

```text
BLOCKING_REQUIRED
    exact blocking_requirement_id
    exact blocked_scope_id
    defer_until_id = null

RECOMMENDED
    all pointers null

DEFER
    blocking pointers null
    exact defer_until_id

NOT_NOW
    all pointers null
```

Frozen call plan:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
90 maximum provider attempts
randomization seed 2026082402
```

Frozen complete outcomes:

```text
PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
incomplete / integrity failed -> no advancement classification
```

`SAFE_BUT_NOT_DIFFERENTIATED` is intentionally legitimate. A strong generic reasoner may already know the small current methodological universe. The benchmark must not be rewritten simply to force SELECTIVE to win.

Checkpoint 175 records the exact provider-free implementation boundary:

```text
validated implementation head             8e199c29e3f082b353f92f27868aedca0ebbbf74
Specification 021 provider-free CI         32722934829  success
Ubuntu job                                 97418007046  success
Windows job                                97418007218  success
dedicated tests                            8 passed per OS
full V1 Python suite                       125 passed, 2 skipped per OS
accepted-seam regressions                  all green on the same exact head
```

The complete fake-runtime pipeline executes 36 reasoner outputs and 36 blinded judge outputs, preserves system-owned provenance, verifies authoritative-state isolation, and mechanically reaches `SAFE_BUT_NOT_DIFFERENTIATED` when all three fake conditions are deliberately oracle-perfect. That result is a machinery self-test only, not scientific evidence.

**No Specification 021 provider call is authorized.** The next legitimate boundary is a separate exact pre-live freeze after the reconciled Checkpoint 175 head is green.

---

## Preservation and continuity hardening

Checkpoint 173 closes the first machine-checkable routing-consistency hardening.

Promoted mechanism:

```text
docs/current_routing.json
    machine-readable routing metadata only

scripts/check_current_routing.py
    manifest contract + checkpoint existence + contradiction checks

.github/workflows/current-routing-consistency.yml
    cross-platform validation for routing-sensitive changes
```

Final closure evidence included push-triggered routing run `32719182489` on exact integration head `09670d5127c14cf3cece727b31823d5de4572211`, with both Ubuntu and Windows jobs successful.

Markdown remains the substantive source of project knowledge. The manifest is not another store for rationale, decisions, experiment interpretation, or historical evidence.

---

## Exact continuation

```text
1. validate the exact Checkpoint 175 reconciliation head provider-free and cross-platform
2. only after that exact head is green, freeze a separate Specification 021 pre-live boundary
3. add the minimal live runner/target workflow only after that pre-live freeze
4. validate the live-capable exact source provider-free before authorization
5. freeze exact source SHA, successful CI evidence, target workflow, confirmation token, and Specification 018 authorization evidence
6. authorize at most one exact governed live run through main
7. preserve raw provider evidence before scientific interpretation
8. do not modify or rescore Specifications 015-020
```

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures and incomplete runs as evidence, and promote only what earns its complexity.
