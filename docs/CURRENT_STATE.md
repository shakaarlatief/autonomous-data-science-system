# Current State

**Checkpoint:** 225  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. Foundation 023 promotes user-configurable non-semantic Cockpit appearance. The active slice is connector / Port Grammar. K1/K4 circular endpoint markers are now layered above nodes, follow the accepted H4 hover lift/release, and are offset mostly outside the rendered work-unit perimeter so they read as connector attachments rather than card content. K2 frame sockets retain their earlier structural treatment. The permanent source-vault bootstrap remains deliberately paused.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-08
Conversation title       08 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/225_configurable_appearance_promoted_connector_grammar_review_opened.md
docs/research/054_connector_composition_directionality_and_endpoint_layering_refinement.md
docs/research/053_connector_and_port_visual_grammar_experiment.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-grammar.css
frontend/design-lab/connector-grammar.js
frontend/design-lab/connector-port-layering.css
frontend/design-lab/connector-port-layering.js
```

Current local URL:

```text
http://localhost:5173/design-lab/connector-grammar.html
```

Current exact browser implementation target:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
```

---

# Provisionally settled world / interaction controls

```text
G4 Adaptive Hybrid                  SELECTED / provisionally settled
Dark mode                           CURRENT design baseline
Travelling grid currents            KEEP
Current distribution                RANDOMIZED across visible 20 px grid lines
Current cadence                     LIVELY preferred
Intersection glints                 KEEP at 100 px major-grid intersections
Glint cadence                       approximately Quiet / independent
Slow ambient light drift            KEEP
Localized semantic activity         KEEP
```

Generic H4 hover/world behavior remains sufficiently settled.

Current work-unit rest/hover baseline:

```text
REST
    Reduced in-box resting light
    narrow asymmetric outward world spill
    no broad circular resting halo

HOVER
    full node-colored halo
    pointer-following hotspot
    local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep
    2 px depth lift
    fast entry + smoother slower release
```

---

# Work-unit semantic grammar

Current semantic category marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Rejected/retired historical directions remain preserved:

```text
bare Q / I / V / M / E letters
G2 Compact Marker Rail
S3 Inner Instrument Architecture
G1 Instrument Glyph Family retired from active focused comparison
```

---

# Foundation 023: configurable appearance

Promoted product principle:

```text
ADS owns semantic meaning
+
user controls approved non-semantic appearance dimensions
```

Current proven configurable dimensions:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

Appearance choices must not redefine category, disposition, runtime, importance, evidence, provenance, or methodological meaning.

Production persistence remains unresolved. A plausible later hierarchy remains:

```text
user appearance profile
    global personal default

project appearance override
    optional project-specific choice

semantic project state
    independent from both
```

---

# Active Slice 02C: connector and Port Grammar

Bounded design question:

> How should generic project relationships visually meet work units and remain legible without turning the Cockpit into graph noise?

Held controls:

```text
G4 world
scientific category markers
Reduced in-box light
accepted H4 hover/world response
Subtle shapes
Micro material
same churn-project fixture
same four generic relationships
```

Current candidates:

```text
K0  Clean Curve
    direct edge-to-edge line, no ports

K1  Micro Dots
    small source/target endpoint dots

K2  Frame Sockets
    small square structural sockets

K3  Target Cue
    restrained target-side directional cue

K4  Hover Ports
    clean rest state, endpoint dots revealed on related-node hover
```

## Connector layering invariant

```text
world / grid
    -> connector curves below nodes
    -> work-unit body
    -> micro dots / hover ports / directional endpoint cues above node perimeter
```

K2 Frame Sockets are intentionally exempt from the above-node overlay because human review preferred the earlier under-node structural docking treatment.

## Hover-lift geometry invariant

The accepted H4 hover state lifts a node by 2 px. Connector geometry must follow the rendered perimeter during that motion rather than remain at pre-hover coordinates.

Current behavior:

```text
hover entry
    geometry synchronized through the fast node lift

hover release
    geometry synchronized through the slower return

Reduced motion
    one immediate geometry refresh
```

This keeps both the curve endpoint and above-node marker attached to the moving box throughout the transition.

## Circular terminal placement invariant

K1 Micro Dots and K4 Hover Ports should read as connector-owned attachment points, not as card content.

Current behavior:

```text
curve anchor
    remains exactly on the rendered work-unit edge

circular terminal center
    offset 2 SVG user units outward along the attachment side

visual result
    marker sits mostly outside the card
    only a small overlap remains with the perimeter
    left-side dots no longer sit across the category color rail
```

K2 sockets remain unchanged and frame-integrated. K3 direction cues remain unchanged pending the combined directionality/composition experiment.

Exact outward-dot refinement:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
```

---

# Preliminary connector-composition hypothesis

Human review has already supplied a likely architectural direction, but final connector composition is intentionally pending one more visual verification.

Current hypothesis:

```text
connector grammar should be compositional
not one universal K0-K4 winner
```

Potential orthogonal dimensions:

```text
RELATION SEMANTICS
    what the relation means

DIRECTIONALITY
    none
    A -> B
    B -> A
    bidirectional

BASE PRESENTATION
    curve + optional non-directional attachment treatment

PROGRESSIVE DISCLOSURE
    hover ports / relation emphasis
```

Examples mentioned by the project owner include chronological and causal relations, but no final relation vocabulary is frozen.

Hover Ports should remain available. For a non-directional baseline, Micro Dots versus Frame Sockets remains an open human preference. A later user-configurable choice may also remain possible.

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                              connector composition human review
```

There is no pending Claude obligation.

---

# Important non-decisions

Still unresolved:

```text
final connector composition
Micro Dots vs Frame Sockets as initial non-directional endpoint treatment
final semantic relation vocabulary
relation colors / dashed-solid semantics
dependency / evidence / lineage connector distinctions
runtime-flow connector behavior
selected/focused persistent treatment
runtime / waiting / blocked / approval treatment
final work-unit taxonomy
final node dimensions and typography
semantic zoom
C5 Internal Layout Grammar
2.5D focus/depth system
Conversation Workspace composition
large-project layout/grouping/command architecture
production appearance persistence
final production design system
```

Only isolated `frontend/design-lab/**` artifacts are authorized for the current experiment. Production `/cockpit` remains the control baseline.

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
```

Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Exact continuation

```text
1. use Checkpoint 225 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. refresh http://localhost:5173/design-lab/connector-grammar.html
4. verify K1/K4 circular markers now touch the perimeter from mostly outside rather than sitting across the card/color rail
5. verify they stay attached during hover lift and release
6. verify K2 retains the earlier frame-socket treatment
7. human gives the fuller connector-composition preference
8. only then implement the combined directionality/composition experiment
9. keep production Cockpit untouched
10. keep source-vault deployment paused until explicitly resumed
```
