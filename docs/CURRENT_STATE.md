# Current State

**Checkpoint:** 258  
**Date:** 2026-08-29  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-09
Conversation title       09 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
Collaboration thread     MC-0004
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

```text
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
```

Checkpoint 258 closes the prior human-review gate because the project owner explicitly accepted the Checkpoint 256 / 257 corrected Cockpit for continuation.

Accepted current substrate:

```text
Conversation Boxes spacing
    16px list row gap
    6px top/bottom structural WorkUnit-row padding

current flat Project Grid rail
    Fullscreen present
    Expand selected WorkUnit absent
    Hide project HUD absent

current-process Focus
    unchanged and working

Deep Dive topology compass
    Checkpoint 255 live implementation carried forward unchanged

canonical no-query route
    normal current Cockpit route
```

The newly opened human-review question is:

```text
Does the Adaptive Conversation Dock produce a professional,
native co-present Conversation/Cockpit composition while preserving
the accepted Conversation semantics and source work state?
```

Production `/cockpit` remains untouched.

---

# Whole-product browser and routes

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Accepted current no-query substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Current opt-in human-review candidate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Route roles:

```text
plain route
    accepted current whole-product substrate
    no adaptive Conversation integration study mounted

?conversation=adaptive-dock
    current opt-in whole-product Conversation co-presence candidate
    not yet accepted as default

?edge=none
    internal regression-only earlier-shell substrate
    not a product route or design candidate

explicit ?edge=... / ?rail=...
    historical rail-study routes
    isolated from the current default flat rail
```

The source-faithful integrated Cockpit remains the protected whole-product design substrate. New shell/composition decisions are evaluated on this complete browser rather than in disconnected fixtures.

---

# Adaptive Conversation Dock candidate

## Problem being tested

The prior co-present implementation used a wide right-side Conversation surface while also keeping the permanent Conversation thread rail visible inside it. Human review of the integrated Cockpit showed that this reads as two complete applications placed beside one another rather than one coherent professional workbench.

The semantic Conversation architecture is not reopened. Research 086 already established that these axes are orthogonal:

```text
work context
    Grid / X5 / Deep Dive

Conversation presentation
    compact composer / full-focus / co-present

Conversation scope
    project-general / WorkUnit
```

Exact co-present split geometry, resizing and pane persistence remained open.

## Candidate behavior

Full-focus Conversation remains source-faithful Quiet Graphite with the persistent Boxes/Text thread rail.

Co-present Conversation becomes a compact secondary dock:

```text
default width       clamp(520px, 38vw, 650px)
position            right side
resize              direct left-edge resize + keyboard separator support
Cockpit hierarchy   majority visible / primary
thread navigation   hidden by default
Threads             invokes the same accepted Boxes/Text rail as a drawer
A6                  available as invoked inspector sheet
composer             project-aware source-faithful composer retained
```

This is a presentation adaptation only. It does not change conversation ownership, project selection, X5, Deep Dive source state or semantic project state.

## Implementation artifacts

```text
frontend/design-lab/cockpit-conversation-integration-study.css
frontend/design-lab/cockpit-conversation-integration-study.js
frontend/design-lab/cockpit-spatial-rail-study-gen2-anchor.js
frontend/e2e/cockpit-reintegration-conversation-integration-study.spec.ts
```

---

# Deterministic fidelity status

Implementation target:

```text
00957b684cbc57dad11561f7ed262faf1bba4383
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33238181528
job           99062775945
result        SUCCESS
browser tests 71 / 71 passing
```

The gate now verifies all previous 68 source-faithful Cockpit contracts plus:

```text
plain route remains outside the adaptive study
adaptive route mounts compact co-present dock geometry
Threads invokes the held Boxes/Text rail instead of permanently nesting it
dock resize does not mutate selected project state
full-focus restores persistent thread navigation
open / resize / presentation switch / close preserve source work state
```

A green deterministic gate protects implementation integrity. It does not decide whether the candidate feels professionally correct.

---

# Held Conversation semantics remain intact

```text
Quiet Graphite baseline
project-general + WorkUnit-scoped conversation
Boxes / Text user-switchable thread navigation
A6 Adaptive Anchor
no redundant A6 floating home card
Conversation access from Grid neutral / selected / X5 / Deep Dive
full-focus + co-present capability
source work-state preservation
Conversation ownership separate from SEL2 selection
compact native Cockpit composer
```

Checkpoint 258 changes none of these. It evaluates only the co-present composition and persistence of navigation within that composition.

---

# Other held Phase-C decisions remain intact

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation-class carrier
D0-D3 semantic directionality
single active connector terminal treatment
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
one switchable operational carrier
T7 Soft Shade runtime tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 four outside corner brackets
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working internal-layout default
Z7 Pull-Back Then Dive specialist-workspace entry
full-stage specialist workspace
compact topology compass retained
S0 Geometric Control provisional zoom working default
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

L0 remains provisional. Semantic zoom remains deferred. No current-process Focus implementation was changed.

Important exact accepted implementation provenance remains governed by:

```text
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

---

# Implementation-provenance recovery remains complete

```text
23 manifest entries
19 required MUST_PORT / MUST_PRESERVE
4 deliberately non-promotable records
```

First exact-history provenance proof:

```text
workflow run 33156357834
result       PASS
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only and must never be used as an accepted visual source or parent implementation.

`docs/cockpit/PHASE_C_DECISION_LEDGER.md` remains exhaustive for its declared Research 037-088 scope. Later reintegration and whole-product studies are preserved in Research 089 onward, checkpoints and current routing.

---

# Deferred / paused work remains unchanged

```text
semantic zoom
    DEFERRED
    S0 geometric control remains the provisional working default

source-vault bootstrap
    PAUSED
    not cancelled or rejected

Course 2 source-universe gate
    unchanged
```

---

# Exact next step

```text
Human visually reviews the Adaptive Conversation Dock on the opt-in route.

Review:
    Cockpit versus Conversation hierarchy
    default dock width
    Threads drawer behavior
    resize behavior
    compact co-present header/composer
    full-focus restoration
    A6 inspector if exercised

If good:
    preserve explicit acceptance / tuning values
    decide whether to make the adaptive dock the normal co-present presentation

If wrong:
    challenge or replace the adaptive-dock composition family
    do not reopen held Conversation semantics
    keep the accepted plain Cockpit substrate unchanged
```
