# Current State

**Checkpoint:** 154  
**Date:** 2026-08-23  
**Active development branch:** `v1-disposition-semantics-diagnostic`  
**Active PR:** #15 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at failure-preservation merge `10aa3f59bedc5ee45a38f0ae05c68da901d9adff`  
**Development stage:** Prototype V0 complete; bounded V1 has an accepted real-model selective-context seam, an immutable failed first recommendation/action-value experiment, and a separately preregistered disposition-semantics diagnostic whose provider-free implementation is now cross-platform green and whose secret-gated live boundary is frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the final Checkpoint 154 live-ready branch head under ordinary provider-free CI, expose only the identical manual workflow dispatcher on `main`, then execute the unchanged Specification 016 live diagnostic once. No live Specification 016 call has occurred yet.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` intentionally trails active V1 work except for explicit manual-workflow dispatcher exposure.

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
    -> disposition-semantics diagnosis                [provider-free green; live next]
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

Live run:

```text
workflow              V1 recommendation action value live
run                   32642733784
frozen source head    d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
reasoner outputs      36 / 36
blinded judge outputs 36 / 36
provider attempts     72
retries               0
```

Frozen result:

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
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Active Specification 016 diagnostic

Research 023, Specification 016 v0.1, `disposition_semantics_v1.json`, and Checkpoint 152 froze the diagnostic before implementation and live calls.

The diagnostic intentionally removes the methodological-treatment comparison and asks a narrower construct-validity question.

### Experimental operational distinction

```text
DEFER
    action already justified in represented plan
    + exact unresolved supplied trigger
    + action becomes current next work after that trigger
    + defer_until_id = exact trigger ID

NOT_NOW
    current objective/state does not materially justify prioritizing action
    + no represented supplied trigger activates it as current next work
    + defer_until_id = null
```

This is not yet a production taxonomy.

### Frozen benchmark

```text
6 contrastive pairs
2 variants per pair
3 repetitions per variant
12 variants
36 planned successful reasoner calls
45 maximum provider attempts
randomization seed 2026082302
```

Domains:

```text
DS-01 model tuning
DS-02 subgroup error analysis
DS-03 feature-interaction engineering
DS-04 missingness sensitivity
DS-05 probability calibration
DS-06 distribution evidence
```

One reasoner condition only:

```text
no reusable methodological assets
no retrieval / Horizon / selective context
no GENERIC / SELECTIVE / FULL comparison
no semantic judge
no tools
no previous response state
```

### Frozen hard gates

```text
DS-G01  zero unresolved invalid successful outputs
DS-G02  aggregate exact disposition accuracy >= 0.95
DS-G03  every variant correct >= 2 / 3 repetitions
DS-G04  every pair has both sides correct >= 2 / 3 repetitions
DS-G05  expected-DEFER exact trigger-pointer accuracy == 1.00
DS-G06  expected-NOT_NOW null-pointer correctness == 1.00
```

Frozen outcomes:

```text
DISPOSITION_BOUNDARY_SUPPORTED
DISPOSITION_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

---

## Provider-free implementation gate passed

Checkpoint 153 preserves the implementation head:

```text
6e7af25fd96d79673a59845e1c608c752970f658
```

Dedicated workflow:

```text
V1 disposition semantics diagnostic
run 32646969810
```

Results:

```text
Ubuntu targeted       15 passed
Windows targeted      15 passed
Ubuntu full suite     62 passed, 2 skipped
Windows full suite    62 passed, 2 skipped
```

Inherited regressions on the same head also passed:

```text
Checkpoint metadata          run 32646969848 PASS
V1 reasoning context value   run 32646969808 PASS
```

Provider-free validation covers:

```text
fixture construct rules
36-call deterministic randomized plan
truth-blinded model input
exact pointer invariants
attempt/retry ledger
full fake-runtime execution
SUPPORTED / NOT_SUPPORTED / INCOMPLETE gate behavior
provider-neutral structured-output forwarding
application/domain isolation from provider SDK imports
```

The historical RA-02 expected-DEFER examples are diagnostically classified as not admissible under the stronger Specification 016 unambiguous-DEFER construction rule because they lack an explicit trigger-backed dependency. This is a new diagnostic fact, not a rescore of Specification 015.

---

## Specification 016 live boundary frozen

Checkpoint 154 adds the explicit secret-gated workflow:

```text
.github/workflows/v1-disposition-semantics-live.yml
```

Manual confirmation:

```text
RUN_SPEC_016_FROZEN
```

The workflow:

```text
runs only from v1-disposition-semantics-diagnostic
requires OPENAI_API_KEY
reruns the frozen provider-free targeted suite first
installs openai-agents==0.19.4 only for live execution
runs experiments.disposition_semantics.runner
uploads the complete result directory even after partial failure
```

No Specification 016 live provider call has occurred.

The final branch head containing Checkpoints 153-154 and reconciled routing must now pass ordinary provider-free CI. After that exact head is green, the experiment branch must not change before the live run.

The identical live-workflow file may then be copied to `main` only to expose GitHub's manual dispatcher. The run itself must explicitly select `v1-disposition-semantics-diagnostic`.

---

## Current non-selections

Still deliberately open:

```text
whether DEFER and NOT_NOW should both exist in production
whether sequencing should instead be an explicit dependency relation
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

Do not modify Specification 015 in place. Do not change Specification 016 after observing live results.

---

## Exact continuation

```text
1. finish current routing reconciliation around Checkpoint 154
2. validate the exact resulting PR #15 head with:
       V1 disposition semantics diagnostic
       V1 reasoning context value
       Checkpoint metadata
3. if and only if that exact head is green, make no further branch commits
4. expose the identical v1-disposition-semantics-live.yml dispatcher on main only
5. manually dispatch V1 disposition semantics live
6. select branch v1-disposition-semantics-diagnostic
7. enter RUN_SPEC_016_FROZEN
8. preserve the complete artifact before interpretation or design changes
```

Primary active sources:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
tests/fixtures/reasoning/disposition_semantics_v1.json
docs/checkpoints/152_disposition_semantics_failure_attribution_contract_frozen.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
experiments/disposition_semantics/harness.py
experiments/disposition_semantics/runner.py
```
