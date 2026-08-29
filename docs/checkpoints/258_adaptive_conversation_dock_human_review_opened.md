# Checkpoint 258: Adaptive Conversation Dock Human Review Opened

**Date:** 2026-08-29  
**Status:** Current human-review checkpoint  
**Checkpoint class:** DESIGN / CONTINUITY  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Scope:** Records acceptance-for-continuation of the Checkpoint 256/257 Cockpit corrections and opens human review of the opt-in Adaptive Conversation Dock candidate for professional Conversation/Cockpit co-presence.  
**Authority:** Historical/current-boundary provenance. Held semantic/product decisions remain governed by accepted specifications, foundations and explicit prior selections; this checkpoint does not promote the Adaptive Conversation Dock before human review.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-10`  
**Conversation title:** `10 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT  
**Collaboration thread:** `MC-0004`

## 1. Boundary transition

The project owner visually reviewed the current canonical Cockpit and explicitly confirmed:

```text
Checkpoint 256 Conversation Boxes spacing
    good / accepted for continuation

Checkpoint 256 current flat Project Grid rail control set
    good / accepted for continuation

Checkpoint 257 canonical no-query route
    continue from this normal route
```

This closes the prior human-review gate. The accepted current substrate therefore retains:

```text
16px Conversation list gap
6px top/bottom structural WorkUnit-row padding
Fullscreen in the current flat rail
Expand selected WorkUnit absent from that rail
Hide project HUD absent from that rail
current-process Focus unchanged and working
Checkpoint 255 live topology compass unchanged
```

No production promotion occurs merely from this acceptance-for-continuation.

## 2. Newly opened whole-product question

The next issue was observed in the complete Cockpit rather than a detached fixture.

The existing co-present Conversation surface occupies a wide portion of the right side and includes the permanent Conversation thread rail inside that surface. In the supplied human screenshot, this makes the composition read like two complete applications placed beside each other rather than one coherent professional Cockpit.

The reopened question is therefore narrow:

> **How should the already-held Conversation Workspace coexist with active Cockpit work in co-present mode so that the Cockpit remains primary and the result feels like one professional analytical workbench?**

The following remain held and are not reopened:

```text
Quiet Graphite visual baseline
project-general + WorkUnit-scoped conversations
Boxes / Text thread navigation semantics
A6 Adaptive Anchor
Grid + X5 + Deep Dive Conversation access
full-focus + co-present capability
source work-state preservation
```

## 3. Research basis

Research 097 combines:

```text
internal Conversation design evidence from Research 079 and 081-086
human screenshot diagnosis on the integrated Cockpit
current professional-workbench references from VS Code and Notion
whole-product implementation rather than a disconnected mockup
```

The key internal architectural fact from Research 086 is that work context, Conversation presentation and Conversation scope are orthogonal axes. Exact co-present split geometry, resizing and pane-collapse behavior remained open.

## 4. Current review candidate: Adaptive Conversation Dock

The current candidate deliberately differentiates full-focus and co-present presentation.

### Full focus

The source-faithful Quiet Graphite Workspace remains the primary stage owner and keeps its persistent thread rail.

### Co-present

Conversation becomes a compact native secondary dock:

```text
right-side dock
width clamp(520px, 38vw, 650px)
resizable from the left edge
Cockpit retains majority of visible width
thread rail hidden by default
Threads control invokes the same accepted Boxes/Text rail as a temporary drawer
A6 remains available as an invoked inspector sheet
project-aware composer retained
```

The candidate changes presentation hierarchy only. It does not create new Conversation ownership or project-state semantics.

## 5. Review route isolation

The new candidate is intentionally opt-in:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

The accepted current substrate remains unchanged on:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

This separation is deliberate. The new co-presence geometry must earn human acceptance before it becomes the default.

## 6. Deterministic evidence

Implementation target:

```text
00957b684cbc57dad11561f7ed262faf1bba4383
```

Complete Cockpit fidelity workflow:

```text
workflow run  33238181528
job           99062775945
result        SUCCESS
browser tests 71 / 71 passing
```

The 71-test gate contains all previous 68 source-faithful Cockpit tests plus three new tests for the adaptive study.

It verifies:

```text
plain canonical route remains outside the adaptive study
compact co-present dock geometry activates only on the opt-in route
thread rail is invoked rather than permanently nested in co-present mode
Boxes / Text remains available through the same source-faithful rail
dock resizing preserves selected project state
full-focus restores persistent Conversation navigation
opening / resizing / switching presentation / closing does not mutate source work state
```

A green gate does not imply aesthetic acceptance.

## 7. Current human-review gate

The next actor is the human reviewer.

Review the opt-in candidate at the actual local viewport and judge the whole composition:

```text
Cockpit versus Conversation visual hierarchy
default dock width and amount of visible project world
whether Threads-as-drawer feels natural
whether resizing is useful and restrained
whether the co-present header/composer feel integrated
whether full-focus remains the correct long-form Conversation destination
whether A6 remains understandable from the compact dock
```

If the direction is good:

```text
preserve explicit acceptance
refine only concrete tuning that human review identifies
then consider whether the adaptive dock should replace the current default co-present geometry
```

If the direction is wrong:

```text
challenge the adaptive-dock composition family
keep the accepted Conversation semantic architecture intact
keep the canonical no-query Cockpit unchanged until a replacement earns review
```

Production `/cockpit` remains untouched.
