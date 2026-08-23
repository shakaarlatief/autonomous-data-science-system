# Current State

**Checkpoint:** 155  
**Date:** 2026-08-23  
**Active development branch:** `v1-disposition-semantics-diagnostic`  
**Active PR:** #15 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at failure-preservation merge `10aa3f59bedc5ee45a38f0ae05c68da901d9adff`  
**Development stage:** Prototype V0 complete; bounded V1 has an accepted real-model selective-context seam, an immutable failed first recommendation/action-value experiment, and a completed live disposition-semantics diagnostic whose frozen outcome is `DISPOSITION_BOUNDARY_SUPPORTED`.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** finish the Specification 016 result promotion/reconciliation, validate the exact reconciled PR #15 head, merge exactly that green head into `v1-frontend-spike`, then preregister a new recommendation/action-value experiment using explicit dependency-backed sequencing before any further live model call.

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
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> real reasoning evidence                         [accepted bounded seam]
    -> recommendation / REQUIRED-BLOCKING / action    [first live seam failed]
    -> disposition-semantics diagnosis                [completed and supported]
    -> revised recommendation/action value            [next, not yet frozen]
```

### Accepted implementation boundaries

```text
D-028  SQLite-centered local-first architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Specification 008 / Checkpoints 126,130
    promoted Project Cockpit interaction architecture

Specification 012 v1.0 / Checkpoint 141
    explained MethodologicalHorizon

Specification 013 v1.0 / Checkpoint 143
    selective exact-revision MethodologicalContextPack

Specification 014 v1.0 / Checkpoint 146
    first real-model selective-context value gate passed
```

No final provider/model, multi-agent architecture, production semantic retrieval stack, final Horizon/context budget, production recommendation taxonomy, or automatic project mutation/execution policy is selected.

---

## Accepted real reasoning-context evidence

Specification 014 observed:

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

This accepts the bounded selective-context + ADS-owned `ReasoningRuntime` seam, not a universal context budget or final model choice.

Primary evidence:

```text
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
```

---

## Immutable Specification 015 negative evidence

Specification 015 tested GENERIC, SELECTIVE, and FULL_HORIZON recommendation/action behavior under a preregistered four-disposition taxonomy:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

Live run `32642733784` completed all planned calls with no retries, but the frozen result was:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0
outcome            FAIL
```

Fourteen of fifteen named gates passed. The sole failed gate was `RA-G05`, localized to `RA-02 MODEL_CHOICE`:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
required floor 0.800000
```

The repeated mismatch was `DEFER` expected versus `NOT_NOW` observed for two noncritical expansion actions. All nine RA-02 semantic judge outputs scored `1.000000`.

The frozen FAIL is not repaired or rescored.

Negative evidence was isolated from the rejected implementation through PR #14 and merged into `v1-frontend-spike` at:

```text
10aa3f59bedc5ee45a38f0ae05c68da901d9adff
```

PR #13 was closed without merge.

Primary evidence:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Completed Specification 016 diagnostic

Specification 016 isolated the exact `DEFER` versus `NOT_NOW` construct-validity question without methodological-context treatment comparison, semantic judge, tools, or project mutation.

Frozen operational distinction:

```text
DEFER
    action already justified in represented plan
    + exact unresolved supplied activating trigger
    + action becomes current next work after trigger
    + defer_until_id = exact trigger ID

NOT_NOW
    current objective/state does not materially justify prioritizing action
    + no represented supplied trigger activates it as current next work
    + defer_until_id = null
```

The live workflow ran from exact frozen source head:

```text
7db27fd35151c10cdb3562cdf4410fb8f4b09e8b
```

Workflow/run provenance:

```text
V1 disposition semantics live
run 32652636943
artifact 9496624273
```

Observed execution:

```text
reasoner outputs        36 / 36
validated observations 36 / 36
provider attempts       36 / 45
failed attempts         0
retries                 0
```

Frozen gate result:

```text
aggregate exact disposition accuracy    1.000000
all 12 variants                          3 / 3 correct
all 6 pair sides                         3 / 3 correct
expected-DEFER exact pointer accuracy    1.000000
expected-NOT_NOW null-pointer accuracy   1.000000

outcome                                  DISPOSITION_BOUNDARY_SUPPORTED
```

The complete downloaded artifact was preserved before next-experiment design at:

```text
experiments/disposition_semantics/results/spec016-live-20260823-run-32652636943/
```

Stable result:

```text
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
```

### Supported failure attribution

The result makes two Specification 015 explanations less likely on explicit unambiguous cases:

```text
A. DEFER / NOT_NOW are inherently operationally inseparable
C. the fixed reasoner cannot apply an explicit distinction reliably
```

The historical discrepancy remains consistent with:

```text
B. the original RA-02 state did not encode a uniquely activating DEFER relation strongly enough
```

The provider-free audit reports both disputed historical expected-DEFER examples as not admissible examples of unambiguous Specification 016 DEFER. This does not change their historical Specification 015 labels or FAIL result.

The remaining downstream question is still:

```text
D. does explicit SELECTIVE methodological knowledge add recommendation/action value beyond a strong GENERIC reasoner once sequencing semantics are made measurable?
```

---

## Current semantic design constraint earned by Specification 016

For future recommendation/action experiments:

```text
DEFER-like sequencing
    must not be a bare low-priority label
    must carry a concrete represented activating dependency/trigger

NOT_NOW-like state
    means no current material justification
    and no represented activating dependency that makes the action next work
```

This is a result-backed design/evaluation constraint for the next experiment. It is not yet a production enum or persistence contract.

---

## Current non-selections

Still deliberately open:

```text
whether DEFER and NOT_NOW should both exist as production enums
how explicit sequencing dependencies should become Foundation 018 production relations
whether explicit methodological knowledge adds recommendation value beyond a strong generic reasoner
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
final recommendation ranking/priority model
complete Foundation 018 production schema
mapping future accepted recommendations to authoritative project events
automatic execution and human approval/escalation
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist recommendation architecture
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

Do not modify or rescore Specification 015. Do not treat Specification 016's deliberately unambiguous benchmark as proof that real project states will always make sequencing explicit.

---

## Exact continuation

```text
1. finish current result/routing reconciliation for Checkpoint 155
2. update PR #15 with the measured live result and bounded interpretation
3. validate the exact reconciled PR #15 head through all relevant provider-free workflows
4. merge exactly that green PR #15 head into v1-frontend-spike
5. branch from the promoted merge boundary
6. design and preregister the next recommendation/action-value experiment
7. require explicit dependency-backed sequencing for any DEFER-like frozen truth
8. test SELECTIVE value versus GENERIC again only under the new separately frozen contract
9. make no new live model call before that contract and implementation are provider-free validated
```
