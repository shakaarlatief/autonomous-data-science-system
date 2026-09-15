# Research 178: ChatGPT Independent W0 Implementation Architecture Design

**Date:** 2026-09-15
**Status:** CHATGPT INDEPENDENT W0 DESIGN FROZEN / WITHHELD FROM CLAUDE UNTIL MC-0017 MESSAGE 001 / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing implementation contract:** Specification 028
**Independent substantive base:** `1f09fc812e8d7b1f31771a8b545864b76ea61db0`
**Scope:** Freeze ChatGPT's preferred production W0 software/repository architecture before Claude produces an independent implementation design from the same pre-design base.
**Authority:** Design evidence only. Specification 028 remains the frozen implementation contract. This record does not authorize W0 implementation, W1 migration, or any authority switch.
**Declared references:** `specification:028`, `research:144`, `research:145`, `research:175`, `research:177`, `checkpoint:523`, `path:docs/README.md`, `path:docs/CONTINUITY.md`, `path:docs/model_collaboration/README.md`

## 1. Why freeze an independent implementation design

The selected logical architecture and the frozen physical contract still leave meaningful software-architecture choices open. Starting Codex implementation immediately would risk hardening one decomposition before a second model has independently reasoned about the implementation layer.

MC-0017 therefore uses an `INDEPENDENT_THEN_COMPARATIVE` design pattern. Claude's first pass is bound to the exact pre-Research-178 commit above. This record is intentionally withheld until Claude Message 001 is frozen.

## 2. Design stance

The production W0 implementation should remain deliberately small and deterministic. It should not recreate a framework platform around a framework platform.

Preferred principles:

```text
one in-memory semantic model
one declaration/schema path
one deterministic build graph for full + incremental generation
pure domain algorithms where possible
repository/Git I/O isolated at edges
no project-knowledge database
no hidden registry of canonical truth
no LLM dependency for correctness
no duplicated source/derived authority
```

The existing research prototypes are algorithm/evidence donors, not the desired production module architecture.

## 3. Package shape

Keep the Specification 028 package boundary:

```text
tools/project_knowledge/
```

Prefer a shallow responsibility-based module structure rather than introducing a full enterprise `domain/application/infrastructure` hierarchy during W0.

```text
tools/project_knowledge/
    __init__.py
    __main__.py
    model.py
    declaration.py
    discovery.py
    references.py
    git.py
    identity.py
    authority.py
    workstreams.py
    views.py
    reconstruction.py
    capture.py
    migration.py
    validation.py
    cli.py
```

`discovery.py` is the one addition to Research 177's illustrative list. Source discovery is important enough not to hide inside views or declaration parsing.

Do not split these modules further until real production pressure demonstrates a reason.

## 4. Internal semantic model

Use immutable typed Python records, preferably frozen dataclasses plus enums and small value objects. The model should be representation-neutral after declaration parsing.

Core values:

```text
SemanticId                optional except where continuity requires it
AuthorityClass            canonical / candidate / historical / derived / evidence / capture
Profile                    semantic-source / workstream / governing-procedure / ...
SemanticScope              structured conjunction of dimensions
Relation                   mode + target + optional scoped applicability
SourceRevision             path + commit/basis/digest
SourceRecord               carrier metadata + parsed declaration + revision
AuthorityQuery             action + target/scope + consequence + contextual qualifiers
AuthorityReceipt           result + governing sources + revisions + activated constraints
Workstream                 durable state + graph/control semantics
ActionReceipt              completed consequential step evidence
DerivedViewManifest        exact inputs + generator + output metadata
ReconstructionContract     task-shaped required/optional/negative context
CaptureRecord              explicitly non-authoritative candidate material
```

Do not invent a universal semantic-object base class whose identity is mandatory for all profiles. Shared Python interfaces may exist without changing Candidate 01's selective-identity semantics.

## 5. Schema architecture

Use JSON Schema Draft 2020-12.

Prefer one small shared definitions file for stable primitives:

```text
common.v1.schema.json
    authority class
    semantic ID lexical form
    relation mode
    revision descriptor
    common enums/basic structures
```

Each of the eight required profile schemas should then be independently understandable and use `$ref` only for genuinely common primitives.

Avoid a large base schema with dozens of optional properties. That would reproduce a universal ontology structurally even if the logical design says otherwise.

Use `additionalProperties: false` for machine-control structures where extension ambiguity is dangerous. Extension points should be explicit fields rather than unrestricted arbitrary keys.

## 6. Declaration parsing

The parser should have two layers:

```text
extract_declaration(text)
    marker discipline only

parse_and_validate_declaration(raw_json)
    duplicate-key rejection
    strict JSON parsing
    profile dispatch
    schema validation
    typed conversion
```

Use `json.loads(..., object_pairs_hook=...)` or equivalent to reject duplicate keys deterministically.

The extraction function should distinguish:

```text
ABSENT
VALID_BLOCK
MALFORMED_MARKERS
MULTIPLE_BLOCKS
```

instead of returning `None` for every non-success case.

## 7. Repository source discovery

Do not create a manually maintained canonical-source registry.

Preferred discovery mechanism:

```text
tracked repository files
    -> bounded supported carrier extensions/roots
    -> cheap marker/profile detection
    -> parse only governed sources
```

For a full rebuild, `git ls-files` or an equivalent tracked-tree reader provides a deterministic source universe. For incremental refresh, changed tracked paths are the first discriminator.

Generated outputs, test fixtures, `.git`, `.tmp`, private local state and research result fixtures must be excluded by policy rather than accidentally rediscovered as current canonical semantic sources.

The derived `source_catalog.json` is an output of discovery, never an input authority registry.

## 8. Scope semantics

Do not leave scope matching as generic dictionary magic.

W0 should define a deliberately small exact semantics:

```text
scope = conjunction of named dimensions
source scope constrains zero or more dimensions
query must provide enough dimensions to select unambiguously
matching means every source-constrained dimension equals the corresponding query dimension
missing query dimensions that affect selection -> UNRESOLVED_SCOPE_REQUIRED
```

No wildcard mini-language, regex scopes or arbitrary predicates in W0.

If later evidence needs richer scope algebra, add it prospectively rather than embedding an unbounded expression language now.

## 9. Identity and transition architecture

Identity resolution should be a pure graph transformation over only identity-bearing sources and transition records.

Build two products:

```text
complete transition graph
    preserves provenance/history semantics

flattened current identity index
    bounded lookup from historical/current ID to current carrier/successor state
```

The current index is generated from the transition graph and ordinary source declarations. It is not hand-authored.

Cycle detection, ambiguous split target resolution and invalid merge/split combinations should fail validation rather than be guessed.

## 10. Authority resolver algorithm

The resolver should be a deterministic pipeline, not one large conditional function:

```text
1. validate query completeness
2. collect current canonical candidates with matching action/scope/time
3. verify required source freshness/availability
4. apply scoped relation closure
5. evaluate qualified joint-authority declarations only when present
6. determine ordered governing set
7. activate governing-procedure constraint IDs
8. emit resolved or fail-visible receipt
```

Relation behavior should stay source-owned:

```text
REPLACE       removes predecessor only in the overlapping governed scope
SUPPLEMENT    retains predecessor and adds relation owner in deterministic order
SPECIALIZE    relation owner governs the narrower matching scope
CORRECT       relation owner replaces incorrect predecessor content in declared scope
```

Optional retrieval nominations may influence candidate discovery outside the resolver but must never alter resolver disposition.

## 11. Workstream engine

Represent workstreams as immutable snapshots plus pure transition/evaluation functions.

Keep repository writes outside `workstreams.py`.

Required mechanics:

```text
DAG validation
parent/child and multi-dependency relationships
ACTIVE / PAUSED / BLOCKED / COMPLETED / SUPERSEDED
pause reason + return condition + resume target
route projection
interruption recovery from durable action receipts
compare-and-swap style expected-revision checks
```

A stale update returns a rejection plus actual revision and proposed patch metadata, with no mutated successor snapshot.

## 12. Derived-view build architecture

The most important production simplification is that full rebuild and incremental refresh should share the same pure view builders.

Use a build model equivalent to:

```text
RepositorySnapshot
    parsed semantic sources + exact revisions

ViewSpec
    view ID
    dependencies / relevant profile kinds
    deterministic builder
    serializer

BuildGraph
    source -> affected view edges

build(snapshot, selected_views)
    same function for full and incremental operation
```

Full rebuild selects all views.

Incremental refresh computes the affected view set from changed semantic sources, then calls the exact same builders against the current repository snapshot. It should not have separate incremental business logic capable of drifting from full rebuild semantics.

If dependency impact is uncertain, select more views or fall back to full rebuild.

## 13. Persistent derived views

For W0, persist only the views required by Specification 028. Do not add more merely because they are cheap to generate.

Each view payload should be deterministic and contain no refresh timestamp. Operational timing belongs in an execution receipt or manifest field excluded from semantic/byte equality if needed.

A manifest should bind:

```text
view ID/path/schema
ordered exact source input bindings
hash basis + content digest
generator identity/version
output digest
rebuildability class
```

The generator implementation digest should be stable and explicit enough to invalidate stale views after relevant code changes.

## 14. Reconstruction planner

Keep the core planner deterministic by accepting an explicit structured task specification. Do not require W0 to solve arbitrary free-text intent classification.

Input can contain:

```text
task_class
subjects/domains
requested action + scope when governed
consequence class
known workstream context
```

The planner then combines:

```text
current-state core
source catalog
subject index
workstream graph
risk/obligation index
authority resolver when action-shaped
```

and emits must-load, optional, negative/do-not-load and freshness/receipt requirements.

A model may later help translate free text into this task specification, but the safe reconstruction closure remains project-controlled.

## 15. The recent Claude-history forgetting failure

The observed failure should be treated as evidence, but not as a command to invent another registry.

Important correction after inspecting current authority:

```text
docs/README.md already explicitly describes docs/model_collaboration/
docs/CONTINUITY.md already makes docs/README.md a mandatory early bootstrap read
docs/CONTINUITY.md already defines reconstruction of active collaboration threads
```

Therefore the failure does **not** prove the current architecture lacks a repository topology description. It demonstrates that available structural knowledge was not sufficiently activated/used in the actual reasoning path.

The W0 design should test the broader requirement:

> Given a task about architecture design and whether Claude has already contributed, can task-shaped reconstruction surface the model-collaboration region and the relevant MC thread lineage without the human naming the folder?

Preferred first hypothesis: Candidate 01's existing source catalog + subject index + current/workstream/risk views + reconstruction planner are sufficient. Do not create a new canonical `semantic_topology_registry` unless that hypothesis fails.

Professional architecture documentation may provide the human-readable whole-system self-model; machine reconstruction should derive task-relevant routes from canonical semantic declarations and generated indexes rather than parse the diagram as authority.

## 16. Capture and promotion

Model capture/promotion as an explicit plan/receipt workflow.

W0 should implement:

```text
validate capture is non-authoritative
construct PromotionPlan
require review disposition
resolve natural target owner
bind expected target revision
produce prospective change/receipt metadata
```

W0 should not need to perform an actual canonical promotion.

Do not implement promotion as `capture.authority_class = canonical`.

## 17. Validation architecture

Use structured diagnostics rather than boolean-only validation.

Each finding should include:

```text
code
severity
source path / semantic ID when available
message
related sources
suggested human remediation when useful
```

Validation should have composable passes:

```text
local declaration/schema
cross-source identity/relation
workstream graph
public/private
revision/freshness
view-manifest/build parity
```

The CLI should aggregate findings without embedding domain logic in argument handlers.

## 18. CLI architecture

`cli.py` should translate arguments into application functions and render human/JSON output.

Preferred W0 behavior:

```text
validate          read-only
check-freshness   read-only
rebuild           stage by default; explicit write flag if persistent outputs are requested
refresh           stage by default; explicit write flag
resolve-authority read-only receipt
reconstruct       read-only contract
migration-audit   read-only during W0
```

Canonical semantic sources are never auto-mutated by these commands.

## 19. Architecture documentation / visualization

Use text-native diagram sources during W0, preferably Mermaid unless independent review exposes a concrete deficiency.

Repository shape:

```text
docs/project_knowledge/architecture/
    README.md
    whole_architecture.md
    semantic_authority_model.md
    knowledge_lifecycle.md
    reconstruction_and_action.md
    migration_and_cutover.md
    diagrams/
        whole_architecture.mmd
        semantic_authority.mmd
        knowledge_lifecycle.mmd
        reconstruction_action.mmd
        migration_cutover.mmd
```

The whole-architecture diagram should show logical layers and boundaries, not every Python module. Focused diagrams may show the physical realization where useful.

Rendered SVG should wait until the source stabilizes or a deterministic renderer is deliberately added. GitHub-native Mermaid rendering is sufficient for W0 source review.

## 20. Test architecture

Use production API tests, not wrappers around research scripts.

Preferred organization:

```text
tests/fixtures/project_knowledge/
tests/unit/test_project_knowledge_declaration.py
tests/unit/test_project_knowledge_schemas.py
tests/unit/test_project_knowledge_identity.py
tests/unit/test_project_knowledge_authority.py
tests/unit/test_project_knowledge_workstreams.py
tests/unit/test_project_knowledge_views.py
tests/unit/test_project_knowledge_reconstruction.py
tests/unit/test_project_knowledge_capture.py
tests/unit/test_project_knowledge_cli.py
```

Qualified research cases should be translated into fixture scenarios whose expected semantics come from the frozen contracts, not imported by executing the old probes.

## 21. Strongest risks in this design

The main risk is accidental framework growth before W1 gives real canonical-source pressure. The shallow package and fixture corpus could look clean while real source diversity later forces abstraction changes.

The response should be reversibility:

```text
keep W0 interfaces small
avoid persistent databases
avoid universal base object classes
avoid clever scope languages
avoid premature plugin architecture
keep fixture-to-production transition explicit
```

A second risk is source discovery accidentally becoming a slow repository-wide scan. Incremental refresh and tracked-file filtering should address ordinary use, while periodic full rebuild may remain history/size proportional without violating bounded task reconstruction.

## 22. Questions intentionally left for independent Claude design

The highest-value comparative questions are:

```text
flat responsibility modules vs a layered package
tracked-tree marker scanning vs another source-discovery contract
scope representation and matching semantics
whether all eight persistent derived views should be committed
manifest/generator versioning details
how incremental dependency impact should be represented
whether Mermaid is the right durable diagram source
whether reconstruction needs an explicit repository-semantic-region concept
whether Specification 028 over-constrains any implementation choice
whether another W0 gate is needed for architecture-history activation/self-reconstruction
```

## 23. Frozen ChatGPT position

```text
CHATGPT_W0_DESIGN=FROZEN
INDEPENDENT_BASE=1f09fc812e8d7b1f31771a8b545864b76ea61db0
CLAUDE_HAS_NOT_SEEN_THIS_DESIGN=REQUIRED_UNTIL_MC0017_MESSAGE_001
PREFERRED_IMPLEMENTATION_STYLE=SHALLOW_DETERMINISTIC_REPOSITORY_LOCAL_TOOLING
NEW_TOPOLOGY_REGISTRY=NOT_JUSTIFIED_BY_CURRENT_EVIDENCE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=MC0017_CLAUDE_INDEPENDENT_W0_DESIGN
```
