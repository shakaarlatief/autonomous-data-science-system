# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. Bounded V1 is now constructing the serious methodological knowledge universe. Its prerequisite Source Universe substrate has been accepted and promoted, and the active stage is permanent deployment of that substrate on user-controlled durable storage.**

```text
checkpoint            198
active branch         v1-source-vault-bootstrap
active PR             #75
promoted V1 head      8215718db3e44f000cc6ed53d6a051522d429dbd
latest specification  Specification 023
source outcome         SOURCE_SUBSTRATE_ACCEPTED
latest experiment      Specification 022
experiment outcome     INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary       permanent user-controlled source-vault bootstrap;
                       Course 2 blocked until recovery proof succeeds
```

The current source route is:

```text
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/checkpoints/197_source_substrate_canonical_reconciliation_and_promotion_candidate.md
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```

Foundation 022 is the canonical renumbering of the source-universe foundation originally drafted as Foundation 021. The pre-existing professional product/interface foundation remains Foundation 021.

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

PR #74 has now promoted that accepted implementation into `v1-frontend-spike` at:

```text
8215718db3e44f000cc6ed53d6a051522d429dbd
```

---

## Permanent source-vault bootstrap

The active operational stage is governed by:

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

The deployment must resolve five private locations without committing them to Git:

```text
ORIGINAL_SOURCE_ROOT
SOURCE_REGISTRY_DATABASE
SOURCE_VAULT_ROOT
INDEPENDENT_BACKUP_ROOT
CLEAN_RESTORE_ROOT
```

The original VU Machine Learning folder remains read-only input from ADS's perspective. The permanent vault and independent backup must remain outside the public repository.

Before Course 2 is admitted, the original folder must be compared against the prospective fingerprints, every mismatch class must be reviewed, the intended corpus must be ingested, the working store must audit cleanly, an independent backup must be created and verified, and a clean restore must reproduce the source corpus with a second clean audit.

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

Source binaries are a separate private evidence substrate. Stable architecture, schemas, code, public-safe metadata, decisions, checkpoints, validation evidence, and project history remain versioned here.

---

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md

docs/checkpoints/197_source_substrate_canonical_reconciliation_and_promotion_candidate.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md

docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/specifications/023_v1_source_universe_substrate.md

docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

## Exact next step

```text
1. identify the original local VU Machine Learning folder
2. choose the permanent Source Registry and Source Vault locations
3. choose a genuinely independent backup destination
4. choose a temporary clean-restore location
5. verify storage capacity and separation from the public Git repository
6. execute compare before any permanent ingestion
7. review every mismatch / additional-source result
8. ingest the reviewed corpus
9. run a clean integrity audit
10. create and verify the independent backup
11. clean-restore and run the restored integrity audit
12. preserve only safe deployment evidence in PR #75
13. only after that gate succeeds, admit the next educational course batch
14. then map the wider source corpus and resume the six deep methodological pressure tests
```
