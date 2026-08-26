# Checkpoint 215: Grid/World Provisionally Settled, Work-Unit Lighting Human Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records provisional settlement of the current G4 grid/world treatment and opens a bounded browser review of work-unit interaction lighting, including full hover halos, pointer-responsive light, local grid spill, connector emphasis and one-time perimeter sweep behavior.  
**Authority:** Current product-design routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Grid/world layer is provisionally settled

The project owner judged the current G4 treatment good enough to stop tuning for now while explicitly preserving the right to revisit it later.

Current provisional grid/world direction:

```text
G4 Adaptive Hybrid             SELECTED
Dark mode                      active design baseline
Light mode                     deferred
Randomized currents            retained
Lively current cadence         preferred
Major-grid glints              retained
Glint cadence                  approximately Quiet
Ambient drift                  retained
Localized semantic activity    retained
```

"Provisionally settled" does not mean final production specification or irreversible freeze.

## 2. Next bounded question

The project owner strongly liked the colored work-unit lighting and proposed richer node-specific hover response.

The current hypothesis is:

```text
rest       localized / asymmetric / quiet
hover      fuller node-specific colored response
selected   later persistent focus treatment
runtime    later state-bearing semantic treatment
```

A representative Question node should therefore be able to produce a yellow hover-light response, with other categories using their own representative color.

## 3. Research 044

Current research artifact:

```text
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
```

This research intentionally isolates interaction lighting before the full work-unit grammar is redesigned.

## 4. New browser design lab

```text
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-lighting.html
```

Four treatments are exposed under the same G4 world and representative project fixture.

## 5. H1-H4

```text
H1 Full Halo
    localized asymmetric rest light
    full colored perimeter on hover
    very small depth lift

H2 Cursor Edge
    H1
    + pointer-following/specular hotspot

H3 World Spill
    full hover light
    + nearby grid receives faint node-colored illumination
    + immediate connectors become clearer

H4 Integrated Response
    localized rest light
    full hover halo
    pointer hotspot
    world spill
    connector emphasis
    one restrained perimeter sweep on hover entry
    small depth lift
```

The variants are intended to be decomposed and recombined. Human review does not need to select one literally.

## 6. Important boundaries

Still unresolved:

```text
final work-unit silhouette/shape grammar
final category colors
status vocabulary and status lighting
selected-state visual system
runtime / running / waiting visual system
blocked-state treatment
final dimensions and typography
connector semantic vocabulary
production motion implementation
```

Only hover/interaction lighting is under review here.

## 7. Human review gate

The next expected actor is the project owner.

Review questions:

```text
should full-perimeter colored hover light survive?
is pointer-following light attractive?
should local grid illumination survive?
should immediate connectors respond to hover?
should the one-time perimeter sweep survive?
should rest lighting remain localized/asymmetric?
```

## 8. Production boundary

No production `/cockpit` implementation change is authorized.

Only `frontend/design-lab/**` may contain the experiment.

No graph library, motion library, renderer, route architecture or final design system is selected.

## 9. Source-vault pause remains unchanged

The permanent source-vault bootstrap remains paused, preserved and unchanged. The Course 2 recovery-integrity gate is unaffected.

## 10. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 215
2. treat the current G4 grid/world layer as provisionally settled
3. preserve dark-first sequencing and the current ambient behavior
4. pull the latest branch locally
5. open http://localhost:5173/design-lab/work-unit-lighting.html
6. hover the same colored work units across H1-H4
7. record keep/reject/combine/refine feedback for each lighting mechanism
8. refine once if useful
9. then continue into deeper work-unit visual grammar
10. keep production Cockpit implementation untouched until later integrated evidence warrants promotion
11. keep source-vault deployment paused until the project owner chooses to resume it
```
