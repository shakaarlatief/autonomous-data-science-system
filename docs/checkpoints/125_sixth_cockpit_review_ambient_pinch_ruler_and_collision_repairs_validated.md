# Checkpoint 125: Sixth Cockpit Review, Ambient/Pinch/Ruler/Collision Repairs Validated

**Date:** 2026-08-21  
**Status:** Historical design/implementation checkpoint; Specification 007 remains candidate pending another real-browser human product review, with real laptop pinch feel still requiring direct human validation  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 professional frontend exploration  
**Scope:** Preserves the sixth real-browser Cockpit review and the ambient-continuity, pinch-stability, stage-ruler, and Jump/composer collision repair gate.  
**Authority:** Historical product/design provenance. Later Cockpit research, checkpoints, and Specification 008 govern the promoted current interaction architecture and later human-review status.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Focus of this checkpoint

This checkpoint preserves the sixth real-browser human review of the Project Cockpit and the bounded implementation/validation iteration that followed it.

The review began from the passing fifth-review Cockpit candidate and focused on four concrete defects visible in real use:

```text
ambient depth revealed the old project-plane box at low zoom
native two-finger pinch zoom was functionally correct but visibly jumpy
Framing/Evaluation stage-ruler terminals were geometrically inconsistent
Jump-to/search could overlap the persistent system composer
```

The user again assessed the overall Cockpit direction positively and described the product as making real progression.

The pinch observation was supported by an uploaded 13.55-second 1920x1080, 30-fps browser recording, so the defect was treated as temporal interaction evidence rather than inferred from static screenshots alone.

---

## 2. Human-review findings

### 2.1 Ambient depth must belong to the navigable world

The fifth review correctly changed the spatial model to:

```text
finite navigable grid world
    contains
        semantic project plane
```

However, the CSS still rendered a second radial ambient layer on the smaller `ProjectCanvas`.

At reduced zoom that smaller glow ended at the project-plane edge and visually reconstructed the box the design was trying to eliminate.

The bounded resolution is:

```text
ProjectWorld
    owns workspace-level grid and ambient depth

ProjectCanvas
    owns semantic stage regions / nodes / connectors
    does not own a second clipped workspace-atmosphere layer
```

This preserves the restrained atmospheric design language that received positive human review while removing a non-semantic implementation boundary from the visible product.

### 2.2 Pinch zoom must be temporally stable, not merely eventually correct

The prior implementation transformed each native `ctrlKey + wheel` pinch event directly into a scale change. The uploaded video showed that this technically worked but felt too jumpy for a spatial analytical workspace.

The refined browser-input pipeline is:

```text
native pinch/wheel events
    -> normalize delta units
    -> accumulate a short burst within one animation frame
    -> clamp pathological per-frame delta
    -> apply conservative exponential scale
    -> use immediately current zoom state
    -> preserve the gesture anchor approximately
    -> supersede obsolete pending anchor-correction frames
```

The implementation now maintains an immediate zoom ref in addition to React state, coalesces native pinch input per animation frame, bounds extreme deltas, uses lower sensitivity, and keeps the gesture anchored around the pointer location as layout changes.

This is still a candidate browser/native-input solution. Automated synthetic wheel events cannot establish whether the gesture now feels correct on the user's actual laptop trackpad.

### 2.3 Stage-ruler terminals should use authoritative rendered semantic geometry

The fifth-review stage ruler correctly became vertically viewport-aware while remaining horizontally aligned with project semantics.

Its horizontal position/width was nevertheless inferred from canvas width and logical zoom. At minimum CSS zoom this did not agree with the actual rendered stage-region boundaries, which produced the visible Framing/Evaluation terminal inconsistency.

The first sixth-review CI attempt quantified the mismatch at approximately:

```text
left terminal delta   ~84 px
right terminal delta ~182 px
```

The implementation now derives ruler geometry directly from the rendered semantic stage regions:

```text
ruler left
    = rendered left edge of Framing

ruler right
    = rendered right edge of Evaluation
```

Terminal stage labels and underline insets use the same rules as the middle stages.

Neutral world reserve outside the semantic project plane therefore stays visually neutral rather than appearing to be accidental extra Framing/Evaluation space.

### 2.4 Jump/search must respect the composer as an explicit safe area

The scalable Jump-to/search interaction remains the correct direction, but a long result list could descend into the persistent system composer at laptop-height viewports.

That made lower results harder to inspect or select and violated the existing collision-safety requirement.

The bounded repair treats the composer as a real viewport-safe-area occupant:

```text
upper Cockpit chrome
    ↓
Jump/search palette
    bounded max height
    internally scrolling result list
    ↓
explicit gap
    ↓
persistent composer
```

At the supported 1024x768 boundary, the palette now remains above the composer and its lowest representative result remains reachable/selectable.

---

## 3. Bounded implementation resolution

Implemented on temporary validation branch:

```text
v1-frontend-spike-review6
```

Changes include:

```text
ambient continuity
    world-owned radial atmosphere
    ProjectCanvas ambient pseudo-layer removed

pinch interaction
    zoomRef for immediately current scale
    delta-mode normalization
    animation-frame coalescing
    bounded per-frame delta
    reduced sensitivity
    anchored zoom correction
    obsolete correction-frame cancellation

stage ruler
    geometry sourced from rendered Framing/Evaluation boundaries
    consistent terminal title/underline treatment

Jump/search
    fixed collision-safe placement adjacent to right tool rail
    viewport-derived maximum height
    independently scrolling results
    composer separation preserved at 1024x768
```

No graph/canvas framework or gesture library was introduced.

---

## 4. Validation history

### 4.1 First sixth-review validation attempt

Initial repair head:

```text
39a2fea181ceebb286f2775eee6d409a45df76b1
```

Workflow:

```text
V1 frontend spike
run number: 138
run id: 32474789703
```

Results:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser gate
    FAIL
```

The browser failure contained two different kinds of evidence.

#### Genuine implementation defect

The stage-ruler alignment was still calculated from inferred CSS-zoom geometry and failed to align with the rendered terminal semantic stages.

This was a real product defect and was fixed by using the rendered stage-region boundaries directly.

#### Invalid synthetic assertion

The first pinch regression test required every small synthetic pinch event to produce a strictly larger rounded integer percentage label.

That assertion was not a valid smoothness criterion. Distinct small continuous zoom values can legitimately round to the same displayed percentage.

The product sensitivity was deliberately **not** increased merely to make the integer label change on every event.

The corrected gate instead measures:

```text
small initial scale increment
bounded cumulative progression
approximate gesture-anchor preservation
absence of a large per-event jump
```

### 4.2 Corrected validation

Validated implementation head:

```text
a2e401408c55a74905e0654c40185f4f9990becc
```

Workflow:

```text
V1 frontend spike
run number: 140
run id: 32475241980
```

Final results:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The validated head was fast-forwarded into:

```text
v1-frontend-spike
```

GitHub therefore records validation PR #5 (`Repair sixth Cockpit review interaction defects`) as merged at the same validated head.

---

## 5. New automated evidence

The sixth-review regression gate now establishes that:

```text
ambient radial depth exists on ProjectWorld
ProjectCanvas no longer owns a competing clipped ambient pseudo-layer

stage ruler begins at the rendered Framing boundary
stage ruler ends at the rendered Evaluation boundary
terminal ruler title/underline styles are consistent

small synthetic pinch input produces a small zoom increment
pinch remains approximately anchored to the chosen work unit
repeated pinch input yields bounded cumulative zoom progression

Jump/search stays above the persistent composer at 1024x768
its results region scrolls independently
its lowest representative result remains selectable
```

Existing gates continue to cover the previously established Cockpit behaviors including 2D movement, minimum-zoom panning, explicit zoom/fit/reset, searchable project navigation, Data/EDA/Missingness focus, URL/browser-history behavior, fold-away chrome, fullscreen, collision recovery, accessibility, and cross-platform build/unit behavior.

---

## 6. Promotion audit

### Promote into the active candidate contract

The following requirements have enough human evidence plus executable support to strengthen Specification 007:

```text
workspace-level ambient depth must not reveal semantic sub-plane clipping
native pinch processing should be temporally bounded/coalesced and approximately anchored
stage-ruler terminal geometry should follow authoritative semantic/rendered boundaries
Jump/search must honor the composer as a collision-safe viewport boundary
```

These are candidate interaction requirements, not final implementation-technology decisions.

### Do not promote as final architecture

Do not infer selection or freezing of:

```text
React Flow or another graph/canvas framework
final gesture library
final pinch/wheel normalization constants
final geometric zoom range
final auto-layout algorithm
final semantic-zoom algorithm
final minimap
final stage taxonomy
final project-search backend
final Cockpit visual identity
exact permanent ambient-gradient geometry
canonical Cockpit screenshot baseline
```

The current evidence still does not justify introducing a dedicated graph/canvas or gesture dependency.

---

## 7. Exact continuation

The immediate next Cockpit step is another real-browser human product gate against the corrected sixth-review implementation.

The review should explicitly test:

```text
ambient circles/glow no longer reveal a smaller hidden project box
Framing and Evaluation ruler terminals remain intentional across zoom/pan
Jump/search stays comfortably separate from the composer and lowest results are easy to select

real laptop trackpad pinch:
    slow pinch in
    slow pinch out
    faster pinch in/out
    pinch around different project regions
    switch immediately between two-finger pan and pinch
    judge whether the visual anchor remains understandable
```

The automated gate proves bounded geometric behavior, but **real laptop pinch feel remains open until human review**.

If the corrected interaction is strongly accepted, perform a deliberate Specification 007 promotion decision rather than continuing visual iteration automatically.

Other active V1 tracks remain unchanged:

```text
governed PostgreSQL reusable-knowledge round-trip closure
agent-runtime bakeoff
retrieval / MethodologicalHorizon benchmark
```
