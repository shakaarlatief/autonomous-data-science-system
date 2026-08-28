# Accepted Project Cockpit Implementation Manifest

**Date:** 2026-08-28  
**Status:** Current Phase-C holistic-integration contract  
**Scope:** Exact implementation provenance and fidelity boundaries for held next-generation Cockpit mechanisms.  
**Authority:** Implementation-provenance contract beneath accepted semantic/product authority. The machine-readable companion is `accepted_implementation_manifest.json`.

## Core rule

```text
DO NOT redraw accepted mechanisms from prose.

accepted implementation exists
    -> reuse or port exact implementation
    -> preserve accepted geometry / behavior / visual hierarchy
    -> adapt only inside the stated boundary
    -> verify against the exact source target
```

The first holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` violates this rule and is excluded from the source graph.

## Source-binding model

A mechanism can have two exact refs:

```text
decision target
    commit at or near the human selection/refinement

integration source target
    later exact executable snapshot used for porting when it safely carries
    the earlier decision together with later compatible refinements
```

This distinction is necessary for G4/H4 and other mechanisms that survived through later controlled fixtures.

---

# Required integration items

| ID | Mechanism | Maturity | Exact integration source | Primary source family |
| --- | --- | --- | --- | --- |
| M01 | Promoted Specification 008 interaction architecture | MUST_PRESERVE | `ed5b60bdc882bed0799ce55228ce8187f9c55aa1` | `frontend/src/components/CockpitProjectMap.tsx`, `frontend/src/cockpit.css`, `frontend/src/components/AppShell.tsx`, `frontend/src/components/MissingnessWorkspace.tsx` |
| M02 | G4 Adaptive Hybrid world / ambient behavior | MUST_PORT | `e7304fe834d86166d843fda7e1df0f4ddb1f793a` | `grid-world.css`, `work-unit-grammar.html/.css/.js` |
| M03 | Canonical WorkUnit + H4 rest/hover lighting | MUST_PORT | `e7304fe834d86166d843fda7e1df0f4ddb1f793a` | `work-unit-grammar.*`, `work-unit-grammar-lighting-controls.css` |
| M04 | Scientific category marker grammar | MUST_PORT | `6f27ae22dd47c3a395c6c8462ba325e1ebb19a2a` | `work-unit-grammar-focused.*`, `work-unit-grammar-focused-refinement.css` |
| M05 | Approved non-semantic appearance configurability | MUST_PRESERVE | `c1f996f6500672641de8e00780d5a4949c5dcb28` | `work-unit-grammar-customizable.*` |
| M06 | D0-D3 connector directionality / endpoint grammar | MUST_PORT | `07d573b6569b9f09a3b7e00936f3eadecee721b3` | `connector-directionality.*` |
| M07 | E5 Hue + Tag relation-class carrier | MUST_PORT | `497e81f06ba1f9901511449237d1bb9f96b2d108` | `relation-class-grammar.*` |
| M08 | P7 Neutral Tag + Tone disposition | MUST_PORT | `fac1db37af4225927d6c799e37418a3ad9c42c13` | `work-unit-disposition-grammar.*` |
| M09 | Editable current-process focus lens | MUST_PORT | `da115b74de526fca05ed6f468bef39bdb801355c` | `work-unit-process-focus.*` |
| M10 | Conditional runtime + R1/R5 switchable carrier | MUST_PORT | `fb847bd65ff6e5e4203a89ee2d4f74b7187c8359` | `work-unit-runtime-carrier-switch.*`, trace support |
| M11 | T7 Soft Shade runtime tag | MUST_PORT | `08534f94c2f272f969159087de2797a23e36b330` | `work-unit-runtime-tag-motion.*`, `work-unit-runtime-tag-motion-shade.css` |
| M12 | BLOCKER/BLOCKS/BLOCKED + BLOCKED/FAIL ring distinction | MUST_PORT | `88fd3c3cfe7a1eff4664afde06341b7b654c97f4` | `work-unit-progress-constraint.*`, `work-unit-blocked-carrier.*`, ring-swap CSS |
| M13 | A3 HIGH-attention Signal Bars | MUST_PORT | `767c66f76974d3c0a851de0dfa17c502817a4b12` | `work-unit-attention-priority.*` |
| M14 | SEL2 four outside corner brackets | MUST_PORT | `e7304fe834d86166d843fda7e1df0f4ddb1f793a` | `work-unit-selection-state.*` + canonical WorkUnit base |
| M15 | X5 balanced two-axis expansion, no context recession | MUST_PORT | `94bc1100b7388cc56497cafc03051ce326424a80` | `work-unit-detail-expansion.*`, X5 accepted CSS/JS, scroll CSS |
| M16 | L0 Flat Fields internal layout | PROVISIONAL_ONLY | `871075bcda8ff812e1a96b18b442c803d5da7faf` | `work-unit-internal-layout.*` |
| M17 | Z7 Pull-Back Then Dive + full-stage specialist end state | MUST_PORT | `04616a52df5cceff6c59223bbd6f07448d027510` | `work-unit-deep-focus-spatial-zoom.html/.css/.js`, `work-unit-deep-focus-spatial-zoom-refinement.css` |
| M18 | S0 Geometric Control while semantic zoom remains deferred | PROVISIONAL_ONLY | `65ac02326a75b1c9f056676819d2d1b7b23b74c5` | `work-unit-semantic-zoom.*` |
| M19 | Quiet Graphite Conversation Workspace | MUST_PORT | `c66f72a74e681f89fd52ba591a1387ea50f0e959` | `conversation-workspace-chatgpt-independent.*` |
| M20 | Conversation scope + Boxes/Text rail + A6 no-floating-card refinement | MUST_PORT | `606e027f281b35c2dfc93d059a1681df23bc2b73` | `conversation-workspace-work-unit-anchor.*`, canonical-boxes CSS |
| M21 | Grid/X5/Deep-Dive Conversation access + full/co-present state restoration | MUST_PORT | `db31970d6885ce785609f9c3300f22123130d821` | `conversation-workspace-access-coexistence.*` |
| M22 | Conversation entry-transition E0-E4 candidates | DO_NOT_SELECT_DURING_INTEGRATION | `43ee0ae0ffc63eba6e99a42e9157568c53cc8806` | `conversation-workspace-entry-transition.*` |
| M23 | Failed holistic integration | EXCLUDED_SOURCE | no integration source | `cockpit-integrated-baseline.*` at failed target only |

The JSON companion contains the full exact paths, decision sources, invariant lists, adaptation boundaries, caveats and verification requirements for all 23 entries.

---

# High-risk fidelity invariants

## M02 G4 world

```text
dark-first current baseline
20px minor / 100px major grid
Lively travelling-current direction
currents distributed across grid-coherent positions/timing
100px-major-intersection glints only
glints independent/quieter than Lively currents
ambient drift retained
ambient motion subordinate to semantic activity
reduced-motion fallback
```

Do not reintroduce visibly repeating fixed authored current/glint focal points.

## M03 canonical WorkUnit / H4

Reference project-scene geometry at the exact integration source:

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

Rest must remain localized/asymmetric with the narrow semantic-edge spill. The broad circular resting halo is rejected. Hover retains the richer world response, pointer hotspot, related-connector emphasis and small lift.

## M04 category marker mapping

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Category remains distinct from disposition, runtime, blocked condition, attention, selection and focus.

## M05 appearance configurability

Current proven dimensions:

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

Appearance may not mutate semantic state. Design-lab `localStorage` is not a production persistence decision.

## M06 directionality

```text
D0  undirected   -> no arrow
D1  A -> B       -> arrow at B
D2  A <- B       -> arrow at A
D3  A <-> B      -> arrows at both ends
```

One terminal treatment at a time. Hover is orthogonal. Arrow tips dock to actual rendered edges. Arrow+dot/socket stacking remains rejected without a future semantic reason.

## M07 relation class

E5 uses restrained hue plus an explicit compact tag. Relation class is distinct from direction. Stroke rhythm is intentionally reserved as an unassigned future semantic channel. The fixture relation taxonomy is provisional.

## M08 disposition

P7 uses a neutral tag plus tone. Category perimeter remains dominant. No disposition-colored perimeter and no disposition rhythm. The fixture vocabulary is not the final production ontology.

## M09 focus versus M15 X5

Do not conflate these two decisions:

```text
Current-process focus lens
    may recede contextual work as view composition

X5 contextual expansion
    surrounding project context remains at normal salience
    NO X5-specific context recession
```

Focus membership is user-editable and does not mutate semantic state.

## M10-M11 runtime

Runtime ornament exists only while a real operation exists/is active. R1 and R5 are presentation carriers for the same semantic state. T7 is subtle shade flow with the text label dominant; it is not a spinner or fake progress meter.

## M12 progress constraint

```text
BLOCKER WorkUnit
    -> BLOCKS relation
    -> BLOCKED target WorkUnit
```

BLOCKED is not runtime. Current selected carrier distinction:

```text
BLOCKED    sharper compact ring
FAIL       smoother circular compact ring
```

## M13 attention

A3 Signal Bars appear only for HIGH attention, at the far right edge, with restrained height. Attention is orthogonal to other semantic/presentation channels.

## M14 selection

SEL2 is four neutral cool outside right-angle corner brackets. It persists at rest and layers with H4 hover. Selection is UI state, not project semantics. Conversation ownership does not automatically imply SEL2.

## M15 X5

Reference geometry:

```text
390 x 210px
balanced width + height expansion
one integrated WorkUnit
surrounding context normal salience
bounded internal scrolling
```

The production implementation may respond to viewport constraints, but it must preserve the accepted balanced two-axis character rather than revert to a sidecar/drawer design.

## M16 L0

L0 is explicitly **provisional only**. The six comparison fields are not a frozen semantic schema. L1-L8 remain preserved/not rejected.

## M17 Z7

Transition:

```text
brief pull-back establishes spatial depth
selected WorkUnit remains the causal origin
camera then dives through selected work
```

End state:

```text
specialist workspace owns the full Cockpit stage
project grid/other boxes absent
selected category identity remains represented
compact topology compass retained
```

Specialist internal analytical modules and exact motion timing remain open.

## M18 semantic zoom

Semantic zoom remains **deferred**. S0 is geometric-only working behavior. S1-S8 are preserved, not rejected. The integrator may not invent semantic grouping/abstraction merely because the holistic product needs zoom.

## M19 Quiet Graphite

Reference source contains the actual selected workspace system, including:

```text
--bg                 #070a0f
--stage              #0b1017
--panel              #0f151d
--accent             #69d9c2
--transcript-width   850px
--message-gap        30px
--message-pad        14px 16px
```

The selected baseline is a first-class Conversation workspace with thread rail, broad transcript, structured project references/events, bounded context surface and compact native composer. Do not reduce it to a generic narrow chat panel.

## M20 A6 / scope / rail

Preserve:

```text
project-general conversation
work-unit-scoped conversation
per-turn context as separate concept
Boxes / Text rail switch
A6 Adaptive Anchor
no redundant floating A6 source/home card
conversation ownership != SEL2 map selection
```

## M21 access / coexistence

Work contexts:

```text
Grid neutral
Grid selected
Grid X5 expanded
Deep Dive
```

Conversation presentations:

```text
compact/work only
full Conversation focus
co-present work + Conversation
```

Opening/closing Conversation must preserve and restore the source work state. Final split width/resizing and transition choreography remain open.

## M22 no transition winner

Research 085 E0-E4 remains choreography evidence only. Minimum neutral integration glue is allowed, but no E0-E4 candidate may be called accepted without a new decision.

## M23 failed browser exclusion

The failed source family may be inspected only to understand the failure. It must not be imported, copied, restyled or treated as the parent baseline of the replacement integrated Cockpit.

---

# Allowed adaptation categories

The next integrator may change implementation details only when the relevant manifest entry permits them. Typical legitimate adaptations are:

```text
DOM/component boundaries
application state plumbing
fixture text/content
responsive layout around an accepted reference geometry
world extent scaling
production persistence mechanisms that remain explicitly open
minimum whole-product shell glue where no accepted answer exists
```

Any new glue must be separately identified as provisional.

Typical illegitimate adaptations are:

```text
new visual geometry because integration feels easier that way
new color/font system replacing an accepted source
simplifying a layered interaction into a merely similar effect
using one semantic channel to carry another concept
selecting a deferred candidate through implementation accident
copying the failed holistic browser and polishing it
```

---

# Holistic fidelity gate

A replacement integrated browser may not be called a baseline until every `MUST_PORT` / `MUST_PRESERVE` entry passes its declared checks.

Minimum gate:

```text
M01 promoted interaction capabilities present
M02 G4 world fidelity
M03 canonical WorkUnit/H4 fidelity
M04 marker mapping
M05 appearance/semantics separation
M06 D0-D3 directionality and endpoint geometry
M07 E5 relation class
M08 P7 disposition
M09 editable focus lens
M10 conditional runtime + carrier switch
M11 T7 Soft Shade
M12 BLOCKER/BLOCKS/BLOCKED + ring distinction
M13 A3 attention
M14 SEL2 selection
M15 X5 without context recession
M16 L0 still explicitly provisional
M17 Z7 + full-stage specialist end state
M18 no accidental semantic zoom selection
M19 Quiet Graphite fidelity
M20 scope + Boxes/Text + A6 no-floating-card refinement
M21 Conversation access + source-state restoration
M22 no accidental transition winner
M23 failed browser excluded from source graph
```

Run the structural validator before integration review:

```text
python scripts/check_cockpit_implementation_manifest.py
```

When repository history is available locally, also run:

```text
python scripts/check_cockpit_implementation_manifest.py --verify-git-history
```

The second form verifies that every declared source path exists at its exact historical integration target.
