# Checkpoint 249: Holistic Integrated Cockpit Baseline Review Opened

**Date:** 2026-08-28  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / INTEGRATION_BASELINE  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Pauses the default component-by-component design-lab workflow and opens holistic human review of one integrated Cockpit reconstruction containing the accepted/held decisions accumulated throughout the current Cockpit design phase.  
**Authority:** Current Phase-C routing/evidence boundary. Previously accepted/held mechanisms remain authoritative at their established level. New shell geometry, HUD composition, map/world dimensions, specialist internals, co-present conversation proportions and other integration glue are provisional until explicitly reviewed.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human process decision

The project owner explicitly requested a change in working mode:

```text
stop adding new isolated component questions for the moment

combine everything accepted from the beginning of the current Cockpit phase
    into one actual Cockpit

review and refine that whole Cockpit

use separate design spaces later only when a new question genuinely needs isolation
```

This is a natural checkpoint because the continuation boundary changed from factorized component exploration to holistic product integration.

## 2. Current primary review surface

Local route:

```text
http://localhost:5173/design-lab/cockpit-integrated-baseline.html
```

Files:

```text
frontend/design-lab/cockpit-integrated-baseline.html
frontend/design-lab/cockpit-integrated-baseline.css
frontend/design-lab/cockpit-integrated-baseline.js
```

Exact initial holistic frontend target:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

Research / audit:

```text
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
```

Production `/cockpit` remains untouched.

## 3. Accepted / held mechanisms reconstructed into the baseline

```text
G4 Adaptive Hybrid project world
H4 hover/world response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation class
D0-D3 semantic directionality
single active connector terminal treatment
P7 Neutral Tag + Tone disposition
Current-process focus lens
conditional runtime semantics
one runtime/BLOCKED operational carrier
Dot + dynamic ring / T7 Soft Shade user switch
BLOCKER -> BLOCKS -> BLOCKED distinction
BLOCKED sharper compact ring
FAIL smoother circular ring
A3 Signal Bars attention
SEL2 four outside corner brackets
X5 balanced two-axis contextual expansion
L0 provisional Flat Fields expanded layout
Z7 Pull-Back Then Dive specialist entry
full-stage specialist workspace end state
clean compact topology compass
S0 Geometric Control provisional zoom behavior
Quiet Graphite Conversation Workspace baseline
project-general and work-unit-scoped conversation distinction
Boxes / Text user-switchable conversation navigation
A6 work-unit context expansion
A6 resting state with no redundant floating mini-box
conversation availability across Grid and Deep Dive
full-focus and co-present conversation capability
source work-state preservation across conversation open/close
compact native Cockpit composer
Jump/search, zoom/recovery and fullscreen capability from Specification 008
```

Exact accepted target SHAs remain indexed in Research 087 and CURRENT_STATE.

## 4. Important integration principle

The integrated browser is reconstructed from accepted invariants, not copied from the latest single design-lab fixture.

This is important because later fixtures occasionally contained known fidelity regressions, such as the historical two-corner SEL2 rendering. Production and integrated baselines should use the accepted target decisions rather than inherit incidental fixture defects.

## 5. Work hierarchy now visible in one product

```text
PROJECT GRID
    compact work units
        -> SEL2 persistent selection
        -> X5 contextual expansion
        -> Z7 Deep Dive

SPECIALIST WORKSPACE
    full-stage analytical work
    topology compass

CONVERSATION
    compact project composer
    full Conversation Workspace
    project-general or work-unit scoped
    A6 contextual expansion
    optional co-presence with the current work surface
```

Conversation remains orthogonal to work depth rather than replacing the conceptual Grid/Deep-Dive hierarchy.

## 6. New shell decisions shown only as provisional integration glue

The browser must have concrete geometry to be reviewable, so it currently uses:

```text
54px compact HUD
2400 x 1500 finite world fixture
2200 x 1320 project-plane fixture
compact right map-tool rail
bottom-center compact composer
project/surface/status/actions HUD composition
provisional 46% co-present chat region
collapsed conversation thread rail in co-present mode
schematic specialist workspace modules
```

These values are NOT promoted. They are now visible so the project owner can judge whole-product geometry instead of speculating about it in isolation.

## 7. Previous Checkpoint 248 disposition

Checkpoint 248 correctly established conversation as orthogonal to work depth.

That model is carried forward into the integrated baseline.

Its separate access/coexistence browser remains useful historical evidence, but it is no longer the primary product review surface.

Likewise, Checkpoint 247's E0-E4 conversation full-focus transitions remain preserved as motion evidence. No Conversation Workspace transition winner has been selected.

## 8. Current human review gate

The current review is holistic rather than candidate-selection-first.

```text
1. pull v1-cockpit-design-exploration
2. open cockpit-integrated-baseline.html
3. use the actual interaction loop rather than inspecting a static screenshot
4. select work units
5. expand X5
6. enter / return from Deep Dive
7. use global and work-unit Conversation entry points
8. switch Boxes / Text
9. expand A6 work-unit context
10. try full-focus and co-present conversation
11. close conversation and verify work state remains
12. inspect map/world scale, HUD, map tools and compact composer
13. note holistic inconsistencies or missing product surfaces
14. refine the integrated Cockpit directly where possible
15. reopen a bounded comparison browser only when a newly exposed question genuinely benefits from factorization
```

## 9. Still unfrozen

```text
final Cockpit shell geometry
final HUD structure and visual treatment
final finite-world dimensions / pan reserve
final stage taxonomy / stage ruler treatment
final map-tool rail styling
final compact-composer geometry
final specialist workspace composition
final topology-compass semantics/details
final Conversation co-present layout and split proportions
resizable split behavior
conversation open/close choreography
conversation persistence/session model
conversation URL state
historical conversation home-state rendering
pinned-context model
non-work-unit conversation homes
final semantic zoom
large-project virtualization/grouping
production frontend component architecture
final production visual identity
```

## 10. Process rule from this checkpoint onward

```text
Integrated Cockpit
    primary product review surface

Bounded design-lab experiments
    supporting evidence tool
    created only when useful to isolate a specific unresolved question
```

This preserves the methodological value of controlled comparisons without allowing the product to remain indefinitely fragmented across separate mockups.
