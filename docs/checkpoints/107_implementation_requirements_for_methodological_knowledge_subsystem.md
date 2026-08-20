# Checkpoint 107: Implementation Requirements for the Methodological Knowledge Subsystem

**Date:** 2026-08-20  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 methodological-navigation architecture; implementation-requirements derivation  
**Scope:** Derives technology-neutral implementation requirements from Foundations 018-020 before comparing persistence, retrieval, rule-evaluation, or backend architecture options.  
**Authority:** Historical provenance and active implementation-requirements hypothesis. Foundation 020 and current canonical documents govern conceptual meaning; no technology choice is made here.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## Why this checkpoint exists

Foundation 020 promoted the conceptual representation for reusable methodological knowledge. Checkpoint 106 then changed the active task from representation design to implementation-requirements derivation.

The project should not choose a database, graph store, vector store, rules engine, backend, or other technology merely because the conceptual model contains assets, relations, rules, revisions, and project references.

The correct sequence is:

```text
conceptual meaning
    -> implementation requirements
    -> workload / query patterns
    -> architecture options
    -> comparative evaluation
    -> smallest justified implementation
```

This checkpoint performs the second step and makes the expected workload explicit enough that technology comparison can be evidence-based.

---

## 1. Boundary of this requirements exercise

The requirements here concern the implementation boundary around:

```text
GLOBAL METHODOLOGICAL KNOWLEDGE
PROJECT-STATE ACCESS NEEDED BY THE METHODOLOGICAL BRAIN
METHODOLOGICAL-HORIZON CONSTRUCTION
SELECTIVE LLM CONTEXT ASSEMBLY
KNOWLEDGE GOVERNANCE / HISTORY
HUMAN KNOWLEDGE NAVIGATION
EXECUTION-CAPABILITY REFERENCES
```

They do not attempt to specify the complete future product backend.

In particular, this checkpoint does not fully specify:

```text
large artifact storage
model-serving infrastructure
notebook execution
job scheduling
frontend framework
identity/authentication
billing
cloud deployment
multi-tenant infrastructure
```

Those areas may interact with the knowledge subsystem later but should not distort the first implementation choice.

---

## 2. Requirement classes

Every requirement is classified using one of three states:

```text
V1 MUST HAVE
    needed to preserve promoted conceptual semantics or to test
    the methodological-navigation product honestly

VALUABLE LATER
    useful extension, but V1 can remain valid without it

NOT YET JUSTIFIED
    complexity for which the project currently lacks evidence
```

`V1 MUST HAVE` does not mean the first implementation must be maximally sophisticated. It means the capability must exist in a defensible minimal form.

---

# 3. V1 MUST HAVE requirements

## A. Knowledge identity, revisions, and historical reconstruction

### IR-001: Stable knowledge identity

The implementation must provide a stable identity for every addressable `KnowledgeAsset` independent of its display title, file location, current revision, or execution implementation.

Reason:

```text
projects, relations, components, and history need to reference
"the same methodological knowledge" even when wording changes
```

### IR-002: Distinct revision identity

The implementation must distinguish stable asset identity from a specific knowledge revision.

A project object that materially relied on a knowledge revision must be able to preserve that exact revision reference.

### IR-003: Recoverable historical revisions

Accepted historical revisions must remain recoverable after later edits or supersession.

The system must not silently mutate the methodological basis of historical Questions, Findings, Claims, Decisions, or Runs.

This does not require event sourcing as an implementation technique. It requires recoverable historical interpretation.

### IR-004: Explicit current revision / governance selection

The system must be able to determine which revision is currently accepted for new reasoning while preserving older revisions for history.

Governance state must be inspectable rather than inferred from recency alone.

---

## B. Components, narrative facets, and provenance granularity

### IR-005: Stable component addressing where required

A `KnowledgeComponent` that needs provenance, review, relation targeting, or revision semantics must be addressable below its parent asset.

The implementation does not need independent global retrieval for every component.

### IR-006: Component-level provenance

The system must support provenance below the top-level asset when an important component or rule is sourced, reviewed, challenged, or scoped independently.

### IR-007: Narrative content without object explosion

The implementation must support non-addressable explanatory content (`NarrativeFacet`) without forcing every paragraph, example, or explanatory sentence into a separate global object.

### IR-008: Promotion without destructive migration

It must be possible to promote an important component into a standalone asset later without losing its provenance/history or breaking historical references unnecessarily.

The exact migration mechanism is implementation-specific.

---

## C. Typed semantic relations

### IR-009: Typed relation storage and lookup

The system must support typed semantic relationships among knowledge assets/components.

At minimum it must support efficient queries of the form:

```text
outgoing relations from X
incoming relations to X
relations of type T from X
relations of type T to X
```

### IR-010: Scoped/rationalized relationships where material

A relation must be able to carry scope/conditions and rationale when the relationship is not universally valid.

For example:

```text
Histogram ALTERNATIVE_TO ECDF
for distribution characterization
```

should not degrade into an unexplained generic edge.

### IR-011: Relation provenance and history

Material relations must be governable and historically interpretable. A changed or superseded relationship must not silently rewrite old project reasoning.

### IR-012: Bounded traversal

The implementation must support bounded local traversal of knowledge relationships without requiring the complete knowledge network to be loaded into memory or into an LLM context.

V1 does not require arbitrary graph algorithms.

---

## D. Conditional methodological rules

### IR-013: Explicit rules distinct from static relations

The implementation must represent guarded methodological implications separately from static knowledge relations.

### IR-014: Minimal explicit condition composition

The rule representation must support, at minimum, the conceptual equivalents of:

```text
predicate reference
ALL
ANY
NOT
UNKNOWN
```

This is sufficient for the branch structures demonstrated by Missing Data, Temporal Validation, Prediction-Time Feature Eligibility, and Class Imbalance.

### IR-015: Tri-valued / unknown-aware evaluation

Rule evaluation must distinguish at least:

```text
TRUE
FALSE
UNKNOWN / unresolved
```

Missing context must not silently become `false`.

### IR-016: Explicit rule consequence category

A rule must be able to express a consequence category such as:

```text
activate concern
activate/create Question
require evidence
recommend option
raise priority
lower priority
apply validity constraint
constrain claim
request clarification
require revalidation
```

The exact vocabulary can remain small and extensible.

### IR-017: Rule force and unknown behavior

A rule must carry enough semantics to distinguish hard validity from soft guidance and to state what happens when required context is unknown.

Conceptually:

```text
force = hard / strong / heuristic / informational
unknown behavior = ask / defer / block dependent claim / no inference
```

### IR-018: No hidden analytical action execution

Rule evaluation must not silently perform project actions such as dropping a feature, selecting a model, or accepting a claim.

Rules may create or influence project Questions, Proposals, Constraints, Findings, or Decisions according to the product's configured autonomy model.

### IR-019: Inspectable rule trace for consequential outcomes

When a rule materially contributes to `REQUIRED / BLOCKING`, a validity constraint, or another consequential recommendation, the system must be able to explain:

```text
which rule revision was evaluated
which project facts/findings/definitions it depended on
which condition was true/false/unknown
what consequence was produced
```

This trace can be persisted or reproducibly derived; the storage choice remains open.

---

## E. Retrieval, applicability, and methodological-horizon construction

### IR-020: Direct identity lookup

Exact asset/revision/component lookup must be fast and reliable.

### IR-021: Human text search

The system must support useful text/keyword search over titles, purposes, scope, narrative, concepts, and provenance metadata.

A user should be able to find known knowledge without remembering exact identifiers.

### IR-022: High-recall semantic candidate retrieval

V1 must support retrieval beyond exact keyword matching strongly enough to test the methodological-horizon concept honestly.

This is a capability requirement, not a mandate for embeddings or a vector database.

Acceptable implementations could theoretically include combinations of:

```text
lexical retrieval
structured filtering
synonyms/taxonomy expansion
semantic embeddings
LLM query expansion / reranking
other retrieval approaches
```

Technology remains undecided.

### IR-023: Retrieval cues remain distinct from applicability

The system must preserve the distinction:

```text
retrieved because possibly relevant
    !=
applicable
```

A timestamp may retrieve temporal-validation knowledge without proving that temporal validation is appropriate.

### IR-024: Explicit applicability filtering where reliable

The implementation must support explicit prerequisites/exclusions when they can be evaluated cheaply and reliably.

### IR-025: Context-requirement discovery

The system must be able to identify which project Definitions/Facts/Findings/Questions are required to determine applicability or evaluate a rule.

Missing validity-critical context should be able to become a project Question rather than disappear as a failed filter.

### IR-026: Semantic applicability checks

Applicability questions that genuinely require interpretation must be representable as semantic checks resolved by flexible reasoning, project evidence, or human clarification rather than forced into a brittle rule language.

### IR-027: Bounded methodological horizon

The result of retrieval/filtering must be a bounded project-specific candidate set rather than the full global catalog.

The bound may be configurable by task and context. Foundation 019's illustrative `5,000 -> 60` example is not a fixed numeric contract, but the architecture must support this compression pattern.

### IR-028: Relevance/ranking rationale

The system must be able to explain why a retrieved/applicable asset was:

```text
relevant
recommended
required
not recommended
deferred
```

and which project facts, costs, risks, existing evidence, or human preferences contributed.

### IR-029: Explainable omission states

The implementation must preserve enough information to distinguish:

```text
not known to system
known but not retrieved
retrieved but inapplicable
applicable but low relevance
relevant but not recommended
recommended but skipped
required but unresolved
```

This is important both for user trust and future system evaluation.

---

## F. Project-state integration

### IR-030: Typed project-state lookup

The methodological subsystem must be able to query current project objects relevant to reasoning, including at least concepts represented by Foundation 018 such as:

```text
Definition
Variable
Dataset
Question
Assumption
Evidence
Finding
Claim
Constraint
Proposal
Investigation
Run
Decision
```

The knowledge subsystem should consume project-state interfaces rather than require the global knowledge store to own all project data.

### IR-031: Current versus historical project state

Queries used for current methodological reasoning must distinguish current/superseded/stale project state from historical provenance.

### IR-032: Project references to exact knowledge revisions

When a project object is materially generated, constrained, interpreted, or justified by reusable knowledge, the project must be able to reference the exact knowledge revision involved.

### IR-033: Criterion-Finding support

The project model must support structured criterion Findings with at least:

```text
subject
criterion knowledge revision
verdict
conditions
supporting evidence
rationale
```

without adding a universal top-level Assessment object.

### IR-034: Re-evaluation signaling

When a validity-critical project Definition/Finding changes or a governing knowledge revision is superseded, the system must be able to identify that dependent current reasoning may require reconsideration.

V1 does not need universal recursive invalidation or P0-style generic reopening machinery. A selective, inspectable re-evaluation obligation is sufficient.

---

## G. Provenance, governance, and mutation

### IR-035: Provenance is first-class

Assets, material components, relations, and rules must be able to cite their source/provenance.

Provenance may include:

```text
source document/reference
human author/reviewer
LLM-assisted derivation
project lesson that motivated the knowledge
review/challenge history
```

### IR-036: Candidate-to-accepted governance workflow

V1 must support a minimal lifecycle in which new or changed reusable knowledge can remain a candidate until reviewed/accepted.

A general LLM should not silently promote its own novel methodological suggestion into trusted global knowledge.

### IR-037: Supersession without deletion

Superseding knowledge must preserve the historical asset/revision and the reason/scope of supersession.

### IR-038: Conflict representation

The implementation must permit contradictory or scope-competing knowledge to coexist long enough to be reviewed rather than forcing last-write-wins truth.

Exact contradiction-resolution workflow can remain simple in V1.

### IR-039: Human-reviewable representation/export

Knowledge changes must be inspectable in a human-readable form suitable for review, diffing, and debugging.

The runtime store may be structured, but the project must not create an opaque methodological database that humans cannot audit.

### IR-040: Rebuildable derived indexes

Search indexes, embeddings, caches, and other acceleration structures should be treated as rebuildable derived state where practical, not as the sole authority for methodological knowledge.

This prevents index corruption or model replacement from destroying the canonical knowledge record.

---

## H. Selective LLM context assembly

### IR-041: Task-specific context packs

The implementation must assemble reasoning context selectively from:

```text
current project facts/state
current methodological horizon
specific knowledge components/rules relevant to the task
current evidence/constraints
```

rather than serializing the complete persistent system state.

### IR-042: Explicit context budget

Context assembly must support bounded token/size budgets and prioritization.

The V0 result makes this an architectural requirement, not an optimization afterthought.

### IR-043: Context provenance

A consequential reasoning call must be able to identify which project objects and knowledge revisions were supplied to it.

This supports reproducibility, debugging, evaluation, and later comparison of retrieval strategies.

### IR-044: Mixed structured and narrative context

Context assembly must support both:

```text
compact structured facts / relations / rule outcomes
and
selected narrative methodological explanation
```

because maximum formalization is not the Foundation 020 goal.

### IR-045: Context generation separate from persistence

The persistent representation must not be designed around the exact prompt serialization format of one LLM or model generation.

Different models or reasoning tasks should be able to receive different projections of the same persistent state.

---

## I. Human navigation and inspectability

### IR-046: Browse knowledge catalog

V1 should allow the user to inspect the global knowledge catalog by meaningful collections/categories without exposing internal storage tables as the primary UX.

### IR-047: Search and open an asset

A user must be able to search for and inspect:

```text
what the asset means
scope/limitations
current revision
provenance
important components
relations
applicability information
```

### IR-048: Inspect why knowledge is active in a project

For a current project, the user should be able to inspect why an asset/framework/rule entered the methodological horizon and what current project state made it relevant.

### IR-049: Derived workflow views supported by underlying data model

The implementation must be capable of rendering derived views such as:

```text
Missing Data decision tree
feature-eligibility matrix
validation-design decision map
model-option comparison
required/blocking concerns
```

V1 does not need all of these polished, but the data model must not make them impossible without hard-coded duplicate workflows.

### IR-050: Historical knowledge inspection

The user or developer must be able to inspect earlier revisions when debugging why an old project decision was made.

---

## J. Execution-capability boundary

### IR-051: Methodological knowledge does not own library-specific execution

A METHOD or INVESTIGATION_PATTERN must remain meaningful independently of a concrete software implementation.

### IR-052: Zero-or-more execution capabilities

An executable methodological asset may map to zero, one, or several `ExecutionCapability` implementations.

The system must not infer methodological relevance merely from implementation availability.

### IR-053: Capability compatibility metadata

Automated execution needs enough implementation-specific metadata to answer questions such as:

```text
can this implementation execute this method here?
what input form is supported?
what configuration mapping is required?
what output is produced?
what implementation-specific limitations apply?
```

A minimal registry is sufficient for V1.

---

## K. Data integrity, operational simplicity, and portability

### IR-054: Referential integrity

The system must avoid dangling references among current project objects, knowledge revisions, components, relations, and rules.

If a historical target is retained rather than deleted, historical references must remain resolvable.

### IR-055: Atomic consequential writes

A write that creates a new accepted knowledge revision and updates its current-governance pointer should not leave the system in a half-updated state after interruption.

Equivalent integrity guarantees are required for other multi-record changes that would otherwise create inconsistent current state.

### IR-056: Deterministic export / backup path

The authoritative methodological knowledge and governance metadata must be exportable or backupable in a durable, inspectable form.

Vendor-specific runtime storage should not become the only recoverable representation of the system's methodological memory.

### IR-057: Single-user/local development must be practical

The first implementation must be able to run in a normal development environment without requiring distributed infrastructure.

This is compatible with remote LLM APIs and with later cloud deployment. It does not require every future product deployment to be local-only.

### IR-058: Low operational burden

The first architecture should minimize the number of independently operated stateful services unless another requirement clearly justifies them.

This is a derived requirement from the project's falsification/simplicity philosophy and from the current local-first development hypothesis.

### IR-059: Large artifacts remain outside the methodological knowledge store

Datasets, trained models, large arrays, plots, and other heavy artifacts should be referenced by identity/provenance rather than embedded as large payloads in the knowledge subsystem.

---

# 4. Expected V1 workload and design envelope

The following are **comparison assumptions**, not permanent product limits.

They exist so technologies can be compared against a plausible workload rather than against unlimited hypothetical scale.

## Knowledge scale

Foundation 019 used a `5,000 knowledge units -> 60-unit horizon` illustration. The first implementation should therefore be comfortable with at least an **order-of-thousands** global knowledge catalog and a substantially larger number of components, relations, rules, and provenance records.

A reasonable architecture-comparison envelope is:

```text
KnowledgeAsset revisions:
    thousands to low tens of thousands

KnowledgeComponents / relations / rules / provenance records:
    tens of thousands to low hundreds of thousands

KnowledgeCollections:
    small relative to assets
```

These are not capacity promises. They are intended to prevent both designs that require full-catalog scans for every interaction and designs optimized prematurely for web-scale billions of nodes.

## Project-state scale

A professional long-running project may plausibly accumulate:

```text
hundreds to thousands of Questions / Findings / Claims / Decisions
thousands to tens of thousands of Runs / Evidence / events / references
```

The methodological subsystem should therefore retrieve targeted project slices rather than serialize all project history for each reasoning call.

## Concurrency

For V1:

```text
single active project writer is acceptable
multiple read operations / UI views should be safe
high-contention multi-user editing is not required
```

The architecture should avoid making later multi-user support impossible, but real-time collaborative editing is not a first-selection requirement.

## Latency

The intended product is interactive.

Architecture comparison should prefer designs where:

```text
identity lookup / local relation lookup / structured filtering
    feel effectively immediate

catalog search / methodological-horizon candidate retrieval
    completes on an interactive timescale before LLM reasoning
```

Exact service-level numbers are not frozen yet. The important constraint is that persistence/retrieval overhead should not become the dominant latency relative to reasoning and analytical execution.

## Availability

V1 does not require distributed high availability.

Recoverability, integrity, and reproducibility matter more than failover complexity at this stage.

---

# 5. Canonical query/workload patterns that architecture comparison must support

Any candidate architecture should be tested against concrete operations rather than generic feature lists.

## Knowledge identity/history

```text
get current accepted revision for asset X
get historical revision R of asset X
list revision history for X
show provenance for revision R
```

## Components

```text
list components of asset revision R
open component C
show component provenance
resolve historical component reference
```

## Relations

```text
find alternatives to method X
find frameworks containing X
find constraints governing X
find all assets that reference concept prediction_moment
bounded traversal: X -> governing constraint -> required context concept
```

## Rules

```text
find rules relevant to framework Missing Data
evaluate applicable explicit predicates against current project state
return TRUE/FALSE/UNKNOWN with trace
find rules whose consequence can block claim Y
```

## Retrieval/horizon

```text
retrieve possible knowledge for:
    "binary churn prediction with time and repeated customers"

filter obvious incompatibilities
identify missing context requirements
construct bounded methodological horizon
rank/explain required/recommended/relevant/not-now items
```

## Project integration

```text
get current prediction-moment Definition
get current Variable semantics / availability Findings
find unresolved Questions required by feature-eligibility rule
find current Findings supporting validation decision
find project objects influenced by knowledge revision R
```

## LLM context

```text
assemble context for:
    "decide what missing-data investigation should happen next"

include only:
    relevant project facts
    active framework/rules/questions
    selected supporting methodological narrative
    provenance IDs

exclude:
    unrelated project history
    full global knowledge catalog
```

## Human navigation

```text
search "random forest"
open asset
inspect mechanism / limitations / alternatives
show why it is or is not recommended in current project
browse Models > Tree Ensembles without changing methodological authority
```

## Governance

```text
create candidate revision
compare with current revision
review provenance/scope changes
accept or reject
supersede current revision
preserve historical project references
```

These workloads should become the test cases for the architecture comparison rather than relying only on theoretical feature matching.

---

# 6. VALUABLE LATER capabilities

The following capabilities are plausible extensions but are not needed to validate the first architecture:

```text
real-time multi-user collaborative editing
fine-grained RBAC / enterprise permission models
remote synchronization across many installations
cross-project organization-wide knowledge sharing
automatic cross-project impact notifications after knowledge revision
large-scale knowledge analytics across thousands of projects
advanced graph visualization
complex graph algorithms / centrality / community detection
ontology alignment to external semantic standards
specialized authoring IDE for methodological rules
background distributed indexing
multiple embedding models with learned retrieval routing
large-scale A/B testing of retrieval algorithms
fully automated knowledge-gap promotion
cross-project autonomous knowledge synthesis
cloud high availability / replicas / multi-region deployment
```

The architecture should avoid gratuitously preventing these, but V1 should not pay their full complexity cost.

---

# 7. NOT YET JUSTIFIED as architecture requirements

Nothing in Foundations 018-020 currently requires any of the following technologies or patterns:

```text
dedicated graph database
vector database as a separate service
dedicated production rules engine
RDF / OWL ontology stack
property-graph query language
custom methodology DSL
full event sourcing of every object
CQRS
Kafka or another distributed event bus
microservice decomposition
Kubernetes
distributed transactions
multi-region replication
GPU-hosted embedding infrastructure
one agent per knowledge type
one persistent LLM conversation per project object
full-state serialization into every LLM call
automatic recursive dependency reopening like P0
```

These may become useful later, but choosing them now would be technology-first rather than requirements-first.

---

# 8. Architecture-comparison criteria derived from the requirements

The next technology comparison should score candidate architecture families against at least these dimensions:

```text
1. semantic fit
   Can it represent assets, revisions, components, relations, rules,
   provenance, and project references without awkward duplication?

2. historical integrity
   Can exact prior knowledge revisions remain recoverable and referencable?

3. query/workload fit
   How naturally does it support the canonical operations in Section 5?

4. retrieval flexibility
   Can structured, lexical, and semantic retrieval be combined without
   making one derived index authoritative?

5. rule-evaluation fit
   Can simple explicit rules be stored/evaluated/audited without requiring
   a full rules platform?

6. selective context assembly
   Can targeted project + knowledge slices be assembled cheaply?

7. human inspectability
   Can knowledge and history be reviewed/exported/debugged clearly?

8. transactional / referential integrity
   Can current state remain internally consistent under mutation?

9. local development simplicity
   Can one developer run, test, back up, and inspect the system easily?

10. operational burden
    How many services, indexes, migrations, and failure modes are introduced?

11. portability
    Can project/system data be exported and moved without trapping the
    methodological memory in one proprietary runtime?

12. extensibility
    Can later semantic retrieval, richer collaboration, or larger scale be
    added without discarding the conceptual model?

13. testability
    Can retrieval, rule evaluation, provenance, and context assembly be
    regression-tested deterministically where appropriate?

14. failure isolation
    Can a derived search/index service fail or be rebuilt without corrupting
    authoritative methodological/project state?

15. cost
    Development effort, runtime resource usage, maintenance burden, and
    cognitive complexity.
```

No single dimension should dominate automatically. The project's existing simplicity principle means additional services or abstractions need concrete benefits against these requirements.

---

# 9. Scenario sanity check

The V1 requirements were checked against the methodological examples used to derive Foundation 020.

## Missing Data

Needs:

```text
Framework + Question templates + local rule components
cross-cutting constraints
strategy/method relations
TRUE/FALSE/UNKNOWN rule evaluation
project Question creation
human-facing derived tree
```

Covered by IR-005 through IR-019, IR-025 through IR-034, and IR-049.

## Temporal Validation

Needs:

```text
Concept lookup for prediction moment / target horizon
Framework retrieval
validity rules
method alternatives
project Definition lookup
conditional relevance
```

Covered by relation/rule/project-context/horizon requirements.

## Random Forest

Needs:

```text
Method asset
components/narrative
relations to Bagging / alternatives
implementation-capability mapping
semantic retrieval
```

Covered without making method execution part of the global knowledge record.

## Prediction-Time Feature Eligibility

Needs:

```text
hard RULE revision
project Definitions / lineage Evidence
criterion Finding
Decision
revalidation signaling if prediction semantics change
```

Covered without adding a universal Assessment object or universal P0-style reopening engine.

## Class Imbalance

Needs:

```text
cross-cutting Framework appearing in multiple navigation collections
multiple methods/strategies
metric-interpretation constraints
threshold/calibration follow-ups
project-objective context
```

Covered without requiring one rigid stage hierarchy.

The requirements therefore appear sufficient for the promoted representation while remaining smaller than a full enterprise data platform specification.

---

# 10. Important design consequences already visible

Several consequences follow before any technology comparison:

### The authoritative representation and derived retrieval indexes should be separable

Semantic retrieval is required, but a semantic index does not need to be the source of truth.

This leaves open architectures in which:

```text
canonical structured state
    -> derived lexical index
    -> derived semantic index
```

or a single storage system provides several of those capabilities.

### Graph-like relationships do not imply a graph database

The workloads require local typed relation traversal, not yet large-scale arbitrary graph analytics.

### Conditional rules do not imply a dedicated rules engine

The promoted rule language is intentionally small. A simple application-level evaluator could satisfy V1 if it remains explicit, testable, and auditable.

### Semantic retrieval does not imply a dedicated vector database

The architecture must support semantic candidate retrieval, but scale and operational simplicity may favor an embedded or integrated index initially.

### Historical revision requirements are stronger than raw search requirements

Search can be rebuilt. Historical knowledge references cannot be casually reconstructed after destructive overwrites.

### Project-state integration may matter more than a sophisticated knowledge graph

A method can be perfectly represented globally yet still be useless if the system cannot retrieve the current prediction moment, target definition, variable semantics, unresolved Questions, or Findings needed to assess applicability.

### LLM context assembly is a first-class subsystem

Prototype V0 demonstrated that persistence architecture cannot be evaluated only by what it can store. It must also support cheap, bounded, task-specific extraction.

---

# 11. Open questions to resolve during architecture comparison

The requirements intentionally leave several implementation decisions open:

```text
Should global methodological knowledge and project state use the same
physical database or separate stores behind one interface?

Should revision history use immutable revision rows/documents, Git-backed
files, append-only records, or another technique?

Should component revisions be independent or inherit the asset revision?

How much project event history needs first-class persistence in V1?

What exact structured predicates should the first rule evaluator support?

How should semantic checks invoke LLM/human reasoning without making
rule evaluation nondeterministic and opaque?

What retrieval stack gives strong recall at the expected scale with the
fewest independently operated services?

Should human-authored methodological knowledge have a file-based authoring
source that compiles/imports into runtime storage, or should the runtime
store itself be the primary authoring surface?

What exact provenance is mandatory for candidate versus stable knowledge?

How should current knowledge revisions be selected and promoted atomically?
```

These should be answered by comparing architecture families against the requirements, not by assuming a preferred technology.

---

# 12. Promotion audit

## New foundation

Not warranted yet.

Foundation 020 already governs the conceptual representation. This checkpoint derives active implementation requirements that should first be tested against concrete architecture options.

## New principle

Not warranted yet.

The requirements mostly operationalize existing principles, especially repository authority, provenance, hybrid reasoning, simplicity, professional workflow integration, and the V0 context-scaling lesson.

## Current-state update

Warranted. The project has completed the implementation-requirements derivation step and can move to architecture-family comparison.

## Knowledge-map update

Useful but not strictly required for conceptual authority. Foundation 020 remains the primary promoted representation source; this checkpoint should be routed as the active implementation-requirements artifact until architecture selection advances.

## V1 implementation

Still not warranted.

Requirements are now explicit enough to compare architecture families, but no architecture has yet been selected or falsified.

---

# 13. Exact continuation point

The next legitimate step is a **technology-neutral architecture-family comparison** against this requirements matrix.

At minimum compare:

```text
A. Git/file-centric canonical knowledge + application indexes
B. embedded relational database architecture
C. relational database + integrated/derived semantic retrieval
D. document-oriented architecture
E. dedicated graph-oriented architecture
F. multi-store/hybrid architecture
```

The comparison should not assume that each family requires a separate service. It should distinguish embedded versus client/server variants where operational burden changes materially.

For every family, evaluate:

```text
representation fit
revision/history handling
relations
rules
semantic retrieval
project-state integration
context assembly
human inspectability
local-first workflow
operational burden
future extension
failure modes
```

Then identify the **smallest architecture that satisfies the V1 MUST requirements while preserving credible extension paths**.

Do not implement V1 until that comparison is complete.