# Development Method

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

Both levels are expected to change through use.

## Core development loop

The current method is:

```text
free discussion
    -> identify important insights
    -> challenge and refine them
    -> reach a natural checkpoint
    -> extract stable knowledge
    -> preserve detailed reasoning where valuable
    -> update decisions and open questions
    -> update current state
    -> continue exploration
```

The purpose is to combine conversational freedom with durable project memory.

## Discussion should remain fluid

The project should not interrupt every useful discussion to update many files.

Exploratory reasoning is allowed to be messy. Ideas can be incomplete, contradictory, or speculative during discussion.

Documentation becomes more structured at checkpoints.

This prevents the preservation process from becoming so expensive that it interferes with actual thinking.

## Checkpoints

A checkpoint should be created when one or more of the following occurs:

- a major concept has been clarified;
- an important design decision has been made;
- a subject has been explored deeply enough that moving on would risk losing context;
- the project is about to change direction;
- the current chat is becoming long;
- a new chat may soon be required;
- implementation is about to begin after a conceptual phase;
- or a substantial real-project test has produced system-level lessons.

A checkpoint should normally capture:

- current focus;
- major ideas added or changed;
- accepted decisions;
- active design hypotheses;
- unresolved questions;
- important reasoning that deserves long-form preservation;
- explicit non-decisions;
- and the exact next continuation point.

## Knowledge layers

The project currently uses a layered preservation model.

### 1. Canonical documents

Examples:

- `VISION.md`
- `PRINCIPLES.md`
- `DECISIONS.md`
- `OPEN_QUESTIONS.md`
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
- and the reasoning behind important design hypotheses.

They are not required to be short.

### 3. Checkpoints and session records

These preserve what the project believed or was working on at a particular time.

They are historical snapshots rather than automatically current truth.

### 4. Raw historical material

Raw conversations may later be archived when useful.

If this layer is introduced, it should be treated as provenance rather than as canonical knowledge.

## Authority and conflict resolution

When documents conflict, the project should prefer the current accepted specification over historical material.

A practical hierarchy is:

1. current explicit decisions and current canonical specifications;
2. current principles and current-state records;
3. current requirements or architecture documents once they exist;
4. foundational design memos for rationale;
5. checkpoints and session records for historical state;
6. raw conversation archives for provenance.

If a conflict is material and cannot be resolved from status metadata, it should become an explicit open question rather than being guessed away.

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

This model is not yet formalized into a schema, but the distinction should be respected in writing.

For example, "the system should preserve evidence and assumptions" currently behaves like a principle. "The system should use a graph database" would currently be only an implementation idea.

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
- a new project characterization feature;
- or a revision to the development method itself.

## Avoiding premature completeness

The project should not attempt to enumerate all possible data science decisions before building or testing anything.

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

Before choosing an orchestration framework, database, agent SDK, graph engine, or other major technology, the project should understand what behavior the system actually requires.

## Meta-decisions are part of the project

Changes to the development method should themselves be preserved.

For example, if the project later discovers that a single `DECISIONS.md` file no longer scales, the replacement structure should be introduced deliberately and the reason should be documented.

The evolution of the methodology is itself useful knowledge.

## Documentation should not become the project

Preservation is important, but documentation overhead should remain proportionate.

The project should prefer natural checkpoints over constant micro-updates.

If maintaining current-state documents becomes repetitive or inconsistent, that is evidence that the preservation method should be redesigned or partly automated.

## Future automation of knowledge capture

A mature version of the project may eventually automate parts of this process.

For example, a system could propose:

```text
Potential additions detected:
- 2 decisions
- 3 design hypotheses
- 4 open questions
- 1 principle revision
```

The human could then approve, reject, or edit those changes.

This is not being automated yet. Manual curation is useful at the current stage because it helps reveal what good preservation actually requires.

## Version

**Development methodology version:** 0.1  
**Introduced:** Checkpoint 0, 2026-08-07

This version should be expected to change.
