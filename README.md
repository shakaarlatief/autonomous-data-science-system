# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

Prototype V0 is complete. Bounded V1 is constructing the serious methodological knowledge universe and the supporting professional substrate needed to use it safely.

The Source Universe substrate is accepted and promoted. The permanent user-controlled source-vault bootstrap is preserved but operationally paused.

The major Level-2 collaboration-method work has now passed its review and promotion audit on draft PR #76:

```text
checkpoint            204
active branch         v1-multimodel-development-collaboration
active PR             #76
promoted V1 head      8215718db3e44f000cc6ed53d6a051522d429dbd
latest specification  Specification 024
specification outcome COLLABORATION_STATE_GUARD_ACCEPTED
source outcome         SOURCE_SUBSTRATE_ACCEPTED
latest experiment      Specification 022
experiment outcome     INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary       final PR #76 integration audit;
                       permanent source-vault deployment remains paused
```

No scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from Specification 022.

---

## Governed multi-model development

Development Method v0.5 now accepts provider-neutral governed collaboration among ChatGPT, Claude, the human project owner, and future collaborators.

Canonical route:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/checkpoints/204_multimodel_collaboration_method_promoted.md
docs/DECISIONS.md, D-034
```

Core accepted rules:

```text
repository remains project authority
SOLO work remains first-class
collaboration is selective and task-scoped
one bounded task owner
ROLE != WRITE_SCOPE
one target-state write owner at a time
reviewers may write only declared secondary surfaces
machine-readable thread state is a coherence guard, not an authenticated lock
GitHub issue / PR discussion is transport, not authority
numbered repository messages preserve durable collaboration provenance
independent-first review uses accepted pre-proposal refs where independence matters
known review contamination is disclosed rather than erased
provider-local interaction sessions use IDs such as chatgpt-06 / claude-01
human arbitration is reserved for genuine project-intent / consequential choices
```

The architecture was pressure-tested rather than accepted from one model's proposal:

```text
MC-0001
    architecture counter-design / comparative challenge
    -> exposed candidate-content leakage and global-writer over-coarseness

MC-0002
    direct implementation review of Specification 024
    -> MC-G01 through MC-G16 satisfied
    -> COLLABORATION_STATE_GUARD_ACCEPTED

MC-0003
    deferred review/catch-up pressure test
    -> two Claude obligations coexisted safely
    -> Claude later processed both in priority order with separate exact targets
```

---

## Deferred review and catch-up

A collaborator being temporarily unavailable does not globally block ADS unless a specific review gate has been reached.

The accepted rule is:

```text
collaborator unavailable
    !=
project globally blocked
```

Intended review must not silently become SOLO work. Deferred review preserves an exact immutable target, an explicit review requirement, and the boundary before which the review must occur.

Current convenience route:

```text
docs/model_collaboration/REVIEW_INBOX.md
```

When Claude has pending obligations, the intentionally small manual trigger is:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md, then proceed with the pending Claude reviews in order.
```

The inbox is not authority. Per-thread state, exact Git refs, review requests, and resolution artifacts govern.

Unattended scheduled model review is deliberately deferred. API orchestration is also deferred. Neither is needed for the current repository-mediated workflow.

---

## Interaction provenance

Both ChatGPT and Claude use the human-facing project/workspace name:

```text
Autonomous Data Science System
```

Visible conversations use:

```text
NN - Main Topic / Stage
```

Each interaction environment has its own sequence, with repository session identities such as:

```text
chatgpt-06
claude-01
```

Historical checkpoints through Checkpoint 203 retain their original ChatGPT-specific metadata. Checkpoint 204 begins the prospective provider-neutral checkpoint contract.

---

## Source Universe substrate

External source artifacts are evidence, not the methodological knowledge base itself:

```text
SOURCE UNIVERSE
    exact evidence artifacts + provenance

        !=

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable methodological reasoning
```

The accepted Source Universe architecture is governed by Foundation 022, Research 034, Specification 023, and D-033. It separates exact immutable source artifacts, logical source identity, collections/membership, locators, ingestion events, rights/access metadata, derived lineage, deterministic exports, integrity audits, backup, and clean restore.

First controlled VU Machine Learning corpus evidence:

```text
20 / 20 prospective fingerprint matches
20 NEW_ARTIFACT initial ingests
14 EXACT_DUPLICATE re-encounters
20 logical sources
20 exact artifacts
20 stored objects
34 ingestion events
20 / 20 working integrity audit
20 / 20 restored integrity audit
SU-G01 through SU-G23 PASS
SOURCE_SUBSTRATE_ACCEPTED
```

Source binaries remain outside public Git.

Permanent user-controlled deployment remains preserved by:

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

It is paused, not cancelled. Course 2 remains blocked until the permanent compare, reviewed ingestion, integrity audit, independent backup, clean restore, and restored audit are completed on user-controlled storage.

---

## Serious methodological knowledge-universe construction

The larger V1 program remains governed by:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

Coverage depth:

```text
C0  MAPPED
C1  SOURCED
C2  DECOMPOSED
C3  OPERATIONALIZED
C4  CONNECTED
C5  BEHAVIORALLY_TESTED
C6  PROJECT_EXPOSED
```

Initial deep pressure-test slices:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

Coverage depth remains separate from truth, maturity, source authority, freshness, and enforcement strength.

---

## Durable architectural core

Prototype V0 strongly falsified its original P0 implementation strategy while preserving the broader ADS vision.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Important accepted foundations include:

```text
Foundation 018  OBJECTS / RELATIONS / EVENTS / VIEWS project architecture
Foundation 019  KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED/BLOCKING
Foundation 020  reusable methodological knowledge representation
Foundation 021  professional product/interface architecture
Foundation 022  source/evidence substrate
```

Accepted implementation decisions now include D-028 through D-034.

---

## Repository role

This repository is the durable development source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The multi-model extension preserves the same principle. Collaborators may reason in different products, but accepted project state, review provenance, and continuation must remain reconstructable from shared repository infrastructure.

---

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/204_multimodel_collaboration_method_promoted.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/model_collaboration/README.md
docs/specifications/024_v1_model_collaboration_state_guard.md

docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md

docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

## Exact next step

```text
1. finish the PR #76 integration audit and ensure all applicable checks are green
2. promote the accepted multi-model method into v1-frontend-spike
3. reconcile routing to the exact promoted commit
4. preserve the source-vault bootstrap as paused
5. resume permanent user-controlled source-vault deployment before Course 2
```
