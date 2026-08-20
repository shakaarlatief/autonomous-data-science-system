# ADS V1 Frontend Spike

This directory contains the candidate V1 frontend product spike governed by `docs/specifications/006_v1_frontend_architecture_and_visual_spike.md`.

The spike is intentionally representative rather than production-connected. It uses typed ADS-shaped fixtures behind a `FrontendDataSource` boundary and a bounded interaction-stream abstraction so the UI can be evaluated before the real backend/API transport is selected.

## Local development

```bash
cd frontend
npm install
npm run dev
```

The current spike targets Node 24.

## Validation

```bash
npm run build
npm test
npx playwright install chromium
npm run e2e
```

The CI gate executes build and unit tests on Linux and Windows, then runs Chromium browser and automated accessibility checks on Linux.

## Current evaluation scope

The spike currently covers:

```text
Overview
Data
EDA
Decisions & History
methodological recommendation panel
human approval interaction
light/dark themes
URL-preserved analytical view state
ECharts/Plotly side-by-side implementation path
bounded AG-UI adapter experiment
```

It does not establish the final frontend stack, charting library, agent transport, desktop wrapper, or production API contract. Those require explicit evaluation and promotion.
