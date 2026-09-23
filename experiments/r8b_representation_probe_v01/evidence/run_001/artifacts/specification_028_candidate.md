# Specification 028 — V1 Project-Knowledge Architecture Implementation and Migration Contract

```toml project-meta
contract = "project-knowledge-carrier/1"
id = "SPECIFICATION:028"
kind = "specification"
authority = "canonical"
lifecycle = "active"
subjects = ["project-knowledge-architecture"]

[[relations]]
type = "implements"
target = "D-035"
```

## 1. Purpose and frozen boundary

D-035 selects Candidate 01 as the successor project-development knowledge architecture. Research 175 qualifies the logical architecture 67/67. Research 177 proposes its physical realization.

This specification freezes the first production implementation and migration contract.

It MUST preserve this distinction:

```text
selected logical architecture
    -> frozen by D-035 / Research 144 / Requirements V0.2

physical implementation contract
    -> frozen by Specification 028

current operational authority
    -> existing continuity architecture until explicit later switch
```

The implementation MUST NOT treat this specification as authorization to replace `CURRENT_STATE.md`, `current_routing.json`, `CONTINUITY.md`, `KNOWLEDGE_MAP.md`, or any other current authority surface before the migration/cutover gates defined here are satisfied.

## 2. Product/runtime separation

The project-knowledge implementation is development-support infrastructure around ADS, not an ADS product-domain subsystem.

Production implementation MUST live under:

```text
tools/project_knowledge/
```

and MUST NOT be introduced under:

```text
src/ads_system/
```

unless a later explicit architectural decision changes this boundary.

The implementation MAY use dependencies already governed by the repository's Python environment. It MUST NOT require packaging the project-knowledge tooling as a separately published distribution for V1.

Research-only scripts in `scripts/research/` remain evidence/reference implementations. Production behavior MUST be implemented behind the `tools/project_knowledge/` boundary rather than importing fixture/oracle-specific research orchestration as runtime authority.

## 3. Required production package surface

The initial package MUST expose responsibilities equivalent to:

```text
tools/project_knowledge/
    __init__.py
    __main__.py
    model.py
    declaration.py
    references.py
    identity.py
    authority.py
    workstreams.py
    views.py
    reconstruction.py
    capture.py
    migration.py
    validation.py
    git.py
    cli.py
```

Exact internal helper decomposition MAY differ when implementation evidence supports a cleaner design, but these logical responsibility boundaries MUST remain explicit and testable.

The package MUST NOT persist unique accepted project truth in Python constants or module-local registries.

## 4. Canonical source-location rule

Accepted project knowledge remains in its natural repository owner by default.

Examples include:

```text
docs/DECISIONS.md
numbered research/specification/foundation records
active domain/workstream sources
governing procedures
evidence/validation records
domain control documents that naturally own their state
```

The implementation MUST NOT create a central data store that copies all canonical facts merely for indexing convenience.

A project-level semantic source under `docs/project_knowledge/` is allowed only when that semantic unit naturally has project-global ownership or requires its own lifecycle, such as:

```text
project integration boundary
identity transition / tombstone
qualified joint-authority declaration
capture candidate
selected architecture documentation
```

## 5. Project-knowledge repository directories

The implementation MAY create only the following initial project-knowledge roots without another specification revision:

```text
docs/project_knowledge/
    architecture/
    generated/
        manifests/
    captures/
        open/
        historical/
    transitions/
    joint_authority/

schemas/project_knowledge/

tools/project_knowledge/
```

Additional subdirectories MAY be added when they are implementation-local organization within these roots and do not introduce a new authority role.

A new top-level repository data store, project-knowledge database, or second authoritative registry requires an explicit later decision/specification.

## 6. Markdown structured-declaration contract

A Markdown source participates in machine-resolved Candidate 01 semantics through exactly one bounded declaration block:

```text
<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{ ... strict JSON object ... }
<!-- PKA-STRUCTURED-DECLARATION-END -->
```

Rules:

```text
markers are exact and case-sensitive
at most one declaration block is permitted per carrier in V1
content between markers MUST be one valid JSON object
duplicate JSON object keys MUST be rejected
comments inside JSON are forbidden
trailing non-whitespace content inside the block is forbidden
profile/schema version MUST be explicit
declaration parsing MUST NOT depend on an LLM
absence of a declaration is valid for sources that do not participate in machine-resolved semantics
a malformed present declaration is a hard validation failure
```

The parser MUST tolerate LF or CRLF carrier line endings without changing the semantic JSON object.

## 7. Native JSON carrier rule

A canonical source already represented as JSON MAY carry Candidate 01 semantic fields directly only when:

```text
its existing schema permits those fields
the semantic facts are naturally owned by that JSON source
there is no conflicting compatibility contract
the source's authority class is explicit
```

A fixed compatibility JSON surface MUST NOT be extended merely to carry Candidate 01 metadata. In that case the natural canonical source remains elsewhere and the compatibility JSON remains derived or compatibility-only.

## 8. Profile schemas

Versioned JSON Schemas MUST live under:

```text
schemas/project_knowledge/
```

V1 MUST implement at least:

```text
semantic_source.v1.schema.json
workstream.v1.schema.json
governing_procedure.v1.schema.json
project_boundary.v1.schema.json
identity_transition.v1.schema.json
joint_authority.v1.schema.json
capture.v1.schema.json
derived_view_manifest.v1.schema.json
```

A small shared `$defs` schema MAY be used.

The schemas MUST use profile-specific required fields. They MUST NOT require irrelevant empty fields on every source.

Schema validation is necessary but not sufficient: cross-source identity, relation, authority, workstream, freshness, privacy and migration rules require semantic validators.

## 9. Common governed-source envelope

Every structured canonical/candidate/historical semantic source MUST declare the equivalent of:

```text
schema_version
profile
kind
authority_class
```

and, only where applicable:

```text
semantic_id
state
scope
relations
provenance
risk_or_reopen_triggers
temporal qualifiers
```

Allowed `authority_class` values in V1:

```text
canonical
candidate
historical
derived
evidence
capture
```

`derived` and `capture` MUST never be interpreted as current governing authority.

## 10. Semantic identity contract

A durable `semantic_id` is required only when semantic continuity across carrier changes or explicit cross-source reference materially matters.

Rules:

```text
semantic identity != repository path
semantic identity != Git blob SHA
semantic identity != display title
```

A source that does not require durable identity MUST NOT receive a meaningless generated ID merely to satisfy a global registry.

Within the governed current semantic set, durable IDs MUST be unique unless an explicit transition record represents the identity handoff state during migration.

The identity index is derived and MUST be rebuildable from canonical sources plus authoritative transition records.

## 11. Identity-transition contract

An `identity_transition.v1` source is permitted only when the transition itself requires durable provenance/authority.

Supported V1 transition classes:

```text
MOVE_OR_RENAME
REPRESENTATION_REPLACEMENT
MERGE
SPLIT
SUPERSEDE
RETIRE
REDIRECT
```

The transition MUST record predecessor identity/identities, successor identity/identities where applicable, transition class, source/provenance basis, effective/authority time only when material, and current resolution behavior.

Historical identities MUST remain resolvable after merge/split/retirement when Requirements V0.2 continuity requires it.

The normal identity lookup path MUST use a generated flattened current-target index and MUST NOT require scanning full Git history.

## 12. Relation semantics

V1 authoritative relation modes are:

```text
REPLACE
SUPPLEMENT
SPECIALIZE
CORRECT
```

A relation MUST include an explicit target and scope when the relation is not globally applicable.

Semantics:

```text
REPLACE
    successor fully governs the declared scope instead of predecessor

SUPPLEMENT
    predecessor remains governing and successor must be consumed with it

SPECIALIZE
    successor governs a narrower explicit scope

CORRECT
    predecessor statement is erroneous for the declared scope
```

Relations MUST be authored once by the natural semantic owner wherever a natural direction exists. Reverse edges and closure are generated.

## 13. Joint-authority exception

A `joint_authority.v1` source MUST NOT be created merely because multiple sources are relevant.

Creation requires the J1-J6 admission logic frozen in Candidate 01:

```text
J1 multiple current canonical sources overlap the same governed action/scope/time
J2 ordinary source-owned relations cannot represent the governing-set semantics without an arbitrary non-semantic directional tie-break
J3 an irreducible set-level authoritative fact exists
J4 the set-level fact is independently queried/activated for consequential behavior
J5 creation receives explicit promotion/evidence/review and duplicate ownership is rejected
J6 unclear J1-J4 -> UNRESOLVED, not automatic joint authority
```

The joint source MUST own only combination semantics and MUST NOT duplicate substantive member content.

## 14. Temporal semantics

Git revision/history is the default recording history.

The implementation MUST NOT require universal bitemporal fields.

Selective fields MAY include:

```text
effective_from
effective_to
authority_from
authority_to
```

only when applicability/authority differs materially from repository recording time.

Generated current-authority views MUST resolve explicit temporal semantics when present and MUST NOT use latest-commit recency as a substitute for authority.

## 15. Workstream profile

A resumable workstream with durable continuity MUST use `workstream.v1` and include:

```text
semantic_id
state
objective or objective reference
```

Allowed states:

```text
ACTIVE
PAUSED
BLOCKED
COMPLETED
SUPERSEDED
```

Optional/conditional controls:

```text
parent
depends_on[]
pause_reason
return_condition
resume_target
current_anchor
expected_revision / source revision binding
risk_or_reopen_triggers
```

If state is `PAUSED` and the workstream is expected to resume, `pause_reason`, `return_condition`, and `resume_target` are required.

The workstream graph MUST support multiple dependencies and MUST reject dependency cycles that make deterministic continuation impossible unless an explicit cycle-safe semantics is later specified.

## 16. Interruption and concurrency semantics

Interruption recovery MUST derive completed work from durable project evidence/receipts, not from a previous chat's unstored plan state.

A transition/workflow MAY carry ordered durable step receipts. Recovery MUST distinguish completed and pending steps and MUST NOT blindly replay completed consequential mutations.

Authoritative updates MUST support expected-revision preconditions. A stale expected revision MUST fail before authoritative mutation.

The V1 concurrency contract is optimistic/fail-visible. It does not claim to provide a distributed transaction system or a global lock.

## 17. Governing-procedure and action-contract profile

A `governing_procedure.v1` source that controls consequential guidance or mutation MUST define:

```text
semantic_id
state / applicability
governed action classes / scope
constraint identifiers
preconditions
ordered mandatory constraints or steps where order matters
prohibitions
required postconditions / verification
fail-closed conditions
```

For these machine-checkable facts, the structured declaration is the sole normative machine contract.

Prose remains authoritative for explanation/rationale/context. Material contradiction between prose and the structured contract MUST produce a semantic-drift validation finding and MUST NOT be silently reconciled by a model.

## 18. Source-revision descriptor

A persistent receipt or manifest binding repository authority MUST use an explicit descriptor equivalent to:

```json
{
  "source_path": "docs/example.md",
  "source_commit": "<40-char commit when immutable commit binding is required>",
  "hash_algorithm": "sha256",
  "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
  "content_digest": "<64-char lowercase digest>"
}
```

Allowed V1 `hash_basis` for canonical tracked repository authority:

```text
GIT_BLOB_BYTES_AT_COMMIT
```

Working-tree bytes, normalized text, or external attachment bytes MUST NOT be substituted silently.

External attachment provenance MUST record repository identity and materialization identity separately when both matter.

## 19. Same-commit generated-view binding

A generated view committed in the same commit as changed canonical inputs cannot require the final commit SHA as an input to its own pre-commit generation.

Such a view manifest MUST instead bind:

```text
ordered input source identities / paths
exact canonical input content digests
hash basis for each input
generator identity
generator version / implementation digest
view schema/version
```

After commit, validators MAY additionally record/check commit provenance, but same-commit freshness MUST be decidable without a self-referential commit hash.

## 20. Persistent deterministic derived views

V1 production implementation MUST be able to generate:

```text
docs/project_knowledge/generated/source_catalog.json
docs/project_knowledge/generated/identity_index.json
docs/project_knowledge/generated/authority_index.json
docs/project_knowledge/generated/workstream_graph.json
docs/project_knowledge/generated/subject_index.json
docs/project_knowledge/generated/risk_obligation_index.json
docs/project_knowledge/generated/current_state_core.json
docs/project_knowledge/generated/CURRENT_STATE_CORE.md
```

The exact V1 schemas for these outputs MUST be frozen in implementation tests before canonical migration depends on them.

Every persistent derived view MUST have a `derived_view_manifest.v1` representation under:

```text
docs/project_knowledge/generated/manifests/
```

or an equivalent adjacent location when required by file-format constraints.

Derived views MUST contain no unique accepted truth.

## 21. Derived-view manifest requirements

A persistent derived-view manifest MUST record:

```text
view_id
view_path
view_schema_version
authority_class = derived
input bindings
generator identity
generator version/digest
rebuildability class
created/refreshed boundary
freshness state or verifiable freshness basis
```

Allowed V1 rebuildability classes:

```text
DETERMINISTIC_BYTE_REBUILD
DETERMINISTIC_SEMANTIC_REBUILD
REGENERABLE_NONAUTHORITATIVE
```

Structural views used for routing, identity, authority, workstreams and current core MUST use a deterministic class.

A stale persistent derived view MUST fail freshness validation visibly. It MUST NOT silently continue to govern consequential actions.

## 22. Canonical serialization for generated JSON

Deterministic generated JSON MUST use:

```text
UTF-8
LF line endings
final newline
2-space indentation
stable object-key ordering where semantically irrelevant
stable array ordering defined per view schema
no timestamps unless the timestamp is semantically required and excluded from byte-stability gates
```

If a view includes a refresh timestamp for human observability, deterministic semantic comparison MUST exclude that field or use a separate manifest record so rebuild equality remains testable.

## 23. Full rebuild

The production CLI MUST support:

```text
python -m tools.project_knowledge rebuild
```

A full rebuild MUST:

```text
discover governed semantic sources in the checked repository tree
parse and schema-validate all present declarations
run semantic identity/relation/workstream/authority/privacy checks
generate all deterministic structural views into a temporary/staged location
compare staged outputs with committed outputs or publish them only when explicitly requested by the governed workflow
never mutate canonical sources automatically
report actionable failures non-zero
```

Normal reconstruction MUST NOT require a full rebuild on every task.

## 24. Incremental refresh

The production CLI MUST support an operation equivalent to:

```text
python -m tools.project_knowledge refresh --changed-since <ref>
```

The incremental path MUST:

```text
identify changed governed sources
compute affected derived dependencies
regenerate only affected neighborhoods
produce outputs semantically equivalent to a full rebuild for those views
fall back to a full rebuild when dependency impact cannot be established safely
```

An ordinary local source change MUST NOT require manual edits to every global view.

## 25. Authority resolver

The implementation MUST provide a deterministic project-controlled authority resolver.

Input contract MUST support:

```text
action / requested operation
target / scope
current workstream/environment
actor/role when material
consequence class
time when material
```

Minimum result statuses:

```text
RESOLVED
UNRESOLVED_SCOPE_REQUIRED
UNRESOLVED_AUTHORITY_CONFLICT
MISSING_REQUIRED_AUTHORITY
STALE_REQUIRED_AUTHORITY
REQUIRED_PRIVATE_STATE_UNAVAILABLE
```

A `RESOLVED` receipt MUST record:

```text
governing semantic IDs
carrier paths
exact source revisions
applicability reason
relation / combination semantics
activated action-contract constraint IDs
freshness/availability result
```

Probabilistic retrieval rank MUST NOT set this status.

## 26. Reconstruction planner

The implementation MUST support at least three task classes:

```text
BROAD_CONTINUATION
NARROW_GOVERNED_TASK
EXPLORATORY_RESEARCH
```

A reconstruction contract MUST be able to record:

```text
task class
minimum safe orientation sources/views
must-load governing sources
optional/supporting evidence
negative/do-not-load context guidance where material
freshness requirements
receipt requirements
fail/escalate conditions
```

The planner MAY use model-assisted intent classification, but governing-source closure and safety constraints MUST remain project-controlled and independently inspectable.

## 27. Capture and promotion

Open captures MUST live under:

```text
docs/project_knowledge/captures/open/
```

and MUST validate as `capture.v1`.

A capture is non-authoritative by definition.

Promotion requires an explicit reviewed operation that records:

```text
capture/candidate provenance
review disposition
accepted understanding
natural target canonical source
resulting source revision
```

Promotion updates or creates the natural canonical source. It MUST NOT simply flip the capture's `authority_class` to canonical.

After promotion and provenance verification, the capture MAY move to:

```text
docs/project_knowledge/captures/historical/
```

or be removed if the governing preservation contract proves its provenance is fully retained elsewhere.

## 28. Public/private contract

Public repository authority remains public-safe.

A public semantic source MAY declare an abstract private dependency but MUST NOT expose private paths, secrets, private source-store roots, or private content merely to make reconstruction complete.

A consequential task requiring private state MUST produce a fail-visible unavailable/stale result when that state cannot be verified.

Public derived-view generation MUST run non-leakage validation before publication.

## 29. Optional retrieval caches

V1 safe operation MUST NOT require a vector database, graph database, or project-knowledge SQL database.

Optional lexical/FTS/vector/semantic indexes MAY be introduced later as rebuildable derived caches behind explicit adapters.

Such a cache:

```text
cannot contain unique accepted truth
cannot override explicit authority semantics
can be deleted/rebuilt without knowledge loss
must expose source-role/authority metadata where practical
cannot be required for fail-safe governing-source resolution
```

## 30. Compatibility surfaces during migration

Until the explicit authority switch, these current paths retain their existing authority/compatibility contracts:

```text
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

Migration behavior:

```text
CONTINUITY.md
    remains authored bootstrap/constitutional procedure
    may be reduced only after successor reconstruction is proven and cutover is governed

current_routing.json
    keeps its existing exact schema
    successor generation begins in shadow
    direct generation of the live path requires a later migration-wave gate

CURRENT_STATE.md
    remains current human live-state authority before cutover
    successor compact/current view is shadow-compared first

KNOWLEDGE_MAP.md
    remains navigation authority/compatibility surface before cutover
    generated subject/navigation output is shadow-compared first
```

No W0/W1 implementation may silently change these roles.

## 31. Professional architecture documentation

The implementation program MUST create:

```text
docs/project_knowledge/architecture/README.md
docs/project_knowledge/architecture/whole_architecture.md
docs/project_knowledge/architecture/semantic_authority_model.md
docs/project_knowledge/architecture/knowledge_lifecycle.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/project_knowledge/architecture/migration_and_cutover.md
```

The documentation MUST distinguish logical architecture from physical implementation.

It MUST include one professional whole-architecture overview and focused diagrams for:

```text
semantic ownership / identity / authority
capture-review-promotion lifecycle
fresh-collaborator reconstruction / authority / action
migration / compatibility / cutover / rollback
```

Diagram source MUST be version-controlled and human-reviewable. Where practical, rendered SVG/PNG outputs SHOULD be deterministic/regenerable from that source.

A chat-only visualization does not satisfy this requirement.

## 32. CLI contract

V1 MUST provide command surfaces equivalent to:

```text
python -m tools.project_knowledge validate
python -m tools.project_knowledge rebuild
python -m tools.project_knowledge refresh --changed-since <ref>
python -m tools.project_knowledge check-freshness
python -m tools.project_knowledge resolve-authority <task-spec>
python -m tools.project_knowledge reconstruct <task-spec>
python -m tools.project_knowledge migration-audit
```

The implementation MAY add machine-readable output flags, dry-run/staging controls and explicit root/ref options when they do not widen authority silently.

No CLI command may auto-promote a capture, auto-select authority under unresolved conflict, or auto-switch project operational authority.

## 33. Validation layers

### Local deterministic validation

MUST cover:

```text
declaration parse/schema validity
semantic ID uniqueness
profile-specific conditional fields
relation target existence
workstream dependency validity
procedure constraint identity/order validity
private/public field restrictions
revision-descriptor validity
```

### Impact-aware validation

MUST cover:

```text
identity transition closure
supersession/supplement closure
joint-authority membership/combination semantics
workstream dependency/resume consistency
derived-view impacted dependency set
inbound references relevant to migration/moves
```

### Freshness/rebuild validation

MUST cover:

```text
persistent manifest input bindings
generator identity/version
stale view detection
deletion/rebuild equivalence for deterministic views
incremental/full rebuild semantic equivalence
```

### Behavioral qualification

MUST preserve regression coverage for Candidate 01's qualified hard cases, including:

```text
fresh cold continuation
narrow consequential authority resolution
missing/conflicting authority
retrieval non-authority
contract fidelity
identity/lifecycle cases
nested/multi-dependency workstreams
interruption recovery
stale write rejection
public/private degraded mode
capture/promotion
migration parity and rollback
```

## 34. Integration with existing repository integrity

Production project-knowledge validation MUST become a component of the existing aggregate public repository-integrity gate before any successor-generated compatibility surface becomes authoritative.

The aggregate MUST remain fail-closed and continue to emit:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS
```

only when all required components pass.

The project-knowledge implementation MUST NOT replace existing checkpoint/model-collaboration/current-routing/Knowledge-Map validators before equivalent or stronger behavior is verified and deliberately reconciled.

## 35. Migration waves

Migration MUST proceed in these governed waves.

### W0 — implementation substrate

Create:

```text
tools/project_knowledge/
schemas/project_knowledge/
docs/project_knowledge/architecture/
docs/project_knowledge/generated/ contract/tests
```

Implement parser, schemas, core typed model, Git revision helper, validation skeleton, deterministic generator framework and CLI scaffolding.

No existing canonical source is required to adopt a declaration during W0.

### W1 — live control semantics

Migrate a bounded high-value set only:

```text
selected Candidate 01 architecture/workstream
Project Integration Boundary
Source Vault bootstrap workstream
paused Cockpit workstream
D-035 / directly needed high-consequence governing semantics
```

W1 MUST preserve current compatibility outputs and MUST not switch operational authority.

### W2 — shadow derived views

Generate all V1 structural views from successor semantic owners. Compare with qualified shadow expectations and current compatibility state.

### W3 — compatibility shadow

Produce shadow candidates for routing/current-state/Knowledge-Map roles without overwriting live paths. Classify every difference as:

```text
EXPECTED_SEMANTIC_IMPROVEMENT
EQUIVALENT_REPRESENTATION
MIGRATION_GAP
LEGACY_DRIFT
UNRESOLVED
```

`MIGRATION_GAP` or `UNRESOLVED` blocks advancement.

### W4 — production capture/promotion path

Run one bounded real capture through review and canonical promotion. Verify accepted meaning/provenance remains after capture archival/removal according to the preservation contract.

### W5 — broader current semantic migration

Migrate by semantic responsibility/domain, not chronology or file enumeration. Deep passive history remains latent unless current continuity requires explicit identity/authority semantics.

### W6 — cutover candidate

Successor-generated compatibility surfaces may replace their legacy-authored equivalents only in a controlled cutover candidate branch/state after W0-W5 acceptance.

### W7 — cutover qualification

Re-run the relevant Requirements V0.2 acceptance program against the actual production implementation and migrated repository state.

### W8 — explicit authority switch

Only after W7 PASS, owner confirmation, rollback proof and repository integrity may a new explicit decision change operational authority.

## 36. Migration-unit contract

Every semantically migrated unit MUST receive a migration disposition:

```text
MIGRATE_CANONICAL
DERIVE_COMPATIBILITY_VIEW
KEEP_HISTORICAL_LATENT
KEEP_EVIDENCE_ONLY
CAPTURE_OR_CANDIDATE
PRIVATE_DELEGATED
UNRESOLVED_MIGRATION
```

For `MIGRATE_CANONICAL`, record:

```text
semantic unit identity when applicable
legacy authority source/boundary
successor canonical owner
semantic parity evidence
provenance preservation
inbound-reference disposition when relevant
rollback representation
```

`UNRESOLVED_MIGRATION` blocks cutover for any unit required by the active/current architecture.

## 37. No mass historical conversion

Implementation MUST NOT add Candidate 01 declarations to every historical document merely to maximize structured coverage.

Historical sources remain valid evidence/history under current repository contracts unless:

```text
their current semantic identity must remain resolvable
they participate in current authority closure
they are required for active workstream continuation
a migration/parity requirement specifically needs structured representation
```

This rule is part of the architecture's maintenance-economics contract.

## 38. Research-code reuse rule

Before reusing code from `scripts/research/`, classify each component as:

```text
PROMOTE_NEARLY_AS_IS
REFINE_AND_PROMOTE
REIMPLEMENT_BEHIND_PRODUCTION_CONTRACT
KEEP_AS_TEST_OR_REFERENCE_ONLY
RETIRE_AFTER_PRODUCTION_EQUIVALENT
```

Fixture/oracle-specific constants and experiment-only read restrictions MUST NOT leak into general production behavior.

Research results/oracles remain immutable qualification evidence and MUST NOT be rewritten to match production implementation choices.

## 39. W0 executable gates

W0 is accepted only when all gates below pass.

```text
PKA-G001 package boundary exists under tools/project_knowledge and not src/ads_system
PKA-G002 all eight V1 profile schemas validate positive fixtures and reject required negative fixtures
PKA-G003 Markdown declaration parser rejects malformed/duplicate/multiple blocks and supports LF/CRLF carriers
PKA-G004 canonical semantic model represents authority class, selective identity, scope and typed relations without universal IDs
PKA-G005 Git revision helper verifies GIT_BLOB_BYTES_AT_COMMIT descriptors deterministically
PKA-G006 identity index generator rebuilds deterministically and resolves qualified transition fixtures
PKA-G007 authority resolver passes REPLACE/SUPPLEMENT/SPECIALIZE/CORRECT, ambiguity and retrieval-non-authority regressions
PKA-G008 workstream engine passes DAG, pause/return/resume, interruption and stale expected-revision regressions
PKA-G009 derived-view framework produces deterministic manifests and detects stale input bindings
PKA-G010 current-state-core generator reproduces bounded qualified must-preserve fixture behavior
PKA-G011 capture validation enforces non-authority before explicit promotion
PKA-G012 public/private validation rejects synthetic leakage and preserves consequence-sensitive unavailable state
PKA-G013 full rebuild and incremental refresh are semantically equivalent on the frozen W0 fixture corpus
PKA-G014 CLI validate/rebuild/check-freshness surfaces are deterministic and fail non-zero on hard defects
PKA-G015 professional architecture documentation skeleton plus version-controlled whole-architecture diagram source exists
PKA-G016 existing public repository-integrity aggregate remains PASS
PKA-G017 inherited complete unit suite remains PASS
```

No W0 gate may be waived retrospectively without a prospective Specification 028 revision/amendment.

## 40. W1 executable gates

Before W1 semantics are treated as migration-ready:

```text
PKA-G101 selected architecture/workstream semantic owner validates
PKA-G102 Project Integration Boundary has one natural canonical semantic owner
PKA-G103 Source Vault paused/resume semantics reproduce the qualified real state
PKA-G104 Cockpit paused/resume semantics reproduce the qualified real state
PKA-G105 D-035 selection semantics resolve without duplicating its substantive decision text
PKA-G106 generated workstream/current-core views are deterministic from W1 canonical owners
PKA-G107 no existing live compatibility path is overwritten
PKA-G108 current continuity remains explicit operational authority
PKA-G109 public repository integrity remains PASS
```

## 41. Architecture-documentation acceptance

The documentation is accepted for the selected architecture only when:

```text
the whole-architecture overview distinguishes canonical sources, semantic control, derived access, reconstruction/action and migration/control boundaries
the semantic-authority diagram shows identity separate from authority and retrieval subordinate to authority
the lifecycle diagram shows capture non-authoritative until promotion
the reconstruction diagram distinguishes broad continuation, narrow governed task and exploratory research
the migration diagram makes current authority, shadow successor, qualification, cutover and rollback explicit
diagrams are version-controlled in the repository
rendered visuals, when committed, match their source representation
documentation does not imply that physical files shown are themselves the logical architecture
```

## 42. Cutover qualification minimum

W7 MUST revalidate at least:

```text
all 67 Requirements V0.2 items against production/migrated state
cold fresh-session continuation
provider/tool portability
broad and narrow task budgets
consequential authority + action-contract fidelity
supersession/conflict and retrieval non-authority
workstream interruption/concurrency
public/private degraded mode
capture/promotion
identity/carrier continuity
full generated-view rebuild
incremental/full equivalence
migration parity
rollback export/recovery
repository integrity
```

A prior Research 175 PASS is evidence for the logical architecture, not a substitute for W7 production cutover qualification.

## 43. Authority-switch prohibition

Before W8, every implementation/result MUST preserve:

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

No generator, migration command, test fixture, documentation statement, or target-selection decision may implicitly switch authority.

W8 requires a separate explicit owner-approved decision after successful W7 qualification.

## 44. Explicit non-goals for V1 implementation

Specification 028 does not require or authorize:

```text
project-knowledge graph database
vector database
central canonical SQL store
universal semantic object registry
mass conversion of historical documents
automatic LLM promotion of captures
automatic resolution of unresolved authority conflicts
replacement of Git as durable project-development authority
automatic mutation of canonical sources by rebuild/refresh
network service/API
multi-user distributed locking
source-vault ingestion resumption
Project Cockpit frontend resumption
operational authority switch
```

## 45. Acceptance state transitions

Specification 028 has these program states:

```text
FROZEN / IMPLEMENTATION PENDING
    -> W0 implementation may begin

W0 ACCEPTED
    -> production substrate exists; W1 canonical migration may begin

W1-W6 accepted sequentially
    -> cutover candidate exists but current authority remains live

W7 PASS
    -> authority-switch decision becomes eligible

W8 explicit decision
    -> only then may operational authority change
```

A checkpoint is created only for meaningful verified boundaries, not for every implementation edit.

## 46. Frozen continuation

The immediate continuation is:

```text
Specification 028 freeze
    -> W0 implementation substrate
    -> PKA-G001..PKA-G017
    -> W0 acceptance result
    -> only then W1 live-control semantic migration
```

The first implementation task SHOULD begin with the production package/schema/declaration/revision/validation skeleton and tests, not by converting `CURRENT_STATE.md` or `KNOWLEDGE_MAP.md`.

```text
SPECIFICATION_028=FROZEN
SELECTED_TARGET=PKA-CANDIDATE-01
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=W0_IMPLEMENTATION_SUBSTRATE
```
