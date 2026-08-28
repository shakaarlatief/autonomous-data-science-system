# Current State

**Checkpoint:** 254  
**Date:** 2026-08-28  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C advanced whole-product Cockpit design exploration on the source-faithful integrated substrate. Implementation-provenance recovery is complete; the accepted Phase-C mechanism set has been reintegrated with deterministic browser protection; Product Surface Study A acts as the complete-Cockpit design surface; and Checkpoint 254 opens one clarified resting angled rail for human review after the project owner separated spatial identity from optional clarity expansion.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

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
docs/checkpoints/254_resting_angled_cockpit_rail_human_review_opened.md
docs/research/094_resting_angled_rail_spatial_identity_and_clarity_only_expansion.md
```

Current task:

```text
human-review one resting angled right-side Cockpit rail

primary question:
    does the compact rail itself create the intended spatial / 3D feeling?

judge:
    resting angle
    perspective
    visible chassis thickness
    right-edge attachment
    calmness
    material quality
    control readability
    visual weight
    project-world occlusion

then optionally open the clarity state
only to judge labels / comprehension / width
```

There is no current drag comparison and no need to inspect intermediate pull states. The angled rail is unselected. Production `/cockpit` remains untouched.

---

# Source-faithful reintegration status

The implementation-provenance recovery opened by Checkpoint 250 is complete.

Durable recovery architecture:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

Manifest coverage:

```text
23 total entries
19 required
    MUST_PORT / MUST_PRESERVE

4 non-promotable
    PROVISIONAL_ONLY
    DO_NOT_SELECT_DURING_INTEGRATION
    EXCLUDED_SOURCE
```

First exact-history provenance proof:

```text
workflow run  33156357834
commit        2127563c0ed980f7bf6fad36e36b11e76500c59b

Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

The replacement holistic Cockpit was then built through source reuse / exact mechanism porting plus separately identified whole-product glue.

---

# Fidelity and human-review model

The project distinguishes three different gates:

```text
PROVENANCE GATE
    exact decision/source recovery
    exact historical source resolution
    PASS

DETERMINISTIC INTEGRATION GATE
    accepted mechanism invariants
    cross-mechanism interaction integrity
    whole-product study regressions
    PASS for the current covered implementation

HUMAN PRODUCT-DESIGN GATE
    whether provisional shell choices are actually good
    whether new candidates should be selected
    OPEN
```

Latest complete browser gate:

```text
implementation target  67c3105ff26601a2f259e44007b23ce638b23838
workflow run           33202773778
job                    98956116141
result                 SUCCESS
browser tests          64 / 64 passing
```

The four newest checks specifically prove that the compact angled rail already has perspective and rear depth, no drag grip/slider exists, clarity expansion leaves the 3D transform and project state unchanged, and real Cockpit controls plus full-stage ownership remain intact.

A green automated gate does **not** promote Product Surface Study A or the angled rail into the accepted Cockpit design. Human selection remains required for provisional presentation decisions.

---

# Product Surface Study A

The source-faithful integrated browser is the advanced whole-product design substrate.

Current provisional Product Surface Study A explores:

```text
continuous viewport-owned project grid
compact project identity HUD
right-side spatial tool surface
invoked bounded Jump/search
normal readable Conversation typography
compact full Conversation composer
removal of reintegration-only diagnostic chrome from ordinary review
```

These shell choices are deliberately evaluated on the complete Cockpit so new design decisions can be judged in interaction with the accepted WorkUnits, relations, Conversation, X5, Z7 and project world.

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

The accepted lower-layer mechanisms remain protected by the same holistic test suite while shell candidates change around them.

---

# Current resting angled rail study

Live route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=angled
```

The compact state is the primary state under review.

Current hypothesis:

```text
right-side rail
    remains compact
    is permanently angled inward toward the project world
    exposes visible rear construction / thickness
    reads as an architectural Cockpit surface at rest
```

Current authored study geometry:

```text
compact width              72px
perspective                 1050px
Y orientation               -24deg
X orientation               0.8deg
screen-plane rotation       -0.8deg
front-face Z translation    20px
rear construction offset    +10px x / +7px y / -28px z
```

Those exact values are provisional. The human-review question is whether the resting rail geometry produces the intended spatial feeling.

## Clarity state

```text
compact
    icons only
    spatial geometry already present

clarity expanded
    width 220px
    labels visible
    identical authored 3D transform
```

Expansion is a readability aid only. It does not hinge, telescope, detach, fan into layers or create the 3D effect.

No drag grip exists. No slider role exists. No partial deployment states exist.

The study reuses the real existing Cockpit controls and preserves selection, camera state, relation semantics, Conversation ownership and Deep Dive ownership.

---

# Previous spatial-rail studies

Research 092 and Research 093 remain preserved as design history and interaction evidence.

```text
Research 092
    A · Extruded Blade
    B · Layered Deck
    C · Dock and Float

Research 093
    A · Hinged Instrument Panel
    B · Telescoping Layer Stack
    C · Spatial Command Console
```

Current disposition:

```text
historical / inactive current design axis
not a comparison the human must complete before proceeding
not required to create the intended resting 3D rail feeling
```

Direct manipulation is not universally rejected. It would need a separate future functional justification instead of being used merely to make the rail look spatial.

---

# Whole-product study implementation and CI coverage

Current angled-rail artifacts:

```text
frontend/design-lab/cockpit-spatial-rail-study-angle.css
frontend/design-lab/cockpit-spatial-rail-study-angle.js
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

Product Surface A artifacts include:

```text
frontend/design-lab/cockpit-product-surface-study.css
frontend/design-lab/cockpit-product-surface-study-readability.css
frontend/design-lab/cockpit-product-surface-study.js
```

Historical rail-study artifacts remain preserved under the `cockpit-spatial-rail-study*` family.

The Cockpit fidelity workflow watches:

```text
frontend/design-lab/cockpit-reintegration*
frontend/design-lab/cockpit-product-surface-study*
frontend/design-lab/cockpit-spatial-rail-study*
frontend/e2e/cockpit-reintegration*.spec.ts
```

The current 64-test green run includes all accepted/source-faithful reintegration coverage plus Product Surface A, Research 092, Research 093 and the clarified resting-angle study.

---

# Failed integration remains excluded

The first holistic browser:

```text
frontend/design-lab/cockpit-integrated-baseline.html
exact target 8e554d847bb3b6318db432abcb5dff742f0fa523
```

remains classified as:

```text
FAILED INTEGRATION ATTEMPT
NOT an accepted baseline
NOT a production target
NOT a basis for new visual decisions
EXCLUDED from the implementation source graph
PRESERVED as diagnostic evidence
```

It must not be reused as the parent implementation for current whole-product exploration.

---

# Accepted / held Phase-C decisions remain intact

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
full-stage specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite Conversation Workspace baseline
project-general + work-unit-scoped conversation distinction
Boxes/Text user-switchable conversation rail
A6 Adaptive Anchor work-unit context expansion
A6 resting state without redundant floating home-object card
conversation available from Grid and Deep Dive
full-focus + co-present conversation capability
source work-state preservation across conversation open/close
compact native Cockpit composer
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

Important accepted targets:

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

The complete exact source graph remains in `docs/cockpit/accepted_implementation_manifest.json`.

---

# Semantic zoom disposition

```text
S0 Geometric Control
    provisional working default

S1-S8
    preserved for later
    not rejected

semantic zoom
    DEFERRED
```

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
```

Course 2 remains gated.

---

# Exact next step

```text
Human opens:

http://localhost:4173/design-lab/cockpit-reintegration.html?edge=angled

First judge the compact bar itself:
    angle
    perspective
    thickness
    attachment
    calmness
    readability
    visual weight

Then, only if useful, click the clarity control to inspect labels.

Preserve concrete reactions before refining the resting rail geometry.
```

Do not return to A/B/C drag comparison unless a future functional question independently justifies direct manipulation. Do not move the angled rail into production before explicit human evidence.