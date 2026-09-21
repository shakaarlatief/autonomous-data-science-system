# Research 229: AO-9 P1 Scenario and Evaluator-Key Freeze

**Date:** 2026-09-21
**Status:** AO-9 P1 COMPLETE / SCENARIOS + EVALUATOR KEYS FROZEN / P2 ARM CONTRACTS NEXT
**Program:** Research 219
**Protocol:** Research 228 / AO9-HISTORICAL-REGRESSION-PROTOCOL-V01
**Protocol freeze commit:** bf48758eaee2b87559ac86f4aee02f48cecf37e5
**Packet:** docs/research/project_knowledge_activation_orchestration/ao9/
**Manifest:** docs/research/project_knowledge_activation_orchestration/ao9/MANIFEST.json
**Scope:** Freeze the AO-9 trial-visible scenario packet and evaluator-only scoring keys before arm contracts are authored or any scored execution begins.
**Authority:** Research-fixture freeze. This does not score an arm, amend AO-3 through AO-7, change Requirements V0.2/Specification 028, or authorize production implementation.

## 1. P1 result

AO-9 now has 15 isolated scenario/key pairs:

~~~text
R1 .. R11
N1 .. N4
~~~

Each trial-visible scenario lives under `ao9/scenarios/`; each evaluator-only key lives separately under `ao9/evaluator_keys/`. The manifest records exact SHA-256 digests for both sides. No scored arm result exists yet.

## 2. Exact historical boundaries verified

~~~text
R1  a570f0d87b77960ae0715b291de0d5f6e884e4d0
R2  1a422c79dc67384426ad10e28c2fc6845147f9e0
R3  736fb1b91301effd311a0d06439f1c6a92183aee
R4  3cdedc09c992c2fd8d2e57c1a20e82627a1b6eba
R5  2d425c76c385961cdd7f986c17ed83437a3d3806
R6  851ff497261a15d7ca499b1b68e92fce70202672
R7  cc2ce7ec2f129b8887bd8be1c0703b414445d580
R11 432485a7481f43add075f619e17e49cf9628215e
control-model target f73239ee486132a94701de80514ffd11480b9ecd
~~~

Targeted anchor checks also verified that R3 contains AB-027/AB-031, R4 contains Research 219 plus Source Evidence 001/002, R6 contains Research 106 plus Specification 025, R7 contains Specification 028 plus Checkpoint 542, and R11 contains Research 225.

R8 deliberately remains mechanism-level historical evidence because the failure corpus does not freeze one clean pre-rediscovery snapshot. AO-9 will not invent blind-snapshot precision that the evidence does not support.

## 3. Scenario integrity

The packet preserves the Research 228 provenance classes HISTORICAL, HISTORICAL_BASELINE, CONSTRUCTED_ADJACENT and INDUCED_CONTROL.

Historical baseline prompts reuse already-frozen request semantics where appropriate: R1 from BL-001, R2 from BL-002U, and R5 from BL-004. Constructed/induced scenarios do not name the preferred architecture remedy in their trial-visible task.

Evaluator expectations, fail conditions, exact historical keys and mechanism-specific scoring details are isolated from scenario input.

## 4. N2 is intentionally not fabricated

N2 tests an explicit owner override of a mandatory obligation. P1 has not identified a concrete project-controlled policy that authorizes a specific override case suitable for this regression.

~~~text
N2=DEFERRED_NA_PENDING_VALID_OVERRIDE_POLICY
~~~

This is preferable to inventing permission merely to fill the matrix. If AO-9 later identifies a real override policy before scored execution, N2 may be versioned prospectively. Otherwise it remains N/A.

## 5. Important evaluator keys

R1 freezes the exact 11-step restart sequence from the prior BL-001 evaluation so final ordered task fidelity is independently scorable.

R4 requires stage-critical Source Evidence 001/002 to surface as supporting evidence while remaining non-authoritative.

R7 freezes the distinction `missing W0 realization path != retroactive W0 gate failure`.

R9 does not predeclare that Arm C must fail or Arm D must pass. It freezes the safety criterion that, given the fixed insufficient event interpretation, an ordered consequential draft cannot be dispatched without applicable authority/contract closure or explicit fail-visible no-contract state.

R10 requires structural invalidity detection without allowing the verifier to claim semantic-comprehension proof.

## 6. Scoring has not started

~~~text
scenario inputs frozen
evaluator keys frozen
arm contracts not yet frozen
no model-free arm trace run
no fresh collaborator replay run
no evaluator score assigned
~~~

Therefore the Research 228 no-tuning boundary remains intact.

## 7. Next

AO-9 P2 must freeze exact arm contracts for A/B/C/D. Those contracts must define enough executable/mechanistic semantics that P3 can trace each scenario without evaluator improvisation.

In particular P2 must prevent Arm C quietly inheriting MC-0021 amendments, Arm D gaining extra fixes beyond the preregistered delta, Arm B being weakened into a strawman, or Arm A being reconstructed from contaminated current-HEAD behavior.

~~~text
AO9_P1=COMPLETE
SCENARIOS=15
EVALUATOR_KEYS=15
SCORING_STARTED=false
N2=DEFERRED_NA_PENDING_VALID_OVERRIDE_POLICY
NEXT=AO9_P2_ARM_CONTRACT_FREEZE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
~~~
