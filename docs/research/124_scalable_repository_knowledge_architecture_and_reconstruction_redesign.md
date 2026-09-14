# Research 124: Scalable Repository Knowledge Architecture and Reconstruction Redesign

**Date:** 2026-09-13
**Status:** ACTIVE / REQUIREMENTS V0.2 OWNER-ACCEPTED AND FROZEN / EVIDENCE RECONCILIATION V0.3 COMPLETE / CROSS-PROVIDER Q1+Q2 CHALLENGE NEXT / TARGET ARCHITECTURE NOT SELECTED
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
## 49. MC-0011 foundational dialogue resolved by owner decision

The project owner explicitly accepted closure of MC-0011 after three Claude responses and three ChatGPT responses. The collaboration therefore exits the foundational-dialogue gate without selecting a target architecture.

The durable resolution is:

```text
docs/model_collaboration/threads/MC-0011/RESOLUTION.md
```

The dialogue materially changes the Research 124 working frame in several ways.

First, the redesign is explicitly about **project-development knowledge infrastructure supporting ADS**, not the architecture of the Autonomous Data Science System product itself.

Second, cognitive activation is no longer treated as one undifferentiated problem. At least two failure classes now matter:

```text
reconstruction / retrieval failure
    project-specific knowledge should have been recovered but was not

situation-dispatch failure
    the collaborator never initiated the project-specific retrieval/procedure path
    because generic reasoning began first
```

Third, consolidation/compression is now treated as a first-class cross-cutting scaling function rather than merely an output-format concern. Precise navigation without consolidation can still require traversal cost that grows approximately with the number of currently relevant knowledge units.

Fourth, the stable-entry requirement is refined conceptually. The intended target is not one universal static bootstrap packet. It is one stable **bootstrap/router mechanism** that can determine or elicit task/continuation mode and route into task-shaped reconstruction paths.

Fifth, the dialogue introduces a provisional **reasoning control plane** concept. This remains inside Research 124 only where it answers whether project reasoning has license to proceed given task classification, governing authority, reconstruction coverage and uncertainty. It does not absorb Runtime Bridge transport/mutation safety or model-collaboration write-ownership mechanics.

Sixth, the preferred conceptual direction for task/procedure activation is no longer a hand-maintained central situation registry. A safer hypothesis is:

```text
governing source declares task/situation conditions it governs
    -> generated / rebuildable dispatch representation
    -> narrow routing/policy reasoning checks that representation
    -> ordinary work reasoning proceeds only after the relevant gate
```

This remains a hypothesis to test, not an accepted implementation.

## 50. Working decomposition after MC-0011

Research 124 now carries this provisional problem decomposition into the evidence phase:

```text
knowledge substrate / data plane
    durable authoritative knowledge
    evidence
    provenance
    relationships
    source-of-truth semantics

knowledge lifecycle / consolidation function
    capture
    distill
    synthesize
    promote
    retire from active surface
    regenerate derived views

reasoning control plane
    task/situation classification
    governing-procedure dispatch
    authority preflight
    task-shaped reconstruction routing
    block/fail-visible behavior when required authority is unresolved
    uncertainty / calibration signaling
    reconstruction receipt

collaborator interface
    what a fresh model/human receives
    how scope and authority are exposed
    how broad orientation drills into exact evidence
```

This decomposition is deliberately above implementation mechanism. It does not imply a graph, database, vector store, separate routing model or new artifact family.

### 50.1 Working bootstrap-core principle

The strongest provisional formulation from MC-0011 is:

> **A constitutional/bootstrap core should be a tiny high-stability protocol telling a collaborator how to acquire trustworthy current project understanding. It should contain procedures and pointers, not ordinary changing project-state values or history-growing lists.**

Potential invariants to research later include:

```text
no ordinary changing state values
no enumerable lists expected to grow with project history
all pointers mechanically resolvable
rare explicit amendment path with rationale
small size as a secondary, not sufficient, guard
```

### 50.2 Active knowledge surface

The working definition is:

> **The active knowledge surface is the subset of durable project knowledge that must remain cheaply discoverable, reconstructable or triggerable for current and plausibly near-term work, distinct from deep provenance that remains durable but may stay latent until explicitly traversed.**

The working transition hypothesis is asymmetric:

```text
promotion to active    explicit and deliberate
return to latent       default when governing/workstream relevance ends
```

Where feasible, active status should be derived from live workstream/procedure/dependency state rather than manually maintained as a second per-artifact truth.

## 51. Evidence-phase method after foundational dialogue

The owner accepted an evidence-first next phase while target architecture construction remains paused.

The sequence is now:

```text
1. audit one high-density checkpoint day and one saturated routing domain
2. construct a bounded historical failure corpus across distinct mechanism classes
3. run blind fresh-session/model baselines under the current architecture
4. conduct broad question-driven external research across several disciplines
5. reconcile Phase-B requirements with evidentiary provenance and new evidence
6. stabilize the active-surface and reasoning-control-plane boundary definitions
7. only then begin serious architecture synthesis
8. use mechanism probes/prototypes where causal uncertainty remains
9. expose the owner's withheld paper/video deliberately against the broader evidence base
```

The external source remains withheld at this boundary.

The evidence program should avoid solution-shaped experiments. A failure corpus should preserve what failed and the exact evidence, not encode the architecture expected to fix it.

## 52. Initial empirical audit A: 2026-09-09 high-density checkpoint day

The first requested granularity discriminator examines the 34 numbered checkpoints dated 2026-09-09, Checkpoints 394 through 427.

Current repository measurement:

```text
checkpoint count      34
checkpoint bytes      113,490
mean bytes/checkpoint about 3,338
number range          394-427
```

At the metadata level, the day divides approximately into:

```text
394-399   GitHub App permission / registration / installation / authorization     6
400-409   read-only Runtime Bridge qualification plus one semantic-Git repair     10
410-425   write-family implementation / host qualification / positive-live gates  16
426-427   parity reconciliation and first beyond-parity administration design      2
```

Every sampled checkpoint has an explicit status and scope describing a changed project boundary rather than merely another commit.

A deeper spot-check of Checkpoints 410-415 shows a repeating three-gate pattern for each mutation family:

```text
local implementation + activation + no-write qualification
    -> fresh-host projection/schema/no-write qualification
    -> separately owner-authorized positive-live qualification
```

For repository Git/content this is Checkpoints 410, 411 and 412. For issue mutations it is 413, 414 and 415.

These are not interchangeable micro-adjustments. They correspond to materially different risk/authority states:

```text
code exists and is locally/live structurally qualified, but no external write allowed
host-facing contract is independently qualified, but positive write still not authorized
positive external mutation is separately authorized and read back
```

The existing checkpoint-granularity rule says a checkpoint is warranted for a substantial implementation/experiment milestone, material status change, reusable lesson, fragile continuity or changed project direction, and not merely because another commit/small adjustment occurred.

### 52.1 Provisional finding

This sampled high-density day does **not** support the strong claim that checkpoint count is primarily caused by obvious micro-iteration abuse.

The 34-record count is high, but much of it reflects a deliberately serialized safety/qualification program with distinct verified authority gates. The metadata and the 410-415 content sample show real boundary changes that plausibly satisfy the existing checkpoint rule.

Therefore:

> **High checkpoint count alone is not evidence of excessive checkpoint granularity.**

This weakens the hypothesis that simply creating fewer checkpoints is the main knowledge-scaling solution.

It does not prove all 34 were optimally separated. A complete line-by-line retrospective could still find mergeable cases, but the first bounded audit finds no obvious systematic violation large enough to explain the current knowledge pressure.

The more important pressure may be that valid historical checkpoints continue to occupy high-salience current/navigation surfaces long after the qualification stage closes.

## 53. Initial empirical audit B: saturated `development-governance` routing surface

The second discriminator examines the current human-visible direct path list under the Knowledge Map topic:

```text
development-governance
```

Using the current fenced direct-path block in that topic, after the Research 124 additions but before any redesign, the topic contains 298 unique direct file paths.

Composition is:

```text
docs/checkpoints/                 123   41.3%
docs/local_execution/validation  113   37.9%
docs/research/                     45   15.1%
core / other                        5    1.7%
docs/model_collaboration            4    1.3%
docs/specifications                 4    1.3%
docs/local_execution                2    0.7%
docs/foundations                     1    0.3%
scripts                              1    0.3%
```

Combined checkpoints plus validation evidence:

```text
236 / 298 = 79.2%
```

This measurement is intentionally different from Phase A's validator-normalized route count. It asks what the human-visible direct routing surface currently exposes inside the saturated topic.

### 53.1 Interpretation

The saturation appears to be dominated by historical/evidence-level material rather than by hundreds of independent top-level conceptual authorities.

That matters because those files may be **correctly classified** as development/governance evidence while still being poor default navigation material.

So the problem is not necessarily:

```text
these artifacts are in the wrong semantic topic
```

It may instead be:

```text
a flat topic representation exposes deep evidence at the same navigation depth as
current synthesis, governing procedures and conceptual orientation
```

This distinction supports the active/latent and progressive-disclosure framing from MC-0011.

Historical validation/checkpoint evidence should remain durable and reachable. It need not remain part of the ordinary active navigation surface once a higher-level accepted synthesis or current procedure adequately represents it.

### 53.2 Combined density finding

Taken together, Audits A and B change the initial hypothesis:

```text
initial suspicion
    rapid artifact creation may itself be the primary scaling defect

current evidence
    at least one 34-checkpoint day largely reflects meaningful serialized gates
    while the saturated topic is overwhelmingly populated by checkpoint/validation evidence

stronger current hypothesis
    legitimate historical accumulation is not being folded out of the active/navigation
    surface aggressively enough after its immediate work boundary closes
```

This is provisional and should be tested against additional failure-corpus evidence rather than promoted directly into target architecture.

## 54. Next evidence boundary: historical failure corpus and blind baselines

The next immediate Research 124 task is to construct a deliberately bounded failure corpus before testing any proposed dispatch, retrieval, consolidation or bootstrap mechanism.

Initial mechanism classes from MC-0011 are:

```text
retrieval / discoverability miss
stale convenience or generated view
situation-dispatch / governing-procedure activation miss
authority-resolution or supersession miss
semantic scope/domain conflation
continuation / resume ambiguity
compression / synthesis loss or misleading abstraction
public/private boundary failure
```

Construction rules:

```text
prefer 2-3 real historical exemplars per class where evidence exists
use exact durable evidence rather than chat recollection
record whether the issue was self-caught, validator-caught or owner-caught
add at most 1-2 adjacent constructed variants only when useful for generalization
DO NOT encode the preferred architectural remedy into the corpus entry
absence of enough real exemplars remains evidence rather than being padded artificially
```

After the corpus is frozen, a small set of blind current-architecture baseline trials should establish which failure classes actually reproduce across fresh collaborators/models before mechanism probes begin.

```text
RESEARCH124=ACTIVE
MC0011=RESOLVED
TARGET_ARCHITECTURE=NOT_SELECTED
TARGET_ARCHITECTURE_DESIGN=PAUSED
HIGH_DENSITY_CHECKPOINT_AUDIT=COMPLETE_INITIAL
SATURATED_ROUTING_DOMAIN_AUDIT=COMPLETE_INITIAL
CHECKPOINT_COUNT_PRIMARY_GRANULARITY_FAILURE=NOT_SUPPORTED_BY_FIRST_SAMPLE
ACTIVE_SURFACE_ACCUMULATION_HYPOTHESIS=STRENGTHENED
WITHHELD_EXTERNAL_SOURCE=STILL_WITHHELD
NEXT=BOUNDED_HISTORICAL_FAILURE_CORPUS
```
## 55. Bounded historical failure corpus V0.1 complete

The first Research 124 empirical failure corpus is now preserved at:

```text
docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md
```

The corpus is deliberately solution-neutral. It records what failed, what was merely a near-miss, what required recovery, and what remains only a structural gap. It does not encode the successor mechanism expected to solve each case.

V0.1 contains 22 case rows across nine mechanism classes:

```text
retrieval / discoverability                         3
stale convenience / derived / duplicated view       3
situation dispatch / governing-procedure activation 3
required authority / source selection               2
semantic scope / identity conflation                3
continuation / resume                               2
compression / synthesis / transcription             3
public / private continuity boundary                2
latent known-risk / reopen-trigger activation       1 composite pattern
```

One row, `KF-CR-02`, is explicitly `STRUCTURAL_GAP_NOT_FAILURE`. The remaining 21 rows are observed failures, near-misses, recovery events or composite observed patterns. Row count is not a prevalence estimate; several cases share a broader episode and some classes remain sparse.

### 55.1 Important empirical distinctions

The corpus reinforces that the redesign cannot be evaluated through one generic "retrieval succeeded" metric.

Observed mechanisms include:

```text
knowledge preserved but global semantic route drifted
live/current copies diverged while substantive truth survived
correct governing procedure linked but never activated before guidance
weaker prose summary used instead of stronger exact implementation source
accepted source contract narrowed during promotion
semantic identities/scopes conflated
abnormal interruption made intended-vs-completed continuation ambiguous
summary/transcription corrupted quantitative evidence
public/private continuity surfaces fell out of synchronization
known escalation triggers remained latent until live pressure was noticed independently
```

These mechanisms differ in where the failure occurs. Some are storage/routing problems, some are dispatch problems, some are authority/provenance problems, and some are lossy abstraction/promotion problems.

### 55.2 Strongest repeated evidence currently available

The best-supported repeated patterns are:

```text
routing/current-state/convenience-view drift
    multiple durable examples across current routing, Knowledge Map and summary surfaces

situation-dispatch failure
    at least two distinct task families:
        exact operational restart procedure
        repository-native model collaboration procedure

synthesis/promotion fidelity loss
    exact Cockpit implementation evidence replaced by prose-level reinterpretation
    metadata inventory counts corrupted in durable transcription
    accepted integrity-contract details dropped during specification promotion
```

By contrast, deterministic nested resume remains mainly an observed structural weakness rather than a demonstrated wrong-resume event. The corpus preserves that evidentiary asymmetry instead of treating every Research 124 concern as equally proven.

### 55.3 Evaluator contamination constraint

The corpus itself is evaluator evidence. A future "blind" collaborator should not simply be told to read the corpus before performing a baseline task, because that would disclose both the historical failure classes and the cases selected for evaluation.

The next phase must therefore design a baseline protocol that separates:

```text
source project state available to the tested collaborator

evaluator-only case selection / expected evidence

task prompt presented to the tested collaborator

post-run scoring against the frozen corpus
```

The protocol must also avoid accidentally testing a post-diagnosis repository state that already describes the exact failure being elicited unless the scenario intentionally measures whether current architecture now activates the lesson.

```text
FAILURE_CORPUS_V01=COMPLETE
CASE_ROWS=22
OBSERVED_OR_NEAR_RECOVERY_PATTERN_ROWS=21
STRUCTURAL_GAP_ROWS=1
TARGET_ARCHITECTURE_REMEDIES_ENCODED=false
WITHHELD_EXTERNAL_SOURCE_USED=false
NEXT=BLIND_BASELINE_PROTOCOL_DESIGN
```
## 56. Blind baseline protocol V0.1 frozen

The failure corpus is now paired with a contamination-controlled historical-snapshot pilot protocol:

```text
docs/research/project_knowledge_baselines/PROJECT_KNOWLEDGE_BLIND_BASELINE_PROTOCOL.md
```

The protocol exists because current repository state already contains Research 124 diagnoses. A fresh-session trial against current HEAD would therefore test whether a collaborator can consume an explicit diagnosis, not whether the earlier architecture naturally routed the collaborator before the diagnosis existed.

Each pilot scenario therefore binds one exact historical commit as the sole project-evidence snapshot. The tested collaborator may reason broadly within that snapshot but may not use descendant/current project content, evaluator records, external sources or prior-chat project memory as evidence. If exact snapshot access cannot be constrained reliably, the trial is invalid rather than silently falling back to current HEAD.

### 56.1 Initial pilot matrix

Four deliberately different historical mechanisms are selected:

```text
BL-001  operational governing-procedure activation
        snapshot a570f0d87b77960ae0715b291de0d5f6e884e4d0
        parent KF-SD-01

BL-002  repository-native model-collaboration dispatch
        snapshot 1a422c79dc67384426ad10e28c2fc6845147f9e0
        parent KF-SD-03

BL-003  broad project orientation under drifted global navigation
        snapshot f355994c538e0b9b28b5a3c2a5814252ffea1939
        parent KF-RD-01

BL-004  exact-source fidelity before holistic Cockpit integration
        snapshot 2d425c76c385961cdd7f986c17ed83437a3d3806
        parents KF-AS-01 / KF-CS-01
```

Checkpoint 456 originally froze a two-environment ChatGPT/Claude pilot. The project owner then narrowed the empirical baseline to **ChatGPT only** before any trial was executed. The active pilot therefore uses one fresh disposable ChatGPT conversation per scenario, for four initial trials. Additional fresh ChatGPT replicates are targeted only where a result is borderline, ambiguous or appears stochastic.

This is intentionally not a model leaderboard. The goal is to characterize how the current/historical project-development knowledge architecture behaves across several mechanisms in fresh ChatGPT sessions. Cross-model comparison is not part of the active baseline and would require a later explicit owner-approved protocol.

### 56.2 Evaluation dimensions

The frozen qualitative dimensions are:

```text
S1 task/situation recognition
S2 governing-source discovery
S3 governing-source consumption
S4 authority/source-strength selection
S5 final task correctness / fidelity
S6 uncertainty calibration
S7 broad-vs-narrow context appropriateness
S8 read/tool cost and irrelevant-context burden
```

Results are classified `PASS / PARTIAL / FAIL / N/A` per dimension. There is no aggregate numeric winner score.

Failure attribution must distinguish at least source absence, discoverability, dispatch, authority resolution, post-consumption reasoning, calibration, tool-access and protocol-contamination problems.

### 56.3 Result isolation

Each trial receives one unique result path under:

```text
docs/research/project_knowledge_baselines/results/
```

The tested collaborator may preserve only that result artifact after reasoning is complete. It may not mutate the historical snapshot or other project state. Trials should run sequentially enough that each result commit can synchronize before the next writer commits.

The evaluator corpus, protocol scoring criteria and prior results are not trial input.

### 56.4 External-evidence boundary

Broad external literature research and the project owner's withheld paper/video remain paused until the initial behavioral pilot is completed or explicitly classified infeasible with a preserved reason.

This preserves the pre-external-evidence baseline generated by both the foundational dialogue and the fresh-session trials.

```text
BLIND_BASELINE_PROTOCOL_V02=ACTIVE
PILOT_SCENARIOS=4
PILOT_ENVIRONMENTS=CHATGPT_ONLY
INITIAL_TRIALS=4
HISTORICAL_SNAPSHOT_ISOLATION=REQUIRED
AGGREGATE_MODEL_SCORE=NONE
TARGET_ARCHITECTURE=NOT_SELECTED
WITHHELD_EXTERNAL_SOURCE=STILL_WITHHELD
NEXT=EXECUTE_BLIND_BASELINE_PILOT
```
## 57. Owner narrows pilot to ChatGPT only before execution

After Checkpoint 456 froze an initial ChatGPT-plus-Claude baseline matrix, the project owner explicitly narrowed the pilot to **ChatGPT only** before any trial was executed.

This changes the purpose of the pilot from cross-model comparison to one-environment empirical characterization of the current/historical project-development knowledge architecture.

The active matrix is now:

```text
BL-001  fresh ChatGPT
BL-002  fresh ChatGPT
BL-003  fresh ChatGPT
BL-004  fresh ChatGPT
```

Initial trial count:

```text
4 scenarios x 1 environment = 4 trials
```

Claude baseline trials are not merely postponed implicitly; they are **out of scope for this pilot**. Any future cross-model study requires a separate explicit owner decision and protocol so it does not silently re-expand this evidence phase.

The historical snapshots, task requests, evaluator dimensions, contamination controls and no-aggregate-score principle remain unchanged.

Targeted second ChatGPT replicates remain allowed only where a scenario result is borderline, ambiguous or appears stochastic.

```text
BASELINE_SCOPE_CHANGE=OWNER_ACCEPTED
PILOT_ENVIRONMENT=CHATGPT_ONLY
INITIAL_TRIALS=4
CLAUDE_BASELINE=OUT_OF_SCOPE
CROSS_MODEL_STUDY=REQUIRES_FUTURE_OWNER_DECISION
NEXT=EXECUTE_CHATGPT_BLIND_BASELINE_PILOT
```
## 58. First pilot evidence and BL-002 harness contamination

The ChatGPT-only pilot has begun.

### 58.1 BL-001-A: governing source activated, exact task contract not preserved

BL-001-A is a usable result and is evaluated at:

```text
docs/research/project_knowledge_baselines/evaluations/BL-001_chatgpt_a_evaluation.md
```

The fresh collaborator successfully recognized the operational task, discovered and materially consumed `docs/local_execution/OPERATIONS.md`, and selected the correct authority class. The historical `KF-SD-01` failure therefore did not reproduce as a simple governing-procedure activation miss.

However, the task explicitly requested the **exact ordered restart/reconnect procedure**, and the final answer did not reproduce that governing sequence. It broadened into substantial project reconstruction and then gestured back to the runbook.

This adds an empirically distinct post-activation failure boundary:

```text
source activation
    !=
contract extraction
    !=
answer/task fidelity
```

A future successor architecture cannot treat `right source entered context` as sufficient evidence of task correctness.

### 58.2 BL-002-A: invalid due tool-response contamination

BL-002-A is preserved but **not scored as a blind baseline**.

Its receipt records that a frozen-commit metadata call unexpectedly returned patch content from prohibited current Research 124. The collaborator explicitly excluded that content from its stated evidence and otherwise reconstructed the repository-native model-collaboration process from the frozen snapshot.

Because later diagnosis content nevertheless entered model context before the answer was frozen, absence of influence cannot be proven. The trial is therefore invalid under the historical-snapshot isolation principle.

Evaluation:

```text
docs/research/project_knowledge_baselines/evaluations/BL-002_chatgpt_a_evaluation.md
```

The invalidation is attributed to **tool/harness contamination**, not to project-knowledge behavior.

### 58.3 Protocol V0.2 access hardening

The pilot repository-access environment is now explicitly controlled:

```text
Codexless Runtime Bridge only
native GitHub plugin/connector not used
```

For BL-002-B and later historical-snapshot trials, the model must use only snapshot-bounded local Git object/tree operations through Codexless read-only command execution, for example:

```text
git show <SNAPSHOT>:<path>
git ls-tree ... <SNAPSHOT>
git grep ... <SNAPSHOT> -- <paths>
```

Broad commit metadata/search/fetch actions that may return unrelated patch context are excluded from the pilot access lane.

If any tool unexpectedly exposes descendant/current project material, the trial now stops with `TRIAL_CONTAMINATED` rather than attempting to continue after mentally excluding the leaked content.

The substantive BL-002 task remains unchanged. An access-hardened replacement request is frozen at:

```text
docs/research/project_knowledge_baselines/requests/BL-002B_model_collaboration_dispatch_access_hardened.md
```

with replacement result path:

```text
docs/research/project_knowledge_baselines/results/BL-002_chatgpt_b.md
```

```text
BL001_A=USABLE
BL001_HISTORICAL_DISPATCH_FAILURE_REPRODUCED=false
BL001_POST_ACTIVATION_TASK_FIDELITY_FAILURE=observed
BL002_A=INVALID_TOOL_CONTAMINATION
BASELINE_PROTOCOL_VERSION=0.2
REPOSITORY_ACCESS_ENVIRONMENT=CODEXLESS_ONLY
BL002_REPLACEMENT=REQUIRED
NEXT=BL-002_CHATGPT_B
```
## 59. BL-002-B valid replacement: process reconstructable under explicit process cue

BL-002-B is the valid replacement for contaminated BL-002-A and is evaluated at:

```text
docs/research/project_knowledge_baselines/evaluations/BL-002_chatgpt_b_evaluation.md
```

The V0.2 access-hardened trial remained inside the exact frozen snapshot through Codexless-only local Git object/tree reads and did not expose later Research 124 material.

The result does not reproduce the historical generic manual-relay behavior. A fresh ChatGPT efficiently reconstructed the repository-native model-collaboration machinery, including thread identity, `BRIEF` / `THREAD` / `STATE`, `REVIEW_INBOX`, coordination-branch versus immutable evidence boundaries, role/write-scope separation, bounded Claude message writes, persistent interaction provenance and the short standardized human-to-Claude relay.

The result is strong evidence that the collaboration process is **discoverable, reconstructable and usable once the task explicitly tells the collaborator to use the way the project already handles multi-model collaboration**.

However, the trial has an important construct-validity limitation. The request itself contains that explicit procedural cue. Historical parent `KF-SD-03` involved a stronger failure: ChatGPT was asked to involve Claude and did not spontaneously activate the preserved project-specific collaboration process until the owner reminded it how the process worked.

Therefore BL-002-B supports:

```text
process existence cued
    -> governing collaboration sources discovered
    -> process reconstructed correctly
    -> short repository-native relay proposed
```

but does not cleanly establish:

```text
uncued "bring Claude in"
    -> situation classified as project-governed collaboration automatically
```

This distinction should survive later architecture synthesis. Situation classification/dispatch and downstream process reconstruction are empirically separable.

No identical BL-002-B repeat is required. A later adjacent uncued variant may be useful after the bounded four-scenario pilot if spontaneous dispatch remains an important unresolved claim.

BL-003 and BL-004 had not yet executed when Protocol V0.2 hardened the access lane, so access-hardened request artifacts are prepared for both without changing their substantive tasks or frozen snapshots.

```text
BL002_B=VALID
BL002_PROCESS_DISCOVERABILITY=PASS
BL002_PROCESS_RECONSTRUCTION=PASS
BL002_UNCUED_DISPATCH=NOT_CLEANLY_TESTED
IDENTICAL_REPLICATE=NO
POSSIBLE_LATER_UNCUED_VARIANT=YES
NEXT=BL-003_CHATGPT_A
```
## 60. BL-003-A valid: broad orientation is recoverable despite map drift, but not cheaply proven

BL-003-A is evaluated at:

```text
docs/research/project_knowledge_baselines/evaluations/BL-003_chatgpt_a_evaluation.md
```

The trial is protocol-valid under V0.2. The fresh ChatGPT remained inside frozen snapshot `f355994c538e0b9b28b5a3c2a5814252ffea1939`, used Codexless-only exact Git object/tree reads, and did not consume descendant Research 124 or evaluator material.

The result does not reproduce a strong-form broad-reconstruction failure. Despite the then-drifted global `KNOWLEDGE_MAP.md`, the collaborator reconstructed a broad project picture spanning epistemic integrity, the LLM/system/human boundary, project state/object/dependency architecture, methodological navigation and reusable knowledge, V1 persistence/retrieval/context infrastructure, Project Cockpit/product architecture, Source Universe provenance, experimental falsification, and project-development governance.

The collaborator did this by **not assuming the global map was complete**. It used repository-tree discovery plus selective deep-source reads across Vision, Development Method, Foundations, Specifications, experiment evidence and specialized subsystem sources.

This weakens the simplistic causal claim:

```text
Cockpit-heavy global map
    -> broad project orientation impossible
```

The better current interpretation is:

> **Global routing drift degraded direct semantic navigation, while broad reconstruction remained possible through compensating repository-wide search and deeper-source traversal.**

The key remaining weakness is cost. The trial used about 18 tool/read actions. That is reasonable for a broad orientation task but does not demonstrate the Research 124 goal that sufficient understanding can be reconstructed under a small bounded cold-start budget as corpus size grows.

So BL-003 adds an important empirical distinction:

```text
recoverability          demonstrated in this frozen case
cheap reconstruction    not demonstrated
sublinear scaling       not demonstrated
```

No identical BL-003 repeat is required. A later fixed-read-budget orientation variant would be more informative if Research 124 needs a sharper scaling discriminator.

```text
BL003_A=VALID
BROAD_ORIENTATION_RECOVERABLE=true
GLOBAL_MAP_DRIFT_EQUAL_TOTAL_RECONSTRUCTION_FAILURE=false
RECONSTRUCTION_COST_PRESSURE=observed
IMMEDIATE_IDENTICAL_REPLICATE=NO
POSSIBLE_LATER_FIXED_BUDGET_VARIANT=YES
NEXT=BL-004_CHATGPT_A
```
## 61. BL-004-A valid and initial four-scenario pilot complete

BL-004-A is evaluated at:

```text
docs/research/project_knowledge_baselines/evaluations/BL-004_chatgpt_a_evaluation.md
```

The trial is valid under Protocol V0.2 and strongly does not reproduce the historical exact-source fidelity failure represented by `KF-AS-01` / `KF-CS-01`.

The fresh ChatGPT reconstructed a task-sensitive source hierarchy instead of flattening all Phase-C evidence into prose peers:

```text
promoted interaction specification
    -> semantic/product foundations
    -> latest explicit Phase-C selections
    -> exact accepted design-lab implementation targets as fidelity oracles
    -> existing production Cockpit as integration substrate rather than visual authority
```

It explicitly rejected recreating accepted visual/interaction mechanisms from memory or prose where exact accepted implementations exist. It proposed porting exact geometry/timing/layering/behavior from source implementations, while refusing to import prototype-only persistence, fixture ontology or experiment controls merely because they co-reside in the prototype.

This is important evidence for a **task-sensitive evidence-depth** requirement:

```text
orientation task
    may stop at accepted synthesis / governing decision

high-fidelity implementation task
    must descend into exact executable provenance when prose alone is too lossy
```

The trial did not exhaustively inspect every accepted design-lab CSS/JS file line-by-line, so it demonstrates correct source-strength reasoning and source-level integration planning rather than complete implementation-source consumption.

### 61.1 Initial pilot synthesis

The original four-scenario ChatGPT pilot is now complete.

```text
BL-001
    operational authority activates
    exact ordered task contract still lost after activation

BL-002-B
    collaboration process discoverable/reconstructable under explicit process cue
    uncued situation dispatch not cleanly tested

BL-003
    broad orientation recoverable despite global-map drift
    reconstruction requires non-trivial compensating search/read effort

BL-004
    exact-source fidelity hierarchy recoverable
    many-source assembly remains non-trivial in cost
```

The pilot therefore changes the empirical framing substantially. The current project-development knowledge architecture is **not generally incapable of preserving or reconstructing project understanding**. Instead, several narrower failure boundaries are supported:

```text
situation activation may fail before retrieval begins
source activation does not guarantee exact answer/task fidelity
broad/exact reconstruction may remain possible but require expensive compensating search
required evidence depth depends on task fidelity
```

### 61.2 One targeted adjacent variant before external research

MC-0011 made uncued situation-class recognition a central unresolved question. BL-002-B cannot answer it because the prompt explicitly told the collaborator to use the way the project already handles multi-model collaboration.

Research 124 therefore authorizes exactly one additional pre-external-evidence variant:

```text
BL-002U
    same historical snapshot as BL-002
    constructed adjacent wording
    no explicit cue that a project-specific collaboration process exists
```

Request:

```text
docs/research/project_knowledge_baselines/requests/BL-002U_uncued_model_collaboration_dispatch.md
```

This is not an automatic expansion into a larger benchmark. No fixed-budget BL-003 variant or extra BL-001/BL-004 replicate is required before external research at this boundary.

After BL-002U, the pilot should be synthesized and the project can move into broad question-driven external research unless the variant itself exposes a protocol defect.

```text
BL004_A=VALID
INITIAL_FOUR_SCENARIO_PILOT=COMPLETE
UNCUED_SITUATION_DISPATCH=UNRESOLVED
TARGETED_ADJACENT_VARIANT=BL-002U_ONLY
TARGET_ARCHITECTURE=NOT_SELECTED
EXTERNAL_RESEARCH=PAUSED_UNTIL_BL002U
WITHHELD_EXTERNAL_SOURCE=STILL_WITHHELD
NEXT=BL-002U_UNCUED_DISPATCH
```
## 62. BL-002U closes the pre-external-evidence baseline phase

BL-002U is evaluated at:

```text
docs/research/project_knowledge_baselines/evaluations/BL-002U_chatgpt_a_evaluation.md
```

The constructed adjacent task removes BL-002-B's explicit substantive instruction to use "the way this project already handles multi-model collaboration." A fresh ChatGPT nevertheless discovers and reconstructs the governed `MC-*` process from frozen snapshot `1a422c79dc67384426ad10e28c2fc6845147f9e0`, selects the independent-first MC-0008 pattern, separates the unrelated MC-0010 obligation, and rejects an informal manual relay as the primary collaboration path.

This strengthens the evidence that the current repository already makes the collaboration process discoverable and reconstructable with modest effort.

The result retains one construct-validity limitation: the evaluator-facing request title says `Uncued Dispatch Variant` and the metadata identifies it as a constructed adjacent variant. Those labels can prime task classification even though they do not reveal the historical failure contents or the expected workflow.

Research 124 therefore does **not** claim perfectly unprimed spontaneous dispatch. The calibrated conclusion is:

> **When the substantive user wording merely asks to involve Claude, a fresh ChatGPT can still recover the repository-native governed collaboration process from the frozen project state. The remaining evaluator-facing scenario label prevents interpreting the run as a perfectly cue-free behavioral experiment.**

The residual limitation does not justify another pre-external-research trial. Further harness purification would have diminishing value relative to the next evidence phase.

### 62.1 Completed baseline picture

The completed ChatGPT baseline program now supports:

```text
BL-001
    governing operational source discoverable and consumed
    exact task contract still omitted after activation

BL-002-B
    collaboration process reconstructable under explicit process cue

BL-002U
    collaboration process still reconstructable after substantive cue removal
    evaluator-facing scenario metadata remains a small priming limitation

BL-003
    broad orientation recoverable despite routing drift
    non-trivial compensating search/read cost remains

BL-004
    exact-source fidelity hierarchy recoverable
    high-fidelity tasks require descent into executable provenance
```

The current architecture is therefore empirically stronger than the initial failure narrative implied. The redesign case should no longer rest on broad claims that project understanding is unrecoverable.

The strongest remaining problem statement is narrower:

```text
reliable task/situation activation at the decision point
exact contract extraction after source activation
bounded reconstruction cost as corpus scale grows
task-sensitive evidence-depth routing
active-surface consolidation so deep provenance remains reachable without staying globally salient
```

### 62.2 Baseline phase closed

No additional ChatGPT baseline scenarios are required before broad external research.

The next phase begins with question-driven research across several disciplines rather than searching for one ready-made "knowledge architecture" solution.

Priority research questions remain:

```text
human factors / forcing functions
    what makes a pre-action check survive expertise, routine and time pressure?

information retrieval / vocabulary problem
    how should lexical, semantic and structured routing interact when terminology drifts?

LLM / agent memory and hierarchical consolidation
    what evidence exists for compression/consolidation without unacceptable recall loss?

software configuration management / reproducible derived state
    which lineage, rebuildability, idempotence and source-vs-derived patterns transfer cleanly?

digital preservation / OAIS and adjacent preservation theory
    what substantive requirements are added beyond labels already present internally?
```

At least one substantial non-AI/ML evidence stream should be included before the project-owner withheld paper/video is exposed.

```text
PRE_EXTERNAL_BASELINE_PHASE=COMPLETE
BL002U=VALID_WITH_METADATA_CUE_LIMITATION
MORE_BASELINE_TRIALS=NO
TARGET_ARCHITECTURE=NOT_SELECTED
BROAD_EXTERNAL_RESEARCH=NEXT
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```
## 63. Owner clarification: Research 124 is a whole-architecture redesign, not a weakness-patching exercise

Before broad external research begins, the project owner reasserted a critical design-freedom constraint.

The empirical baseline and current weakness list are **evidence**, not the boundary of what Research 124 is allowed to improve.

The redesign must not reason as follows:

```text
current architecture shows weakness A, B and C
    -> successor only needs to patch A, B and C
```

That would make the current architecture the hidden design frame and would contradict the opening owner mandate in Section 1.

The correct stance is broader:

```text
current weaknesses
    = concrete evidence about failure modes

current strengths
    = evidence about mechanisms that presently work

neither
    = an obligation to preserve the current architecture or its artifact families

future scenarios / scale / model changes / collaborator changes
    = legitimate design inputs even when no present failure has yet occurred
```

A component that currently works well may still be redesigned if a better architecture can provide stronger reliability, clarity, scaling, maintainability, usability or future robustness. Conversely, an existing mechanism should not be discarded merely for novelty when its current strengths remain valuable.

Research 124 therefore remains free to redesign **any part of the project-development knowledge architecture**, including:

```text
artifact families
knowledge-unit boundaries
subject/domain organization
history/current-state representation
promotion/consolidation lifecycle
routing and indexes
source/derived separation
authority/provenance representation
workstream/resume state
bootstrap and reconstruction surfaces
machine-queryable relationships
storage/retrieval mechanisms
migration and archival representation
```

This is permission to reason from first principles, not a direction to remove checkpoints, research files, foundations or any other current family.

The old architecture remains operational authority until a successor qualifies. Design freedom and migration safety are separate questions.

### 63.1 New architectural discriminator: artifact-family organization versus semantic knowledge organization

The owner also raised a concrete observation about how important project understanding is currently preserved.

Some of the project's most important knowledge is not primarily a task result, checkpoint, research experiment or implementation contract. It is **understanding about what ADS is, why it exists, how its system boundary should be understood, and how the project's vision evolves**.

The owner gave the distinction among:

```text
human-executed data-science project
human + interactive LLM project
ADS / system-mediated data-science project
```

as a representative example.

Repository inspection confirms that this exact concept currently has a multi-layer history:

```text
Checkpoint 022
    historical moment where the distinction became explicit

Foundation 013
    promoted durable canonical system-level interpretation

Knowledge Map
    semantic routing entry into the system-level vision material
```

Foundation 013 itself explicitly documents this preservation relationship: Checkpoint 22 retains historical provenance while Foundation 013 carries the durable system-level interpretation.

This is an example where the current architecture already performs a useful **historical-event -> durable-concept promotion**.

However, the owner's broader architectural question remains open. The current repository is primarily partitioned by artifact role/lifecycle:

```text
foundations       deep durable rationale
research          bounded evidence/candidates/investigations
specifications    scoped contracts
checkpoints       historical/continuity state
collaboration     review/coordination provenance
validation        exact evidence
```

Semantic subject routing is then overlaid through `KNOWLEDGE_MAP.md` and specialized indexes.

That means one conceptual subject can be distributed across many artifact families and historical records. The fact that this currently works in important cases does not establish that this is the best long-term knowledge architecture.

Research 124 should therefore treat the following as a first-class design question rather than assuming the answer:

> **What should be the primary identity of durable project knowledge: documents grouped by lifecycle/role, semantic subjects/concepts, explicit knowledge objects/claims/relationships, events plus materialized syntheses, some hybrid of these, or another representation?**

Subquestions include:

```text
Should durable concepts have identities independent of the files that currently contain them?

Should one subject expose current synthesis, governing decisions, exact evidence and history
as different views/depths rather than as separate manually navigated artifact families?

Should chronology remain a first-class preservation axis while semantic subject/domain becomes
a separate first-class retrieval/reconstruction axis?

Can historical provenance remain complete without forcing historical artifact structure to define
how current understanding is organized?

What knowledge deserves promotion into durable synthesis, and how should that synthesis evolve
without erasing the reasoning/history that produced it?

Can the architecture support important conceptual discussion that does not naturally begin as a
"research", "checkpoint" or "specification" object without losing it or forcing it into an ill-fitting family?
```

No answer is selected here. In particular, this section does **not** propose a subject-only architecture or the removal of current artifact families.

### 63.2 External-research consequence

Broad external research should not be constrained to mechanisms that repair the five currently strongest empirical weaknesses.

It should also ask what stronger architecture is possible even where the present system works, including literature/practice on:

```text
faceted classification and multiple simultaneous organizational axes
knowledge objects / conceptual identity independent of documents
knowledge graphs and provenance models
library/information-science subject organization
records management versus current knowledge representation
event history versus materialized current views
knowledge consolidation / promotion / synthesis lifecycle
software architecture patterns for source-of-truth plus generated views
personal/organizational knowledge systems that separate capture from durable synthesis
```

The objective remains the best justified project-development knowledge architecture for ADS at substantial future scale, not the smallest patch that resolves the current failure corpus.

```text
RESEARCH124_DESIGN_FREEDOM=WHOLE_ARCHITECTURE
CURRENT_WEAKNESSES=EVIDENCE_NOT_SCOPE_LIMIT
CURRENT_STRENGTHS=PRESUMPTION_FREE
CURRENT_ARTIFACT_FAMILIES=NOT_DESIGN_CONSTRAINT
SEMANTIC_KNOWLEDGE_ORGANIZATION=FIRST_CLASS_RESEARCH_QUESTION
CHECKPOINT_RESEARCH_FOUNDATION_REMOVAL=NOT_PROPOSED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=BROAD_QUESTION_DRIVEN_EXTERNAL_RESEARCH_FROM_OPEN_DESIGN_SPACE
```
## 64. Cross-disciplinary external evidence expands the design space

Research 125 now preserves the first broad external evidence field gathered after the internal failure corpus and historical baseline:

```text
docs/research/125_cross_disciplinary_external_evidence_for_project_knowledge_architecture.md
```

The research deliberately spans mature non-AI disciplines as well as modern LLM memory/retrieval work. Sources include information organization, library/reference models, provenance standards, digital preservation, records continuum theory, organizational memory, design rationale, human factors, temporal databases, software architecture documentation, reproducible/derived-state engineering, and recent hierarchical/global/local retrieval research.

The first important result is negative as well as positive:

> **No external framework should be copied wholesale, and the evidence does not identify one ready-made successor architecture.**

Instead, several independent disciplines converge on architectural distinctions that Research 124 should now treat as serious discriminators.

### 64.1 Concept identity versus artifact identity

SKOS and library/reference-model practice demonstrate mature ways to give concepts or intellectual entities identities independent of any one label or physical/document manifestation.

This does not imply an RDF/SKOS ontology. It strengthens the owner's Checkpoint 463 question about whether durable project understanding such as the ADS system identity should remain primarily identified by artifact-family files or instead have a stable conceptual identity with historical, current, evidentiary, and routing manifestations.

### 64.2 Multiple orthogonal views rather than one overloaded hierarchy

Faceted navigation, software architecture viewpoints, provenance models, temporal models, and library user-task frameworks all support the idea that several organizational axes can be valid at once:

```text
semantic subject
artifact / representation type
authority / maturity
chronology / validity
workstream / dependency
provenance / derivation
evidence depth
privacy / access
stakeholder / task viewpoint
```

This weakens any assumption that one directory hierarchy or one universal index should carry every navigation responsibility.

### 64.3 Capture, consolidation, and authority promotion are distinct functions

Organizational-memory and design-rationale research shows the value of capturing reasoning with low disruption. Modern AI memory systems independently show capture -> reflection/synthesis -> retrieval patterns. Preservation/provenance standards add the requirement that derived understanding remain traceable to source and transformation history.

Research 124 should therefore distinguish:

```text
capture
    !=
consolidation / synthesis
    !=
validation
    !=
authority promotion
```

This is directly relevant to important conversation-born insights that do not naturally begin as a Research, Foundation, Checkpoint, or Specification object.

### 64.4 Source knowledge and query-shaped derived views can be different layers

Materialized-view engineering, reproducible-build practice, OAIS descriptive information, and modern RAG indexes all provide precedents for durable source information plus query-optimized derived representations.

The useful transfer is not a database choice. It is the contract:

```text
canonical durable source
    -> declared transformation / indexing / consolidation
        -> rebuildable view or index
```

Derived state should not become a second accidental source of project truth merely because it is convenient or repeatedly used.

### 64.5 History and current understanding need not be the same representation

Preservation theory, PREMIS events, temporal database concepts, event-sourced projections, and the project's own checkpoint-to-foundation promotion examples all support separating historical provenance from current synthesis while keeping explicit lineage between them.

Research 125 also introduces a temporal question not yet modeled deeply in the repository: whether some knowledge needs separate semantics for when it became applicable and when the project learned/recorded it.

No bitemporal database or event-sourcing architecture is selected. Both are deliberately retained as conceptual evidence with strong complexity counterweights.

### 64.6 Reconstruction should be shaped by the task

IFLA user tasks, ISO architecture viewpoints, GraphRAG global/local modes, RAPTOR abstraction levels, and materialized views converge on a common design principle: broad orientation, exact governing-source resolution, exploratory discovery, and implementation-fidelity retrieval are different information tasks.

This strengthens the working reconstruction-planner idea while leaving its implementation open.

### 64.7 Activation is a workflow/control problem as well as a retrieval problem

NASA checklist research and FDA human-factors guidance reinforce the systems principle that making correct information available is weaker than making correct action naturally follow from the workflow/interface under real use conditions.

The transfer must remain calibrated: human aviation/medical cognition is not LLM cognition. The relevant architectural lesson is to reduce dependence on a collaborator remembering that a manual or governing source exists.

### 64.8 Vocabulary mismatch makes single-label discovery fragile

Classic HCI/IR evidence, SKOS labels, faceted search, and semantic retrieval research all indicate that users and systems may refer to the same concept through different language.

Exact paths and controlled terms remain valuable for precision, but aliases, lexical search, explicit relationships, semantic retrieval, and task context should be evaluated as complementary access mechanisms.

### 64.9 External evidence adds strong counterweights against overengineering

The same evidence field warns against maximal formalization:

```text
ontology / knowledge graph
    incurs evolution and governance cost

materialized views
    create refresh / consistency / validation obligations

event sourcing
    is explicitly high-complexity and often unjustified

design-rationale capture
    fails when recording friction is too high

LLM-generated summaries / graphs
    improve retrieval but do not provide authority safety by themselves
```

The successor should therefore optimize not only reconstruction quality but the marginal cost of capture, maintenance, consolidation, regeneration, validation, and migration.

### 64.10 Current evidence boundary

Research 125 Phase 1 establishes a broad independent field but intentionally stops before target synthesis.

The next evidence work should deepen the architecture discriminators where mechanism choice remains genuinely open:

```text
D1  stable knowledge identity
D2  multi-axis organization and views
D3  conversation-born capture -> consolidation -> promotion
D4  canonical source versus rebuildable derived state
D5  authority-aware retrieval and pre-action activation
D6  temporal / supersession semantics
D7  consolidation fidelity and provenance
D8  maintenance economics at 5x / 10x scale
```

After those deep dives, Research 124 should reconcile the internal requirements/invariants with their evidentiary provenance before architecture synthesis.

The owner paper/video remains intentionally withheld.

```text
CROSS_DISCIPLINARY_PHASE1=ESTABLISHED
WHOLE_ARCHITECTURE_DESIGN_SPACE=EXPANDED
TARGET_ARCHITECTURE=NOT_SELECTED
TARGET_ARCHITECTURE_DESIGN=PAUSED
NEXT=TARGETED_EVIDENCE_DEEP_DIVES
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```
## 65. D1-D2 deep dive: knowledge identity and multi-axis organization

Research 126 deepens the first two external-evidence discriminators:

```text
docs/research/126_knowledge_identity_and_multi_axis_organization_deep_dive.md
```

The evidence base now includes SKOS, Getty AAT, IFLA LRM, ICA Records in Contexts, CIDOC CRM and Wikidata/Wikibase. These systems differ substantially in purpose and implementation, but they converge strongly enough to constrain later candidate comparison without selecting a target architecture.

### 65.1 Stable semantic identity is not the same thing as a label, path or carrier

Across SKOS, Getty AAT, IFLA LRM, RiC and CIDOC CRM, the object being described is explicitly separable from one name, one hierarchy position or one physical/digital carrier.

This supports an architecture-neutral requirement for later reconciliation: when ADS deliberately regards some project knowledge as continuous across rename, relocation or representation change, the successor must not require semantic identity to be recreated merely because the current file/path changes.

The inverse is equally important: not every file, paragraph, heading or generated node deserves semantic identity.

### 65.2 Multi-membership is normal; one preferred route can remain a default

Getty AAT is polyhierarchical and allows one concept to have several valid parents while one is marked preferred for default display. RiC Record Sets can group the same record simultaneously in multiple contextual sets based on activity, subject, provenance or another purpose.

The useful project-level distinction is:

```text
preferred navigation route
    !=
exclusive semantic parent
```

This means deterministic project bootstrap and multi-axis semantic organization are not mutually exclusive.

### 65.3 Organizational/view nodes do not automatically become knowledge entities

Getty distinguishes indexable concept records from facets, guide terms and hierarchy names that exist only to organize the thesaurus. Research 126 therefore adds an explicit anti-test against ontology sprawl: a UI node, breadcrumb, generated cluster, convenience heading or display-only grouping normally remains a view/representation unless it has an independently meaningful lifecycle, provenance or cross-context identity.

### 65.4 Artifact identity and knowledge identity are separate concerns

RiC Record Resource/Instantiation and CIDOC Information Object/carrier distinctions make an important nuance explicit. An exact file may matter greatly for authority, source fidelity, provenance or reproducibility while still not being identical to the semantic knowledge it expresses.

A future candidate may therefore need both:

```text
artifact identity
    exact file / source / implementation / validation carrier

semantic identity
    concept, governed knowledge unit, activity/workstream or other persistent project thing
```

Whether both are implemented as explicit objects remains a later design choice.

### 65.5 Relation metadata is conditionally justified

RiC-O supports first-class relations with date, state, certainty and source/evidence. Wikidata independently shows statement-level qualifiers, references and rank.

This provides evidence for richer representation when the relation itself matters, for example:

```text
supersedes
governed-by
returns-to
depends-on
supports / evidence-for
reopens-when
```

It does not justify reifying every edge. A lightweight edge remains preferable where no relation-specific provenance, temporal state, certainty or lifecycle is needed.

### 65.6 Concept identity and claim identity remain distinct

The external evidence is strongest for stable identity of enduring concepts/resources. Statement-level models show that independently governed claims can also deserve metadata, but Research 126 rejects universal sentence/claim atomization as unsupported and likely maintenance-heavy.

Later candidate architectures should therefore justify identity granularity through an explicit test rather than assigning IDs indiscriminately.

### 65.7 Working identity test

Research 126 introduces a comparison test. A thing is a stronger candidate for independent project identity when several of these are true:

```text
it persists across label/path/representation change
multiple contexts need to refer to it
it has an independent lifecycle
it has multiple representations
important relationships attach to it directly
its provenance matters independently
conflating it with its carrier/group creates material ambiguity or loss
```

The test is architecture-neutral and intentionally has no frozen numeric threshold yet.

### 65.8 Minimal semantic-family envelope for later comparison

Without selecting an ontology, the evidence is now strong enough to require later candidates to test whether a small role set can cover the project before adding more types:

```text
subject / concept
independently governed knowledge unit
activity / workstream
evidence / source
representation / artifact
relation, usually lightweight and richer only when needed
```

This is a candidate-comparison envelope, not a selected schema.

### 65.9 Multi-axis view hypothesis is now evidence-backed

Later candidates should be able to compare projections such as:

```text
semantic
authority / epistemic state
workstream / dependency
provenance
temporal
artifact
reconstruction
privacy / access
```

The critical contract is that these remain views over one coherent project authority rather than manually synchronized competing truths.

### 65.10 D1-D2 stop rule and next boundary

The D1-D2 evidence now shows strong convergence. Additional general ontology examples are unlikely to alter the main conclusion enough to justify continued broadening before testing the next open mechanisms.

The next paired deep dive is:

```text
D3  conversation-born capture -> consolidation -> promotion
D4  canonical source versus rebuildable derived state
```

These belong together because capture/consolidation cannot be evaluated safely without deciding how transient, generated or probabilistic synthesis remains subordinate to explicitly promoted project authority.

Target-architecture synthesis remains paused. Requirements/evidentiary-provenance reconciliation still follows the complete targeted evidence set. The owner paper/video remains withheld.

```text
D1_D2_DEEP_DIVE=COMPLETE
KNOWLEDGE_IDENTITY_INDEPENDENT_OF_PATH=EVIDENCE_BACKED
MULTI_AXIS_ORGANIZATION=EVIDENCE_BACKED
PREFERRED_ROUTE_CAN_BE_DISPLAY_DEFAULT=true
UNIVERSAL_SEMANTIC_ATOMIZATION=NOT_JUSTIFIED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=D3_D4_CAPTURE_CONSOLIDATION_SOURCE_DERIVED_DEEP_DIVE
```
## 66. D3-D4 deep dive: capture, consolidation, promotion and source-derived state

Research 127 deepens the next paired discriminators:

```text
docs/research/127_capture_consolidation_promotion_and_source_derived_state_deep_dive.md
```

The evidence base combines OAIS, PREMIS, W3C PROV-O, SLSA provenance, reproducible-build practice, materialized-view/CQRS patterns, Python PEP governance, IETF maturity-process simplification, design-rationale research, and modern LLM reflection/memory systems.

### 66.1 Intake, durable knowledge and consumption views are different roles

OAIS provides the strongest new conceptual structure. It distinguishes submitted information (SIP), preservation-complete archival information (AIP), and consumer-shaped dissemination information (DIP). The packages have different information requirements, and ingest may transform, validate, enrich and audit submissions before they become preservation packages.

The transfer to Research 124 is architecture-neutral:

```text
captured/submitted reasoning
    !=
promoted durable knowledge
    !=
task-shaped reconstruction/dissemination view
```

Conversation-born insight therefore need not satisfy final authority requirements at the instant of capture, while a task-shaped context packet need not become project authority merely because it is useful to a model.

### 66.2 Consolidation may transform source material if lineage survives

OAIS ingest and provenance standards show that durable preservation can involve controlled transformation rather than literal copying. For ADS this keeps open model-assisted distillation, classification, conflict surfacing and relationship extraction, provided the resulting durable knowledge remains traceable to its source basis and preserves material uncertainty.

This does not yet establish how consolidation is implemented or validated.

### 66.3 Consequential transformations deserve provenance; routine operations need not

PREMIS records preservation Events with type, time, details, outcomes, Agents and Objects, while explicitly allowing less important actions to remain ordinary logs rather than first-class events.

Research 124 should therefore preserve provenance for authority-significant transformations such as promotion, supersession, migration, repair and material consolidation without turning every read, retrieval or chat message into a permanent project event.

### 66.4 Generated outputs need source lineage and transformation lineage

W3C PROV-O and SLSA independently model not only which input an output derives from but also the process/activity, producing agent/platform and material parameters/dependencies involved in generation.

For later candidate comparison, ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“generated from the repositoryÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â is insufficient when a derived representation materially affects reconstruction. The candidate should be able to establish a proportionate provenance envelope over sources, generator/transformation and freshness.

### 66.5 Rebuildability has several strengths

Research 127 introduces three comparison classes rather than treating rebuildability as binary:

```text
R0  SOURCE-BOUND
    source/provenance known; repeat generation not promised

R1  REGENERABLE
    authoritative inputs + versioned transformation can produce a fresh
    semantically equivalent representation

R2  DETERMINISTICALLY REPRODUCIBLE
    authoritative inputs + transformation are expected to produce the same
    machine-significant result, subject to declared normalization
```

Structural routing/index/manifests should normally aspire to R2. Probabilistic LLM synthesis may realistically satisfy R1, with semantic review more important than byte identity.

### 66.6 Derived read state should normally be disposable and non-authoritative

Materialized View guidance explicitly treats a view as disposable and rebuildable from source stores, and says applications do not update it directly. CQRS independently separates command/write models from query/read models and warns about eventual consistency and complexity.

This strengthens a later candidate discriminator:

```text
authority-bearing knowledge mutation path
    !=
query/reconstruction/index path
```

No separate database or CQRS implementation is implied.

### 66.7 Discovery through synthesis is not authority through synthesis

LLM-generated reflection may reveal genuinely novel useful conclusions. The safe lifecycle is:

```text
derived insight
    -> candidate capture with provenance
        -> proportionate review / validation
            -> explicit promotion to durable authority
                -> future views may derive from the promoted knowledge
```

A generated cache or summary does not silently acquire authority because humans/models repeatedly consult it.

### 66.8 Promotion is an explicit authority transition

PEP 1 shows a mature distinction between discussion, draft proposal, acceptance, implementation/finality, rejection and historical rationale. It also preserves rejected ideas because the rationale prevents rediscovery, while current formal behavior may be documented elsewhere after resolution.

The project therefore needs a promotion boundary capable of establishing source basis, resulting epistemic/authority status, unresolved uncertainty, supersession/complement relationships and provenance.

IETF RFC 6410 supplies an important counterweight: mature governance deliberately simplified its maturity ladder when too many progression levels became burdensome. Any ADS lifecycle taxonomy must remain minimal.

### 66.9 Low-friction capture and selective promotion are compatible

DRed/design-rationale evidence supports unobtrusive capture while substantive work proceeds. PEP and PREMIS practice simultaneously show that not every idea/action deserves the strongest durable governed representation.

The successor should therefore be evaluated on whether important insight can enter the knowledge lifecycle cheaply without automatic authority or unbounded permanent capture.

### 66.10 D3-D4 constraints

Research 127 freezes architecture-neutral constraints D3-C1 through D3-C7 and D4-C1 through D4-C8. The most important are:

```text
capture does not imply authority
capture / consolidation / validation / promotion are distinguishable
promotion of unique durable understanding is explicit and source-traceable
rejected/superseded rationale may remain durable without remaining current authority
status vocabularies should remain minimal
full indefinite capture of every token/result is not justified

derived views normally remain read-oriented
material derived state needs source binding, transformation identity and freshness
loss of a derived store must not destroy unique accepted truth
probabilistic synthesis needs provenance-complete regeneration rather than false byte-repeat claims
generated unique accepted insight must cross an explicit promotion boundary
task-shaped views may summarize/reorganize authority without becoming authority
hidden material inputs weaken rebuildability
required freshness must fail visibly when it cannot be established
```

### 66.11 Stop rule and next boundary

The D3-D4 evidence now converges strongly enough that more broad examples are unlikely to change the architecture-level result before the remaining discriminators are examined.

The next paired deep dive is:

```text
D5  authority-aware retrieval and pre-action activation
D6  temporal / supersession semantics
```

They are coupled because resolving which source governs a task depends on scope, applicability time, supersession and current-versus-historical state.

D7 consolidation fidelity/provenance and D8 maintenance economics remain after D5-D6. Requirements/evidentiary-provenance reconciliation follows the targeted evidence set. Target-architecture synthesis remains paused. The owner paper/video remains withheld.

```text
D3_D4_DEEP_DIVE=COMPLETE
CAPTURE_DOES_NOT_IMPLY_AUTHORITY=true
PROMOTION_IS_EXPLICIT_AUTHORITY_TRANSITION=true
DERIVED_STATE_UNIQUE_TRUTH=NOT_ALLOWED_WITHOUT_PROMOTION
REBUILDABILITY_LEVELS=REFINED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=D5_D6_AUTHORITY_ACTIVATION_TEMPORAL_SUPERSESSION_DEEP_DIVE
```
## 67. D5-D6 deep dive: authority-aware activation and temporal/supersession semantics

Research 128 deepens the paired authority/temporal discriminators:

```text
docs/research/128_authority_activation_and_temporal_supersession_deep_dive.md
```

The evidence base combines NIST ABAC, OASIS XACML, Open Policy Agent, Kubernetes admission control, temporal-database concepts, RFC Editor update/obsolescence relationships, Wikidata evolving-knowledge semantics and W3C PROV-O revision/invalidation provenance.

### 67.1 Relevance retrieval and authority resolution are now formally distinct

NIST ABAC provides a mature contextual-decision precedent: authorization depends on attributes of the actor, object, requested operation and environment rather than on broad topical similarity alone. Transferred cautiously, this strengthens an ADS distinction that was previously mostly internal:

```text
relevance retrieval
    finds knowledge likely useful to understanding the task

authority resolution
    determines which knowledge is required/allowed to govern the exact
    action, target, scope, state and time
```

Probabilistic retrieval may nominate candidates; it may not silently settle consequential authority when explicit applicability semantics exist.

### 67.2 Authority resolution should be action-shaped

Later candidates should demonstrate how they represent the semantic equivalent of:

```text
requested action / operation
affected target and scope
current environment / project state
actor or collaborator role when relevant
consequence class
time query when current versus historical authority matters
```

and return a governed result containing the applicable source set, why it applies, how sources combine/supersede, required checks/consumption, and unresolved conflicts or unavailable evidence.

This is not a selected API or rule schema.

### 67.3 Decision, administration and enforcement are separate concerns

XACML distinguishes Policy Administration Point, Policy Decision Point and Policy Enforcement Point. OPA independently separates policy decision-making from the application that enforces the decision.

This gives external precedent for the Research 124 working reasoning-control decomposition:

```text
governing knowledge/policy administration
    !=
authority-resolution decision
    !=
action enforcement / required-source consumption
```

The same physical component may perform more than one role; the semantic separation is what matters.

### 67.4 Ambiguity and absence should be first-class resolution outcomes

XACML preserves `NotApplicable` and `Indeterminate` outcomes and includes an `only-one-applicable` combination rule that becomes indeterminate when more than one policy applies where exactly one was expected.

Transferred to ADS, later candidates should be able to distinguish:

```text
resolved governing authority
no special governing authority applicable
conflicting / ambiguous authority
known required authority unavailable / unreadable / stale
```

The architecture should not resolve ambiguity by silently blending plausible sources.

### 67.5 Governing authority may be a source set rather than one document

XACML's policy-combining problem and RFC Editor `Updates` semantics both demonstrate that several sources may remain jointly necessary.

Research 128 therefore rejects a hidden assumption that every action maps to one governing artifact. A correct result may be one source, a base source plus mandatory updates/supplements, default project rules only, or an unresolved state.

The preferred result remains the smallest source set that completely covers the action.

### 67.6 Pre-action activation has mature systems precedent

Kubernetes admission controllers intercept mutation requests after authentication/authorization but before persistence. ValidatingAdmissionPolicy can scope checks to particular operations/resources, deny, warn or audit, and choose fail-closed or fail-open behavior on policy-evaluation errors.

For ADS, the transfer is a **bounded pre-action gate**:

```text
intended action classified
    -> applicable governing-source obligations resolved
        -> availability/freshness established
            -> required source consumption evidenced
                -> action/proposed guidance checked against the contract
                    -> proceed / warn / refuse / escalate
```

This is stronger than cold-start orientation and stronger than merely proving that a runbook was read.

### 67.7 Activation must bind to the action contract

BL-001 showed that correct runbook discovery and consumption can still be followed by an incorrect ordered response. Research 128 therefore sharpens activation:

> **Source consumption alone is not sufficient when correctness depends on preserving a concrete action contract.**

Later candidates should show how high-consequence procedures or mutations can check the proposed action against the governing procedure/preconditions before dispatch or final guidance.

This need not imply deterministic checking of all free-form reasoning.

### 67.8 Enforcement strength should be consequence-sensitive

Kubernetes offers Deny/Warn/Audit and Fail/Ignore policy behaviors. That is useful evidence against one universal ADS behavior.

A future candidate must explain how optional exploratory knowledge gaps differ from missing authority for a mutation, operational procedure, scientific conclusion or authority promotion.

Research 128 keeps the exact consequence taxonomy open but requires the failure/enforcement policy to be explicit and proportionate.

### 67.9 Applicability time and recording time are different semantics

Temporal-database literature distinguishes valid/business time from transaction/system time:

```text
when was the fact/rule true or applicable?
    !=
when was it recorded/known by the information system?
```

Research 124 should therefore permit project knowledge to answer both when the distinction matters. A late-discovered external change or retroactive correction can otherwise make historical reconstruction ambiguous.

Full bitemporal storage is not justified for every knowledge item.

### 67.10 Authority-transition time is another project concept

In project governance there can also be a meaningful difference between when a fact externally applies and when ADS accepts/promotes/supersedes a project representation as governing.

Research 128 therefore keeps three conceptual questions distinct without requiring three persisted timelines everywhere:

```text
domain / applicability time
repository knowledge / recording time
authority transition time
```

Candidates may collapse them where project semantics make them identical.

### 67.11 Replacement and supplementation are materially different

RFC Editor metadata distinguishes `Obsoletes` from `Updates`:

```text
Obsoletes
    newer document replaces older document for current practice,
    while the old document remains permanently archived

Updates
    newer document modifies/adds to older document;
    current understanding may require both
```

This means a generic `supersedes` relation may be insufficient for ADS if current authority depends on whether an older source remains partly governing.

Candidate relation vocabularies must remain minimal, but they must preserve the distinctions real project cases need.

### 67.12 Historical validity is not the same as known-wrong knowledge

Wikidata's evolving-knowledge guidance separates formerly valid historical values, currently preferred values and deprecated mistakes/dismissed beliefs.

Research 128 therefore strengthens the epistemic distinction:

```text
historically/formerly applicable
    !=
superseded as current project authority
    !=
rejected / known wrong
    !=
current accepted / preferred
```

Old authority should remain discoverable for audit/history without entering ordinary current reconstruction by default.

### 67.13 ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œCurrentÃƒÂ¢Ã¢â€šÂ¬Ã‚Â cannot mean merely ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œlatest commitÃƒÂ¢Ã¢â€šÂ¬Ã‚Â

Current governing truth may depend on:

```text
scope
epistemic / lifecycle status
temporal applicability
replacement versus supplementation
precedence / authority class
availability/freshness of required source
```

A generated current-state view can therefore be built from the latest Git revision and still be semantically wrong if its derivation ignores these relations.

### 67.14 D5-D6 constraint boundary

Research 128 freezes D5-C1 through D5-C9 and D6-C1 through D6-C8 for later requirements/evidentiary-provenance reconciliation. The deepest new constraints are:

```text
retrieval != authority resolution
authority resolution is action/context shaped
governing result can be a source set
combination/supersession semantics are explicit
ambiguity/unavailability are fail-visible
source consumption must bind to consequential action contract
failure policy is consequence-sensitive
decision and enforcement are separable

applicability time != repository knowledge time
historical validity != epistemic deprecation
replacement != update/supplement
current authority != recency
historical authority remains identifiable
strong temporal machinery is selective, not universal
```

### 67.15 Stop rule and next boundary

D5-D6 now have strong cross-domain convergence. More general access-control or temporal examples are unlikely to alter the architecture-level conclusion before the final discriminators are researched.

The next paired deep dive is:

```text
D7  consolidation fidelity and provenance
D8  maintenance economics at 5x / 10x scale
```

They belong together because richer knowledge structure and automated consolidation are only improvements if they preserve semantic fidelity and remain economically/operationally maintainable as the corpus grows.

After D7-D8, Research 124 should perform the planned requirements/evidentiary-provenance reconciliation before architecture synthesis.

Target-architecture synthesis remains paused. The owner paper/video remains withheld.

```text
D5_D6_DEEP_DIVE=COMPLETE
RELEVANCE_RETRIEVAL_NE_AUTHORITY_RESOLUTION=true
ACTION_SHAPED_AUTHORITY_RESOLUTION=EVIDENCE_BACKED
PRE_ACTION_GATING=EVIDENCE_BACKED_AS_SYSTEMS_PATTERN
TEMPORAL_APPLICABILITY_NE_RECORDING_TIME=true
REPLACEMENT_NE_SUPPLEMENTATION=true
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=D7_D8_CONSOLIDATION_FIDELITY_MAINTENANCE_ECONOMICS_DEEP_DIVE
```

## 68. D7-D8 deep dive: consolidation fidelity, provenance, and maintenance economics

Research 129 completes the final planned targeted external-evidence pair:

```text
docs/research/129_consolidation_fidelity_provenance_and_maintenance_economics_deep_dive.md
```

The evidence combines summarization factuality and content-coverage evaluation, Cochrane systematic-review extraction/reconciliation and certainty practice, long-context LLM research, materialized-view maintenance, incremental computation/build-system dependency ideas, ontology evolution and the provenance work already established in Research 127.

### 68.1 Consolidation fidelity is multidimensional

External summarization research distinguishes factual consistency from content selection/coverage. A synthesis can avoid hallucination yet still fail by omitting a critical unit. Cochrane evidence-synthesis practice further shows that uncertainty, inconsistency and disagreements must be represented rather than flattened.

Research 129 therefore defines a candidate-comparison fidelity envelope across:

```text
source support
coverage / completeness
epistemic uncertainty and disagreement
authority state
material relationships
temporal meaning
negative / minority evidence
provenance drill-down
task / abstraction contract
```

This is not a universal scorecard to store on every summary.

### 68.2 High-consequence consolidation needs proportionate reconciliation

Cochrane recommends independent duplicate extraction for subjectively interpreted and result-critical information because extraction errors may survive ordinary downstream review. Long-document summarization research independently shows that factuality evaluation is itself difficult and that automatic metrics have important limitations.

The project should therefore reject one unverified generative pass as sufficient qualification for high-consequence knowledge promotion. Possible mechanisms remain open: independent model extraction/reconciliation, deterministic must-preserve-unit checking, owner review for authority promotion, or combinations.

### 68.3 Compression is allowed only under an explicit view contract

A useful summary necessarily omits detail. The safe principle is:

> Compression may remove detail from an active representation when the detail remains durably recoverable and every semantic property required by that representation's declared use is preserved.

Project orientation, an operational procedure, an authority synthesis and a historical narrative have different must-preserve units.

### 68.4 Long context is not a scaling substitute

Long-context research shows that models can use large contexts unevenly and that adding more retrieved material can give diminishing returns. At 5x/10x scale the architecture should therefore continue to optimize task-shaped reconstruction and active-surface size rather than relying on larger raw context windows as the primary escape hatch.

### 68.5 Current empirical scaling pressure is already visible

At Checkpoint 467 the repository has approximately:

```text
1,554 tracked files
1,018 docs/ files
1,040 Markdown files
9.4 MiB Markdown
468 numbered checkpoints
128 numbered Research records
318 direct development-governance paths in the Knowledge Map
```

A deliberately simple linear-pressure thought experiment yields at 10x roughly:

```text
15,540 tracked files
10,180 docs/ files
10,400 Markdown files
93.9 MiB Markdown
4,680 numbered checkpoints
1,280 Research records
3,180 direct development-governance paths
```

These are not forecasts or target artifact ratios. They expose why storage capacity is not the primary risk. Active routing, maintenance fan-out, semantic review and reconstruction cost become the important scaling variables.

### 68.6 Maintenance cost should track the affected dependency neighborhood

Materialized-view maintenance and self-adjusting-computation research provide a strong general systems principle: when a small source change affects only part of a derived computation, update the affected dependency neighborhood rather than recomputing or manually revisiting everything.

Research 129 therefore strengthens KA-I13 and related requirements:

```text
ordinary local change cost
    should normally depend on affected semantic/dependency fan-out
    rather than total accumulated corpus size
```

Periodic automated full rebuilds and full qualification can still be legitimate.

### 68.7 Rich structure must pay for itself

Ontology-evolution research and view-maintenance economics provide a counterweight to semantic overengineering. Every new universal entity type, relation type, lifecycle state, generated view and integrity rule creates capture, evolution, validation and migration cost.

A later candidate must therefore optimize total lifecycle economics rather than one local objective.

Research 129 introduces the comparison decomposition:

```text
C_capture
C_rel
C_change
C_propagate
C_validate
C_consolidate
C_reconstruct
C_migrate
C_failure
```

A design that sharply reduces reconstruction cost while exploding metadata/relationship/validation maintenance is not automatically superior.

### 68.8 Active-surface economics are separate from archival economics

Cheap storage does not mean cheap reasoning. The architecture needs separate metrics for archival corpus size and the amount/fan-out of knowledge that remains active in bootstrap, routing and ordinary reconstruction.

Consolidation is therefore a recurring control loop rather than only a one-time migration activity:

```text
accumulation
    -> measurable active-surface pressure
        -> consolidation candidate
            -> fidelity qualification
                -> detail becomes latent/history
                    -> provenance remains traversable
```

### 68.9 D7-D8 constraints and qualification metrics

Research 129 freezes D7-C1 through D7-C10 and D8-C1 through D8-C12 for requirements reconciliation. It also introduces candidate-scale metrics including manual-touch fan-out, generated-view fan-out, incremental/full rebuild cost, validator footprint, semantic-review burden, active-route/context size, cold-start reconstruction cost, authority-resolution cost, consolidation cost, stale-view repair latency and schema-migration footprint.

These become important later when candidate architectures are stress-tested on 5x/10x synthetic states.

### 68.10 Targeted evidence stop rule

The planned D1-D8 evidence program is now complete:

```text
Research 126   D1-D2
Research 127   D3-D4
Research 128   D5-D6
Research 129   D7-D8
```

Continuing broad external collection now risks diminishing returns and confirmation bias.

The next phase is **requirements/evidentiary-provenance reconciliation**, not target design. The 45 requirements and 15 invariants frozen before external research must be systematically revisited against:

```text
owner goals
internal historical failure evidence
blind baseline evidence
D1-D8 external evidence
analogy strength / transfer limits
redundancy / solution-shaping risk
normative strength: MUST / SHOULD / MAY / discriminator
```

Target architecture synthesis remains paused. The owner paper/video remains withheld until the reconciliation establishes the independent evidence field cleanly enough to assess its incremental contribution.

```text
D7_D8_DEEP_DIVE=COMPLETE
TARGETED_EXTERNAL_EVIDENCE_D1_D8=COMPLETE
CONSOLIDATION_FIDELITY=MULTIDIMENSIONAL
ROUTINE_MAINTENANCE_SHOULD_BE_DEPENDENCY_LOCAL=true
ACTIVE_SURFACE_COST_NE_ARCHIVAL_STORAGE_COST=true
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REQUIREMENTS_EVIDENTIARY_PROVENANCE_RECONCILIATION
```
## 69. Provisional requirements reconciliation V0.2 complete

Research 130 performs the planned post-evidence reconciliation:

```text
docs/research/130_requirements_evidentiary_provenance_reconciliation.md
```

The reconciliation compares all 45 original KA-R requirements and 15 KA-I invariants against owner intent, historical failures, blind baseline evidence and D1-D8 external evidence.

The original boundary remains substantially sound, but later evidence requires several material calibrations.

Most importantly, Research 130 rejects the hidden Phase-B assumption that every narrow consequential task must first reconstruct the full Tier-A project orientation. BL-001 shows that overly broad reconstruction can reduce exact task fidelity, while BL-003 shows that broad orientation is recoverable but can be expensive. The proposed V0.2 rule is therefore:

```text
generic continuation / cold start
    -> broad project orientation required

narrow governed task
    -> task-shaped minimum safe orientation required
       sufficient to establish current state, scope, authority and uncertainty
```

Research 130 also strengthens consequential authority preflight. Resolving and reading the right source is not enough when correctness depends on a concrete procedure/contract; the governing contract must be bound closely enough to the proposed action/guidance that material conformance can be checked.

Five explicit requirements are proposed because the original 45 do not cleanly express later evidence:

```text
KA-R46  representation-independent continuity of identity
KA-R47  multi-axis organization without truth duplication
KA-R48  capture / consolidation / promotion boundary
KA-R49  selective temporal and supersession semantics
KA-R50  recurring active-surface consolidation lifecycle
```

Two invariants are proposed:

```text
KA-I16  capture does not imply authority
KA-I17  intended semantic continuity is not forced to equal carrier continuity
```

The proposal therefore contains 50 requirements and 17 invariants if accepted. No original requirement is simply deleted; several are refined, conditionalized or reclassified as qualification requirements.

The most important weakening/calibration is that the current architecture is not treated as broadly unreconstructable. The redesign objective is reliability, task fidelity, context/maintenance economics and future robustness rather than repairing a system that cannot preserve project understanding at all.

The most important strengthening is around action fidelity, stable semantic identity, source-set authority, temporal meaning, consolidation fidelity and dependency-local maintenance.

Research 130 remains deliberately provisional because this is the first point where the evidence program proposes revising a previously frozen owner-facing requirement boundary. The project owner should review the major calibrations before V0.2 becomes the new frozen acceptance boundary.

Until owner acceptance/amendment:

```text
original Phase-B requirements/invariants
    remain the last frozen boundary

Research 130 V0.2
    remains the proposed evidence-reconciled successor boundary
```

Target architecture design remains paused and the withheld owner paper/video remains unexposed.

```text
REQUIREMENTS_RECONCILIATION=PROVISIONAL_V02_COMPLETE
PROPOSED_REQUIREMENTS=50
PROPOSED_INVARIANTS=17
OWNER_REVIEW=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```
## 70. Requirements V0.2 owner acceptance and freeze

The project owner explicitly accepted the Research 130 reconciliation without amendment.

The current frozen requirements boundary is now:

```text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
```

It contains:

```text
50 KA-R requirements
17 KA-I invariants
```

The original Phase-B KA-R01..KA-R45 and KA-I01..KA-I15 wording remains durable historical provenance in this Research 124 record, but it is superseded for candidate-design and qualification purposes by V0.2.

The owner accepted four important decisions:

```text
1. Generic continuation/cold start requires broad project orientation.
   Narrow governed work may instead use task-shaped safe orientation sufficient
   for state, scope, authority and uncertainty.

2. KA-R46..KA-R50 and KA-I16..KA-I17 are accepted.

3. No original requirement needs to remain deliberately stronger than the
   evidence-reconciled V0.2 boundary as an additional owner-value override.

4. Candidate eligibility remains intentionally broad enough for radically
   different successor architecture families to compete.
```

This freeze still does not select a target architecture, artifact family, ontology, database, retrieval mechanism or control-plane implementation.

The anti-anchoring condition for the owner-provided paper/video is now satisfied. The source may be introduced **after** this independent internal/external evidence and requirements boundary has been durably frozen, and its contribution should be evaluated incrementally:

```text
what does it add?
what does it contradict?
what does it independently reinforce?
what important requirement/discriminator does it expose that V0.2 missed?
what mechanism does it advocate that should remain only a candidate rather than a requirement?
```

Only after that incremental-source evaluation should Research 124 construct several neutral candidate architecture families and begin comparative synthesis.

```text
REQUIREMENTS_V02=OWNER_ACCEPTED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
ANTI_ANCHORING_SOURCE_GATE=OPEN
NEXT=WITHHELD_OWNER_SOURCE_INCREMENTAL_EVALUATION
```

## 71. Owner-provided ICM source evaluated incrementally; candidate architecture synthesis next

The project-owner-provided Interpretable Context Methodology material has now been evaluated at the anti-anchoring boundary preserved by Checkpoint 470. Detailed evidence is preserved in:

```text
docs/research/131_owner_provided_icm_source_incremental_evaluation.md
```

The evaluation treats the ICM paper and the current `RinDig/icm-architect` repository as incremental evidence only. The owner did not recommend adoption, and Research 124 does not reinterpret the preceding failure corpus, blind baselines, D1-D8 research or frozen V0.2 requirements as though ICM had guided them. The supplied Instagram account/reel remained unavailable for direct inspection through the active retrieval surfaces, so no unseen video content is used as evidence.

The strongest ICM contribution is independent convergence plus implementation concreteness. Its small payload-light catalogs, layered task-shaped context, stage contracts, one-home-per-fact discipline, generated views, cold-agent walk tests and dependency-local change-impact reasoning strongly reinforce conclusions Research 124 had already reached independently around bounded bootstrap, progressive disclosure, source-versus-derived state, reconstruction qualification and dependency-local maintenance.

Several mechanisms remain worth carrying into later architecture design without becoming requirements or a bundled ICM adoption:

```text
positive + negative context contracts, including explicit do-not-load boundaries
routing-payload pressure as an active-surface smell
repeating-unit-first representation choice
ghost / represented-but-not-wired diagnostic state
forward + reverse dependency/reference walks
copy -> verify parity -> remove migration discipline
source-map-like semantic provenance for consequential transformations
cross-stage verification contracts
repeated downstream correction -> governed source-improvement proposal
```

ICM also provides useful counter-evidence against overgeneralization. Its paper primarily targets sequential, repeatable, human-reviewed workflows; its empirical observations are preliminary rather than controlled; and its filesystem-first state/orchestration model does not by itself solve the broader ADS requirements around representation-independent identity, action-shaped authority source sets, temporal/supersession semantics, multi-workstream DAG continuation, interruption recovery, concurrent collaborators, public/private governance or qualified authority migration.

The requirement disposition is therefore unchanged:

```text
REQUIREMENTS_V02_AMENDMENT=NO
REQUIREMENTS_COUNT=50
INVARIANTS_COUNT=17
ICM_TARGET_SELECTION=NO
TARGET_ARCHITECTURE=NOT_SELECTED
```

The owner-source gate is now complete. Research 124 may resume architecture construction, but the next phase must follow the methodology correction already preserved in Sections 48 and 51: reason deeply from the complete evidence and frozen requirements, construct materially different serious alternatives to expose assumptions and trade-offs, use prototypes and shared stress tests for falsification/qualification, and only later narrow toward a coherent target. It must not turn into a shallow architecture tournament and must not make ICM the default candidate merely because it was owner-provided last.

```text
OWNER_SOURCE_INCREMENTAL_EVALUATION=COMPLETE
RESEARCH131=COMPLETE
REQUIREMENTS_V02=UNCHANGED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CANDIDATE_ARCHITECTURE_SYNTHESIS
```

## 72. MC-0012 opens staged Claude reassessment before architecture synthesis

Before beginning serious candidate architecture synthesis, the project owner asked whether Claude should contribute at the current boundary. Repository-native collaboration evidence showed an important asymmetry: Claude's MC-0011 position was preserved before the empirical failure corpus, blind baseline program, Research 125-129 external evidence, Research 130 reconciliation, Requirements V0.2 freeze and the later owner-source exposure. Claude therefore had not yet evaluated most of the evidence that now constrains the design space.

The owner explicitly authorized a new bounded collaboration rather than reopening MC-0011. MC-0012 uses staged information control:

```text
PHASE 1
    exact substantive evidence snapshot:
    d9794a880ad0b235102fc752dae91bde6c29bd24

    Claude evaluates:
        post-MC-0011 empirical audits
        historical failure corpus
        BL-001 / BL-002-B / BL-002U / BL-003 / BL-004
        Research 125-129
        Research 130
        frozen Requirements V0.2

    Claude does NOT see:
        owner-source identity/content
        Research 131
        Checkpoint 471 post-source conclusions
        descendant Research 124 source-evaluation material

PHASE 2
    may be opened only after Claude Message 001 is durably frozen
    and ChatGPT dispositions the Phase-1 contribution

    then the owner source can be exposed explicitly so its incremental
    contribution can be separated from the larger evidence-program update
```

This creates a stronger evidence chain than moving directly from MC-0011 to post-source Claude review:

```text
Claude MC-0011
    pre later empirical/external evidence
    pre owner source
        ->
Claude MC-0012 Phase 1
    post evidence + post V0.2 freeze
    still pre owner source
        ->
Claude MC-0012 Phase 2
    post owner source
        ->
ChatGPT/Claude reconciliation
        ->
architecture synthesis
```

The current coordination branch already contains Research 131, so Phase 1 cannot safely use current HEAD as its substantive evidence base. MC-0012 therefore permits current-branch reads only for collaboration routing and binds all substantive Phase-1 project reasoning to the exact pre-source-evaluation snapshot. Unexpected descendant/post-exposure leakage invalidates the phase rather than being mentally ignored.

The Phase-1 questions are deliberately broader than ICM. They ask Claude to reassess its own MC-0011 positions against the density audits, failure corpus, blind baselines, D1-D8 external research and the full V0.2 requirement/invariant set; distinguish owner constitutional choices from external empirical claims; challenge solution-shaping risk; state remaining uncertainty; and freeze pre-exposure revision predictions before any source identity is disclosed.

This is a bounded collaboration gate, not a general requirement that Claude approve Research 124. Candidate architecture synthesis is paused only until the staged reassessment supplies the missing second-model evidence or fails visibly.

```text
MC0012=OPEN
MC0012_PHASE1=POST_EVIDENCE_PRE_OWNER_SOURCE_REASSESSMENT
PHASE1_REVIEW_BASE=d9794a880ad0b235102fc752dae91bde6c29bd24
CLAUDE_SESSION=claude-03
OWNER_SOURCE_EXPOSURE_TO_CLAUDE=PAUSED_UNTIL_MESSAGE_001
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MC0012_MESSAGE_001
```

## 73. MC-0012 Phase 1 accepted; controlled owner-source exposure opens

Claude Message 001 is durably preserved as the post-evidence/pre-owner-source comparison point. It is valid and materially useful. The main update is epistemic calibration: Claude explicitly retracts the stronger MC-0011 implication that situation dispatch is a reliably recurring dominant failure mechanism, recognizes BL-001 post-activation task-contract fidelity as a distinct and stronger empirical result, and reframes current architecture weakness as expensive/fragile reconstruction plus measurable active-surface scaling pressure rather than present-day inability to reconstruct.

ChatGPT's Phase-1 disposition preserves several corrections and qualifications before exposing the source.

First, Claude's claimed unresolved checkpoint-granularity blocker is not actually open at this boundary. Research 124 Sections 52-53, inside the exact frozen target Claude read, already contain the bounded empirical audits:

```text
34-checkpoint 2026-09-09 audit
    -> no evidence that obvious systematic checkpoint micro-iteration abuse explains
       the high count; sampled records largely represent distinct serialized risk gates

298-path development-governance audit
    -> 236 / 298 = 79.2% checkpoint + validation evidence
    -> historical/evidence material is exposed at the same navigation depth as current
       synthesis/procedure/orientation

combined bounded finding
    -> active/navigation-surface accumulation is the stronger measured pressure
       than simply creating fewer checkpoints
```

Claude's failure to retrieve this finding from a file it was required to read is itself a useful example of evidence-depth/task-fidelity limits, not a reason to reopen the research question as though no verdict existed.

Second, Claude correctly identifies that the historical blind baseline is ChatGPT-only. Checkpoint 457 records that this was an explicit project-owner scope decision. The current `claude-03` interaction cannot now run a clean Claude blind replication because it has read the protocol and all evaluations. A future cross-model study would require a fresh uncontaminated Claude environment and separate owner-approved protocol; it is not inserted as a blocker here.

Third, Claude's V0.2 critiques are carried forward mainly as candidate-design/qualification pressure rather than requirement amendments: break the potential circularity in governing/risk-bearing discovery, keep receipt semantics representation-neutral, preserve evidence-class visibility near requirement consumption, measure dispatch reliability when candidates claim improvement, govern semantic identity merge/split carefully, and make `C_failure` consequence-aware rather than symbolic.

No Phase-1 evidence justifies changing the frozen 50 KA-R / 17 KA-I boundary before the source comparison.

MC-0012 Phase 2 now exposes the owner-provided ICM source to Claude while preserving one remaining independence boundary: Claude must form and freeze its own direct post-source assessment before reading ChatGPT's Research 131, Checkpoint 471 owner-source synthesis or this Research 124 record's Section 71 interpretation.

```text
MC0012_PHASE1=COMPLETE_VALID
MC0012_PHASE2=OWNER_SOURCE_INDEPENDENT_INCREMENTAL_EVALUATION_ACTIVE
REQUIREMENTS_V02_AMENDMENT=NO
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MC0012_MESSAGE_003
```

## 74. Cross-model owner-source reconciliation complete; synthesis resumes

MC-0012 completed the intended staged comparison. Claude first updated its MC-0011 position against the full pre-source Research 124 evidence field, then independently inspected ICM while ChatGPT's Research 131 interpretation remained withheld. Research 132 reconciles the two post-source assessments.

The models strongly converge: ICM independently reinforces bounded routing, task-shaped context, source/derived separation, cold-agent qualification, dependency-local maintenance and move/reference integrity; its current repository is materially richer than the original paper; its empirical evidence is preliminary; and its sequential human-reviewed workflow class is narrower than the ADS project-development knowledge problem. Neither model recommends reopening V0.2 or selecting ICM as the target.

Claude adds useful candidate-level calibration: ICM's L0/L1 routing layers total roughly 500-1,300 tokens as one external benchmark; verified System-map cards require freshness/revision/citation evidence while `stale` remains explicit; repeated independent observations are a better basis for structural pattern claims than one memorable incident; ICM's human gates often sidestep rather than test ADS situation-dispatch/task-fidelity failures; factory/product is a different axis from source/derived authority; and file-move continuity does not solve semantic identity merge/split governance.

Research 131's complementary mechanisms remain live, including negative context contracts, routing-payload pressure, repeating-unit-first representation choice, repeated-correction source-improvement proposals, semantic-debugging/source-map provenance and forward/reverse impact walks.

No further MC-0012 round is required. The remaining issues are named candidate-design/qualification risks rather than missing evidence-program gates: identity merge/split governance, ChatGPT-only historical baselines, KA-R07 authority-discovery circularity, evidence-class visibility at consumption, dispatch reliability metrics and consequence-aware `C_failure` calibration.

Research 124 can now resume serious candidate architecture synthesis. Multiple materially different architecture families or mechanism combinations should be constructed to expose assumptions and trade-offs, not to create a shallow score-and-pick tournament. The frozen 50 KA-R / 17 KA-I boundary remains the common acceptance contract.

```text
MC0012=RESOLVED
RESEARCH132=CROSS_MODEL_ICM_RECONCILIATION_COMPLETE
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CANDIDATE_ARCHITECTURE_SYNTHESIS
```

## 75. First candidate-family synthesis complete; MC-0013 independent counter-design opens

Research 133 begins serious architecture synthesis from the complete evidence field and frozen Requirements V0.2. It does not score technologies or select a winner. Instead it identifies common semantic responsibilities, derives constraints that survive multiple implementation families, and constructs six materially different coherent architecture families to expose where semantic cost can be paid.

```text
A  Distributed Document Contracts
   rich authoritative documents + local structured declarations + generated views

B  Bounded Semantic/Control Spine
   rich authoritative sources + small authoritative identity/control relation layer

C  Knowledge-Object-Primary Repository
   semantic/workstream/source objects primary; human documents mostly composed views

D  Transition Journal + Materialized Current Knowledge
   authority-significant transitions primary; current/workstream/authority projections derived

E  Relational Canonical Registry + Attached Artifacts
   normalized structured authority for selected state/relations; rich evidence attached

F  Retrieval-First Minimal Formalism
   rich documents + minimal deterministic control declarations + dynamic retrieval
```

The alternatives reveal a deeper continuum than `files versus database`: less explicit structure reduces capture/schema cost but increases repeated inference/reconstruction ambiguity; more explicit structure strengthens deterministic identity/authority/query behavior but increases relation, validation and migration cost.

Several cross-family deductions already narrow the design space without selecting a technology:

```text
pure prose is insufficient for every required authority/workstream/identity control semantic
probabilistic retrieval cannot own consequential governing authority
pure current snapshots cannot replace historical lineage
pure history/event replay cannot be the ordinary reconstruction interface
global hand-maintained registries cannot grow linearly with history
universal sentence/claim atomization is unjustified
source/write authority must remain distinguishable from derived read/reconstruction views
active salience should be derived from current workstream/authority/dependency state where practical
workstream continuation and consequential authority are the strongest cases for deterministic structure
```

Research 133 records one integrated ChatGPT hypothesis worth challenging rather than adopting: rich Git-authoritative source artifacts plus a bounded authoritative semantic/control spine plus rebuildable multi-axis/query views. The physical representation of such a spine remains intentionally open. The hypothesis may be wrong because it can inherit both document and structured-registry costs, expand into a disguised database, or duplicate semantic facts across source and spine.

High-information probes are identified for identity merge/split, joint-authority closure, nested workstream interruption, active-surface derivation, local-change economics, derived-store deletion and post-activation contract fidelity. These are intended to falsify assumptions before major implementation rather than instantiate six full systems.

Before ChatGPT's candidate content is exposed cross-model, MC-0013 opens an `INDEPENDENT_THEN_COMPARATIVE` Claude counter-design. Claude's substantive design base is exact pre-candidate commit:

```text
233eb932062a24473fcc4f4fe93160c952eea426
```

The current branch is routing-only for MC-0013 Phase 1. Claude may use the same complete pre-candidate evidence field, including Research 132 and ICM, but must not inspect Research 133 or descendant candidate synthesis until Message 001 is frozen. This tests architecture-design convergence/divergence rather than evidence reconstruction.

```text
RESEARCH133=FIRST_ARCHITECTURE_SYNTHESIS_COMPLETE
MC0013=OPEN_INDEPENDENT_COUNTER_DESIGN
CHATGPT_WORKING_HYPOTHESIS=BOUNDED_SEMANTIC_CONTROL_SPINE_HYBRID
WORKING_HYPOTHESIS_STATUS=CHALLENGE_NOT_SELECTION
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MC0013_MESSAGE_001
```

## 76. MC-0013 independent design valid; comparative architecture review opens

Claude MC-0013 Message 001 is durably frozen and valid as a candidate-design-independent architecture pass. It was written from exact substantive base `233eb932062a24473fcc4f4fe93160c952eea426` while Research 133 and Checkpoint 475 remained hidden. The independent design therefore supplies a useful second architecture path over the same frozen evidence field rather than a reaction to ChatGPT's candidate synthesis.

Claude independently converges with Research 133 on several major boundaries: deterministic/project-controlled representation is needed for selected identity, authority, relation and continuation semantics; rich prose remains important for rationale and nuanced knowledge; probabilistic retrieval is subordinate to governing-authority resolution; distributed document declarations and explicit object/graph structures are both serious candidates; and project-wide event sourcing is not justified merely by selective temporal requirements.

The main design divergence is now sharper than the original family lists. Claude prefers distributed source-local metadata/frontmatter compiled into generated routing/dispatch views, plus a narrow authority-transition ledger. ChatGPT's strongest hypothesis instead gives selected cross-artifact identity/control semantics their own bounded authoritative spine while rich sources retain rationale/exact content and global views remain derived.

ChatGPT Message 002 preserves the comparison and corrects requirement overstatements before the next Claude turn. In particular, the frozen V0.2 boundary does not force a pointer-only core, a single physical truth store, a literal workstream state machine, or a prose-only source-of-truth layer. KA-R48 also means ordinary canonical commits alone do not fully explain low-friction candidate capture.

A new comparative hypothesis is now explicit: semantic ownership might be partitioned so source-local facts remain local while cross-object/control-state facts receive their own authoritative home. This is not accepted architecture. The next comparative turn must attack whether that partition is coherent or simply creates two authoring systems.

Mechanism-probe sequencing also remains open. The current preference is to complete the cheap comparative dialogue first, then freeze a common hard-case fixture and represent it through the strongest surviving hypotheses rather than prototyping only one model's preferred family first.

```text
MC0013_MESSAGE001=VALID_INDEPENDENT_DESIGN
MC0013_PHASE=COMPARATIVE_ARCHITECTURE_REVIEW
MAIN_DISAGREEMENT=DISTRIBUTED_DECLARATIONS_VS_BOUNDED_CROSS_OBJECT_SPINE
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MC0013_MESSAGE_003
```

## 77. MC-0013 resolved; common-fixture mechanism probes become the next evidence gate

Claude MC-0013 Message 003 completes the comparative architecture dialogue. The independent-first process produced real movement rather than superficial agreement: Claude's original preference for pure distributed source-local declarations plus a narrow authority-transition ledger changed after examining Research 133's cross-object ownership argument. Claude now accepts that identity merge/split mappings, joint governing-source closure, workstream state spanning several artifacts and relations with their own lifecycle need a credible authoritative home that is not arbitrarily assigned to one endpoint document.

The live candidate set therefore narrows without selecting a target:

```text
H1  Distributed Document Contracts
H2  Partitioned Semantic Ownership / Bounded Cross-Object Spine

reference poles
H3  Object-Primary Structured Authority
H0  Retrieval-First Minimal Formalism
```

Project-wide Transition Journal and the narrower event-ledger variant are deferred because Git already supplies recording chronology and current evidence does not demonstrate enough value in replayable cross-fact history to justify the extra mechanism. Relational storage is folded into H2/H3 as a physical implementation option rather than retained as a separate semantic family.

Research 134 freezes the semantic-ownership partition and one representation-neutral Common Fixture V0.1. The fixture covers identity rename/merge/reversal/split, joint governing-source closure and conflict, nested workstream interruption/resume, low-friction capture/consolidation/promotion, 1x/5x/10x active-surface pressure, derived-store deletion/rebuild and BL-001-style post-activation contract fidelity. H1 and H2 must face identical facts and transitions. H3 is used only deeply enough to calibrate the upper-structure alternative.

No further Claude architecture discussion is required before probe evidence exists. The next gate is empirical: determine whether H2's cross-object spine remains genuinely bounded and locally maintainable under the hard cases, or whether H1 can satisfy those same cases with less machinery and without ambiguous/duplicated semantic ownership.

```text
MC0013=RESOLVED
RESEARCH134=COMMON_FIXTURE_PROTOCOL_FROZEN
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_COMMON_FIXTURE_AND_H1_H2_PROBES
```

## 78. Common Fixture V0.1 receives an exact machine freeze before H1/H2 implementation

Research 135 converts Research 134's conceptual fixture into one exact representation-neutral machine artifact **before** either candidate receives implementation logic. This prevents the hard cases or expected outputs from being quietly adapted after seeing how H1 or H2 behaves.

```text
fixture: docs/research/project_knowledge_architecture_probe_v01/COMMON_FIXTURE_V01.json
fixture_id: PKA-CF-V01
SHA-256: c8ed1873014b7a69016eb6fb259791d1c34b9cd14219547f1ebc0e755b836fe8
```

The fixture contains F1-F7 plus a synthetic private/non-leakage overlay. It does not assign semantic facts to source-local declarations or a cross-object spine. H1 and H2 must consume identical fixture bytes and face identical challenge mutations. Any later fixture defect requires a new version and a complete rerun.

```text
COMMON_FIXTURE_V01=MACHINE_FROZEN
H1_IMPLEMENTATION=NEXT
H2_IMPLEMENTATION=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 79. Common Fixture V0.1 probe challenges the assumed necessity of a separate spine

Research 136 records the first executable H1/H2 comparison against the exact fixture frozen before implementation in Research 135. Both candidates pass every V0.1 semantic/failure challenge. H2's seven top-level spine records remain exactly seven while historical/evidence items grow from 20 to 100 to 200, so passive history does not make the physical spine grow in this fixture. Both candidates keep the same active semantic view at 138 serialized bytes across 1x/5x/10x history.

The more important result is that H1 is materially stronger than the pre-probe prose argument assumed. H1 represents directional relations once on an asserting/source artifact, lets first-class workstream sources own their own control state, and derives joint governing/contract closure deterministically. It therefore covers the same normalized 32 semantic propositions without duplicate authoritative owners and without a separate cross-object store.

```text
normalized semantic ownership

H1
    30 source-local authoritative propositions
     0 spine-owned propositions
     2 derived-only closure propositions

H2
     5 source-local authoritative propositions
    27 spine-owned propositions
     0 derived-only closure propositions
```

This exposes a second boundedness dimension. H2 is physically small in V0.1, but its seven records own 27/32 of the normalized control/relationship propositions. Future qualification must therefore measure semantic responsibility share as well as file/row/record count. A physically small substrate that gradually owns most project semantics can still become a central registry in architectural terms.

H2 also incurs one explicit local-to-spine authority reclassification and 18 instrumented authored-location touches versus H1's 12 in the same synthetic transition/challenge sequence. These counts are directional evidence only, not universal maintenance ratios.

The valid first-probe conclusion is not H1 selection. V0.1's cross-object cases each still admit a plausible directional/subject-local owner: S-B owns its identity-transition history, P2 owns the supplement relation, workstream artifacts own their state, and joint closure can remain derived. The fixture therefore does not yet strongly test a relationship whose own lifecycle/status/provenance cannot be assigned to an endpoint without arbitrary ownership.

H3 does not need implementation yet because H1/H2 both satisfy V0.1 without converging on object-primary complexity. The next discriminator should be a separately frozen V0.2 relation-lifecycle fixture in which a relation has its own stable identity, independent proposed/disputed/accepted/superseded state, relation-specific evidence/temporal applicability, genuinely n-ary or symmetric semantics and stale-concurrency pressure while endpoints remain stable. H1 may not solve that by creating a dedicated authoritative relation artifact under another name; doing so would cross the H2 boundary. H2 should simultaneously be narrowed to a minimal admission-rule spine so the test measures whether semantic boundedness survives.

```text
COMMON_FIXTURE_V01=COMPLETE
H1=PASS
H2=PASS
H2_PHYSICAL_HISTORY_BOUNDEDNESS=SUPPORTED_IN_V01
H2_SEMANTIC_BOUNDEDNESS=NOT_ESTABLISHED
SEPARATE_SPINE_NECESSITY=NOT_ESTABLISHED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=RELATION_LIFECYCLE_DISCRIMINATOR_FIXTURE_V02
```

## 80. Relation-Lifecycle Discriminator V0.2 is machine-frozen before implementation

Research 137 freezes the exact second mechanism fixture at SHA-256 `ece094762e3fe4f064640004da3f2293aa39168268af183df6f1347ba7f4b4c0` before either H1 or H2 receives V0.2 implementation logic. It responds directly to the construct-validity limitation exposed by V0.1.

The new fixture keeps endpoint semantic state fixed while a symmetric ternary relation `R-ABC-1` develops its own stable identity, proposed/disputed/accepted/verified/superseded lifecycle, relation-specific provenance, recorded/authority/effective times and optimistic-concurrency revision. A later `R-ABC-2` becomes effective independently of any endpoint change. A stale relation update must fail without mutation and missing required relation evidence must fail visibly.

H1 remains prohibited from creating a separately authoritative relation object/store. It may choose one endpoint as the deterministic owner of the relation declaration, but must disclose whether that choice is semantically natural or arbitrary and expose the resulting touch coupling. H2 is narrowed to a minimal admission rule: only a relation with stable identity, independent lifecycle, relation-specific provenance and no natural endpoint owner may enter the first-class relation spine. An ordinary directional `S-D depends_on S-A` control relation must remain source-local.

The fixture also scales ordinary non-qualifying relations from 10 to 50 to 100. H2's first-class relation spine should remain two records if its admission boundary is genuinely selective.

```text
RELATION_LIFECYCLE_FIXTURE_V02=MACHINE_FROZEN
H1_V02=IMPLEMENTATION_NEXT
H2_V02=IMPLEMENTATION_NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 81. V0.2 supports selective first-class relation ownership without selecting a target

Research 138 records the completed Relation-Lifecycle Discriminator V0.2. Both H1 and narrowed H2 pass every frozen semantic, temporal, provenance, stale-update, missing-evidence and derived-rebuild oracle. The final implementation deliberately strengthens H1 to the source-owned sidecar form that Research 137 permits, so relation-only changes do not modify endpoint intrinsic documents.

The remaining discriminator is semantic ownership rather than raw correctness. H1 places both symmetric ternary relations in `sidecar:S-A:relations` because `S-A` wins an explicit lexicographic tie-break; the fixture provides no semantic reason to prefer A over B or C. H2 lets each qualifying relation own its independent identity/lifecycle directly.

The trade-off is not one-sided. H1 uses one source-owned authoritative relation location and four authoritative location touches across successful lifecycle transitions. H2 uses two first-class relation locations and five location touches because the supersession transition updates both predecessor and successor. H2 therefore improves ownership naturalness but does not establish lower physical write cost.

The narrowed H2 admission rule does pass its first selectivity test: only `R-ABC-1/2` enter the relation substrate, the ordinary `S-D depends_on S-A` relation stays source-local, and materializing 10/50/100 additional ordinary relations leaves first-class relation records at 2/2/2 with zero false-positive admissions.

V0.1 and V0.2 jointly support a more selective working hypothesis: source-local authority by default; separately authoritative semantic/control objects only when the thing itself earns independent identity/lifecycle/provenance and lacks a natural source owner; broad routing/search/closure/context remain rebuildable views. This is not yet a selected target and does not choose the physical substrate.

Research 134 explicitly deferred another Claude contribution until empirical probe evidence existed. That condition is now satisfied. The next step is a bounded adversarial cross-model interpretation of the frozen V0.1/V0.2 fixtures, raw results and ChatGPT interpretations before target narrowing.

```text
V01_PROBE=COMPLETE
V02_PROBE=COMPLETE
SELECTIVE_FIRST_CLASS_RELATION_MECHANISM=SUPPORTED
BROAD_SPINE=NOT_SELECTED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=ADVERSARIAL_CROSS_MODEL_INTERPRETATION
```

## 82. MC-0014 opens a post-probe adversarial interpretation gate

MC-0014 is opened in `ADVERSARIAL_REVIEW` mode against exact result commit `85ade407b2f1957f5a3980aca92c09500db430b8`. This executes Research 134's earlier plan to defer another Claude contribution until empirical probe evidence existed.

The thread is intentionally not blind. Claude already participated in the architecture-design sequence and is now given both raw V0.1/V0.2 fixtures/results/implementations and ChatGPT's Research 136/138 interpretations. Its role is to attack evidence quality and interpretation, not generate another independent architecture from scratch.

The review must directly test whether the strong-H1 source-owned sidecar remains honestly H1, whether V0.2's admission rule is circular, whether first-class relation identity actually implies a centralized `spine`, whether the maintenance metrics are fair, whether the synthetic selectivity result transfers at all to ambiguous real ADS relationships, whether H3 or another family should reopen, and what minimum real-repository/behavioral evidence is still needed before target narrowing.

Only Claude Message 001 is currently authorized. No target architecture is selected while this gate is open.

```text
MC0014=OPEN
MODE=ADVERSARIAL_REVIEW
EXACT_TARGET=85ade407b2f1957f5a3980aca92c09500db430b8
NEXT=CLAUDE_MESSAGE_001
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 83. MC-0014 resolves with a narrower mechanism concept and a real-corpus discriminator

Claude's MC-0014 Message 001 performed the intended code-level adversarial interpretation of V0.1/V0.2. ChatGPT accepts the material corrections and closes the thread without another round.

The strongest clean result remains V0.1: directional relations and several workstream/identity facts can remain source-local with deterministic derived closure and zero duplicate authoritative owners. V0.2 remains useful for relation lifecycle, temporal semantics, stale-update rejection, evidence failure and derived-view rebuildability, but two earlier claims are downgraded.

First, the final strong-H1 sidecar already contains a lifecycle-bearing first-class relation object structurally near-identical to H2's relation object. V0.2 therefore mainly compares address/ownership namespace, not reification versus non-reification. Second, H2's admission/selectivity test reads hand-authored fixture flags that encode the answer; its 0/0 false-positive/false-negative result validates rule execution, not real ADS classification reliability.

The leading semantic vocabulary is therefore corrected from `bounded spine` to **selective semantic reification** / **selectively first-class semantic/control objects**. First-class identity does not itself imply central physical storage. H3 remains a reference pole: relation-object machinery convergence partially approaches one reopening condition, but object-primary simplification of the broader hard-case set is still unobserved.

Research 139 freezes the next protocol. The project will use a small real ADS relationship corpus with no architecture labels, obtain mutually hidden independent ChatGPT and Claude judgments, and only afterward evaluate any mechanized observable-feature admission rule. Authoring-time ownership/classification cost and reviewer disagreement become empirical evidence rather than fixture assumptions.

```text
MC0014=RESOLVED
V02_ADMISSION_SELECTIVITY_REAL_WORLD=UNTESTED
BOUNDED_SPINE_LEADING_LABEL=RETIRED
SELECTIVE_SEMANTIC_REIFICATION=WORKING_CONCEPT
REAL_CORPUS_DISCRIMINATOR=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 84. Real ADS Relationship Corpus V0.1 is frozen before reviewer judgments

Research 140 freezes a 15-case real-repository relationship corpus at SHA-256 `cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5` before either ChatGPT or Claude produces an ownership/reification label. The cases are drawn from actual ADS project-development authority, workstream, governance, provenance, navigation, collaboration and transition surfaces at exact source commit `47656a2a6ed98061d987786814a6be39d38b3999`.

Each case carries exact source path/hash/line-range/excerpt evidence but no expected label, `natural_owner`, `independent_lifecycle`, `should_reify`, H1/H2/H3 designation, mechanized admission output or reviewer judgment. This directly removes the answer-bearing fixture flags that made the V0.2 admission test self-confirming.

The first reviewer sequence is staged. ChatGPT will freeze its complete 15-case judgment first. Claude will later be routed to the exact corpus-freeze commit rather than the descendant containing ChatGPT labels. Only after both judgment sets are frozen will the project compare agreement/disagreement and decide whether an observable-feature admission rule is worth mechanizing.

```text
REAL_CORPUS_V01=FROZEN_UNLABELED
CHATGPT_JUDGMENT=NEXT
CLAUDE_LABEL_EXPOSURE=PROHIBITED_UNTIL_OWN_SET_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 85. ChatGPT real-corpus judgment freezes before Claude exposure

Research 141 freezes ChatGPT's complete 15-case judgment set over Corpus V0.1 before any Claude case labels exist. The judgment artifact has SHA-256 `73848d51f659fab83c2cd461cad7b8a0973ade569db6d958ad2b024a7d3cd7dd` and is bound to corpus freeze commit `ae87c1facbf7c7d7508414e86a935bc439404c24`.

ChatGPT assigns 10 cases SOURCE_LOCAL, 2 FIRST_CLASS_SEMANTIC_OBJECT, 2 DERIVED_ONLY and 1 UNRESOLVED, with 12 HIGH and 3 MEDIUM confidence judgments. The two first-class cases are both real workstream-continuation/control cases; the two derived-only cases concern CI-run obsolescence and Knowledge Map routing membership. `current_routing.json` is intentionally left unresolved from the packet because its field-level authority-class boundary is not established by the evidence packet itself.

These are reviewer labels, not ground truth. No mechanized rule is allowed yet and no comparison may occur until Claude independently freezes all 15 labels. Claude's substantive reads must be bound to the exact corpus-freeze commit, with Research 141 and the ChatGPT judgment artifact withheld.

```text
CHATGPT_REAL_CORPUS_JUDGMENT=FROZEN
CLAUDE_INDEPENDENT_JUDGMENT=NEXT
CROSS_REVIEWER_COMPARISON=NOT_YET_ALLOWED
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 86. MC-0015 opens the mutually hidden second real-corpus judgment

MC-0015 now executes the second-reviewer half of Research 139's real-corpus protocol. Claude's substantive evidence boundary is the exact unlabeled corpus-freeze commit `ae87c1facbf7c7d7508414e86a935bc439404c24`. Current descendant routing exists only to locate the obligation.

The ChatGPT judgment set is already durably frozen on a descendant commit, but Claude is explicitly prohibited from reading it, Research 141, Checkpoint 485+ bodies, descendant current-state synthesis or any other surface that exposes case labels/confidence/rationales until its own complete set is frozen. This is reviewer-label independence rather than architecture-problem blindness.

Claude must classify all 15 cases using exactly SOURCE_LOCAL, FIRST_CLASS_SEMANTIC_OBJECT, DERIVED_ONLY or UNRESOLVED and provide the required rationale/owner/continuity/derived-input/missing-evidence fields. Packet evidence controls; any necessary deeper source read must use the corpus's exact source snapshot and be declared.

No cross-reviewer comparison and no mechanized admission rule is authorized yet.

```text
MC0015=OPEN
CLAUDE_INDEPENDENT_JUDGMENT=ACTIVE
CHATGPT_LABEL_EXPOSURE=PROHIBITED
CROSS_REVIEWER_COMPARISON=BLOCKED
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 87. Two independent real-corpus judgments expose a taxonomy construct question

Claude's MC-0015 Message 001 is accepted as reviewer-label independent. The two frozen judgment sets agree on 12 of 15 cases. They independently converge on source-local ownership for scoped supersession, governance, reopen triggers, thread/review control state, provenance, public/private authority policy and the sampled architecture-transition policy; they also converge on derived-only treatment for same-branch CI obsolescence and Knowledge Map topic membership.

The three disagreements are more useful than a simple score. RC-005 is FIRST_CLASS for ChatGPT and SOURCE_LOCAL for Claude, but both rationales may be simultaneously true if a first-class workstream object is represented by one natural source artifact. RC-006 is FIRST_CLASS for ChatGPT and DERIVED_ONLY for Claude; Claude's decomposition suggests durable per-workstream identity/state can coexist with a derived aggregate active/paused/next route view. RC-012 is UNRESOLVED for ChatGPT and SOURCE_LOCAL for Claude, but Claude's rationale uses authority claims not present in the packet despite declaring no additional source reads, so this case needs a protocol audit rather than a winner.

Research 142 therefore blocks mechanized admission-rule work and opens one bounded comparative Claude turn. The core construct question is whether the four-class taxonomy incorrectly treats semantic first-classness, authority ownership/home and derived-view status as one mutually exclusive dimension. Requirements V0.2 remain unchanged and no architecture is selected.

```text
REAL_CORPUS_EXACT_AGREEMENT=12_OF_15
TAXONOMY_CONSTRUCT_VALIDITY=OPEN
MECHANIZED_RULE=BLOCKED
MC0015_COMPARATIVE_TURN=ACTIVE
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 88. MC-0015 resolves the real-corpus construct and returns Research 124 to architecture synthesis

Claude Message 003 confirms that the first real-corpus disagreement was largely a construct problem, not evidence that one model had simply chosen the wrong architecture. Semantic first-classness and authoritative home are separate questions; RC-005 is a durable workstream with one natural source. RC-006 combines durable workstream units with a derived aggregate route view and therefore requires decomposition. Claude also explicitly corrects its RC-012 packet-grounding violation, leaving that frozen packet unresolved.

Research 143 replaces the old mutually exclusive `SOURCE_LOCAL / FIRST_CLASS / DERIVED / UNRESOLVED` taxonomy for future reasoning with a required singular semantic unit plus two axes: semantic continuity/identity (`DURABLE_IDENTITY / NO_SEPARATE_IDENTITY / UNRESOLVED`) and authority mode/home (`SINGLE_SOURCE / JOINT_AUTHORITY / DERIVED_ONLY / UNRESOLVED`).

The first real corpus supports single-source authority as the dominant sampled pattern, derived views for computable/navigation state, and durable identity with single-source authority for project-development workstreams. It does not demonstrate a real `DURABLE_IDENTITY + JOINT_AUTHORITY` case. Therefore broad central relation/spine machinery is not justified as the default.

The next stage is no longer another admission-classifier experiment. Research 124 is ready to synthesize a serious whole-architecture candidate from the full evidence field and qualify it systematically against all frozen requirements and invariants.

```text
MC0015=RESOLVED
CORRECTED_SEMANTIC_AXES=FROZEN_FOR_RESEARCH
MECHANIZED_ADMISSION_CLASSIFIER=DEFERRED
WHOLE_ARCHITECTURE_CANDIDATE_SYNTHESIS=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 89. Whole-architecture Candidate 01 clears the design-coverage gate

Research 144 synthesizes the first post-MC-0015 whole-architecture candidate from the complete evidence field. `PKA-CANDIDATE-01` keeps rich repository-native semantic sources primary, assigns durable semantic identity selectively, defaults authoritative facts to one canonical semantic source, represents joint authority only as a bounded exception, derives global current/navigation/closure views, and adds task-shaped authority resolution plus action-contract activation for consequential work.

The candidate explicitly does not revive the old H1/H2 split. It uses Research 143's singular semantic-unit rule and separates semantic continuity/identity from authority mode/home. A first-class workstream can therefore remain single-source, while an aggregate route can remain derived-only.

Research 145 maps the candidate against every frozen acceptance statement. All 50 KA-R requirements and all 17 KA-I invariants have explicit candidate mechanisms; no design-coverage hole currently forces a different architecture family. That result is only a **design coverage pass**, not target qualification. The machine-readable matrix intentionally records zero final qualified passes because Candidate 01 has not yet been implemented and exercised as one integrated system.

Ten selection-blocking qualification clusters remain: reconstruction/discovery; authority/action-contract fidelity; identity/relation/temporal semantics; workstream/concurrency; capture/promotion/consolidation; derived-view rebuild/freshness; public/private degraded behavior; scale/maintenance economics; migration/authority switch; and qualification methodology itself.

The next high-value boundary is adversarial review of the concrete candidate followed by the smallest shadow prototype capable of exercising those clusters. Current project-development authority remains unchanged.

```text
PKA_CANDIDATE_01=WHOLE_ARCHITECTURE_SYNTHESIZED
KA_R_DESIGN_MAPPED=50_OF_50
KA_I_DESIGN_MAPPED=17_OF_17
DESIGN_COVERAGE_GATE=PASS
INTEGRATED_EVIDENCE_GATE=PENDING
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=ADVERSARIAL_CANDIDATE_REVIEW_THEN_SHADOW_PROTOTYPE
```

## 90. MC-0016 opens adversarial review before Candidate 01 implementation

MC-0016 is opened in `ADVERSARIAL_REVIEW` mode against exact Candidate 01 design commit `69aed186a0d63b3c395a133cd920099d5fa8e000`. The design-coverage mapping is treated as a claim to falsify rather than an accepted proof.

The review explicitly attacks interactions that a requirement-by-requirement matrix can hide: prose versus structured declaration drift, selective identity/tombstone maintenance, source-local authority versus joint-authority exceptions, generated current-state feasibility, workstream identity/home, action-contract fidelity, capture/consolidation burden, public/private degraded behavior, migration/rollback and 5x/10x economics. It must also independently identify any frozen requirement or invariant that is not actually design-covered and state whether Candidate 01 has accumulated enough object/relation machinery to reopen H3 or another family.

No implementation or authority migration is authorized while this review is pending.

```text
MC0016=OPEN
EXACT_REVIEW_TARGET=69aed186a0d63b3c395a133cd920099d5fa8e000
CANDIDATE=PKA-CANDIDATE-01
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MESSAGE_001
```

## 91. MC-0016 Message 001 materially amends Candidate 01

Claude's exact-target adversarial review is accepted as substantive evidence. It identifies a repeated architecture risk: stating an admission, precedence or fidelity intention in prose is not enough if the architecture lacks an observable rule that governs disagreement or transition. Research 146 reconciles the review and Candidate 01 is amended at `64d04fcc6ba2bcf6b66d4abbcccea714ca11870b`.

The most important new rules are one normative home for exact action-contract facts, a deterministic-plan-first assurance ladder, a default-deny J1-J6 joint-authority promotion test, must-preserve manifests for consequential consolidation, deterministic current-state core plus subordinate narrative, dependency-local ordinary refresh, bounded current identity lookup, paused-workstream salience, capture-backlog pressure and exporter-based rollback without dual authority.

The review's requirement-level downgrades are preserved as exact-target reviewer evidence but calibrated against frozen requirement scope. The task-owner working mapping returns to 50 KA-R / 17 KA-I design-covered after amendment, while final qualified passes remain zero.

Claude requested one short follow-up if concrete answers were supplied for the two most architecture-sensitive defects. MC-0016 therefore remains open only for Message 003 reviewing (B) normative action-contract precedence and (D) J1-J6 joint-authority admission.

```text
MC0016_MESSAGE001=RECONCILED
CANDIDATE_01_AMENDED_TARGET=64d04fcc6ba2bcf6b66d4abbcccea714ca11870b
TASK_OWNER_DESIGN_MAPPING=50_KA_R__17_KA_I
FINAL_QUALIFIED_PASSES=0
MC0016_MESSAGE003=NARROW_REVIEW_NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 92. MC-0016 closes and falsification-first shadow implementation begins

Claude Message 003 validates the sole-normative action-contract rule and supplies one final precision correction to `JOINT_AUTHORITY`: ordinary source-owned relations remain preferred whenever a natural semantic direction exists; a first-class joint-authority semantic source is eligible only when correct governing semantics would otherwise require an arbitrary, non-semantically-motivated directional tie-break among otherwise symmetric participants and an independently relevant set-level authoritative fact exists.

The message also identifies a separate source-integrity risk: a human may edit explanatory procedure prose without updating the structured contract. Candidate 01 now requires an impact-aware semantic-drift check on governed-procedure edits. This validator flags suspected divergence for review but never makes prose a competing normative source.

Claude explicitly states that neither issue blocks the falsification-first shadow prototype, H3 should not reopen before prototype evidence, and no further Claude round is needed. MC-0016 is therefore resolved.

Research 147 freezes the first executable slice. It is intentionally smaller than the full qualification program and must test the highest-risk foundations first: one normative contract home plus drift detection, natural directional authority versus irreducible symmetric joint authority, BL-001-style contract omission, dependency-local incremental generation versus clean full rebuild, and bounded current identity lookup over growing transition history.

```text
MC0016=RESOLVED
CANDIDATE_01=PROTOTYPE_READY_AT_DESIGN_LEVEL
DESIGN_MAPPING=50_KA_R__17_KA_I_AFTER_AMENDMENT
FINAL_QUALIFIED_PASSES=0
H3_REOPEN=NO
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=FALSIFICATION_FIRST_SHADOW_PROTOTYPE
```

## 93. Candidate 01 shadow fixture freezes before implementation

Research 148 freezes `PKA-C01-SHADOW-V01` plus a separate test-only oracle before implementation. This preserves the anti-treatment-bias discipline used by the earlier architecture probes while also correcting MC-0014's self-confirming-label problem: the semantic fixture contains no expected joint-authority label and the implementation is prohibited from reading the oracle.

The fixture directly exercises the five prototype-entry questions from Research 147: one normative action-contract home plus semantic drift review, natural directional ownership versus irreducible symmetric set-level authority, BL-001-style output fidelity, dependency-local refresh versus clean rebuild, and bounded current identity lookup while transition history grows 1x/5x/10x.

```text
SHADOW_FIXTURE_V01=FROZEN
FIXTURE_SHA256=77ffecc278995ef03130d962f863d46ccebac41d446de7099cc666750e8b66f7
ORACLE_SHA256=3ced74eb18f4d792c9a43eaf2b3d6956c497bc7b85c71bfc6b5e226f840fc38b
IMPLEMENTATION=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 94. Candidate 01 survives the first falsification-first shadow slice

Research 149 implements the exact fixture frozen at public commit `8ccefd17e229ee5a484c4481ed005290efc0282e`. The implementation reads the fixture hash but not the test oracle. The preserved first run and final raw result are byte-identical at SHA-256 `b4498e20d2f4984d938e6e6e32e9a34d7e4706ad17daf010d0ab6f7eb162ebd1` and all ten focused oracle tests pass without a repair cycle.

The five prototype-entry mechanisms all survive: procedure drift is surfaced without giving prose competing normative authority; natural SUPPLEMENT/SPECIALIZE relations remain source-owned while the symmetric X1/X2/X3 case alone earns a joint-authority object; BL-001-style omission/reordering fails visibly; one P2 change refreshes only two dependent views while full rebuild cost grows linearly with passive history; and identity current-target lookup remains one index operation at 1x/5x/10x while rebuild scans 24/104/204 identity events.

None of Research 147's stop/reopen conditions fires and H3 remains deferred. This is still synthetic/narrow evidence, so final qualified passes remain zero. The next architecture-research step is a broader shadow slice exercising ordinary operational behavior before migration: workstream DAG/pause/resume, capture/consolidate/promote fidelity, generated current-state/routing/navigation, public/private degraded mode and consequence-sensitive missing/conflicting authority.

```text
SHADOW_V01=PASS_ON_FIRST_RUN
FOUNDATIONAL_STOP_CONDITIONS=NONE
H3_REOPEN=NO
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=BROADER_SHADOW_OPERATIONAL_BEHAVIOR_SLICE
```

## 95. Operational Shadow V0.2 freezes before implementation

Research 150 freezes the broader Candidate 01 operational fixture/oracle after V0.1 survived its foundational stop gate. The new fixture adds the still-untested operational behaviors most likely to determine whether the candidate can replace the current continuity architecture safely: explicit workstream continuation and interruption recovery, capture/promotion fidelity, generated current views, public/private degraded mode and authority uncertainty.

```text
OPERATIONAL_SHADOW_V02=FROZEN
FIXTURE_SHA256=6daefddd448ead145281d56da8325925cb82c71fc57418283ef21c65418ec486
ORACLE_SHA256=a1af441f356fbd0e7cac65ba1f6c45589f96941139e669d99de4276acf8440b6
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_OPERATIONAL_SHADOW_V02
```

## 96. Operational Shadow V0.2 passes after preserving first-run defects

Research 151 implements the operational fixture frozen at `7231fcb0d6423787f58ed561a9064841e5f9a724`. The first run passed 35/38 checks and preserved three failures before repair: two deterministic ordering-contract mismatches and one substantive reversal of base/supplement authority order. The implementation was repaired without modifying the frozen fixture/oracle, and the final result `6a7e2f1b9846cb2e7c3e349c75a512c30540ccdab0ae485a3154d398236a7de6` passes all focused V0.2 tests.

The broader slice now demonstrates synthetic workstream DAG/pause/resume/interruption behavior, stale-write rejection, fidelity-gated promotion, generated current views, public/private non-leakage/degraded mode and fail-visible missing/conflicting authority. All unit tests pass.

After two synthetic slices, the next evidence should use a bounded real repository shadow. Another synthetic expansion would increasingly test our fixtures rather than the architecture.

```text
OPERATIONAL_SHADOW_V02=PASS_AFTER_PRESERVED_REPAIR
FIRST_RUN=35_OF_38
FINAL_ORACLE=PASS
H3_REOPEN=NO
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REAL_REPOSITORY_SHADOW_PARITY_AND_BEHAVIOR
```

## 97. Real-repository Shadow V0.1 freezes migration-seed burden before implementation

Research 152 moves Candidate 01 beyond synthetic evidence. The experiment is bound to exact repository commit `e10fd108330f2cf8d260a621ea59053aebd28291` and forbids generation from reading the three global surfaces it later compares against.

The freeze makes two migration burdens explicit rather than hiding them: one active workstream semantic unit needs a successor-style canonical workstream seed, and three live project-control facts are still uniquely owned by the existing global live-state architecture. Those facts are admitted as `MIGRATION_FROM_EXISTING_GLOBAL_AUTHORITY`, not credited as already source-local.

The same fixture also tests a real governing procedure by mapping the ordered new-session reconstruction contract in `CONTINUITY.md` to stable B01..B10 constraint IDs.

```text
REAL_SHADOW_V01=FROZEN
MIGRATION_SEED_WORKSTREAMS=1
MIGRATION_SEED_PROJECT_CONTROL_FACTS=3
GENERATION_COMPARISON_TARGET_READS=FORBIDDEN
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_REAL_SHADOW_V01
```

## 98. Real-repository Shadow V0.1 passes and exposes concrete control ownership

Research 153 executes the exact real-repository fixture frozen at Checkpoint 497. The first run passes 24/24 checks without repair and the final result remains byte-identical at `54e666aa5d42bb83b97e0ff2a8124bd6024dfd22ab71f2740bb87638ee0f50a3`. Generation reads zero comparison targets; `current_routing.json`, `CURRENT_STATE.md` and `KNOWLEDGE_MAP.md` are opened only after the shadow projection exists.

The most important outcome is not parity itself but its decomposition. One current workstream semantic unit needs successor-native representation, while active PR and promoted integration branch/SHA were still migration-seeded from today's global live-state authority. Candidate 01 is amended so the primary active workstream owns its branch/PR/boundary execution anchor, while one narrow Project Integration Boundary source owns promoted branch + exact promoted commit. A broad `PROJECT_CONTROL` registry is rejected for now.

The next experiment must eliminate those migration seeds entirely and reproduce routing from successor-native shadow sources only.

```text
REAL_SHADOW_V01=PASS_ON_FIRST_RUN
FIRST_RUN_CHECKS=24_OF_24
ROUTING_EXACT_PARITY=PASS_WITH_SEEDS
CONTROL_OWNERSHIP=AMENDED
ZERO_SEED_ROUTING_SHADOW=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 99. Zero-seed successor-native routing fixture freezes before implementation

Research 154 operationalizes the control-ownership amendment from Research 153. Two successor-native shadow canonical sources now own the active workstream execution anchor and promoted integration boundary. The generator is allowed zero current global live-state facts and zero reads of the current routing/state/navigation targets before comparison.

This experiment therefore tests whether the candidate can cross the important line from **parity with migration seeds** to **parity from successor-native semantic owners**.

```text
ZERO_SEED_ROUTING_FIXTURE=FROZEN
SUCCESSOR_SHADOW_SOURCES=2
GLOBAL_LIVE_STATE_GENERATION_FACTS=0
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_ZERO_SEED_ROUTING_V01
```

## 100. Zero-seed routing passes and current-state decomposition becomes the next bottleneck

Research 155 executes the fixture frozen at Checkpoint 499. The first run passes 8/8 checks without repair and remains byte-identical to the final result at `cf0d4f9505ad8fdab0c54bf293e9022448239318516f9f2f88dcdab12a7dd5eb`. Two successor-native shadow sources plus real Specification 027 and Checkpoint 192 reproduce the exact frozen routing target with zero global live-state generation facts and zero forbidden target reads.

This is the first direct evidence that one current global control surface can become a deterministic compatibility view after facts are relocated to natural semantic owners. The next major uncertainty is not routing but `CURRENT_STATE.md`, whose current role mixes live facts, orientation, rationale and history.

```text
ZERO_SEED_ROUTING=PASS
ROUTING_SHADOW_SUBSYSTEM=SUPPORTED
CURRENT_STATE_DECOMPOSITION=NEXT
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 101. Real CURRENT_STATE decomposition exposes active-surface drift and one canonical migration gap

Research 156 performs complete block-level coverage of the real 1,159-line / 282,796-byte Checkpoint 500 `CURRENT_STATE.md`. The audit classifies 98.28% of bytes into historical/latent, source-owned-elsewhere, stale historical/rotation, or derived-navigation roles, while only 1.72% remains in coarse A/B/C categories. This is not deletion authorization; every D block still requires must-preserve/source-trace parity before migration.

The audit reproduces four concrete drift defects in the current operational surface: stale Checkpoint 353 current-boundary language, stale MC-0010 OPEN status, stale chatgpt-19 / Research-122 rotation language, and a fixed minimum-reading packet that omits Research 124 / Research 155 / Checkpoint 500. Those false current-language claims are corrected immediately without changing authority roles.

The principal A-category gap is the paused Source Vault bootstrap state. Its evidence is distributed across runbook/checkpoints/research, but no single Candidate-01-style source currently owns the complete resumable workstream state. The next shadow must create that workstream source and then generate a compact current-state core under a must-preserve contract.

```text
CURRENT_STATE_DECOMPOSITION=COMPLETE_AT_BLOCK_LEVEL
REAL_DRIFT_FINDINGS=4_REPAIRED_IN_CURRENT_SURFACE
SOURCE_VAULT_WORKSTREAM_CANONICAL_MIGRATION=NEXT
CURRENT_STATE_AUTHORITY_SWITCH=NOT_AUTHORIZED
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 102. Source Vault workstream and compact current-state-core fixture freeze

Research 157 closes the main A-category ownership gap from Research 156 in shadow form. One durable Source Vault bootstrap workstream now owns the paused/resumable semantic state while the permanent bootstrap runbook remains the governing procedure and validation/checkpoint records remain evidence.

A 23-item must-preserve contract separates core orientation from detailed source-owned drill-down. Generation may not read current routing/state targets. The experiment therefore tests whether Candidate 01 can preserve current truth without recreating another large global copy.

```text
CURRENT_STATE_CORE_FIXTURE=FROZEN
MUST_PRESERVE_ITEMS=23
CORE_REQUIRED=15
SOURCE_VAULT_WORKSTREAM_SHADOW=FROZEN
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_CURRENT_STATE_CORE_V01
```

## 103. Compact current-state core passes; return to whole-architecture qualification

Research 158 executes the exact fixture frozen at Checkpoint 502. The first run passes 12/12 checks without repair and remains byte-identical to the final result at `56c26acb345e164feeddf7a92101f3e332f62d34ece2eaf25a3a4bd6ba81cc64`. All 23 must-preserve semantics remain recoverable, the Source Vault successor workstream aligns with real evidence, the compact core is 871 bytes, and generation consumes zero facts from current routing/state targets.

This is enough evidence to stop treating current global files as the immediate research sequence. The next stage returns to Candidate 01's ten qualification clusters and asks which architecture-level uncertainties still block selection. Only those blockers should trigger further experiments.

```text
CURRENT_STATE_CORE=PASS_ON_FIRST_RUN
MUST_PRESERVE=23_OF_23
LEGACY_FILE_BY_FILE_SEQUENCE=NOT_THE_NEXT_METHOD
WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION=NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 104. Whole-architecture evidence reconciliation selects Q3 by uncertainty, not file order

Research 159 audits Candidate 01 evidence across all ten qualification clusters. The current record contains 50/67 items with synthetic-or-better support and 32/67 with some real-repository evidence, but still zero final qualified passes.

The evidence audit explicitly rejects sequential conversion of `CONTINUITY.md`, `KNOWLEDGE_MAP.md` or other legacy artifacts as the next research method. Those artifacts may be used as evidence only when an architecture-level uncertainty requires them.

Q3 identity/relationship/temporal semantics is selected next because it has zero real Candidate 01 implementation evidence and directly tests whether selective repository-native source profiles remain simpler than an object-primary architecture.

```text
WHOLE_ARCH_EVIDENCE_RECONCILIATION=COMPLETE
Q6_Q8=STRONGEST_REAL_SUBSYSTEM_EVIDENCE
Q3=NEXT_ARCHITECTURE_FALSIFICATION_TARGET
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 105. Q3 real identity/temporal fixture freezes before implementation

Research 160 freezes five real ADS Q3 cases and five profile-specific Candidate 01 shadow sources before implementation. The cases cover scoped supersession with retained outcome, multi-successor partial supersession, real Git carrier/identity repair, durable paused workstream identity and epistemic-role transition.

The H3/Object-Primary reopening rule is prospective: central-registry need, relation/transition-source proliferation, authoritative duplication, universal objectization or unresolved real queries reopen comparative architecture work.

```text
Q3_REAL_FIXTURE=FROZEN
REAL_CASES=5
H3_REOPEN_RULE=ACTIVE
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q3_REAL_V01
```

## 106. Q3 real result passes without H3 reopening

Research 161 executes the five real Q3 cases frozen at Checkpoint 505. The preserved first run exposed one probe defect: it incorrectly required a Git rename commit to be duplicated in the historical Markdown source. The single repair moved that proof back to its natural owner, Git history, without changing the fixture or oracle. Final comparison passes 4/4 aggregate checks and all five real cases resolve.

No H3/Object-Primary reopening trigger fires. Candidate 01 therefore gains real subsystem support for selective identity, source-owned scoped supersession, selective temporal semantics and epistemic-role transition. Q3 is not finally qualified because merge/split/tombstone remain without equivalent real cases.

The next high-value uncertainty is Q7 public/private boundary and degraded mode, currently synthetic-only.

```text
Q3_REAL_SUBSYSTEM_SUPPORT=PASS
H3_REOPEN=NO
Q3_FINAL_QUALIFICATION=PENDING
NEXT=Q7_REAL_PUBLIC_PRIVATE_BOUNDARY
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 107. Q7 real public/private fixture freezes before implementation

Research 162 freezes five cross-repository public/private scenarios using exact public authority sources and hash-bound real private companion evidence. The fixture contains no exact private path or value. Runtime-supplied private surfaces may be read only to test independent freshness, bounded dependency and redacted public projection.

The frozen real private anchor is intentionally stale relative to the current public target, creating a real FAIL case that must remain orthogonal to public repository integrity and must not downgrade `RESOLVED_PRIVATE` facts to unresolved.

```text
Q7_REAL_FIXTURE=FROZEN
PRIVATE_VALUE_PUBLICATION=ZERO
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q7_REAL_V01
```

## 108. Q7 real public/private result passes; Q9 migration/rollback is next

Research 163 executes the frozen cross-repository Q7 fixture on the first run with 7/7 oracle checks and no implementation repair. A privacy-preserving receipt is derived inside the private authority boundary; the public result contains zero exact private-value leaks and zero private-path serialization. The real private companion anchor is stale against the frozen public target and correctly produces `PRIVATE_CONTINUITY_INTEGRITY=FAIL` without changing public repository integrity or downgrading `RESOLVED_PRIVATE` facts.

All six Q7 items now have real subsystem evidence, but final qualification remains zero because the successor is still shadow-only. The next architecture-level blocker is Q9 staged migration, semantic preservation, rollback and explicit authority-switch preparation.

```text
Q7_REAL_SUBSYSTEM_SUPPORT=PASS
PRIVATE_VALUE_LEAKS=0
Q7_FINAL_QUALIFICATION=PENDING
NEXT=Q9_MIGRATION_ROLLBACK_SHADOW
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 109. Q9 migration/rollback fixture freezes before implementation

Research 164 freezes Candidate 01's first explicit migration/rollback experiment against the exact Checkpoint 508 public authority boundary. Ten migration-critical semantic units are mapped from legacy owners to three shadow successor semantic sources. The experiment must preserve semantic identity/provenance, keep compatibility paths resolvable, generate temporary legacy-compatible rollback surfaces accepted by the existing routing validator, keep the authority switch blocked, and reconstruct the migration's own workstream state from Candidate 01 semantics.

The experiment is intentionally shadow-only. No current authority file may be overwritten and no switch may occur.

```text
Q9_MIGRATION_FIXTURE=FROZEN
CURRENT_ARCHITECTURE=STILL_AUTHORITY
AUTHORITY_SWITCH=FORBIDDEN_IN_EXPERIMENT
NEXT=IMPLEMENT_Q9_MIGRATION_V01
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 110. Q9 shadow migration/rollback passes; evidence field must be reconciled again

Research 165 executes the frozen Q9 real-base migration/rollback probe with 10/10 first-run oracle checks, 11/11 final checks and no implementation repair. Ten migration-critical semantics preserve exact parity, reverse-reference compatibility targets remain unbroken, a temporary successor-to-legacy export passes the existing routing validator, live authority files remain unchanged, the authority switch stays blocked, and the migration workstream reconstructs itself from Candidate 01 semantics.

The result raises descriptive evidence coverage to 49/67 items with some real repository evidence and 58/67 with synthetic-or-better evidence while final qualified passes remain zero. Because Q3, Q7 and Q9 have now all received major real/shadow evidence since Research 159, the next step is a fresh whole-architecture evidence reconciliation rather than another inherited subsystem experiment.

```text
Q9_SHADOW_SUBSYSTEM_SUPPORT=PASS
ROLLBACK_EXPORT=PASS
AUTHORITY_SWITCH=BLOCKED
FINAL_QUALIFIED_PASSES=0
NEXT=WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_V02
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 111. Evidence reconciliation V0.2 moves the next test to integrated Q1/Q2/Q5

Research 166 recomputes Candidate 01 evidence after the Q3, Q7 and Q9 programs. The current distribution is 49/67 items with real evidence, 58/67 with synthetic-or-better evidence and 0 final qualified passes. Q3, Q6, Q7, Q8 and Q9 now have real subsystem evidence for every cluster item. Remaining architecture uncertainty is concentrated in Q1/Q2/Q4/Q5 plus the final Q10 governing program.

The highest-value next falsification is one integrated Q1+Q2+Q5 challenge combining fresh successor-native reconstruction/discovery, consequential authority/risk activation and capture -> explicit promotion. Q4 follows; Q10 remains the final multidimensional gate rather than the immediate next task.

```text
WHOLE_ARCH_EVIDENCE_V02=COMPLETE
REAL_EVIDENCE_ITEMS=49_OF_67
SYNTHETIC_OR_BETTER=58_OF_67
FINAL_QUALIFIED_PASSES=0
NEXT=Q1_Q2_Q5_INTEGRATED_CHALLENGE
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 112. Integrated Q1/Q2/Q5 fresh-collaborator fixture freezes

Research 167 freezes the next Candidate 01 challenge against exact public base `f5996aed3710c63e1ba859ee248c264abd678636`. A fresh collaborator must start from a bounded successor-native bootstrap, decide the real Source Vault Course 2 admission question, activate the governing runbook and relevant reopen risks, reject a historical distractor, fail visibly on a stale derived authority view, emit a source-bound authority receipt, and capture at most one new insight without promoting it.

The run is limited to nine allowed evidence reads and zero legacy `CURRENT_STATE` / routing / Knowledge Map bootstrap reads. Current authority is unchanged.

```text
Q1_Q2_Q5_FIXTURE=FROZEN
FRESH_COLLABORATOR=REQUIRED
NEXT=RUN_FRESH_COLLABORATOR_Q1_Q2_Q5_V01
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 113. Integrated Q1/Q2/Q5 fresh-collaborator run passes and exposes revision-binding basis defect

Research 168 records a fresh manual collaborator result with 9/9 bounded evidence reads, zero legacy bootstrap reads, correct Course 2 block, correct governing/risk activation, fail-visible stale derived authority and explicit capture -> review -> shadow promotion. The collaborator result required no repair.

The run also exposed that a bare SHA-256 authority binding is ambiguous across Git-blob versus checkout byte representations. Candidate 01 is amended so repository-backed revision bindings declare commit, path, hash algorithm, hash basis and digest. `GIT_BLOB_BYTES_AT_COMMIT` is the default basis for tracked repository authority.

Evidence coverage rises to 58/67 real and 63/67 synthetic-or-better while final qualified passes remain zero. Q4 real workstream concurrency/interruption stress is next.

```text
Q1_Q2_Q5_INTEGRATED_SUPPORT=PASS
REVISION_BINDING_BASIS=EXPLICIT_DESCRIPTOR_REQUIRED
NEXT=Q4_REAL_WORKSTREAM_STRESS
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 114. Q4 real-source workstream stress fixture freezes

Research 169 freezes the next Q4 challenge against exact Checkpoint 513 base `eece72a16d9664387a67e38998ec715f8efe927e`. The fixture uses current real qualification results/gaps, actual paused Source Vault/Cockpit workstreams and the real Cockpit source bytes. It stresses two multi-dependency nodes, interruption recovery from durable receipts after unrelated work, and an optimistic-concurrency sequence in a temporary Cockpit copy using the Research 168 `GIT_BLOB_BYTES_AT_COMMIT` revision basis.

The coordination edges are explicitly shadow representations of the current qualification program rather than claims about a pre-existing canonical dependency graph. Live workstream mutation is forbidden.

```text
Q4_REAL_FIXTURE=FROZEN
MULTI_DEPENDENCY_NODES=2
REVISION_BASIS=GIT_BLOB_BYTES_AT_COMMIT
CURRENT_ARCHITECTURE=STILL_AUTHORITY
NEXT=IMPLEMENT_Q4_REAL_V01
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 115. Q4 real-source stress passes and closes the remaining Q4 mechanism gap

Research 170 preserves an oracle-blind first Q4 implementation with no repair. All ten declared sources hash-match, the two multi-dependency nodes reconstruct correctly, interruption recovery resumes from S3 without replaying completed S1/S2, and an expected-revision race over the exact frozen Cockpit Git blob rejects the stale writer with zero mutation while fresh writers apply. The live Cockpit source remains unchanged.

The semantic oracle comparison passes 20/20. One literal status-label difference (`STALE_REVISION` versus `REJECTED_STALE_REVISION`) is preserved as non-semantic variance because the fixture did not prescribe a result enum and stale-revision/zero-mutation semantics match exactly.

Q4 now has real subsystem evidence on every cluster item. Descriptive coverage rises to 61/67 real and remains 63/67 synthetic-or-better, with zero final qualified passes. A fresh whole-architecture evidence reconciliation is next.

## 116. Evidence reconciliation V0.3 leaves three pre-Q10 real gaps

Research 171 recomputes all 67 frozen items after Q4. Descriptive evidence is now 61 real, 2 synthetic-only and 4 design-only. Q3/Q4/Q5/Q6/Q7/Q8/Q9 each have real subsystem evidence on every item. The only non-Q10 gaps are KA-R36 provider/tool portability and Q2 KA-R14/KA-R24.

The next experiment combines those three gaps in one controlled non-OpenAI provider challenge with bounded successor-native evidence, probabilistic nomination that cannot decide authority, explicit supersession/supplement/conflict semantics and a deterministic receipt. Q10 follows only after that pre-Q10 challenge.
