# Research 064: Rapid-Iteration Repository Preservation Audit and Checkpoint Hygiene

**Date:** 2026-08-27  
**Status:** Accepted development-method audit evidence  
**Scope:** Audits whether the repository knowledge-preservation architecture remains healthy under the high-frequency Project Cockpit Phase-C design loop, identifies one concrete checkpoint-hygiene defect, repairs it, and records the smallest justified process hardening.  
**Authority:** Development-method evidence. The canonical checkpoint-format contract remains `docs/checkpoints/README.md`; canonical project-development method remains `docs/DEVELOPMENT_METHOD.md`.

## 1. Trigger

After accepting the editable current-process focus set, the project owner explicitly asked whether the repository-preservation process was still working well despite many small design changes and frequent updates, and whether the architecture should be changed or extended before proceeding.

This was treated as a Level-2 development-method audit rather than answered from conversational memory.

## 2. Architecture reviewed

The audit inspected the existing layered preservation architecture:

```text
canonical/current documents
    VISION / PRINCIPLES / DECISIONS / DEVELOPMENT_METHOD / CONTINUITY

foundations
    durable rationale and promoted design principles

research + specifications
    bounded evidence, alternatives, executable design hypotheses and contracts

checkpoints
    historical continuity / decision / experiment boundaries

collaboration state
    MC threads, review inbox and exact cross-model provenance

routing
    README
    CURRENT_STATE
    KNOWLEDGE_MAP
    current_routing.json

mechanical guards
    checkpoint metadata validator
    current-routing consistency validator
    collaboration-state guard
```

The basic architecture remains appropriate for the growing project.

## 3. What is working well

The current structure successfully separates several things that would otherwise become conflated:

```text
historical evidence != current authority
research != promotion
checkpoint != canonization
visual implementation target != documentation head
semantic project state != user-configurable presentation
chat continuity != repository authority
```

The recent Cockpit work also demonstrates that exact Git implementation targets plus research/checkpoint interpretation remain reconstructable even after many small visual iterations.

The existing README / CURRENT_STATE / KNOWLEDGE_MAP / current_routing layering is somewhat redundant by design, but each surface has a different role and deterministic consistency checking exists. No additional database, semantic index or generated mega-ledger is justified by the current evidence.

## 4. Concrete defect found

The audit found a real preservation-integrity defect in recent checkpoints.

Checkpoint 223 through Checkpoint 234 had drifted away from the provider-neutral checkpoint metadata contract. Checkpoints 223-229 retained the historical/authority core but omitted the required provider-neutral interaction provenance. Checkpoints 230-234 had drifted further and omitted parts of the mandatory historical/authority core as well.

This did not erase the substantive design evidence, but it weakened historical interpretability and violated the repository's own checkpoint contract.

The existing `Checkpoint metadata` GitHub Action had already been capable of detecting this. For example, the original Checkpoint 234 creation commit produced a failed validation check. The operational failure was that rapid iteration continued without inspecting and closing the failed check.

## 5. Repair completed

Checkpoints 223-234 were repaired conservatively.

The repair:

```text
added only required metadata / provenance
preserved historical titles
preserved substantive bodies
preserved dates and design conclusions
preserved exact implementation targets
```

The validator is global over the numbered checkpoint directory for Checkpoint 100+, so a successful validation after the repair establishes that the mandatory checkpoint metadata contract is again clean across the enforced range.

Verified successful metadata-validation commit:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
```

## 6. Smallest justified method hardening

Two changes are justified by observed failure rather than speculative architecture expansion.

### 6.1 Checkpoint operational acceptance gate

`docs/checkpoints/README.md` now states that a checkpoint-producing change is not operationally closed until its metadata validation succeeds.

The development behavior becomes:

```text
write checkpoint
-> inspect metadata validation
-> repair if red
-> only then rely on it as a clean continuation boundary
```

### 6.2 Granularity rule for rapid visual iteration

The same checkpoint contract now makes explicit that ordinary Git history and the active research record should absorb micro-refinements that do not alter the review question, semantic interpretation, decision evidence, promotion status, active route or continuation boundary.

Examples that normally do not need a new checkpoint inside an already-open gate:

```text
pixel-level tuning
small geometry corrections
copy / label refinements
implementation defects that leave the tested hypothesis unchanged
exact-target refreshes within the same human review gate
```

This reduces routing churn while retaining exact implementation provenance in Git.

### 6.3 Current-routing guard on development branches

The `Current routing consistency` workflow previously ran on push only for two named branches. It has been broadened to run on any push that touches the guarded routing surfaces.

The path filter remains narrow, so this adds protection without turning every implementation commit into a routing CI run.

## 7. What should not be added now

The audit does not justify adding a new knowledge database, semantic repository search layer, generated experiment index, automatic promotion engine or another specification solely because the Cockpit design loop contains many small changes.

The existing layers already preserve:

```text
fine implementation history        Git
bounded design evidence             research memos
meaningful transitions              checkpoints
promoted durable principles         foundations / canonical docs
current continuation                CURRENT_STATE + routing
cross-model provenance              MC thread artifacts
```

Adding another layer now would mostly duplicate existing ownership.

## 8. Ongoing operating rule

The architecture remains healthy if the process follows three disciplines:

```text
1. checkpoint meaningful boundaries, not every micro-change
2. inspect deterministic preservation guards when their surfaces change
3. perform periodic reconciliation at meaningful stage boundaries
```

If future scale creates a real discoverability or synchronization failure that these mechanisms cannot handle, that failure should become the evidence for the next bounded preservation mechanism.

## 9. Audit conclusion

```text
repository preservation architecture   SOUND
structural overhaul                     NOT WARRANTED
checkpoint metadata drift               FOUND AND REPAIRED
checkpoint granularity                  HARDENED
checkpoint validation closure           HARDENED
active-branch routing validation        HARDENED
new knowledge subsystem                 NOT JUSTIFIED
```

The project can proceed without redesigning the preservation architecture.
