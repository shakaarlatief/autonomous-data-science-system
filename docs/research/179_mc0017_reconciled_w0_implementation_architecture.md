# Research 179: MC-0017 Reconciled W0 Implementation Architecture

**Date:** 2026-09-15
**Status:** ACCEPTED W0 IMPLEMENTATION ARCHITECTURE / MC-0017 RECONCILED / SPECIFICATION 028 UNCHANGED / W0 SUBSTRATE SLICE 1 ACCEPTED / IDENTITY+AUTHORITY ENGINES NEXT
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Scope:** Freeze the concrete production W0 software/repository architecture after independent ChatGPT and Claude designs plus bounded comparative reconciliation.
**Authority:** Accepted implementation-design interpretation subordinate to D-035, Requirements V0.2 and Specification 028. This record resolves implementation freedom left open by Specification 028 but does not amend that specification, migrate canonical knowledge, or switch operational authority.
**Declared references:** `research:144`, `research:175`, `research:176`, `research:177`, `research:178`, `specification:028`, `path:docs/model_collaboration/threads/MC-0017/messages/001_claude_independent_w0_implementation_architecture.md`, `path:docs/model_collaboration/threads/MC-0017/messages/002_chatgpt_comparative_w0_implementation_architecture.md`, `path:docs/model_collaboration/threads/MC-0017/messages/003_claude_comparative_w0_implementation_critique.md`

## 1. Outcome

MC-0017 produced strong independent convergence and a small number of useful corrections. The reconciled design keeps Candidate 01 unchanged and gives Codex a concrete W0 production target.

```text
LOGICAL_ARCHITECTURE_REOPEN_REQUIRED=false
H3_REOPEN_TRIGGERED=false
SPECIFICATION_028_AMENDMENT_REQUIRED_BEFORE_W0=false
FURTHER_CLAUDE_DESIGN_ROUND_REQUIRED=false
W0_IMPLEMENTATION_MAY_BEGIN=true
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 2. Package and dependency architecture

Use a shallow layered package under the Specification 028 boundary:

```text
tools/project_knowledge/
    __init__.py
    __main__.py
    model.py

    adapters/
        gitio.py
        fsio.py
        schema.py

    declaration.py
    references.py
    identity.py
    authority.py
    workstreams.py
    views.py
    reconstruction.py
    capture.py

    services/
        discovery.py
        generation.py
        validation.py
        migration.py
        workstream_ops.py

    cli.py
```

The load-bearing dependency rule is:

```text
L0 model/value objects
    -> stdlib only

L1 adapters
    -> L0

L2 semantic/domain modules
    -> L0 only
    -> MUST NOT import adapters or services

L3 services/orchestration
    -> L0 + L1 + L2

L4 CLI
    -> L0 + L3
```

The package stays shallow to avoid framework growth, but the import direction is mechanically enforced by an AST-based architecture test. Pure semantic algorithms receive already-read bytes/value objects rather than repository handles.

## 3. Typed semantic model

Use immutable typed records, preferably frozen dataclasses/enums/value objects.

Minimum production concepts:

```text
SemanticId
AuthorityClass
Profile
LifecycleState
RelationMode
TransitionClass
Scope
Relation
SourceRevision
GovernedSource
Workstream
ActionContract
AuthorityQuery
AuthorityResult
AuthorityReceipt
ViewManifest
ReconstructionPlan
CaptureRecord
PromotionPlan
Diagnostic
```

Selective identity remains an invariant:

```text
semantic_id is optional unless continuity requires it
no function auto-mints semantic IDs from path/title/hash
sources without semantic IDs remain first-class governed sources
```

`SemanticId` lexical validation must use an actual validating value object/factory rather than relying on Python `NewType` as runtime validation.

## 4. JSON Schema architecture

Use JSON Schema Draft 2020-12.

Prefer one small shared definitions file containing reusable property/value schemas only. Do not use a giant base object schema.

Each of the eight profile schemas declares its complete allowed property set explicitly and uses:

```text
additionalProperties: false
```

Shared property definitions are referenced with `$ref`; object composition should not rely on the broken pattern of placing common fields in one `allOf` branch while another branch applies `additionalProperties: false`.

G002 must include, for every profile:

```text
valid envelope + valid profile fields -> PASS
same object + one unknown property    -> FAIL
```

This proves strictness is actually honored by the running validator.

## 5. `project_boundary.v1`

W0 implements a deliberately narrow control-semantics profile:

```text
common governed-source fields
semantic_id required
state when material
scope when material
relations when naturally owned
provenance/references when material
NO arbitrary generic facts object
```

Rich prose in the Project Integration Boundary source owns substantive project-wide meaning. The declaration carries only machine-needed control semantics.

W1 watch item: once the real source exists, determine whether this profile gains a genuinely distinguishing required field or can be folded into `semantic_source.v1`. This is not a W0 blocker.

## 6. Declaration parsing

Markdown declaration parsing is strict and deterministic:

```text
exact case-sensitive markers
UTF-8 strict decode
zero blocks is valid
multiple/unbalanced/inverted markers are hard failures
strict JSON object only
duplicate keys rejected with object_pairs_hook
profile-selected schema validation
LF/CRLF tolerated without rewriting carrier semantics
```

Native JSON carriers and Markdown carriers converge to one internal raw-declaration representation downstream of extraction.

## 7. Repository snapshot and discovery model

W0 has two explicit snapshot modes.

### COMMIT_SNAPSHOT

```text
source universe: git ls-tree -r <ref>
bytes: exact Git blobs
purpose: durable evidence, persistent receipts/manifests, immutable verification
```

### WORKTREE_SNAPSHOT

```text
source universe: git ls-files --cached --others --exclude-standard
purpose: local validation/rebuild before commit, including unstaged new sources
status: NON_COMMITTED / never durable authority evidence
```

Snapshot mode is a structural field on repository snapshots and on any receipt/manifest representation that may escape local execution. A durable-evidence validator MUST reject artifacts produced from `WORKTREE_SNAPSHOT` as commit-bound authority evidence.

Persistent canonical revision binding continues to use Specification 028's:

```text
GIT_BLOB_BYTES_AT_COMMIT
```

Worktree fingerprints may exist internally for local change detection but must not masquerade as persistent source revisions.

## 8. Source discovery and catalog

Do not maintain a canonical-source registry.

Discovery scans bounded supported carriers under one centralized policy. Generated outputs, captures, research fixtures and other non-production roots are excluded by explicit policy, but exclusions remain observable.

Persistent `source_catalog.json` contains governed production semantic sources, not every Markdown/JSON file in the repository.

Discovery diagnostics include:

```text
EXCLUDED_BUT_DECLARED      severity ERROR
malformed declarations     severity ERROR
excluded candidate counts
undeclared candidate counts
bounded counts by root
```

The bounded counts preserve saturation observability without turning the source catalog into a file inventory.

## 9. Scope semantics

Action and time are not duplicated inside `Scope`.

```text
AuthorityQuery
    action
    target
    scope
    consequence
    at_time
    workstream/actor when material

Scope
    finite conjunction of named exact-match facets
    each facet value is one value or a finite allowed set
    no regex
    no executable predicates
    no wildcard language
```

Per-candidate scope matching is three-valued:

```text
NO_MATCH
UNDERSPECIFIED
MATCH
```

A missing query facet makes a candidate `UNDERSPECIFIED`, but it does not automatically make the whole resolution unresolved.

`UNRESOLVED_SCOPE_REQUIRED` is emitted only when an omitted facet can discriminate the resulting governing set. If every possible value compatible with the surviving candidates produces the same governing set, resolution may continue.

Consequence never converts an undetermined authority query into a determined one.

Specificity between declared scopes is a partial order used to validate/fire `SPECIALIZE`. Stable sort order may serialize results but never creates semantic precedence.

## 10. Authority resolver

`resolve_authority()` is pure domain logic over explicit inputs.

The production pipeline is:

```text
1. collect current canonical candidates for action/target
2. evaluate scope candidates and discrimination
3. apply temporal applicability
4. apply REPLACE / CORRECT / SPECIALIZE / SUPPLEMENT closure
5. evaluate qualified JOINT_AUTHORITY only over surviving candidates
6. detect unresolved conflicts
7. verify source revision/freshness
8. enforce required private dependency availability
9. activate ordered governing-procedure constraints
10. emit deterministic receipt
```

Rules:

```text
retrieval nominations never set disposition
joint authority cannot resurrect a filtered source
REPLACE/CORRECT cycles are unresolved conflict
sorting never creates authority priority
scope ambiguity is fail-visible independent of consequence
```

A resolved receipt includes the Specification 028 minimum plus:

```text
per-source scope disposition
removed sources + explicit removal reason
snapshot mode
```

## 11. Identity transitions

Build a complete transition/provenance representation and a flattened current lookup index.

Normal lookup is bounded and never scans Git history.

Supported classes remain:

```text
MOVE_OR_RENAME
REPRESENTATION_REPLACEMENT
MERGE
SPLIT
SUPERSEDE
RETIRE
REDIRECT
```

Transition records exist only when the transition itself carries durable semantic/provenance meaning. The generated current identity index is deletable/rebuildable and is not a registry of authority.

## 12. Workstreams and route semantics

The pure workstream layer computes:

```text
validated DAG
active_ready_set
paused/blocked/completed state
parent/dependency closure
pause/return/resume consistency
interruption recovery classification
```

A primary route is derived only from explicit semantic controls such as parent/current-anchor/resume semantics.

It MUST NOT be selected by fixture order, file order or lexical `semantic_id` sorting.

When multiple ready branches exist without a unique semantic primary route, the planner returns:

```text
NO_UNIQUE_PRIMARY_ROUTE
active_ready_set with branch anchors/context
```

rather than an empty answer or an invented priority.

Authoritative writes remain service-layer operations with expected-revision checks immediately before mutation. Stale writes fail before mutation.

## 13. Derived-view engine

There is one build architecture for full and incremental operation.

Each view has an explicit specification equivalent to:

```text
view_id
input selector/dependencies
pure compute function
pure deterministic serializer
manifest builder
```

Full rebuild selects all views.

Incremental refresh selects only affected views, but every selected view is recomputed from its **complete current input set** using the exact same builder as full rebuild.

Incremental refresh never patches persisted view state as a separate semantic implementation.

If impact is uncertain, select more views or fall back to full rebuild.

## 14. Generator identity and digest basis

Persistent view manifests carry both human-intent versioning and mechanical implementation binding:

```text
generator_id
generator_version
implementation_basis = GIT_BLOB_BYTES_AT_COMMIT
ordered implementation_files[]
implementation_digest
```

Aggregate digest framing:

```text
sha256(
    for each implementation path in declared order:
        UTF8(path) || NUL || exact Git blob bytes || NUL
)
```

The implementation file list is explicit and auditable. `generator_version` changes when output semantics intentionally change; the digest catches implementation changes that forgot a version bump. Freshness fails if either expected version or implementation binding mismatches.

For pre-commit generation, exact staged/index blob bytes may be used to compute the would-be canonical Git-blob digest, but persistent post-commit validation must verify those digests against the committed Git blobs. Worktree bytes must never silently substitute.

## 15. Persistent derived views

Implement all eight views required by Specification 028 during W0. Do not remove subject/risk indexes by taste before evidence exists.

Instrument view churn/size so W2 can revisit whether every view should remain persistently committed.

Persistent generated structural views contain no unique accepted truth.

## 16. Reconstruction planner

Free-text/model understanding may produce a small explicit `TaskIntent`. From that boundary onward, reconstruction is deterministic and project-controlled.

Supported classes remain:

```text
BROAD_CONTINUATION
NARROW_GOVERNED_TASK
EXPLORATORY_RESEARCH
```

Plans carry:

```text
must-load
optional
negative/do-not-load
freshness requirements
receipt requirements
fail/escalate conditions
```

The recent missed Claude-history activation is classified as a dispatch/activation failure, not proof of a missing topology registry.

W0 therefore adds the falsifier `PKA-W0-J1`:

```text
fixture contains relevant collaboration-history sources outside active workstream
project-history/narrow task intent names the subject, not the folder
planner must surface the correct collaboration sources and roles
no human-supplied repository path is allowed
broad continuation exposes the generated navigation/discovery capability and how to invoke it
broad current core need not enumerate every dormant domain
```

No new global semantic-topology registry is introduced.

## 17. Capture and promotion

Captures are structurally separate from canonical discovery and cannot enter the authority resolver.

The capture schema fixes non-authority. W0 computes and validates `PromotionPlan`; it does not perform real W1/W4 promotion.

Preservation is checked with explicit semantic-unit dispositions rather than a fake semantic-equivalence function:

```text
required semantic unit IDs
capture provenance chain
canonical target revision
per-unit disposition:
    MATERIALIZED_IN_CANONICAL_SOURCE
    INTENTIONALLY_LATENT_WITH_RECOVERABLE_SOURCE
    REJECTED_WITH_REVIEWED_RATIONALE
```

Mechanical validation proves complete disposition/provenance coverage. Human/model semantic review remains responsible for judging whether canonical prose actually realizes accepted meaning where that cannot be deterministically verified.

## 18. Public/private boundary

Public/private protection is layered:

```text
public schemas expose only public-safe fields
public generation consumes public-safe projections rather than raw private records
known private fixture values are checked against rendered bytes
rendered-byte pattern checks provide defense in depth
resolver enforces required private availability/freshness for consequential work
```

Rendered-byte checking is not claimed as proof of universal non-leakage.

Existing `RESOLVED_PRIVATE` semantics remain preserved: unavailable private inspection does not turn an already public-resolved fact into unresolved state.

## 19. Diagnostics

Use a stable structured diagnostic vocabulary:

```text
code
severity
carrier_path
semantic_id when present
message
related_sources when present
remediation when useful
```

Severity:

```text
ERROR    blocks publication/acceptance
WARNING  visible but non-blocking
INFO     observability
```

Prose/structured-contract drift in W0 is handled honestly: deterministic change-asymmetry and structural checks can require review, but the implementation must not claim a general semantic-equivalence verifier.

## 20. CLI safety boundary

Read-only commands:

```text
validate
check-freshness
resolve-authority
reconstruct
migration-audit
promotion-plan
```

Generated-output commands default to staged/diff behavior and require explicit materialization:

```text
rebuild
refresh
```

W0 does not expose canonical promotion or authority cutover commands.

No command may guess unresolved authority, auto-promote captures, mutate current compatibility authority, or switch project authority.

## 21. Architecture documentation and visualization

Canonical W0 diagram source is embedded Mermaid inside the owning Markdown architecture documents:

```text
docs/project_knowledge/architecture/README.md
docs/project_knowledge/architecture/whole_architecture.md
docs/project_knowledge/architecture/semantic_authority_model.md
docs/project_knowledge/architecture/knowledge_lifecycle.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/project_knowledge/architecture/migration_and_cutover.md
```

The whole-architecture overview must be intentionally composed and professional, with logical architecture clearly separated from physical implementation.

Focused diagrams carry detail that would overload the overview.

If SVG/PNG renders are later committed, they are derived artifacts and must have deterministic generator provenance/manifest coverage rather than becoming untracked visual truth.

## 22. Test architecture and strengthened gates

Preserve repository test topology:

```text
tests/fixtures/project_knowledge/
tests/unit/test_project_knowledge_*.py
```

In addition to PKA-G001 through PKA-G017, W0 tests must cover:

```text
AST dependency-layer enforcement
no auto-minted SemanticId capability
schema unknown-property rejection for all profiles
EXCLUDED_BUT_DECLARED -> ERROR
scope truth table + discrimination cases
receipt completeness/removal reasons
COMMIT_SNAPSHOT vs WORKTREE_SNAPSHOT authority boundary
no arbitrary workstream route tie-break
PKA-W0-J1 history/reconstruction activation
capture scanner structurally disconnected from authority resolver
semantic-unit promotion disposition completeness
generator digest framing/basis
```

These strengthen G002, G004, G007, G008, G009, G011, G013 and G015 without changing the frozen numbered gate set.

## 23. Implementation risks to monitor

Highest risks now are implementation mistakes rather than unresolved architecture forks:

```text
scope discrimination implemented too aggressively or too weakly
WORKTREE_SNAPSHOT artifacts accidentally treated as commit-bound evidence
schema strictness silently not enforced by runtime validator
primary workstream route invented from deterministic sort order
source discovery exclusions hiding real production declarations
generator implementation file lists too coarse or incomplete
project_boundary profile remaining a label rather than a meaningful contract
architecture diagrams becoming attractive but semantically stale derived artifacts
```

Each has an explicit W0 regression or W1/W2 watch item.

## 24. Specification 028 disposition

No pre-W0 amendment is required.

The reconciled choices are implementation freedoms already allowed by Specification 028, plus stricter tests/interpretations that preserve its guarantees.

If implementation demonstrates that any accepted choice cannot satisfy a frozen gate honestly, stop and amend prospectively rather than weakening the gate after seeing failure.

## 25. Final W0 continuation

```text
Candidate 01 selected and qualified
    -> Specification 028 frozen
    -> MC-0017 implementation architecture reconciled
    -> production W0 implementation may begin
    -> run PKA-G001..PKA-G017 + strengthened regressions
    -> W0 acceptance checkpoint
    -> only then W1 live-control semantic migration
```

Current compatibility authority remains untouched throughout W0.

```text
RESEARCH179=RECONCILED_W0_IMPLEMENTATION_ARCHITECTURE_ACCEPTED
MC0017=READY_TO_CLOSE
SPECIFICATION_028=UNCHANGED
W0_IMPLEMENTATION=AUTHORIZED_TO_BEGIN
W1_MIGRATION=BLOCKED_UNTIL_W0_ACCEPTANCE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
