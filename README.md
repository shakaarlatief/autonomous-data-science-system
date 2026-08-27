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
checkpoint            236
active branch         v1-cockpit-design-exploration
active PR             none
exploration base      2480109fadeee1e480ef03b82e335aacdf9adf91
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      conditional runtime-state human review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

---

## Current Cockpit design direction

Held controls:

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

Foundation 023 preserves user-configurable non-semantic work-unit appearance while ADS owns semantic meaning. Foundation 024 preserves configurable connector treatment, orthogonal hover/focus behavior and system-owned relation directionality.

Relation-class visual grammar remains sufficiently settled:

```text
E5  Hue + Tag
```

Project-disposition visual direction is accepted for the current Phase-C round:

```text
P7  Neutral Tag + Tone

REST
    category color remains dominant
    disposition tag remains neutral
    Completed / Deferred / Future retain selective tonal recession

HOVER
    disposition tag reveals its state-specific hue
```

The current-process focus architecture is also accepted as a product direction:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

The user may explicitly add or remove work units from the current focus set without deleting work or changing project disposition. The exact accepted editable-focus implementation is:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Final production focus-set ownership, persistence and automatic suggestion logic remain open.

---

## Repository preservation audit

A rapid-iteration preservation audit was completed before opening the runtime slice.

Result:

```text
repository architecture        SOUND
structural overhaul            NOT WARRANTED
new knowledge subsystem        NOT JUSTIFIED
checkpoint metadata drift      FOUND AND REPAIRED
checkpoint granularity         HARDENED
validation closure             HARDENED
active-branch routing guard    HARDENED
```

Checkpoints 223-234 were repaired to the existing provider-neutral metadata contract without rewriting substantive historical conclusions.

Verified global checkpoint metadata validation:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
    validate  SUCCESS
```

Audit evidence:

```text
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
```

---

## Active Slice 02H: conditional work-unit runtime state

Human review of the first runtime fixture exposed an important semantic correction.

The current model is:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

Runtime is therefore conditional rather than universally present.

The key distinction is:

```text
No runtime
    no current execution/work episode exists

Idle runtime
    an execution episode exists but is doing nothing
```

The current browser uses `No runtime`, not `Idle`, as the absence control. Deferred, Future and Completed work normally has no current runtime carrier. Current work may have no runtime or a live state. Recommended/Next work normally has no runtime but may be Queued if it has already been scheduled.

`Current` is preferred over `Active` for project disposition so project-state language does not imply execution.

`Blocked` is explicitly unresolved. It may ultimately be an orthogonal progress constraint that can coexist with Current or Next rather than a peer lifecycle/disposition value.

Controlled runtime fixtures:

```text
NONE    No runtime
QUEUE   Queued
RUN     Running
WAIT    Waiting
HUMAN   Waiting for Human
FAIL    Failed current attempt
```

Browser carrier families remain:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

For `NONE`, R1-R6 intentionally render no runtime instrumentation.

The mixed-category practical scene now includes:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

Browser:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Exact corrected browser implementation target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

Research and checkpoint:

```text
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/checkpoints/236_runtime_state_made_conditional_human_review_reopened.md
```

Current runtime state is distinct from historical execution provenance. The final runtime ontology, final project-disposition ontology, Blocked semantics and runtime-flow connector grammar remain unfrozen.

---

## Collaboration state

Claude's latest Phase-C contribution remains:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

No model-collaboration obligation is pending.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

## Production boundary

Current design work remains isolated under `frontend/design-lab/**`.

Production `/cockpit` remains the control baseline.

Not yet authorized:

```text
production Cockpit replacement
final runtime / execution-state ontology
final runtime visual carrier
final project-disposition ontology
final Blocked / progress-constraint semantics
execution-history presentation
runtime-flow connector semantics
final current-focus membership semantics
automatic focus-selection logic
production focus-set ownership / persistence
multiple named focus lenses
priority / relevance visual grammar
final semantic relation taxonomy
production relation colors / codes
semantic assignment of connector stroke rhythm
new graph/canvas dependency
new motion-library adoption
final visual-system freeze
```

Specification 008 remains the promoted interaction architecture.

---

## Source Universe substrate

Specification 023 remains `SOURCE_SUBSTRATE_ACCEPTED`.

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

docs/checkpoints/236_runtime_state_made_conditional_human_review_reopened.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
frontend/design-lab/work-unit-runtime-grammar.html

docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/checkpoints/README.md

docs/research/063_user_curated_current_process_focus_membership.md
frontend/design-lab/work-unit-process-focus.html

docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md

docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

## Exact next step

```text
1. pull v1-cockpit-design-exploration
2. open http://localhost:5173/design-lab/work-unit-runtime-grammar.html
3. verify NONE shows no runtime instrumentation under R1-R6
4. compare R1-R6 on QUEUE / RUN / WAIT / HUMAN / FAIL
5. inspect DEFER + NONE and FUTURE + NONE in the practical scene
6. toggle Reduced motion and confirm live runtime meaning remains legible
7. judge clarity, clutter, category/disposition competition and professional feel
8. prefer / reject / combine / refine runtime carriers
9. do not freeze the final runtime/disposition/Blocked ontology from this visual gate alone
10. keep production Cockpit untouched
```