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

geometric project zoom
    zoom out / percentage / zoom in
    100% reset
    fit project
    + / - / 0 / F keyboard equivalents
    trackpad-style pinch zoom around the gesture anchor

scalable project navigation
    Jump to quick semantic destinations
        Active work
        Blocker
        Investigation
        Evaluation
    searchable meaningful project work

canvas-dominant immersive chrome
    one reduced top HUD
    explicit HUD hide/show
    stage strip directly attached to project space
    floating project-map toolbar
    floating project details
    floating System Focus
    composer floating over continuous project canvas
    lower/right recovery margin so overlays do not trap work

explicit browser fullscreen control with fallback
```

Current human-review and implementation evidence:

```text
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
```

Validated refinement head:

```text
e500eb45c1de59f24b1531b890f55d2ec3bfffc5
```

Validation:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

## Current non-decisions

The spike does **not** establish the final:

```text
frontend stack promotion
charting library
agent/event transport
production API contract
graph/canvas library
auto-layout system
minimap
semantic-zoom implementation
geometric zoom range
pan/zoom persistence contract
project-search backend
pointer-proximity HUD reveal
Cockpit stage taxonomy
Cockpit URL contract
Cockpit visual identity
Cockpit screenshot baseline
desktop wrapper
```

The immediate next step is real-browser human product review of the current Specification 007 candidate v0.3 `/cockpit` implementation. The Cockpit visual baseline and deeper canvas/semantic-zoom architecture must not be frozen before that review.
