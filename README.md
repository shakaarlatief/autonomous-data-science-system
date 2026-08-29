# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS), a rigorous adaptive environment for data-science projects in which a strong LLM is one reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            265
active branch         v1-cockpit-design-exploration
active PR             none
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
latest experiment     INCOMPLETE
Cockpit baseline      Specification 008
method                 Development Method v0.6
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

## Current interaction continuity

```text
interaction session  chatgpt-10
conversation title   10 - Project Cockpit Design Exploration
collaboration thread MC-0004
```

Repository artifacts remain authoritative across chats and models.

## Current Level-2 method boundary

Checkpoint 265 reconciles the development method for a larger repository.

The audit found that the substantive knowledge was still preserved, but the global `KNOWLEDGE_MAP.md` had drifted from its intended project-wide topic-library role into a mostly current-Cockpit routing document. The broad library has now been restored and protected by a structural validator.

Development Method v0.6 also separates development verification from acceptance verification:

```text
V0  documentation / provenance validators
V1  targeted regression
V2  subsystem regression
V3  full integrated gate
V4  promotion / release gate
```

Unknown or shared blast radius defaults conservatively to V3. Small visual iterations can use V1/V2 before human review, with the broader/full gate paid once when the meaningful acceptance boundary closes.

Small changes inside one open review question should normally be aggregated into that review/checkpoint boundary rather than creating a new numbered checkpoint for every implementation commit.

Primary method sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/checkpoints/265_development_method_v06_knowledge_routing_and_verification_reconciliation.md
```

## Knowledge discovery

`docs/KNOWLEDGE_MAP.md` is again the main global navigation layer.

It contains:

```text
Current continuation route
    exact active boundary and next sources

Evergreen topic library
    topic -> canonical authority + rationale + evidence/history + specialized index
```

The evergreen library covers system vision, project state, reusable knowledge, evaluation/falsification, runtime/persistence, retrieval/MethodologicalHorizon, recommendation/calibration, Methodological Knowledge Universe, Source Universe, development/continuity, Cockpit architecture, visual grammar, interaction states, Conversation Workspace, implementation provenance/fidelity, shell/rail/topology and canonical history.

Specialized maps remain authoritative for their own domains, for example:

```text
docs/methodological_knowledge/COVERAGE_MAP.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md
```

## Current Cockpit product boundary

Checkpoint 265 does not change the Cockpit product design.

The active product human-review gate remains Checkpoint 264:

```text
General project discussion
    same visible footprint as WorkUnit boxes
    selected frame belongs to visible project box only

WorkUnit conversation
    selected frame belongs to visible WorkUnit surface only

existing Conversation spacing
    remains correct

current-process Focus
    remains working as far as tested
```

Normal review browser:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

The Adaptive Conversation Dock remains an opt-in design candidate and resumes after Checkpoint 264 is visually confirmed:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

The last complete pre-v0.6 Cockpit gate was:

```text
implementation/test target  9881efe313b8cf04d9521c0464050b30b29944c1
workflow run                33251166351
job                         99096968925
browser tests               78 / 78 passing
```

Because the verification workflow itself changes at Checkpoint 265, the method transition requires one fresh full V3 Cockpit gate before it is closed.

Production `/cockpit` remains untouched.

## Critical Cockpit integration history

The first holistic integrated Cockpit browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` is not an accepted baseline. It remains diagnostic evidence only because the integration reimplemented accepted mechanisms from summaries instead of faithfully porting their exact reviewed implementations.

The durable provenance layer remains:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/265_development_method_v06_knowledge_routing_and_verification_reconciliation.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md

docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```
