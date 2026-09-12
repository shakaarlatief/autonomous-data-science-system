# Research 124: Scalable Repository Knowledge Architecture and Reconstruction Redesign

**Date:** 2026-09-12
**Status:** ACTIVE / PHASE A BASELINE COMPLETE / REQUIREMENTS AND INVARIANTS NEXT / TARGET ARCHITECTURE NOT YET SELECTED
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