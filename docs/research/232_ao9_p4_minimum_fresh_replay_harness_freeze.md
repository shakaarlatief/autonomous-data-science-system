# Research 232: AO-9 P4 Minimum Fresh-Replay Harness Freeze

**Date:** 2026-09-21
**Status:** AO-9 P4 HARNESS FROZEN / FRESH COLLABORATOR REPLAY NOT YET STARTED
**Program:** Research 219
**Protocol:** Research 228
**P3 trace:** Research 231 / commit 02f17d733052fae031b14f62208a55096a846c2a
**Assignments:** docs/research/project_knowledge_activation_orchestration/ao9/p4_assignments/
**Manifest:** docs/research/project_knowledge_activation_orchestration/ao9/p4_assignments/MANIFEST.json
**Scope:** Freeze the minimum 13 decision-relevant fresh-collaborator assignments before any P4 model turn, with exact arm/scenario bytes, trial/evaluator separation, historical evidence boundaries, receipt requirements and contamination rules.
**Authority:** Research-fixture freeze. This does not score any assignment or alter architecture.

## 1. Minimum decision set

P3 reduced the mandatory fresh replay to:

~~~text
B_R2  C_R2
B_R3  C_R3
B_R6  C_R6
B_R7  C_R7
B_R8  C_R8
D_N1  D_N3  D_N4
~~~

These 13 runs are sufficient to decide the preregistered B-vs-C stopping rule and the negative-control side of AO8-E01 if their evidence is valid.

## 2. Assignment isolation

Each assignment embeds the exact frozen scenario and exact frozen arm contract, with SHA-256 bindings.

Fresh collaborators may not read:

~~~text
evaluator_keys/**
traces/**
evaluations/**
Research 231
MC-0021 comparative/reconciliation messages
prior P4 trial outputs
~~~

If any prohibited material is exposed, the run must report CONTAMINATED and stop substantive reasoning.

## 3. Historical access

Exact-snapshot scenarios preserve their frozen Git commit boundary.

R8 remains explicitly mechanism-level historical. Its assignment preserves that limitation rather than pretending a clean original blind snapshot exists.

## 4. Required receipt

Every P4 result must report:

~~~text
exact repository revisions consulted
project paths materially consulted
commands/tool actions used in order
read/access failures
uncertainty / areas not checked
approximate repository read/tool action count
whether prohibited current material was exposed
~~~

This is required so evaluator-side scoring can distinguish actual activation from unsupported self-report.

## 5. No repository mutation by tested collaborator

The tested collaborator returns the result to the caller only.

The caller freezes exact result bytes under the non-ignored `ao9/trial_outputs/` path after the turn.

This avoids the repository-wide `**/results/` ignore rule discovered during P3.

## 6. Freshness requirement

Each assignment should use a fresh collaborator context with no prior scored P4 output.

Reusing one conversation sequentially across scored assignments is not acceptable because later runs would see prior scored outputs.

## 7. Model/provider role

P4 tests control behavior, not one provider's permanent superiority.

A fresh Codex agent is acceptable as a provider-independent collaborator replay when:

~~~text
the assignment is isolated
the arm contract is frozen
historical access is respected
the evidence receipt is complete
the run is not given evaluator material
~~~

Provider/model identity is recorded in each trial output and remains a limitation when interpreting generality.

## 8. P4 harness disposition

~~~text
AO9_P4_HARNESS=FROZEN
ASSIGNMENT_COUNT=13
FRESH_REPLAY_STARTED=false
PRIOR_RESULT_EXPOSURE_ALLOWED=false
REPOSITORY_MUTATION_BY_TRIAL=false
TRIAL_OUTPUT_PATH=ao9/trial_outputs/
NEXT=EXECUTE_FRESH_ASSIGNMENTS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
~~~
