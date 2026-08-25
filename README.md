# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. Bounded V1 is constructing the serious methodological knowledge universe. Its prerequisite Source Universe substrate has been accepted and promoted. The permanent source-vault deployment is preserved but temporarily paused while the project pressure-tests a major Level-2 change: governed multi-model development collaboration between ChatGPT, Claude, and the human project owner.**

```text
checkpoint            201
active branch         v1-multimodel-development-collaboration
active PR             #76
promoted V1 head      8215718db3e44f000cc6ed53d6a051522d429dbd
latest specification  Specification 023
source outcome         SOURCE_SUBSTRATE_ACCEPTED
latest experiment      Specification 022
experiment outcome     INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary       MC-0001 bounded Phase D Claude challenge;
                       PR #75 source-vault bootstrap paused
```

The active collaboration route is:

```text
docs/checkpoints/201_mc_0001_phase_b_and_c_recorded_bounded_phase_d_challenge_opened.md
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/model_collaboration/threads/MC-0001/THREAD.md
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
```

GitHub Issue #77 is the optional live transport surface for `MC-0001`; the issue is collaboration transport, not canonical project authority.

The permanent source-vault route remains preserved on draft PR #75 and is not abandoned.

---

## Why multi-model collaboration is a first-class Level-2 problem

The existing repository already allows a new model or chat to reconstruct project state without depending on the previous conversation. That solves information continuity, but not coordination.

A safe multi-model development process must also answer:

```text
who owns a bounded task
who may mutate canonical state
how another model reviews without silently becoming co-owner
how independent judgment is preserved
how material disagreement remains visible
how the human arbitrates genuine project-intent conflicts
how model-to-model communication avoids constant user copy-paste
how collaboration provenance remains separate from authority
when automated API orchestration would actually earn its cost/complexity
```

Research 035 is the first ChatGPT-authored candidate architecture. It is **not** yet Development Method v0.5.

The first trial, `MC-0001`, used an independent-then-comparative Claude review. Claude's Phase A was independent from the full Research 035 memo and ChatGPT message 001, but Claude correctly identified that the required routing/current-state documents already exposed several candidate architecture ideas. Phase A is therefore partially independent rather than fully blind, and contaminated convergence is not counted as clean independent confirmation.

Claude then completed a full Phase-B comparative review. It materially improved the architecture by identifying a missing machine-checkable collaboration-state mechanism, strengthening contamination handling, operationalizing review intensity, refining transport/human-role choices, and challenging its own earlier defaults.

ChatGPT has now completed Phase C in `004_chatgpt_response_to_claude.md`. It accepts several Claude additions while rejecting blanket `risk-averse wins` and `narrow-scope wins` routing, distinguishing role from write scope, and preferring scoped per-thread write ownership over one global active-writer field.

The current next step is one bounded Claude Phase-D challenge on the remaining disagreements. The goal remains neither consensus nor disagreement. The goal is calibrated cross-model reasoning.

---

## Dedicated Model Collaboration Exchange

The candidate exchange lives at:

```text
docs/model_collaboration/
```

It separates:

```text
GitHub issue / PR comments
    optional low-friction transport

Model Collaboration Exchange
    durable structured collaboration provenance

normal accepted project artifacts
    authority after existing review/promotion governance
```

The candidate method uses one bounded task owner, serialized target-state writes, explicit task roles, append-only substantive review messages, explicit disagreement classification, and provider-neutral collaboration identities rather than permanently assigning one model as architect and another as reviewer.

A key new candidate requirement is machine-readable collaboration state before routine multi-model canonical development. The exact mechanism is not frozen. A single global active-writer field is currently considered too coarse; a per-thread model separating target-state ownership from allowed review-message surfaces is under discussion.

No automated OpenAI/Anthropic API orchestrator is being built at this stage.

---

## Why sources became a first-class subsystem

The project is preparing to ingest a large educational and external source corpus spanning machine learning, econometrics, statistics, optimization, mathematics, AI, time series, and related areas.

Those source artifacts are not themselves the methodological knowledge base.

The durable separation is:

```text
SOURCE UNIVERSE
    exact evidence artifacts and provenance

        !=

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable methodological reasoning
```

A PDF may support many knowledge propositions; one methodological proposition may be supported by several sources. Source identity, exact bytes, rights/access, provenance, extraction lineage, and knowledge acceptance therefore require separate governance.

---

## Accepted Source Universe substrate

Specification 023 provides the accepted bounded V1 path:

```text
filesystem source input
    -> exact SHA-256 + byte count
    -> staging
    -> immutable content-addressed SourceArtifactStore
    -> relational Source Registry
    -> collection / membership provenance
    -> deterministic PRIVATE_SNAPSHOT / PUBLIC_SAFE_CATALOG
    -> integrity audit
    -> verified provider-neutral backup
    -> clean restore
    -> restored integrity audit
```

The implemented identities include:

```text
SourceRecord
SourceArtifact
SourceCollection
SourceCollectionMembership
SourceLocator
SourceIngestionEvent
DerivedSourceArtifact
```

Source binaries live outside the public Git repository. ChatGPT Library, Project Sources, and cloud drives may help with intake or access, but none becomes semantic source authority merely by containing the file.

The physical backend is local-first behind an ADS-owned storage abstraction. A future object-store backend can therefore be introduced without redefining source identity.

---

## First real-corpus validation

The first controlled corpus was the 20-file VU Amsterdam Machine Learning batch supplied during Design Session 06.

Before implementation, exact SHA-256 and byte-size fingerprints were frozen in:

```text
docs/source_universe/intake_snapshots/001_vu_machine_learning_chat_intake.md
```

After implementation:

```text
20 / 20 files matched prospective fingerprints
20 NEW_ARTIFACT initial ingests
14 EXACT_DUPLICATE real re-encounters
20 logical sources
20 SourceArtifact rows
20 stored objects
34 SourceIngestionEvent rows
```

The two PCA-book-like files remained byte-distinct. Uncertain `Lecture9-*` course membership remained `POSSIBLE` rather than being silently strengthened.

The source store passed a clean audit, a verified backup, a clean restore, and a second full integrity audit. The prospectively frozen SU-G01 through SU-G23 gates all passed on the accumulated executable and first-corpus evidence.

Classification:

```text
SOURCE_SUBSTRATE_ACCEPTED
```

This acceptance proves the architecture and implementation seam. It does **not** mean the permanent user-controlled source vault already exists. The first validation used disposable development storage and the exact uploaded bytes available to the active development runtime.

PR #74 promoted that accepted implementation into `v1-frontend-spike` at:

```text
8215718db3e44f000cc6ed53d6a051522d429dbd
```

---

## Permanent source-vault bootstrap is paused, not cancelled

The operational stage remains preserved by:

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
PR #75
```

The deployment still requires five private locations:

```text
ORIGINAL_SOURCE_ROOT
SOURCE_REGISTRY_DATABASE
SOURCE_VAULT_ROOT
INDEPENDENT_BACKUP_ROOT
CLEAN_RESTORE_ROOT
```

No local source-vault operation is currently running. When the project returns to PR #75, Course 2 remains blocked until compare, reviewed ingestion, integrity audit, independent backup, clean restore, and restored audit succeed on user-controlled storage.

---

## Serious methodological knowledge-universe construction

The broader construction program remains governed by:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

The coverage-depth ladder is:

```text
C0  MAPPED
C1  SOURCED
C2  DECOMPOSED
C3  OPERATIONALIZED
C4  CONNECTED
C5  BEHAVIORALLY_TESTED
C6  PROJECT_EXPOSED
```

Coverage depth is not truth, maturity, source quality, freshness, or enforcement authority.

The first six deep pressure-test areas are:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

The representation is allowed to change if serious source-backed content reveals a real deficiency.

---

## Durable architectural core

Prototype V0 strongly falsified the original P0 implementation strategy, while the broader ADS vision survived.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Foundation 018 separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Foundation 019 defines the methodological-navigation progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Foundation 020 provides the current reusable-knowledge representation direction around assets, components, narrative facets, relations, conditional rules, collections, exact revisions, and provenance.

Foundation 021 governs the professional product/interface foundation. Foundation 022 adds the separate source/evidence substrate beneath the governed knowledge universe.

---

## Accepted V1 implementation decisions

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime
D-033  ADS-owned private Source Universe substrate and relational Source Registry
```

The runtime database, knowledge interchange, source artifact store, and rebuildable retrieval indexes remain different authority layers.

No multi-model development decision has yet been added to this accepted decision list.

---

## Retrieval and reasoning evidence

The bounded accepted chain remains:

```text
lexical retrieval
    -> dense complementarity
    -> hybrid comparator
    -> explained MethodologicalHorizon
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

Specification 014 preserved equal measured reasoning quality on its bounded benchmark while reducing provider input by 66.56%. That result supports selective context economy but does not select the final navigation strategy for a serious knowledge universe.

Later recommendation/action experiments remain deliberately bounded evidence. In particular, Specification 022 ended `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no legitimate `GENERIC`, `ADS_HORIZON`, or `ORACLE_HORIZON` comparison exists from that run.

---

## Repository role

This repository is the project's durable development source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The emerging multi-model architecture generalizes that principle: collaborators may reason in different products, but durable project state and collaboration provenance must be recoverable from shared project infrastructure.

---

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/201_mc_0001_phase_b_and_c_recorded_bounded_phase_d_challenge_opened.md
docs/checkpoints/200_mc_0001_phase_a_recorded_partial_independence_contamination_phase_b_opened.md
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/model_collaboration/threads/MC-0001/THREAD.md
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md

docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md

docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/specifications/023_v1_source_universe_substrate.md

docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

## Exact next step

```text
1. Claude reads messages/004_chatgpt_response_to_claude.md
2. Claude performs one bounded Phase-D challenge rather than reopening the whole architecture
3. preserve messages/005_claude_phase_d_challenge.md
4. Claude marks each unresolved item AGREE / DISAGREE / PARTIAL and gives the strongest reason + change-of-mind evidence
5. route remaining disagreements to bounded design/prototype, evidence check, human project-intent decision, or explicit deferral
6. only after resolution decide whether Development Method v0.5 / provider-neutral checkpoint provenance is justified
7. if mechanical collaboration-state support remains required, design and test it before declaring routine multi-model canonical development ready
8. PR #75 remains paused until the user chooses to resume the permanent source-vault deployment
```