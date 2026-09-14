# Portable External-Provider Packet V0.1

**Status:** FROZEN DERIVED CONSUMPTION PACKET / NOT PROJECT AUTHORITY
**Packet ID:** `PKA-C01-Q1-Q2-CROSS-PROVIDER-V01`
**Exact source base:** `a685ef48c4c4853babff9295f03f198c7b3dcd1d`
**Purpose:** Test whether Candidate 01 authority semantics remain reconstructable by a capable non-OpenAI provider/tool without prior ADS conversation context.

## Authority rule

This packet is a bounded derived view over exact repository sources. It is not itself a new authority source. The following Candidate 01 rules govern interpretation:

1. Probabilistic retrieval may nominate candidates but cannot silently make the final governing decision when explicit authority semantics exist.
2. `REPLACE` means the successor fully replaces the predecessor for the declared scope.
3. A partially superseded source may retain explicit outcomes or residual applicability outside the replaced scope.
4. If the requested scope is insufficient to resolve which authority relationship applies, the result must remain visibly unresolved rather than choosing the highest-ranked retrieved source.
5. A derived/search ranking cannot override explicit source-local lifecycle and relation semantics.

## Exact source bindings

```json
[
  {
    "source_key": "decisions",
    "path": "docs/DECISIONS.md",
    "bytes": 45566,
    "sha256": "2db2b79712c9333159aca2985f4be75a34d7b8357610714eca299a5f0597e4cd",
    "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
    "source_commit": "a685ef48c4c4853babff9295f03f198c7b3dcd1d",
    "source_class": "current_decision_authority"
  },
  {
    "source_key": "d011_shadow",
    "path": "docs/research/project_knowledge_candidate_01_q3_real_v01/SHADOW_DECISION_D011.md",
    "bytes": 1136,
    "sha256": "7ce4e736d21615cbd84dcf48447c031f1e5cab78457c5efa0a8c8d1a321f0e5f",
    "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
    "source_commit": "a685ef48c4c4853babff9295f03f198c7b3dcd1d",
    "source_class": "qualified_candidate_shadow"
  },
  {
    "source_key": "d015_shadow",
    "path": "docs/research/project_knowledge_candidate_01_q3_real_v01/SHADOW_DECISION_D015.md",
    "bytes": 749,
    "sha256": "86e4535fefdf6f6bbb519724a86c7c2d538ddf3b1ac581e7225a191d49800b46",
    "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
    "source_commit": "a685ef48c4c4853babff9295f03f198c7b3dcd1d",
    "source_class": "qualified_candidate_shadow"
  },
  {
    "source_key": "candidate144",
    "path": "docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md",
    "bytes": 62349,
    "sha256": "37b911abf32260c29262a2ab70f274192114c87c3e23a5e85d2bfa27042a1f3a",
    "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
    "source_commit": "a685ef48c4c4853babff9295f03f198c7b3dcd1d",
    "source_class": "candidate_architecture"
  },
  {
    "source_key": "research171",
    "path": "docs/research/171_whole_architecture_evidence_reconciliation_v03_final_pre_q10_gap_selection.md",
    "bytes": 5076,
    "sha256": "58daf0a521e999bf6590c9e228b6980e9074cab074fcadb93b8e1ac7b7dec7a2",
    "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
    "source_commit": "a685ef48c4c4853babff9295f03f198c7b3dcd1d",
    "source_class": "qualification_plan"
  }
]
```

## Candidate 01 relation declaration: D-011

The qualified Candidate 01 shadow declaration for D-011 states:

```json
{
  "semantic_id": "D-011",
  "epistemic_state": "PARTIALLY_SUPERSEDED",
  "relations": [
    {"mode":"REPLACE","target":"D-028","scope":"v1_persistence_retrieval_architecture"},
    {"mode":"REPLACE","target":"D-029","scope":"persistence_tooling"},
    {"mode":"REPLACE","target":"D-030","scope":"python_project_dependency_tooling"},
    {"mode":"REPLACE","target":"D-031","scope":"reusable_knowledge_interchange"},
    {"mode":"REPLACE","target":"D-032","scope":"initial_reasoning_runtime"},
    {"mode":"REPLACE","target":"D-033","scope":"source_universe_substrate"}
  ],
  "residual_applicability": "implementation_subsystems_not_yet_selected"
}
```

## Candidate 01 relation declaration: D-015

```json
{
  "semantic_id": "D-015",
  "epistemic_state": "PARTIALLY_SUPERSEDED",
  "relations": [{"mode":"REPLACE","target":"D-033","scope":"external_source_architecture_uncertainty"}],
  "retained_outcomes": ["public_git_source_binary_exclusion"]
}
```

## Canonical decision excerpts

### D-011

## D-011. Do not select the implementation architecture yet

**Status:** Superseded for the V1 persistence/retrieval architecture by D-028, persistence tooling by D-029, Python project/dependency tooling by D-030, reusable-knowledge interchange by D-031, initial reasoning runtime by D-032, and source-universe substrate by D-033; still applicable to implementation subsystems not yet selected
**Date:** 2026-08-07
**Superseded in scope:** 2026-08-20, 2026-08-22, and 2026-08-25

The project will not yet choose an agent framework, number of agents, LLM providers, orchestration framework, database, graph technology, rule engine, execution architecture, or other implementation stack.

### Rationale

Selecting technology before the system's goals, requirements, reasoning model, and evaluation criteria are sufficiently understood would create premature constraints.

### D-015

## D-015. Keep the currently attached learning materials outside the repository for now

**Status:** Superseded in architectural-uncertainty scope by D-033; durable public-Git exclusion outcome retained
**Date:** 2026-08-07
**Superseded in scope:** 2026-08-25

The machine learning and time-series/econometrics source materials currently available in the ChatGPT project were not copied into the GitHub repository while the project had no accepted external-source architecture.

### Rationale

At the time of this decision, the project had not decided how external knowledge sources, course material, references, or derived knowledge modules should be stored permanently. Copying material then would have prematurely defined a source architecture.

Foundation 021, Specification 023, Checkpoint 196, and D-033 now resolve that architectural uncertainty. The original conservative outcome remains: source binaries do not belong in the public Git repository merely because ADS uses them.

### D-028

## D-028. Use a SQLite-centered local-first architecture for V1 methodological knowledge and project state

**Status:** Accepted for V1
**Date:** 2026-08-20

V1 will use a SQLite-centered local-first operational architecture for reusable methodological knowledge metadata/state and project metadata/state.

The accepted architecture direction is:

```text
SQLite operational store
    stable knowledge identities and revisions
    components / relations / conditional rules
    provenance / governance
    project epistemic and decision objects
    project references to exact knowledge revisions
    execution-capability metadata

SQLite FTS5
    rebuildable lexical search index

rebuildable embeddings
    initial in-process exact semantic similarity search

application-layer rule evaluator
    minimal TRUE / FALSE / UNKNOWN conditional semantics

selective LLM context assembly
    bounded projection of project state + methodological horizon

filesystem / Git / artifact storage
    code and large generated/input artifacts outside SQLite
```

V1 will **not** introduce a dedicated graph database, vector database/service, external rules engine, or PostgreSQL server unless measured requirements justify the additional complexity.

The relational design must preserve a credible migration path to PostgreSQL. PostgreSQL, with pgvector where appropriate, is the preferred first migration family if future multi-writer, shared-server, concurrency, or semantic-index scale requirements exceed the SQLite envelope.

Human-readable deterministic exports of accepted reusable knowledge must remain available for review, diffing, debugging, backup/migration testing, and optional Git preservation. These exports and rebuildable indexes are not competing runtime authorities.

Large datasets, trained models, arrays, notebooks, and other large artifacts remain outside the operational metadata database; SQLite stores metadata, provenance, and references to them.

### Rationale

Foundations 017 through 020 and Checkpoint 107 now provide the product model, methodological-horizon architecture, reusable-knowledge representation, and technology-neutral implementation requirements that D-011 intentionally waited for.

Architecture comparison in Checkpoint 108 found that SQLite satisfies the current V1 requirement envelope with the lowest operational burden. SQLite provides transactional relational state, foreign-key integrity, FTS5, recursive CTEs for bounded relationship traversal, JSON support, and WAL-based reader/writer concurrency compatible with the accepted initial one-writer model.

A targeted synthetic viability spike also found no order-of-magnitude performance reason to introduce specialized stores at the expected V1 scale. Exact in-process vector similarity over the expected methodological-knowledge scale was comfortably feasible in the spike, so ANN/vector-server infrastructure is currently unnecessary.

PostgreSQL + pgvector is technically stronger for multi-user concurrency and larger integrated vector workloads, but V1 does not currently require the server/extension operational surface. Neo4j is capable of graph and vector workloads, but the current requirement is bounded local traversal rather than graph analytics as a dominant workload. Multi-store architectures introduce consistency and operational boundaries without current evidence of need.

This decision is deliberately scoped to V1. It is not a claim that SQLite is the final database for the complete long-term product.

See:

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
experiments/architecture_spikes/sqlite_v1_viability.py
```

### D-033

## D-033. Use an ADS-owned private source universe substrate for external evidence artifacts

**Status:** Accepted for V1
**Date:** 2026-08-25

V1 will preserve external evidence artifacts through an ADS-owned Source Universe substrate that is distinct from reusable methodological knowledge.

The accepted initial architecture is:

```text
user-controlled private SourceArtifactStore
    exact immutable source bytes
    SHA-256 content addressing
    no filename-based artifact identity

relational Source Registry
    logical Source identity
    exact SourceArtifact identity
    SourceCollection / membership
    uncertainty-preserving association state
    locators and ingestion events
    rights / access metadata
    bounded derived-artifact lineage

provider-neutral backup / restore
    deterministic PRIVATE_SNAPSHOT
    verified exact object payload
    clean-target restore
    full integrity audit

public Git repository
    code, schemas, policies, manifests, safe validation evidence,
    and explicitly public-safe metadata only
```

The first storage adapter is a local filesystem content-addressed store behind an ADS-owned `SourceArtifactStore` boundary. The physical vault root is configuration, not domain identity, and the architecture does not depend on that local adapter remaining the final backend.

Source binaries, private observed paths, private registry snapshots, backup payloads, and material with unknown redistribution rights must not be placed in the public repository merely because ADS consumes them.

ChatGPT Library, ChatGPT Project Sources, Google Drive, OneDrive, and similar services may be useful intake, synchronization, backup, or development surfaces. They are not the semantic source authority unless a future explicit architecture decision changes that boundary.

The Source Universe does not itself create accepted methodological knowledge. Source evidence must pass through the separate knowledge extraction, provenance, review, and governance boundaries before reusable methodological authority is created.

### Rationale

Foundation 021 and Specification 023 distinguish logical sources from exact byte artifacts, collection membership from artifact identity, original evidence from rebuildable derived representations, and source support from accepted knowledge.

The provider-free implementation passed the prospectively frozen SU-G01 through SU-G23 gate set on Ubuntu and Windows. The first 20-file VU Amsterdam Machine Learning corpus matched its prospectively recorded hashes, ingested as 20 exact artifacts, preserved fourteen real duplicate re-encounters as extra ingestion events without duplicate artifact rows or stored objects, retained uncertain course associations without strengthening them, passed clean integrity audit, and completed verified backup plus clean restore with exact semantic registry equality and 20/20 restored objects passing integrity verification.

This evidence resolves the source-architecture uncertainty that motivated D-015 while retaining D-015's conservative outcome that educational source binaries do not belong in the public Git repository.

See:

```text
docs/foundations/021_source_universe_artifact_integrity_and_evidence_provenance.md
docs/research/034_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
```

## Probabilistic retrieval nominations

The following rankings are deliberately plausible and potentially misleading. They are derived evidence-access hints only.

```json
{
  "TASK_A": {
    "query": "Which decision governs the V1 persistence/retrieval architecture?",
    "candidates": [
      {
        "rank": 1,
        "semantic_id": "D-011",
        "score": 0.96,
        "reason": "strong lexical match to implementation architecture selection"
      },
      {
        "rank": 2,
        "semantic_id": "D-028",
        "score": 0.91,
        "reason": "explicit V1 persistence/retrieval architecture decision"
      },
      {
        "rank": 3,
        "semantic_id": "D-029",
        "score": 0.66,
        "reason": "persistence tooling adjacency"
      }
    ]
  },
  "TASK_B": {
    "query": "Which implementation architecture decision governs?",
    "candidates": [
      {
        "rank": 1,
        "semantic_id": "D-011",
        "score": 0.95,
        "reason": "generic implementation architecture language"
      },
      {
        "rank": 2,
        "semantic_id": "D-028",
        "score": 0.9,
        "reason": "selected persistence/retrieval architecture"
      },
      {
        "rank": 3,
        "semantic_id": "D-033",
        "score": 0.86,
        "reason": "selected source-universe substrate"
      },
      {
        "rank": 4,
        "semantic_id": "D-032",
        "score": 0.82,
        "reason": "selected initial reasoning runtime"
      }
    ]
  },
  "TASK_C": {
    "query": "What governs external learning-source architecture and may source binaries go into public Git?",
    "candidates": [
      {
        "rank": 1,
        "semantic_id": "D-015",
        "score": 0.97,
        "reason": "direct learning-material/public repository language"
      },
      {
        "rank": 2,
        "semantic_id": "D-033",
        "score": 0.93,
        "reason": "accepted external source-universe architecture"
      }
    ]
  }
}
```

## Tasks

### Task A: scoped replacement versus retrieval rank

Question: **Which decision governs the V1 persistence/retrieval architecture?**

Return the governing semantic ID(s), explain the lifecycle/relation reason, and state whether the top retrieval candidate determined authority.

### Task B: under-specified scope / conflict visibility

Question: **Which implementation architecture decision governs?**

The question intentionally omits a subsystem/scope. Do not invent one. Determine whether the packet supplies enough explicit semantics to select one governing decision. If not, fail visibly and state what information is missing.

### Task C: partial supersession with retained outcome

Question: **What governs external learning-source architecture, and may ADS place source binaries in the public Git repository merely because ADS consumes them?**

Distinguish the current architecture decision from any retained outcome of an older partially superseded decision.

## Output schema

Return exactly one JSON object and no prose outside it:

```json
{
  "provider": "<provider>",
  "model": "<exact model name shown in your UI/API>",
  "fresh_session": true,
  "prior_ads_context": false,
  "packet_id": "PKA-C01-Q1-Q2-CROSS-PROVIDER-V01",
  "task_a": {
    "resolution_status": "<string>",
    "governing_ids": ["<id>"],
    "retrieval_used_as_authority": false,
    "reason": "<concise reason>"
  },
  "task_b": {
    "resolution_status": "<string>",
    "governing_ids": [],
    "retrieval_used_as_authority": false,
    "missing_scope_or_conflict": "<concise statement>"
  },
  "task_c": {
    "resolution_status": "<string>",
    "governing_architecture_ids": ["<id>"],
    "retained_outcomes": ["<outcome id>"],
    "public_git_source_binaries_allowed_merely_because_ads_consumes_them": false,
    "retrieval_used_as_authority": false,
    "reason": "<concise reason>"
  },
  "authority_receipt": {
    "source_base_commit": "a685ef48c4c4853babff9295f03f198c7b3dcd1d",
    "source_ids_considered": ["<id>", "..."],
    "retrieval_is_non_authoritative": true,
    "unresolved_items": ["<item>", "..."]
  }
}
```
