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
horizontal + vertical navigation
keyboard panning and recovery
Reset and jump navigation
compact/expandable project HUD
collapsible System Focus context drawer
collision-safe composer/map geometry
explicit browser fullscreen control with fallback
```

The current immersive-scale implementation and automated gate are preserved in:

```text
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
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
Cockpit stage taxonomy
Cockpit URL contract
Cockpit visual identity
Cockpit screenshot baseline
desktop wrapper
```

The immediate next step is real-browser human product review of the current `/cockpit` implementation. The Cockpit visual baseline and deeper canvas/semantic-zoom architecture must not be frozen before that review.