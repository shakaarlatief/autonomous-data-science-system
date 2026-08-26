# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 213  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration base:** `v1-frontend-spike` Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`

## Start here

```text
README.md                         project overview and current stage
docs/CURRENT_STATE.md             exact present state and continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable project routing metadata
docs/VISION.md                    high-level product/system direction
docs/PRINCIPLES.md                accepted high-level design principles
docs/DECISIONS.md                 accepted project-level decisions
docs/OPEN_QUESTIONS.md            unresolved questions
docs/DEVELOPMENT_METHOD.md        current canonical development method v0.5
docs/CONTINUITY.md                provider-neutral continuity procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current route:

```text
checkpoint                        213
active development branch        v1-cockpit-design-exploration
active PR                        none
latest specification             Specification 024
promoted Cockpit baseline        Specification 008
current boundary                 MC-0004 Phase C randomized G4 ambient-distribution human review
source-vault deployment          PAUSED, Course 2 gate unchanged
```

---

# Active Cockpit design route

## Human-selected grid/world baseline

```text
G4 Adaptive Hybrid  SELECTED
Dark mode           ACTIVE DESIGN BASELINE
Light mode          DEFERRED
```

G1 Precision Lines, G2 Dot Matrix and G3 Cross Lattice are no longer primary substrate candidates.

Primary grid/world evidence:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
frontend/design-lab/grid-world.html
```

## Ambient dynamics decisions

All tested ambient mechanisms survive:

```text
travelling grid currents
intersection glints
ambient light drift
localized semantic activity
```

Human review also established:

```text
initial D1-D4 cadence      TOO SUBTLE
combined preset preference LIVELY
fixed ambient coordinates  REJECTED
```

Current supporting evidence:

```text
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
docs/research/041_combined_g4_ambient_motion_intensity_tuning.md
docs/research/042_g4_randomized_ambient_distribution_and_grid_intersection_glints.md

docs/checkpoints/211_g4_selected_dark_first_ambient_dynamics_review_opened.md
docs/checkpoints/212_combined_g4_ambient_intensity_human_review_opened.md
docs/checkpoints/213_g4_randomized_ambient_distribution_human_review_opened.md
```

Current browser lab:

```text
frontend/design-lab/grid-dynamics-combined.html
frontend/design-lab/grid-dynamics-combined.css
frontend/design-lab/grid-dynamics-combined.js
```

Local route:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html
```

## Current spatial-randomization rules

```text
CURRENTS
    horizontal or vertical
    random visible grid line
    snapped to 20 px lattice
    random start, direction, distance, length and timing

GLINTS
    x snapped to 20 px
    y snapped to 20 px
    always centered on an actual grid intersection / cell corner

AMBIENT DRIFT
    random start position
    random size
    random motion vector
    random opacity within cadence preset
```

The semantic activity layer remains separate and is not randomized as decoration.

---

# Phase-C design protocol

The preferred workflow is:

```text
choose one design question
inspect real references if useful
build bounded browser variants
hold project state constant
human compares
record prefer/reject/combine/refine
iterate if needed
move to next design question
```

Generated-image UI concepts are not part of the preferred Cockpit evaluation workflow.

Isolated experimental code lives under:

```text
frontend/design-lab/**
```

The production `/cockpit` remains the control baseline until later integrated evidence warrants promotion.

---

# MC-0004 evidence route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
docs/model_collaboration/REVIEW_INBOX.md
```

Phase A:

```text
Claude independent proposal
commit                  cd2e12f2c79ee3b2f205457c5940eb2022b4631a
review base             bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
historical independence BLIND_TO_CANDIDATE
```

Phase B:

```text
Claude comparative review
commit          d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
classification  COMPARATIVE_ONLY
```

Phase C:

```text
PHASE_C_BROWSER_DESIGN_EVALUATION
next expected actor  human
```

No pending Claude review obligation exists.

---

# Broad Cockpit research and synthesis

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
```

Strongly reinforced design mechanisms still awaiting broader integration:

```text
semantic zoom
category-level work-unit visual grammar
semantic connector type + direction + state
full Conversation Workspace
conversation <-> structured project links
information-density lenses
multi-axis project/runtime/importance state treatment
2.5D before true 3D
large-project scalability
```

Remaining major slices after grid/world refinement:

```text
work-unit visual grammar
connector visual language
semantic zoom
stage/orientation system
Conversation Workspace
conversation + analytical coexistence
information-density lenses
runtime/waiting/approval visualization
focus/depth transitions
command architecture at scale
large-project grouping/layout
final design system
```

---

# Promoted Cockpit interaction architecture

Primary route:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Specification 008 remains accepted and is not replaced by the current visual experiments.

Still intentionally unfrozen include final visual identity, graph technology, semantic zoom/grouping details, auto-layout, minimap, stage taxonomy/ruler treatment, permanent tool-rail design, ambient treatment, route/persistence details and canonical screenshot baseline.

---

# Source Universe route

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

Current interpretation:

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```

---

# Methodological knowledge-universe program

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

The current Cockpit work is a deliberate frontend/product subtrack and does not replace the larger methodological program.
