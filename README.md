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
checkpoint            227
active branch         v1-cockpit-design-exploration
active PR             none
exploration base      2480109fadeee1e480ef03b82e335aacdf9adf91
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      simplified arrow directionality human browser review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

---

## Current Cockpit design direction

MC-0004 is in browser-rendered Phase-C product-design evaluation.

Preferred loop:

```text
bounded design question
-> browser-rendered alternatives
-> human comparison
-> preserve prefer / reject / combine evidence
-> progressively integrate surviving mechanisms
```

Held visual direction:

```text
G4 Adaptive Hybrid world                          SELECTED / provisionally settled
H4 generic hover/outward-world response          SELECTED / sufficiently settled
Reduced in-box resting light                      SELECTED preferred working baseline
```

Current scientific category-marker grammar:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

---

## Foundation 023: user-configurable Cockpit appearance

Human browser review approved the principle that multiple high-quality, semantically compatible work-unit mechanisms may coexist as user-selectable appearance dimensions.

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

Current proven work-unit appearance controls:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

Production settings persistence is not yet selected.

---

## Connector treatment and hover behavior

Human review retained the useful connector mechanisms but clarified that they should not be stacked without a semantic reason.

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Current interaction rule:

```text
one terminal treatment normally active at a time
+
hover / focus is a separate reveal or emphasis mechanism
```

So hover is not a fifth terminal symbol. It may reveal or intensify the selected treatment.

Important retained refinements:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    Micro-dot / hover-port circles sit mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    Frame sockets adopt active relation color / restrained glow when highlighted
```

---

## Foundation 024: connector treatment vs semantic directionality

Refined foundation:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Core principle:

```text
semantic relation state
    system-owned

connector treatment
    configurable within approved bounds
    normally one active terminal treatment at a time

hover behavior
    orthogonal interaction mechanism
```

Direction remains semantic:

```text
undirected
A -> B
A <- B
A <-> B
```

If arrows are used, their placement follows the relation direction exactly.

---

## Active Slice 02D: simplified arrow directionality

The first directionality browser mixed arrows with dots / sockets as compatibility controls. Human review simplified the question.

The current browser now isolates the earlier preferred K3-style edge-connected arrow only.

Browser route:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact browser implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Current direction states:

```text
D0  Undirected      A - B
    no arrow

D1  Forward         A -> B
    arrow docked directly to B

D2  Reverse         A <- B
    exact same arrow docked directly to A

D3  Bidirectional   A <-> B
    same arrow at both endpoints
```

No dots or sockets are mixed into the directionality comparison.

The arrow tip touches the exact rendered work-unit perimeter and follows H4 hover lift / release through the existing dynamic geometry system.

If human review accepts this simple arrow grammar, the next slice is semantic relation classes such as chronology, causality, dependency, evidence and lineage.

---

## Collaboration state

Claude's Phase-C divergent work-unit contribution is complete at:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

No model-collaboration obligation is currently pending.

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

docs/checkpoints/227_directionality_arrow_grammar_simplified_human_review_opened.md
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
frontend/design-lab/connector-directionality.html

docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md

docs/research/054_connector_composition_directionality_and_endpoint_layering_refinement.md
frontend/design-lab/connector-grammar.html

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
2. open http://localhost:5173/design-lab/connector-directionality.html
3. verify D0 through D3 use only the simple edge-connected arrow grammar
4. verify forward / reverse / bidirectional arrows touch the correct work-unit edge
5. verify no dots or sockets are mixed into arrow directionality
6. if accepted, preserve directionality as sufficiently settled
7. then open semantic relation-class exploration
8. keep production Cockpit untouched
```
