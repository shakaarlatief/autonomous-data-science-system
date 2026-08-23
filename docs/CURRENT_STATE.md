# Current State

**Checkpoint:** 159  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-value-relation-backed`  
**Active PR:** #16 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 016 promotion merge `6bda0c1efcf078476859b2c2c64fb0586964899d`  
**Development stage:** Prototype V0 complete; bounded V1 has an accepted selective real-reasoning seam, preserved negative recommendation evidence from Specification 015, supported dependency-backed disposition semantics from Specification 016, and an incomplete first live execution of Specification 017 whose raw evidence is preserved but whose recommendation/action seam is not promoted.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** close Specification 017 through preservation-only integration, reject its experimental implementation as production code, then design a governed autonomous live-experiment launcher and separately preregister the next recommendation/action-value experiment with system-owned provenance.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` intentionally trails active V1 work except narrowly scoped control-plane workflow exposure.

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

Current evidence chain:

```text
large reusable knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> real reasoning evidence                         [accepted bounded seam]
    -> first recommendation/action-value experiment   [FAIL, preserved]
    -> dependency-backed disposition diagnostic       [SUPPORTED, promoted bounded constraint]
    -> relation-backed recommendation experiment      [INCOMPLETE, preserved, not promoted]
```

Accepted technical/runtime boundaries remain D-028 through D-032. Specification 008 remains the promoted Project Cockpit interaction architecture. Specifications 012-014 remain the accepted bounded Horizon/selective-context/real-reasoning seams.

No final provider/model, multi-agent architecture, production semantic retrieval stack, final context budget, production recommendation taxonomy, dependency persistence schema, or automatic project mutation/execution policy is selected.

---

## Accepted real reasoning-context evidence

Specification 014 / Checkpoint 146:

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

Bounded conclusion: selective exact-revision context can preserve measured reasoning quality while materially reducing provider input for the frozen tasks.

---

## Immutable Specification 015 negative evidence

Specification 015 returned frozen outcome:

```text
FAIL
```

Only `RA-G05` failed, localized to the old RA-02 `DEFER` versus `NOT_NOW` truth. Its implementation was not promoted. The experiment remains immutable negative evidence.

Primary sources:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Promoted Specification 016 construct evidence

Specification 016 isolated dependency-backed sequencing and observed:

```text
run                                   32652636943
reasoner outputs                      36 / 36
aggregate exact disposition accuracy  1.000000
DEFER trigger-pointer accuracy        1.000000
NOT_NOW null-pointer correctness      1.000000
outcome                               DISPOSITION_BOUNDARY_SUPPORTED
```

Promoted bounded constraint:

```text
DEFER-like sequencing
    must carry a concrete represented activating dependency/trigger
    if deterministic separation from NOT_NOW is expected.
```

This does not make `DEFER` or `NOT_NOW` final production enums.

---

## Specification 017 live result: incomplete, no advancement classification

Specification 017 retained the GENERIC / SELECTIVE / FULL_HORIZON comparison, prospectively rebuilt all expected-DEFER truth under the stronger Specification 016 relation-backed construction, and froze a 36-reasoner + 36-judge live plan.

First live execution:

```text
run                         32656446705
job                         97235820936
frozen source head          bf041f4b4a485382d0e6e5c508ad916199601ee8
planned reasoner outputs    36
successful reasoner         29
planned judge outputs       36
successful judge            29
scored observations         29
provider attempts           77 / 90
complete scored design      false
execution integrity         true
gate evaluation             none
advancement outcome         none
```

Condition completion:

```text
SELECTIVE       12 / 12
FULL_HORIZON    12 / 12
GENERIC          5 / 12
```

All 19 failed reasoner attempts occurred in GENERIC and were mechanically classified `INVALID_STRUCTURED_RESPONSE`. The model repeatedly put the requested reasoning-function label into `methodological_basis`:

```text
VALIDITY_CONSTRAINT
MODEL_OPTION
EVIDENCE_OPTION
DECISION_FRAMEWORK
```

but GENERIC supplied zero reusable knowledge revisions, so the frozen contract required an empty methodological basis.

Observed boundary:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

The system already owns exact supplied-context provenance. Requiring a second model-authored provenance representation created an avoidable structured-output incompatibility.

### Historical interpretation

Specification 017 is **not** classified as any of:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Those outcomes require the complete scored design. Partial condition scores are not advancement evidence and must not be used to tune benchmark truth or thresholds.

Do not silently sanitize GENERIC output, reinterpret reasoning-function labels as knowledge keys, change the frozen fixture, or rerun the unchanged full workflow merely hoping for stochastic schema conformance.

### Raw evidence

```text
experiments/relation_backed_recommendation_action_value/
    V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md

experiments/relation_backed_recommendation_action_value/results/
    spec017-live-20260823-run-32656446705/

docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
```

---

## Next recommendation/action design constraint

The next experiment must separate:

```text
SYSTEM-OWNED PROVENANCE
    exact supplied stable_key@revision_id
    context digest
    treatment/context identity

MODEL-OWNED RECOMMENDATION CONTENT
    action dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales
```

Any model-authored knowledge citation layer must justify its value separately and be constrained to an explicit supplied-ID menu. GENERIC reusable-knowledge provenance is deterministically empty system-side.

No new recommendation/action live call is authorized until a new contract incorporating that boundary is preregistered and its exact provider-free implementation head is green.

---

## Autonomous live-experiment control-plane observation

During post-result preservation, a default-branch GitHub Actions workflow triggered by a GitHub issue created through the connected GitHub interface successfully:

```text
received an owner-created issue event
    -> started GitHub Actions without workflow_dispatch
    -> downloaded the exact prior run artifact
    -> verified all frozen SHA-256 digests
    -> committed the preserved evidence to the experiment branch
```

Successful preservation run:

```text
32658108544
```

This is not Specification 017 scientific evidence. It is control-plane feasibility evidence for the user's requested next capability: allowing ADS development to launch future explicitly authorized live experiments without a repeated manual GitHub button click.

A general launcher is not yet accepted. It must be designed with an allowlisted experiment registry, owner/actor checks, exact frozen source SHA, exact contract/confirmation identity, CI-gate verification, no arbitrary command execution from issue text, and auditable run linking.

---

## Current non-selections

Still deliberately open:

```text
whether DEFER and NOT_NOW should exist as production enums
complete Foundation 018 dependency persistence schema
whether explicit methodological knowledge adds recommendation/action value beyond a strong generic reasoner
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
final recommendation ranking/priority model
mapping accepted recommendations to authoritative project objects/events
automatic execution and human approval/escalation policy
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist recommendation architecture
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

---

## Exact continuation

```text
1. reconcile PR #16 to the incomplete Specification 017 result
2. create a preservation-only PR from v1-frontend-spike
3. carry frozen Specification 017 sources, raw result, stable result ledger, Checkpoints 156-159, and current routing
4. do not promote/copy the experimental recommendation/action implementation into the integration branch
5. validate and merge the preservation-only PR
6. close PR #16 without merge
7. remove temporary one-shot preservation workflows and close their control issues
8. design and provider-free validate a governed autonomous live-experiment launcher
9. separately preregister the next recommendation/action-value experiment with system-owned provenance
10. make no new recommendation/action live provider call before that new experiment contract and exact implementation head are frozen and green
```
