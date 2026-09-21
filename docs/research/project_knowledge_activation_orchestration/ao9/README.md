# AO-9 Scenario and Evaluator-Key Packet

**Program:** Research 219 / AO-9
**Protocol:** Research 228 / AO9-HISTORICAL-REGRESSION-PROTOCOL-V01
**Protocol freeze commit:** bf48758eaee2b87559ac86f4aee02f48cecf37e5
**Status:** P4 HARNESS FROZEN / FRESH REPLAY NEXT
**Authority:** Research fixtures only. These files do not amend architecture or project authority.

This packet separates trial-visible scenario inputs from evaluator-only expected behavior.

~~~text
scenarios/
    trial-visible problem/event facts only

evaluator_keys/
    expected mechanism, applicable dimensions and scoring key
    NEVER trial input

arm_contracts/
    frozen A/B/C/D mechanism contracts from AO-9 P2

traces/
    durable model-free mechanism traces from AO-9 P3

p4_assignments/
    frozen minimum decision-relevant fresh-collaborator assignments

trial_outputs/
    reserved non-ignored durable path for P4 fresh-collaborator outputs

evaluations/
    evaluator-side analyses; NEVER trial input
~~~

Historical snapshots are exact where a suitable boundary is known. Where no clean historical snapshot is available, the scenario is explicitly mechanism-level rather than pretending to be a blind replay.

Constructed and induced controls follow the failure-corpus freeze rule: parent mechanism is named in metadata, surface wording is changed, and the task does not name the preferred remedy.

N2 is intentionally deferred until a real policy-authorized owner-override case is available. AO-9 will not invent an override permission merely to fill the matrix.

Harness note: the repository-wide `**/results/` ignore rule makes `results/` unsuitable for durable AO-9 evidence. Research 231 records the pre-scoring storage correction to `traces/` and `trial_outputs/`; experimental semantics are unchanged.
