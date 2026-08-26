# Checkpoint 117: Unified Cockpit Workspace Direction Confirmed

**Date:** 2026-08-20  
**Status:** Historical design and product-architecture checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 professional frontend exploration  
**Scope:** Records human confirmation of the spatial click-to-focus Cockpit interaction and the stronger requirement that deep Data/EDA/Validation/Modeling work should be executable inside the same immersive Cockpit experience when technically sound, while preserving direct specialist navigation as an alternative entry path.  
**Authority:** Historical rationale and current design direction only. Research 002 and Research 003 explain the active hypothesis; no final Cockpit interface specification or canvas library is accepted by this checkpoint.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Human review result

Human review strongly confirmed the following interaction as matching the intended product experience:

```text
click a project/work block
    -> smoothly zoom/focus into it
    -> perform real analytical work
    -> return smoothly to the surrounding project context
```

The follow-up requirement was stronger than the earlier Research 002 wording.

The user does not want the Cockpit to become a shallow map that inevitably hands off to normal pages for any serious analysis if a professional scalable architecture can avoid that.

The desired experience is:

```text
Cockpit
    -> Data
    -> EDA
    -> Validation
    -> Features
    -> Models
    -> Experiments
    -> Evaluation
    -> evidence / decisions / reporting
```

through a continuous focus/transition interaction where practical, without visible browser-style page loading.

At the same time, the existing project-navigation views remain valuable and should continue to support direct entry into Data, EDA, Decisions & History, and later specialist areas.

---

## 2. Technical feasibility conclusion

This requirement is compatible with a professional production frontend.

The system does not need to choose between:

```text
smooth immersive Cockpit
```

and:

```text
scalable modular software architecture
```

The implementation can preserve both by separating internal navigation from visible interaction.

A persistent SPA shell can update route/view state, mount or lazy-load a specialist analytical module, fetch data, and preserve browser history while the user sees a smooth spatial focus transition rather than a traditional page jump.

The key rule is:

```text
visible continuity
    !=
keep the entire application permanently rendered
```

---

## 3. Reusable specialist surfaces

The preferred architecture is now:

```text
DataWorkspace
EDAWorkspace
ValidationWorkspace
FeatureWorkspace
ModelWorkspace
ExperimentWorkspace
EvaluationWorkspace
...
```

with each workspace reusable in two hosts:

```text
CockpitFocusHost
    immersive transition from project map

SpecialistRouteHost
    direct navigation / inspection entry point
```

This avoids duplicate implementations.

The same Data or EDA capability can therefore be reached either by spatially focusing from the Cockpit or by selecting Data/EDA directly from project navigation.

---

## 4. Important implementation boundary

The detailed workspace should not literally remain a tiny graph node that is permanently CSS-scaled up.

Preferred behavior:

```text
node identifies transition origin
    -> project canvas recedes
    -> normal full-resolution DOM work surface becomes active
    -> reverse transition returns to node/project context
```

This preserves the desired spatial illusion while allowing normal tables, charts, forms, accessibility, scrolling, responsive layouts, and bounded rendering.

The macro project map and micro analytical workbench should therefore remain separate rendering regimes joined by transition.

---

## 5. Scalability requirements established by this review

A complete Cockpit must still enforce:

```text
lazy/code-split analytical modules
bounded project-map projection
no full project-object graph in the DOM
backend pagination/streaming for large data
virtualization only as a rendering optimization
route-addressable focus state
browser back/refresh/deep-link reconstruction
run lifecycle independent of React component lifecycle
accessibility and reduced-motion alternatives
animation optional for correctness
```

The Cockpit may make the reachable product surface enormous while the currently mounted/rendered surface remains bounded.

---

## 6. Product model after this checkpoint

```text
AUTONOMOUS DATA SCIENCE SYSTEM

Project Cockpit
    primary immersive active-work environment
    project map + conversation + system activity
    smooth focus into complete specialist analytical surfaces

Overview / Data / EDA / Validation / Features / Models / ...
    direct information/inspection entry paths
    reuse the same project modules and state
```

This is intentionally not framed as Cockpit versus pages.

It is:

```text
one project system
    +
two complementary navigation/interaction modes
```

The Cockpit presents the project as a living process.

The project navigation presents it as an inspectable information system.

---

## 7. Research preservation

Detailed design basis:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
```

Research 003 specifically records:

```text
SPA/no-reload feasibility
spatial handoff rather than literal permanent scaling
dual Cockpit/direct-route hosting
route-addressable focus state
code splitting/lazy loading
large-data/backend rules
hierarchical but bounded focus depth
state separation
run-lifecycle separation
conversation focus context
accessibility
performance strategy
non-goals
next mockup scenarios
```

---

## 8. Promotion audit

### New Foundation?

No.

Foundation 021 already makes the frontend a first-class product/reasoning/control surface. This checkpoint makes one interaction direction much more concrete but does not yet justify a new durable Foundation.

### New principle?

Not yet.

The important scalability rules are implementation/design constraints under the current frontend exploration. They should be promoted only if the upcoming Cockpit prototypes confirm them as durable across interface variants.

### New accepted decision?

Not yet.

The user has strongly confirmed the desired experience, but the exact interaction architecture has not yet been demonstrated through realistic prototypes and performance/accessibility tests. It is therefore recorded as a strongly preferred design direction rather than a final D-series technology/interface decision.

### New specification?

Not yet.

Specification 006 remains the candidate frontend architecture/visual spike contract. A later Cockpit-specific specification is justified only after the next concepts prove the navigation/focus model with realistic Data and EDA depth.

---

## 9. Next bounded frontend design task

The next Cockpit prototype should prove depth, not only appearance.

At minimum demonstrate:

```text
Scenario A
project map
    -> Missingness investigation
    -> smooth focus transition
    -> full EDA-quality missingness workspace
    -> detailed variable/evidence interaction
    -> scoped system interaction
    -> project state change
    -> smooth return to map

Scenario B
project map
    -> Data understanding
    -> full Data workspace
    -> variable selection
    -> filter/sort/pagination or representative data interaction
    -> return to project map
```

The prototype must test whether the user can do real work for an extended period without feeling that the Cockpit is merely a launch screen.

Only after this should the project decide whether a node-canvas library, the browser View Transition API, a specific animation library, or an exact route/focus schema belongs in the accepted V1 interface architecture.
