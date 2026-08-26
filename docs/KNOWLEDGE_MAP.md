# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 220  
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
checkpoint                        220
active development branch        v1-cockpit-design-exploration
active PR                        none
latest specification             Specification 024
promoted Cockpit baseline        Specification 008
current boundary                 corrected work-unit grammar human verification before Claude ideation
source-vault deployment          PAUSED, Course 2 gate unchanged
```

---

# Active Cockpit design route

## Grid/world baseline: provisionally settled

```text
G4 Adaptive Hybrid    SELECTED
Dark mode             ACTIVE DESIGN BASELINE
Light mode            DEFERRED
```

Current retained ambient behavior:

```text
travelling currents       randomized across 20 px grid lines, Lively preferred
major-grid glints          100 px intersections only, approximately Quiet
ambient drift              retained
localized semantic glow    retained
fixed authored positions   rejected
```

Primary grid/world evidence:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
docs/research/041_combined_g4_ambient_motion_intensity_tuning.md
docs/research/042_g4_randomized_ambient_distribution_and_grid_intersection_glints.md
docs/research/043_g4_major_grid_glints_and_decoupled_ambient_cadence.md

docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
docs/checkpoints/211_g4_selected_dark_first_ambient_dynamics_review_opened.md
docs/checkpoints/212_combined_g4_ambient_intensity_human_review_opened.md
docs/checkpoints/213_g4_randomized_ambient_distribution_human_review_opened.md
docs/checkpoints/214_g4_major_grid_glints_quiet_cadence_human_review_opened.md

frontend/design-lab/grid-world.html
frontend/design-lab/grid-dynamics.html
frontend/design-lab/grid-dynamics-combined.html
```

"Provisionally settled" means stop tuning continuously for now, not permanent freeze.

Research 040 preserves the visual-design distinction:

```text
semantic motion
    communicates project/runtime meaning

ambient/decorative motion
    may exist purely for polish/atmosphere
    must remain lower-salience and must not masquerade as semantic state
```

---

# Completed Slice 02A: H4 generic interaction lighting

Primary evidence:

```text
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
docs/research/045_h4_resting_node_light_world_spill_refinement.md
docs/checkpoints/215_grid_world_provisionally_settled_work_unit_lighting_review_opened.md
docs/checkpoints/216_h4_selected_resting_world_spill_human_review_opened.md
docs/checkpoints/217_h4_interaction_lighting_settled_work_unit_visual_grammar_opened.md
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

Human review selected:

```text
H4 Integrated Response  SELECTED
```

Final generic H4 model:

```text
REST
    clean localized/asymmetric in-box illumination
    narrow asymmetric outward world spill
    no broad circular resting halo

HOVER
    full node-colored halo
    pointer-following/specular hotspot
    stronger local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep on entry
    small depth lift
    fast entry + smoother slower release
```

Final human review accepted both the outward-only resting spill and the hover timing.

No further generic hover/outward-spill variant is currently justified.

Later selected/focused and runtime/blocked/approval states may use lighting when those semantic slices are tested.

---

# Current Slice 02B: work-unit category / silhouette visual grammar

Primary route:

```text
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
docs/checkpoints/218_work_unit_visual_grammar_browser_experiment_human_review_opened.md
docs/checkpoints/219_work_unit_grammar_preliminary_review_claude_ideation_requested.md
docs/checkpoints/220_work_unit_grammar_h4_control_corrected_claude_ideation_ready.md
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar-lighting-controls.css
frontend/design-lab/work-unit-grammar.js
```

Local route:

```text
http://localhost:5173/design-lab/work-unit-grammar.html
```

The active category question is:

```text
How should meaningful work-unit kinds become visually distinguishable
without collapsing category, project disposition, runtime state and importance
into one overloaded visual treatment?
```

First-round browser directions:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

Representative fixture categories:

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

These are not a frozen production taxonomy.

The design lab exposes:

```text
Category strip
    neutral category comparison

Project scene
    realistic G4/H4 context + connectors

In-box light
    H4 baseline
    Reduced

Reduced motion
    secondary accessibility check
```

## Preliminary human result

The first W1-W4 implementation received a strongly positive preliminary human review, but no variant was selected.

The project owner judged that the current four candidates likely cover too little of the plausible work-unit grammar design space and explicitly requested additional Claude ideas and inspiration before convergence.

There is no artificial candidate-count cap. Preserve all genuinely distinct and worthwhile candidates. Browser testing may use multiple batches for clarity, but batching is not rejection.

## Browser/control corrections before Claude

Human review exposed three issues:

```text
Project Scene could remain overlaid with Category strip
accepted H4 in-box resting light was accidentally suppressed by the grammar DOM
resting light stayed left-biased when category signature bars moved to top/bottom/right
```

All are corrected.

Research 047 records the H4 control integrity lesson:

```text
preserving accepted rendered behavior
!=
merely copying old CSS values into a different DOM stack
```

The current browser experiment restores the accepted H4 in-box appearance as the default and preserves the quieter appearance as an explicit optional comparison.

### H4 baseline versus Reduced

```text
H4 baseline
    default restored accepted in-box resting illumination

Reduced
    intentionally near-dark / low-colour in-box resting alternative
```

This comparison changes in-box resting-light intensity only.

It does not intentionally reopen:

```text
outward resting spill
hover halo
pointer hotspot
hover world light
connector hover emphasis
perimeter sweep
hover timing
```

No preference exists yet.

### Signature-side-aware lighting

The structural rule is:

```text
if a visible category signature/accent edge moves,
signature-anchored resting light moves with it
```

Current mapping:

```text
W1
    all left

W2 / W4
    Question        left
    Investigation   left
    Validation      top
    Model           bottom
    Evaluation      right

W3
    no explicit signature bar
    retain accepted left-biased H4 baseline
```

The in-box light, near-node rest light and outward spill rotate/mirror together.

Corrected exact browser target after human verification:

```text
03d3997498192544ce92c97c2a49e839b3a95af4
```

---

# Current MC-0004 collaboration gate

Request:

```text
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
```

Expected output:

```text
docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
```

Classification:

```text
COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

Current sequencing:

```text
human verifies corrected browser target
-> Claude divergent ideation
-> ChatGPT synthesis / browser implementation
-> human comparison
```

Claude is asked to broaden the design space rather than merely rank W1-W4.

Claude may inspect all current candidate material. Historical Phase-A independence remains preserved separately.

Claude may comment on the explicit H4-baseline-vs-Reduced in-box-light comparison if useful, but it remains secondary to category-grammar ideation.

Claude write scope:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

ChatGPT retains target-state write ownership.

Current evidence state:

```text
first-round research brief       complete
first-round browser experiment   complete
preliminary human review         positive, no selection
Project Scene defect             corrected
H4 in-box control drift          corrected
signature-side lighting          corrected
H4 baseline vs Reduced           explicit comparison OPEN
Claude divergent ideation        PENDING after human verification
production promotion             not authorized
```

Still deliberately unresolved:

```text
H4 baseline vs Reduced in-box preference
final work-unit taxonomy
final semantic category colors
multi-axis status treatment
selected-state treatment
runtime/running/waiting treatment
blocked/approval treatment
final node sizing and typography
final connector vocabulary
production motion implementation
```

---

# Phase-C design protocol

Preferred workflow:

```text
choose one design question
inspect real references if useful
build bounded browser variants
hold unrelated variables constant
human compares
record prefer/reject/combine/refine
use another model selectively when divergent design value is expected
iterate if needed
move to the next design question
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
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
docs/model_collaboration/REVIEW_INBOX.md
```

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Current  human corrected-target verification, then Claude divergent ideation
```

---

# Broad Cockpit research and synthesis

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
```

Strongly reinforced mechanisms still awaiting broader integration:

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

Remaining major slices after category/silhouette grammar include:

```text
multi-axis status treatment
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

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Specification 008 remains accepted and is not replaced by the current visual experiments.

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
