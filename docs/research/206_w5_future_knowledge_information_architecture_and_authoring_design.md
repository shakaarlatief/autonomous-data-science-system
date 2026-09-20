# Research 206: W5 Future Knowledge Information Architecture and Authoring Design

**Date:** 2026-09-20
**Status:** ACTIVE / W5 INFORMATION-ARCHITECTURE DESIGN IN PROGRESS
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted boundary:** Checkpoint 554 / Research 205 / W4 ACCEPTED AND FINALIZED
**Scope:** Design the concrete future repository information architecture for ADS project-development knowledge before broader W5 semantic migration: physical folder/file roles, naming and granularity, prospective artifact families, natural-owner placement, multi-axis subject organization, preferred navigation routes, lifecycle/archival behavior, and the ordinary authoring rules that determine what a collaborator should create or update when new knowledge appears.
**Authority:** Active architecture-design research. This record does not yet freeze the future physical layout, rename or move existing historical artifacts, start broad semantic migration, overwrite live compatibility surfaces, or change operational authority.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-27
**Conversation title:** 27 - Project Knowledge Migration and Qualification
**Primary collaborator:** ChatGPT

## 1. Why W5 begins with information architecture rather than migration

W5 is not merely a fact-conversion wave. Before broader current semantic migration, ADS needs a concrete answer to a simpler day-to-day question:

> When durable project knowledge appears tomorrow, what existing source should be updated, or what new repository artifact should be created, where should it live, how should it be named, and how should it participate in navigation without duplicating truth?

Candidate 01 already freezes the deeper logical constraints:

```text
semantic meaning != path
path != identity
natural semantic ownership by default
selective durable identity
one directory hierarchy cannot carry all semantic organization
multi-axis organization without truth duplication
preferred/default route != exclusive semantic parent
derived views contain no unique accepted truth
capture != consolidation != promotion
deep history is not mass-converted merely for structured coverage
Git remains durable project-development authority
```

What remains intentionally open is the concrete future authoring and placement contract.

W5 therefore starts with physical information architecture before broad current-knowledge migration. W6 should consume a settled W5 physical/authoring design rather than inventing repository structure during cutover-candidate construction.

## 2. Baseline repository shape is evidence, not the target design

The current public documentation tree contains twelve root documentation files and these top-level documentation domains/families:

```text
docs/checkpoints/              557 files
docs/cockpit/                    8 files
docs/experiments/                2 files
docs/foundations/               25 files
docs/local_execution/          227 files
docs/methodological_knowledge/   1 file
docs/model_collaboration/      127 files
docs/private_companion/          1 file
docs/project_knowledge/         31 files
docs/research/                 352 files
docs/source_universe/           11 files
docs/specifications/            28 files
```

The root documentation surfaces currently include:

```text
CONTINUITY.md
current_routing.json
CURRENT_STATE.md
DECISIONS.md
DEVELOPMENT_METHOD.md
KNOWLEDGE_MAP.md
MAJOR_CHANGES.md
OPEN_ARCHITECTURE_BACKLOG.md
OPEN_QUESTIONS.md
PRINCIPLES.md
README.md
VISION.md
```

These numbers and paths describe the legacy/current repository at the W5 opening boundary. They are not a mandate to preserve every family, location, filename convention, or hierarchy prospectively.

The current repository also includes non-document development families such as `src/`, `frontend/`, `schemas/`, `migrations/`, `scripts/`, `tests/`, `experiments/`, `prototype_v0/`, `tools/` and repository/runtime control files. W5 must distinguish project-development knowledge architecture from executable source-code architecture while still accounting for where durable implementation evidence belongs.

## 3. W5 design questions

The future information architecture must explicitly answer all of the following.

### 3.1 Physical ownership and placement

```text
What deserves a project-global owner?
What belongs under a semantic/domain directory?
When should a domain gain its own directory?
When is a README only navigation versus a canonical owner?
When should one overloaded file be split?
When should related files be consolidated?
When should a current owner move or be representation-replaced?
Which physical paths are compatibility-only and therefore not target owners?
```

### 3.2 Prospective artifact/file families

W5 must evaluate all present families and any missing future family, not only Research and Checkpoints.

At minimum:

```text
vision / principles
decisions
open questions
deferred architecture obligations
development method
continuity / reconstruction
workstreams
governing procedures
specifications / contracts
foundations / durable rationale
research / investigations
experiments / results
validation evidence
domain control knowledge
operational runbooks
implementation provenance
collaboration records
captures
identity transitions
joint-authority declarations
private-delegated knowledge
generated views
current orientation
navigation / subject views
historical project boundaries
selective structural history
```

Each family must receive a prospective disposition such as:

```text
KEEP_AS_IS
KEEP_BUT_REFINE_CONTRACT
MOVE
RENAME
SPLIT
MERGE
REPLACE_WITH_NATURAL_CANONICAL_OWNER
REPLACE_WITH_GENERATED_VIEW
RETIRE_PROSPECTIVELY
HISTORY_ONLY
UNRESOLVED
```

These are design dispositions, not Specification 028 migration-unit dispositions.

### 3.3 Naming

W5 must freeze enough naming policy that future collaborators do not invent conventions ad hoc.

Questions include:

```text
directory naming style
file naming style
when descriptive names are sufficient
when stable numeric identities are useful
when dates belong in filenames
whether IDs belong in filenames or only declarations
how names relate to semantic identity
how rename/move continuity is represented
how historical artifact naming differs from current canonical-owner naming
```

A filename remains a carrier label, never the semantic identity by itself.

### 3.4 Granularity

W5 must define when knowledge should be:

```text
an edit to an existing canonical owner
a new canonical source
a subsection within an existing domain source
a bounded research/evidence record
a checkpoint
an open capture
a generated projection
historical/latent only
```

The system should avoid both mega-documents and atomizing every claim into its own file/object.

### 3.5 Multi-axis subjects and navigation

Requirement KA-R47 is already frozen:

```text
the same durable knowledge can participate in multiple relevant organizational views
without copying unique truth into independently maintained structures
```

Research 124/126 further establishes:

```text
preferred/default navigation route != exclusive semantic parent
one physical directory hierarchy != the project's semantic organization
organizational/view nodes do not automatically become knowledge entities
```

The current generated `subject_index.json` proves the mechanism at a basic level by projecting multiple memberships from kind/profile/scope metadata. W5 must design the richer authoring model, including:

```text
subject vocabulary ownership
subject identity where justified
subject-to-subject hierarchy / polyhierarchy
multiple parent membership
preferred/default route
authored versus derived membership
domain versus subject versus workstream distinctions
view-only groupings versus durable subject entities
subject aliases/renames when materially needed
how legacy Knowledge Map subjects migrate into successor views
```

The target must not force one manually maintained subject tree to become truth.

### 3.6 Lifecycle

The architecture must explain what happens as knowledge ages:

```text
current canonical -> superseded
active workstream -> paused/completed
open capture -> promoted/rejected/latent -> historical
current experiment -> final result/evidence
current compatibility surface -> derived/retired
current research/design question -> accepted owner / unresolved backlog / historical evidence
```

Physical relocation is optional. Lifecycle semantics should not require moving files merely for cosmetic tidiness when status/identity already expresses the change safely.

### 3.7 Ordinary authoring contract

The final W5 architecture must let a future collaborator answer:

```text
If X happens, update/create Y here.
```

Examples to qualify:

```text
current workstream state changes
new project-global architecture decision is accepted
new domain-specific operating procedure is accepted
conversation produces a potentially durable insight
a substantial investigation is performed
a governed experiment completes
a meaningful continuity boundary is reached
new validation evidence is produced
a domain accumulates enough durable knowledge to need its own owner/navigation
one source belongs to several subjects
a canonical source is renamed/moved/replaced
knowledge becomes historical but remains valuable
```

## 4. Design method: architecture first, representative-corpus pressure test second

W5 must avoid both extremes:

```text
BAD A:
    walk every legacy file in sequence
    -> let accidental history dictate the future structure

BAD B:
    invent a clean folder tree in isolation
    -> discover later that real ADS knowledge does not fit
```

The adopted method is iterative:

```text
frozen Candidate 01 principles
    -> provisional physical/authoring architecture
    -> representative corpus from every major current artifact family
    -> pressure-test awkward / cross-cutting / lifecycle cases
    -> refine
    -> repeat until stable
    -> freeze target information architecture
    -> only then execute broader current semantic migration
```

Historical knowledge is therefore design evidence. It is not automatically a migration target.

## 5. Representative-corpus requirements

Before freezing the target structure, the design must be exercised against representative real ADS cases covering at least:

```text
project-global current control
cross-project decision
principle / vision
foundation rationale
specification
large research program
small bounded research result
checkpoint
experiment result
validation result
workstream
resume target
governing procedure
domain README/control source
operational runbook
implementation provenance ledger/manifest
model-collaboration thread
open architecture backlog item
open question
capture -> promotion history
private-delegated state
generated current/navigation view
cross-cutting knowledge with several legitimate subjects
rename/move/representation-replacement case
```

The corpus should include both files that fit the current structure well and files whose present placement or family role is awkward.

## 6. W5 sub-stages

The working W5 decomposition is:

```text
W5-A  Future knowledge information-architecture design
W5-B  Representative current/historical corpus audit
W5-C  Target physical repository structure
W5-D  Multi-axis subject/navigation authoring architecture
W5-E  Prospective authoring, naming and lifecycle contract
W5-F  Broader current semantic migration using the frozen design
W5-G  Parity, provenance, reverse-reference, rebuild and rollback qualification
```

These labels organize W5 work. They do not independently change operational authority.

## 7. Initial design invariants

The following are frozen inputs rather than topics to casually reopen:

```text
IA-I01  Physical containment expresses primary carrier ownership, not exclusive semantic parentage.

IA-I02  Natural domain/project owners remain preferred over a universal project_knowledge data registry.

IA-I03  Current durable meaning should not require reading historical research/checkpoint chronology when a stronger natural current owner exists.

IA-I04  Historical evidence may remain in its original carrier/form when semantic migration is unnecessary.

IA-I05  Generated navigation/current-state surfaces contain no unique accepted truth.

IA-I06  One durable source may participate in multiple subject/workstream/provenance/temporal views without truth duplication.

IA-I07  Subject/view groupings do not automatically receive durable semantic identity.

IA-I08  File and directory names must be useful to humans but are not semantic identity.

IA-I09  Rename/move/representation replacement must preserve continuity when the project regards the underlying semantic thing as continuous.

IA-I10  Future authoring should normally update an existing natural canonical owner rather than create another global summary copy.

IA-I11  New file families require a distinct semantic/lifecycle responsibility, not merely a desire for tidier folders.

IA-I12  W5 target design must remain portable through ordinary Git/filesystem tooling and must not require a database merely to know where project knowledge belongs.
```

## 8. Baseline observations already visible

Several current patterns are immediately useful as design evidence:

1. `CURRENT_STATE.md` and `KNOWLEDGE_MAP.md` grew because one manually maintained artifact accumulated several responsibilities. W2/W3 already demonstrate the successor alternative: small canonical owners plus derived views.
2. `docs/research/` and `docs/checkpoints/` are large primarily because they preserve chronology/evidence. Their size alone is not evidence that they should be physically rewritten.
3. Domain-local areas such as `docs/source_universe/` and `docs/cockpit/` demonstrate that some knowledge has a natural subject/domain home independent of artifact type.
4. `docs/local_execution/` and `docs/model_collaboration/` demonstrate specialized operational/provenance families with substantial internal structure. W5 must decide whether those structures remain appropriate prospectively rather than flattening them into global artifact families.
5. Candidate 01's current `docs/project_knowledge/` area is correctly narrow: architecture documentation, project-global boundary/workstream owners, generated views, captures and exceptional transition/joint-authority carriers. W5 should preserve that anti-registry boundary unless evidence disproves it.
6. Existing filename numbering is useful for some chronological/evidence families but should not automatically become the naming strategy for future current canonical owners.

## 9. What W5 will not do yet

At this opening design boundary:

```text
no mass renames
no mass directory moves
no rewrite of historical Research/Checkpoint/Validation files
no automatic creation of declarations across legacy history
no compatibility-path overwrite
no authority switch
no assumption that every current folder survives
no assumption that every current folder is removed
no final subject taxonomy yet
```

Those outcomes must follow evidence from the design and representative-corpus phases.

## 10. Immediate next action

Build the first W5 representative artifact-family matrix from real repository sources and use it to draft the target physical/authoring architecture.

The matrix must track at least:

```text
current family / example
semantic responsibility
current authority role
current lifecycle role
current physical home
prospective family
prospective physical-home rule
prospective naming rule
multi-axis membership needs
prospective disposition
migration implication
open design questions
```

Only after the representative matrix exposes enough real cases should W5 freeze the new information architecture and begin broad semantic migration.

```text
W4=ACCEPTED_AND_FINALIZED
W5=IN_PROGRESS
W5_CURRENT_SUBSTAGE=INFORMATION_ARCHITECTURE_DESIGN
TARGET_PHYSICAL_STRUCTURE=NOT_YET_FROZEN
TARGET_AUTHORING_CONTRACT=NOT_YET_FROZEN
TARGET_SUBJECT_ARCHITECTURE=NOT_YET_FROZEN
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=REPRESENTATIVE_ARTIFACT_FAMILY_MATRIX_AND_TARGET_DESIGN
```
