# Checkpoint 259: Cockpit Presentation-State Integrity Recovery

**Date:** 2026-08-29  
**Status:** Current verification / human-confirmation checkpoint  
**Checkpoint class:** DESIGN / VERIFICATION / CONTINUITY  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Scope:** Records recovery and deterministic verification of intermittent Conversation Boxes spacing and current-process Focus presentation failures reported during Checkpoint 258 review.  
**Authority:** Current-boundary provenance. This checkpoint repairs implementation integrity for already-held presentation behavior; it does not reopen or replace accepted Conversation spacing values, M09 Focus semantics, or the Adaptive Conversation Dock design question.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT  
**Collaboration thread:** `MC-0004`

## 1. Human-reported failures

During initial review of the Adaptive Conversation Dock, the project owner paused design evaluation because two older surfaces were intermittently unstable:

```text
Conversation Boxes spacing
    accepted gaps sometimes disappeared again

current-process Focus
    sometimes correct
    sometimes boxes failed to recess
    sometimes only relation lines recessed
```

Because both states had previously appeared correct and then regressed without an intentional design change, the task was treated as a presentation-state integrity investigation.

## 2. Root causes

Research 098 records the detailed diagnosis.

The Conversation defect included selector drift:

```text
current renderer identity     data-thread-scope="work"
Checkpoint 256 padding rule   .is-workunit-thread
```

The accepted spacing guarantee also depended on a stylesheet mounted through a separate late-loaded rail module.

The Focus defect included lifecycle asymmetry:

```text
WorkUnit focus membership     initialized once
relation focus classes        continuously resynchronized
```

A WorkUnit carrier remount could therefore leave node recession and relation recession out of sync. Focus CSS was also runtime-injected rather than statically present in the integrated stylesheet graph.

## 3. Recovery

Implemented recovery:

```text
Conversation
    static presentation-integrity stylesheet
    16px Boxes row gap guaranteed
    6px top/bottom WorkUnit-row padding guaranteed
    current data-thread-scope="work" selector used
    historical class selector retained only as compatibility fallback

Focus
    focus stylesheet statically linked
    accepted recession rules protected from later study-style precedence
    authoritative membership set independent of DOM carriers
    WorkUnit remount observer repairs data-process-scope
    replacement membership controls restored
    relation classification resynchronized after repair
```

No semantic project state was changed.

## 4. Deterministic evidence

Implementation target:

```text
0374d624ec0e88d65060fb2424ce18291ca40792
```

Complete Cockpit fidelity workflow:

```text
workflow run  33240152004
job           99067985262
result        SUCCESS
browser tests 73 / 73 passing
```

The two new tests explicitly cover:

```text
Adaptive Conversation full-focus / co-present / Threads-drawer spacing lifecycle
Boxes -> Text -> Boxes spacing recovery
static Focus stylesheet readiness
repeated process-focus switching
node/relation recession agreement
WorkUnit DOM replacement and membership recovery
```

All previous 71 source-faithful Cockpit tests remain green.

## 5. Current boundary

The Adaptive Conversation Dock candidate remains opt-in and unaccepted as a default:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

The normal current substrate remains:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Checkpoint 259 temporarily places one human confirmation gate in front of further adaptive-dock judgment:

```text
confirm Conversation spacing no longer collapses intermittently
confirm Focus no longer desynchronizes boxes from relations
```

If both remain stable in normal use, return immediately to the Checkpoint 258 Adaptive Conversation Dock visual review. No additional design decision is required for the repaired mechanisms.

Production `/cockpit` remains untouched.
