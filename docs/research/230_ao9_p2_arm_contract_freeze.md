# Research 230: AO-9 P2 Arm-Contract Freeze

**Date:** 2026-09-21
**Status:** AO-9 P2 COMPLETE / FOUR ARM CONTRACTS FROZEN / P3 MODEL-FREE TRACE NEXT
**Program:** Research 219
**Protocol:** Research 228 / AO9-HISTORICAL-REGRESSION-PROTOCOL-V01
**Scenario packet:** Research 229 / commit 76f5d6e784651f244d882b5373d7f750b1a706ef
**Arm packet:** docs/research/project_knowledge_activation_orchestration/ao9/arm_contracts/
**Manifest:** docs/research/project_knowledge_activation_orchestration/ao9/arm_contracts/MANIFEST.json
**Scope:** Freeze exact A/B/C/D mechanism contracts before any AO-9 scored trace so evaluator judgment cannot strengthen or weaken an arm after results are visible.
**Authority:** Research-fixture freeze. This does not amend AO-3 through AO-7, Requirements V0.2, Specification 028, or production behavior.

## 1. Arm A

`BASELINE_CURRENT_BEHAVIOR` is historical evidence, not a current-HEAD simulation.

Where a preserved incident or blind baseline exists, that exact evidence is the arm result. Where no historical behavioral result exists, Arm A may be N/A rather than reconstructed using today's AO-aware repository.

## 2. Arm B

`PLANNER_ONLY` is intentionally strong.

It receives Specification 028 section 26 reconstruction semantics plus authority resolution when the planner calls for it. It can form task-shaped must-load governing/supporting evidence and fail/escalate conditions.

It does not receive AO-3's event/state ControlObligationSet, AO-4 evolution orchestration, AO-5 recovery routing, AO-6 Git lifecycle control, AO-7 bridge behavior, AO-3 postflight self-observation, or the MC-0021 output-shape amendment.

This avoids a strawman planner baseline.

## 3. Arm C

`AO3_AO7_CANDIDATE` is frozen to semantic target:

~~~text
f73239ee486132a94701de80514ffd11480b9ecd
~~~

It includes the accepted AO-3 through AO-7 architecture only.

For the decisive R9 seam, P2 freezes an important interpretation:

~~~text
if S3 fast-paths
and no other candidate-defined obligation requires S6,
Arm C does not gain a new independent post-output trigger by implication.
~~~

S8 may check an established ActionContract; it does not itself invent the missing S6 contract.

## 4. Arm D

`AO3_AO7_PLUS_REVIEW_AMENDMENT_VARIANT` equals C plus only three preregistered deltas:

~~~text
independent output/action-shape re-entry
structural receipt/claim verification
NO_CONTRACT_AVAILABLE distinct from CONFORMANT
~~~

The output/action-shape screen runs after a proposed result exists and before dispatch/mutation. It is independent of the S1/S3 event-class hypothesis.

For induced mechanism scenarios, the scenario may freeze a shape fact such as `ordered_operational_or_procedural_steps=true`; the D arm may use that fact directly without reclassifying the owner event.

The screen can only force bounded authority/contract closure. It cannot authorize an action or create semantic authority.

## 5. D is intentionally narrow

P2 explicitly excludes from Arm D:

~~~text
universal control ledger
three-field continuity collapse
veto-only bridge
Requirements R51/R52 amendments
predicate-retirement machinery
new explicit discharges metadata
any other post-review fix
~~~

So a good D result cannot silently accumulate every useful idea from MC-0021.

## 6. Structural verification boundary

D's verifier may prove structural claims such as existence of a cited revision/path/identity/constraint ID and deterministic predicate recomputation.

It may not claim this proves that a model read, understood, or correctly used a source.

That distinction is frozen before R10 scoring.

## 7. Scoring still has not started

At P2 closure:

~~~text
scenario inputs frozen
evaluator keys frozen
four arm contracts frozen
no model-free trace scored
no fresh collaborator replay scored
no arm may be edited after scored execution starts
~~~

## 8. Next

AO-9 P3 performs the model-free mechanism trace across the frozen scenario packet and frozen arm contracts.

P3 must record ambiguity as ambiguity rather than using evaluator knowledge to infer model behavior. Cases whose outcome genuinely depends on a probabilistic model judgment should be carried to P4 fresh collaborator replay.

~~~text
AO9_P2=COMPLETE
ARMS=A|B|C|D
ARM_CONTRACTS_FROZEN=true
SCORING_STARTED=false
NEXT=AO9_P3_MODEL_FREE_MECHANISM_TRACE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
~~~
