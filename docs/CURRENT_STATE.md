# Current State

**Checkpoint:** 167  
**Date:** 2026-08-24  
**Active development branch:** `v1-blocking-calibration-diagnostic`  
**Active PR:** #44 draft, Specification 020 diagnostic  
**Promoted V1 integration branch:** `v1-frontend-spike` at reconciled head `b9c9c3a38935983075a9ca88632177980bb20ede`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, Horizon/selective-context, real-reasoning, dependency-backed sequencing, and governed autonomous live-experiment launch seams. Specification 019 completed the first matched system-owned-provenance recommendation/action rerun and classified `FAIL`; its frozen authority and negative evidence are integrated without the failed implementation. Specification 020 is now prospectively frozen as a construct-validity diagnostic for `RECOMMENDED` versus dependency-backed `BLOCKING_REQUIRED`.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** implement Specification 020 provider-free, validate its exact implementation head cross-platform, and freeze a later live boundary only if those gates pass. No new provider call is authorized.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` intentionally trails V1 application development but hosts the narrow governed live-launch control plane required for explicitly authorized experiments.

---

## Durable architecture

Prototype V0 established the scaling rule:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Foundation 018 separates Objects, Relations, Events, and Views. Foundation 019 establishes:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Foundation 020 separates reusable methodological knowledge from project state, execution implementation, and presentation.

Accepted technical/runtime boundaries remain D-028 through D-032. Specification 008 remains the promoted Project Cockpit interaction architecture. Specifications 012-014 remain the bounded accepted Horizon/selective-context/real-reasoning chain.

---

## Current evidence chain

```text
reusable methodological knowledge
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> real reasoning evidence                              [SUPPORTED]
    -> recommendation/action experiment 015                 [FAIL, PRESERVED]
    -> dependency-backed disposition diagnostic 016         [SUPPORTED]
    -> relation-backed recommendation experiment 017        [INCOMPLETE, PRESERVED]
    -> governed live-experiment launcher 018                 [SUPPORTED]
    -> system-owned-provenance recommendation experiment 019 [FAIL, PRESERVED]
    -> recommendation/blocking calibration diagnostic 020   [CONTRACT FROZEN]
```

Specification 014 showed equal frozen reasoning quality for SELECTIVE and FULL_HORIZON while SELECTIVE used 66.56% fewer provider input tokens.

Specification 016 supported the bounded construct that DEFER-like sequencing needs a concrete represented activating dependency if deterministic separation from NOT_NOW is expected.

Specification 017 did not complete its matched live design because model-authored methodological provenance was not a valid proxy for the task/reasoning-function label.

Specification 019 prospectively repaired that instrumentation boundary by making exact supplied-context provenance system-owned. The complete matched live design then produced a genuine scientific `FAIL`, not an incomplete execution.

Specification 020 now isolates the remaining calibration question before another recommendation-value comparison.

---

## Specification 019 complete live result

Frozen source:

```text
6b5e6237b738250458550f95c9f3a6b0d51e86ec
```

Governed live execution:

```text
launch issue          35
launcher run          32664527166
live run              32664534864
live job              97255789247
artifact               9499756280
reasoner outputs       36 / 36
judge outputs          36 / 36
provider attempts      72 / 90
retries                0
execution integrity    true
```

Aggregate frozen quality:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           0.944444       0.916667        0.944444
semantic score           0.950000       0.950000        0.950000
blocking false positives 4              6               4
```

Frozen classifier:

```text
absolute gates           FAIL
relative gates           FAIL
expansion gates          FAIL
positive value signals   0
advancement outcome      FAIL
```

RB-02 is the central recommendation-calibration failure. SELECTIVE labeled both compact nonlinear model-comparison actions `BLOCKING_REQUIRED` in all three repetitions although the frozen truth was `RECOMMENDED`, while correctly keeping tuning `DEFER`red behind `model-family-selected`. GENERIC and FULL_HORIZON made the same over-blocking error in two of three repetitions but were correct once.

RB-04 was deterministically perfect in every condition but semantically scored `0.800000` everywhere because the frozen training-only preprocessing/leakage-prevention obligation was omitted. The frozen contract did not permit a post-hoc exemption.

Specification 019 remains permanently `FAIL` under its own frozen gates.

---

## Durable positive lesson from Specification 019

The provenance instrumentation repair worked:

```text
SYSTEM-OWNED PROVENANCE
    exact supplied stable_key@revision_id
    methodology payload digest
    methodology byte count
    treatment identity

MODEL-OWNED CONTENT
    dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales
```

The full reasoner design completed without provenance-induced schema failures and with zero retries. Exact supplied-context provenance should therefore remain a deterministic system trace rather than a mandatory duplicate model-authored field.

That instrumentation lesson does not promote the failed recommendation/action treatment.

---

## Integrated preservation and control-plane boundary

Specification 019 evidence is preserved at:

```text
experiments/system_owned_provenance_recommendation_action_value/results/
    spec019-live-20260824-run-32664534864/
```

Stable interpretation:

```text
experiments/system_owned_provenance_recommendation_action_value/
    V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Preservation-only PR #43 merged into `v1-frontend-spike` at:

```text
e88c41b31788a53c7da115a24b0f9baeea48516b
```

Failed implementation PR #33 is closed without merge.

Post-Specification-019 cleanup is complete on `main`:

```text
active live authorizations                    0
Specification 019 live workflow exposure      removed
Specification 019 observer helper             removed
Specification 019 result-preservation helper  removed
Specification 019 preservation-copy helper    removed
temporary issues 34-42                        closed; audit history retained
```

The accepted Specification 018 launcher remains available only for separately frozen, exact, provider-free validated experiments.

---

## Reconciled integration validation

After Specification 019 preservation and canonical reconciliation, the exact integration boundary:

```text
b9c9c3a38935983075a9ca88632177980bb20ede
```

passed:

```text
Checkpoint metadata       run 32695017695   success
V1 frontend spike         run 32695017696   success
Ubuntu build/unit                              success
Windows build/unit                             success
Chromium browser/accessibility/visual gate     success
```

Specification 020 branch `v1-blocking-calibration-diagnostic` was created exactly from that head.

---

## Specification 020 frozen diagnostic

Authoritative sources:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
tests/fixtures/reasoning/blocking_calibration_v1.json
docs/checkpoints/167_recommended_vs_blocking_required_calibration_contract_frozen.md
```

The diagnostic distinction is:

```text
BLOCKING_REQUIRED
    candidate action is currently justified
    + exact unresolved supplied requirement
    + exact active defended supplied downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action is represented as the resolver of that requirement
    + exact requirement and scope pointers

RECOMMENDED
    action is materially worthwhile now or soon
    + no exact active supplied downstream scope is represented as blocked on it
    + both blocking pointers null
```

High importance, urgency, common best practice, and generic sequencing language are explicitly insufficient for `BLOCKING_REQUIRED`.

The frozen benchmark contains six contrastive pairs:

```text
BC-01  prediction-time feature availability
BC-02  temporal validation sensitivity
BC-03  missing-data treatment sensitivity
BC-04  subgroup error analysis
BC-05  probability calibration assessment
BC-06  nonlinear model-family comparison
```

Frozen live design if a later provider-free boundary earns authorization:

```text
6 pairs x 2 variants x 3 repetitions
36 planned successful reasoner calls
45 maximum provider attempts
seed 2026082401
one reasoner condition only
no reusable methodology
no semantic judge
no tools
no project mutation
```

Frozen structured output:

```text
BlockingCalibrationResult
    disposition: BLOCKING_REQUIRED | RECOMMENDED
    blocking_requirement_id: str | None
    blocked_scope_id: str | None
    rationale: str
```

Frozen hard gates:

```text
BC-G01  zero unresolved invalid successful outputs
BC-G02  aggregate exact disposition accuracy >= 0.95
BC-G03  every variant >= 2/3 correct
BC-G04  every pair both sides >= 2/3 correct
BC-G05  all 18 expected-BLOCKING_REQUIRED observations have exact
         disposition + requirement pointer + blocked-scope pointer
BC-G06  all 18 expected-RECOMMENDED observations have exact
         disposition + both pointers null
```

BC-G05 and BC-G06 intentionally make support effectively require exact correctness across all 36 deliberately unambiguous observations. This strictness is frozen before implementation.

Allowed outcomes:

```text
BLOCKING_BOUNDARY_SUPPORTED
BLOCKING_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

No provider call is authorized by Checkpoint 167.

---

## Current non-selections

Still deliberately open:

```text
final recommendation/action taxonomy and ranking policy
production REQUIRED/BLOCKING semantics
how defended downstream scope should determine blocking status in production
whether DEFER and NOT_NOW become production enums
complete dependency persistence schema
whether explicit methodological knowledge adds recommendation/action value beyond a strong generic reasoner
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
mapping accepted recommendations to authoritative project objects/events
automatic project execution and human approval/escalation policy
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist architecture
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

---

## Exact continuation

```text
1. implement Specification 020 provider-free only
2. add experiment-only BlockingCalibrationResult and strict supplied-ID validation
3. mechanically audit all six contrastive pairs and evaluator-truth blinding
4. build and hash the complete deterministic 36-call plan before any provider path exists
5. implement attempt-ledger, deterministic gate evaluation, and fake-runtime integration
6. add dedicated provider-free Ubuntu/Windows CI with OPENAI_API_KEY explicitly absent
7. run accepted V1 regression suites on the exact implementation head
8. freeze the exact green implementation/live boundary in a later checkpoint
9. only then expose or authorize a live workflow through Specification 018
10. preserve raw live evidence before any interpretation or tuning if a live run is eventually authorized
11. do not modify or rescore Specification 019
12. make no new provider call before steps 1-8 are complete
```