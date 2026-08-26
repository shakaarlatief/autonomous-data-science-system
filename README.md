# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

Prototype V0 is complete. Bounded V1 is constructing the methodological knowledge universe and the professional substrate needed to use it safely.

Current route:

```text
checkpoint            225
active branch         v1-cockpit-design-exploration
active PR             none
exploration base      2480109fadeee1e480ef03b82e335aacdf9adf91
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      connector / Port Grammar human browser review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

---

## Current Cockpit design direction

MC-0004 is in browser-rendered Phase-C product-design evaluation.

The preferred loop is:

```text
bounded design question
-> browser-rendered alternatives
-> human comparison
-> preserve prefer/reject/combine evidence
-> progressively integrate surviving mechanisms
```

### Held world and interaction direction

```text
G4 Adaptive Hybrid world                          SELECTED / provisionally settled
H4 generic hover/outward-world response          SELECTED / sufficiently settled
Reduced in-box resting light                      SELECTED preferred working baseline
```

### Current scientific category-marker grammar

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

---

## Foundation 023: user-configurable Cockpit appearance

Human browser review approved the principle that multiple high-quality, semantically compatible visual mechanisms may coexist as user-selectable appearance dimensions.

Promoted foundation:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Core principle:

```text
ADS owns semantic meaning
+
user controls approved non-semantic appearance dimensions
```

Current proven appearance controls:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

The scientific marker mapping, semantic project state and accessibility constraints remain independent from those appearance choices.

A plausible later hierarchy remains:

```text
user appearance profile
    global personal default

project appearance override
    optional project-specific preference

semantic project state
    independent from both
```

Production settings persistence is not yet selected.

---

## Customizable-preview connector fix

The configurable preview had one remaining implementation defect: relation lines used static coordinates and therefore did not reliably meet the rendered work-unit boxes.

The fix now derives line endpoints from rendered `.node-surface` geometry and recalculates them when relevant geometry changes.

Exact fix commit:

```text
c1f996f6500672641de8e00780d5a4949c5dcb28
```

Configurator route:

```text
http://localhost:5173/design-lab/work-unit-grammar-customizable.html
```

---

## Active Slice 02C: connector and Port Grammar

The next bounded visual question is:

> How should generic project relationships meet work units and remain legible without turning the Cockpit into graph noise?

This activates Claude concept C4 Port Grammar at the dependency boundary originally reserved for it.

Current browser route:

```text
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-grammar.css
frontend/design-lab/connector-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-grammar.html
```

Exact browser implementation target:

```text
e3394447eeae721eab9bd66d347d0d327dbe0485
```

Connector candidates:

```text
K0  Clean Curve
    edge-to-edge curve, no visible ports

K1  Micro Dots
    small source/target endpoint dots

K2  Frame Sockets
    small square structural sockets

K3  Target Cue
    restrained target-side direction cue

K4  Hover Ports
    clean rest state, ports revealed on related-node hover
```

Held controls:

```text
G4 world
scientific markers
Reduced in-box light
accepted H4 hover response
Subtle shapes
Micro material
same project fixture
same generic relationships
```

Final semantic connector types remain deliberately unfrozen.

---

## Collaboration state

Claude's Phase-C divergent work-unit contribution is complete at:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

No model-collaboration obligation is currently pending.

C4 Port Grammar is now active in the connector slice.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

## Production boundary

The current work remains isolated under `frontend/design-lab/**`.

Production `/cockpit` remains the control baseline.

Not yet authorized:

```text
production Cockpit replacement
production appearance persistence
final semantic connector vocabulary
new graph/canvas dependency
new motion-library adoption
final visual-system freeze
```

Specification 008 remains the promoted interaction architecture.

---

## Source Universe substrate

Specification 023 remains:

```text
SOURCE_SUBSTRATE_ACCEPTED
```

Permanent deployment remains preserved but paused. Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Repository role

This repository is the durable development source of truth.

> **The chat is where we think. The repository is where the system remembers.**

---

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/225_configurable_appearance_promoted_connector_grammar_review_opened.md
docs/research/053_connector_and_port_visual_grammar_experiment.md
frontend/design-lab/connector-grammar.html

docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/research/052_configurable_cockpit_review_connector_geometry_fix_and_foundation_promotion.md
frontend/design-lab/work-unit-grammar-customizable.html

docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md

docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

## Exact next step

```text
1. pull v1-cockpit-design-exploration
2. optionally refresh work-unit-grammar-customizable.html and confirm the connector attachment fix
3. open http://localhost:5173/design-lab/connector-grammar.html
4. compare K0 through K4
5. hover work units and inspect connector emphasis / K4 hover ports
6. judge resting noise, attachment clarity, direction usefulness and scaling plausibility
7. prefer, reject or combine connector mechanisms
8. preserve a generic connector baseline before adding semantic relation classes
9. keep production Cockpit untouched
```
