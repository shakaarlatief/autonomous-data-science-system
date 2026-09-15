# Research 176: Candidate 01 Owner Selection and Implementation / Migration Program Opening

**Date:** 2026-09-15
**Status:** PKA-CANDIDATE-01 SELECTED SUCCESSOR TARGET / PHYSICAL ARCHITECTURE V0.1 PROPOSED / SPECIFICATION 028 NEXT / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Selection decision:** `D-035`
**Qualification basis:** Research 175 / 67 of 67 frozen requirements and invariants PASS
**Scope:** Convert the selected logical project-development knowledge architecture into a concrete physical implementation and migration program without prematurely switching authority or freezing accidental details of the current representation.
**Authority:** Program-opening record. D-035 selects the target architecture; current continuity remains operational authority until a later explicit qualified cutover.
**Declared references:** `path:docs/DECISIONS.md`, `research:124`, `research:144`, `research:145`, `research:175`, `checkpoint:520`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`

## 1. Selection boundary

The owner has explicitly approved Candidate 01. The project is no longer comparing Candidate 01 as merely one possible architecture family.

```text
qualified                         yes, 67 / 67
selected successor target         yes
owner acceptance                  yes
current operational authority     existing continuity architecture
authority switch allowed          no
```

Selection closes the architecture-family choice under the current evidence boundary. It does not close future evolution: D-035 can be revised explicitly if material new evidence later invalidates the selected architecture.

## 2. What is selected versus what remains open

### Selected now

The project accepts the logical contracts defined by Candidate 01, including:

```text
repository-native canonical semantic ownership
selective durable identity
single-source authority by default
explicit narrow joint-authority exception
scoped supersession / supplementation / specialization / correction semantics
derived current/routing/navigation/search/closure surfaces
retrieval subordinate to authority
explicit capture -> review -> promotion
durable workstream continuation and dependency semantics
fail-visible missing/conflicting authority
action-shaped authority resolution and contract activation
public/private separation
explicit revision binding, concurrency and migration safety
```

### Still open

The following are implementation questions, not reasons to reopen architecture-family selection by default:

```text
exact structured-declaration encoding
physical directory/package layout
which derived views are committed versus ephemeral
JSON/Markdown/SQLite boundaries
identity/authority index storage format
generator and validation implementation structure
reconstruction-planner implementation
search/index implementation details
exact migration wave partitioning
final repository architecture-documentation format
```

Each choice must preserve the selected logical semantics and the 67 frozen acceptance conditions.

## 3. Implementation program

The next stage should proceed architecture-first rather than file-by-file.

### Stage I0: physical architecture and repository contract

Define the concrete implementation architecture for:

```text
semantic source declarations
identity and relationship representation
derived-view manifests and generators
authority resolver and receipts
reconstruction planner / task packets
workstream graph and continuation state
capture / review / promotion
validation and freshness
public/private projections
migration and rollback tooling
```

The physical design may reuse proven shadow implementations, but experiment code is evidence, not automatically production architecture.

### Stage I1: professional architecture documentation

Create durable repository documentation for the selected architecture. It should include at least:

```text
1. one polished whole-architecture overview diagram
2. semantic ownership / identity / authority diagram
3. knowledge capture-promotion and lifecycle diagram
4. fresh-collaborator reconstruction / authority / action flow
5. migration, compatibility, cutover and rollback diagram
```

The whole-architecture view should be understandable on its own and serious enough for professional technical communication. Focused diagrams should carry detail that would make the overview unreadable.

The final diagram technology and exact repository location should be chosen with the physical architecture/documentation design rather than frozen merely because a chat visualization already exists.

### Stage I2: canonical-source migration model

Build a semantic migration inventory by **responsibility**, not by walking existing files in arbitrary order. Partition current knowledge into:

```text
canonical semantic source required
derived compatibility view
historical / latent evidence
capture / candidate material
private delegated state
unresolved migration case
```

Preserve semantic IDs where continuity matters and record transition/tombstone semantics only where genuinely required.

### Stage I3: successor implementation substrate

Implement the production-quality parser/validator/generator/resolver/planner boundaries. Reuse shadow evidence only after converting it into maintainable production code and contracts.

### Stage I4: shadow operation and compatibility parity

Generate successor current-state/routing/navigation/identity/authority views while the current architecture remains authoritative. Differences must be classified semantically, not hidden by byte matching alone.

### Stage I5: bounded migration waves

Migrate high-value live semantics first, then broader durable current knowledge, while leaving deep history latent unless active semantics require conversion. Every wave requires semantic parity, reverse-reference safety and rollback evidence.

### Stage I6: cutover qualification

Before authority switching, rerun the relevant Requirements V0.2 gates against the **actual production implementation and migrated repository state**, including cold continuation, consequential authority resolution, public/private degraded behavior, concurrency, rebuildability and rollback.

### Stage I7: explicit authority-switch decision

Only after I6 may the project consider a separate explicit decision that changes operational authority. Selection and implementation success do not imply cutover.

## 4. Migration invariants

The implementation/migration program inherits these non-negotiable conditions:

```text
one operational authority at a time
no semantic knowledge loss
no silent duplicate authority
no hidden current-vs-historical collapse
no retrieval-ranked authority substitution
no chat-only accepted truth
current compatibility surfaces remain valid until intentionally retired
private details do not leak into public projections
stale writes fail before authoritative mutation
rollback remains possible through the cutover stabilization boundary
```

## 5. Reuse versus rewrite rule

The extensive Candidate 01 shadow implementations are valuable because they already encode tested semantics. They should be treated as **qualified mechanism evidence and reusable implementation material**, not as automatically canonical production modules.

For each reusable component, the implementation stage should decide:

```text
PROMOTE_NEARLY_AS_IS
REFINE_AND_PROMOTE
REIMPLEMENT_BEHIND_SAME_CONTRACT
KEEP_AS_TEST_OR_REFERENCE_ONLY
RETIRE_AFTER_PRODUCTION_EQUIVALENT
```

This avoids both wasteful rewriting and accidental promotion of research scaffolding.

## 6. Documentation and visualization principle

Architecture visualization is now timely because the logical target is selected. The documentation should distinguish:

```text
logical architecture       what semantics and guarantees exist
physical architecture      how the repository/software realizes them
runtime reconstruction     how a fresh collaborator obtains task-safe knowledge
migration architecture     how authority moves safely from legacy to successor
```

A single whole-architecture overview should exist, but it should not be forced to contain every low-level relation. Professional focused diagrams should complement it.

## 7. Immediate next work

The next substantive task is **Stage I0 physical architecture and repository contract**, informed by the already-qualified shadow mechanisms and current repository constraints.

This stage should answer the physical questions without reopening the logical candidate unless implementation evidence exposes a genuine contradiction.

```text
RESEARCH176=SELECTED_CANDIDATE_IMPLEMENTATION_MIGRATION_PROGRAM_OPEN
SELECTED_TARGET=PKA-CANDIDATE-01
OWNER_ACCEPTANCE=true
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=PHYSICAL_ARCHITECTURE_AND_REPOSITORY_CONTRACT
```

## 8. Stage I0 physical architecture proposal completed

Research 177 proposes the concrete repository/software realization: a repo-local `tools/project_knowledge` implementation package separate from ADS product runtime; embedded strict-JSON declarations in natural Markdown canonical sources; profile-specific schemas; deterministic generated structural views; no central authority database; explicit revision/hash-basis descriptors; staged compatibility migration; and durable architecture documentation under `docs/project_knowledge/architecture`.

The next boundary is Specification 028, which should freeze the implementable contract before production code or canonical-source migrations begin.
