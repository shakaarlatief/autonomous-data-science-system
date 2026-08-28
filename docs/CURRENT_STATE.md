# Current State

**Checkpoint:** 256  
**Date:** 2026-08-28  
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
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

```text
docs/checkpoints/256_structural_conversation_spacing_and_project_tool_rail_controls_review_opened.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md
```

Current human-review task:

```text
1. inspect Conversation Boxes-mode spacing at the actual local viewport
2. inspect the current flat right-side Project Grid rail control set
```

Current-process Focus is explicitly outside this correction boundary because the project owner confirmed that it is working correctly.

The Checkpoint 255 live topology compass remains carried forward unchanged.

Production `/cockpit` remains untouched.

---

# Current whole-product browser

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Current review route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=angled
```

The `edge=angled` query is historical implementation plumbing. The visible rail is normal flat 2D.

The source-faithful integrated Cockpit remains the protected whole-product design substrate. New shell decisions are evaluated on this complete browser rather than in disconnected fixtures.

---

# Checkpoint 256 corrections

## Conversation rail

The prior row-gap-only correction was insufficient. Canonical Conversation WorkUnits are scaled/transformed inside rail slots, so visual content could consume the apparent separation even while the parent list reported a valid CSS gap.

The current layout reserves real row geometry:

```text
thread-list row gap       16px
WorkUnit row padding       6px top + 6px bottom
canonical WorkUnit size    unchanged
accepted rail footprint    unchanged
```

The deterministic gate now measures the actual rendered WorkUnit `.node-surface` rectangles.

Required visible spacing:

```text
project-general -> first WorkUnit  >= 16px
WorkUnit -> next WorkUnit          >= 20px
```

Both requirements are checked at 1600px and 760px viewport widths.

Held Conversation semantics remain unchanged:

```text
Quiet Graphite baseline
project-general + work-unit-scoped conversation
Boxes / Text user-switchable rail
A6 Adaptive Anchor
no redundant A6 floating home card
full-focus + co-present Conversation
Grid + Deep Dive access
source work-state preservation
```

## Right-side Project Grid rail

The current rail remains the compact normal flat 2D candidate from Checkpoint 255.

Current visible control set:

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
Tool-label clarity control
```

Explicitly removed from this current rail composition:

```text
Expand selected WorkUnit
Hide project HUD
```

These are shell-composition changes only. X5 remains an accepted mechanism and Specification 008 immersive/fold-away chrome capability remains part of the promoted architecture.

The current flat rail remains a review candidate, not a promoted production baseline.

## Current-process Focus

The project owner explicitly confirmed that Focus is working correctly and asked that the previous Focus correction request be ignored.

Therefore:

```text
M09 focus behavior unchanged
focus membership editing unchanged
context recession unchanged
focus UI unchanged
```

No Focus implementation was changed in Checkpoint 256.

## Deep Dive topology compass carried forward

The Checkpoint 255 live topology compass remains active and unchanged:

```text
one dot per actual mounted WorkUnit
real current relation links rendered
actual selected WorkUnit highlighted
related WorkUnits receive quieter context emphasis
selection changes update the compass
compass reads state but never owns or mutates selection
```

---

# Deterministic fidelity status

Implementation target:

```text
e2768a807b2a80f438248a25f7d41e53be561d51
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33211613408
job           98985900484
result        SUCCESS
browser tests 68 / 68 passing
```

The newest tests verify:

```text
actual visible Conversation WorkUnit spacing at desktop width
actual visible Conversation WorkUnit spacing at narrow width
Fullscreen visible in current flat rail
Expand selected WorkUnit absent from current flat rail
Hide project HUD absent from current flat rail
same control set retained after clarity expansion
all prior source-faithful Cockpit regression checks remain green
```

A green deterministic gate protects mechanism integrity and concrete geometry contracts. It does not decide whether the current visual tuning is aesthetically accepted.

---

# Implementation-provenance recovery remains complete

The recovery architecture established after the failed holistic integration remains authoritative:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

Manifest coverage remains:

```text
23 total entries
19 required MUST_PORT / MUST_PRESERVE
4 deliberately non-promotable records
```

First exact-history provenance proof remains:

```text
workflow run 33156357834
Cockpit implementation manifest: PASS
exact historical source verification: PASS
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only and must never be used as an accepted visual source or parent implementation.

---

# Held Phase-C decisions remain intact

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
Quiet Graphite Conversation Workspace
project-general + work-unit-scoped conversations
Boxes / Text conversation rail
A6 Adaptive Anchor
conversation from Grid + Deep Dive
full-focus + co-present conversation capability
source work-state preservation
compact native Cockpit composer
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

Checkpoint 256 changes Conversation row geometry and the visible flat-rail control set only. It does not revoke these held semantics.

Important accepted targets remain:

```text
directionality                07d573b6569b9f09a3b7e00936f3eadecee721b3
relation class E5             497e81f06ba1f9901511449237d1bb9f96b2d108
P7 disposition                fac1db37af4225927d6c799e37418a3ad9c42c13
editable focus                da115b74de526fca05ed6f468bef39bdb801355c
T7 Soft Shade                 08534f94c2f272f969159087de2797a23e36b330
switchable runtime            fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
BLOCKED/status carrier        88fd3c3cfe7a1eff4664afde06341b7b654c97f4
A3 attention priority         767c66f76974d3c0a851de0dfa17c502817a4b12
SEL2 selection                e7304fe834d86166d843fda7e1df0f4ddb1f793a
X5 contextual expansion       94bc1100b7388cc56497cafc03051ce326424a80
Z7 specialist deep focus      04616a52df5cceff6c59223bbd6f07448d027510
semantic zoom browser         65ac02326a75b1c9f056676819d2d1b7b23b74c5
Quiet Graphite source         c66f72a74e681f89fd52ba591a1387ea50f0e959
A6 no-floating-box refinement 606e027f281b35c2dfc93d059a1681df23bc2b73
Conversation coexistence      db31970d6885ce785609f9c3300f22123130d821
```

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
Human visually reviews the two Checkpoint 256 corrections in the live browser.

If Conversation spacing and the rail control set are visually good:
    preserve explicit acceptance / tuning values
    continue whole-product Cockpit design from this corrected substrate

If either visual detail is wrong:
    tune that exact surface only
    do not reopen accepted Phase-C mechanisms
    do not modify current-process Focus unless explicitly reopened
```
