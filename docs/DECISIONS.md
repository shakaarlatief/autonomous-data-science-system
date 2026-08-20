# Decisions

This document records explicit project-level decisions that have already been made.

A decision is stronger than an idea or design hypothesis. Decisions may still be revised later, but revisions should be explicit and should preserve the history of what changed and why.

## D-001. Create a dedicated project separate from individual data projects

**Status:** Accepted  
**Date:** 2026-08-07

The Autonomous Data Science System is maintained as its own project rather than inside the existing collection of individual data projects.

### Rationale

The system sits conceptually above individual projects. Individual projects may later be used to test, develop, and improve the system, but they are not the same artifact.

---

## D-002. Use a dedicated GitHub repository as the persistent home of the project

**Status:** Accepted  
**Date:** 2026-08-07

The repository `autonomous-data-science-system` is the persistent home of the project.

### Rationale

A project of this scope cannot safely depend on long chat histories or model memory. Version-controlled files provide durable state, provenance, history, and a way for future sessions or models to reconstruct the project.

---

## D-003. Keep the repository private during the early design stage

**Status:** Superseded in current repository state; the repository is now public  
**Date:** 2026-08-07  
**Superseded in scope:** By 2026-08-20; the exact visibility-change decision/date is not preserved in this decision record

The repository was kept private during the early design stage. The current GitHub repository is public, so this early-stage visibility decision no longer describes present repository state.

### Rationale

The project was highly exploratory and many ideas were intentionally provisional. Public presentation was explicitly left open for reconsideration once the structure and goals became more mature.

This reconciliation records the observable current visibility without inventing an unpreserved rationale or exact transition date for the later change.

---

## D-004. Treat chat as the design workspace and the repository as the source of truth

**Status:** Accepted  
**Date:** 2026-08-07

Free-form discussion can continue in chat, but stable project knowledge must be extracted into repository artifacts.

### Rationale

Chat is effective for exploration but unreliable as permanent project memory. Repository artifacts make continuity deliberate rather than accidental.

---

## D-005. Preserve important knowledge at multiple levels of detail

**Status:** Accepted  
**Date:** 2026-08-07

The project will preserve both concise canonical knowledge and detailed foundational reasoning.

### Rationale

Aggressive summarization can destroy important motivations, examples, distinctions, and reasoning. Keeping only raw conversations creates the opposite problem: too much unstructured material for efficient future use.

The current solution is layered preservation.

---

## D-006. Foundational design memos are first-class project artifacts

**Status:** Accepted  
**Date:** 2026-08-07

Important early discussions may be reconstructed into long-form design memos rather than compressed into only short principles or decisions.

### Rationale

Some of the earliest reasoning defines the intellectual foundation of the project. The reasoning itself may later be needed to challenge, revise, or understand an architectural choice.

---

## D-007. Historical conversation material is not automatically canonical

**Status:** Accepted  
**Date:** 2026-08-07

If raw conversations are archived later, they will be treated as historical provenance rather than the authoritative current specification.

### Rationale

Conversations contain speculative ideas, repetition, abandoned directions, and statements that may later become outdated.

---

## D-008. Establish an explicit new-chat continuity procedure

**Status:** Accepted  
**Date:** 2026-08-07

The project must support continuing in a new chat when the current conversation becomes too long or otherwise unusable.

A new session should reconstruct state from repository documents rather than requiring the user to manually explain the previous conversation.

### Rationale

Chat capacity is a predictable limitation and should be designed around from the beginning.

See `CONTINUITY.md`.

---

## D-009. Use checkpoints rather than trying to document every message immediately

**Status:** Accepted  
**Date:** 2026-08-07

Discussion should remain fluid. After substantial progress, a checkpoint should consolidate stable knowledge, detailed reasoning where necessary, open questions, and the next continuation point.

### Rationale

Updating many project files after every message would create excessive overhead and interfere with exploration. Checkpoints provide a practical balance between preservation and conversational flow.

---

## D-010. Treat the documentation methodology as provisional

**Status:** Accepted  
**Date:** 2026-08-07

The current repository structure and knowledge-preservation method are version 0.1, not a final architecture.

### Rationale

The project is expected to discover better ways to organize knowledge through actual use. The methodology for building the system should evolve in the same evidence-driven way as the target system.

---

## D-011. Do not select the implementation architecture yet

**Status:** Superseded for the V1 persistence/retrieval architecture by D-028, persistence tooling by D-029, and Python project/dependency tooling by D-030; still applicable to implementation subsystems not yet selected  
**Date:** 2026-08-07  
**Superseded in scope:** 2026-08-20

The project will not yet choose an agent framework, number of agents, LLM providers, orchestration framework, database, graph technology, rule engine, execution architecture, or other implementation stack.

### Rationale

Selecting technology before the system's goals, requirements, reasoning model, and evaluation criteria are sufficiently understood would create premature constraints.

---

## D-012. Do not attempt to design one complete fixed workflow for all data science projects

**Status:** Accepted at the conceptual level  
**Date:** 2026-08-07

The project rejects the idea that one globally fixed linear pipeline can adequately represent all data science projects.

### Rationale

Different projects require different questions, validation designs, assumptions, analyses, and modelling approaches. Findings discovered later may also require returning to earlier stages.

This decision does not yet specify the final alternative architecture.

---

## D-013. Use real projects to develop and test the system

**Status:** Accepted  
**Date:** 2026-08-07

Real or realistic data projects will be used as coverage tests for the system.

### Rationale

Trying to enumerate the complete universe of data science reasoning in advance is unlikely to succeed. Projects can expose missing questions, weak branches, unnecessary work, bad assumptions, and interactions that were not anticipated.

---

## D-014. Generalize project lessons when appropriate

**Status:** Accepted  
**Date:** 2026-08-07

When a project exposes a missing capability or reasoning failure, the system should determine whether the lesson is generalizable. If so, it should be incorporated into reusable system knowledge or process rather than patched only in that project.

### Rationale

This turns each project into both an analytical task and a source of system improvement.

---

## D-015. Keep the currently attached learning materials outside the repository for now

**Status:** Accepted for the current stage  
**Date:** 2026-08-07

The machine learning and time-series/econometrics source materials currently available in the ChatGPT project are not being copied into the GitHub repository yet.

### Rationale

The project has not decided how external knowledge sources, course material, references, or derived knowledge modules should be stored permanently. Copying material now would prematurely define a source architecture.

---

## D-016. Create Checkpoint 0 before continuing deeper system design

**Status:** Accepted and executed  
**Date:** 2026-08-07

The first repository artifacts capture the state reached during the initial design conversation before continuing to the next conceptual question.

### Rationale

The initial conversation already contains foundational ideas that should not be allowed to disappear as the chat grows.

---

## D-017. Define the primary purpose in project-relative terms

**Status:** Accepted  
**Date:** 2026-08-08

The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective of the system.

### Rationale

Different projects legitimately require different balances. A research project, production project, rapid exploratory analysis, learning-focused portfolio project, and high-stakes analytical project should not all optimize the same process characteristics.

Autonomy and predictive performance remain important capabilities, but they are means that should serve project intent rather than universal ends.

This decision does not yet define the exact project-intent schema or the non-negotiable methodological standards that must hold across all project profiles.

---

## D-018. Make checkpoint detection a proactive AI responsibility

**Status:** Accepted  
**Date:** 2026-08-08

The AI design collaborator should decide when repository preservation or a checkpoint is warranted during an active design conversation. The user should not need to request every update manually.

The AI should preserve material when substantial conceptual progress, a major transition, continuity risk, or another natural checkpoint makes preservation more valuable than further uninterrupted discussion.

### Rationale

The user should be able to focus on the substance of the project rather than on remembering when documentation maintenance is due. The repository is intended to protect the project from conversational loss, so the design collaborator should actively manage that continuity risk.

This does not authorize automatic promotion of ideas into accepted decisions. Maturity distinctions must still be respected.

See `DEVELOPMENT_METHOD.md` version 0.2.

---

## D-019. Use numbered, content-specific design-session names

**Status:** Accepted  
**Date:** 2026-08-08

Chats inside the `Autonomous Data Science System` ChatGPT project use the convention:

```text
NN - Main Topic / Stage
```

The sequence number preserves chronology and the content-specific title makes earlier sessions easier to locate.

### Rationale

A purely numbered convention becomes difficult to navigate as the project grows, while completely free-form names obscure chronological order. The hybrid convention provides both.

Session names are provenance and navigation metadata only. The repository must not depend on a chat retaining a specific title, and a single chat may contain multiple repository checkpoints.

---

## D-020. Make design-chat rotation a proactive AI responsibility

**Status:** Accepted  
**Date:** 2026-08-08

The AI design collaborator should decide when the active design conversation should move to a new chat. A new chat should be opened primarily because conversation capacity, context pressure, degraded continuity, or another practical session-boundary risk makes continuing in the current chat unsafe or inefficient, not merely because the conceptual subject changes or a new checkpoint is reached.

A single chat may therefore span many topics and many repository checkpoints when continuity remains healthy.

Before recommending a new chat, the AI should normally ensure that material reasoning has been preserved, `CURRENT_STATE.md` and the relevant canonical documents are current, and the next step is explicit. It should then give the user a suitable numbered, content-specific chat title and a minimal continuation instruction. The user should not need to manually reconstruct or re-explain the project.

The AI does not need an exact client-side context-limit meter to perform this responsibility. It should use the conversational context and continuity signals available to it and recommend rotation before meaningful context loss is likely. If a platform-specific limit becomes ambiguous and cannot otherwise be assessed, the AI may ask the user for relevant UI information, but screenshots should not be a routine requirement.

### Rationale

The goal of session management is reliable continuity, not creating many chats. Topic changes and checkpoints are useful documentation boundaries but are not, by themselves, reasons to fragment the working conversation. Proactive session rotation reduces the risk of reaching a context boundary unexpectedly and then requiring the user to recover the project manually.

See `CONTINUITY.md`.

---

## D-021. Add an explicit promotion audit to substantive checkpoints

**Status:** Accepted  
**Date:** 2026-08-18

Every substantive checkpoint should explicitly determine whether any newly stabilized material deserves promotion into a more durable current layer such as a canonical document, foundation, specification, experiment ledger, knowledge-map route, or major-change entry.

No promotion is a valid outcome.

### Rationale

Checkpoint 22 demonstrated that knowledge can be physically durable but conceptually buried. The system-level vision remained safely stored in Git, yet its importance still depended on someone remembering that the checkpoint existed.

The promotion audit turns that failure mode into an explicit process responsibility rather than relying on human memory.

See `DEVELOPMENT_METHOD.md` version 0.3 and Foundation 014.

---

## D-022. Maintain a knowledge map as a routing layer

**Status:** Accepted  
**Date:** 2026-08-18

The repository will maintain:

```text
docs/KNOWLEDGE_MAP.md
```

as a concise routing/index layer that points to current canonical knowledge, detailed foundational reasoning, frozen specifications, active experiment ledgers, and important historical origins.

The knowledge map does not become another copy of the substantive knowledge.

### Rationale

As the number of foundations, checkpoints, experiments, and prototypes increases, Git history alone does not answer where the authoritative explanation of a concept lives.

A routing layer improves discoverability without introducing a database or duplicating every document.

---

## D-023. Perform periodic knowledge reconciliation and separate current state from detailed experiment ledgers

**Status:** Accepted  
**Date:** 2026-08-18

At meaningful stage boundaries, the project should reconcile canonical documents, foundations, decisions, open questions, routing, current state, and experiment records for stale, duplicated, contradictory, or unpromoted knowledge.

`docs/CURRENT_STATE.md` should remain concise and present-tense. Long-running detailed experiment mechanics should live in experiment-specific ledgers such as:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

### Rationale

The held-out experiment caused `CURRENT_STATE.md` to accumulate detailed run histories already preserved elsewhere. Separating navigation from the detailed ledger reduces duplication and improves new-session reconstruction.

See Foundation 014 and Development Method v0.3.

---

## D-024. Keep Git and Markdown as the current preservation substrate and defer advanced knowledge infrastructure

**Status:** Accepted for the current stage  
**Date:** 2026-08-18

The project will not currently introduce a graph database, vector database, ontology service, automatic summarization pipeline, or similar preservation infrastructure merely because the repository is growing.

Potential future upgrades such as machine-readable metadata, semantic retrieval, generated indexes, contradiction detection, dependency graphs, promotion queues, and reconciliation assistants are explicitly preserved as future options.

### Rationale

The demonstrated failure is currently about semantic lifecycle management: discoverability, promotion, authority, and reconciliation. It is not yet a storage-capacity problem.

More advanced infrastructure should be introduced only when observed retrieval, dependency, consistency, concurrency, or automation problems justify its cost and complexity.

See `docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`.

---

## D-025. Maintain a selective major-changes ledger

**Status:** Accepted  
**Date:** 2026-08-18

The project will maintain:

```text
docs/MAJOR_CHANGES.md
```

for major architectural, methodological, evaluation, preservation, repository, and experimental-phase changes that future sessions should be able to discover quickly.

It is intentionally selective and does not replace Git history or detailed checkpoints.

### Rationale

Git records every implementation change, while checkpoints record many local milestones. Neither by itself gives a concise conceptual history of the few structural changes that materially altered how the project operates.

---

## D-026. Use the retrospectively validated held-out supervisor for remaining Prototype V0 execution

**Status:** Accepted and frozen for Prototype V0 operational use  
**Date:** 2026-08-18

The remaining Prototype V0 held-out treatment attempts may be launched through the external condition-neutral supervisor implemented in:

```text
prototype_v0/src/ads_v0/heldout_supervisor.py
prototype_v0/src/ads_v0/heldout_verifier.py
```

The supervisor must continue to delegate every paid treatment attempt to the unchanged frozen `heldout_runner.execute_next_attempt()` path, preserve sequential preregistered order, preserve the registered replacement policy, and perform only external mechanical verification between attempts.

The validated implementation is frozen for the remainder of held-out execution unless a genuine condition-neutral infrastructure defect is discovered and handled transparently under the experiment's existing defect policy.

The first prospective batch is intentionally bounded to at most three paid model attempts. Later batch size may increase after the first live batch confirms that the supervisor behaves as validated.

### Rationale

The full test suite passed and the verifier retrospectively reproduced the established mechanical record for all 12 completed attempt directories with 12 integrity passes and zero integrity failures. This provides direct parity evidence against the manual process used for the first ten resolved slots while removing repeated human transport and bookkeeping.

This decision changes experiment operations, not treatment behavior, scoring, benchmarks, budgets, run order, semantic judging, or continuation/falsification criteria.

See Foundation 015 and Checkpoint 82.

---

## D-027. Allow large bounded unattended supervisor batches after the prospective smoke test

**Status:** Accepted for the remaining Prototype V0 treatment-execution phase  
**Date:** 2026-08-18

The initial three-paid-attempt prospective supervisor gate has passed. The validated supervisor may therefore be invoked with a substantially larger explicit paid-attempt allowance, including:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

The command remains bounded rather than unconditionally running 30 treatments. It must stop at `EXPERIMENT_COMPLETE` when all frozen treatment slots are resolved, at the explicit paid-attempt limit, or earlier on an existing supervisor/runner safety state such as mechanical integrity failure, interrupted attempt, or replacement exhaustion.

Prototype V0 remains strictly sequential. This decision does not authorize concurrency.

### Rationale

The first prospective live batch launched exactly three new attempts in frozen order, mechanically verified each one before advancing, produced 3 / 3 integrity PASS results, stopped exactly at the explicit batch limit, and derived the correct next frozen slot. After that batch, all 15 completed attempt directories had verifier integrity PASS and zero had integrity failure.

The operational evidence now consists of 77 passing software tests, 12 / 12 retrospective verification passes before live use, and 3 / 3 prospective live verification passes. Continuing to require artificial three-attempt batches would preserve human waiting and transport without a demonstrated integrity benefit.

This decision changes only how many already-validated sequential supervisor iterations may occur inside one invocation. It does not change the experiment plan, treatments, budgets, replacement rules, scoring, or semantic evaluation.

See Foundation 015 and Checkpoint 83.

---

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

---

## D-029. Use SQLAlchemy Core and Alembic for V1 persistence implementation

**Status:** Accepted for V1  
**Date:** 2026-08-20

V1 persistence adapters will use **SQLAlchemy Core 2.0 stable-series APIs** for relational schema/query/transaction integration and **Alembic 1.x** for ordered schema migration history.

SQLAlchemy ORM will not be the primary V1 domain/persistence model. Raw DBAPI/direct SQL will not be the normal repository implementation style, but remains allowed inside narrowly scoped adapter or migration code for genuinely backend-specific behavior such as SQLite PRAGMAs or FTS5.

The implementation must preserve the boundaries defined by Specification 001:

```text
domain/application semantics
    -> stable persistence ports
    -> SQLAlchemy Core adapter
    -> SQLite for V1
    -> PostgreSQL adapter later if requirements justify migration
```

Alembic revisions are the authoritative production schema-evolution path. `MetaData.create_all()` may support isolated tests/spikes but does not replace migration history for real V1 workspaces.

Alembic autogeneration may assist migration authoring but generated migrations must always be manually reviewed before acceptance.

The production schema must use deterministic constraint naming and preserve SQLite STRICT behavior during batch table recreation.

### Rationale

SQLAlchemy Core matches the accepted explicit relational architecture without requiring the database representation to become the domain object model. It provides schema metadata, explicit transactions, custom type adaptation, SQLite/PostgreSQL dialects, inspection, and conditional DDL while keeping application semantics behind ports.

A raw DBAPI-first approach would force the project to manually own dialect branching, type mapping, query construction, migration integration, schema metadata, and future PostgreSQL portability. The ORM is capable but introduces object/session identity and state-oriented unit-of-work semantics that are not required by the current explicit domain model and type-specific lifecycle architecture.

A committed dual-backend spike tested SQLAlchemy 2.0.52 + Alembic 1.19.0 on SQLite and PostgreSQL 18. It passed SQLite STRICT creation, connection-level foreign-key enforcement, transaction rollback, portable UUID mapping, dialect-isolated FTS DDL, real Alembic migration on both databases, and a forced SQLite batch recreation that preserved data, STRICT mode, and a named CHECK constraint.

SQLAlchemy 2.1 remains beta at this decision point, so V1 stays on the stable 2.0 API line until a later explicit dependency review.

See:

```text
docs/specifications/002_v1_persistence_tooling_standard.md
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
experiments/architecture_spikes/tooling_sqlalchemy_core_alembic_spike.py
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
```

---

## D-030. Use uv with standards-based pyproject metadata for the V1 Python project

**Status:** Accepted for V1  
**Date:** 2026-08-20

V1 will use `pyproject.toml` as the standards-based Python project/dependency declaration, `uv` as the project/dependency/environment manager, a committed `uv.lock` for reproducible cross-platform resolution, and `uv_build` as the current PEP 517 build backend for the pure-Python `ads_system` package.

The current validated tooling baseline is:

```text
uv 0.12.5
uv_build >=0.12.5,<0.13
Python >=3.12
```

The package is tested on Python 3.12, 3.13, and 3.14 on Linux and Windows.

The distribution/import names are:

```text
distribution: autonomous-data-science-system
import package: ads_system
```

The dependency intent remains in standard `pyproject.toml` metadata. `uv.lock` is committed but tool-managed, and uv's PEP 751 `pylock.toml` export is retained as an interoperability path. The project is not architecturally coupled to uv's lock format.

### Rationale

The first production persistence slice now depends on SQLAlchemy/Alembic and needs repeatable local/CI environments. Ad-hoc package installation would undermine the architecture's reproducibility goals.

uv provides one cross-platform workflow for locking, synchronization, Python selection, command execution, and package building while still consuming standard Python project metadata. A committed universal lockfile supports reproducible development and dependency upgrades. The build backend is replaceable through the standard PEP 517 boundary if future extension-module or packaging requirements change.

A committed project-tooling gate generated the lockfile and passed package import/tests/build plus PEP 751 export on Linux and Windows across Python 3.12-3.14.

See:

```text
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

---

## D-031. Use JSON plus JSON Schema and semantic validation for V1 reusable-knowledge interchange

**Status:** Accepted for V1  
**Date:** 2026-08-20

The canonical V1 reusable-methodological-knowledge interchange uses:

```text
standard JSON
    +
JSON Schema Draft 2020-12
    +
application-level semantic validation
    +
deterministic normalization and serialization
```

The operational database remains the runtime authority. Interchange files are human-reviewable, storage-neutral representations for review, diffing, seeding, migration verification, fixtures, and deterministic export. Rebuildable lexical and semantic indexes remain separate derived state.

Normal `CANDIDATE_SET` and `BENCHMARK_FIXTURE` import must not silently create accepted methodological authority. Accepted knowledge requires an explicit governance operation. `ACCEPTED_SNAPSHOT` import is restricted to a trusted restore/bootstrap/migration path.

The representative heterogeneous corpus is benchmark material and remains candidate-only unless knowledge is independently reviewed and explicitly accepted.

### Rationale

The interchange layer must preserve Foundation 020's distinction among assets, components, narrative facets, static relations, conditional rules, provenance, retrieval hints, applicability, and required context without making the SQLite physical schema the human authoring format.

JSON provides unambiguous parser behavior, mature cross-language support, deterministic serialization, and a natural representation for recursive rule conditions and heterogeneous typed knowledge. JSON Schema provides a formal structural contract, while application validation covers cross-object uniqueness, reference resolution, governance safety, and other semantic invariants that are not conveniently expressed as document-local schema constraints.

The committed KI-01 through KI-10 validation gate passed on Linux and Windows across Python 3.12, 3.13, and 3.14 using the ten-asset heterogeneous benchmark corpus. The pass includes deterministic byte-stable serialization, formatting-independent semantic digests, recursive condition validation, reference resolution, duplicate rejection, and candidate/accepted import-safety checks.

This decision does not select an embedding model, reranker, vector backend, authoring UI, complete knowledge taxonomy, or full provenance ontology.

See:

```text
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
experiments/architecture_spikes/V1_KNOWLEDGE_INTERCHANGE_RESULT.md
schemas/reusable_knowledge_bundle_v1.schema.json
```
