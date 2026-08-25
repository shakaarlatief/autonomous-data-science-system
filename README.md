# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

Prototype V0 is complete. Bounded V1 is constructing the serious methodological knowledge universe. Its Source Universe substrate is accepted and promoted. The permanent user-controlled source-vault bootstrap is preserved on draft PR #75 but remains paused while a major Level-2 development-method change, governed multi-model development, is pressure-tested.

```text
checkpoint            203
active branch         v1-multimodel-development-collaboration
active PR             #76
promoted V1 head      8215718db3e44f000cc6ed53d6a051522d429dbd
latest specification  Specification 024
source outcome         SOURCE_SUBSTRATE_ACCEPTED
latest experiment      Specification 022
experiment outcome     INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary       Specification 024 implementation is green and frozen
                       for direct Claude review in MC-0002;
                       PR #75 source-vault bootstrap remains paused
```

No scientific comparison may be inferred from Specification 022.

---

## Governed multi-model development

The project owner requested a professional collaboration architecture for ChatGPT, Claude, and future collaborators rather than informal model switching.

The first architecture thread, `MC-0001`, is now resolved. Its durable route is:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/model_collaboration/threads/MC-0001/THREAD.md
docs/model_collaboration/threads/MC-0001/RESOLUTION.md
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
docs/model_collaboration/threads/MC-0001/messages/005_claude_phase_d_challenge.md
docs/model_collaboration/threads/MC-0001/messages/006_chatgpt_phase_d_resolution.md
docs/checkpoints/202_mc_0001_resolved_specification_024_frozen_mc_0002_opened.md
```

The resolved candidate direction is:

```text
repository remains project authority
SOLO ChatGPT-only and Claude-only work remain first-class
collaboration is selective and task-scoped
one bounded task owner
role and write scope are separate
one collaborator owns target-state writes at a time
reviewers may write only explicitly declared secondary surfaces
GitHub issues/PR comments are transport, not authority
numbered repository messages are durable collaboration provenance
independent-first review is selective and must account for framing/contamination
provider-local session IDs are self-describing, e.g. chatgpt-06 / claude-01
human arbitration is reserved for genuine project-intent or consequential choices
API orchestration remains deferred until evidence justifies its cost and complexity
```

MC-0001 also produced two important empirical findings. Claude detected candidate-content leakage through the supposedly neutral reconstruction set and the lack of any machine-checkable collaboration-state mechanism. ChatGPT in turn identified that Claude's first single-`active_writer` mechanism was too coarse and that role and write authority must remain distinct. Both models revised their own positions.

The first trial was only partially independent because current routing documents already exposed candidate ideas. Future deliberately blind reviews should normally use an accepted pre-proposal base/ref plus a neutral problem packet and explicit exposure audit.

---

## Specification 024: collaboration-state coherence guard

The one load-bearing mechanical follow-up from MC-0001 is frozen in:

```text
docs/specifications/024_v1_model_collaboration_state_guard.md
```

The implementation adds:

```text
schemas/model_collaboration_thread_state_v1.schema.json
scripts/check_model_collaboration_state.py
tests/unit/test_model_collaboration_state.py
.github/workflows/model-collaboration-state.yml
docs/model_collaboration/threads/MC-0002/STATE.json
```

The mechanism records task ownership, target-state write ownership, allowed secondary write surfaces, lifecycle/phase, next actor, independence status, and latest transition.

It is deliberately a **coherence guard, not an authenticated distributed lock**. Current provider integrations share the project owner's GitHub authority, so repository metadata cannot cryptographically prove whether ChatGPT or Claude authored a mutation.

The implementation initially exposed one test-fixture defect. The valid state and validator had passed, but one test attempted to create the same temporary directory twice. That fixture was corrected without relaxing Specification 024 or changing its frozen gates.

Exact green pre-review implementation head:

```text
a9efc43d7c441c8283d2cd954cc6fa1abd021689
```

Dedicated workflow run `32902050014` passed on both Ubuntu and Windows, including 26 focused unit tests and the no-global-lock-field assertion for `current_routing.json`.

MC-0002 now uses the mechanism itself and is waiting for one bounded direct Claude review:

```text
docs/model_collaboration/threads/MC-0002/BRIEF.md
docs/model_collaboration/threads/MC-0002/THREAD.md
docs/model_collaboration/threads/MC-0002/STATE.json
docs/model_collaboration/threads/MC-0002/messages/001_chatgpt_implementation_review_request.md
GitHub Issue #78
```

No Development Method v0.5 or accepted multi-model decision has been promoted yet. Specification 024 must first satisfy MC-G01 through MC-G16 and be classified.

---

## Source Universe substrate

The project is preparing to ingest a large educational and external source corpus. Source artifacts are evidence, not themselves the methodological knowledge base.

```text
SOURCE UNIVERSE
    exact evidence artifacts + provenance

        !=

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable methodological reasoning
```

The accepted source architecture is governed by Foundation 022, Research 034, and Specification 023. It separates immutable content-addressed source artifacts, a relational Source Registry, derived representations, deterministic exports, integrity audits, backup/restore, and public-safe Git metadata.

Specification 023 was validated on the first 20-file VU Amsterdam Machine Learning batch:

```text
20 / 20 prospective fingerprint matches
20 NEW_ARTIFACT initial ingests
14 EXACT_DUPLICATE real re-encounters
20 logical sources
20 exact artifacts
20 stored objects
34 ingestion events
20 / 20 clean working audit
20 / 20 clean restored audit
SU-G01 through SU-G23 PASS
SOURCE_SUBSTRATE_ACCEPTED
```

Source binaries remain outside public Git.

The accepted implementation was promoted in `v1-frontend-spike` at:

```text
8215718db3e44f000cc6ed53d6a051522d429dbd
```

Permanent source-vault deployment remains preserved by Checkpoint 198, `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`, and draft PR #75. It is paused, not cancelled. Course 2 remains blocked until permanent user-controlled compare, reviewed ingestion, audit, independent backup, clean restore, and restored audit succeed.

---

## Serious methodological knowledge-universe construction

The broader program remains governed by:

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

The first six deep pressure-test areas remain:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

Coverage depth is not truth, maturity, source authority, freshness, or enforcement strength.

---

## Durable architectural core

Prototype V0 strongly falsified the original P0 implementation strategy while preserving the broader ADS vision.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Important accepted directions include:

```text
Foundation 018  OBJECTS / RELATIONS / EVENTS / VIEWS project architecture
Foundation 019  KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED/BLOCKING
Foundation 020  reusable methodological knowledge representation
Foundation 021  professional product/interface foundation
Foundation 022  source/evidence substrate
```

Accepted implementation decisions currently remain D-028 through D-033, covering local-first persistence, SQLAlchemy/Alembic, uv packaging, deterministic knowledge interchange, ADS-owned reasoning runtime, and the Source Universe substrate. No multi-model decision has yet been promoted.

---

## Repository role

This repository is the project's durable development source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The multi-model extension keeps the same rule: collaborators may reason in different products, but durable project state, review provenance, and accepted conclusions must remain recoverable from shared project infrastructure.

---

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/203_specification_024_implementation_green_pre_review_head_frozen.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/model_collaboration/threads/MC-0002/THREAD.md
docs/model_collaboration/threads/MC-0002/STATE.json

docs/model_collaboration/threads/MC-0001/RESOLUTION.md
docs/checkpoints/202_mc_0001_resolved_specification_024_frozen_mc_0002_opened.md

docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md

docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

## Exact next step

```text
1. Claude performs one direct MC-0002 implementation review against Specification 024
2. Claude writes messages/002_claude_implementation_review.md only
3. ChatGPT applies only bounded required corrections, if any
4. rerun all frozen gates after any correction
5. classify Specification 024
6. perform the canonical multi-model Development Method / Continuity / provenance / decision promotion audit only after classification
7. keep PR #75 paused until the project returns to permanent source-vault deployment
```
