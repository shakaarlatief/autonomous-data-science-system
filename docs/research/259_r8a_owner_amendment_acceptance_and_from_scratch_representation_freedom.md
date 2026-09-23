# Research 259: R8-A Owner Amendment Acceptance and From-Scratch Representation Freedom

**Date:** 2026-09-23
**Status:** R8-A ACCEPTED AS AMENDED / MC-0025 RESOLVED / REPRESENTATION-CONTENT DESIGN UNBLOCKED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Original R8-A recommendation:** Research 257
**Adversarial review:** MC-0025 Message 001
**Reconciliation:** Research 258 / MC-0025 Message 002
**Owner decision:** AMEND
**Repository base before acceptance:** 7e9dafd675611632769a482cffca69661567a00e
**Scope:** Record the owner's explicit R8-A amendment acceptance and freeze an additional design principle: the next representation/content architecture is from-scratch and is not required to preserve current file-internal formats, metadata structures, document templates or serialization conventions merely because they exist today.

## 1. Owner decision

The project owner explicitly chose:

    I AMEND.

This accepts Research 257's exact-target architecture family as amended by Research 258.

The accepted target therefore includes:

    Product / Project Level-1 split
    independent Product and Project Python dependency resolution
    Product runtime and interaction workspaces
    Project system / engineering / research / reproductions / knowledge areas
    JW1 as the Project Development System
    PSMF framework-versus-instance seam
    permanent transition-management responsibility
    generate-independent cold start
    PC7 internal seams
    JW1 semantic-validation versus repository-engineering validation boundary
    research terminal-disposition discipline
    reproduction admission gate
    continuity/recovery/collaboration discriminator
    operations/engineering six-subarea model and review bound 8
    AO-3 through AO-9 semantics retained

No physical migration is authorized by this acceptance.

## 2. Additional owner clarification: representation and file internals are also redesignable from scratch

Before proceeding, the owner explicitly clarified that the same from-scratch mentality used for repository and information architecture applies **inside the future carriers themselves**.

The current repository may contain files with structures such as:

    Markdown headings
    metadata headers
    front matter
    embedded strict JSON declarations
    source-local declaration blocks
    thread/message metadata
    checkpoint metadata
    research-document headers
    status fields
    authority fields
    relationship fields
    identifiers
    timestamps
    provenance fields
    schema-version fields
    document templates
    generated JSON shapes
    file naming conventions

None of those structures becomes a future target requirement merely because it appears in a current accepted or recently authored file.

For example, the metadata currently present in:

    docs/model_collaboration/threads/MC-0025/messages/
        002_chatgpt_r8a_adversarial_reconciliation_and_amendment_candidate.md

is **current-era evidence and current operational structure**, not a template the future architecture must preserve.

The same applies to every other current carrier.

## 3. From-scratch representation principle

The next architecture stage must ask first:

> What information, identity, authority, provenance, lifecycle, relationship, reconstruction and machine-operability semantics does the future system actually need?

Only after that should it ask:

> What carrier model, serialization, metadata model, schema, database, graph, document structure or hybrid representation best realizes those needs?

The decision order is therefore:

    semantic responsibility / required behavior
        ->
    information objects and lifecycle
        ->
    authority / identity / provenance / relation requirements
        ->
    human and machine access requirements
        ->
    representation alternatives
        ->
    selected representation
        ->
    metadata/schema design
        ->
    exact carrier/document/database realization

NOT:

    inspect current Markdown/JSON metadata
        ->
    preserve its shape
        ->
    reorganize it under new folders

## 4. Current artifacts are evidence, not preservation requirements

Current files may still be valuable for at least four reasons:

    CONTENT EVIDENCE
        they contain durable information that may need to survive

    BEHAVIORAL EVIDENCE
        they show which contracts have been useful or qualified

    MIGRATION EVIDENCE
        they expose references, path dependencies and operational assumptions

    NEGATIVE EVIDENCE
        they expose awkwardness, duplication, accidental coupling or
        representation choices that should not survive

But current artifacts do not receive target status by default.

For every current structural convention, the future architecture may:

    KEEP
    CLARIFY
    AMEND
    SUPERSEDE
    REPLACE
    SPLIT
    MERGE
    ELIMINATE

provided the change is governed and any currently accepted authority/behavior is handled explicitly rather than silently broken.

## 5. No hidden grandfathering of current metadata

The following are specifically **not grandfathered** into the future architecture:

    one fixed Markdown metadata header
    one fixed front-matter convention
    one declaration block per carrier
    embedded JSON as the only machine-readable structure
    JSON Schema as the only schema mechanism
    current checkpoint metadata fields
    current research-document metadata fields
    current model-collaboration message metadata
    current THREAD / STATE / RESOLUTION file pattern
    current numbered Research / Checkpoint document families
    current generated-view JSON schemas
    current status vocabulary
    current relationship-field vocabulary
    current naming conventions

Some of these may survive after evaluation.

Their current existence is not sufficient reason.

## 6. Relationship to accepted semantic contracts

This clarification does **not** silently erase previously accepted behavior.

For example, current evidence-backed principles such as:

    path != identity
    path != authority
    generated views contain no unique accepted truth
    capture != promotion
    declaration instances are carrier-resident under the current contract
    selective first-class identity
    controlled semantic subjects
    governed architecture evolution

remain current design inputs and current authority where applicable.

However, even these are not metaphysically immutable.

If the from-scratch representation design produces evidence that a retained contract itself is suboptimal or internally inconsistent with the accepted higher-level architecture, the project may reopen it through AO-4:

    evidence / trigger
        ->
    accepted contract identified
        ->
    KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN
        ->
    explicit owner decision where material
        ->
    prospective realization

Therefore:

    CURRENTLY ACCEPTED
        !=
    FOREVER UNCHANGEABLE

and:

    CURRENT FILE SHAPE
        !=
    ACCEPTED SEMANTIC CONTRACT

These distinctions are mandatory in the next stage.

## 7. Specification 028 implication

Specification 028 remains the current governing implementation/migration authority until explicitly amended.

That does **not** mean its current representation choices are target constraints.

The next representation stage must treat all representation-sensitive clauses in Specification 028 as candidates for deliberate review, including:

    Markdown declaration participation
    strict embedded JSON declaration blocks
    native JSON carrier rules
    JSON Schema contracts
    one declaration per carrier
    generated JSON view paths/shapes
    current project-knowledge directory assumptions
    no-database constraints stated for V1 safe operation
    parser and validation assumptions
    source catalog / identity / authority / graph/index representations

The possible outcomes per clause are:

    RETAIN
    GENERALIZE
    AMEND
    SUPERSEDE

No clause is changed until the review is completed and the amendment is explicitly accepted.

## 8. Representation-stage design freedom

The next stage is free to evaluate, without preference-by-inheritance:

    Markdown
    structured Markdown
    JSON
    YAML
    TOML
    relational storage
    SQLite
    graph representations
    graph databases
    event/log representations
    object stores
    generated indexes
    generated graph projections
    vector/search indexes
    source-local metadata
    central bounded registries
    hybrid architectures
    other justified mechanisms

This is not permission to use technology arbitrarily.

Every representation must be justified by:

    authority semantics
    lifecycle
    update locality
    human inspectability
    machine determinism
    reconstruction
    provenance
    migration safety
    failure/recovery behavior
    versioning/evolution
    validation
    performance where relevant
    PSMF upgradeability
    Product/Project separation
    operational complexity

## 9. Bounded exception already accepted at R8-A

One narrow representation decision remains intentionally selected:

    project_anchor.json

The root anchor is a small machine-readable locator contract and JSON is currently accepted for that bounded purpose.

Even this may be revisited by AO-4 if later evidence shows the choice conflicts with recovery or host/tool constraints.

Its existence must not bias the rest of the representation architecture toward JSON.

## 10. Next-stage method

The next stage must not begin by mapping current files to formats.

It should derive a representation model from first principles.

Recommended sequence:

    A. enumerate future information/control classes
    B. derive per-class authority and lifecycle
    C. derive identity / relation / provenance requirements
    D. derive human-read / machine-read / write-pattern requirements
    E. classify source-of-truth versus derived/cache material
    F. compare representation families
    G. select representation per class or class family
    H. design metadata/schema only after representation selection
    I. map retained current semantics into the new model
    J. produce Specification 028 delta
    K. only then build file-level migration disposition

The stage must explicitly detect when an existing metadata field, heading convention or document family is being retained merely through familiarity.

## 11. Accepted R8-A target

The accepted high-level target remains:

    ROOT
        .github/
        .gitignore
        README.md
        project_anchor.json
        pyproject.toml
        product/
        project/

    product/
        runtime/
        interaction/
            web/

    project/
        system/
        engineering/
        research/
        reproductions/
        knowledge/
            governance/
            evidence/
            operations/
            history/

Exact internal representation beneath these responsibility boundaries remains open except where explicitly accepted.

## 12. Still held

    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false
    W5_F0=PAUSED
    AO10=HELD
    PSMF_EXTRACTION=NOT_AUTHORIZED
    SPECIFICATION028=UNCHANGED

The next stage designs the representation/content architecture. It does not move the repository.

## 13. Current state

    R8A=ACCEPTED_AS_AMENDED
    RESEARCH257=HISTORICAL_BASE_RECOMMENDATION
    RESEARCH258=ACCEPTED_AMENDMENT
    OWNER_REPRESENTATION_FREEDOM_CLARIFICATION=ACCEPTED
    MC0025=RESOLVED

    CURRENT_FILE_INTERNALS=EVIDENCE_NOT_TARGET_REQUIREMENTS
    CURRENT_METADATA_SHAPES=NOT_GRANDFATHERED
    CURRENT_DOCUMENT_TEMPLATES=NOT_GRANDFATHERED
    CURRENT_SERIALIZATION_CHOICES=REVIEWABLE
    CURRENT_SEMANTIC_CONTRACTS=RETAIN_UNTIL_EXPLICITLY_AMENDED
    AO4_REOPEN_PATH=AVAILABLE

    REPRESENTATION_CONTENT_ARCHITECTURE=UNBLOCKED
    SPECIFICATION028=UNCHANGED_PENDING_REPRESENTATION_REVIEW
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R8_REPRESENTATION_AND_CONTENT_ARCHITECTURE_FROM_SCRATCH
