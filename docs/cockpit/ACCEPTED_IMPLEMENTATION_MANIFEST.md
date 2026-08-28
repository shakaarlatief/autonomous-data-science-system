# Accepted Project Cockpit Implementation Manifest

**Date:** 2026-08-28  
**Status:** Current Phase-C holistic-integration contract  
**Scope:** Exact implementation provenance and fidelity boundaries for held next-generation Cockpit mechanisms.  
**Authority:** Implementation-provenance contract beneath accepted semantic/product authority. Where this manifest conflicts with an accepted specification/foundation/decision on semantics, the higher authority wins. Where prose describes a visual mechanism but this manifest points to an exact accepted implementation, the exact implementation is the integration source unless explicitly superseded.

## Core rule

```text
DO NOT redraw accepted mechanisms from prose.

Accepted implementation exists
    -> reuse or port exact implementation
    -> preserve its accepted geometry / behavior / visual hierarchy
    -> adapt only inside the stated boundary
    -> verify against exact source target
```

The first holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` violates this rule and is excluded from the source graph.

## Source-binding model

Some mechanisms were selected at one commit and subsequently carried unchanged or compatibly refined into later human-reviewed fixtures. The manifest therefore distinguishes:

```text
decision target
    exact target at or near the human selection/refinement

integration source target
    exact later source snapshot that should be ported when it contains
    the held mechanism together with compatible later accepted refinements
```

When those differ, the later source target does not change the earlier semantic decision. It is simply the safest executable source snapshot for composition.

---

# M01. Promoted V1 Cockpit interaction architecture

**Maturity:** `MUST_PRESERVE`  
**Authority:** Specification 008  
**Promoted integration source:** `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`

Primary source files:

```text
frontend/src/components/CockpitProjectMap.tsx
frontend/src/cockpit.css
frontend/src/components/AppShell.tsx
frontend/src/components/MissingnessWorkspace.tsx
```

Required invariants:

```text
Project Cockpit remains primary immersive active-work model
finite navigable world != semantic project plane
2D movement and recovery
bounded geometric zoom
fit/reset/recenter
Jump/search
selective specialist mounting
compact/fold-away chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable important focus/deep-work state
keyboard accessibility
reduced-motion support
reachability != simultaneous mounting
```

Allowed integration adaptation:

```text
visual identity may adopt the accepted Phase-C design system
fixture project content may change
implementation may be ported into a newer component architecture
```

Not allowed:

```text
removing promoted navigation/recovery capabilities because a design-lab fixture omitted them
turning geometric zoom into semantic zoom without a later decision
making the Conversation Workspace the only primary product surface
```

Verification:

```text
capability checklist against Specification 008
keyboard/reduced-motion review
browser interaction tests for zoom, fit/reset, Jump/search and fullscreen
source-state/URL reconstruction review where applicable
```

---

# M02. G4 Adaptive Hybrid world and ambient behavior

**Maturity:** `MUST_PORT`  
**Decision evidence:** Research 040-043  
**Integration source target:** `e7304fe834d86166d843fda7e1df0f4ddb1f793a`

Primary source files:

```text
frontend/design-lab/grid-world.css
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

Required invariants:

```text
dark-first current visual baseline
20px minor grid with 100px major grid
restrained world-owned ambient drift
travelling currents distributed across grid-coherent positions
current orientation/position/timing not collapsed to a few authored coordinates
Lively current cadence direction
major-grid glints only on 100px intersections
glints quieter/independent from Lively currents
ambient motion lower salience than semantic project activity
reduced-motion degradation
```

Known caveat:

```text
The G4 decision predates the SEL2 target. The SEL2 source target is used as the
integration snapshot because it preserves the accepted G4 world while also
containing later human-reviewed WorkUnit/H4 compatibility. G4 must still be
checked against Research 040-043 rather than inferred from SEL2 selection semantics.
```

Allowed adaptation:

```text
world dimensions / visible extent may change
number of generated ambient elements may scale with world size
implementation may be componentized
```

Not allowed:

```text
fixed authored focal points that visibly repeat
semantic colors used as ambiguous ambient decoration
sparkle-like glint density
removing the distinction between ambient and semantic activity
```

Verification:

```text
source comparison against work-unit-grammar.js scheduler
major-grid glint coordinate test
inspection for hard-coded repeating current focal positions
reduced-motion check
live visual comparison against exact source target
```

---

# M03. Canonical WorkUnit surface and H4 lighting/hover response

**Maturity:** `MUST_PORT`  
**Decision target:** `bdf021d90b9a849cd2c9f992e0e18e1cc6deb80a`  
**Integration source target:** `e7304fe834d86166d843fda7e1df0f4ddb1f793a`

Primary source files:

```text
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
frontend/design-lab/work-unit-grammar-lighting-controls.css
```

Canonical project-scene geometry in the integration snapshot:

```text
width      176px
height      92px
radius       9px
padding     11px 11px 10px 14px
```

Required layers:

```text
rest-spill
rest-light
hover-light
hover-world-light
pointer-light
perimeter-sweep
frame-signature
```

Required interaction invariants:

```text
resting light remains localized/asymmetric
narrow outward spill is anchored to the semantic accent side
broad circular resting halo is rejected
hover becomes richer than rest
small ~2px lift
fuller category-colour halo
local world/grid illumination
pointer-follow light
related connector emphasis
one restrained perimeter sweep
crisp entry / calmer release
```

Allowed adaptation:

```text
component API / DOM wrappers may change
content strings may change
position in the world may change
```

Not allowed:

```text
resizing/restyling the WorkUnit as a new visual object merely to fit integration
replacing layered H4 behavior with one generic node glow
reintroducing the rejected broad resting halo
```

Verification:

```text
computed geometry comparison
layer-presence assertions
hover screenshot/video comparison
pointer-light behavior test
resting-state comparison before any integrated review
```

---

# M04. Scientific category marker grammar

**Maturity:** `MUST_PORT`  
**Decision target:** `6f27ae22dd47c3a395c6c8462ba325e1ebb19a2a`

Primary source files:

```text
frontend/design-lab/work-unit-grammar-focused.html
frontend/design-lab/work-unit-grammar-focused.css
frontend/design-lab/work-unit-grammar-focused-refinement.css
frontend/design-lab/work-unit-grammar-focused.js
```

Required semantic mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Required invariants:

```text
marker is semantic category redundancy, not a runtime/disposition/priority carrier
stable mapping inside the active product version
left reading edge remains stable
aggressive upper-left Validation cut remains rejected
```

Allowed adaptation:

```text
exact future category taxonomy may evolve through a separate decision
approved Normal/Subtle box-shape choice may coexist
```

Verification:

```text
marker mapping assertion
non-color-only category recognition review
comparison against exact focused target
```

---

# M05. User-configurable non-semantic WorkUnit appearance

**Maturity:** `MUST_PRESERVE`  
**Authority:** Foundation 023  
**Implementation target:** `c1f996f6500672641de8e00780d5a4949c5dcb28`

Primary source files:

```text
frontend/design-lab/work-unit-grammar-customizable.html
frontend/design-lab/work-unit-grammar-customizable.css
frontend/design-lab/work-unit-grammar-customizable.js
```

Approved current dimensions:

```text
Box shape
    Normal
    Subtle

Micro design
    None
    Micro material
    Micro light

Presets
    Clean
    Structured
    Rich
```

Required invariants:

```text
presentation choice never mutates semantic project state
scientific marker mapping remains stable
Reduced in-box resting light remains baseline
connector geometry derives from rendered node surfaces
```

Known caveat:

```text
localStorage in the design-lab is proof-of-concept only; production preference persistence is open.
```

Verification:

```text
appearance switch does not change semantic data
connector endpoints remain attached under shape changes
reset/default behavior review
```

---

# M06. Connector directionality and endpoint grammar

**Maturity:** `MUST_PORT`  
**Decision target:** `07d573b6569b9f09a3b7e00936f3eadecee721b3`  
**Authority:** Foundation 024

Primary source files:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Required direction states:

```text
D0  undirected   -> no arrow
D1  A -> B       -> arrow at B
D2  A <- B       -> arrow at A
D3  A <-> B      -> arrows at both ends
```

Required invariants:

```text
one terminal treatment active at a time
hover/focus is orthogonal behavior, not a terminal symbol
arrow tip docks directly to exact rendered WorkUnit edge
reverse direction uses same mechanism at opposite endpoint
connector curve remains beneath WorkUnit bodies
endpoint overlays track H4 lift/release
semantic direction cannot be changed by appearance preference
```

Rejected without new evidence:

```text
arrow + dot stacking
arrow + socket stacking
socket + dot stacking
```

Verification:

```text
D0-D3 deterministic endpoint test
rendered-edge geometry test
hover-lift endpoint tracking test
z-layer inspection
```

---

# M07. Relation-class carrier E5 Hue + Tag

**Maturity:** `MUST_PORT`  
**Decision target:** `497e81f06ba1f9901511449237d1bb9f96b2d108`

Primary source files:

```text
frontend/design-lab/relation-class-grammar.html
frontend/design-lab/relation-class-grammar.css
frontend/design-lab/relation-class-grammar.js
```

Required invariants:

```text
relation class uses restrained hue + explicit compact tag
meaning != directionality
hover emphasis does not redefine relation class
final production relation taxonomy remains unfrozen
stroke rhythm remains an unassigned future semantic channel
```

Verification:

```text
E5 active-state assertion
relation hue/tag comparison against exact target
ensure stroke rhythm is not silently repurposed
```

---

# M08. Project disposition P7 Neutral Tag + Tone

**Maturity:** `MUST_PORT`  
**Decision target:** `fac1db37af4225927d6c799e37418a3ad9c42c13`

Primary source files:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Required invariants:

```text
neutral disposition tag
category perimeter remains dominant
no disposition-colored perimeter
no disposition rhythm
Active normal
Recommended mild emphasis
Deferred softened
Completed clearly muted
Blocked mildly suppressed
Future strongly de-emphasized
```

Known caveat:

```text
the fixture's exact disposition vocabulary is not the final production ontology.
```

Verification:

```text
category marker/perimeter remains unchanged across disposition changes
disposition tag/tone comparison against exact target
```

---

# M09. Editable current-process focus lens

**Maturity:** `MUST_PORT`  
**Decision target:** `da115b74de526fca05ed6f468bef39bdb801355c`

Primary source files:

```text
frontend/design-lab/work-unit-process-focus.html
frontend/design-lab/work-unit-process-focus.css
frontend/design-lab/work-unit-process-focus.js
```

Required invariants:

```text
focus is view composition, not semantic object state
focus membership is user-editable/curated
fixture membership is not authoritative project truth
H4 remains functional inside focus mode
context may recede under the focus lens while remaining available
```

Important distinction:

```text
CP1 current-process focus may recede surrounding context
X5 contextual expansion final accepted behavior does NOT recurse/dim context
```

Verification:

```text
semantic data unchanged by focus membership edits
focus membership edit/restore test
H4 interaction test in focused and contextual nodes
```

---

# M10. Conditional runtime semantics and switchable carrier

**Maturity:** `MUST_PORT`  
**Decision target:** `fb847bd65ff6e5e4203a89ee2d4f74b7187c8359`

Primary source files:

```text
frontend/design-lab/work-unit-runtime-carrier-switch.html
frontend/design-lab/work-unit-runtime-carrier-switch.css
frontend/design-lab/work-unit-runtime-carrier-switch.js
frontend/design-lab/work-unit-runtime-carrier-switch-trace.css
frontend/design-lab/work-unit-runtime-carrier-switch-trace.js
```

Required carriers:

```text
R1 Identity Accent + Ring
R5 Soft Shade Tag
```

Required semantic invariants:

```text
runtime is orthogonal to category/disposition/focus
runtime ornament exists only while an operation exists/is active
terminal Completed/Failed/Cancelled project meaning does not leave false live-runtime decoration
carrier switch changes presentation, not runtime semantic state
```

Verification:

```text
runtime presence/absence state test
carrier switch semantic-equivalence test
terminal-state ornament removal test
```

---

# M11. T7 Soft Shade runtime tag

**Maturity:** `MUST_PORT`  
**Decision target:** `08534f94c2f272f969159087de2797a23e36b330`

Primary source files:

```text
frontend/design-lab/work-unit-runtime-tag-motion.html
frontend/design-lab/work-unit-runtime-tag-motion.css
frontend/design-lab/work-unit-runtime-tag-motion-shade.css
frontend/design-lab/work-unit-runtime-tag-motion.js
```

Required invariants:

```text
state label is dominant
subtle moving/internal shade only
minimal or no glow
not a spinner
not fake determinate progress
reduced-motion remains understandable
```

Verification:

```text
visual comparison against T7 target
reduced-motion check
assert no progress semantics are introduced
```

---

# M12. BLOCKER -> BLOCKS -> BLOCKED and operational ring distinction

**Maturity:** `MUST_PORT`  
**Decision target:** `88fd3c3cfe7a1eff4664afde06341b7b654c97f4`

Primary source files:

```text
frontend/design-lab/work-unit-blocked-carrier.html
frontend/design-lab/work-unit-blocked-carrier.css
frontend/design-lab/work-unit-blocked-carrier.js
frontend/design-lab/work-unit-blocked-carrier-ring-swap.css
frontend/design-lab/work-unit-progress-constraint.html
frontend/design-lab/work-unit-progress-constraint.css
frontend/design-lab/work-unit-progress-constraint.js
```

Required semantic model:

```text
BLOCKER WorkUnit
    -> BLOCKS relation
    -> BLOCKED target WorkUnit
```

Required visual distinction:

```text
BLOCKED    sharper compact ring
FAIL       smoother circular compact ring
```

Required invariants:

```text
BLOCKED != runtime state
BLOCKER causal/source role != BLOCKED target condition
shared visual carrier family does not collapse semantics
```

Verification:

```text
relation semantic fixture test
BLOCKED/FAIL shape comparison against target
ensure both can coexist with category/disposition channels without overwriting them
```

---

# M13. A3 HIGH-attention Signal Bars

**Maturity:** `MUST_PORT`  
**Decision target:** `767c66f76974d3c0a851de0dfa17c502817a4b12`

Primary source files:

```text
frontend/design-lab/work-unit-attention-priority.html
frontend/design-lab/work-unit-attention-priority.css
frontend/design-lab/work-unit-attention-priority.js
```

Required invariants:

```text
Signal Bars appear only for HIGH attention
they sit at far right edge
short/restrained geometry
attention remains orthogonal to category, disposition, runtime and blocked state
```

Verification:

```text
HIGH-only visibility assertion
coexistence test with BLOCKED and category markers
geometry comparison against exact target
```

---

# M14. SEL2 persistent selection

**Maturity:** `MUST_PORT`  
**Decision / integration target:** `e7304fe834d86166d843fda7e1df0f4ddb1f793a`

Primary source files:

```text
frontend/design-lab/work-unit-selection-state.html
frontend/design-lab/work-unit-selection-state.css
frontend/design-lab/work-unit-selection-state.js
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

Required invariants:

```text
four outside right-angle corner brackets
neutral cool-white/blue rather than category colour
small restrained glow
persistent at rest
H4 layers on hover rather than being replaced
selection is UI state, not semantic project state
conversation ownership does not automatically imply SEL2
```

Verification:

```text
four-bracket geometry assertion
rest/hover comparison
semantic-state non-mutation test
```

---

# M15. X5 balanced contextual expansion

**Maturity:** `MUST_PORT`  
**Decision target:** `94bc1100b7388cc56497cafc03051ce326424a80`

Primary source files:

```text
frontend/design-lab/work-unit-detail-expansion.html
frontend/design-lab/work-unit-detail-expansion.css
frontend/design-lab/work-unit-detail-expansion.js
frontend/design-lab/work-unit-detail-expansion-x5-accepted.css
frontend/design-lab/work-unit-detail-expansion-x5-accepted.js
frontend/design-lab/work-unit-detail-expansion-scroll.css
```

Accepted geometry:

```text
width     390px
height    210px
```

Required invariants:

```text
one integrated WorkUnit grows in width and height
surrounding project map remains at normal salience
NO X5-specific context recession
richer title/status/explanation/metadata/evidence can be shown
long text may scroll inside bounded detail surface
```

Verification:

```text
390x210 reference geometry check at design-lab scale
surrounding-context opacity/salience assertion
scroll behavior test
selection/state preservation test
```

---

# M16. Expanded WorkUnit internal layout L0

**Maturity:** `PROVISIONAL_ONLY`  
**Experiment target:** `871075bcda8ff812e1a96b18b442c803d5da7faf`

Primary source files:

```text
frontend/design-lab/work-unit-internal-layout.html
frontend/design-lab/work-unit-internal-layout.css
frontend/design-lab/work-unit-internal-layout.js
```

Current rule:

```text
L0 Flat Fields may be used as the temporary internal layout
L0 is NOT a final accepted information architecture
six-field fixture payload is NOT a frozen semantic schema
L1-L8 remain preserved and not rejected
```

Verification:

```text
integration documentation labels L0 provisional
no production semantic schema is inferred from the six fixture fields
```

---

# M17. Z7 Pull-Back Then Dive and full-stage specialist workspace

**Maturity:** `MUST_PORT`  
**Decision target:** `04616a52df5cceff6c59223bbd6f07448d027510`

Primary source files:

```text
frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
frontend/design-lab/work-unit-deep-focus-spatial-zoom.css
frontend/design-lab/work-unit-deep-focus-spatial-zoom.js
frontend/design-lab/work-unit-deep-focus-spatial-zoom-refinement.css
frontend/design-lab/work-unit-deep-focus-spatial-zoom-refinement.js
```

Required transition invariants:

```text
world pulls back / zooms out first
selected WorkUnit remains anchored/highlighted
then dive toward selected work
motion preserves spatial causality
```

Required end-state invariants:

```text
specialist workspace uses full available stage
no giant framed panel with large leftover margins
selected category treatment remains represented
compact topology compass retained
return preserves coherent project context
```

Allowed adaptation:

```text
specialist analytical module internals remain open
motion timing may be tuned if spatial meaning is preserved
```

Verification:

```text
transition sequence recording against exact target
end-state stage-occupancy comparison
return-state restoration test
reduced-motion alternative review
```

---

# M18. Semantic zoom disposition / S0 working behavior

**Maturity:** `PROVISIONAL_ONLY`  
**Browser target:** `65ac02326a75b1c9f056676819d2d1b7b23b74c5`

Primary source files:

```text
frontend/design-lab/work-unit-semantic-zoom.html
frontend/design-lab/work-unit-semantic-zoom.css
frontend/design-lab/work-unit-semantic-zoom.js
```

Current rule:

```text
S0 Geometric Control is the working default
semantic zoom itself is DEFERRED
S1-S8 are preserved, not rejected
```

Not allowed:

```text
choosing or inventing a semantic abstraction/grouping policy during holistic integration
claiming S0 is a final semantic-zoom design
```

Verification:

```text
only geometric zoom is active unless a later explicit decision changes this
```

---

# M19. Quiet Graphite Conversation Workspace

**Maturity:** `MUST_PORT`  
**Decision target:** `c66f72a74e681f89fd52ba591a1387ea50f0e959`

Primary source files:

```text
frontend/design-lab/conversation-workspace-chatgpt-independent.html
frontend/design-lab/conversation-workspace-chatgpt-independent.css
frontend/design-lab/conversation-workspace-chatgpt-independent.js
```

Reference visual tokens include:

```text
--bg                 #070a0f
--stage              #0b1017
--panel              #0f151d
--accent             #69d9c2
--transcript-width   850px
--message-gap        30px
--message-pad        14px 16px
```

Required architectural/visual invariants:

```text
Conversation is a first-class professional workspace, not a generic side chat
thread rail
broad readable transcript
structured project references/events embedded in conversation
compact native composer
bounded context surface
Quiet Graphite hierarchy, spacing and palette remain the baseline
```

Rejected current baselines:

```text
Deep Navy
Warm Slate
Monochrome Signal
Violet Ink
Editorial Dark
Claude Technical Manuscript
Claude Studio Console
Claude Hybrid
```

Verification:

```text
visual token/geometry comparison against exact target
transcript width/spacing check
Conversation structural region checklist
```

---

# M20. Conversation scope, Boxes/Text rail and A6 Adaptive Anchor

**Maturity:** `MUST_PORT`  
**Decision refinement target:** `606e027f281b35c2dfc93d059a1681df23bc2b73`

Primary source files:

```text
frontend/design-lab/conversation-workspace-work-unit-anchor.html
frontend/design-lab/conversation-workspace-work-unit-anchor.css
frontend/design-lab/conversation-workspace-work-unit-anchor.js
frontend/design-lab/conversation-workspace-work-unit-anchor-canonical-boxes.css
```

Required scope model:

```text
project-general conversation
work-unit-scoped conversation
per-turn context remains separate from conversation ownership
```

Required A6 invariants:

```text
source WorkUnit expands/becomes part of Conversation context
closer composition while retaining Quiet Graphite
active WorkUnit identity remains obvious in the rail/header
Boxes mode uses canonical WorkUnit box identity
Text mode remains ordinary text navigation
NO redundant floating A6 home-object card in the transcript/resting workspace
work-unit conversation ownership does not automatically create SEL2 map selection
```

Verification:

```text
A6 adaptive-mode floating-card absence assertion
Boxes/Text switch comparison
scope identity test
Quiet Graphite base-style comparison
```

---

# M21. Conversation access and coexistence

**Maturity:** `MUST_PORT`  
**Decision/browser target:** `db31970d6885ce785609f9c3300f22123130d821`

Primary source files:

```text
frontend/design-lab/conversation-workspace-access-coexistence.html
frontend/design-lab/conversation-workspace-access-coexistence.css
frontend/design-lab/conversation-workspace-access-coexistence.js
```

Required work-context access states:

```text
Grid neutral
Grid selected
Grid X5 expanded
Deep Dive specialist
```

Required Conversation presentation states:

```text
compact/work-only state
full Conversation focus
co-present work + Conversation
```

Required invariants:

```text
project-general and WorkUnit-scoped Conversation both remain available
Conversation access is orthogonal to work context
opening Conversation does not destroy source work state
closing Conversation restores/preserves the prior work state
full-focus and co-present are both legitimate modes
```

Known open details:

```text
final co-present width/split resizing
full-chat transition choreography
conversation persistence/session model
conversation URL-state contract
```

Verification:

```text
state matrix test across all work-context x Conversation-presentation combinations
open/close restoration assertion
scope preservation assertion
```

---

# M22. Conversation entry-transition candidates E0-E4

**Maturity:** `DO_NOT_SELECT_DURING_INTEGRATION`  
**Evidence target:** `43ee0ae0ffc63eba6e99a42e9157568c53cc8806`

Primary source files:

```text
frontend/design-lab/conversation-workspace-entry-transition.html
frontend/design-lab/conversation-workspace-entry-transition.css
frontend/design-lab/conversation-workspace-entry-transition.js
```

Current rule:

```text
no winner selected
preserve as future choreography evidence only
integration may use minimum neutral transition glue
integration must not label an E0-E4 candidate accepted
```

---

# M23. Failed holistic browser exclusion

**Maturity:** `EXCLUDED_SOURCE`  
**Failed target:** `8e554d847bb3b6318db432abcb5dff742f0fa523`

Excluded files:

```text
frontend/design-lab/cockpit-integrated-baseline.html
frontend/design-lab/cockpit-integrated-baseline.css
frontend/design-lab/cockpit-integrated-baseline.js
```

Rule:

```text
may be inspected only to understand the failure
must not be copied as visual source
must not provide new geometry/palette/component decisions
must not become the parent baseline for the replacement build
```

---

# Holistic fidelity gate

Before a replacement integrated browser can be presented as a baseline, every `MUST_PORT` item must be checked.

Minimum gate:

```text
M01 promoted interaction capabilities present
M02 G4 world source fidelity
M03 canonical WorkUnit/H4 fidelity
M04 scientific marker mapping
M05 appearance/semantics separation
M06 D0-D3 directionality and endpoint geometry
M07 E5 relation class
M08 P7 disposition
M09 editable focus lens
M10 conditional runtime + switchable carrier
M11 T7 Soft Shade
M12 BLOCKER/BLOCKS/BLOCKED + BLOCKED/FAIL ring distinction
M13 A3 Signal Bars
M14 SEL2 selection
M15 X5 expansion without context recession
M16 L0 still labeled provisional
M17 Z7 + full-stage specialist end state
M18 no accidental semantic zoom selection
M19 Quiet Graphite fidelity
M20 scope + Boxes/Text + A6 no-floating-card refinement
M21 Grid/X5/Deep Dive Conversation access + state restoration
M22 no accidental transition winner
M23 failed browser not used as source
```

The corresponding machine-readable contract is `accepted_implementation_manifest.json`.
