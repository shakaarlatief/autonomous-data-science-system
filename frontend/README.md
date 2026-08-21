# ADS V1 Frontend Spike

This directory contains the candidate V1 frontend product work governed primarily by:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
```

The frontend remains an evaluation and product-validation track rather than a finalized production architecture. It uses typed ADS-shaped fixtures behind application boundaries so interaction, information architecture, accessibility, scalability, and visual quality can be tested before the real backend/API transport and final frontend technology choices are promoted.

## Local development

The current spike targets Node 24.

From the repository root:

```bash
cd frontend
npm ci
npm run dev
```

Open the local Vite URL and use `/cockpit` for the current primary Project Cockpit product gate.

## Validation

```bash
cd frontend
npm ci
npm run build
npm test
npx playwright install chromium
npm run e2e
```

The CI gate executes build and unit tests on Linux and Windows, then Chromium browser, interaction, automated accessibility, and controlled direct-project visual-regression checks on Linux.

## Current product surfaces

The conventional project-view shell currently covers:

```text
Overview
Data
EDA
Decisions & History
methodological recommendation/guidance state
human approval interaction
run/activity state
light/dark themes
URL-preserved analytical view state
ECharts/Plotly comparison path
bounded AG-UI adapter experiment
```

The Project Cockpit is the strongly preferred primary active-work direction and currently demonstrates:

```text
immersive /cockpit route
living stage-zone project map
meaningful project work units
blocked / attention / selected / complete / deferred state
native system composer
smooth focus into shared Data and EDA workspaces
Production Missingness focused investigation
URL-addressable focus and browser Back restoration
reduced-motion-safe transitions

large two-dimensional project viewport
native horizontal + vertical scroll/trackpad navigation
Arrow / Shift+Arrow / Home keyboard recovery

FiniteNavigableGridWorld != SemanticProjectPlane
    symmetric always-pannable surrounding world
    continuous low-contrast grid through navigation reserve
    subtle finite-world boundary cue
    workspace-level ambient depth owned by ProjectWorld
    no second clipped ProjectCanvas atmosphere layer

geometric project zoom
    zoom out / percentage / zoom in
    100% reset
    fit project
    + / - / 0 / F keyboard equivalents

native trackpad pinch candidate
    normalized wheel delta units
    animation-frame coalescing
    bounded per-frame progression
    immediately current zoom state
    approximate gesture anchoring
    obsolete anchor-correction cancellation

viewport-aware stage ruler
    remains near the top of the operating viewport
    follows semantic stage geometry horizontally
    begins at rendered Framing boundary
    ends at rendered Evaluation boundary

scalable project navigation
    Jump to quick semantic destinations
        Active work
        Blocker
        Investigation
        Evaluation
    searchable meaningful project work
    collision-safe placement above the persistent composer
    independently scrolling result region

canvas-dominant immersive chrome
    one reduced top HUD
    explicit HUD hide/show
    narrow right-edge vertical project-map tool rail
    explicit tool-rail fold/restore
    floating project details
    floating System Focus
    composer floating over the continuous grid world

explicit browser fullscreen control with fallback
```

## Current Cockpit evidence

Current design and implementation sources:

```text
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/research/007_fifth_cockpit_human_review_continuous_grid_world_stage_ruler_and_vertical_tool_rail.md
docs/research/008_sixth_cockpit_human_review_world_ambient_continuity_pinch_stability_and_collision_safety.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
docs/checkpoints/123_fourth_cockpit_review_balanced_spatial_world_and_orientation_validated.md
docs/checkpoints/124_continuous_grid_world_stage_ruler_and_vertical_tool_rail_gate_passed.md
docs/checkpoints/125_sixth_cockpit_review_ambient_pinch_ruler_and_collision_repairs_validated.md
```

Specification 007 is currently **candidate v0.6**.

Validated refinement head:

```text
a2e401408c55a74905e0654c40185f4f9990becc
```

Validation evidence:

```text
V1 frontend spike
run 140 / 32475241980

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The first sixth-review browser gate is retained as useful evidence. It exposed a real stage-ruler geometry defect and an over-strict synthetic pinch test. The ruler now derives its terminal geometry from rendered semantic stage boundaries. The pinch gate now evaluates underlying continuous-scale progression, bounded change, and approximate anchor stability rather than requiring every small gesture event to change a rounded integer percentage label.

## Current human/hardware gate

The automated gate does not close real laptop trackpad feel.

The next review should explicitly exercise:

```text
slow pinch in
slow pinch out
faster pinch in/out
pinch around different project regions
immediate switching between two-finger pan and pinch
perceived anchor stability

ambient depth at low zoom
Framing/Evaluation ruler terminals across pan/zoom
Jump/search separation from the composer
lowest-result reachability
professional overall Cockpit interaction/visual quality
```

If this review succeeds strongly enough, Specification 007 should receive a deliberate promotion decision rather than being promoted merely because automated gates are green.

## Current non-decisions

The spike does **not** establish the final:

```text
frontend stack promotion
charting library
agent/event transport
production API contract
graph/canvas library
gesture library
native-pinch normalization/sensitivity constants
auto-layout system
minimap
semantic-zoom implementation
geometric zoom range
finite-world extent algorithm
pan/zoom persistence contract
project-search backend
pointer-proximity HUD reveal
Cockpit stage taxonomy
permanent stage-ruler treatment
permanent vertical tool-rail design
Cockpit URL contract
Cockpit visual identity
exact ambient styling
Cockpit screenshot baseline
desktop wrapper
```

The immediate next step is the real-browser/hardware human product review of the current Specification 007 candidate v0.6 `/cockpit` implementation. The Cockpit visual baseline and deeper canvas/gesture/semantic-zoom architecture must not be frozen before that review.
