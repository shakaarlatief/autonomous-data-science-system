# Current State

**Checkpoint:** 158  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-value-relation-backed`  
**Active PR:** #16 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 016 promotion merge `6bda0c1efcf078476859b2c2c64fb0586964899d`  
**Development stage:** Prototype V0 complete; bounded V1 has an accepted real-model selective-context seam, an immutable failed first recommendation/action-value experiment, a supported dependency-backed disposition diagnostic, and a second relation-backed recommendation/action-value experiment whose provider-free implementation is cross-platform green and whose explicit live boundary is now frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the exact final Checkpoint 158 branch head under all relevant provider-free workflows; if that exact head is green, make no further experiment-branch commit, expose only the identical live workflow on `main`, then execute the unchanged Specification 017 live experiment once.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` intentionally trails active V1 work except explicit manual-workflow dispatcher exposure.

---

## Durable architecture already accepted

### Post-V0 scaling rule

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore P0's large always-on state/context/frontier, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

### Project semantics

Foundation 018 distinguishes:

```text
OBJECTS / RELATIONS / EVENTS / VIEWS
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
```

### Methodological navigation

Foundation 019:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Current executable path:

```text
large reusable knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> real reasoning evidence                         [accepted bounded seam]
    -> first recommendation/action-value experiment   [failed, preserved]
    -> relation-backed disposition diagnostic         [supported]
    -> second recommendation/action-value experiment  [provider-free green, pre-live]
```

Accepted technical/runtime boundaries remain D-028 through D-032. Specification 008 remains the promoted Project Cockpit interaction architecture. Specifications 012-014 remain the accepted bounded Horizon/selective-context/real-reasoning seams.

No final provider/model, multi-agent architecture, production semantic retrieval stack, final context budget, production recommendation taxonomy, dependency persistence schema, or automatic project mutation/execution policy is selected.

---

## Accepted real reasoning-context evidence

Specification 014 / Checkpoint 146 observed:

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

This supports the bounded selective-context + ADS-owned `ReasoningRuntime` seam. It does not establish recommendation/action value by itself.

---

## Immutable Specification 015 negative evidence

Specification 015 compared GENERIC, SELECTIVE, and FULL_HORIZON recommendation/action behavior and returned frozen outcome:

```text
FAIL
```

Only `RA-G05` failed, localized to `RA-02 MODEL_CHOICE`:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
required floor 0.800000
```

The repeated mismatch was expected `DEFER` versus observed `NOT_NOW` for two noncritical expansion actions. All nine RA-02 semantic judge outputs scored `1.000000`.

Specification 015 is not repaired or rescored. Its failed implementation remains unpromoted; its negative evidence is preserved.

Primary sources:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Promoted Specification 016 diagnostic result

Specification 016 isolated the `DEFER` versus `NOT_NOW` construct question with explicit activating dependency/trigger semantics.

Live result:

```text
run                                   32652636943
reasoner outputs                      36 / 36
provider attempts                     36 / 45
failed attempts                       0
retries                               0
aggregate exact disposition accuracy  1.000000
all 12 variants                       3 / 3 correct
all 6 pair sides                      3 / 3 correct
DEFER trigger-pointer accuracy        1.000000
NOT_NOW null-pointer correctness      1.000000
outcome                               DISPOSITION_BOUNDARY_SUPPORTED
```

Promoted merge:

```text
6bda0c1efcf078476859b2c2c64fb0586964899d
```

Supported bounded design/evaluation constraint:

```text
DEFER-like sequencing
    must carry a concrete represented activating dependency/trigger
    if deterministic distinction from NOT_NOW-like absence of current justification is expected.
```

This does not make `DEFER` or `NOT_NOW` final production enums.

Primary sources:

```text
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

---

## Active Specification 017 experiment

Research 024, Specification 017 v0.1, the frozen benchmark fixture, Checkpoint 156, provider-free gate Checkpoint 157, and pre-live Checkpoint 158 govern the active slice.

Frozen question:

> Given the same project microstate, explicit task profile, candidate action menu, relation-backed sequencing evidence, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control?

### Conditions

```text
GENERIC
    no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact task-specific revisions

FULL_HORIZON
    all ten exact current accepted Horizon revisions
```

### Frozen cases and selective sets

```text
RB-01  VALIDITY_GATE_AND_SEQUENCE
       prediction-moment + prediction-time-feature-eligibility + temporal-validation

RB-02  COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE
       random-forest + gradient-boosted-trees

RB-03  DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION
       histogram + ecdf

RB-04  MISSINGNESS_IMBALANCE_DECISION_SEQUENCE
       class-imbalance + missing-data
```

### Relation-backed output contract

Every action decision contains:

```text
action_id
disposition
defer_until_id
rationale
```

Frozen pointer invariant:

```text
DEFER
    exact supplied unresolved activating trigger required

BLOCKING_REQUIRED / RECOMMENDED / NOT_NOW
    defer_until_id = null
```

The benchmark does not copy Specification 015's ambiguous expected-DEFER examples into the new truth set.

### Frozen advancement outcomes

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
    all absolute/relative/expansion gates pass
    + at least one preregistered positive value signal

SAFE_BUT_NOT_DIFFERENTIATED
    all absolute/relative/expansion gates pass
    + zero positive value signals

FAIL
    any frozen absolute/relative/expansion gate fails
```

A strong GENERIC ceiling result is therefore allowed to close as safe but not differentiated.

### Provider-free implementation gate

Checkpoint 157 preserves exact implementation head:

```text
07da2a091b5686b0378c7f8114495fe1d0b29c32
```

Dedicated workflow `32655457836` passed on both operating systems:

```text
Ubuntu targeted       13 passed
Windows targeted      13 passed
Ubuntu full suite     71 passed, 2 skipped
Windows full suite    71 passed, 2 skipped
```

Inherited reasoning-context, disposition-semantics, and checkpoint-metadata workflows also passed on the same exact head.

The provider-free full fake execution proves the complete 36-reasoner + 36-judge shape, deterministic plans/gates, relation-backed pointer validation, blinded judge contract, attempt accounting, and authoritative-state isolation. A perfect three-condition ceiling correctly evaluates to `SAFE_BUT_NOT_DIFFERENTIATED` rather than promotion.

### Explicit live boundary

Checkpoint 158 freezes:

```text
.github/workflows/v1-relation-backed-recommendation-action-value-live.yml
manual confirmation: RUN_SPEC_017_FROZEN
required branch: v1-recommendation-action-value-relation-backed
```

The frozen live plan remains:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
90 maximum provider attempts
randomization seed 2026082303
```

No Specification 017 live provider call has occurred.

The live experiment is not authorized until the exact final branch head containing Checkpoints 157-158, the live workflow, and current routing reconciliation passes ordinary provider-free CI. After that green head, no further experiment-branch commit is permitted before the live run.

Primary active sources:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
docs/checkpoints/157_relation_backed_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/158_specification_017_live_boundary_frozen.md
```

---

## Current non-selections

Still deliberately open:

```text
whether DEFER and NOT_NOW should exist as production enums
how activating dependencies should be persisted in the complete Foundation 018 schema
whether explicit methodological knowledge adds recommendation/action value beyond a strong generic reasoner
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
final recommendation ranking/priority model
mapping future accepted recommendations to authoritative project state/events
automatic execution and human approval/escalation
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist recommendation architecture
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

Do not modify or rescore Specifications 015 or 016. Do not change Specification 017's fixture, thresholds, value signals, randomization, call plan, retry policy, or concrete treatment in response to future live outputs.

---

## Exact continuation

```text
1. validate the exact final Checkpoint 158 PR #16 head under:
       V1 relation-backed recommendation action value
       V1 reasoning context value
       V1 disposition semantics diagnostic
       Checkpoint metadata
2. if and only if that exact head is green, make no further experiment-branch commits
3. copy only the identical Specification 017 live workflow to main for workflow_dispatch visibility
4. manually dispatch V1 relation-backed recommendation action value live
5. select branch v1-recommendation-action-value-relation-backed
6. enter RUN_SPEC_017_FROZEN
7. preserve the complete live artifact before interpretation or design changes
```
