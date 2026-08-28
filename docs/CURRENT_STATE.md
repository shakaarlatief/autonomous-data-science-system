# Current State

**Checkpoint:** 255  
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
docs/checkpoints/255_flat_project_rail_conversation_spacing_and_live_compass_review_opened.md
docs/research/095_conversation_spacing_flat_project_rail_and_live_topology_compass.md
```

Current human-review task:

```text
1. inspect Conversation Boxes-mode spacing
2. inspect the current right-side Project Grid rail as a normal flat 2D surface
3. inspect the Deep Dive project-position compass as a live topology instrument
```

The prior resting 3D / angled rail direction is no longer active. The current route still uses `?edge=angled` only as historical implementation plumbing.

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

The source-faithful integrated Cockpit remains the protected whole-product design substrate. New shell decisions are evaluated on this complete browser rather than in disconnected fixtures.

---

# Checkpoint 255 corrections

## Conversation rail

Boxes mode now gives canonical WorkUnit conversation objects deliberate vertical breathing room.

Current authored review value:

```text
thread-list gap  10px
```

The exact pixel value remains tunable. The intended design requirement is that the WorkUnit boxes read as distinct objects and do not visually run into one another.

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

The project owner explicitly requested that the current rail keep its compact structure but become normal 2D.

Current state:

```text
flat 2D surface
no perspective
no 3D transform
no rear depth plate
no 3D spine
no angled clip-path
real existing Cockpit controls retained
clarity-only label expansion retained
```

The current flat rail is a review candidate, not a promoted production baseline.

Historical 3D rail studies remain preserved in Research 092, 093 and 094 but are inactive for the current design axis.

## Deep Dive topology compass

M17 still requires a compact topology compass. The historical Z7 fixture used static hard-coded dots and therefore did not truthfully report the integrated six-WorkUnit project topology.

The integrated compass is now live:

```text
one dot per actual mounted WorkUnit
real current relation links rendered
actual selected WorkUnit highlighted
related WorkUnits receive quieter context emphasis
selection changes update the compass
compass reads project state but never owns or mutates selection
```

The container was also corrected to one coherent instrument hierarchy:

```text
one outer border
inner topology field without a second border
clear vertical separation from specialist side panels
```

Current review geometry:

```text
outer width        132px
minimum height      96px
inner topology      62px
side-panel reserve 114px
```

These dimensions remain visually tunable.

---

# Deterministic fidelity status

Implementation target:

```text
10cf3cfd26553d95c3b786df6d3a14137a29767a
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33207377429
job           98971755372
result        SUCCESS
browser tests 65 / 65 passing
```

The newest tests verify:

```text
flat rail geometry and no remaining perspective transform
clarity expansion without project-state mutation
real rail controls remain functional
Conversation WorkUnit vertical separation
live compass node count equals actual project WorkUnit count
live compass relation count equals mounted relation count
exactly one current WorkUnit is highlighted
compass follows changed selection across Deep Dive entry
single-border compass hierarchy
compass does not collide with specialist panels
```

A green deterministic gate protects mechanism integrity. It does not decide whether the current visual tuning is aesthetically accepted.

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

Checkpoint 255 changes shell presentation and compass implementation fidelity only. It does not revoke these held semantics.

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
Human visually reviews the three Checkpoint 255 corrections in the live browser.

If spacing, flat rail and compass are visually good:
    preserve explicit acceptance / tuning values
    continue whole-product Cockpit design from this corrected substrate

If any visual detail is wrong:
    tune that exact surface only
    do not reopen accepted Phase-C mechanisms
    do not revive 3D rail exploration unless explicitly requested
```
