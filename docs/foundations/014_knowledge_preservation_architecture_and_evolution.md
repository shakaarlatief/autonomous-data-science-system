# Foundation 014: Knowledge Preservation Architecture and Evolution

**Date:** 2026-08-18  
**Status:** Foundational design memo  
**Maturity:** Accepted current project-development architecture with explicitly deferred future tooling  
**Scope:** How this project preserves, promotes, discovers, reconciles, and evolves its own knowledge. This does not change Prototype V0 treatment behavior.

## Purpose

The Autonomous Data Science System project has always treated knowledge preservation as part of the design problem rather than as incidental documentation. The original method established a layered repository so that long-running design work would not depend on chat memory.

Actual use has now exposed the first important scaling weakness in that method.

Checkpoint 22 preserved a system-level synthesis that later proved important enough to deserve foundational status. The checkpoint was never physically at risk because it was committed to Git, but its importance became increasingly dependent on someone remembering that it existed. The material was therefore historically preserved but not sufficiently discoverable or promoted.

This distinction motivates Development Method version 0.3.

The problem is no longer only:

```text
Will knowledge disappear?
```

It is also:

```text
Can future work find the right knowledge?
Can it tell which document is authoritative?
Can durable ideas move out of historical records when appropriate?
Can stale or duplicated knowledge be detected before it causes drift?
Can current-state documents stay useful as the project grows?
```

The current answer is to keep the existing Git-and-Markdown foundation while strengthening the semantic lifecycle around it.

---

## 1. Preservation has several distinct failure modes

Version 0.1 primarily protected against conversational loss. Version 0.2 added proactive checkpoint detection. Experience now shows that preservation quality has at least five distinct dimensions.

### Durability

The information continues to exist after chats, context windows, models, or sessions change.

Git-backed repository artifacts already provide this reasonably well.

### Discoverability

A future session can locate the relevant explanation without knowing a historical checkpoint number or searching hundreds of files manually.

This becomes increasingly important as foundations, checkpoints, experiments, and prototype generations accumulate.

### Authority

A future reader can distinguish current canonical knowledge from rationale, historical state, frozen experiment contracts, open hypotheses, and superseded material.

### Promotion

Important knowledge that first appears in discussion or a checkpoint can move into the appropriate durable layer when its maturity or importance changes.

### Reconciliation

The project periodically checks whether canonical files, foundations, open questions, experiment records, and routing documents have drifted, duplicated one another incorrectly, or retained stale statements.

A repository can succeed at durability while failing badly at the other four.

---

## 2. The preservation architecture

The current architecture is:

```text
DISCUSSION / CHAT
    exploratory reasoning
        |
        v
CHECKPOINT
    historical snapshot and provenance
        |
        v
PROMOTION AUDIT
    decide whether new material belongs elsewhere
        |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
CANONICAL DOCUMENTS       FOUNDATIONS            HISTORY ONLY
current operational       deep durable           no promotion
knowledge                 reasoning
        |                      |
        +-----------+----------+
                    v
             KNOWLEDGE MAP
       routing and discoverability
                    |
                    v
             CURRENT STATE
       concise present-tense navigation
                    |
                    v
             CONTINUITY PROCESS
```

The important point is that the knowledge map is not another copy of the knowledge. It is a routing layer that points to where authoritative and explanatory knowledge lives.

---

## 3. Existing layers remain valid

The project keeps the existing layers because they solve different problems.

### Canonical documents

Examples include:

```text
VISION.md
PRINCIPLES.md
DECISIONS.md
OPEN_QUESTIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
```

These should remain current enough for routine project navigation and decision making.

### Foundational design memos

Foundations preserve detailed reasoning, examples, distinctions, motivations, and design hypotheses that would be damaged by aggressive compression.

They are not automatically implementation contracts.

### Checkpoints

Checkpoints preserve historical project state, experiment milestones, implementation transitions, and the reasoning context of important moments.

They remain first-class provenance but are not automatically current truth.

### Experiment records

Detailed long-running experiment ledgers should live in experiment-specific status documents rather than making `CURRENT_STATE.md` grow indefinitely.

### Raw historical material

Raw chats or other transcripts may later be archived, but remain provenance rather than canonical knowledge unless explicitly promoted.

---

## 4. Promotion audit

Every substantive checkpoint should now include an explicit promotion audit.

The audit asks whether any newly stabilized material should update one or more of:

```text
VISION
PRINCIPLES
DECISIONS
OPEN QUESTIONS
DEVELOPMENT METHOD
CONTINUITY
A FOUNDATION
A SPECIFICATION OR FROZEN CONTRACT
THE KNOWLEDGE MAP
AN EXPERIMENT STATUS DOCUMENT
THE MAJOR-CHANGES LEDGER
```

No promotion is a valid outcome.

For many checkpoints the correct result will be:

```text
Promotion required: none.
Reason: this checkpoint is historical/mechanical only.
```

The purpose is not to create documentation churn. The purpose is to prevent important knowledge from remaining buried merely because nobody remembered to promote it.

Promotion must preserve maturity distinctions. An interesting idea should not become a principle simply because it appeared in a checkpoint. If status is uncertain, preserve it at the weaker level.

---

## 5. Knowledge map

`docs/KNOWLEDGE_MAP.md` is introduced as the primary routing layer for durable project knowledge.

Its responsibilities are:

```text
identify major knowledge domains;
point to current canonical documents;
point to deep foundational reasoning;
point to frozen specifications where relevant;
point to important historical origins where useful;
show which document should be read first for a question;
avoid duplicating the full content of those documents.
```

It should answer questions such as:

```text
Where is the current system vision?
Where is the explanation of why a system is needed beyond one LLM?
Where is project-state theory documented?
Where is knowledge activation theory documented?
Where is the Prototype V0 experiment contract?
Where is current held-out execution status?
Where is the history of major architecture changes?
```

The map should remain concise enough to function as navigation rather than becoming another foundation.

---

## 6. Authority and lightweight metadata

Important documents should make their role explicit enough that future readers do not need to infer authority from directory names alone.

Where useful, a document should state some subset of:

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

Not every Markdown file needs a rigid machine-readable header immediately. Version 0.3 introduces the semantic requirement, not a mandatory universal schema.

The minimum goal is that high-value or potentially conflicting documents explain whether they are:

```text
canonical current knowledge;
foundational rationale;
historical provenance;
a frozen experiment contract;
an experiment status ledger;
an active hypothesis;
or a superseded artifact.
```

A future version may formalize these fields if manual conventions become insufficient.

---

## 7. Knowledge reconciliation

Checkpoint-by-checkpoint preservation is not enough because local updates can accumulate drift over time.

At meaningful stage boundaries, the project should perform a knowledge reconciliation.

Typical triggers include:

```text
completion of a conceptual design phase;
freezing a prototype architecture;
completion of a held-out experiment;
beginning a new prototype generation;
a major system-level architectural revision;
a major development-method revision;
or evidence that canonical files have become stale or duplicative.
```

A reconciliation should review recent durable knowledge and ask:

```text
Were important checkpoint insights promoted?
Are canonical documents still current?
Are accepted decisions reflected consistently?
Are open questions still genuinely open?
Did any foundation become superseded or materially revised?
Is the knowledge map routing correctly?
Is CURRENT_STATE concise and current?
Are detailed experiment records stored in the right place?
Are there contradictions or duplicate canonical statements?
Does the major-changes ledger capture the significant structural change?
```

This should be periodic rather than performed after every small update.

---

## 8. Current state versus detailed ledgers

`docs/CURRENT_STATE.md` should return to its intended role as a concise present-tense orientation document.

It should primarily answer:

```text
What are we building?
What stage are we in?
What important current conclusions or constraints matter now?
What is the next action?
What should a future session read?
```

Detailed run histories, repeated metrics, and full experiment mechanics should live in experiment-specific ledgers such as:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

Checkpoints remain the detailed historical records for individual milestones.

This separation reduces duplication and makes continuity less dependent on a continuously growing current-state file.

---

## 9. Major changes deserve their own selective ledger

Git history contains every commit, but a commit log is not the same as a conceptual history of the project.

`docs/MAJOR_CHANGES.md` therefore records only changes that materially alter one of the following:

```text
system-level vision;
target architecture direction;
prototype architecture;
evaluation architecture;
development methodology;
knowledge-preservation architecture;
major experimental phase or frozen contract;
repository structure where the change affects how future work should operate.
```

This file should remain selective. Ordinary checkpoint creation, typo fixes, and routine run records do not belong there.

Each entry should point to the detailed decision, foundation, checkpoint, or specification rather than reproduce it.

---

## 10. Deferred advanced preservation infrastructure

The project deliberately does not introduce a database, knowledge graph engine, vector database, ontology service, or automatic summarization pipeline merely because the repository is growing.

The current storage medium remains:

```text
Git
Markdown
explicit repository structure
manual or AI-assisted curation
```

This is intentional because the immediate failure mode is semantic lifecycle management, not lack of storage technology.

Possible future upgrades include:

```text
machine-readable document metadata;
a generated knowledge index;
semantic search over canonical and foundational artifacts;
a structured promotion queue;
a contradiction/staleness detector;
a dependency graph among decisions, foundations, experiments, and claims;
a reconciliation assistant that proposes stale or duplicated items;
a provenance-aware raw-conversation archive;
a graph or database representation if cross-document dependencies become too complex for Markdown;
a vector or hybrid retrieval layer if exact routing and ordinary repository search become insufficient;
a machine-checkable authority and supersession model.
```

These are deliberately deferred, not rejected.

They should be introduced only when a demonstrated retrieval, consistency, dependency, scale, or automation problem justifies the added machinery.

A future trigger for stronger infrastructure might be evidence such as:

```text
manual knowledge-map maintenance becoming unreliable;
frequent failure to discover relevant existing knowledge;
repeated contradictory canonical statements;
large dependency networks that cannot be maintained safely in prose;
reconciliation becoming too expensive to perform manually;
or multiple concurrent contributors/models needing stronger transactional semantics.
```

---

## 11. Why this matters for the target system

The preservation problem encountered by this project is structurally similar to the problem the Autonomous Data Science System is intended to solve inside real analytical projects.

For example:

```text
evidence may exist but no longer be current;
a decision may exist but its dependencies may be unclear;
an old assumption may be contradicted without downstream repair;
a useful insight may exist but never activate in future reasoning;
historical material may be mistaken for current truth;
important knowledge may be durable but practically undiscoverable.
```

The repository therefore acts as a small live laboratory for project-state and knowledge-lifecycle ideas.

This does not mean the repository documentation architecture should be copied directly into the eventual product. It means failures in our own long-running design process can reveal genuine requirements for the broader system.

---

## 12. Current accepted architecture

Development Method version 0.3 therefore adopts the following principles for project knowledge preservation:

```text
1. Keep Git and Markdown as the current storage foundation.
2. Preserve layered knowledge rather than one giant canonical document.
3. Treat checkpoints as history, not automatic current truth.
4. Perform an explicit promotion audit at substantive checkpoints.
5. Maintain a KNOWLEDGE_MAP routing layer.
6. Make important document authority/maturity visible.
7. Perform periodic knowledge reconciliation at meaningful stage boundaries.
8. Keep CURRENT_STATE concise and move detailed experiment ledgers elsewhere.
9. Maintain a selective MAJOR_CHANGES ledger for structural evolution.
10. Defer graph/vector/database/automation infrastructure until observed problems justify it.
```

This architecture should itself remain empirical. If actual use exposes another failure mode, the development method should evolve again rather than being preserved for its own sake.
