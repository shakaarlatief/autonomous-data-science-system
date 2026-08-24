# Current State

**Checkpoint:** 166  
**Date:** 2026-08-24  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none; preservation-only PR #43 merged and failed Specification 019 implementation PR #33 closed without merge  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 019 preservation merge `e88c41b31788a53c7da115a24b0f9baeea48516b`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, Horizon/selective-context, real-reasoning, dependency-backed sequencing, and governed autonomous live-experiment launch seams. Specification 019 completed the first matched system-owned-provenance recommendation/action rerun and classified `FAIL`; its frozen authority and negative evidence are integrated without the failed implementation.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** prospectively design the next recommendation/blocking-calibration experiment. No new recommendation/action provider call is authorized.

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
```

Specification 014 showed equal frozen reasoning quality for SELECTIVE and FULL_HORIZON while SELECTIVE used 66.56% fewer provider input tokens.

Specification 016 supported the bounded construct that DEFER-like sequencing needs a concrete represented activating dependency if deterministic separation from NOT_NOW is expected.

Specification 017 did not complete its matched live design because model-authored methodological provenance was not a valid proxy for the task/reasoning-function label.

Specification 019 prospectively repaired that instrumentation boundary by making exact supplied context provenance system-owned. The complete matched live design then produced a genuine scientific `FAIL`, not an incomplete execution.

---

## Specification 019 complete live result

Frozen source:

```text
6b5e6237b738250458550f95c9f3a6b0d51e86ec
```

Provider-free validation:

```text
run 32664369953
Ubuntu dedicated     13 passed
Windows dedicated    13 passed
Ubuntu full V1       116 passed, 2 skipped
Windows full V1      116 passed, 2 skipped
provider credential  absent
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

Failed gates:

```text
SPRA-G06  SELECTIVE every-case exact accuracy floor
SPRA-G08  SELECTIVE every-case semantic floor
SPRA-G09  SELECTIVE per-case exact non-inferiority vs GENERIC
SPRA-G10  SELECTIVE per-case exact non-inferiority vs FULL_HORIZON
SPRA-G20  SELECTIVE blocking false positives <= FULL_HORIZON
```

Frozen classifier:

```text
absolute gates           FAIL
relative gates           FAIL
expansion gates          FAIL
positive value signals   0
advancement outcome      FAIL
```

RB-02 is the central recommendation-calibration failure. SELECTIVE labeled both compact nonlinear model-comparison actions `BLOCKING_REQUIRED` in all three repetitions although the frozen truth was `RECOMMENDED`, while correctly keeping tuning `DEFER`red behind `model-family-selected`. GENERIC and FULL_HORIZON made the same over-blocking error in two of three repetitions but were correct once, so SELECTIVE crossed the frozen per-case non-inferiority margin and accumulated six blocking-scope false positives versus four for FULL_HORIZON.

RB-04 was deterministically perfect in every condition but semantically scored `0.800000` everywhere because the frozen training-only preprocessing/leakage-prevention obligation was omitted. That treatment-invariant ceiling does not implicate SELECTIVE specifically, but the preregistered absolute case floor still fails.

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

The 36-output reasoner design completed without provenance-induced schema failures and with zero retries. Exact supplied-context provenance should therefore remain a deterministic system trace rather than a mandatory duplicate model-authored field.

That instrumentation lesson does not promote the failed recommendation/action treatment.

---

## Integrated preservation boundary

Raw evidence is preserved at:

```text
experiments/system_owned_provenance_recommendation_action_value/results/
    spec019-live-20260824-run-32664534864/
```

Stable interpretation:

```text
experiments/system_owned_provenance_recommendation_action_value/
    V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Checkpoint 166 records the frozen failure and promotion audit.

Preservation-only PR #43 merged into `v1-frontend-spike` at:

```text
e88c41b31788a53c7da115a24b0f9baeea48516b
```

Its exact pre-merge head `2d5795246f710ab222bf9a29f6d4e3e3b39ba57e` passed Checkpoint metadata, Ubuntu/Windows governed-launcher CI with no provider credential, the accepted reasoning-context workflow, and the accepted disposition-semantics workflow.

Failed implementation PR #33 is closed without merge. The accepted integration branch therefore contains the frozen Specification 019 authority and evidence, but not its failed harness, runner, judge, implementation tests, or experiment workflows.

---

## Specification 018 accepted control-plane boundary

The accepted launcher remains a bounded capability:

```text
owner request transport
    -> repository authorization registry
    -> exact owner/source/CI/duplicate checks
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

The launcher receives no provider credential. Issue text cannot define executable workflow/ref/SHA/command/model/prompt/secret configuration.

Post-Specification-019 cleanup is complete on `main`:

```text
active live authorizations                 0
Specification 019 live workflow exposure   removed
Specification 019 observer helper          removed
Specification 019 result-preservation helper removed
Specification 019 preservation-copy helper removed
temporary issues 34-42                    closed; audit history retained
```

No active authorization exists for another recommendation/action provider run.

---

## Current non-selections

Still deliberately open:

```text
final recommendation/action taxonomy and ranking policy
production REQUIRED/BLOCKING semantics
how defended downstream scope should determine blocking status
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
1. begin a new prospective design boundary for recommendation/blocking calibration
2. define what exact represented relation makes work genuinely BLOCKING_REQUIRED for a defended downstream scope
3. preserve the accepted dependency-backed DEFER construction from Specification 016
4. preserve system-owned supplied-context provenance from Specification 019
5. retain strong GENERIC and FULL_HORIZON controls
6. do not tune truth, thresholds, or treatment from repeated Specification 019 outputs
7. freeze the successor research memo, specification, fixture, gates, call plan, and checkpoint before implementation
8. validate the exact implementation head provider-free on required platforms
9. authorize any future live run only through Specification 018 after that exact head is green
10. make no new recommendation/action provider call before steps 1-9 are satisfied
```