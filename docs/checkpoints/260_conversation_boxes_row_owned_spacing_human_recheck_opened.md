# Checkpoint 260: Conversation Boxes Row-Owned Spacing Human Recheck Opened

**Date:** 2026-08-29  
**Status:** Current human-review checkpoint  
**Checkpoint class:** CONTINUITY / PRESENTATION_INTEGRITY / HUMAN_RECHECK  
**Scope:** Conversation Boxes visible separation on the normal and Adaptive Conversation routes. Current-process Focus is carried forward unchanged and is not under active repair.  
**Authority:** The project owner's direct visual review is authoritative for whether the accepted spacing is actually visible. Checkpoint 256 remains authoritative for the intended spacing target and canonical WorkUnit footprint.  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Project / workspace:** Autonomous Data Science System  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT

## 1. Boundary transition

Checkpoint 259 opened a human stability confirmation after repairing two intermittent presentation-state failures.

The project owner's retest produced:

```text
current-process Focus
    working as far as tested

Conversation Boxes
    still missing the original visible spacing
```

The supplied screenshots make the Conversation failure concrete: the canonical WorkUnit artifacts still read as visually joined rather than as separate conversation objects.

Accordingly:

```text
Focus branch of Checkpoint 259
    human evidence currently positive
    no further Focus change in this pass

Conversation branch of Checkpoint 259
    human confirmation FAILED
    implementation investigation continued
```

Research 099 preserves the correction and recovery.

## 2. Important correction to the prior diagnosis

Research 098's stale-selector finding was real but incomplete.

The integrated Phase-C completion adapter also restores `.is-workunit-thread` to canonical WorkUnit rows. Therefore selector drift alone could not explain the persistent local visual failure.

The stronger issue was that visible spacing still depended on parent grid geometry and on the exact canonical rail-state string, even though the current Conversation UI resolves every non-Text state as Boxes/artifact.

The new recovery removes that dependency.

## 3. Current spacing contract

The intended visual amount is not redesigned.

The geometry is now expressed as:

```text
Conversation list row-gap      0px
project row bottom margin     16px
WorkUnit top padding           6px
WorkUnit bottom padding        6px
WorkUnit bottom margin        16px
last WorkUnit bottom margin    0px
canonical WorkUnit footprint   unchanged
```

The important architectural change is ownership:

```text
before
    separation substantially depended on the parent grid

after
    every conversation object owns the space after itself
```

This makes the breathing room structural and local to the rows that must remain visually distinct.

## 4. Boxes / artifact compatibility

Current CSS protects every non-Text Conversation rail state:

```text
html:not([data-conversation-rail="text"])
```

This covers both the current `boxes` representation and historical `artifact` state.

The screenshot does not establish that the project owner's exact runtime state was `artifact`; this checkpoint does not claim that. The point is that a state the current UI itself interprets as Boxes can no longer bypass the spacing contract.

## 5. Deterministic validation

Implementation target:

```text
29419f7a1ccbd3cbcdc98f333e1b594c01d63fb1
```

Complete Cockpit fidelity workflow:

```text
workflow run  33241369935
job           99071179670
result        SUCCESS
browser tests 74 / 74 passing
```

The new test specifically adds:

```text
1536 x 864 user-like viewport
legacy data-conversation-rail="artifact" runtime state
Boxes control still visually selected
row-owned spacing preserved
actual rendered WorkUnit separation preserved
```

Existing normal-route, narrow-route, Adaptive Dock, source-faithful mechanism and Focus lifecycle tests all remain green.

## 6. Focus boundary

No Focus file was modified for Checkpoint 260.

The current human evidence says Focus is working. Research 098's membership/remount synchronization repair therefore remains the current implementation.

Do not reopen Focus unless a new concrete reproduction appears.

## 7. Adaptive Conversation Dock disposition

The Adaptive Conversation Dock remains:

```text
OPEN PRODUCT-DESIGN CANDIDATE
NOT promoted
NOT rejected
```

Product judgment remains temporarily paused only because the underlying Boxes rail must be visually trustworthy before judging the larger Conversation composition.

No Conversation ownership, scope, Boxes/Text semantics, A6 behavior, source-state preservation or Adaptive Dock geometry was changed by this spacing pass.

Production `/cockpit` remains untouched.

## 8. Exact next step

The next actor is the human reviewer.

Pull the latest branch state and hard-refresh the browser, then inspect Boxes on:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html

http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Required result:

```text
project-general artifact
    visibly separated from first WorkUnit

every WorkUnit
    visibly separated from the next WorkUnit

Focus
    continues to behave as in the successful retest
```

If the visible spacing is now correct:

```text
close Checkpoint 260
resume Checkpoint 258 Adaptive Conversation Dock visual review
```

If it is still wrong:

```text
preserve the screenshot and exact route/state
keep Adaptive Dock judgment paused
continue only the Conversation rail presentation-integrity investigation
```
