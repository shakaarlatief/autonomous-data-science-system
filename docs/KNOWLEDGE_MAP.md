# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-28  
**Current checkpoint:** 255  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/255_flat_project_rail_conversation_spacing_and_live_compass_review_opened.md
docs/research/095_conversation_spacing_flat_project_rail_and_live_topology_compass.md

docs/checkpoints/254_resting_angled_cockpit_rail_human_review_opened.md
docs/research/094_resting_angled_rail_spatial_identity_and_clarity_only_expansion.md

docs/checkpoints/253_architectural_cockpit_edge_gen2_human_review_opened.md
docs/research/093_architectural_cockpit_edge_instrument_surface_depth_study.md

docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md
docs/research/092_spatial_edge_rail_depth_direct_manipulation_and_docking_study.md

docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
docs/research/091_source_faithful_reintegration_interaction_integrity_gate.md

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

Current route:

```text
checkpoint                255
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
current boundary          flat rail + Conversation spacing + live topology compass human review
```

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

The query name is historical. Checkpoint 255 deliberately flattens that rail to normal 2D.

Current review implementation:

```text
frontend/design-lab/cockpit-reintegration-review-255.css
frontend/design-lab/cockpit-reintegration-topology-compass.js
frontend/design-lab/cockpit-reintegration-review-fixes.js
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

Current product-surface substrate:

```text
frontend/design-lab/cockpit-product-surface-study.css
frontend/design-lab/cockpit-product-surface-study-readability.css
frontend/design-lab/cockpit-product-surface-study.js
```

---

# Checkpoint 255 review targets

## Conversation Boxes rail

```text
canonical accepted WorkUnit footprint retained
project-general artifact retained
Boxes/Text semantics retained
10px vertical list gap currently under visual review
```

## Project Grid right rail

```text
compact right-side rail retained
normal flat 2D presentation
perspective / rotations / rear depth construction removed
real Cockpit controls retained
clarity-only label expansion retained
```

The former resting-angle hypothesis is rejected for the current rail direction. Research 092-094 remain historical evidence only.

## Deep Dive project-position compass

```text
compact M17 compass retained
single coherent outer instrument container
inner topology field has no second border
one live dot per actual mounted WorkUnit
current mounted relation links shown
actual selected WorkUnit highlighted
selection changes synchronize into the compass
compass reads state but never owns selection
```

The old static five-dot fixture is superseded in the integrated Cockpit.

---

# Latest deterministic evidence

Implementation target:

```text
10cf3cfd26553d95c3b786df6d3a14137a29767a
```

Complete Cockpit fidelity workflow:

```text
workflow run  33207377429
job           98971755372
result        SUCCESS
browser tests 65 / 65 passing
```

The new test set protects the flat rail, Conversation spacing, live compass topology, selected-position synchronization, single-border compass hierarchy and collision clearance while all prior source-faithful integration checks remain green.

---

# Source-of-truth architecture

Use these layers together:

```text
SEMANTIC / PRODUCT AUTHORITY
    accepted specifications
    foundations
    explicit human-reviewed selections

DESIGN DISPOSITION
    docs/cockpit/PHASE_C_DECISION_LEDGER.md

IMPLEMENTATION PROVENANCE
    docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    docs/cockpit/accepted_implementation_manifest.json

CURRENT ROUTING
    docs/CURRENT_STATE.md
    docs/KNOWLEDGE_MAP.md
    docs/current_routing.json
    latest checkpoint + research record
```

A future integrator must never infer accepted implementation details from shorthand labels alone.

---

# Provenance and fidelity gates

Implementation-provenance recovery remains complete.

```text
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

First exact-history proof:

```text
workflow run 33156357834
entries      23
required     19
exact historical source verification PASS
```

Current gate model:

```text
PROVENANCE GATE
    PASS

DETERMINISTIC INTEGRATION GATE
    PASS for current covered implementation

HUMAN PRODUCT-DESIGN GATE
    OPEN at Checkpoint 255
```

---

# Failed holistic integration remains excluded

The browser frozen at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is still:

```text
FAILED INTEGRATION ATTEMPT
NOT an accepted baseline
NOT a production target
NOT a visual source of truth
PRESERVED only as diagnostic evidence
```

Research 088 remains the source-level diagnosis of that failure.

---

# Held Phase-C semantics / product direction

```text
G4 Adaptive Hybrid world
H4 hover/outward response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation-class carrier
D0-D3 directionality
single terminal-treatment appearance choice
P7 Neutral Tag + Tone disposition
current-process focus lens
conditional runtime semantics
Dot + ring / T7 Soft Shade carrier switch
BLOCKER -> BLOCKS -> BLOCKED
BLOCKED sharper ring / FAIL smoother ring
A3 Signal Bars
SEL2 four outside corner brackets
X5 balanced two-axis expansion
L0 provisional Flat Fields
Z7 Pull-Back Then Dive
full-stage specialist workspace
compact topology compass
S0 Geometric Control
Quiet Graphite Conversation Workspace
project-general + work-unit conversations
Boxes / Text conversation rail
A6 work-unit context expansion
no redundant A6 floating WorkUnit box
Conversation access from Grid + Deep Dive
full-focus + co-present Conversation
source work-state preservation
compact native Cockpit composer
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

Checkpoint 255 does not revoke any of these.

Important accepted targets:

```text
directionality                07d573b6569b9f09a3b7e00936f3eadecee721b3
relation class E5             497e81f06ba1f9901511449237d1bb9f96b2d108
P7 disposition                fac1db37af4225927d6c799e37418a3ad9c42c13
editable current focus        da115b74de526fca05ed6f468bef39bdb801355c
T7 Soft Shade                 08534f94c2f272f969159087de2797a23e36b330
switchable runtime            fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
BLOCKED/status carrier        88fd3c3cfe7a1eff4664afde06341b7b654c97f4
A3 attention priority         767c66f76974d3c0a851de0dfa17c502817a4b12
SEL2 persistent selection     e7304fe834d86166d843fda7e1df0f4ddb1f793a
X5 contextual expansion       94bc1100b7388cc56497cafc03051ce326424a80
Z7 specialist deep focus      04616a52df5cceff6c59223bbd6f07448d027510
semantic zoom browser         65ac02326a75b1c9f056676819d2d1b7b23b74c5
Quiet Graphite source         c66f72a74e681f89fd52ba591a1387ea50f0e959
A6 no-floating-box refinement 606e027f281b35c2dfc93d059a1681df23bc2b73
Conversation coexistence      db31970d6885ce785609f9c3300f22123130d821
```

The complete exact source graph remains in `docs/cockpit/accepted_implementation_manifest.json`.

---

# Historical whole-product rail studies

```text
Research 092
    Extruded Blade / Layered Deck / Dock and Float
    historical direct-manipulation evidence

Research 093
    Hinge / Stack / Console
    historical architectural 3D edge evidence

Research 094
    resting angled rail
    spatial-identity hypothesis now rejected for current rail direction

Research 095
    flat rail + Conversation spacing + live compass
    current review evidence
```

Do not revive a historical 3D candidate without explicit new human direction.

---

# Source Universe route

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
Course 2 gate unchanged
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

No Claude obligation is pending. The next actor remains the human reviewer.

---

# Exact next step

```text
Review Conversation box spacing,
then the flat 2D right rail,
then the live Deep Dive topology compass.

Preserve concrete visual reactions before further tuning.
```
