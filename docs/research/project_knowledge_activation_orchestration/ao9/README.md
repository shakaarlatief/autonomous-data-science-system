# AO-9 Scenario and Evaluator-Key Packet

**Program:** Research 219 / AO-9
**Protocol:** Research 228 / AO9-HISTORICAL-REGRESSION-PROTOCOL-V01
**Protocol freeze commit:** bf48758eaee2b87559ac86f4aee02f48cecf37e5
**Status:** P1 SCENARIO / EVALUATOR-KEY CONSTRUCTION
**Authority:** Research fixtures only. These files do not amend architecture or project authority.

This packet separates trial-visible scenario inputs from evaluator-only expected behavior.

~~~text
scenarios/
    trial-visible problem/event facts only

evaluator_keys/
    expected mechanism, applicable dimensions and scoring key
    NEVER trial input

arm_contracts/
    created/frozen in AO-9 P2

results/
evaluations/
    created only after scored execution begins
~~~

Historical snapshots are exact where a suitable boundary is known. Where no clean historical snapshot is available, the scenario is explicitly mechanism-level rather than pretending to be a blind replay.

Constructed and induced controls follow the failure-corpus freeze rule: parent mechanism is named in metadata, surface wording is changed, and the task does not name the preferred remedy.

N2 is intentionally deferred until a real policy-authorized owner-override case is available. AO-9 will not invent an override permission merely to fill the matrix.
