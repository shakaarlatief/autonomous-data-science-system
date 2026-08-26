# Development Method

**Status:** Current canonical project-development method  
**Current version:** 0.5  
**Last reviewed:** 2026-08-26

## Purpose

This document defines the current method for designing, documenting, testing, reviewing, and evolving the Autonomous Data Science System itself.

The method is intentionally provisional. ADS evolves at two levels simultaneously:

```text
Level 1
    the target Autonomous Data Science System

Level 2
    the method used to build, preserve, review, and evolve that system
```

Changes at either level should be evidence-driven and should preserve maturity, authority, provenance, and reversibility.

---

## Two levels are evolving in parallel

### Level 1: target-system questions

Examples include:

- how a data project should be understood;
- which analyses and investigations matter;
- how reusable methodology should be activated;
- how evidence, claims, decisions, and project state should be represented;
- what execution and reasoning capabilities are useful;
- when the human should be involved;
- how project state should evolve;
- and how completed projects should improve the system.

### Level 2: development-method questions

Examples include:

- how important reasoning should be preserved;
- what belongs in canonical knowledge versus historical provenance;
- when checkpointing and promotion are warranted;
- how new sessions/models reconstruct project state;
- how multiple AI collaborators may work without corrupting ownership or independence;
- how reviews should be routed, deferred, and resolved;
- how disagreement should remain visible;
- how session/provenance metadata should remain provider-neutral;
- and when additional automation has actually earned its complexity.

Both levels are expected to change through use.

---

## Core development loop

The current loop is:

```text
free discussion / exploration
    -> identify important insights or implementation boundaries
    -> challenge and refine them
    -> active AI collaborator detects a natural checkpoint
    -> preserve the checkpoint
    -> perform a promotion audit
    -> update canonical/foundational/specification knowledge when warranted
    -> update routing when warranted
    -> update current state
    -> continue exploration
```

At major stage boundaries, this local loop is supplemented by a broader knowledge reconciliation.

The purpose is to combine conversational freedom with durable, discoverable, correctly classified project memory.

---

## Discussion should remain fluid

The project should not interrupt every useful discussion to update many files.

Exploratory reasoning may be incomplete, contradictory, or speculative while it is still developing.

Documentation becomes more structured at natural checkpoints.

The preservation process must not become so expensive that it interferes with the substantive work.

---

## Proactive checkpoint responsibility

The active AI design collaborator is responsible for deciding when repository preservation or a checkpoint is warranted.

The user should not need to request every update manually.

A checkpoint is normally warranted when one or more of the following becomes material:

- a major concept has been clarified;
- an important decision has been made;
- a coherent cluster of hypotheses deserves preservation;
- implementation is about to begin after a conceptual phase;
- a substantial implementation/result milestone has been reached;
- the project is about to change direction;
- a real project or experiment has produced system-level lessons;
- the current interaction is becoming long or fragile;
- another session/model may need to continue the work;
- or the user explicitly requests preservation.

A checkpoint should not be created merely because a fixed number of messages has passed.

Checkpointing is preservation, not unilateral canonization. If maturity is unclear, preserve the weaker status rather than silently promoting the idea.

---

## Checkpoint contents

A substantive checkpoint should normally preserve:

```text
current focus
important changes since the prior checkpoint
accepted decisions
active hypotheses
unresolved questions
important detailed reasoning
explicit non-decisions
promotion-audit result
exact next continuation point
```

Operational/experiment checkpoints may be narrower when the purpose is to preserve one specific execution or verification boundary.

### Checkpoint metadata contract

Checkpoint metadata is governed by:

```text
docs/checkpoints/README.md
```

All checkpoints use a mandatory historical/authority core:

```text
Date
Status
Checkpoint class
Project stage
Scope
Authority
```

Historical checkpoints through Checkpoint 203 retain the earlier ChatGPT-specific interaction provenance:

```text
Design session
ChatGPT project
Session title
```

Beginning with Checkpoint 204, new checkpoints use provider-neutral interaction provenance:

```text
Interaction environment
Project / workspace
Interaction session
Conversation title
Primary collaborator
```

The migration is prospective. Historical checkpoint provenance is not rewritten merely for cosmetic uniformity.

The validator:

```text
scripts/check_checkpoint_metadata.py
```

must enforce the appropriate contract according to checkpoint number.

---

## Promotion audit

Every substantive checkpoint should explicitly ask whether newly stabilized material deserves promotion beyond the historical checkpoint layer.

Candidate destinations include:

```text
VISION.md
PRINCIPLES.md
DECISIONS.md
OPEN_QUESTIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
a foundational memo
a research memo
a current/frozen specification
KNOWLEDGE_MAP.md
an experiment/status ledger
MAJOR_CHANGES.md
```

No promotion is a valid outcome.

Promotion must respect maturity. Historical prominence, model confidence, or multi-model agreement does not by itself create authority.

---

## Knowledge layers

### 1. Canonical documents

Examples:

```text
VISION.md
PRINCIPLES.md
DECISIONS.md
OPEN_QUESTIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
accepted specifications
```

These should remain reasonably concise, current, and operationally usable.

### 2. Foundational design memos

Foundations preserve durable reasoning that would be damaged by aggressive compression: motivations, distinctions, examples, alternatives, failure scenarios, conceptual structure, and deeper rationale.

A foundation is not automatically an implementation contract.

### 3. Research and specifications

Research preserves bounded candidate reasoning and evidence. Specifications define explicit contracts for their declared scope, with status/maturity determining whether they are candidate, frozen, accepted, failed, or superseded.

### 4. Checkpoints and session records

Checkpoints preserve what the project believed, observed, or did at a particular time. They are historical provenance rather than automatic current truth.

### 5. Experiment/status ledgers

Long-running or detailed operational evidence belongs in dedicated ledgers rather than bloating `CURRENT_STATE.md`.

### 6. Collaboration provenance

`docs/model_collaboration/` preserves cross-model briefs, machine-readable collaboration state, numbered review messages, deferred-review routing, and resolution records.

These artifacts are provenance/coordination evidence. They do not become canonical project truth merely because multiple models participated.

### 7. Raw historical material

Raw conversations may be archived later where useful, but remain provenance rather than canonical authority.

---

## Routing layer: KNOWLEDGE_MAP

`docs/KNOWLEDGE_MAP.md` is a routing/index layer, not another owner of substantive truth.

It should answer:

```text
Where is the current canonical statement?
Where is the deep rationale?
Where is the frozen/accepted contract?
Where is the historical origin?
Where is the current detailed status?
```

It should point to authorities rather than duplicate them.

---

## Authority and conflict resolution

The practical authority order remains:

1. accepted/frozen current specifications/contracts within their declared scope;
2. current explicit decisions and current canonical specifications;
3. current principles, vision, development method, continuity, and current-state records;
4. foundational memos for rationale and durable hypotheses;
5. research memos for bounded candidate reasoning;
6. checkpoints and collaboration records for historical/review provenance;
7. raw historical material.

If a material conflict cannot be resolved from status, scope, chronology, supersession, or accepted authority, preserve it as an explicit open question rather than guessing.

---

## Knowledge maturity

A useful conceptual path is:

```text
raw thought
  -> candidate idea
  -> active design hypothesis
  -> tested on examples/projects/implementation
  -> accepted principle or decision
  -> challenged
  -> revised, superseded, or rejected
```

Different axes such as truth confidence, implementation status, source quality, coverage, enforcement strength, and freshness must not be collapsed into one maturity label.

---

# Governed multi-model development

Development Method v0.5 introduces provider-neutral governed collaboration among ChatGPT, Claude, the human project owner, and future collaborators.

The governing protocol is:

```text
docs/model_collaboration/README.md
```

The collaboration architecture was not accepted from one model proposal. It was pressure-tested through MC-0001, mechanically exercised by Specification 024/MC-0002, and extended through the real deferred-review pressure test in MC-0003.

## Collaboration is selective

Multi-model capability does not mean multi-model requirement.

Normal modes include:

```text
SOLO
REVIEWED
INDEPENDENT_THEN_COMPARATIVE
COORDINATED_HANDOFF
ADVERSARIAL_REVIEW
```

ChatGPT-only and Claude-only development remain first-class. A second model should enter because its contribution is expected to add meaningful value, not because dual-model ceremony is mandatory.

## One bounded task owner

Every substantive collaborative bounded task has one task owner unless ownership is explicitly transferred.

The owner is responsible for task scope, integration, preservation, and coherent target-state mutation.

## Role and write scope are separate

```text
ROLE != WRITE_SCOPE
```

A reviewer, researcher, critic, verifier, or counter-designer may have permission to write an explicitly declared secondary surface without owning the target implementation or canonical state.

One collaborator owns target-state writes at a time. Secondary writers must remain inside declared secondary surfaces.

The accepted Specification 024 state guard makes this coordination state machine-checkable for guarded threads.

The guard is a coherence mechanism, not authenticated model identity or a distributed mutex.

## Collaboration transport and authority

GitHub issues/PR comments may be used for low-friction notices, pointers, or discussion.

Numbered repository message files preserve substantive collaboration provenance.

Neither surface is automatically canonical authority. Accepted project changes still pass through normal checkpoint/promotion/decision mechanisms.

## Genuine review

Agreement is not rewarded. Disagreement is not rewarded.

When agreeing, the reviewer should still identify the strongest plausible failure mode, strongest alternative considered, and evidence that would change its view.

When disagreeing, the reviewer should identify the exact disputed choice, why it matters, preferred alternative, what would reverse its position, and the disagreement type.

Material disagreement should not be averaged away for social smoothness.

## Independent review integrity

For consequential questions where independence matters, the default design is:

```text
accepted pre-proposal repository ref
+
neutral problem brief
+
constraints/success criteria
+
explicit exposure audit
```

The reviewer freezes its independent position before seeing the detailed proposer solution.

If current routing or other supposedly neutral material already leaks the candidate design, the review must be classified as partially independent rather than falsely labeled blind.

## Disagreement routing

Useful categories include:

```text
FACT
INTERPRETATION
REQUIREMENT
ARCHITECTURE
RISK
EVIDENCE_SUFFICIENCY
NORMATIVE_PROJECT_INTENT
SCOPE
```

Typical routing:

```text
FACT
    inspect repository/source/test evidence

INTERPRETATION
    expose shared evidence and seek discriminating evidence

REQUIREMENT
    inspect accepted requirement first; human decides when it must be chosen/changed

ARCHITECTURE
    compare against accepted requirements; prototype/falsify where useful

RISK
    reason proportionately about consequence, likelihood/uncertainty,
    reversibility, blast radius, mitigation, and precaution cost

EVIDENCE_SUFFICIENCY
    define stronger evidence/gate or preserve unresolved status

NORMATIVE_PROJECT_INTENT
    human decision

SCOPE
    inspect task authority and obligations; no blanket narrow-scope-wins rule
```

There is no universal conservative-wins or narrow-scope-wins default.

## Human role

The human project owner is not a routine transport clerk or approval gate for every model transition.

The human remains authoritative for:

```text
project intent
normative choices
desired requirement changes
consequential risk acceptance
resource commitments
important technically underdetermined trade-offs
```

Routine thread opening, ordinary review, and uncontested ownership transfer may proceed under the governed method.

---

# Deferred asynchronous review and catch-up

The canonical supplement is:

```text
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
```

Core rule:

> **Collaborator unavailability does not globally block ADS unless a specific accepted gate requires that collaborator before the next relevant boundary.**

Intended review must not silently become SOLO because the reviewer is unavailable.

The process distinguishes:

```text
Is review REQUIRED or OPTIONAL?

Before what boundary must it happen?
```

A required review must name a real gate. `NONE` is reserved for optional review.

Exact immutable review targets are mandatory for deferred review. A review of ancestor commit X does not automatically cover descendant Y.

One-by-one catch-up is the default. Related obligations may be batched in one model session only if each retains separate target identity, findings, corrections, and disposition.

If later work materially depends on an unreviewed result, it should remain reversible/provisional or the review gate should move earlier. If a late review changes an upstream result, downstream impact must be inspected.

Cross-thread dependency discovery is currently procedural rather than machine-readable. It is a future mechanization trigger, not a reason to create Specification 025 prematurely.

`docs/model_collaboration/REVIEW_INBOX.md` is a convenience routing view for pending obligations. Per-thread state and exact repository evidence remain authoritative.

---

## Resource proportionality

Collaboration quality must be considered together with time, context size, provider limits, and user burden.

Use expensive independent/comparative review selectively for genuinely high-impact work. Routine implementation under a frozen contract normally deserves a bounded direct review. Mechanical checks may remain deterministic or SOLO.

Model, effort level, and product surface are operational choices rather than permanent architecture. Collect evidence before institutionalizing model-specific defaults.

The first Claude collaboration trial demonstrated that repository-heavy review can consume scarce product usage quickly. This is a real scheduling/resource constraint, but exact percentages or current provider limits are not frozen into the method.

---

## Scheduled execution and API orchestration

Unattended scheduled model review is not part of the current method.

It was considered and deferred because it does not create extra weekly subscription capacity and adds unattended write/concurrency, clarification, and budget-consumption risks at a stage where manual triggering is already lightweight.

API orchestration is also deferred. It would add separately metered usage, repeated context transmission, credentials, retries/failure handling, and orchestration infrastructure.

Revisit either mechanism only when observed manual coordination cost, backlog scale, or product capabilities justify the added machinery.

---

## Interaction provenance

The accepted provider-neutral convention is defined in:

```text
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
```

Visible ChatGPT and Claude conversations use:

```text
NN - Main Topic / Stage
```

with provider-local repository session IDs such as:

```text
chatgpt-06
claude-01
```

The common human-facing project/workspace name is:

```text
Autonomous Data Science System
```

Provider/model identity is provenance, not authority.

---

## Knowledge reconciliation

Periodic reconciliation is required at meaningful stage boundaries such as:

- completion of a conceptual design phase;
- acceptance/failure of a major specification;
- major experiment completion;
- beginning a new prototype generation;
- major target-system architecture change;
- major development-method revision;
- or observed documentation/routing inconsistency.

A reconciliation should ask:

```text
Were durable insights promoted where appropriate?
Are VISION, PRINCIPLES, DECISIONS, and OPEN_QUESTIONS current?
Does KNOWLEDGE_MAP route to the right sources?
Is CURRENT_STATE concise and present-tense?
Are experiment/status details stored in the right ledgers?
Are checkpoint metadata and interaction provenance valid?
Are collaboration threads correctly resolved/deferred?
Are pending review obligations discoverable?
Are there contradictions or duplicated canonical statements?
Does MAJOR_CHANGES capture the significant structural evolution?
```

Reconciliation is periodic, not required after every checkpoint.

---

## Unplanned session-boundary recovery

The canonical recovery procedure lives in:

```text
docs/CONTINUITY.md
```

Important distinction:

```text
substantive preservation failure
    !=
routing/current-state reconciliation drift
```

If substantive artifacts already exist, the next session/model should reconstruct from repository authority, identify incomplete routing/canonical updates, and repair them conservatively rather than recreate missing conversation context from memory.

---

## Major structural changes

`docs/MAJOR_CHANGES.md` is the selective conceptual history for changes that materially alter:

```text
system-level vision
target architecture
prototype/evaluation architecture
development methodology
knowledge-preservation architecture
collaboration architecture
major experimental phase or frozen contract
repository structure affecting future work
```

Routine commits and typo fixes do not belong there.

---

## Real projects as system tests

ADS should be developed against heterogeneous real or realistic projects, not only abstract design.

Each project can test whether the system:

- understands the important data/project structure;
- asks the right questions before modelling;
- selects appropriate validation;
- detects leakage and invalid assumptions;
- activates relevant methodology;
- avoids unnecessary analysis;
- handles invalidation and repair;
- involves the human at useful points;
- preserves evidence and decisions;
- and produces reproducible outputs.

The project tests the quality of the process, not merely final model performance.

---

## System gap extraction

When work reveals a weakness, analyze:

```text
observed failure
    -> why did the current system/method miss it?
    -> project-specific or general?
    -> if general, what reusable capability should change?
    -> what future test can prevent regression?
```

Possible generalized improvements include new questions, rules, review triggers, evidence requirements, project-state features, validators, or method revisions.

Important Level-2 examples already include:

```text
Checkpoint 22
    durable knowledge was insufficiently promoted/discoverable
    -> Development Method v0.3

Checkpoint 100
    loose checkpoint metadata drifted
    -> v0.4 explicit metadata contract

MC-0001
    prose-only collaboration ownership and supposed blind review were insufficient
    -> Specification 024 + accepted multi-model governance

MC-0003
    asynchronous review needed explicit gate/target/catch-up semantics
    -> v0.5 deferred-review protocol
```

---

## Avoiding premature completeness and implementation

The project should not enumerate every possible data-science decision, collaboration edge case, or infrastructure component in advance.

Use the pattern:

```text
establish a strong core
    -> use it
    -> observe failure/inefficiency
    -> generalize the lesson
    -> add the smallest justified mechanism
```

Technology should follow clarified requirements rather than popularity or convenience.

---

## Deferred preservation/collaboration infrastructure

The repository-preservation foundation remains:

```text
Git
Markdown
explicit repository structure
small deterministic validators where earned
AI-assisted curation under normal governance
```

Potential future upgrades remain deferred until observed need, including:

```text
machine-generated indexes
semantic/hybrid repository retrieval
promotion queues
contradiction/staleness detection
dependency graphs
generated review inboxes
cross-thread dependency discovery
reconciliation assistants
provenance-aware conversation archives
stronger transactional/multi-writer collaboration controls
API-based orchestration
```

A small validator is not a rejection of minimalism when a repeatedly observed precise consistency requirement exists.

---

## Documentation should not become the project

Documentation and governance overhead must remain proportionate.

Prefer natural checkpoints over constant micro-updates.

Use collaboration threads only when collaboration is actually useful.

Use expensive review modes only when the decision importance justifies them.

If maintaining routing, metadata, review inboxes, or collaboration state becomes repetitive or inconsistent, treat that as evidence for bounded automation rather than adding machinery speculatively.

---

## Future automation of knowledge capture

A mature system may propose promotions, stale statements, contradictions, dependency impacts, or review obligations automatically.

Automatic extraction or detection must not imply automatic promotion into trusted authority.

The current project still uses human/AI judgment around acceptance because this continues to expose what good governance actually requires.

---

# Version history

## Version 0.5

**Introduced:** Checkpoint 204, 2026-08-26

Changes:

- promoted governed provider-neutral multi-model development after MC-0001 through MC-0003;
- retained SOLO work as a first-class mode and made collaboration selective/task-scoped;
- separated role from write scope and accepted one target-state writer plus declared secondary surfaces;
- accepted Specification 024's machine-readable collaboration-state coherence guard;
- formalized independent-first review using accepted pre-proposal refs and explicit exposure/contamination handling;
- formalized model-to-model repository messages and GitHub issue/PR transport without making either automatic authority;
- added disagreement classification/routing and preserved human authority for genuine project-intent/consequential choices;
- added deferred asynchronous review/catch-up with explicit review gates and exact immutable review targets;
- adopted provider-local interaction session IDs and a prospective provider-neutral checkpoint-provenance contract from Checkpoint 204 onward;
- explicitly deferred unattended scheduled model review and API orchestration;
- preserved known future triggers instead of opening Specification 025 prematurely: downstream thread dependencies, inbox consistency generation, and secondary-vs-secondary overlap when real use justifies them.

Detailed evidence:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/threads/MC-0001/RESOLUTION.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/model_collaboration/threads/MC-0002/RESOLUTION.md
docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md
docs/model_collaboration/threads/MC-0003/RESOLUTION.md
```

## Version 0.4

**Introduced:** Checkpoint 100, 2026-08-19  
**Contract strengthened and normalization closed:** Checkpoint 103, 2026-08-20

Changes:

- converted checkpoint metadata from a loose convention into an explicit mandatory minimum contract;
- introduced `docs/checkpoints/README.md` as the checkpoint-format specification;
- required a historical/authority metadata core;
- required ChatGPT session provenance for the then-single-provider development process;
- normalized legacy checkpoint metadata conservatively;
- strengthened `scripts/check_checkpoint_metadata.py` to detect drift mechanically.

The later multi-model migration is prospective and does not rewrite the historical v0.4 records.

## Version 0.3

**Introduced:** Checkpoint 76, 2026-08-18

Changes:

- added explicit promotion audits;
- introduced `KNOWLEDGE_MAP.md` routing;
- introduced periodic knowledge reconciliation;
- introduced lightweight authority/maturity/provenance metadata;
- separated concise current state from experiment-specific ledgers;
- introduced `MAJOR_CHANGES.md`;
- preserved more advanced knowledge infrastructure as deferred until observed need.

Detailed rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

## Version 0.2

**Introduced:** Checkpoint 2, 2026-08-08

Changes:

- made proactive checkpoint detection an explicit AI collaborator responsibility;
- based checkpoint timing on conceptual progress/continuity value rather than message count;
- clarified that preservation does not imply automatic promotion;
- made proactive design-chat rotation part of continuity management.

## Version 0.1

**Introduced:** Checkpoint 0, 2026-08-07

Initial method establishing fluid discussion, layered knowledge preservation, checkpoints, maturity distinctions, real-project testing, and explicit method evolution.