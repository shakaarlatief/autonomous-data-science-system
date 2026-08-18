# Development Method

**Status:** Current canonical project-development method  
**Current version:** 0.3  
**Last reviewed:** 2026-08-18

## Purpose

This document defines the current method for designing, documenting, testing, and evolving the Autonomous Data Science System itself.

The method is intentionally provisional. The project is expected to improve not only the target system, but also the process used to build that system.

## Two levels are evolving in parallel

The project has two coupled design problems.

### Level 1: the target system

Questions include:

- How should a data project be understood?
- What analyses should be considered?
- How should relevant investigations be activated?
- How should evidence be gathered?
- What roles or agents are useful?
- How should decisions be reviewed?
- When should the human be involved?
- How should project state be represented?
- How should the system learn from completed projects?

### Level 2: the method used to build the target system

Questions include:

- How should design discussions be preserved?
- What belongs in canonical documentation?
- What deserves a long-form foundational memo?
- How should speculative ideas be distinguished from accepted decisions?
- How should open questions remain visible?
- How should a new chat reconstruct the project?
- How should documentation evolve without becoming burdensome?
- How should important knowledge remain discoverable as the repository grows?
- How should historical insights be promoted when their maturity changes?
- How should duplicated or stale knowledge be detected?
- Who should decide when repository preservation is needed?

Both levels are expected to change through use.

## Core development loop

The current method is:

```text
free discussion
    -> identify important insights
    -> challenge and refine them
    -> AI design collaborator detects a natural checkpoint
    -> preserve the checkpoint
    -> perform a promotion audit
    -> update canonical/foundational/specification knowledge when warranted
    -> update routing in KNOWLEDGE_MAP when warranted
    -> update current state
    -> continue exploration
```

At meaningful stage boundaries, this local loop is supplemented by a broader knowledge reconciliation.

The purpose is to combine conversational freedom with durable, discoverable, correctly classified project memory.

## Discussion should remain fluid

The project should not interrupt every useful discussion to update many files.

Exploratory reasoning is allowed to be messy. Ideas can be incomplete, contradictory, or speculative during discussion.

Documentation becomes more structured at checkpoints.

This prevents the preservation process from becoming so expensive that it interferes with actual thinking.

## Proactive checkpoint responsibility

Beginning with development-method version 0.2, the AI design collaborator is explicitly responsible for deciding when a checkpoint or repository update is warranted during an active design conversation.

The user should not need to remember to request preservation after every important discussion.

The AI should continue the conversation when ideas are still developing fluidly and should initiate a checkpoint when preservation has become more valuable than additional uninterrupted exploration.

This responsibility is about checkpoint detection, not unilateral canonization. The AI must still distinguish accepted decisions from strong hypotheses, open questions, provisional abstractions, and historical reasoning.

If the status of an idea is unclear, it should be preserved at the weaker maturity level rather than silently promoted to a principle or decision.

## Checkpoints

A checkpoint should be created when one or more of the following occurs:

- a major concept has been clarified;
- an important design decision has been made;
- a subject has been explored deeply enough that moving on would risk losing context;
- a coherent cluster of strong design hypotheses has emerged and deserves preservation before a new topic;
- the project is about to change direction;
- the current chat is becoming long;
- a new chat may soon be required;
- implementation is about to begin after a conceptual phase;
- a substantial real-project test has produced system-level lessons;
- a major experiment milestone has been reached;
- or the user explicitly requests a repository update.

A checkpoint should normally capture:

- current focus;
- major ideas added or changed;
- accepted decisions;
- active design hypotheses;
- unresolved questions;
- important reasoning that deserves long-form preservation;
- explicit non-decisions;
- the promotion-audit result;
- and the exact next continuation point.

A checkpoint should not be created merely because a fixed number of messages has passed.

## Promotion audit

Beginning with version 0.3, every substantive checkpoint should explicitly ask whether newly stabilized material deserves promotion beyond the historical checkpoint layer.

Candidate destinations include:

```text
VISION.md
PRINCIPLES.md
DECISIONS.md
OPEN_QUESTIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
a foundational design memo
a current specification or frozen contract
KNOWLEDGE_MAP.md
an experiment-specific status document
MAJOR_CHANGES.md
```

No promotion is a valid and common outcome.

A checkpoint can therefore state:

```text
Promotion audit: none required.
Reason: mechanical or historical record only.
```

The audit exists to prevent important knowledge from becoming dependent on someone remembering a historical checkpoint number.

Promotion must respect maturity. Historical prominence is not evidence that an idea should become canonical.

## Knowledge layers

The project uses a layered preservation model.

### 1. Canonical documents

Examples:

- `VISION.md`
- `PRINCIPLES.md`
- `DECISIONS.md`
- `OPEN_QUESTIONS.md`
- `DEVELOPMENT_METHOD.md`
- `CONTINUITY.md`
- future specifications and requirements

These should be reasonably concise, current, and intentionally maintained.

Their purpose is operational usability.

### 2. Foundational design memos

These preserve rich reasoning that would be damaged by aggressive compression.

They may include:

- motivations;
- examples;
- arguments;
- distinctions;
- failure scenarios;
- conceptual diagrams;
- rejected alternatives;
- domain stress tests;
- and the reasoning behind important design hypotheses.

They are not required to be short and are not automatically binding implementation contracts.

### 3. Checkpoints and session records

These preserve what the project believed or was working on at a particular time.

They are historical snapshots rather than automatically current truth.

### 4. Experiment-specific status ledgers

Long-running experiments may maintain detailed current ledgers separate from `CURRENT_STATE.md`.

For Prototype V0:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

The ledger contains detailed run-by-run mechanics. `CURRENT_STATE.md` should only summarize what is needed for project continuity.

### 5. Raw historical material

Raw conversations may later be archived when useful.

If this layer is introduced, it should be treated as provenance rather than as canonical knowledge.

## Routing layer: KNOWLEDGE_MAP

Version 0.3 introduces:

```text
docs/KNOWLEDGE_MAP.md
```

The knowledge map is not another knowledge layer in the sense of owning the substantive truth. It is a routing/index layer.

Its job is to answer:

```text
Where is the current canonical statement?
Where is the deep rationale?
Where is the frozen experiment contract?
Where is the historical origin?
Where is the current detailed experiment status?
```

It should remain concise enough to navigate and should point to authoritative sources rather than duplicating them.

## Authority and conflict resolution

When documents conflict, the project should prefer the current accepted specification over historical material.

A practical hierarchy is:

1. frozen current specifications/contracts for their declared scope;
2. current explicit decisions and current canonical specifications;
3. current principles, vision, and current-state records;
4. foundational design memos for rationale and durable hypotheses;
5. checkpoints and session records for historical state;
6. raw conversation archives for provenance.

If a conflict is material and cannot be resolved from status metadata, it should become an explicit open question rather than being guessed away.

## Lightweight document metadata

Version 0.3 introduces an explicit requirement that important documents make their role and authority visible enough that a future reader does not need to infer it from folder location alone.

Where useful, documents should include some subset of:

```text
Status
Maturity
Authority or scope
Date / last reviewed
Origin or sources
Supersedes
Superseded by
Change constraints
```

This is currently a semantic convention rather than a rigid machine-readable schema.

A future version may formalize the metadata if manual conventions become insufficient.

## Knowledge maturity

Not every statement should be treated as equally mature.

The current conceptual maturity path is:

```text
raw thought
  -> candidate idea
  -> active design hypothesis
  -> tested on examples or projects
  -> accepted principle or decision
  -> challenged
  -> revised, superseded, or rejected
```

The distinction should be respected in writing, promotion, and routing.

For example, "the system should preserve evidence and assumptions" behaves like a principle. "The epistemic core consists exactly of five invariants" remains a strong design hypothesis until broader evidence justifies stronger status.

## Knowledge reconciliation

Version 0.3 adds periodic knowledge reconciliation at meaningful stage boundaries.

Typical triggers include:

- completion of a conceptual design phase;
- freezing a prototype architecture;
- completion of a held-out experiment;
- beginning a new prototype generation;
- a major target-system architecture revision;
- a major development-method revision;
- or evidence that current documentation has become stale, repetitive, or inconsistent.

A reconciliation should ask:

```text
Were durable checkpoint insights promoted where appropriate?
Are VISION, PRINCIPLES, and DECISIONS still current?
Are OPEN_QUESTIONS actually open and accurately described?
Are important foundations still correctly scoped?
Does KNOWLEDGE_MAP route to the right current sources?
Is CURRENT_STATE concise and present-tense?
Are detailed experiment records stored outside CURRENT_STATE?
Are there contradictions or duplicated canonical statements?
Does MAJOR_CHANGES capture significant structural evolution?
```

Reconciliation is periodic, not required after every checkpoint.

## Major structural changes

Version 0.3 introduces:

```text
docs/MAJOR_CHANGES.md
```

This is a selective conceptual history, not a commit log.

It should record changes that materially alter:

```text
system-level vision;
target architecture direction;
prototype architecture;
evaluation architecture;
development methodology;
knowledge-preservation architecture;
major experimental phase or frozen contract;
or repository structure in ways that affect future work.
```

Routine run records, typo fixes, and ordinary checkpoints do not belong there.

## Real projects as system tests

The system should be developed against heterogeneous data projects rather than only abstract discussion.

A project can test questions such as:

- Did the system identify the important structural properties of the data?
- Did it ask the right questions before modelling?
- Did it select an appropriate validation design?
- Did it identify leakage risks?
- Did it investigate missingness appropriately?
- Did it consider relevant model families without unnecessary breadth?
- Did it recognize when a later finding invalidated an earlier choice?
- Did it involve the human at useful points?
- Did it waste effort on irrelevant analysis?
- Did it preserve evidence and decisions correctly?
- Did it generate reproducible outputs?
- Did the emerging epistemic invariants explain the failures and safeguards encountered in practice?

The goal is not merely to obtain a good model. The project also tests the quality of the process that produced the model.

## System gap extraction

When a project reveals a weakness, the project should record the gap conceptually even if a formal gap registry has not yet been created.

A useful analysis is:

```text
observed failure
    -> why did the current system miss it?
    -> is the lesson project-specific or general?
    -> if general, what reusable capability should change?
    -> what future test can prevent regression?
```

Possible reusable improvements include:

- a new question;
- a new trigger;
- a new decision branch;
- a new hard constraint;
- a new reviewer;
- a new evidence requirement;
- a new project-characterization feature;
- or a revision to the development method itself.

The Checkpoint 22 promotion gap is an example at Level 2: knowledge was durable but not sufficiently discoverable/promoted, so the project generalized the lesson into Development Method v0.3.

## Avoiding premature completeness

The project should not attempt to enumerate all possible data-science decisions before building or testing anything.

Instead:

1. establish a strong core;
2. test it on different projects;
3. observe where it fails or becomes inefficient;
4. extract general lessons;
5. expand coverage deliberately.

This is similar in spirit to test-driven or case-driven development of the reasoning system.

## Avoiding premature implementation

Technology choices should follow from clarified requirements.

The project should not select tools merely because they are popular or because they make the current idea easy to prototype.

Before choosing an orchestration framework, database, agent SDK, graph engine, vector database, or other major technology, the project should understand what behavior the system actually requires.

## Deferred preservation infrastructure

The current preservation storage foundation remains:

```text
Git
Markdown
explicit repository structure
manual or AI-assisted curation
```

Version 0.3 deliberately does not introduce Neo4j, another graph database, a vector database, an ontology service, or an automatic summarization pipeline.

Potential future upgrades are preserved in Foundation 014 and include:

```text
machine-readable metadata;
generated indexes;
semantic or hybrid retrieval;
promotion queues;
contradiction/staleness detection;
dependency graphs;
reconciliation assistants;
provenance-aware raw conversation archives;
stronger transactional knowledge storage when multiple contributors require it.
```

These are deferred rather than rejected. They should be introduced when an observed scale, retrieval, consistency, dependency, or automation problem justifies the added complexity.

## Meta-decisions are part of the project

Changes to the development method should themselves be preserved.

Version 0.2 recorded proactive checkpoint detection. Version 0.3 records the move from durability-focused preservation toward an explicit lifecycle covering discoverability, promotion, authority, reconciliation, and selective structural history.

The evolution of the methodology is itself useful knowledge.

## Documentation should not become the project

Preservation is important, but documentation overhead should remain proportionate.

The project should prefer natural checkpoints over constant micro-updates.

Promotion audits should be short when no promotion is required. Reconciliation should happen at stage boundaries, not continuously.

If maintaining the knowledge map, current state, metadata, or reconciliation process becomes repetitive or inconsistent, that is evidence that partial automation may now be justified.

## Future automation of knowledge capture

A mature version of the project may eventually automate parts of this process.

For example, a system could propose:

```text
Potential promotions detected:
- 2 decisions
- 3 design hypotheses
- 4 open questions
- 1 principle revision
- 2 knowledge-map routing changes
```

A reconciliation assistant could also detect candidate stale or contradictory statements.

Automatic extraction must not imply automatic promotion into trusted reusable knowledge. Manual curation remains useful at the current stage because it continues to reveal what good preservation actually requires.

## Version history

### Version 0.3

**Introduced:** Checkpoint 76, 2026-08-18

Changes:

- added an explicit promotion audit for substantive checkpoints;
- introduced `docs/KNOWLEDGE_MAP.md` as a routing layer;
- introduced periodic knowledge reconciliation at meaningful stage boundaries;
- introduced lightweight authority/maturity/provenance metadata conventions;
- introduced experiment-specific status ledgers so `CURRENT_STATE.md` can remain concise;
- introduced `docs/MAJOR_CHANGES.md` as a selective structural history;
- explicitly preserved but deferred more advanced knowledge infrastructure such as graph databases, vector retrieval, generated indexes, and automated reconciliation until observed needs justify them;
- treated the Checkpoint 22 promotion issue as a real failure mode of the prior preservation process and generalized the lesson.

Detailed rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

### Version 0.2

**Introduced:** Checkpoint 2, 2026-08-08

Changes:

- made proactive checkpoint detection an explicit responsibility of the AI design collaborator;
- clarified that checkpoint timing should be based on conceptual progress and continuity value rather than message count;
- clarified that proactive preservation does not imply automatic promotion of hypotheses into accepted decisions;
- added the emerging epistemic-core hypothesis as an example of maturity-status discipline.

### Version 0.1

**Introduced:** Checkpoint 0, 2026-08-07

Initial development method establishing fluid discussion, layered knowledge preservation, checkpoints, maturity distinctions, real-project testing, and explicit methodological evolution.
