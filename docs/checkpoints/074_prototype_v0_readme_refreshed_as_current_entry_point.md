# Checkpoint 74: Prototype V0 README refreshed as current entry point

**Date:** 2026-08-18  
**Status:** Historical preservation-method record  
**Checkpoint class:** PRESERVATION_METHOD  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: Prototype V0 README refreshed as current entry point.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

The Prototype V0 implementation and held-out experiment had advanced substantially beyond the original `prototype_v0/README.md`. The README still described P0, semantic evaluation, and the held-out runner as future work, which made it a poor entry point for understanding the current experiment.

This checkpoint records a documentation-only refresh. No treatment behavior, prompt, benchmark, resource limit, judge, bundle, run order, controller logic, provider configuration, or held-out execution rule was changed.

## README change

`prototype_v0/README.md` was rewritten as the current short conceptual and operational overview of Prototype V0.

The refreshed README now explains:

```text
what Prototype V0 is testing
what one treatment run actually does
why the churn benchmark contains deliberate semantic and methodological traps
the three project phases
B0, B1, and P0
why B1 is the primary architectural control
P0 typed state
P0 relations and dependency repair
the four reusable knowledge components
prospective final-test safeguarding
the state-derived runnable frontier
traceable state history
H1 and H2
why the experiment contains 30 held-out treatment slots
mechanical versus blinded semantic evaluation
how to interpret a P0 win, loss, or mixed result
where the executable implementation and governing specifications live
how to inspect status and advance one held-out attempt
```

The README explicitly states that the frozen foundation documents govern if a conflict ever appears between the short overview and the preregistered specification.

## Repository documentation roles

The intended navigation is now:

```text
prototype_v0/README.md
    quick current entry point

prototype_v0/src/ads_v0/
    executable Prototype V0 implementation

docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
    conceptual and benchmark specification

docs/foundations/011_prototype_v0_technical_specification.md
    detailed technical specification

docs/foundations/012_preregistered_held_out_evaluation_protocol.md
    frozen held-out evaluation contract

docs/CURRENT_STATE.md
    current execution state and next authorized slot

docs/checkpoints/
    append-only project history
```

## Experimental status

This documentation refresh does not change the held-out experiment.

Current treatment state remains:

```text
resolved treatment slots: 8 / 30
next slot: h1-r03-b1
next attempt: h1-r03-b1-a01
```

No S1-S10 or SC1-SC2 judging has begun.

The next treatment action remains exactly one preregistered H1 R3 B1 attempt after pulling this checkpoint.