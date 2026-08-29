# Checkpoint 256: Structural Conversation Spacing and Project Tool Rail Controls Review Opened

**Date:** 2026-08-28  
**Status:** Current human-review checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / WHOLE_PRODUCT_CORRECTION  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Scope:** Records the Checkpoint 256 correction candidate for structural Conversation WorkUnit separation and the visible control set of the current compact flat Project Grid rail.  
**Authority:** Historical design provenance. Later checkpoints and current routing govern active state; this checkpoint does not alter held Phase-C semantics and records the review boundary as understood at that time.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT  
**Collaboration thread:** `MC-0004`

## 1. Boundary transition

Checkpoint 255 opened review of Conversation spacing, the flat 2D Project Grid rail and the live topology compass.

The project owner then confirmed two remaining presentation corrections:

```text
Conversation WorkUnit boxes still appeared visually joined after pulling latest GitHub state.
The current flat rail should restore Fullscreen and remove Expand selected WorkUnit + Hide project HUD.
```

The project owner also explicitly clarified:

```text
Current-process Focus is working correctly.
Do not modify Focus in this pass.
```

Research 096 preserves the diagnosis and implementation evidence.

## 2. Conversation spacing correction

The prior row-gap-only approach was insufficient because the canonical Conversation WorkUnits are transformed/scaled inside rail slots. Visual content could therefore consume apparent separation even while the parent list reported a valid gap.

Checkpoint 256 changes the layout contract to reserve real row geometry:

```text
thread-list row gap      16px
WorkUnit row padding      6px top + 6px bottom
canonical WorkUnit size   unchanged
```

The deterministic gate now measures actual rendered WorkUnit surfaces at both 1600px and 760px viewport widths.

Required visible geometry:

```text
project-general -> first WorkUnit >= 16px
WorkUnit -> next WorkUnit       >= 20px
```

## 3. Current flat rail control set

The visible current candidate now contains:

```text
Jump / search
Zoom out
zoom readout
Zoom in
Fit project
Reset view
Deep Dive
Current process focus
Conversations
Appearance
Fullscreen
Tool labels
```

Explicitly removed from this rail composition:

```text
Expand selected WorkUnit
Hide project HUD
```

This is a shell-composition decision only. X5 expansion remains an accepted mechanism and immersive/fold-away chrome remains part of the promoted Cockpit architecture.

## 4. Focus boundary

No Focus behavior, styling or semantics were changed.

The accepted M09 current-process focus lens remains intact and the project owner explicitly reports it as working correctly.

## 5. Carried-forward compass state

The Checkpoint 255 live topology compass remains unchanged and continues to be part of the corrected integrated substrate.

It still:

```text
reads actual mounted WorkUnits
renders actual relation links
highlights the selected source WorkUnit
updates with selection
never owns or mutates selection
```

## 6. Deterministic validation

Implementation target:

```text
e2768a807b2a80f438248a25f7d41e53be561d51
```

Complete browser gate:

```text
workflow run  33211613408
job           98985900484
result        SUCCESS
browser       68 / 68 passing
```

New checks cover:

```text
visible WorkUnit spacing at desktop width
visible WorkUnit spacing at narrow width
Fullscreen visible in current flat rail
Expand selected WorkUnit absent from current flat rail
Hide project HUD absent from current flat rail
same rail control set after clarity expansion
```

All prior source-faithful Cockpit mechanisms remain green.

## 7. Current human-review gate

The next actor is the human reviewer.

Review:

```text
1. Conversation Boxes spacing at the actual local viewport
2. current flat right-side rail control set
```

If those two surfaces are visually correct, preserve acceptance and continue whole-product Cockpit design from this corrected substrate.

Production `/cockpit` remains untouched.
