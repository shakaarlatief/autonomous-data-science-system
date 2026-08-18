# Foundation 015: Held-Out Supervision and Mechanical Verification Architecture

**Date:** 2026-08-18  
**Status:** Validated and frozen operational experiment infrastructure for the remainder of Prototype V0 held-out execution  
**Scope:** Condition-neutral orchestration and post-run mechanical verification only. This document does not modify the frozen B0, B1, or P0 treatments.

## Purpose

The first ten resolved Prototype V0 held-out slots exposed an operational scaling problem separate from the scientific experiment itself.

The scientific experiment was stable and carefully controlled, but the surrounding human workflow had become:

```text
run one attempt
-> copy terminal output into chat
-> classify the attempt
-> manually create a ZIP
-> upload the ZIP
-> manually inspect repeated mechanical facts
-> update repository state
-> pull repository changes
-> run the next attempt
-> repeat
```

This conservative procedure was useful early in held-out execution because it helped validate replacement semantics, expose provider structured-output ambiguity, distinguish a pre-provider credential interruption from a real treatment attempt, confirm terminal budget-crossing behavior, and establish confidence in the frozen executor.

Once those mechanics had been exercised repeatedly, however, the human had become an unnecessary transport and bookkeeping layer. The process did not scale and consumed substantial wall-clock time without adding corresponding scientific value.

The project therefore distinguishes:

```text
FROZEN TREATMENT EXECUTION
what B0, B1, and P0 experience

from

EXTERNAL EXPERIMENT SUPERVISION
how completed attempts are mechanically verified, sequenced, summarized, and reviewed
```

The goal is to automate the second without changing the first.

---

## 1. Non-negotiable experimental boundary

The supervisor must not alter any frozen treatment property.

The following remain governed by Foundation 012 and the existing held-out runner:

```text
B0 prompt
B1 prompt
P0 controller and knowledge
H1/H2 bundles and identities
run and condition order
replacement eligibility and maximum attempts per slot
model/provider configuration
reasoning effort
call/token/Python limits
provider normalization and retry semantics
protected final-test rules
A0-A4 evaluator
semantic rubric and blinded judge
continuation and falsification criteria
```

The external supervision layer may:

```text
read already-persisted attempt artifacts;
revalidate frozen plan and bundle identities;
recompute deterministic mechanical checks;
verify resource and trace accounting;
record compact verification reports outside attempt directories;
call the already-frozen execute_next_attempt function sequentially;
advance automatically when the persisted attempt is mechanically coherent;
allow the already-frozen replacement policy to operate through the existing runner;
pause when experiment integrity cannot be established;
package compact reports for review.
```

It may not:

```text
change treatment-visible artifacts;
write into completed attempt directories;
feed prior held-out outcomes to later treatments;
perform semantic S1-S10 judging during execution;
change a behavior-evaluable outcome into a replacement;
change slot order;
run treatments concurrently in Prototype V0;
modify budgets or stopping rules;
use held-out outcomes to tune P0, B0, or B1.
```

---

## 2. Architecture

```text
                 FROZEN RUN PLAN
                       |
                       v
              heldout_runner.py
          existing frozen executor
                       |
                 one attempt
                       |
                       v
          append-only attempt artifacts
                       |
                       v
              heldout_verifier.py
             read-only mechanical layer
                       |
              integrity PASS / FAIL
                       |
              +--------+--------+
              |                 |
            PASS               FAIL
              |                 |
              v                 v
      heldout_supervisor.py     pause
        sequential control      human review
              |
              v
       next frozen attempt
```

The critical information-flow property is one-way:

```text
treatment attempt -> verifier/supervisor
```

There is no path from verifier output back into treatment prompts, project bundles, P0 state, or later treatment-model context.

---

## 3. Mechanical verifier

`prototype_v0/src/ads_v0/heldout_verifier.py` verifies persisted experiment mechanics. The current schema is `v0.1.0`.

For each completed attempt it checks:

```text
M01 required attempt artifacts exist
M02 attempt identity matches frozen slot and attempt number
M03 plan and bundle hashes match frozen identities
M04 registered runtime configuration matches frozen plan
M05 summary and executor classification are internally consistent
M06 resource arithmetic and budget flags are self-consistent
M07 trace sequences and resource counts reconcile with summary totals
M08 deterministic evaluation recomputes exactly from persisted trace
M09 milestone artifacts agree with trace completion state
M10 protected final-test value access is at most once and occurs after final lock
M11 conversation shape reconciles with successful model-call count
```

These are not new treatment-scoring criteria. They formalize facts that were already being inspected manually after each attempt.

The verifier also records non-blocking behavioral observations such as:

```text
budget exhaustion
incomplete run
Python error or timeout
treatment command error
provider generation retry/failure
deterministic assertion failure
```

The distinction is deliberate:

```text
INTEGRITY FAILURE
The supervisor cannot establish that the persisted experiment evidence is mechanically coherent.
=> pause automatic execution.

BEHAVIORAL FAILURE OR FRICTION
The treatment itself behaved poorly, exhausted budget, made a Python mistake,
or failed a deterministic criterion.
=> retain exactly as registered and continue if experiment integrity is intact.
```

A poor treatment outcome must never be converted into an infrastructure excuse for replacement.

---

## 4. Verification reports are outside treatment artifacts

Treatment attempt directories remain append-only evidence.

The verifier writes to:

```text
results/held_out/mechanical_verification/
```

rather than modifying:

```text
results/held_out/attempts/<attempt_id>/
```

Each verification report includes SHA-256 fingerprints of the attempt artifacts it inspected. This links a compact report to exact source bytes without making verifier output part of treatment input.

---

## 5. Retrospective validation before prospective use

Because the supervisor was introduced after ten treatment slots had already resolved, prospective use required a condition-neutral validation gate:

```text
1. run the full deterministic software test suite;
2. run the verifier over every existing completed attempt directory;
3. require integrity PASS for all completed attempts;
4. compare compact summaries with the manual records already preserved;
5. repair only verifier/supervisor defects if needed;
6. freeze the validated supervision layer before paid use.
```

This ensures that the same verifier applies to earlier and later attempts rather than creating one set of integrity rules only for the remaining slots.

### Validation result

The gate passed on 2026-08-18:

```text
pytest
    77 passed in 30.43s

retrospective verifier
    completed attempts verified: 12
    integrity passed: 12
    integrity failed: 0
```

The 12 completed attempt directories included:

```text
10 behavior-evaluable retained attempts
2 non-behavior-evaluable H1 R2 B0 provider/interface attempts
```

The compact reports reproduced the established manual record for:

```text
attempt identities and classifications;
model-call, token, and Python-attempt totals;
P0 budget-exhaustion states;
H1 R2 B0 provider failures and replacement eligibility;
H1 R2 B0 A03 Python timeout;
H1 R3 P0 incomplete final-report state;
H1 R4 B0 Python error and recovery;
final-lock and protected-test sequencing;
final-report presence;
A0-A4 deterministic results.
```

No mechanical discrepancy with the prior manual record was found.

Validated implementation blob identities:

```text
heldout_supervisor.py
    ef6ffbea671d4f177e41002becfd8751e176ddad

heldout_verifier.py
    03fb33280f87d0056a3dbb264a63651df9ffb431
```

These versions are frozen for remaining Prototype V0 operational use unless a genuine condition-neutral infrastructure defect is discovered.

Detailed validation provenance:

```text
docs/checkpoints/082_held_out_supervisor_retroactively_validated_and_frozen_for_live_use.md
```

---

## 6. Sequential supervisor

`prototype_v0/src/ads_v0/heldout_supervisor.py` wraps the existing executor rather than replacing it.

It can:

```text
show status;
verify all existing attempts without inference;
run a bounded batch of sequential attempts;
mechanically verify each completed attempt immediately;
automatically continue through mechanically coherent behavior-evaluable outcomes;
allow registered provider-failure replacement attempts through the frozen runner;
pause on verifier integrity failure, interrupted attempt, replacement exhaustion,
or another existing runner safety state;
export one compact review ZIP.
```

A batch is bounded explicitly by a maximum number of paid model attempts:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 3
```

Three paid attempts do not necessarily mean three resolved treatment slots. A provider failure followed by a replacement consumes two paid attempts while remaining inside one preregistered slot.

The batch remains sequential. No second attempt begins until the previous attempt has returned, persisted its executor record, and passed mechanical integrity verification.

---

## 7. Automatic replacement is not a new policy

If the existing runner classifies an attempt as:

```text
NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE
replacement_eligible = true
slot_resolved = false
```

and the verifier confirms mechanical coherence, the next supervisor loop iteration may launch the registered replacement inside the same slot.

This is automation of the frozen replacement rule, not a new replacement decision.

If a result is behavior-evaluable, including an outcome with:

```text
poor methodology
Python error or timeout
budget exhaustion
incomplete work
deterministic failure
```

the slot remains resolved and the supervisor must not replace it.

---

## 8. Compact exports replace repeated raw-ZIP transport

The supervisor stores compact operational records under:

```text
results/held_out/supervisor/
results/held_out/mechanical_verification/
```

and can package them under:

```text
results/held_out/supervisor_exports/
```

The normal compact export deliberately excludes raw treatment conversation text.

The review model is therefore tiered:

```text
normal mechanically coherent run
    -> compact verifier report is sufficient for operational continuation

mechanical integrity failure or unexpected infrastructure state
    -> pause and inspect raw artifacts

later semantic evaluation phase
    -> use the frozen normalized external transcript and blinded judge procedure
```

Raw attempt artifacts remain local and available for anomaly investigation, later audit, and semantic-evaluation preparation.

---

## 9. Semantic judging remains deferred

The supervisor can establish mechanical facts such as:

```text
what files exist;
which hashes were used;
how many provider calls and Python attempts occurred;
whether usage arithmetic reconciles;
whether A0-A4 recompute;
which features were locked;
when protected test access occurred;
whether a final report exists.
```

It must not decide during execution:

```text
whether row semantics were understood deeply enough;
whether validation reasoning was scientifically appropriate;
whether inherited preprocessing contamination was adequately recognized;
whether Phase 2 repair was semantically precise;
whether final claims were appropriately scoped.
```

Those remain S1-S10/SC1-SC2 questions for the preregistered blinded semantic stage.

---

## 10. Scalability beyond Prototype V0

The current supervisor is deliberately local and sequential because Prototype V0 has a frozen sequential order.

A future evaluation platform may generalize into:

```text
experiment specification
    -> scheduler
    -> worker pool
    -> immutable artifact store
    -> mechanical validation
    -> blinded evaluation queue
    -> results database
    -> experiment report
```

Potential later capabilities include:

```text
parallel workers for experiments that preregister concurrency;
provider rate-limit management;
cost ceilings across experiment families;
resume/retry orchestration;
artifact-store integration;
content-addressed attempt bundles;
generated experiment dashboards;
automatic blinded semantic-judge queues;
aggregate statistical analysis;
multiple benchmark families;
multiple treatment-model families;
reproducible experiment manifests;
CI-style behavioral regression suites.
```

Prototype V0 should not retroactively adopt concurrency because concurrency was not part of its frozen execution regime.

---

## 11. Broader system lesson

The experiment has produced a development lesson independent of whether P0 eventually wins or loses.

Manual human supervision is useful while infrastructure is immature and failure modes are unknown. Once repeated checks become stable and formalizable, continuing to perform them manually becomes expensive, less reproducible, and harder to scale.

The general principle is:

> Human attention should concentrate on ambiguous, semantic, exceptional, or high-value decisions. Repeated mechanical integrity work should become explicit automated infrastructure once its rules are understood well enough to encode and validate.

This is closely aligned with the long-term Autonomous Data Science System vision. The goal is not automation for its own sake. The goal is to move stable process intelligence out of repeated human navigation while retaining human intervention where it materially adds value.

---

## 12. Current operational status

At validation freeze:

```text
10 / 30 held-out treatment slots resolved
20 / 30 remain
next frozen attempt: h1-r04-b1-a01
retrospective verification: 12 / 12 integrity PASS
software tests: 77 passed
semantic judging: not started
```

The first prospective supervisor batch is intentionally bounded to three paid model attempts. Its compact export should be reviewed before increasing unattended batch size.

This remains an experiment-infrastructure architecture change, not a treatment change.