# Research 124: Scalable Repository Knowledge Architecture and Reconstruction Redesign

**Date:** 2026-09-12
**Status:** ACTIVE / PHASE B COMPLETE / POST-PHASE-B WEAKNESSES CAPTURED / FOUNDATIONAL CLAUDE DIALOGUE NEXT / TARGET ARCHITECTURE DESIGN PAUSED
**Scope:** Redesign how the ADS project preserves, structures, reconstructs, retrieves, activates, validates, evolves and migrates project-development knowledge as the repository, project history, domains, workstreams and collaborating models grow substantially. This is project-support infrastructure around ADS development, not the architecture of the Autonomous Data Science System product itself.
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

> **The purpose of the project-development knowledge architecture supporting the ADS project is to provide durable, scalable continuity of project understanding across time, conversations, models and collaborators. It must preserve accumulated knowledge, structure its authority and relationships, enable high-recall reconstruction and progressively deeper navigation, activate relevant knowledge when needed, preserve historical provenance without overwhelming current reasoning, and allow the project to grow substantially without requiring any individual reasoning context to contain or reread the entire project.**

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

## 18. Phase A baseline inventory method

The first whole-repository audit was intentionally descriptive. It measured the current information architecture before proposing a successor.

The inventory used the tracked working tree and repository-owned validators to measure:

```text
repository and documentation volume
artifact-family counts and sizes
Git/change velocity
mandatory reconstruction read cost
live-state document growth
Knowledge Map fan-out and overlap
machine-readable routing and metadata coverage
specialized domain navigation surfaces
validator guarantees and blind spots
branch/workstream signals
backlog and open-question load
```

These measurements are a baseline snapshot around Checkpoint 449. They are not permanent thresholds and they do not by themselves prescribe a target architecture.

## 19. Repository scale and growth pressure

At the Checkpoint 449 baseline the repository contains:

```text
tracked files                         1,499
tracked bytes                         17,635,353
docs/ files                             963
Markdown files                          986
Markdown bytes                        9,163,256
Git commits                            2,411
local branches                              7
remote branches                            59
```

The repository began on 2026-08-07 and reached this baseline on 2026-09-12. Commit activity was highly concentrated on some development days, including 361 commits on 2026-08-27, 265 on 2026-08-26, 243 on 2026-08-28 and 207 on 2026-08-20. The important signal is not that this velocity will remain constant. It is that knowledge volume and chronology can expand much faster than a manually curated navigation surface might assume.

The documentation tree is already dominated by historical/evidence families:

```text
checkpoints             452 files     about 2.90 MB
research                143 files     about 2.56 MB
local_execution         213 files     about 1.34 MB
model_collaboration      71 files     about 0.64 MB
foundations               25 files     about 0.56 MB
specifications            27 files     about 0.53 MB
```

The numbered durable families contain:

```text
Foundations               24
Specifications            27
Research records         124
Numbered checkpoints     450
```

Checkpoint production itself has reached dozens of records on individual days. For example, 34 checkpoints were dated 2026-09-07 and another 34 were dated 2026-09-09. Research also had bursts such as 28 records dated 2026-08-27. This makes chronology durable, but it also means that chronology cannot be the primary reconstruction mechanism at larger scale.

## 20. Raw-document scale and concentration

The 986 Markdown files have a median size of about 6.5 KB and a median length of about 173 lines. The upper tail is much larger:

```text
P90 size        about 17.0 KB
P95 size        about 23.9 KB
P99 size        about 42.3 KB
maximum         about 254.6 KB
```

Several important navigation/state/research surfaces are individually large:

```text
Research 122                    about 254.6 KB
CURRENT_STATE.md                about 222.9 KB
Research 123                    about 208.9 KB
OPEN_ARCHITECTURE_BACKLOG.md    about 115.7 KB
Research 117                     about 72.5 KB
Research 037                     about 64.8 KB
KNOWLEDGE_MAP.md                 about 59.0 KB
DECISIONS.md                     about 46.5 KB
```

This matters because the architecture cannot assume that a file is cheap to consume merely because it is a navigation or current-state artifact.

## 21. Mandatory bootstrap cost is already substantial

The current continuity contract directly requires these six bootstrap reads before deeper task-specific traversal:

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

At the baseline snapshot they total approximately:

```text
325,489 bytes
324,505 characters
```

A crude characters-divided-by-four proxy is about 81,000 tokens. This is **not** a tokenizer measurement and should not be treated as an exact model-context cost. It is sufficient, however, to show the order of magnitude and the direction of travel.

Most of that cost comes from two files:

```text
CURRENT_STATE.md      about 222.9 KB
KNOWLEDGE_MAP.md       about 59.0 KB
```

The mandatory bootstrap therefore consumes a large amount of context before the collaborator reads the governing research, specification, operational procedure, domain guide, private complement or exact evidence required by the active task.

This is direct evidence for the scaling principle established in Section 5. The current reconstruction cost is already coupled too strongly to accumulated repository history.

## 22. CURRENT_STATE has accumulated historical burden

`docs/README.md` defines `CURRENT_STATE.md` as the sole human-readable owner of live state and says it should remain present-tense and relatively concise, with older reasoning moved out once historical.

The baseline file is approximately 222.9 KB and contains 102 explicit `Checkpoint NNN` historical paragraphs, spanning many boundaries from the current stage back into earlier work. Its structure includes extensive investigation/history sections before the continuation boundary.

This does not mean the historical material is unimportant. It means the **representation has drifted from its stated single responsibility**:

```text
intended role
    current human-readable state and next boundary

observed accumulated role
    current state + long historical synthesis + continuity evidence + many checkpoint summaries
```

That drift increases cold-start context cost and creates duplication with checkpoints, research records and history surfaces. A successor architecture should preserve the useful synthesis while separating live state from historical accumulation more reliably.

## 23. Knowledge Map saturation is now measured

The current Knowledge Map has 19 validated topic IDs. Using the same route-normalization logic as the repository validator, the map currently contains approximately 602 route entries covering 467 unique routed paths.

Fan-out is extremely uneven. The largest topic is:

```text
development-governance     293 direct routed paths
```

The next largest topics are only in the twenties:

```text
work-unit-visual-grammar    27
conversation-workspace      25
canonical-history           23
cockpit-provenance          22
recommendation-action       21
```

The `development-governance` topic mixes large numbers of checkpoints, local-execution records, research records, specifications, collaboration material and core documents. This turns AB-026 from a hypothetical concern into an observed saturation signal.

The map also legitimately routes some artifacts into multiple topics. There are hundreds of route entries for fewer unique paths, and several central documents appear in many semantic neighborhoods. Cross-topic membership is useful, but the current flat representation gives no machine-readable distinction between:

```text
read-first governing source
current synthesis
supporting evidence
historical provenance
optional deep evidence
```

The existing validator proves exhaustive coverage and path validity. It does **not** prove retrieval usability, semantic coherence, authority ranking or successful consumption of the governing source.

Therefore:

> **Coverage completeness is not retrieval usability.**

## 24. Current routing is compact but cannot represent nested continuation

`docs/current_routing.json` is intentionally compact and currently contains only the live checkpoint, active branch/PR, promoted integration branch/SHA, latest specification/outcome and one `current_boundary`.

That compactness is useful, but it does not encode:

```text
parent workstream
child workstream
active breadcrumb / stack
why a side route opened
pause reason
blocking dependency
return condition
exact resume target
multiple dependency edges
```

Those relationships currently live mainly in prose, checkpoints and human interpretation. This is direct support for AB-025: chronology and one flat current pointer are not equivalent to an explicit continuation/control-flow model.

## 25. Machine-readable relationship coverage remains sparse

The repository has introduced stronger prospective metadata, but it is not a project-wide knowledge graph.

At the baseline, explicit `Declared references` metadata appears in only a small portion of the numbered families:

```text
Foundations          0 / 24
Specifications       3 / 27
Research            14 / 124
Checkpoints           0 / 450
```

This is consistent with the deliberate prospective cutover introduced by the integrity-hardening work. It was never intended as a mass legacy rewrite.

Other machine-readable knowledge surfaces are specialized rather than global, including current routing, Cockpit manifests, model-collaboration thread state, GitHub inventories and Source Universe manifests. There is no general repository-wide machine representation of authority, supersession, dependency, semantic domain, workstream control flow and synthesis/source relationships.

This is not automatically a defect. It identifies the current boundary that stronger candidate architectures must be compared against.

## 26. Specialized domain guides show a useful pattern and a maintenance warning

The repository already contains several specialized navigation surfaces. The strongest example is `docs/cockpit/README.md`, which preserves:

```text
status and authority
pause boundary
exact resume anchor
human-confirmed state
required reading order
artifact roles
provenance and fidelity gates
resume rule
```

`docs/local_execution/README.md`, `docs/model_collaboration/README.md` and the methodological-knowledge coverage map provide similar domain-specific routing for their own scopes.

This is evidence that **hierarchical project -> domain -> evidence navigation is useful in practice**. It does not establish that manually maintained README files are the correct long-term implementation. The redesign should separate the useful semantic pattern from its current storage format and maintenance burden.

## 27. Structural validators are strong but cognitive correctness is largely untested

The repository has earned meaningful deterministic integrity protections. Current validators can prove, among other things:

```text
numbered-family identity and metadata contracts
checkpoint metadata completeness
Knowledge Map topic and route coverage
routed-path existence
current-routing schema and checkpoint freshness
model-collaboration state coherence
selected typed reference validity
```

The formal aggregate public gate passes when run in the repository's managed Python environment.

However, these validators mostly answer structural questions. They do not yet measure whether a fresh collaborator:

```text
formed an adequate broad project model
selected the correct authority among several candidates
noticed a relevant known weakness
consumed the governing operational procedure before giving instructions
understood the active parent/child workstream chain
avoided stale or superseded synthesis
used an appropriate amount of context
could explain what important knowledge remained unread
```

The AB-022 restart-order failure demonstrates this gap concretely. The successor architecture therefore needs qualification scenarios for **reconstruction and activation quality**, not only repository consistency.

## 28. Baseline interpretation against the four capability layers

The current architecture is strongest at **durability**. Git, numbered evidence families, checkpoints and integrity gates preserve a great deal of history and make accidental disappearance increasingly visible.

It is materially stronger than an unstructured document archive at **discoverability and reconstruction**, because it has structural guides, current state, semantic routing, domain indexes and explicit continuity procedures. But the measured bootstrap cost, topic saturation and live-state accumulation show that the current strategy is becoming expensive to consume.

The weakest measured layer is **cognitive activation**. The repository can contain and route the correct authority without guaranteeing that a collaborator consumes it before reasoning or acting.

**Abstraction and synthesis** exist, but their lifecycle is largely manual and their boundaries are not yet strong enough to prevent synthesized live-state/navigation artifacts from growing with history.

The baseline therefore supports this provisional diagnosis:

```text
durability                  STRONG
structural integrity        STRONG
basic discoverability       STRONG BUT SCALING
high-recall reconstruction  PARTIAL
context efficiency          UNDER PRESSURE
hierarchical traversal      PARTIAL / DOMAIN-SPECIFIC
relationship semantics      PARTIAL
nested resume semantics     WEAK / PROSE-HEAVY
cognitive activation        WEAKLY VERIFIED
synthesis lifecycle         PARTIAL / MANUAL
```

These are research classifications, not final scores.

## 29. Previously deferred escalation triggers are now partly observed

Foundation 014 and Research 064/103/104 deliberately deferred stronger machinery until real pressure appeared. The current audit shows that several of those trigger classes are no longer merely theoretical:

```text
frequent discoverability/activation failure
    observed through AB-022 and related operational misses

manual/global navigation saturation
    observed in the 293-path development-governance topic

reconstruction read cost growth
    observed in the roughly 325 KB mandatory bootstrap

prose-heavy dependency/resume structure
    observed in flat current routing plus nested workstream history

large reconciliation surfaces
    observed in CURRENT_STATE, backlog, Knowledge Map and checkpoint accumulation
```

This does **not** prove that a graph database, vector database or any other specific stronger mechanism is now correct. It does prove that those options should no longer be dismissed merely because earlier research deferred them.

## 30. Phase A conclusions and next boundary

The baseline audit changes the research from a general concern into a measured scaling problem.

The current architecture has succeeded at something important: it has preserved enough project knowledge and provenance that this redesign can reconstruct why earlier choices were made. The problem is not that the system failed completely. The problem is that the successful accumulation of knowledge is itself creating reconstruction, routing and activation costs that the current representation does not scale away.

The next phase should therefore convert the purpose, failure model and measured baseline into explicit **requirements and invariants** before architecture candidates are designed.

The requirements phase should answer questions such as:

```text
what every fresh collaborator must know at project level
what can remain latent until a domain/task activates it
what must be machine-resolvable before consequential action
what authority/supersession semantics must be explicit
what reconstruction coverage must be measurable
what context-budget behavior is acceptable
what must remain Git-authoritative and rebuildable
what historical provenance may be compressed but never lost
what workstream/resume semantics must be deterministic
what generated views may exist and how drift is prevented
what 5x and 10x scale targets the architecture must satisfy
```

No target architecture is selected by Phase A.

```text
RESEARCH124=ACTIVE
PHASE_A_BASELINE_INVENTORY=COMPLETE
MEASURED_BOOTSTRAP_PRESSURE=OBSERVED
KNOWLEDGE_MAP_SATURATION=OBSERVED
CURRENT_STATE_ACCUMULATION=OBSERVED
NESTED_ROUTING_GAP=OBSERVED
COGNITIVE_ACTIVATION_GAP=OBSERVED
STRONGER_ARCHITECTURE_OPTIONS=REOPENED_FOR_COMPARISON
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REQUIREMENTS_AND_INVARIANTS
```

## 31. Phase B requirements method

Phase B converts the purpose statement, measured baseline and historical failure evidence into architecture-neutral acceptance requirements before any candidate mechanism is preferred.

The requirements below deliberately avoid assuming that the successor is Markdown-based, graph-based, database-backed, vector-backed or file-only. They state properties the system must provide. A later candidate may satisfy a requirement through source metadata, generated views, an executable router, a graph, a database, deterministic rules, semantic retrieval or a combination.

Requirements are divided into four classes:

```text
functional continuity
    what a fresh collaborator must be able to reconstruct and do

epistemic and authority safety
    how current truth, evidence, conflict and provenance must behave

scale and maintainability
    how cost must behave as the project grows

qualification and transition safety
    how the architecture proves that it works and how it may replace the current system
```

Unless explicitly marked as a comparative preference, the `KA-R` requirements below are acceptance requirements. The later design phase may refine exact thresholds and measurement instruments, but it may not silently remove a requirement merely because one candidate architecture has difficulty satisfying it.

## 32. Reconstruction activation tiers

High-recall reconstruction does not mean loading every durable artifact into every context. Phase B freezes a three-tier activation model at the semantic level.

### Tier A: project orientation

A fresh collaborator must obtain enough project-wide understanding to reason safely before entering narrow task depth. The project-orientation layer must cover at least:

```text
project identity and purpose
current project stage and live boundary
current authority model and conflict-resolution principle
major durable project domains
active workstream and its parent objective
important globally active obligations / blocks / uncertainties
current verification or epistemic boundary
existence and status of relevant private continuity surfaces
```

The orientation may summarize these facts. It does not need to load the detailed evidence behind each fact immediately.

### Tier B: task and domain activation

Once the current task or domain is known, the architecture must activate the domain synthesis and the governing sources needed for that task, including relevant known risks, open questions, constraints, operational procedures, specifications and active dependencies.

### Tier C: evidence and provenance drill-down

Detailed checkpoints, validation records, raw experiment evidence, Git chronology, historical alternatives and deeper rationale may remain latent until required for verification, conflict resolution, explanation or a consequential decision.

The tiers are semantic obligations, not a frozen file hierarchy. A candidate may implement them differently, but it must preserve the broad-to-deep behavior.

## 33. Functional continuity requirements

### KA-R01: persistent project understanding

The architecture must preserve and make reusable the project's accumulated understanding, not merely retain document bytes. Durable knowledge must survive conversation loss, model changes, human memory loss and ordinary environment restarts.

### KA-R02: repository-native bootstrap

One stable project entry must be sufficient to initiate reconstruction. A human-maintained continuation prompt containing a growing list of files, checkpoint numbers or hidden chat context must not be required for normal continuation.

### KA-R03: conversation and model independence

No material current project fact, accepted rationale, active route, unresolved obligation or migration-critical knowledge may exist only in one conversation, one model's memory or one provider-specific hidden memory surface.

### KA-R04: broad project orientation

A fresh collaborator must reconstruct the Tier-A orientation set before narrow consequential work. Passing directly from one live pointer to one next action without broader project/domain orientation is insufficient.

### KA-R05: progressive disclosure

The architecture must support progressively deeper traversal from project orientation to domain, subdomain/workstream, governing source and exact evidence without requiring whole-corpus reading.

### KA-R06: active route reconstruction

The complete active continuation chain must be reconstructable, including the current workstream, parent objective, why the current route exists and what higher-level work resumes after it closes.

### KA-R07: high-recall relevant discovery

A collaborator must be able to discover governing, adjacent and risk-bearing knowledge relevant to a task without already knowing exact filenames, artifact numbers or the prior conversation's search terms.

### KA-R08: reconstruction receipt

A reconstruction must be observable enough to report what project/domain/task surfaces were traversed, which governing sources were activated, which important areas remained latent or unavailable, and which uncertainties remain unresolved. The receipt is evidence of traversal, not proof that a model semantically understood every source.

### KA-R09: consequential-action authority preflight

Before consequential guidance or action, the architecture must resolve the task-relevant governing authority and make its consumption observable. If the required authority cannot be resolved or consumed, the system must fail visibly rather than proceed from memory or plausible inference.

Consequential contexts include at least:

```text
ordered or safety-sensitive operational procedures
repository / host / external-system mutations
security, credential, trust or authority changes
destructive or difficult-to-reverse actions
acceptance, promotion or authority-switch decisions
scientific or experiment conclusions
migration steps that can retire or transform authoritative knowledge
```

For AB-022-style cases, it is not sufficient that the runbook exists or is linked somewhere. The architecture must cause the relevant governing procedure to enter the reasoning path before exact instructions are produced.

### KA-R10: known-risk and evolution-trigger activation

Known limitations, deferred upgrades, reopen triggers and previously observed failure conditions must be activatable when the current task or observed condition intersects them. The architecture must not depend on a human remembering that such a warning exists.

### KA-R11: uncertainty visibility

When required authority is unavailable, evidence conflicts, private state is required but not verified, or the reconstruction cannot establish a necessary relationship, the uncertainty must be explicit. The system must not convert missing resolution into a confident guess.

## 34. Authority, relationship and epistemic requirements

### KA-R12: explicit epistemic role

The architecture must distinguish at least the following semantic roles when they matter:

```text
current accepted architecture / canonical truth
live project state
accepted decision
frozen specification or contract
current synthesis
research candidate / hypothesis
rejected approach
superseded material
historical provenance
raw evidence / validation result
open question
known limitation / deferred capability
```

A candidate does not need one universal schema for every artifact, but the system must be able to resolve these distinctions reliably enough for reconstruction and action.

### KA-R13: explicit authority resolution

Authority must be resolved using governed role, scope, status, chronology and supersession semantics. Recency alone, directory position alone, semantic similarity alone or model confidence alone may not determine current truth.

### KA-R14: supersession and conflict visibility

Explicit supersession must be machine-resolvable where the project has declared it. If two apparently authoritative claims remain incompatible after normal authority rules, the conflict must surface as unresolved rather than being silently blended.

### KA-R15: relationship semantics

The architecture must support explicit representation of relationships that materially affect understanding or continuation, including at least:

```text
derived-from / supported-by
implements / governed-by
tested-by / validated-by
supersedes / superseded-by
depends-on / blocks
opened-from / returns-to
paused-by / resumes-when
synthesis-of / evidence-for
known-risk / reopen-trigger
```

Not every prose mention must become an edge. The requirement is that relationships whose semantics matter to reasoning can be declared and queried without heuristic prose scraping.

### KA-R16: current state and history separation

The architecture must preserve historical depth without requiring current-state surfaces to grow monotonically with all history. Current state, historical chronology and deep evidence must remain distinguishable even if a candidate presents them through generated views.

### KA-R17: loss-aware synthesis

The architecture may compress detailed knowledge into summaries or syntheses, but compression must not silently delete unique accepted rationale, evidence, uncertainty or provenance. Higher abstraction must retain a route downward to the source material from which it derives.

### KA-R18: synthesis traceability

Material claims in promoted or generated synthesis must be traceable to authoritative source artifacts or governed evidence. A synthesis that cannot explain its source basis cannot silently become stronger authority than those sources.

## 35. Source-of-truth and derived-representation requirements

### KA-R19: one explicit project-development authority

ADS must retain one explicit project-development authority. During this redesign that authority remains the public ADS repository. A future governance change would have to be explicit and separately accepted; no candidate may create an accidental competing authority merely by adding a database, graph or index.

### KA-R20: authoritative versus derived classification

Every new knowledge store or view introduced by a candidate must have an explicit authority class. In particular, generated indexes, embeddings, caches, graph projections, search databases and reconstruction plans must not be mistaken for source truth unless the design intentionally promotes them through a governed authority change.

### KA-R21: rebuildable derived state

Derived representations must be reproducible from durable authoritative inputs plus versioned generation logic/configuration where reproduction is part of the design. Loss of a derived index must not destroy unique project truth.

### KA-R22: durable promotion of unique synthesis

If a generated synthesis contains unique accepted human/model reasoning that the project intends to preserve, that synthesis itself must be promoted onto a durable authoritative surface. It may not remain unique only inside an ephemeral cache, vector store or model response.

### KA-R23: freshness and source binding

A derived representation used for reconstruction must expose enough source identity or revision information to detect stale material. The architecture must not present an old generated view as current merely because its backing service still responds.

### KA-R24: probabilistic retrieval is not sole safety authority

Semantic or vector retrieval may improve recall, but a probabilistic retrieval result alone may not be the sole mechanism for satisfying consequential-action authority preflight. High-consequence required authority needs a deterministic or otherwise verifiable resolution path, or a fail-visible result when none can be established.

## 36. Workstream and continuation requirements

### KA-R25: deterministic workstream state

Active, paused, blocked, completed and superseded workstreams must be distinguishable without reconstructing control flow from chronological prose.

### KA-R26: explicit pause and return semantics

Every deliberately paused route that remains expected to resume must be able to express:

```text
why it paused
what condition or dependency permits return
what exact or typed target resumes
what parent objective it belongs to
```

A simple `PAUSED` label without return semantics is insufficient for long-lived nested work.

### KA-R27: multiple dependencies

The continuation model must support multiple dependency edges where real project work requires them. The design must not force a strict tree if the project state is naturally DAG-like.

### KA-R28: interruption recovery

After abnormal interruption during a multi-step transition, the architecture must support reconstruction of intended versus durably completed work from repository state and action evidence. It must not require blind replay of the previous conversation plan.

### KA-R29: concurrent collaborator safety

When multiple humans/models/tools operate on related knowledge, stale or conflicting updates to live state, authority relationships or generated routing must be detectable. The exact concurrency mechanism is a design question, but silent last-writer-wins corruption of project understanding is not acceptable.

## 37. Scale and maintainability requirements

### KA-R30: fixed-budget reconstruction discipline

Candidate qualification must use a predeclared context/read budget for core reconstruction scenarios. The exact budget will be calibrated before comparative testing, but candidates may not obtain better recall simply by consuming an unbounded fraction of the repository.

### KA-R31: sublinear cold-start growth target

Required cold-start cost must not be structurally proportional to total historical corpus size. At 5x and 10x corpus scale, the project-orientation layer should remain within the same order of magnitude and, for the frozen stress tests, within the same predeclared core context budget unless a scenario intentionally adds new active-domain evidence.

### KA-R32: bounded mandatory core

No mandatory bootstrap artifact or mandatory bootstrap set may be designed to accumulate all project history linearly. Historical growth must be pushed behind progressively deeper traversal or generated bounded synthesis.

### KA-R33: bounded marginal maintenance

Adding an ordinary new knowledge artifact should require only local/bounded semantic maintenance or automatically generated global views. It must not require manually editing a growing number of unrelated global catalogs merely to keep the architecture coherent.

### KA-R34: saturation observability

The architecture must expose measurable signals for overloaded routing/index surfaces, such as fan-out, ambiguity, stale synthesis, retrieval miss rates or context pressure, before usability degradation becomes catastrophic.

### KA-R35: human and model usability

Core authority and navigation semantics must remain inspectable by humans as well as machine-consumable. A candidate may use databases or generated structures, but the project must not become understandable only through one opaque service.

### KA-R36: provider and tool portability

Core continuity must not depend on proprietary hidden memory belonging to one model/provider. Different capable collaborators must be able to reconstruct the project from durable project-controlled state using the supported access mechanisms available to them.

## 38. Public/private requirements

### KA-R37: explicit public/private authority boundary

The private companion may be authoritative for explicitly delegated private continuity facts, but it may not silently redefine public ADS development state. Public `RESOLVED_PRIVATE` conclusions remain resolved when the private surface is temporarily inaccessible; lack of access becomes `NOT_VERIFIED`, not invented contradiction.

### KA-R38: private-data non-leakage

Generated public indexes, graph projections, summaries, search stores or exported receipts must not expose private paths, credentials, source locations or other private-only material merely because a private complement participates in reconstruction.

### KA-R39: bounded private dependency

If a task genuinely requires private state, the reconstruction must say so and verify the relevant private continuity status when accessible. If the task does not require it, public reconstruction must remain usable without loading private details.

## 39. Qualification, observability and migration requirements

### KA-R40: structural and cognitive qualification

Success must be tested at two levels:

```text
structural integrity
    sources, metadata, references, freshness, generated-view consistency

cognitive / reconstruction behavior
    orientation recall, authority selection, risk activation, route reconstruction,
    context efficiency and fail-visible uncertainty in realistic scenarios
```

A structurally valid repository is not sufficient evidence that the knowledge architecture works.

### KA-R41: measurable reconstruction coverage

A reconstruction result must be evaluable across explicit dimensions rather than judged only as "seems informed". At minimum the evaluation must score or classify:

```text
project identity / purpose
current stage and live boundary
major domain awareness
active route and parent objective
authority hierarchy
relevant governing-source discovery
known-risk / open-obligation activation
supersession/conflict handling
verification / uncertainty awareness
context/read cost
important omitted or latent knowledge disclosure
```

### KA-R42: fail-visible degraded mode

Failure of an optional semantic, vector, graph-index or generated-view service must not create false confidence. The design must either provide a safe deterministic fallback or explicitly state that required reconstruction cannot currently be completed.

### KA-R43: migration preservation

Migration may change files, families, identifiers, schemas or storage mechanisms, but it must preserve the meaning, authority, provenance and discoverability of unique durable knowledge or explicitly classify any intentional retirement. Silent semantic loss is unacceptable.

### KA-R44: old authority remains until successor qualification

The current architecture remains authoritative during design and migration. The authority switch may occur only after the successor passes the frozen qualification scenarios, migration reconciliation and rollback/recovery criteria appropriate to the selected design.

### KA-R45: self-hosting evolution

The knowledge architecture must be capable of preserving and coordinating a major redesign of itself across multiple conversations and interruptions. If its own migration cannot be reconstructed safely using its continuity model, it fails a core use case.

## 40. Non-negotiable architecture invariants

The requirements above imply the following invariants. Candidate architectures may implement them differently, but a selected target must not violate them without an explicit owner-approved revision to this requirements boundary.

```text
KA-I01  Durable project authority outranks chat/model memory.

KA-I02  The system has one explicit project-development authority; derived stores do not
        silently become a second source of truth.

KA-I03  Rebuildable derived state contains no unique project truth unless that truth is
        separately promoted to a durable authoritative surface.

KA-I04  Current, historical, superseded, rejected and unresolved knowledge remain
        distinguishable.

KA-I05  Consequential exact guidance/action requires task-relevant governing authority
        to be resolved and observably consumed first, or execution fails visibly.

KA-I06  Unresolved authority conflict or missing required evidence is surfaced rather
        than guessed away.

KA-I07  Provenance and routes to deeper evidence survive synthesis, compression and
        migration.

KA-I08  The old continuity system remains operational until the successor earns an
        explicit authority switch.

KA-I09  Paused work that is expected to resume has explicit reason, return condition,
        parent relationship and resume target.

KA-I10  Public/private authority separation is preserved and private data is not leaked
        through public derived representations.

KA-I11  Fresh-collaborator continuation cannot depend on a previous conversation being
        available.

KA-I12  Required cold-start cost is not structurally proportional to accumulated project
        history.

KA-I13  Routine artifact addition does not require unbounded manual edits to global
        routing surfaces.

KA-I14  Optional probabilistic retrieval failure cannot silently bypass required-authority
        safety or produce false reconstruction success.

KA-I15  The architecture can state its own live state, active route, authority status,
        reconstruction coverage and qualification status from durable project state.
```

## 41. Frozen candidate stress-test suite

Every serious candidate architecture must later be evaluated against the same scenario family. Exact fixtures and scoring thresholds may be refined before execution, but candidates must not receive easier scenario definitions simply because their mechanism differs.

### KA-S01: generic cold start

Starting from only the stable project entry and the instruction `Continue ADS`, reconstruct the project-level orientation, current stage, active route, parent objective, major domains, current uncertainty boundary and next legitimate research step without prior chat memory.

### KA-S02: AB-022 operational authority activation

Ask for exact local restart/startup guidance in a fresh context. The candidate must identify and consume the current governing operations authority before giving ordered instructions, rather than relying on reconstructed chat memory.

### KA-S03: latent known-risk trigger

Present a task whose conditions intersect a previously preserved known limitation or reopen trigger that is not named in the prompt. The candidate must surface the relevant warning and its source.

### KA-S04: nested route closure and resume

Open a child side-route, pause the parent, complete the child and reconstruct the exact deterministic return target and parent objective after context loss.

### KA-S05: saturated semantic domain

Query a domain equivalent to the current 293-path `development-governance` topic. The candidate must obtain useful governing orientation without dumping or reading the full member set.

### KA-S06: supersession and conflict

Provide current, historical and superseded artifacts with overlapping claims. The candidate must select the current governed authority where resolvable and surface any genuine unresolved conflict.

### KA-S07: private complement unavailable

Use public state containing `RESOLVED_PRIVATE` knowledge while the private complement is inaccessible. The candidate must preserve the public resolution, mark private freshness as not verified where relevant and avoid inventing private coordinates.

### KA-S08: abnormal transition interruption

Interrupt a multi-step repository or architecture migration after some durable actions have completed. A fresh collaborator must classify intended versus completed work and continue without blindly replaying uncertain mutations.

### KA-S09: 5x corpus growth

Expand historical/evidence volume approximately fivefold with realistic irrelevant and adjacent knowledge while preserving the same active problem. Core orientation and governing-source activation must stay inside the frozen reconstruction budget and maintain required recall.

### KA-S10: 10x corpus growth

Repeat the same test at approximately tenfold corpus scale. Normal continuation must not degrade into proportional whole-corpus reading.

### KA-S11: derived-store deletion and rebuild

Delete the candidate's rebuildable index/graph/vector/search representation. Prove that unique authoritative knowledge is not lost and that the derived state can be rebuilt or a safe fallback used.

### KA-S12: model/provider switch

Move the same project boundary to another capable collaborator with no previous chat memory. The collaborator must reconstruct the same material current state and authority boundaries from project-controlled sources.

### KA-S13: self-redesign continuity

Continue a multi-chat redesign of the knowledge architecture itself, including requirements, candidate comparison, migration and authority switch, without relying on the originating conversation.

### KA-S14: marginal maintenance cost

Add ordinary new research/evidence/checkpoint-like knowledge and measure which global/manual surfaces require updates. The candidate must demonstrate bounded marginal maintenance rather than corpus-proportional curation.

### KA-S15: concurrent related updates

Have multiple collaborators make related knowledge/state changes from nearby starting points. The candidate must detect stale/conflicting state rather than silently losing one collaborator's semantic update.

### KA-S16: probabilistic retrieval miss and false positive

Force semantic retrieval to omit a relevant item and rank an irrelevant similar item highly. The architecture must still protect required authority resolution and show a deterministic/fail-visible fallback path.

## 42. Candidate rejection gates

Regardless of convenience or implementation elegance, reject or materially redesign a candidate if it requires any of the following as a normal property:

```text
whole-corpus reading for ordinary continuation
human copy-paste of a growing continuation prompt
an opaque non-rebuildable second source of truth
silent use of stale generated state
probabilistic retrieval as the sole required-authority safety path
no deterministic/fail-visible nested resume semantics
loss of unique provenance during synthesis or migration
cold-start cost that grows approximately with corpus history
routine manual maintenance proportional to global corpus size
private continuity details leaking into public derived views
provider-specific hidden memory as a core continuity dependency
confident continuation when required authority or conflict resolution is unavailable
```

A candidate may still have trade-offs. These are failure conditions, not a demand that every dimension be maximized simultaneously.

## 43. Comparative metrics to freeze before candidate testing

Phase B freezes the measurement categories but deliberately does not invent precise numerical thresholds before candidate fixtures exist. Before Phase F comparative execution, each scenario must receive a fixed budget and success rubric shared by all candidates.

The metric set must include at least:

```text
orientation coverage
required-authority recall
known-risk activation recall
false-positive / irrelevant activation burden
authority-resolution correctness
supersession/conflict correctness
active-route reconstruction correctness
context / characters / artifacts consumed
time / tool-call complexity where meaningful
manual maintenance touches per ordinary artifact change
derived-view freshness / rebuild success
unresolved-uncertainty honesty
migration coverage / orphaned-knowledge count
```

For probabilistic retrieval components, both false negatives and false positives matter. High recall bought by flooding the context with hundreds of weakly relevant artifacts is not equivalent to useful reconstruction.

## 44. Architecture-neutral conclusions from Phase B

Phase B narrows the design problem without choosing a mechanism.

The future system is not merely an archive, index or search feature. It must behave as persistent project cognition infrastructure with four coupled responsibilities:

```text
preserve enough truth and provenance to remain durable
reconstruct broad and task-specific understanding efficiently
activate governing and risk-bearing knowledge before it matters
compress and organize accumulated understanding without losing traceability
```

Three design consequences are now explicit:

1. **Reconstruction must be planned and observable.** A fresh session should not simply receive a pile of files. It should traverse a bounded broad-to-deep route and be able to produce a reconstruction receipt.
2. **Required authority and ordinary relevance are different retrieval problems.** Semantic search can help discover relevance, but consequential governing authority needs stronger resolution semantics than similarity ranking alone.
3. **The knowledge system must separate authoritative durable knowledge from rebuildable acceleration structures.** Graphs, databases, embeddings, generated indexes and caches remain fully open options, but their authority/freshness/rebuild semantics must be explicit.

The target architecture remains unselected.

## 45. Originally planned next phase: candidate architecture families

This section preserves the Phase-B plan that existed before the project owner's immediate post-freeze methodology correction. Section 48 supersedes it as the current routing boundary. Candidate alternatives and shared stress tests remain useful later, but they are not the immediate next activity and must not become a shallow architecture-tournament or model-selection exercise.

When target-architecture design eventually resumes, serious alternatives should still be used to expose trade-offs and hidden assumptions rather than incrementally polishing the current design.

The candidate set should include at minimum serious variants of:

```text
distributed authoritative metadata + generated hierarchical views
Git-authoritative artifacts + explicit static/queryable relationship graph
Git-authoritative artifacts + rebuildable SQLite/indexed knowledge substrate
hierarchical project/domain synthesis + deterministic task authority router
hybrid lexical/semantic/vector retrieval subordinate to explicit authority graph
richer graph/database-first acceleration layer with Git-authoritative source
```

Combinations are allowed. The point of separate candidates is to expose trade-offs in authority, recall, complexity, context efficiency and maintenance rather than to force artificial purity.

Before ChatGPT's preferred target is reconciled, the independent-first multi-model pattern from Section 16 should be used so the challenger is not anchored on the primary design.

```text
RESEARCH124=ACTIVE
PHASE_A_BASELINE_INVENTORY=COMPLETE
PHASE_B_REQUIREMENTS_AND_INVARIANTS=COMPLETE
REQUIREMENTS_COUNT=45
INVARIANTS_COUNT=15
FROZEN_STRESS_SCENARIOS=16
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CANDIDATE_ARCHITECTURE_FAMILIES
```

## 46. Post-Phase-B evidence: collaboration-process activation failure

Immediately after Phase B, the project owner requested that Claude join the foundational discussion before architecture design proceeds. The first ChatGPT response incorrectly reverted to an ad hoc human-relay pattern: it drafted a large task prompt for the owner to copy into Claude instead of first using the repository-native model-collaboration protocol already preserved in `docs/model_collaboration/README.md`, `REVIEW_INBOX.md` and the `MC-*` thread machinery.

The owner had to remind ChatGPT how the established collaboration process works.

This is direct new evidence for the same class of problem that motivates cognitive activation in Research 124:

```text
correct process knowledge existed durably
    +
current collaborator had repository access
    +
process was relevant to the immediate task
    !=
process was activated at the decision point
```

The failure is stronger evidence than a simple missing link. The project had already invested in a repository-native collaboration protocol specifically so the human would not need to carry a large task contract between models, yet the reasoning process defaulted to the generic manual pattern until corrected by the owner.

This reinforces KA-R09 and the broader cognitive-activation layer. A mature project-development knowledge architecture must help activate not only domain facts and operational runbooks, but also **governing process knowledge about how project work itself is supposed to proceed** when the triggering situation occurs.

It also exposes a useful qualification question for later design work:

> Can the system recognize the current task class and activate the governing project-development procedure before the collaborator improvises a generic workflow?

## 47. Post-Phase-B evidence: semantic scope conflation

The same exchange exposed a second weakness. ChatGPT referred to the knowledge architecture under redesign as though it were "ADS" itself.

The project owner clarified the scope:

```text
ADS
    = the Autonomous Data Science System being built

project-development knowledge architecture
    = infrastructure used to preserve, structure, reconstruct, activate and evolve
      understanding about the ADS project and its development
```

The second supports development of the first. It is not the ADS product/system architecture itself.

This distinction matters because a large long-lived project can contain multiple architectural domains:

```text
ADS product/system architecture
project-development knowledge architecture
local execution / Runtime Bridge architecture
model-collaboration architecture
Source Vault architecture
Project Cockpit architecture
other future project-support infrastructure
```

If synthesis, retrieval or routing collapses these scopes into one undifferentiated "ADS architecture", the collaborator can select the wrong authority or reason at the wrong conceptual level even when every underlying document is individually correct.

Therefore semantic **scope identity** is now an explicit concern for the next discussion. Phase B remains the current stable requirements baseline, but it is not treated as immutable in the face of newly observed evidence. The Claude foundational dialogue should examine whether scope/domain identity deserves an explicit requirement/invariant and how strongly the architecture should represent it.

## 48. Design phase paused for foundational multi-model dialogue

The project owner has also corrected the methodology implied by the phrase `candidate architecture families`.

The next stage must not become a model-selection-style exercise in which several shallow architectures are generated, scored and a numerical winner is chosen. Alternative designs, prototypes and common stress tests remain valuable, but they are subordinate to deep architecture reasoning.

The intended design philosophy is now:

```text
understand the problem and conceptual structure deeply
    -> derive architecture principles and necessary mechanisms
    -> use alternatives to expose trade-offs and hidden assumptions
    -> use prototypes/experiments where reality is uncertain
    -> use stress tests primarily to falsify, qualify and refine reasoning
    -> synthesize a coherent architecture whose components can be justified
```

Research 124 target-architecture construction is therefore paused before Phase C while a current-context Claude collaboration examines the purpose, framing, Phase A/B work, missing concepts, methodology and relevant external fields without being forced to produce a target architecture.

An external paper/video that may be relevant is intentionally withheld during the first Claude discussion round. This creates a preserved pre-exposure baseline and reduces design fixation. The source may be introduced later through a separate collaboration turn so pre- and post-exposure reasoning remain distinguishable.

```text
POST_PHASE_B_EVIDENCE=CAPTURED
COLLABORATION_PROTOCOL_ACTIVATION_FAILURE=OBSERVED
SEMANTIC_SCOPE_CONFLATION=OBSERVED
ADS_PRODUCT_ARCHITECTURE_NE_PROJECT_KNOWLEDGE_ARCHITECTURE=true
PHASE_B_BASELINE=STABLE_BUT_AMENDABLE_BY_NEW_EVIDENCE
TARGET_ARCHITECTURE_DESIGN=PAUSED
NEXT=CLAUDE_FOUNDATIONAL_KNOWLEDGE_ARCHITECTURE_DIALOGUE
```