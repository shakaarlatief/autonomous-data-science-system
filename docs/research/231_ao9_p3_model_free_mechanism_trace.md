# Research 231: AO-9 P3 Model-Free Mechanism Trace

**Date:** 2026-09-21
**Status:** AO-9 P3 COMPLETE / MODEL-FREE TRACE FROZEN / P4 FRESH REPLAY NEXT
**Program:** Research 219
**Protocol:** Research 228 / AO9-HISTORICAL-REGRESSION-PROTOCOL-V01
**Scenario packet:** Research 229 / commit 76f5d6e784651f244d882b5373d7f750b1a706ef
**Arm contracts:** Research 230 / commit 80b05a8ae36e951000dc66ca5fed571571f33606
**Machine trace:** docs/research/project_knowledge_activation_orchestration/ao9/traces/P3_MODEL_FREE_TRACE_V01.json
**Evaluation:** docs/research/project_knowledge_activation_orchestration/ao9/evaluations/P3_MODEL_FREE_TRACE_V01.md
**Scope:** Trace the frozen scenario packet through the frozen A/B/C/D arm semantics using preserved historical evidence and architecture guarantees only, without fresh collaborator behavior and without converting probabilistic activation into assumed success.
**Authority:** Research evidence only. P3 does not amend the architecture, decide AO8-E01, or authorize AO-10 implementation.

## 1. Method

P3 separates three things that could otherwise be confused:

```text
historically observed behavior
deterministic architecture guarantee/gap
model-dependent behavior that still requires fresh replay
```

A capability is not scored PASS merely because an arm contains a mechanism that could help. When task interpretation, semantic nomination, source selection depth or actual final-output behavior remains probabilistic, P3 marks the cell for P4.

## 2. Historical Arm-A evidence

The current/legacy architecture is empirically mixed:

```text
R1  FAIL     right restart authority found, exact ordered answer lost
R2  PARTIAL  governed collaboration discovered, residual metadata cue
R3  FAIL     architecture-trigger knowledge required owner reminder
R4  FAIL     high-level continuation succeeded, stage evidence remained latent
R5  PARTIAL  exact-source hierarchy recovered, non-trivial cost
R6  PASS     abnormal interruption successfully reconstructed after audit request
R7  FAIL     W0 realization gap not exposed at acceptance boundary
R8  FAIL     known reopen conditions rediscovered after live pressure
R11 PARTIAL  selected rotation preserved as incomplete, realization gate missing
```

R9/R10 and the negative controls do not have clean historical Arm-A results and are not fabricated.

## 3. Deterministic C-versus-D finding on AO8-E01

R9 is the decisive induced control.

The scenario freezes:

```text
event interpretation = insufficient/wrong
S3 event-derived governing obligation = absent
proposed result = ordered consequential operational steps
```

Under frozen Arm C:

```text
independent output/action-shape re-entry = false
S8 cannot manufacture a missing S6 ActionContract
=> deterministic mechanism gap
```

Under frozen Arm D:

```text
ordered operational/procedural output shape fires independently
=> bounded reconstruction/authority closure re-entry
=> contract established or fail-visible no-contract state
=> normal conformance before dispatch
```

So P3 establishes a real architecture delta:

```text
R9_C = FAIL at mechanism level
R9_D = PASS at mechanism level
```

This is not yet enough to support AMEND. Research 228 also requires behavioral D passes on N1, N3 and N4 without excessive deep loads or new safety failures.

## 4. Structural claim verification

R10 gives D another deterministic capability:

```text
invalid revision / identity / constraint references
    -> structural verifier rejects the control claim
    -> no semantic-comprehension claim is inferred
```

C may still reject the malformed receipt through ordinary authority reasoning, but its frozen contract does not guarantee the generic verifier. C therefore remains P4-required rather than being declared FAIL.

## 5. Obligation-realization gap

R7 exposes a stronger issue.

Neither C nor D contains a deterministic cross-artifact join that can prove:

```text
accepted MUST obligation
    -> executable implementation/migration gate
    -> evidence
    -> qualification
    -> operational activation or governed deferral
```

Therefore both arms have a deterministic guarantee gap for the R7 requirement-level audit.

This is mechanistic support for the AO8-R52 requirement candidate. It is not yet a requirements amendment.

## 6. Git-lifecycle realization

R11 is deterministic PARTIAL for C/D:

```text
selected ROTATE != completed rotation           PASS
failed remote probe not mistaken for success    PASS
attach/switch obligation remains visible        PASS
executable realization gate exists              NOT YET
```

This confirms AO10-O01 remains necessary.

## 7. Planner-only comparison remains genuinely open

Arm B is not a strawman. It may successfully reconstruct many tasks when its model-assisted TaskIntent chooses the right task-shaped evidence.

Model-free reasoning cannot honestly decide the required B-vs-C stopping set:

```text
R2 collaboration activation
R3 architecture trigger activation
R6 interruption/recovery routing
R7 obligation realization
R8 known-risk activation
```

Those comparisons move to P4.

## 8. Minimum P4 replay set

P3 reduces the decision-relevant fresh replay to 13 arm/scenario runs:

```text
B and C on R2, R3, R6, R7, R8   = 10 runs
D on N1, N3, N4                  = 3 runs
```

These are the minimum runs needed to resolve the preregistered B-vs-C stopping rule and the negative-control side of AO8-E01.

High-value non-minimum replays remain:

```text
R1   B/C/D  final ordered action fidelity
R4   B/C    Chat-28 supporting-evidence activation
R5   B/C    exact-source depth and cost
R10  C      malformed receipt handling without D verifier
```

These may be added if fresh replay capacity remains useful after the minimum decision set.

## 9. Result-path harness correction

The repository-wide `.gitignore` contains `**/results/`, so the protocol's proposed `ao9/results/` path would silently hide scored artifacts from ordinary Git durability. P3 detected this before any scored behavioral replay.

The exact P3 JSON bytes were relocated without modification to:

```text
ao9/traces/P3_MODEL_FREE_TRACE_V01.json
```

and retain SHA-256:

```text
909aa608d803143a3a1ce2436c1f499fad40eb26226276b1fded41edcf920734
```

For P4, durable scored collaborator outputs should use a non-ignored path such as `ao9/trial_outputs/`; evaluator material remains under `ao9/evaluations/`. This changes storage plumbing only, not scenario, arm, scoring, or no-tuning semantics.

## 10. Contamination boundary

Fresh P4 collaborators must not read:

```text
ao9/evaluator_keys/**
ao9/traces/P3_MODEL_FREE_TRACE_V01.json
ao9/evaluations/P3_MODEL_FREE_TRACE_V01.md
Research 231
prior scored P4 outputs
```

They may read only the assigned scenario input, assigned arm contract, permitted historical/project evidence, and a neutral execution harness.

## 11. P3 disposition

```text
AO9_P3=COMPLETE
MODEL_FREE_TRACE=FROZEN
FRESH_COLLABORATOR_REPLAY_USED=false
R9_C=DETERMINISTIC_GAP
R9_D=DETERMINISTIC_CLOSURE
R10_D=DETERMINISTIC_CLOSURE
R7_C_D=DETERMINISTIC_REALIZATION_GAP
R11_C_D=DETERMINISTIC_PARTIAL
AO8_E01=NOT_FINAL
B_VS_C_STOPPING_RULE=NOT_FINAL
R52_MECHANISTIC_SUPPORT=YES
P4_MINIMUM_DECISION_REPLAY_COUNT=13
NEXT=AO9_P4_FRESH_COLLABORATOR_REPLAY
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
