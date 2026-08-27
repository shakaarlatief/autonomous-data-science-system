# Current State

**Checkpoint:** 226  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. Work-unit appearance configurability is promoted in Foundation 023. Connector presentation configurability plus semantic directionality separation is promoted in Foundation 024. The active slice is connector directionality review. The permanent source-vault bootstrap remains deliberately paused.  
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
docs/checkpoints/226_connector_presentation_made_configurable_directionality_review_opened.md
docs/research/055_connector_presentation_configurability_and_directionality_browser_slice.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Current local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact current browser implementation target:

```text
41bbdb75f338388f02a34fdf7dbac3ea90f86300
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

Current semantic category-marker mapping:

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

# Foundation 023: configurable work-unit appearance

Promoted principle:

```text
ADS owns semantic meaning
+
user controls approved non-semantic appearance dimensions
```

Current proven work-unit appearance dimensions:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

Production persistence remains unresolved.

---

# Connector visual-grammar result

The K0-K4 connector review no longer requires a single winner.

Human review decided the useful connector presentation mechanisms should coexist as user-adjustable choices.

Current compositional interpretation:

```text
REST ATTACHMENT PRESENTATION
    Clean
    Micro dots
    Frame sockets

HOVER ATTACHMENT EMPHASIS
    Off
    On
```

Latest accepted refinements:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    K1/K4 circular markers moved mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    K2 frame sockets keep dark interiors but adopt active relation color / restrained glow when highlighted
```

Held connector interaction/geometry invariants:

```text
curve remains below work-unit bodies
rendered-edge geometry is authoritative
connector follows H4 hover lift / release
Micro dots / Hover ports render above the perimeter and sit mostly outside the card
Frame sockets remain frame-integrated
```

---

# Foundation 024: configurable connector presentation + semantic directionality

Promoted product principle:

```text
ADS owns relation meaning and directionality
+
user controls approved non-semantic connector presentation dimensions
```

This means:

```text
user may change
    HOW the connector looks

user may not change by appearance preference
    whether the relation exists
    whether it is directed
    source / target orientation
    what the relation means
```

A directed relation must remain recognizably directed in every approved appearance profile.

Promoted artifact:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

---

# Active Slice 02D: connector directionality

Bounded question:

> How should a relationship communicate no direction, one-way direction in either orientation, or bidirectional direction while remaining visually restrained and compatible with configurable attachment presentation?

Current comparison states:

```text
D0  Undirected      A — B
D1  Forward         A -> B
D2  Reverse         A <- B
D3  Bidirectional   A <-> B
```

Browser controls are presentation compatibility checks only:

```text
Rest attachment
    Clean
    Micro dots
    Frame sockets

Hover attachment emphasis
    On / Off

Reduced motion
    On / Off
```

Those controls do not alter direction semantics.

The direction cue is intentionally persistent at rest because direction carries meaning.

Current review questions:

```text
Is A -> B immediately readable?
Is A <- B equally readable?
Does A <-> B read clearly as bidirectional?
Are the restrained endpoint chevrons sufficient?
Do direction cues coexist cleanly with dots / sockets?
```

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                               connector directionality human review
```

There is no pending Claude obligation.

C4 Port Grammar has now matured into connector presentation configurability plus directionality work.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Important non-decisions

Still unresolved:

```text
final direction-cue shape
final semantic relation taxonomy
chronology / causality / dependency / evidence / lineage connector semantics
relation colors / dashed-solid semantics
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
1. use Checkpoint 226 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/connector-directionality.html
4. compare D0-D3
5. optionally switch Clean / Micro dots / Frame sockets
6. toggle Hover attachment emphasis and verify direction remains semantically visible
7. judge forward, reverse and bidirectional cue clarity
8. preserve keep / refine / replace direction-cue evidence
9. then open semantic relation-class exploration
10. keep production Cockpit untouched
11. keep source-vault deployment paused until explicitly resumed
```
