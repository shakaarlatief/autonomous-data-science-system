# Current State

**Checkpoint:** 76  
**Date:** 2026-08-18  
**Development stage:** Prototype V0 held-out execution active  
**Resolved treatment slots:** 8 / 30  
**Next frozen slot:** `h1-r03-b1-a01`

## What we are building

The Autonomous Data Science System aims to create the best defensible data-science process for the particular project, where the meaning of "best" depends on project goals, constraints, deliverables, and desired human involvement while methodological integrity remains non-negotiable.

The long-term system-level distinction is documented in:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

The LLM is treated as one reasoning component inside a wider system. Explicit system mechanisms must still earn their complexity empirically.

## Current experiment

Prototype V0 asks:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

Quick V0 overview:

```text
prototype_v0/README.md
```

Frozen held-out protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Detailed current held-out run ledger:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

No H1/H2 S1-S10 or SC1-SC2 semantic judging has begun.

## Current experiment counts

```text
resolved treatment slots: 8 / 30
behavior-evaluable retained attempts: 8
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

The two non-behavior-evaluable provider/interface attempts belong to the H1 R2 B0 slot. Its third attempt was behavior-evaluable and permanently resolved that slot.

The one administrative pre-provider interruption occurred before the genuine H1 R3 B0 attempt because a local terminal lacked `OPENAI_API_KEY`. No provider inference occurred and the genuine `a01` was preserved.

## Important current experimental consequence

P0 has exhausted the common 250,000-token envelope in two retained H1 runs:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria permit no more than one P0 budget-exhausted run. That specific criterion can therefore no longer be satisfied regardless of later outcomes.

This is an objective resource result, not a semantic or overall architectural verdict. The frozen experiment continues so reliability, semantic quality, repair precision, completion, false blocking, and comparative resource distributions can still be evaluated without selective stopping.

## Frozen experiment integrity

The following remain frozen during held-out execution:

```text
P0 treatment behavior
B0/B1 prompts
P0 knowledge components
H1/H2 benchmark bundles
run order
resource budgets
provider/model configuration
provider normalization and retry semantics
semantic rubric
blinded judge protocol
continuation/falsification criteria
held-out executor behavior
```

No preservation/documentation update in Checkpoints 74-76 changed treatment behavior.

## Knowledge-preservation architecture v0.3

Checkpoint 76 upgrades the way this project preserves its own knowledge after actual use exposed that historically safe knowledge can still become conceptually buried.

Current preservation architecture:

```text
discussion
    -> checkpoint
    -> promotion audit
    -> canonical/foundational/specification update when warranted
    -> KNOWLEDGE_MAP routing update when warranted
    -> concise CURRENT_STATE

meaningful stage boundary
    -> knowledge reconciliation
```

Key files:

```text
docs/KNOWLEDGE_MAP.md
    Routing layer showing where important knowledge lives.

docs/DEVELOPMENT_METHOD.md
    Current method, now version 0.3.

docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
    Detailed rationale and deferred future tooling.

docs/MAJOR_CHANGES.md
    Selective history of major structural changes.

docs/experiments/prototype_v0/HELD_OUT_STATUS.md
    Detailed current V0 experiment ledger.
```

The current storage substrate remains Git + Markdown. Graph databases, vector retrieval, automatic summarization, generated dependency graphs, and similar infrastructure are explicitly preserved as future options but deferred until demonstrated need justifies the complexity.

Detailed change record:

```text
docs/checkpoints/076_knowledge_preservation_architecture_v0_3.md
```

## Current documentation roles

```text
README.md
    project-level entry point

docs/CURRENT_STATE.md
    concise present state and next step

docs/KNOWLEDGE_MAP.md
    routing to current and foundational knowledge

docs/VISION.md
    current system vision

docs/PRINCIPLES.md
    current principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    reconciled unresolved questions

docs/foundations/
    detailed durable reasoning and specifications

docs/checkpoints/
    historical provenance

docs/experiments/
    detailed current experiment ledgers

docs/MAJOR_CHANGES.md
    selective structural history
```

## Next authorized action

According to the frozen preregistered order:

```text
variant: H1
replicate: 3
condition: B1
slot: h1-r03-b1
attempt: h1-r03-b1-a01
```

After pulling Checkpoint 76, exactly one next invocation is authorized:

```bash
python -m ads_v0.heldout_runner run-next
```

Stop immediately after the executor result. Do not begin H1 R4 before the H1 R3 B1 terminal result is classified and mechanically inspected.

## Minimum reading for a future session

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

For system-level architectural context also read:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

For preservation-method context read:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

## Current priority

**Resume the unchanged frozen held-out experiment with exactly one `h1-r03-b1-a01` attempt, then stop for inspection.**
