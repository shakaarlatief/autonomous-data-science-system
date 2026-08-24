# Current State

**Checkpoint:** 171  
**Date:** 2026-08-24  
**Active development branch:** `v1-blocking-calibration-diagnostic`  
**Active PR:** #44 draft, Specification 020 diagnostic with preserved supported result  
**Promoted V1 integration branch:** `v1-frontend-spike` at `b9c9c3a38935983075a9ca88632177980bb20ede`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, and governed autonomous live-experiment launch seams. Specification 020 completed its governed frozen diagnostic with `BLOCKING_BOUNDARY_SUPPORTED`.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** retire Specification 020 one-shot control-plane exposure, validate and promote the cleaned PR #44 branch only if green, then implement the small machine-checkable routing-consistency guard before freezing another recommendation-value experiment.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` intentionally hosts the narrow governed live-launch control plane plus temporary one-shot experiment exposure only when explicitly authorized. Temporary Specification 020 exposure is now due for retirement.

---

## Durable architecture and accepted evidence

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

Accepted technical/runtime boundaries remain D-028 through D-032. Specification 008 remains the promoted Project Cockpit interaction architecture. Specifications 012-014 remain the bounded accepted Horizon/selective-context/real-reasoning chain. Specification 018 remains the accepted governed live-experiment launcher.

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
    -> governed live-experiment launcher 018                 [SUPPORTED, PROMOTED]
    -> system-owned-provenance recommendation experiment 019 [FAIL, PRESERVED]
    -> recommendation/blocking calibration diagnostic 020   [SUPPORTED, PRESERVED]
```

Specification 014 showed equal frozen reasoning quality for SELECTIVE and FULL_HORIZON while SELECTIVE used 66.56% fewer provider input tokens.

Specification 016 supported the bounded construct that DEFER-like sequencing needs a concrete represented activating dependency if deterministic separation from NOT_NOW is expected.

Specification 019 completed the matched recommendation-value rerun after system-owned provenance repaired the instrumentation defect, but the frozen result remained `FAIL`.

Specification 020 prospectively isolated the recommendation/blocking construct and completed successfully.

---

## Specification 020 complete result

Frozen live source:

```text
82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
```

Governed live execution:

```text
launch issue          45
launcher run          32701990350
live run              32701999678
live job              97355284139
artifact               9510887324
artifact SHA-256       35ed6b472eac22090e563bbafee30aab1b666c00453ebcfd8cd0a832b79be678
reasoner outputs       36 / 36
provider attempts      36 / 45
failed attempts        0
retries                0
execution integrity    true
```

Frozen gate result:

```text
BC-G01 structured validity                    PASS
BC-G02 aggregate exact accuracy               1.000000  PASS
BC-G03 every variant majority-correct         12 / 12 at 3 / 3  PASS
BC-G04 every pair both sides majority-correct 6 / 6, both sides 3 / 3  PASS
BC-G05 exact joint blocking pointers          1.000000  PASS
BC-G06 RECOMMENDED null pointers              1.000000  PASS

outcome                                      BLOCKING_BOUNDARY_SUPPORTED
```

Supported conclusion:

```text
exact unresolved requirement
    + exact active defended downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action resolves requirement

can make BLOCKING_REQUIRED operationally separable from RECOMMENDED
for the frozen deliberately unambiguous microstates with the fixed reasoner.
```

This does not promote production `BLOCKING_REQUIRED`/`RECOMMENDED` enums or establish selective methodological-context recommendation value.

Specification 019 remains immutable `FAIL` evidence and is not rescored.

Raw and interpreted evidence:

```text
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
```

---

## Preservation and continuity consequence

The stage-boundary verification found no substantive preservation failure. It did confirm recurring routing drift in mutable current-state/index documents relative to already durable checkpoint/result evidence.

This now justifies one small Level-2 hardening:

```text
machine-readable current routing pointers
    -> lightweight CI consistency validator
    -> Markdown remains substantive source of truth
```

Do not introduce a graph database, vector database, or machine-generated documentation system for preservation on this evidence.

---

## Current non-selections

Still deliberately open:

```text
final recommendation/action taxonomy and ranking policy
production REQUIRED/BLOCKING semantics
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
1. retire Specification 020 one-shot authorization and temporary main helpers
2. validate the cleaned PR #44 head on Specification 020 Ubuntu/Windows CI and accepted V1 regression seams
3. promote PR #44 into v1-frontend-spike only if green
4. implement the small routing-consistency manifest + CI validator as the next Level-2 hardening
5. only after that freeze a successor recommendation-value contract
6. do not modify or rescore Specifications 015-020
```

## Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```
