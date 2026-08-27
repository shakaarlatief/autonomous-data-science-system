# Checkpoint 235: Editable Focus Accepted, Preservation Audit Closed, Runtime Review Opened

**Date:** 2026-08-27  
**Status:** Current mixed design / preservation-method checkpoint  
**Checkpoint class:** MIXED / PRODUCT_DESIGN / PRESERVATION_METHOD  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Preserves human acceptance of user-curated current-process focus membership, closes a repository-preservation audit and metadata repair triggered by rapid Phase-C iteration, hardens checkpoint/routing hygiene, and opens the next work-unit runtime-state visual-grammar browser review.  
**Authority:** Current Phase-C continuity and development-method boundary. The checkpoint-hygiene rules in `docs/checkpoints/README.md` are governing process guidance; the runtime-state browser remains research evidence only and does not freeze the final ADS execution-state ontology. Production `/cockpit` remains untouched.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT  
**Active branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Collaboration thread:** MC-0004

## 1. User-curated current-process focus accepted

The project owner reviewed the editable focus-set interaction and concluded:

```text
It is perfect.
```

Accepted current Phase-C product direction:

```text
Context visible
    wider project remains readable

Focus current process
    current focus remains visually dominant
    outside context is strongly suppressed

Edit focus set
    user can add work units to focus
    user can remove work units from focus
    this does not delete work
    this does not change project disposition
```

Browser-local persistence remains prototype convenience only. Final production ownership/persistence and automatic focus-selection logic remain unfrozen.

Exact accepted editable-focus implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Primary evidence:

```text
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
docs/research/063_user_curated_current_process_focus_membership.md
```

## 2. Repository-preservation audit

The project owner also requested an explicit check that the repository knowledge-preservation process remains healthy despite many small Phase-C changes.

Audit evidence:

```text
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
```

Conclusion:

```text
repository architecture        SOUND
structural overhaul            NOT WARRANTED
new knowledge subsystem        NOT JUSTIFIED
checkpoint metadata drift      FOUND AND REPAIRED
checkpoint granularity         HARDENED
validation closure             HARDENED
active-branch routing guard    HARDENED
```

The layered architecture remains appropriate:

```text
Git                         fine implementation history
research                    bounded design evidence
checkpoints                 meaningful continuity / decision boundaries
foundations/canonical docs  promoted durable knowledge
routing/current state       continuation and discoverability
MC artifacts                collaboration provenance
```

## 3. Concrete integrity defect repaired

The audit found Checkpoints 223-234 had drifted from the provider-neutral checkpoint metadata contract during rapid browser iteration.

The repair conservatively added only required metadata/provenance and did not rewrite substantive historical conclusions.

Verified global checkpoint-metadata validation after repair:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
    Checkpoint metadata / validate
    SUCCESS
```

Because `scripts/check_checkpoint_metadata.py` scans the enforced checkpoint range globally, this successful run confirms the mandatory metadata contract is clean again for the enforced Checkpoint 100+ range.

## 4. Preservation-method hardening

`docs/checkpoints/README.md` now explicitly records two operating rules:

```text
MICRO-REFINEMENT GRANULARITY
    pixel tuning / small geometry fixes / copy refinements / same-gate implementation corrections
    normally stay in Git + active research evidence
    do not automatically create another checkpoint

CHECKPOINT ACCEPTANCE GATE
    checkpoint write
    -> inspect metadata validation
    -> repair if red
    -> only then rely on the checkpoint as a clean continuation boundary
```

The current-routing workflow was also widened from selected push branches to all pushes that touch the guarded routing surfaces. Its path filters remain narrow.

This is a process correction based on observed failure, not speculative governance expansion.

## 5. Next bounded Cockpit slice: runtime state

With category, project disposition and current-focus membership separated, the next unresolved work-unit question is:

> How should a work unit communicate what is happening now?

Research:

```text
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
```

Browser:

```text
frontend/design-lab/work-unit-runtime-grammar.html
frontend/design-lab/work-unit-runtime-grammar.css
frontend/design-lab/work-unit-runtime-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Exact browser implementation target:

```text
099e516bf9a7351a756bee00037edbcc731a2738
```

## 6. Runtime fixtures

The first visual-test runtime set is deliberately provisional:

```text
Idle
Queued
Running
Waiting
Waiting for Human
Failed
```

Semantic separation remains binding:

```text
category               what is this?
project disposition    where does it stand in the project?
runtime                 what is happening now?
priority / relevance    how important is it now?
current-focus membership is it in the emphasized process set?
```

## 7. Runtime encoding families

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

The browser includes both controlled same-category rows and a mixed-category practical scene with P7 neutral disposition tags retained.

Reduced-motion mode removes semantic animation but retains static runtime-state identity.

## 8. Current human gate

```text
pull v1-cockpit-design-exploration
open http://localhost:5173/design-lab/work-unit-runtime-grammar.html
compare R0-R6 in controlled rows
inspect the mixed-category scene
compare normal vs Reduced motion
judge clarity / clutter / category competition / professional feel
record prefer / reject / combine / refine
```

No final runtime ontology must be selected in this gate.

## 9. Production boundary

Production `/cockpit` remains untouched.

No execution-engine state contract is changed.

No runtime connector-flow semantics are assigned.

No final priority/relevance visual grammar is selected.

The permanent source-vault bootstrap remains paused and the Course 2 gate remains unchanged.
