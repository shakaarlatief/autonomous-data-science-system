# Research 177: Selected Candidate 01 Physical Architecture and Repository Contract V0.1

**Date:** 2026-09-15
**Status:** PHYSICAL ARCHITECTURE V0.1 ACCEPTED INTO SPECIFICATION 028 / REFINED BY RESEARCH 179 / W0 SUBSTRATE SLICE 1 ACCEPTED / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Selection decision:** `D-035`
**Scope:** Convert the selected logical architecture into a concrete repository/software architecture suitable for production implementation and staged migration, while preserving the distinction between ADS product runtime architecture and ADS project-development knowledge infrastructure.
**Authority:** Implementation-design research only. D-035 owns target selection. Existing continuity remains operational authority until a later explicit cutover.
**Declared references:** `path:docs/DECISIONS.md`, `research:144`, `research:145`, `research:175`, `research:176`, `checkpoint:521`, `path:pyproject.toml`

## 1. Design objective

The physical design must realize Candidate 01 without accidentally turning the project-development knowledge architecture into either:

```text
1. another giant hand-maintained global summary system;
2. a central database that becomes a second project authority;
3. a universal object graph that reopens H3 by implementation drift;
4. product-runtime code coupled to development-continuity infrastructure;
5. research-prototype scripts promoted wholesale without production boundaries.
```

The architecture should remain repository-native, inspectable, deterministic where authority depends on it, and usable by humans and capable AI tools without requiring one provider-specific runtime.

## 2. Physical boundary: separate project-development tooling from ADS product runtime

The selected project-knowledge implementation should **not** be placed inside `src/ads_system/` as though it were an ADS product-domain subsystem.

The proposed production boundary is:

```text
tools/project_knowledge/
    repository-local implementation package
    parsers / models / validators / generators
    identity / authority / workstream / reconstruction logic
    capture / promotion / migration support
    CLI entrypoint via python -m tools.project_knowledge

schemas/project_knowledge/
    versioned profile-specific JSON Schemas

docs/project_knowledge/
    human architecture documentation
    generated derived structural views / manifests
    bounded capture/transition/joint-authority exceptional artifacts
```

Rationale:

- project-development knowledge is infrastructure **around development of ADS**, not the ADS product itself;
- a repo-local `tools/` package is still version-controlled, testable and portable without contaminating product package boundaries;
- it avoids adding a second published distribution merely to run repository governance;
- it can use the repository's managed Python environment and existing `jsonschema` dependency;
- later extraction into a standalone package remains possible if another project needs the same tooling.

Research-only scripts under `scripts/research/` remain evidence/reference code and are not the production namespace.

## 3. Canonical knowledge remains where it naturally belongs

Candidate 01 does **not** introduce a new central `project_knowledge/data/` directory containing copies of all authoritative facts.

Existing and future canonical sources remain in natural project locations, for example:

```text
docs/DECISIONS.md
numbered research/specification/foundation records
active workstream/domain sources
governing procedure files
domain README/control sources where they naturally own state
public-safe evidence records
```

Only semantic units that genuinely need their own natural global home should live beneath `docs/project_knowledge/`, such as:

```text
PROJECT_INTEGRATION_BOUNDARY.md
identity transition / tombstone records when the transition itself is authoritative
exceptional joint-authority declarations
capture queue records before promotion
selected architecture documentation
```

This preserves source-local ownership rather than moving knowledge into a new registry merely because tooling exists.

## 4. Structured declaration encoding

### 4.1 Markdown carrier

For Markdown canonical sources participating in machine-resolved semantics, V0.1 should promote the declaration mechanism already exercised throughout Candidate 01 qualification:

```text
<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{ ... canonical JSON object ... }
<!-- PKA-STRUCTURED-DECLARATION-END -->
```

The declaration has an explicit schema/profile version and is valid strict JSON.

Reasons to prefer this over YAML/front matter for V0.1:

```text
existing qualified prototype evidence already uses it
JSON parsing is deterministic and already supported
no implicit scalar typing or YAML parser dependency
rich Markdown remains readable without making metadata the document body
machine semantics stay physically adjacent to the rich canonical source
Git diffs remain straightforward
```

The exact markers become part of Specification 028 and must not be interpreted as generic HTML metadata outside that contract.

### 4.2 Native JSON carrier

A canonical source already represented as JSON may carry equivalent profile fields directly when doing so does not violate an existing fixed schema/compatibility contract.

If an existing JSON file has a frozen compatibility schema that cannot accept Candidate 01 fields, its semantic owner remains elsewhere and the JSON file stays derived/compatibility-only rather than receiving an authoritative sidecar copy.

## 5. Profile-specific schemas, not one universal ontology

`schemas/project_knowledge/` should contain a small family of versioned schemas sharing a minimal envelope but validating only fields relevant to each responsibility.

Initial profiles:

```text
semantic_source.v1
    accepted decision / synthesis / ordinary durable knowledge unit

workstream.v1
    durable workstream identity, state, dependencies, pause/return/resume, execution anchor

governing_procedure.v1
    applicability + action contract + constraint identities

project_boundary.v1
    narrow project-global integration facts with a natural global owner

identity_transition.v1
    move/replacement/merge/split/retirement/tombstone when transition semantics need authority

joint_authority.v1
    rare J1-J6-qualified governing-set combination semantics

capture.v1
    non-authoritative intake / candidate provenance

derived_view_manifest.v1
    source bindings, generator identity, freshness and rebuildability
```

Profiles may share reusable `$defs`, but irrelevant fields are not required on every source.

## 6. Normative responsibility inside one source

The physical contract must prevent prose and structured declarations from becoming two competing authorities.

For a governed source:

```text
rich prose
    owns explanation, rationale, context and human-readable meaning

structured declaration
    is the sole normative representation for the machine-resolved control facts
    explicitly covered by that declaration/profile

validator
    detects material prose/declaration drift where governed concepts overlap
    but never silently rewrites either side
```

For governing procedures, structured constraint IDs/order/preconditions/prohibitions are the normative machine contract. Prose remains essential explanatory authority, but contradictory machine-checkable procedure semantics are a validation failure rather than an invitation for an LLM to choose between copies.

## 7. Repository-local implementation package

Proposed module decomposition:

```text
tools/project_knowledge/
    __init__.py
    __main__.py

    model.py
        immutable typed internal records
        SourceRevision / SemanticId / Relation / Scope / Receipt

    declaration.py
        marker extraction
        JSON parsing
        profile dispatch
        schema validation

    references.py
        typed repository references
        semantic-ID -> carrier resolution
        exact Git-blob revision descriptors

    identity.py
        durable identity index
        transition/tombstone closure
        bounded current-target lookup

    authority.py
        applicability / scope matching
        REPLACE/SUPPLEMENT/SPECIALIZE/CORRECT closure
        JOINT_AUTHORITY combination
        fail-visible missing/conflicting result states
        authority receipt construction

    workstreams.py
        DAG validation
        active/paused/blocked/completed semantics
        dependencies and route projection
        pause/return/resume validation
        interruption recovery support

    views.py
        deterministic structural derived views
        current-state core
        subject/navigation index
        identity/authority/workstream indexes
        compatibility projections

    reconstruction.py
        broad vs narrow task contracts
        must-load / optional / negative-context planning
        reconstruction receipts

    capture.py
        capture validation
        review/promotion records
        no-authority-before-promotion enforcement

    migration.py
        semantic migration units
        parity / reverse-reference checks
        rollback-compatible exports

    validation.py
        local + impact-aware + freshness + non-leakage validation

    git.py
        bounded Git object/blob helpers
        revision/content-digest abstraction

    cli.py
        stable repository command surface
```

This decomposition expresses logical responsibilities, not service boundaries. Modules may be merged if implementation evidence shows the split creates unnecessary ceremony.

## 8. Revision identity

Research 168 and Research 173 exposed the danger of a bare `sha256` without a representation basis.

Production revision descriptors therefore use an explicit shape equivalent to:

```json
{
  "source_path": "docs/example.md",
  "source_commit": "<40-char commit when immutable commit binding is required>",
  "hash_algorithm": "sha256",
  "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
  "content_digest": "..."
}
```

For generated views committed in the **same commit** as changed canonical inputs, a self-referential source commit cannot be required. Their manifests therefore bind the exact **set of input paths + canonical Git-blob/content digests** plus generator identity/version. Freshness is verified from those input descriptors rather than a whole-commit hash.

External attachments additionally record materialization identity separately when checkout bytes may differ from canonical Git-blob bytes.

## 9. Generated structural view architecture

The production system should generate a small set of deterministic inspectable views under:

```text
docs/project_knowledge/generated/
```

Initial generated artifacts:

```text
source_catalog.json
    all governed current semantic sources and profiles

identity_index.json
    semantic ID -> current carrier + transition closure

authority_index.json
    current authority candidates / scoped relation closure inputs

workstream_graph.json
    workstream nodes / dependencies / active route projection

subject_index.json
    multi-axis subject/navigation membership

risk_obligation_index.json
    known risks, reopen triggers and active obligations that sources expose

current_state_core.json
    compact machine current orientation

CURRENT_STATE_CORE.md
    compact human current orientation
```

Every persistent generated artifact has a deterministic derived-view manifest. Manifests may be stored adjacent or in `docs/project_knowledge/generated/manifests/` depending on file-format constraints.

Generated artifacts contain no unique accepted truth.

## 10. Compatibility surfaces during migration

The current globally referenced paths remain intact until cutover and stabilization:

```text
docs/CONTINUITY.md
    remains authored bootstrap/constitutional procedure
    is progressively reduced only after successor views are proven

docs/current_routing.json
    keeps its exact compatibility schema
    becomes generated from successor semantic owners only at a separately qualified migration wave

docs/CURRENT_STATE.md
    remains current operational owner until cutover
    successor-generated replacement is shadow-compared first

docs/KNOWLEDGE_MAP.md
    remains current navigation compatibility surface
    generated replacement is shadow-compared before role transition
```

Because fixed compatibility schemas cannot always carry derived-view metadata, their Candidate 01 source/freshness manifests live under the generated manifest area rather than altering the compatibility payload.

## 11. Full rebuild versus incremental refresh

Two generation modes are required:

```text
FULL REBUILD
    scan governed current repository sources
    parse declarations
    rebuild all structural derived views
    used for CI/milestone verification and recovery

INCREMENTAL REFRESH
    use changed source paths plus dependency graph
    regenerate only affected derived neighborhoods
    used for ordinary local maintenance
```

Required reconstruction never depends on rescanning full Git history. Historical Git traversal is used only when the queried semantic transition/provenance actually requires it.

## 12. Discovery and retrieval

V0.1 production cutover does not require a vector database or project-knowledge database.

The access stack begins with:

```text
semantic ID lookup
structured indexes
exact repository paths/references
lexical Git/repository search
```

Optional local semantic/vector or SQLite/FTS discovery may be added later as a **derived rebuildable cache** behind an adapter. It cannot become authority and is not required for safe governing-source resolution.

This preserves provider/tool portability and avoids coupling cutover to retrieval infrastructure that qualification did not require.

## 13. Authority resolver contract

The resolver receives an explicit task/action query:

```text
action / requested operation
target / scope
current workstream/environment
actor/role when material
consequence class
time when material
```

It returns one of:

```text
RESOLVED
UNRESOLVED_SCOPE_REQUIRED
UNRESOLVED_AUTHORITY_CONFLICT
MISSING_REQUIRED_AUTHORITY
STALE_REQUIRED_AUTHORITY
REQUIRED_PRIVATE_STATE_UNAVAILABLE
```

A successful receipt records exact source IDs, carrier paths, source revisions, why each source applies, combination/supersession semantics, activated action constraints and freshness status.

Probabilistic retrieval output may be cited as candidate-discovery evidence but cannot set the resolver disposition.

## 14. Reconstruction planner contract

The planner produces a task-shaped reconstruction contract rather than a universal bootstrap bundle.

### Broad continuation

```text
small authored bootstrap
-> current-state core / route
-> active workstream source(s)
-> current risks / obligations
-> domain depth on demand
```

### Narrow consequential task

```text
bootstrap rule
-> classify action/scope
-> authority resolver
-> exact governing sources + action contract
-> minimum supporting evidence
-> conformance / fail-visible gate
```

### Exploratory research

```text
structured/lexical/optional semantic discovery
-> evidence drill-down
-> explicit source roles
-> uncertainty retained
```

The planner records both positive context and negative/do-not-load guidance when that materially protects bounded context.

## 15. Capture and promotion storage

Low-friction captures are non-authoritative repository artifacts under a bounded area such as:

```text
docs/project_knowledge/captures/open/
```

One capture per file is preferred to a monolithic mutable queue because it gives independent identity, provenance and merge behavior.

Promotion does **not** convert the capture itself into authority. An accepted promotion updates/creates the natural canonical semantic source and records the capture provenance. The capture may then become historical/archived once provenance sufficiency is verified.

## 16. Exceptional semantic sources

Two exceptional families may need a project-level home:

```text
docs/project_knowledge/transitions/
    identity transition/tombstone records only when transition semantics require their own authority

docs/project_knowledge/joint_authority/
    J1-J6-qualified governing-set declarations only
```

Their growth is a monitored complexity signal. If these areas begin behaving like a universal object registry, the selected architecture's H3 reopening condition is reconsidered explicitly.

## 17. Professional architecture documentation and visualization

The selected architecture should receive a dedicated durable documentation set under:

```text
docs/project_knowledge/architecture/
```

Planned documents:

```text
README.md
    architecture overview and navigation

whole_architecture.md
    polished full-system overview

semantic_authority_model.md
    source ownership, identity, authority, relations, time

knowledge_lifecycle.md
    capture -> review -> promotion -> derived consumption

reconstruction_and_action.md
    fresh collaborator -> task-shaped reconstruction -> authority -> safe action

migration_and_cutover.md
    legacy authority -> shadow successor -> parity -> cutover -> rollback
```

Each should include a version-controlled diagram. The whole-architecture diagram is the primary professional overview; focused diagrams carry detail that would make one mega-diagram unreadable.

Where practical, keep a text/source representation that can be deterministically regenerated into a polished visual artifact. A rendered SVG/PNG may also be committed for easy viewing once the diagram source is stable.

## 18. CLI and developer workflow

The stable command surface should converge toward:

```text
python -m tools.project_knowledge validate
python -m tools.project_knowledge rebuild
python -m tools.project_knowledge refresh --changed-since <ref>
python -m tools.project_knowledge check-freshness
python -m tools.project_knowledge resolve-authority <task-spec>
python -m tools.project_knowledge reconstruct <task-spec>
python -m tools.project_knowledge migration-audit
```

CI checks validation and regeneration parity but does not automatically commit generated changes or promote captures.

## 19. Migration strategy after selection

The selected architecture should now move through production waves:

```text
W0 implementation substrate
    tools package + schemas + tests + generated-area contract

W1 live control semantics
    selected architecture workstream
    Project Integration Boundary
    Source Vault workstream
    Cockpit paused workstream
    D-035 / current high-consequence governing sources

W2 shadow derived views
    identity / authority / workstream / subject / current-core views

W3 compatibility shadow
    generate routing/current-state/Knowledge Map candidates without overwriting live paths

W4 capture/promotion production path
    one real bounded capture -> review -> canonical promotion

W5 broader current semantic migration
    migrate by responsibility/domain, not chronology

W6 cutover candidate
    successor-generated compatibility surfaces + cold continuation / authority tests

W7 cutover qualification
    actual migrated production state against Requirements V0.2

W8 explicit authority switch
    separate decision only after W7 passes
```

History is not mass-converted merely to increase structured coverage. Legacy deep history remains discoverable evidence unless a current semantic need justifies explicit migration.

## 20. Reuse disposition for research implementations

The existing shadow code provides qualified mechanism evidence, but most scripts are monolithic fixture-specific programs. The default disposition is therefore:

```text
semantic algorithms / tested cases      REFINE_AND_PROMOTE
fixture/oracle loaders                  KEEP_AS_TEST_OR_REFERENCE_ONLY
research-specific path/hash constants   RETIRE_AFTER_PRODUCTION_EQUIVALENT
monolithic run_probe orchestration      REIMPLEMENT_BEHIND_PRODUCTION_MODULES
Q10 qualification implementation        KEEP_AS FINAL EVIDENCE / REGRESSION INPUT
```

Specific reusable algorithms include workstream DAG logic, expected-revision stale-write semantics, authority conflict/supersession handling, declaration parsing, derived-view generation patterns, migration parity checks and source-revision diagnostics.

## 21. Physical architecture V0.1 disposition

This proposal preserves the selected Candidate 01 logical architecture while making concrete choices that are deliberately reversible where they are not logically essential.

```text
PROJECT_SUPPORT_CODE=tools/project_knowledge
PRODUCT_RUNTIME_COUPLING=NO
CANONICAL_KNOWLEDGE=CURRENT_NATURAL_REPOSITORY_SOURCES
STRUCTURED_DECLARATION=EMBEDDED_STRICT_JSON_FOR_MARKDOWN
PROFILE_SCHEMAS=schemas/project_knowledge
PERSISTENT_DERIVED_VIEWS=docs/project_knowledge/generated
PROFESSIONAL_ARCHITECTURE_DOCS=docs/project_knowledge/architecture
CENTRAL_AUTHORITY_DATABASE=NO
VECTOR_DATABASE_REQUIRED=NO
CURRENT_CONTINUITY_AUTHORITY=UNCHANGED
NEXT=SPECIFICATION_028_PHYSICAL_IMPLEMENTATION_AND_MIGRATION_CONTRACT
```

## 22. Specification 028 freezes the production contract

Specification 028 adopts this V0.1 physical architecture into a prospective production/migration contract. It fixes the project-support package boundary, profile/schema family, embedded strict-JSON declaration format, derived-view and manifest contracts, resolver/reconstruction/capture responsibilities, compatibility migration waves, professional architecture-documentation requirement, and W0/W1 executable gates.

The immediate next stage is W0 implementation substrate. No current authority surface is migrated or overwritten merely because the specification is frozen.
