# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

Prototype V0 is complete. Bounded V1 is constructing the serious methodological knowledge universe and the professional substrate needed to use it safely.

The source substrate and governed multi-model development method are both accepted. The project owner has deliberately paused the permanent user-controlled source-vault bootstrap and reopened the Project Cockpit as a broad visual/product design problem.

Current route:

```text
checkpoint            206
active branch         v1-cockpit-design-exploration
active PR             none
exploration base      2480109fadeee1e480ef03b82e335aacdf9adf91
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
collaboration outcome COLLABORATION_STATE_GUARD_ACCEPTED
Cockpit baseline      Specification 008
source outcome         SOURCE_SUBSTRATE_ACCEPTED
latest experiment      Specification 022
experiment outcome     INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary       next-generation Cockpit design exploration
MC-0004                Claude independent Phase A pending
source-vault           PAUSED, preserved, Course 2 gate unchanged
```

No scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from Specification 022.

No frontend implementation file has yet been changed for this new design phase.

---

## Next-generation Project Cockpit exploration

The current design work is intentionally broader than another CSS polish pass.

The project may reconsider unfrozen visual and interaction choices such as:

```text
grid/world visual treatment
work-unit visual grammar
meaningful connector semantics
state-bearing motion and moving signals
semantic zoom / level of detail
stage/orientation treatment
navigation and contextual commands
runtime and waiting/approval visualization
completed versus unresolved visual state
depth / 2.5D / bounded 3D
full long-form conversation experience
rendering/canvas technology when justified
```

The first broad research map is:

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
```

It draws design/technical lessons from current spatial graph tools, data/workflow control planes, developer environments, agent workspaces, motion systems and large-graph renderers without selecting any one product or library as the ADS template.

Current mockup directions are deliberately provisional:

```text
A. Precision Instrument
B. Living Analytical Field
C. Spatial Control Room
D. Depth-Aware Workbench
```

The correct order is research and comparison first, then realistic mockups/prototypes, then human product review, and only then a bounded implementation specification if the evidence is strong enough.

---

## Promoted Cockpit interaction baseline

Specification 008 remains the accepted V1 Project Cockpit interaction architecture.

Promoted properties include:

```text
Project Cockpit as primary immersive active-work environment
living project-process projection
meaningful work-unit semantics
spatial focus into reusable specialist workspaces
reachability != simultaneous mounting
finite navigable world distinct from semantic project plane
2D project navigation and recovery
bounded geometric zoom / native pinch capability
viewport-aware semantic stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

Specification 008 deliberately leaves the final visual identity, graph/canvas library, semantic zoom/grouping, auto-layout, minimap, stage taxonomy/ruler treatment, tool-rail design and several other visual choices unfrozen.

The current design phase therefore explores legitimate open space rather than discarding previously validated interaction architecture merely because the visuals are being revisited.

Canonical frontend/product route:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
frontend/README.md
```

---

## Long-form Conversation Workspace

The compact Cockpit composer remains useful, but it is no longer treated as the complete conversation experience.

ADS must also support substantial project dialogue in which the user can:

```text
hold long multi-turn data-science conversations
see and revisit previous messages
continue earlier discussions
search/navigate conversation history
discuss visible project work while retaining project context
```

The current design research distinguishes:

```text
Composer
Conversational response
Conversation history
Conversation Workspace
```

Candidate presentations include a docked conversation region, a focused conversation workspace, an analytical/conversation split workbench, a canvas-anchored expansion, and a direct Conversation specialist view.

No presentation or persistence model is selected yet.

The governing project-state principle remains:

```text
conversation can be rich and durable for the user
    but
consequential project truth must not exist only as prose history
```

Decisions, Questions, Findings, Proposals, Investigations, Runs, approvals and other consequential outcomes should continue to map into structured project state and may be linked from conversation.

---

## MC-0004 independent design comparison

The current design task uses the accepted provider-neutral collaboration method in:

```text
INDEPENDENT_THEN_COMPARATIVE
```

mode.

Thread:

```text
docs/model_collaboration/threads/MC-0004/
```

Exact neutral Claude Phase-A review base:

```text
bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
```

Current state:

```text
phase                   PHASE_A_INDEPENDENT_DESIGN
next expected actor     Claude
independence            BLIND_TO_CANDIDATE
Claude write surface    docs/model_collaboration/threads/MC-0004/messages/**
```

Claude must preserve its independent proposal before reading Research 037 or later ChatGPT candidate-design material. Comparative synthesis begins only after that Phase-A proposal is frozen.

Current convenience route:

```text
docs/model_collaboration/REVIEW_INBOX.md
```

---

## Governed multi-model development

Development Method v0.5 accepts provider-neutral governed collaboration among ChatGPT, Claude, the human project owner, and future collaborators.

Canonical route:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/specifications/024_v1_model_collaboration_state_guard.md
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
reviewers write only declared secondary surfaces
machine-readable thread state is a coherence guard, not an authenticated lock
GitHub issue / PR discussion is transport, not authority
numbered repository messages preserve durable collaboration provenance
independent-first review uses accepted pre-proposal refs where anchoring matters
known review contamination is disclosed rather than erased
human arbitration is reserved for genuine project-intent / consequential choices
```

MC-0001, MC-0002 and MC-0003 are closed. MC-0004 is the active Cockpit design thread.

Unattended scheduled model review and API orchestration remain deliberately deferred.

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

The accepted Source Universe architecture is governed by Foundation 022, Research 034, Specification 023, and D-033.

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

Permanent user-controlled deployment is preserved by:

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

Current interpretation:

```text
permanent deployment   PAUSED
accepted architecture  UNCHANGED
real deployment        NOT YET EXECUTED
Course 2 gate          UNCHANGED
```

When the project owner resumes this work, the original source folder comparison, reviewed ingestion, working audit, independent backup, clean restore and restored audit still have to succeed before Course 2 is admitted.

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

The current Cockpit work is a deliberate frontend/product subtrack. It does not replace the larger methodological knowledge-universe objective.

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

Accepted implementation decisions remain D-028 through D-034.

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

docs/checkpoints/206_source_vault_paused_cockpit_design_exploration_opened.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md

docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

## Exact next step

```text
1. have Claude complete MC-0004 Phase A from exact neutral review base bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
2. preserve Claude's independent proposal under MC-0004/messages/
3. only then compare it with Research 037
4. select the strongest 2-4 design mechanisms/directions for realistic mockups
5. explicitly test the long-form Conversation Workspace
6. pressure-test medium/large project state and active/blocked/completed/runtime scenarios
7. perform human visual/product review
8. freeze a bounded implementation/prototype specification only after that evidence
9. resume permanent source-vault deployment whenever the project owner chooses
```