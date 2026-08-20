# Checkpoint 76: Knowledge Preservation Architecture v0.3

**Date:** 2026-08-18  
**Status:** Historical preservation-method record  
**Checkpoint class:** PRESERVATION_METHOD  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: Knowledge Preservation Architecture v0.3.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Type:** Major project-development / knowledge-preservation architecture update  
**Prototype V0 treatment impact:** None

## Purpose

The project paused before continuing held-out execution to ask whether its own knowledge-preservation method was still adequate as the repository grows.

The immediate trigger was the promotion of Checkpoint 22 into Foundation 013.

Checkpoint 22 had been safely committed to Git, so the knowledge was not physically lost. However, its durable system-level importance still depended on the user remembering that the historical checkpoint existed. This exposed a broader failure mode:

```text
knowledge can be durable
without being sufficiently discoverable,
authoritatively classified,
or promoted into the right current layer.
```

The project therefore treated this as a genuine Level-2 system-design lesson and upgraded the project-development method from version 0.2 to version 0.3.

## Diagnosis

The existing layered preservation method remains fundamentally sound:

```text
chat for exploratory reasoning
canonical documents for current knowledge
foundations for detailed durable reasoning
checkpoints for historical state
Git for versioned persistence
```

The weakness was in the lifecycle between those layers.

Three scaling risks had become concrete:

```text
1. Discoverability
   Important material may exist but future work may not know where to find it.

2. Implicit promotion
   A historical checkpoint may contain an idea that later becomes foundational,
   but nothing required the project to reconsider its status.

3. Duplication and drift
   CURRENT_STATE, canonical documents, checkpoints, and experiment records can
   begin repeating the same material and slowly diverge.
```

The correct response was not to introduce a database or complex retrieval system immediately. The demonstrated problem is semantic knowledge lifecycle management rather than storage capacity.

## Accepted preservation architecture v0.3

The new project-development architecture is:

```text
DISCUSSION / CHAT
    -> CHECKPOINT
    -> PROMOTION AUDIT
    -> canonical/foundational/specification update when warranted
    -> KNOWLEDGE_MAP routing update when warranted
    -> CURRENT_STATE concise orientation

At meaningful stage boundaries:
    -> KNOWLEDGE RECONCILIATION
```

The following changes are accepted.

### 1. Promotion audit at substantive checkpoints

Every substantive checkpoint must explicitly determine whether newly stabilized knowledge should be promoted into another layer.

Possible destinations include:

```text
VISION
PRINCIPLES
DECISIONS
OPEN QUESTIONS
DEVELOPMENT METHOD
CONTINUITY
FOUNDATION
SPECIFICATION / FROZEN CONTRACT
EXPERIMENT LEDGER
KNOWLEDGE MAP
MAJOR CHANGES
```

No promotion remains a valid and expected result for many checkpoints.

### 2. Knowledge map

Created:

```text
docs/KNOWLEDGE_MAP.md
```

The map is a routing layer, not another copy of project knowledge.

It points future sessions to:

```text
current canonical knowledge;
deep foundations;
frozen specifications;
active experiment ledgers;
important historical origins.
```

### 3. Periodic knowledge reconciliation

At meaningful stage boundaries, the project will review whether:

```text
important checkpoint insights were promoted;
canonical documents remain current;
open questions are still accurately described;
foundations are correctly scoped;
knowledge-map routing is correct;
CURRENT_STATE remains concise;
detailed experiment records live in dedicated ledgers;
contradictions or duplicate canonical statements exist;
major structural evolution is discoverable.
```

This is periodic rather than checkpoint-by-checkpoint bureaucracy.

### 4. Lightweight authority and maturity metadata

Important documents should make their role explicit through useful metadata such as:

```text
Status
Maturity
Authority / scope
Last reviewed
Origin / sources
Supersedes / superseded by
Change constraints
```

This is currently a semantic convention rather than a mandatory machine-readable schema.

### 5. Separate current state from detailed experiment status

Created:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

This now holds the detailed current run ledger for Prototype V0.

`docs/CURRENT_STATE.md` will return to a concise navigation role containing only the experiment summary, material current consequences, exact next step, and required reading.

### 6. Selective major-changes history

Created:

```text
docs/MAJOR_CHANGES.md
```

This records only major architectural, methodological, evaluation, preservation, repository, and experiment-phase changes that materially affect how future work should understand or operate the project.

It does not replace Git history or detailed checkpoints.

### 7. Preserve advanced future options without implementing them prematurely

Foundation 014 explicitly records possible future preservation infrastructure including:

```text
machine-readable metadata
generated indexes
semantic / hybrid retrieval
promotion queues
contradiction and staleness detection
dependency graphs
reconciliation assistants
provenance-aware raw conversation archives
graph or database representations
vector retrieval where justified
stronger transactional semantics for concurrent contributors
```

These options are deferred rather than rejected.

The current preservation substrate remains:

```text
Git + Markdown + explicit repository structure + curated updates
```

Advanced infrastructure should be introduced only when observed scale, retrieval, dependency, consistency, concurrency, or automation problems justify it.

## Files created

```text
docs/KNOWLEDGE_MAP.md
docs/MAJOR_CHANGES.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## Files materially updated

```text
README.md
    refreshed to the actual current Prototype V0 stage and new navigation architecture

docs/DEVELOPMENT_METHOD.md
    upgraded from version 0.2 to version 0.3

docs/CONTINUITY.md
    aligned with knowledge-map routing, promotion audits, reconciliation,
    concise CURRENT_STATE, and experiment-specific status ledgers

docs/DECISIONS.md
    added D-021 through D-025 covering the accepted preservation architecture

docs/OPEN_QUESTIONS.md
    reconciled stale Prototype V0 statuses and added Q-043 for the future
    transition beyond Git/Markdown preservation
```

## Open-question reconciliation performed

The first v0.3 reconciliation exposed several stale Prototype V0 entries in `OPEN_QUESTIONS.md`.

Notable corrections include:

```text
Q-016: V0 system evaluation is now in active held-out execution.
Q-019: invalidation is implemented in minimal P0 and under held-out evaluation.
Q-033: QUESTION/CLAIM distinction is implemented minimally in P0.
Q-036: the narrow initialization mechanism is implemented and under held-out evaluation.
Q-037: P0 activation is implemented and under held-out evaluation.
Q-039: the first held-out benchmark is active.
Q-040: the minimum prototype is implemented; empirical verdict pending.
Q-041: V0 concrete implementation is answered and frozen for held-out execution.
Q-042: baseline calibration question is answered; the common protocol was frozen.
Q-043: new explicit question records when more advanced knowledge infrastructure
       would become justified.
```

This validates the need for periodic reconciliation: several entries had become historically stale while current work had advanced substantially.

## Decisions added

```text
D-021  Add an explicit promotion audit to substantive checkpoints.
D-022  Maintain a knowledge map as a routing layer.
D-023  Perform periodic reconciliation and separate CURRENT_STATE from experiment ledgers.
D-024  Keep Git/Markdown now and defer advanced knowledge infrastructure until justified.
D-025  Maintain a selective major-changes ledger.
```

## Foundational rationale

The detailed rationale is preserved in:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

The broader system-level analogy is intentional: this project itself can suffer from stale evidence, unclear authority, hidden dependencies, and undiscoverable knowledge, which are structurally similar to the problems the target Autonomous Data Science System is intended to manage inside real data-science projects.

The repository-development process should therefore continue to act as a small live laboratory for knowledge-lifecycle requirements without assuming that the repository architecture should become the production system architecture.

## Experiment integrity

This entire checkpoint is meta-level documentation and project-development architecture.

No change was made to:

```text
P0 treatment behavior
B0/B1 prompts
P0 knowledge components
held-out benchmark bundles
H1/H2 data
held-out run order
resource budgets
provider/model configuration
provider normalization
retry semantics
semantic rubric
blinded judge protocol
continuation/falsification criteria
held-out executor behavior
```

The Prototype V0 experiment therefore remains frozen and comparable.

## Promotion audit

```text
Promoted to canonical development method:
    preservation architecture v0.3

Promoted to foundational reasoning:
    Foundation 014

Promoted to accepted decisions:
    D-021 through D-025

Added routing layer:
    KNOWLEDGE_MAP.md

Added structural-history layer:
    MAJOR_CHANGES.md

Added experiment-ledger separation:
    docs/experiments/prototype_v0/HELD_OUT_STATUS.md

Open-question reconciliation:
    completed for current V0/preservation-status drift
```

No target-system architecture or held-out treatment behavior was promoted or changed.

## Continuation point

After pulling this checkpoint and the accompanying `CURRENT_STATE.md` update, the frozen Prototype V0 experiment resumes from exactly the same next treatment slot as before this documentation architecture change:

```text
variant: H1
replicate: 3
condition: B1
slot: h1-r03-b1
attempt: h1-r03-b1-a01
```

Exactly one `run-next` invocation is authorized before stopping for terminal inspection.
