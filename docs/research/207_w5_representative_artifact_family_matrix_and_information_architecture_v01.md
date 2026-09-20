# Research 207: W5 Representative Artifact-Family Matrix and Future Information Architecture V0.1

**Date:** 2026-09-20
**Status:** PROVISIONAL W5 DESIGN V0.1 / REPRESENTATIVE CORPUS AUDIT COMPLETE / ADVERSARIAL REVIEW NEXT
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Parent design record:** Research 206
**Scope:** Pressure-test the W5 future-authoring questions against representative real ADS artifact families and propose a concrete V0.1 target for physical placement, file/folder naming, artifact-family roles, multi-axis subject organization, lifecycle, and ordinary authoring behavior.
**Authority:** Design candidate only. This record does not yet authorize broad renames/moves, schema changes, semantic migration, compatibility overwrite, or authority cutover.

## 1. Result in one sentence

The current ADS repository does **not** need a wholesale folder-tree replacement. Its strongest future structure is a hybrid:

```text
small project-global singleton control surfaces at docs/
+
top-level epistemic/lifecycle families for rationale/contracts/research/history
+
top-level semantic/domain homes for current domain knowledge
+
a deliberately narrow docs/project_knowledge/ infrastructure area
+
generated multi-axis navigation that is independent of physical containment
```

The major redesign is therefore not "move everything into a new master hierarchy." It is to make the physical tree express **primary carrier ownership**, make current durable meaning live in natural owners, make evidence/history remain evidence/history, and let generated multi-axis views carry cross-cutting subject organization.

## 2. Representative corpus

The representative audit covers these real source classes:

```text
project-global vision
project-global principles
project-global decisions
open questions
deferred architecture obligations
development method
continuity/reconstruction
current state/routing
Knowledge Map/navigation
selective structural history
foundation
specification
large architecture research program
accepted migration research result
checkpoint
scientific experiment result
local-execution operating guidance
local-execution validation evidence
model-collaboration protocol/thread structure
Cockpit domain control/provenance
Source Universe workstream/procedure/evidence
Methodological Knowledge coverage
private-companion public contract
project-knowledge architecture docs
project-knowledge captures
generated successor views
specialized ledgers/manifests
```

The audit also considers executable source/test/schema trees as adjacent implementation artifacts so documentation is not asked to duplicate what code/Git already owns.

## 3. Artifact-family matrix

| Current family / representative | Primary semantic responsibility | V0.1 prospective disposition | Target physical-home rule | Prospective naming rule |
| --- | --- | --- | --- | --- |
| `docs/README.md` | Structural repository landing/navigation | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton | Reserved singleton name |
| `docs/VISION.md` | Current project/product direction | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton | Preserve reserved singleton |
| `docs/PRINCIPLES.md` | Current cross-project principles | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton | Preserve reserved singleton |
| `docs/DECISIONS.md` | Accepted explicit cross-project decisions | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton | Preserve reserved singleton; local/domain decisions should remain with natural domain owner when not cross-project |
| `docs/OPEN_QUESTIONS.md` | Material unresolved cross-project questions | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton | Preserve reserved singleton; domain questions should normally be domain-local |
| `docs/OPEN_ARCHITECTURE_BACKLOG.md` | Explicit deferred architecture obligations | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton while backlog remains cross-project | Preserve reserved singleton |
| `docs/DEVELOPMENT_METHOD.md` | Current operational method for building ADS | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global singleton | Preserve reserved singleton |
| `docs/CONTINUITY.md` | Bootstrap/reconstruction procedure | KEEP_BUT_REFINE_CONTRACT | `docs/` bootstrap singleton | Preserve reserved singleton; future reduction allowed after cutover |
| `docs/CURRENT_STATE.md` | Legacy live human orientation | REPLACE_WITH_GENERATED_VIEW at cutover | compatibility path until W6-W8; successor current-state core/generated candidate after qualified switch | Compatibility filename preserved through migration |
| `docs/current_routing.json` | Legacy compact machine route | REPLACE_WITH_GENERATED_VIEW at cutover | compatibility path until W6-W8 | Compatibility filename/schema preserved through migration |
| `docs/KNOWLEDGE_MAP.md` | Legacy semantic subject library | REPLACE_WITH_GENERATED_MULTI_AXIS_NAVIGATION at cutover | compatibility path until W6-W8; successor navigation generated from authored semantics | Compatibility filename preserved until role transition |
| `docs/MAJOR_CHANGES.md` | Selective structural/evolution history | KEEP_BUT_REFINE_CONTRACT | `docs/` project-global selective-history singleton | Preserve reserved singleton |
| `docs/foundations/NNN_*.md` | Deep durable rationale that remains useful beyond one investigation | KEEP_BUT_REFINE_CONTRACT | `docs/foundations/` epistemic family | `NNN_lower_snake_case.md` |
| `docs/specifications/NNN_*.md` | Explicit scoped governed contracts | KEEP_BUT_REFINE_CONTRACT | `docs/specifications/` contract family | `NNN_lower_snake_case.md` |
| `docs/research/NNN_*.md` | Bounded investigation, comparison, experiment/design evidence | KEEP_BUT_REFINE_CONTRACT | `docs/research/` evidence/investigation family | `NNN_lower_snake_case.md` |
| `docs/checkpoints/NNN_*.md` | Meaningful historical project-state/evidence boundary | KEEP_BUT_REFINE_CONTRACT | `docs/checkpoints/` historical-continuity family | `NNN_lower_snake_case.md`; no checkpoint per commit |
| `docs/experiments/<program>/...` | Durable experiment-program interpretation/result docs | KEEP_BUT_REFINE_CONTRACT | `docs/experiments/<program>/` when the experiment program itself has durable multi-artifact identity | descriptive names inside program; executable bytes remain in repository `experiments/` |
| `docs/local_execution/*.md` | Current local-execution subsystem contracts/runbooks | KEEP_DOMAIN_HOME | `docs/local_execution/` natural subsystem home | descriptive filenames; standardized role names may remain uppercase |
| `docs/local_execution/validation/NNN_*.md` | Local-execution qualification evidence | KEEP_DOMAIN_LOCAL_EVIDENCE | under the subsystem it validates, not a new global validation dump | local sequence + descriptive slug |
| `docs/model_collaboration/` | Collaboration protocol and provenance | KEEP_DOMAIN_HOME | `docs/model_collaboration/` project-development subsystem home | stable role names + `MC-NNNN` thread identity |
| `docs/cockpit/` | Cockpit current control/provenance/navigation | KEEP_DOMAIN_HOME | `docs/cockpit/` natural product-domain home | descriptive current owners; specialized manifests/ledgers stay domain-local |
| `docs/source_universe/` | Source Universe current state/procedure/evidence | KEEP_DOMAIN_HOME | `docs/source_universe/` natural subsystem home | descriptive current owners; local evidence/manifests remain nested |
| `docs/methodological_knowledge/` | Methodological Knowledge Universe control/navigation | KEEP_DOMAIN_HOME | `docs/methodological_knowledge/` natural subsystem home | descriptive current owners |
| `docs/private_companion/` | Public contract for private continuity complement | KEEP_DOMAIN_HOME | `docs/private_companion/` boundary documentation only | descriptive/standard role names |
| `docs/project_knowledge/architecture/` | Architecture of the project-knowledge system itself | KEEP_NARROW_INFRASTRUCTURE_HOME | `docs/project_knowledge/architecture/` | descriptive architecture docs |
| `docs/project_knowledge/project_integration_boundary.md` and workstream owner | Genuine project-global project-knowledge control semantics | KEEP_NARROW_INFRASTRUCTURE_HOME | `docs/project_knowledge/` because responsibility is genuinely project-knowledge-global | descriptive canonical-owner filename |
| `docs/project_knowledge/captures/` | Non-authoritative intake / historical capture provenance | KEEP_CAPTURE_AREA | `docs/project_knowledge/captures/open|historical/` | descriptive slug or stable capture identity; no authority inferred from filename |
| `docs/project_knowledge/transitions/` | Exceptional identity transition/tombstone authority | KEEP_EXCEPTIONAL_AREA | only when transition itself needs authority | semantic/descriptive transition slug |
| `docs/project_knowledge/joint_authority/` | Rare qualified joint-authority semantics | KEEP_EXCEPTIONAL_AREA | only after joint-authority admission criteria | semantic/descriptive declaration slug |
| `docs/project_knowledge/generated/` | Deterministic derived indexes/orientation | KEEP_GENERATED_AREA | fixed successor-generated area | stable machine-facing lowercase names |
| Cockpit/Source-Universe manifests and ledgers | Domain-specific provenance/control projections | KEEP_DOMAIN_LOCAL | adjacent to domain owner rather than global registry | role-specific names; JSON + Markdown pairs only where both have distinct human/machine roles |
| `schemas/`, `tests/`, code and Git history | Executable contracts/mechanisms and exact implementation provenance | NOT_DOCUMENT_KNOWLEDGE_MIGRATION | remain in implementation tree | governed by implementation conventions, not docs IA |

## 4. Physical topology V0.1

The audit does not justify inserting a generic `docs/domains/` wrapper or moving all global singleton files into a new `docs/project/` folder.

The provisional target remains shallow:

```text
docs/
    README.md
    VISION.md
    PRINCIPLES.md
    DECISIONS.md
    OPEN_QUESTIONS.md
    OPEN_ARCHITECTURE_BACKLOG.md
    DEVELOPMENT_METHOD.md
    CONTINUITY.md
    MAJOR_CHANGES.md

    # compatibility surfaces during migration
    CURRENT_STATE.md
    current_routing.json
    KNOWLEDGE_MAP.md

    # epistemic / lifecycle families
    foundations/
    specifications/
    research/
    checkpoints/
    experiments/

    # natural semantic/subsystem homes
    cockpit/
    source_universe/
    methodological_knowledge/
    local_execution/
    model_collaboration/
    private_companion/

    # project-knowledge infrastructure only
    project_knowledge/
        architecture/
        generated/
        captures/
            open/
            historical/
        transitions/
        joint_authority/
        navigation/          # proposed W5 addition; navigation metadata only
```

A new top-level domain directory is justified when the thing has an independent durable responsibility/lifecycle and enough current knowledge to need a natural home. A one-off topic does not earn a directory merely because it appears in several documents.

## 5. Folder semantics

The physical tree has only one normative interpretation:

> A carrier lives where its **primary natural owner/responsibility** lives.

It does **not** answer every question about semantic subject.

Therefore:

```text
physical parent
    != exclusive semantic parent

folder path
    != authority

folder path
    != durable semantic identity

folder path
    != complete navigation
```

This allows, for example, a Source Universe procedure to remain physically under `docs/source_universe/` while appearing simultaneously in generated views for source management, data infrastructure, operational procedure, paused-workstream continuation and private-dependency boundaries.

## 6. Naming V0.1

### 6.1 Directories

New directories use:

```text
lowercase_snake_case
```

unless an external/tooling contract requires otherwise.

Avoid wrapper directories that add no semantic boundary.

### 6.2 Descriptive current canonical carriers

New ordinary descriptive files default to:

```text
lowercase_snake_case.md
lowercase_snake_case.json
```

Filename labels should remain human-readable and stable, but they do not mint semantic identity.

Established project-global singleton names such as `VISION.md`, `PRINCIPLES.md`, `DECISIONS.md`, `DEVELOPMENT_METHOD.md`, `CONTINUITY.md` and conventional role names such as `README.md`, `STATE.json`, `RESOLUTION.md` remain reserved exceptions. W5 does not justify mass cosmetic renaming merely to normalize case.

### 6.3 Numbered families

Use `NNN_lower_snake_case.md` only where ordered artifact identity materially helps the family:

```text
foundations
specifications
research
checkpoints
bounded domain validation series where local sequence is genuinely useful
```

Numbers remain artifact/provenance identifiers, not semantic identity.

### 6.4 Dates and semantic IDs

Dates belong in filenames only when time is part of the artifact-family identity, such as the governed historical-intermediate checkpoint form. Semantic IDs normally live in declarations/metadata rather than filenames.

## 7. Document-granularity rules V0.1

A new file is warranted when at least one of these is true:

```text
the responsibility has an independent lifecycle
several other sources must refer to it directly
it has a distinct authority scope
it needs independent provenance/revision control
keeping it inside the current owner would create ambiguous or conflicting ownership
its size/volatility would make the existing owner operationally overloaded
```

Prefer updating an existing natural canonical owner when:

```text
the new knowledge is simply a state change or refinement of the same responsibility
the same owner already governs the scope
a new file would create a second place to keep current truth synchronized
```

Do not create one file per claim, one directory per topic, or one semantic ID per paragraph.

## 8. Future authoring decision tree V0.1

When new durable material appears:

```text
1. Is this already within an existing canonical owner's responsibility?
       yes -> update that owner
       no  -> continue

2. Is it still unreviewed / conversation-born / candidate understanding?
       yes -> capture
              -> review
              -> promote/latent/reject
       no  -> continue

3. Is it a bounded investigation, comparison or design study?
       yes -> Research record
       no  -> continue

4. Is it an explicit scoped contract that execution must satisfy?
       yes -> Specification
       no  -> continue

5. Is it deep durable rationale that must remain reusable beyond one investigation?
       yes -> Foundation, used sparingly
       no  -> continue

6. Is it validation/qualification evidence for one subsystem?
       yes -> domain-local validation/evidence
       no  -> continue

7. Is it a governed experiment program/result with an independent durable identity?
       yes -> experiment program/result owner
       no  -> continue

8. Is it a meaningful project-state/evidence boundary?
       yes -> Checkpoint
       no  -> continue

9. Is it only orientation, routing, indexing or navigation?
       yes -> generated/derived view, not unique truth
       no  -> identify/create the narrowest natural canonical owner
```

Cross-project decisions/questions remain in the project-global singleton surfaces. Domain-local decisions/questions should not be promoted into global files merely because they are important locally.

## 9. Multi-axis navigation V0.1

### 9.1 Separate semantic subjects from other facets

The generated navigation system should expose several axes without pretending all are "subjects":

```text
semantic subject
physical domain / natural owner
artifact family / representation
authority state
lifecycle state
workstream / dependency
provenance / evidence depth
temporal status
privacy / access
reconstruction/task relevance
```

Kind/profile/scope already provide several derived axes. W5 should not duplicate them manually as subject tags.

### 9.2 Proposed authored navigation block

For future governed canonical sources that need explicit semantic-subject placement, V0.1 proposes a small optional navigation block conceptually equivalent to:

```json
{
  "navigation": {
    "subjects": [
      "project-knowledge-architecture",
      "repository-governance"
    ],
    "preferred_subject": "project-knowledge-architecture"
  }
}
```

This metadata is for navigation. It does not alter authority, scope or semantic identity.

Whether this block is embedded in each profile or normalized through a shared schema definition remains an implementation question for the next W5 design step.

### 9.3 Subject catalog / graph

V0.1 proposes a narrow authored navigation source under:

```text
docs/project_knowledge/navigation/subject_catalog.json
```

Its role is to define durable navigation subjects only where a stable subject concept is useful.

A subject entry may contain:

```text
subject ID
human label
optional description
zero or more broader parents
optional preferred parent for default display
aliases when needed
lifecycle/status when materially useful
```

Multiple `broader` parents permit polyhierarchy. `preferred_parent` controls one deterministic display route without asserting exclusive semantic parentage.

The subject catalog is **navigation authority**, not substantive project-content authority. It may say that "GitHub integration" is under both "repository infrastructure" and "external integrations"; it does not own the facts about GitHub integration.

### 9.4 View-only groupings

A generated grouping does not receive a durable subject ID merely because it is convenient in a UI or report.

Examples likely to remain view-only:

```text
all active workstreams
all current specifications
all private-dependent procedures
all evidence deeper than level X
all artifacts changed this month
all items relevant to one reconstruction task
```

This preserves the anti-ontology-sprawl requirement.

## 10. Legacy/historical subject membership

W5 should **not** add navigation declarations to hundreds of historical Research/Checkpoint/Foundation records solely for new-system coverage.

During migration:

```text
current governed sources
    -> explicit future navigation metadata where useful

legacy numbered/history families
    -> existing Knowledge Map + deterministic migration adapter/inventory
       -> successor generated subject view

later natural edits to a historical artifact
    -> do not opportunistically retrofit semantics unless a current need requires it
```

This lets the successor navigation system cover history without mass rewriting history.

## 11. Domain creation and nested structure rules

A new `docs/<domain>/` home is warranted when several of these hold:

```text
the domain owns current durable knowledge
it has an independent lifecycle/workstream
it has multiple related current/evidence artifacts
it has specialized procedures or manifests
it would otherwise overload project-global files
other domains need to refer to it as a coherent responsibility
```

Inside a domain, add nested directories only for a real repeated family or lifecycle boundary, for example:

```text
validation/
manifests/
intake_snapshots/
threads/
captures/
historical/
```

Do not nest merely to mirror a conceptual taxonomy that is better represented by multi-axis navigation.

## 12. What this proposal deliberately keeps

V0.1 preserves several existing structures because they are semantically justified, not merely because they already exist:

```text
small docs-root global singleton set
numbered Foundation/Specification/Research/Checkpoint families
domain-local Source Universe/Cockpit/local-execution/model-collaboration knowledge
narrow docs/project_knowledge infrastructure home
domain-local validation and provenance when it belongs to one subsystem
Git/code/tests as implementation provenance rather than duplicated documentation
```

## 13. What this proposal deliberately changes

The main changes are prospective role changes rather than cosmetic tree churn:

```text
CURRENT_STATE -> successor-generated current orientation after cutover
current_routing -> successor-generated route after cutover
KNOWLEDGE_MAP -> successor-generated multi-axis navigation after cutover

current durable knowledge should migrate out of historical/evidence-only carriers
when those carriers are still serving as accidental current owners

new semantic-subject authoring becomes explicit and multi-parent capable
rather than relying on one flat manually maintained Knowledge Map

future creation/update decisions follow one authoring decision tree

folder location is formally limited to primary natural ownership
rather than overloaded as semantic classification
```

## 14. Adversarial questions before freezing

V0.1 remains provisional until it survives at least these challenges:

```text
Q1  Does keeping global singleton files at docs/ retain too much legacy structure?
Q2  Do numbered Research/Foundation/Specification families still scale once they are no longer active truth?
Q3  Is one authored subject catalog a healthy navigation contract or a disguised central ontology/registry?
Q4  Should subject membership be embedded in canonical declarations or stored separately?
Q5  Can domain-local sources express cross-domain subjects without awkward duplication?
Q6  Is preferred_subject sufficient for deterministic default navigation?
Q7  How are aliases, subject renames and subject merges handled without turning every navigation edit into identity machinery?
Q8  How does the model handle identity-free canonical sources that still need subject membership?
Q9  Can existing Knowledge Map coverage be deterministically migrated without touching historical artifacts?
Q10 Does the proposed naming policy create unnecessary rename pressure on current canonical sources?
Q11 Are local validation series truly domain-local evidence, or do some deserve a cross-project qualification family?
Q12 Does the authoring decision tree distinguish experiments, research and validation clearly enough in real ambiguous cases?
```

## 15. Provisional conclusion

The first real-corpus pass supports a **hybrid physical architecture plus generated multi-axis semantic organization**, not a wholesale move into one new tree.

```text
PHYSICAL_TARGET_V01=PROPOSED
GLOBAL_SINGLETONS=KEEP_NARROW_SET
EPISTEMIC_FAMILIES=KEEP_WITH_REFINED_CONTRACTS
DOMAIN_HOMES=KEEP_AND_USE_FOR_CURRENT_NATURAL_OWNERS
PROJECT_KNOWLEDGE_DIRECTORY=KEEP_NARROW_INFRASTRUCTURE_ONLY
GENERIC_DOMAINS_WRAPPER=NOT_JUSTIFIED
MASS_HISTORICAL_REWRITE=REJECTED
MULTI_AXIS_NAVIGATION=REQUIRED
SUBJECT_POLYHIERARCHY=PROPOSED
PREFERRED_ROUTE_WITHOUT_EXCLUSIVE_PARENT=PROPOSED
FUTURE_AUTHORING_DECISION_TREE=PROPOSED
W5_BROAD_SEMANTIC_MIGRATION=NOT_STARTED
NEXT=INDEPENDENT_ADVERSARIAL_REVIEW_AND_SCHEMA/VIEW_REALIZATION_DECISION
```
