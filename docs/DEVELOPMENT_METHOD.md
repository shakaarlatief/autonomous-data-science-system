# Development Method

**Status:** Current canonical project-development method  
**Current version:** 0.4  
**Last reviewed:** 2026-08-20

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

### Checkpoint metadata contract

Beginning with Development Method v0.4, checkpoint metadata is an explicit contract rather than a loose authoring convention.

The current checkpoint-format specification is:

```text
docs/checkpoints/README.md
```

Every new checkpoint created under the current ChatGPT-based development process must contain the following historical/authority core immediately after the title:

```text
Date
Status
Checkpoint class
Project stage
Scope
Authority
```

and must also preserve the current interaction-session provenance:

```text
Design session
ChatGPT project
Session title
```

The historical/authority core exists so a checkpoint can be interpreted without reconstructing its role from the filename or surrounding Git history. Session provenance exists so a future continuation can identify where the checkpoint was produced without depending on the old chat remaining available.

Checkpoint classes may add type-specific metadata when useful. Experiment records, for example, may add condition, run, attempt, blinding, verification, or treatment-impact information. Heterogeneous checkpoint classes should not be forced to carry semantically meaningless fields merely for visual uniformity.

The historical checkpoint body remains provenance. Metadata normalization may improve classification and discoverability, but it must not rewrite historical conclusions using later knowledge or silently promote old records into current authority.

The legacy normalization is complete. On 2026-08-20, Checkpoints `000` through `099` were normalized conservatively by the repository migration workflow while preserving titles and substantive bodies. The successful normalization commit is:

```text
bae5b8d00fa5da16029afee790c1a6762dc6c0fc
Normalize legacy checkpoint metadata
```

Checkpoints `100` through `102`, which were created in Design Session 02 before session provenance had again become mandatory, were subsequently backfilled in:

```text
ce6b029af78a33bb64f85377f5ff753f088ba190
Backfill Session 02 checkpoint provenance
```

The lightweight validator:

```text
scripts/check_checkpoint_metadata.py
```

now checks the current checkpoint contract, including the required session-provenance fields. The completed normalization should therefore be treated as closed historical repair, not as pending work.

See Checkpoint 103 and `docs/checkpoints/README.md` for the detailed contract and migration record.

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

Their mandatory historical/authority metadata, ChatGPT session provenance, and type-specific extension rules are governed by `docs/checkpoints/README.md`.

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

Version 0.3 introduced:

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

## Document metadata

Important documents should make their role and authority visible enough that a future reader does not need to infer it from folder location alone.

For documents other than checkpoints, where useful, metadata may include some subset of:

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

This remains a semantic convention rather than a rigid machine-readable schema for every repository document.

Checkpoint records are the exception. Actual repository use showed that the earlier loose convention produced inconsistent checkpoint headers, so v0.4 gives checkpoints a mandatory historical/authority core, mandatory ChatGPT session provenance under the current development process, and type-specific extensions through `docs/checkpoints/README.md`.

A future version may formalize metadata for additional document classes if observed inconsistency justifies doing so.

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
Are checkpoint metadata and authority classifications consistent?
Are there contradictions or duplicated canonical statements?
Does MAJOR_CHANGES capture significant structural evolution?
```

Reconciliation is periodic, not required after every checkpoint.

## Unplanned session-boundary recovery

The normal development loop assumes the project has time to complete its checkpoint, promotion, routing, and current-state updates before a design session ends. A platform conversation limit or other abrupt interruption can prevent that final reconciliation even when substantive reasoning has already been preserved.

The canonical recovery procedure lives in:

```text
docs/CONTINUITY.md
```

The Session 02 to Session 03 transition demonstrated the important distinction:

```text
substantive preservation failure
    !=
routing/current-state reconciliation drift
```

If research/specification/checkpoint artifacts already preserve the material reasoning, a new session should reconstruct from the active repository branch, identify the incomplete routing/canonical updates, and repair those conservatively rather than attempting to recreate an unavailable conversation from memory.

Checkpoint 120 records the first real use of this recovery path.

This clarification does not require Development Method v0.5. Version 0.4 already requires proactive preservation, promotion audits, current-state maintenance, routing, and stage-boundary reconciliation. `CONTINUITY.md` specifies how to finish those responsibilities after an unplanned boundary.

## Major structural changes

Version 0.3 introduced:

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

The checkpoint-header drift discovered at Checkpoint 100 is another Level-2 example: a deliberately loose metadata convention became inconsistent under sustained operational use, so the lesson was generalized into the v0.4 checkpoint metadata contract and mechanical validation direction.

The unexpected Session 02 boundary is a third Level-2 example: substantive knowledge survived because important research/specification/checkpoint material had already been preserved, but incomplete end-of-session routing still caused an incorrect initial reconstruction from `main`. The generalized recovery procedure now lives in `CONTINUITY.md` rather than requiring a new method version.

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

Version 0.4 does not alter the decision to defer a graph database, vector database, ontology service, or automatic summarization pipeline for repository preservation.

Potential future upgrades preserved in Foundation 014 include:

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

A small checkpoint-metadata validator is not a reversal of that deferral. It is a narrow mechanical check introduced because a precise, repeatedly observed consistency requirement now exists.

## Meta-decisions are part of the project

Changes to the development method should themselves be preserved.

Version 0.2 recorded proactive checkpoint detection. Version 0.3 recorded the move from durability-focused preservation toward an explicit lifecycle covering discoverability, promotion, authority, reconciliation, and selective structural history. Version 0.4 records the move from optional checkpoint metadata conventions to a mechanically validated checkpoint contract, including explicit session provenance under the current ChatGPT development process.

The evolution of the methodology is itself useful knowledge.

## Documentation should not become the project

Preservation is important, but documentation overhead should remain proportionate.

The project should prefer natural checkpoints over constant micro-updates.

Promotion audits should be short when no promotion is required. Reconciliation should happen at stage boundaries, not continuously.

Checkpoint metadata is intentionally a small mandatory historical/authority core plus mandatory session provenance and genuinely useful type-specific extensions. It should improve professional consistency without forcing every historical or operational record into a large universal template.

If maintaining the knowledge map, current state, metadata, or reconciliation process becomes repetitive or inconsistent, that is evidence that partial automation may be justified. Version 0.4 applies that principle narrowly by adding mechanical validation for checkpoint headers.

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

### Version 0.4

**Introduced:** Checkpoint 100, 2026-08-19  
**Contract strengthened and normalization closed:** Checkpoint 103, 2026-08-20

Changes:

- converted checkpoint metadata from a loose "some subset" convention into an explicit mandatory minimum contract;
- introduced `docs/checkpoints/README.md` as the checkpoint-format specification;
- required the historical/authority core `Date`, `Status`, `Checkpoint class`, `Project stage`, `Scope`, and `Authority` for every new checkpoint;
- made `Design session`, `ChatGPT project`, and `Session title` mandatory checkpoint provenance under the current ChatGPT-based development process;
- preserved type-specific metadata extensions rather than forcing heterogeneous checkpoint classes into one oversized header;
- normalized Checkpoints 000-099 conservatively without rewriting their substantive historical content;
- backfilled Session 02 provenance for Checkpoints 100-102;
- added and strengthened `scripts/check_checkpoint_metadata.py` to detect metadata and session-provenance drift mechanically;
- treated the observed checkpoint-header inconsistency as a real Level-2 development-method failure and generalized the lesson.

The subsequent unplanned Session 02 boundary did not create version 0.5. Its recovery procedure is a continuity specialization of the existing v0.4 preservation/reconciliation responsibilities and is documented in `docs/CONTINUITY.md` and Checkpoint 120.

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
