# Research 124: Scalable Repository Knowledge Architecture and Reconstruction Redesign

**Date:** 2026-09-12
**Status:** ACTIVE / PURPOSE AND REQUIREMENTS DISCOVERY / TARGET ARCHITECTURE NOT YET SELECTED
**Scope:** Redesign how ADS preserves, structures, reconstructs, retrieves, activates, validates, evolves and migrates project knowledge as the repository, project history, domains, workstreams and collaborating models grow substantially.
**Authority:** Active Level-2 architecture research. This record owns the redesign inquiry and preserves the project-owner mandate, research questions and emerging conceptual conclusions. It does not yet replace the current repository information architecture, continuity procedure, authority hierarchy or integrity contracts.
**Declared references:** `research:064`, `research:103`, `research:104`, `research:106`, `research:107`, `research:108`, `checkpoint:448`, `path:docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`, `path:docs/CONTINUITY.md`, `path:docs/DEVELOPMENT_METHOD.md`, `path:docs/KNOWLEDGE_MAP.md`

## 1. Stage opening and owner mandate

Research 123 is complete. The project owner explicitly selected the project-knowledge architecture as the next ADS stage rather than inferring a continuation from the previously paused Research 113, Source Vault, or AB-030 routes.

This stage has a deliberately broader optimization objective than earlier preservation refinements. The current architecture is evidence, migration cost and an operational continuity substrate. It is **not** a redesign constraint.

The owner explicitly authorizes a full redesign if evidence supports it:

```text
existing files may be retained, changed, merged, split, transformed or retired
existing artifact families may be retained, changed, replaced or migrated
large migration effort is acceptable when justified by long-term quality
sunk cost is not a reason to preserve a weak architecture
foreseeable scaling pressure is a valid design input
the design should be professional and robust for substantial future growth
```

This does not authorize accidental knowledge loss. Replacing a representation is different from discarding the understanding, provenance or evidence that representation currently carries.

The current architecture remains operationally authoritative until a successor has been selected, implemented, migrated and validated strongly enough to assume that role.

## 2. Start with purpose, not mechanisms

The first question of this research is deliberately not which files to create, whether to use a graph or vector database, or whether to improve the Knowledge Map. Those questions already assume a solution shape.

The first question is:

> **What is the project-knowledge architecture for? What outcome are we trying to achieve?**

A storage-first framing is too narrow. Git and Markdown can preserve large amounts of information while a new collaborator still fails to find, interpret, activate or correctly prioritize the knowledge needed for the current task.

The emerging purpose is therefore:

> **Turn an ever-growing project history into durable, usable, scalable project understanding across time, conversations, models and collaborators.**

A fuller working formulation is:

> **The purpose of the ADS project-knowledge architecture is to provide durable, scalable continuity of project understanding across time, conversations, models and collaborators. It must preserve accumulated knowledge, structure its authority and relationships, enable high-recall reconstruction and progressively deeper navigation, activate relevant knowledge when needed, preserve historical provenance without overwhelming current reasoning, and allow the project to grow substantially without requiring any individual reasoning context to contain or reread the entire project.**

This wording is provisional and should be tested during the requirements phase, but the distinction underneath it is already important:

> **The goal is not to preserve documents. The goal is to preserve and make reusable the project's accumulated understanding.**

Documents, indexes, graphs, databases, generated views and summaries are implementation mechanisms, not the objective.

## 3. Persistent cognitive infrastructure

The active reasoning agent is transient. One conversation ends; another starts with no guaranteed working memory of the first; another model may enter with different context; humans forget details; every model has finite context; project knowledge continues to accumulate.

A highly capable reasoning model can still behave poorly on a long-lived project if it repeatedly loses long-term context, cannot locate the right evidence, cannot distinguish current authority from historical thought, or does not know that relevant knowledge exists.

The architecture can therefore be understood as persistent **project memory, navigation, epistemic structure and continuity infrastructure** around transient reasoning systems.

```text
session A
    -> project gains knowledge
    -> durable knowledge architecture
    -> future session / different model
    -> reconstructs relevant project understanding
    -> continues intelligently
```

The better this layer becomes, the less project intelligence remains trapped inside a single conversation.

## 4. Four capability layers

The opening discussion distinguishes at least four different problems.

### 4.1 Durability

```text
Can the knowledge survive?
```

Important understanding must survive conversation loss, model changes, terminal loss, time and personnel changes.

### 4.2 Reconstruction and discoverability

```text
Can another intelligence recover the necessary understanding?
```

A fresh collaborator should be able to build a strong model of the project without depending on the previous conversation or a human-maintained giant continuation prompt.

### 4.3 Cognitive activation

```text
Does the right knowledge enter reasoning when it matters?
```

Stored and even discoverable knowledge is insufficient if the collaborator does not know that it needs to retrieve or consume the governing source before acting. AB-022 is the concrete failure case: the correct restart procedure existed and was linked, but it was not consumed before consequential guidance was produced.

### 4.4 Abstraction and synthesis

```text
Can useful understanding scale much better than raw information volume?
```

An unlimited archive is not automatically a useful memory. A mature system should preserve raw evidence while also supporting higher-level synthesis and progressively deeper drill-down.

```text
raw history
    -> structured evidence
    -> current synthesis
    -> broad project understanding
```

with traceability downward whenever exact evidence is needed.

## 5. Core scaling principle

A central requirement is:

> **As the quantity of project information grows, the cost of acquiring sufficient project understanding should not grow proportionally with it.**

If ADS grows to ten times its current knowledge volume and every new session requires ten times as much reading/context, the architecture has not solved the scaling problem.

This rules out two simplistic optimization targets:

```text
read everything
    not scalable and may harm context quality

read the bare minimum
    can omit important governing, adjacent or latent knowledge
```

The target is **maximum useful, authority-aware understanding under finite context**.

## 6. One stable repository-native entry

The project owner should not have to act as the project's memory router. A mature architecture should make a request such as `Continue ADS.` sufficient to start repository-native reconstruction.

Target behavior:

```text
one stable repository entry
    -> project explains how to reconstruct itself
    -> broad orientation
    -> current live state and active route
    -> relevant domains
    -> active domain and governing authority
    -> unresolved obligations and known weaknesses
    -> deeper evidence on demand
    -> reconstruction / coverage verification
```

The entry mechanism is not assumed to be Markdown. It may eventually be a document, manifest, generated router, executable protocol, database-backed index or hybrid. That decision belongs later in this research.

The current copy-pasted continuation prompt is therefore a migration-era convenience, not an intended permanent dependency.

## 7. Hierarchical breadth before depth

Literal exhaustive reading is not the goal, but a fresh persistent collaborator should obtain much more than a narrow next-action slice. The owner specifically wants broad project understanding followed by domain-specific depth.

A promising abstract pattern is:

```text
project-level orientation
    -> durable major domains
        -> selected domain synthesis
            -> subdomain / active workstream
                -> governing current sources
                    -> exact evidence and history when needed
```

For example, a collaborator entering Project Cockpit work should first understand ADS at project level, then Cockpit as a domain, then the relevant Cockpit subdomain, then its accepted decisions/specifications/evidence.

This is a research direction, not a frozen file hierarchy.

## 8. Authority, epistemic state and relationships

More stored information can make reasoning worse if the system cannot distinguish current accepted architecture, current live state, accepted decision, working hypothesis, research candidate, rejected approach, superseded result, historical provenance, raw evidence, open question, known limitation and deferred capability.

The successor architecture must make authority, chronology, supersession and current-vs-historical status sufficiently explicit for humans and models.

It should also preserve relationships, not merely documents:

```text
decision came from research
specification implements a decision
validation tested a specification
one route paused another
one conclusion superseded another
one known limitation has a reopen trigger
one workstream depends on another
one completed child route resumes a parent
```

The appropriate technical representation remains open.

## 9. Preserve the redesign while redesigning preservation

This research may span multiple long conversations. Losing the reasoning used to design the successor would directly violate the objective being studied.

The stage therefore adopts this transition invariant:

```text
CURRENT ARCHITECTURE
    remains operational continuity authority

NEW ARCHITECTURE RESEARCH
    is continuously preserved inside it

CANDIDATE SUCCESSOR
    is designed, prototyped and stress-tested

MIGRATION
    preserves meaning, provenance and authority

AUTHORITY SWITCH
    occurs only after successor reconstruction is reliable

OLD ARCHITECTURE
    may then be retired, reduced or archive-mapped
```

Do not dismantle the existing continuity bridge while the project still depends on it.

Preservation should occur at meaningful conceptual milestones rather than waiting for chat rotation or trying to archive every sentence. Exploratory reasoning should be distilled into durable research knowledge; accepted results should later be promoted into stronger authority layers.

## 10. Primary evidence and open architecture gaps

Research 124 treats these backlog items as primary requirements/evidence:

```text
AB-022  governing operational authority can exist but remain unread/unactivated
AB-023  deferred architecture knowledge itself may be hard to surface at the right time
AB-024  high-recall reconstruction and hierarchical traversal
AB-025  nested workstream graph / active route stack / deterministic resume
AB-026  Knowledge Map saturation and retrieval usability
AB-027  known limitations, deferred upgrades and evolution triggers
```

They are not predetermined solutions.

Foundation 014 and Research 064/103/104 also matter because they preserve previously deferred stronger mechanisms and the conditions under which they should be reconsidered. Earlier deferrals were scope- and evidence-dependent, not permanent prohibitions.

## 11. Architecture space is fully reopened

This research must seriously compare, rather than prematurely select:

```text
richer structured per-artifact metadata
generated structural and semantic indexes
one canonical bootstrap/router
hierarchical project/domain/subdomain guides
authority / supersession / dependency graph
workstream DAG plus explicit active stack
reconstruction planner and reconstruction receipt
known-risk / evolution-trigger register
Git-authoritative source plus rebuildable indexed database
lexical + semantic + vector hybrid retrieval
generated synthesis / promoted summaries
graph database vs static graph vs SQLite vs files + generated views
incremental reconciliation and validation
context-budget-aware retrieval planning
```

A database, graph or vector layer must not become a second accidental source of truth merely because it improves retrieval. Source-of-truth versus derived/rebuildable representation is a first-class design question.

## 12. Initial research questions

The initial question set includes:

1. What is the long-term purpose and success definition of the architecture?
2. Which capabilities are required to achieve that purpose?
3. What failure modes would demonstrate that the architecture is not achieving it?
4. Which current artifact families should remain, merge, split, transform or retire?
5. What should be canonical source truth versus generated/rebuildable view?
6. What should a fresh collaborator read or traverse first?
7. How should broad project awareness be obtained without reading every file?
8. How should domain-specific depth be activated efficiently?
9. How should current truth, synthesis, rationale, evidence and history relate?
10. How should supersession, contradiction, staleness and repair be represented?
11. How should latent known weaknesses and reconsideration triggers surface before rediscovery?
12. How should nested workstreams, dependencies and deterministic resume semantics work?
13. What metadata should be universal, family-specific, generated or absent?
14. What role should an explicit graph/DAG play?
15. What role should lexical, semantic, vector or hybrid retrieval play?
16. How should topic saturation and hierarchy be managed?
17. How can reconstruction completeness and missed-governing-artifact risk be measured?
18. How should synthesis remain subordinate and traceable to sources?
19. How can a large migration preserve provenance and avoid semantic loss?
20. Which integrity mechanisms are required for generated or machine-routed knowledge?
21. How should the private companion participate without becoming a second development authority?
22. Does the architecture remain usable and maintainable at 5x and 10x current scale?
23. Can the architecture preserve and continue a major redesign of itself across conversation boundaries?

## 13. Evaluation dimensions

Candidate architectures should be compared on reconstruction recall, authority clarity, retrieval precision, context efficiency, broad-project orientation, domain-depth navigation, cognitive activation reliability, supersession/staleness safety, dependency/resume reliability, known-risk discoverability, human and AI maintainability, mechanical verifiability, generated-view drift risk, migration safety, historical provenance, public/private integrity, human readability, tool/provider portability, 5x/10x scale behavior and operational complexity.

## 14. Failure model to audit

The inventory/requirements phase should explicitly seek:

```text
knowledge durable but not discovered
knowledge discovered but not consumed
wrong authority selected
stale or superseded content used
known warning preserved but not activated
nested route / resume target lost
topic or index saturation
context overflow
duplicate or contradictory truth
private/public continuity mismatch
multiple-model concurrency ambiguity
interruption/recovery ambiguity
generated view drifting from canonical sources
derived index not rebuildable
semantic retrieval false negatives or false positives
maintenance burden growing too quickly
```

## 15. Research sequence

Do not begin by merely improving `KNOWLEDGE_MAP.md` or `CONTINUITY.md`.

The planned sequence is:

```text
A. whole-repository architecture and artifact inventory
B. failure-mode and scaling-pressure inventory
C. purpose, requirements and invariants
D. multiple candidate architecture families, including stronger deferred options
E. independent multi-model counter-design
F. comparative evaluation using concrete reconstruction / stress scenarios
G. selected target architecture
H. migration and compatibility design
I. prototype, validators and measurable qualification
J. staged migration only after acceptance
```

The first substantive audit should quantify and classify the current repository knowledge system: artifact families, sizes/growth, routing/index surfaces, metadata, typed references, source-vs-derived relations, current/historical/superseded representation, duplication, domain fan-out, workstream representation, deferred-trigger locations, private/public links, reconstruction path, validators and historical failure cases.

## 16. Multi-model review

A later architecture-design phase should reuse the independent-first collaboration pattern that worked for MC-0008:

```text
independent challenger proposal before exposure
    -> primary candidate
    -> comparative review
    -> final reconciliation
```

The independent model should receive a neutral requirements/evidence brief rather than a prompt that presupposes the current architecture or ChatGPT's preferred design.

## 17. Current non-decisions

Research 124 has **not** yet selected a graph database, vector database, semantic index, universal metadata schema, new checkpoint system, replacement for research/specification files, domain-guide format, generated catalog, bootstrap executable, workstream-DAG implementation or migration plan.

## 18. Immediate next boundary

The next research boundary is a neutral whole-repository knowledge-architecture inventory and failure/scale-pressure audit, followed by a requirements/invariants brief.

No target architecture should be frozen until that evidence is available.

```text
RESEARCH124=ACTIVE
PURPOSE_FIRST=true
CURRENT_ARCHITECTURE=OPERATIONAL_AUTHORITY_DURING_REDESIGN
FULL_REDESIGN_ALLOWED=true
SUNK_COST_CONSTRAINT=false
READ_EVERYTHING_TARGET=false
BARE_MINIMUM_TARGET=false
TARGET=MAXIMUM_USEFUL_AUTHORITY_AWARE_UNDERSTANDING
ONE_REPOSITORY_NATIVE_ENTRY=REQUIREMENT
TARGET_ARCHITECTURE=NOT_SELECTED
AB022_027=PRIMARY_INPUTS
RESEARCH113=PAUSED
SOURCE_VAULT=PAUSED
AB030=PARKED
NEXT=WHOLE_REPOSITORY_KNOWLEDGE_ARCHITECTURE_INVENTORY
```