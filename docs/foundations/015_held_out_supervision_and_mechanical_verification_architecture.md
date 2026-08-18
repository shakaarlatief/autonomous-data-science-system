# Foundation 015: Held-Out Supervision and Mechanical Verification Architecture

**Date:** 2026-08-18  
**Status:** Operational experiment-infrastructure design, introduced during Prototype V0 held-out execution  
**Scope:** Condition-neutral orchestration and post-run verification only. This document does not modify the frozen B0, B1, or P0 treatments.

## Purpose

The first ten resolved Prototype V0 held-out slots exposed an operational scaling problem that is separate from the scientific experiment itself.

The registered experiment is sequential and carefully controlled, but the surrounding human workflow had become:

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

This procedure was deliberately conservative at the beginning of held-out execution. It helped validate the replacement policy, identify provider structured-output ambiguity, distinguish a pre-provider credential interruption from a real attempt, confirm terminal budget-crossing semantics, and establish confidence in the frozen executor.

However, once those mechanics had been exercised repeatedly, the human became an unnecessary transport and bookkeeping layer. The process did not scale to larger experiments and was consuming substantial wall-clock time without adding corresponding scientific value.

The project therefore introduces an explicit distinction between:

```text
FROZEN TREATMENT EXECUTION
what B0, B1, and P0 experience

and

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
H1/H2 bundles
bundle identities
run order
condition order
replacement eligibility
maximum attempts per slot
model/provider configuration
reasoning effort
call/token/Python limits
provider normalization
retry semantics
protected final-test rules
A0-A4 evaluator
semantic rubric
blinded semantic judge
continuation and falsification criteria
```

The new infrastructure is permitted to:

```text
read already-persisted attempt artifacts;
revalidate the frozen plan and bundle identities;
recompute deterministic mechanical checks;
verify resource and trace accounting;
record compact verification reports outside attempt directories;
call the already-frozen execute_next_attempt function sequentially;
advance automatically when the persisted attempt is mechanically coherent;
apply the already-frozen replacement policy through the existing runner;
pause when experiment integrity cannot be established;
package compact reports for later review.
```

It is not permitted to:

```text
change treatment-visible artifacts;
write into completed attempt directories;
feed prior held-out outcomes to later treatments;
perform semantic S1-S10 judging during execution;
change a behavior-evaluable outcome into a replacement;
change slot order;
run treatments concurrently in Prototype V0;
modify budgets or stopping rules;
or use held-out outcomes to tune P0, B0, or B1.
```

---

## 2. Architecture

The operational architecture is:

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

The most important direction of information flow is one-way:

```text
treatment attempt -> verifier/supervisor
```

There is no path from verifier output back into treatment prompts, project bundles, P0 state, or later model context.

---

## 3. Mechanical verifier

`prototype_v0/src/ads_v0/heldout_verifier.py` verifies persisted experiment mechanics.

The first verifier schema is `v0.1.0`.

For each attempt it checks at least:

```text
M01 required attempt artifacts exist
M02 attempt identity matches the frozen slot and attempt number
M03 plan and bundle hashes match frozen identities
M04 registered runtime configuration matches the frozen plan
M05 summary and executor classification are internally consistent
M06 resource arithmetic and budget flags are self-consistent
M07 trace sequences and resource counts reconcile with summary totals
M08 deterministic evaluation recomputes exactly from the persisted trace
M09 milestone artifacts agree with trace completion state
M10 protected final-test value access is at most once and occurs after final lock
M11 conversation shape reconciles with successful model-call count
```

These are not new treatment-scoring criteria. They are integrity checks on the experiment artifacts and on facts that were already being inspected manually after each attempt.

The verifier also records non-blocking behavioral observations such as:

```text
budget exhaustion
incomplete run
Python error or timeout
treatment command error
provider generation retry/failure
deterministic assertion failure
```

These observations do not make an attempt replacement-eligible. They remain behavioral evidence under the frozen protocol.

This distinction is important:

```text
INTEGRITY FAILURE
The supervisor cannot establish that the experiment artifact is mechanically coherent.
=> pause automatic execution.

BEHAVIORAL FAILURE OR FRICTION
The treatment itself behaved poorly, exhausted budget, made a Python mistake,
or failed a deterministic criterion.
=> retain exactly as registered and continue if experiment integrity is intact.
```

---

## 4. Verifier reports live outside treatment artifacts

Treatment attempt directories remain append-only evidence.

The verifier writes to:

```text
results/held_out/mechanical_verification/
```

rather than writing inside:

```text
results/held_out/attempts/<attempt_id>/
```

Each report includes SHA-256 fingerprints of the attempt artifacts it verified. This creates a compact linkage from a verification result to the exact source bytes without turning the verification output into treatment input.

The verifier can therefore be rerun later against the same attempt and its result can be audited against source hashes.

---

## 5. Retroactive validation before prospective use

The supervisor must not immediately replace the manual process merely because its code exists.

Before any new paid held-out attempt is launched through the supervisor:

```text
1. run the deterministic software test suite;
2. run the verifier retroactively over every existing completed attempt;
3. require verifier integrity PASS for all existing completed attempts;
4. compare the verifier's compact mechanical summaries with the manual records
   already preserved in the held-out ledger and checkpoints;
5. fix verifier/supervisor defects only, without changing treatment behavior;
6. freeze the validated supervision layer for the remaining V0 execution.
```

This retroactive step matters because it applies the same verifier to earlier and later attempts rather than creating one post-hoc rule for only the remaining slots.

It also provides a direct parity test against the manual inspection process that was used for the first ten slots.

---

## 6. Sequential supervisor

`prototype_v0/src/ads_v0/heldout_supervisor.py` wraps the existing executor rather than replacing it.

The supervisor can:

```text
show status;
verify all existing attempts without inference;
run a bounded batch of sequential attempts;
mechanically verify each completed attempt immediately;
automatically continue through clean behavior-evaluable outcomes;
automatically apply registered replacement attempts through the frozen runner;
pause on verifier integrity failure, interrupted attempts, replacement exhaustion,
or another safety state;
export one compact review ZIP.
```

A batch is bounded explicitly by the user with a maximum number of paid model attempts.

For example:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 3
```

This does not mean three treatment slots necessarily resolve. A provider failure followed by a replacement consumes two paid model attempts while remaining inside one preregistered slot.

The batch remains sequential. No second attempt begins until the prior attempt has returned, persisted its executor record, and passed mechanical integrity verification.

---

## 7. Automatic replacement remains the frozen replacement policy

If the existing runner classifies an attempt as:

```text
NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE
replacement_eligible = true
slot_resolved = false
```

and the verifier confirms the artifact mechanics are coherent, the supervisor may allow the next loop iteration to execute the registered replacement attempt inside the same slot.

This is not a new replacement decision. It is automation of the already-frozen policy.

If the runner instead returns a behavior-evaluable result, including:

```text
poor methodology
Python error or timeout
budget exhaustion
incomplete work
deterministic failure
```

the slot remains resolved and the supervisor must not replace it.

---

## 8. Compact exports replace repeated ZIP transport

The supervisor writes compact reports under:

```text
results/held_out/supervisor/
results/held_out/mechanical_verification/
```

and can package them into one ZIP under:

```text
results/held_out/supervisor_exports/
```

The compact export deliberately excludes raw treatment conversation text.

Its purpose is to allow one review artifact to summarize multiple attempts rather than requiring the user to manually create and upload one raw ZIP after every normal run.

Raw attempt artifacts remain local and available if a verifier failure, anomaly, or later audit requires deeper inspection.

This yields a tiered review model:

```text
normal mechanically coherent run
    -> compact verifier report is sufficient for operational continuation

mechanical integrity failure or unexpected infrastructure state
    -> pause and inspect raw artifacts

later semantic evaluation phase
    -> use the frozen normalized external transcript and blinded judge procedure
```

---

## 9. Why semantic judging is still deferred

Automation must not collapse mechanical supervision and scientific judgment into one stage.

The supervisor can establish facts such as:

```text
what files exist;
which hashes were used;
how many provider calls occurred;
how many Python attempts occurred;
whether usage arithmetic reconciles;
whether A0-A4 recompute;
which features were locked;
when protected test access occurred;
whether a final report exists.
```

It must not decide during execution:

```text
whether row semantics were understood deeply enough;
whether validation reasoning was scientifically strong;
whether inherited preprocessing contamination was recognized adequately;
whether Phase 2 repair was semantically precise;
or whether final claims were appropriately scoped.
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

Future capabilities may include:

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
and CI-style behavioral regression suites.
```

Prototype V0 should not retroactively adopt concurrency because concurrency was not part of its frozen execution regime. The current supervisor therefore gains scalability by removing human transport and repeated inspection while preserving sequential treatment execution.

---

## 11. Broader system lesson

The experiment has produced a system-development lesson independent of whether P0 eventually wins or loses.

Manual human supervision is useful while infrastructure is immature and failure modes are unknown. Once repeated checks become stable and formalizable, continued manual repetition becomes both expensive and less reproducible than deterministic automation.

The general principle is:

> Human attention should concentrate on ambiguous, semantic, exceptional, or high-value decisions. Repeated mechanical integrity work should become explicit automated infrastructure once its rules are understood well enough to encode and validate.

This is closely aligned with the long-term Autonomous Data Science System vision. The goal is not automation for its own sake. The goal is to move stable process intelligence out of repeated human navigation while retaining human intervention where it materially adds value.

---

## 12. Current status

At creation of this foundation:

```text
10 / 30 held-out treatment slots are resolved;
the next frozen slot remains h1-r04-b1-a01;
heldout_verifier.py has been implemented;
heldout_supervisor.py has been implemented;
unit tests for both layers have been added;
no new paid attempt has yet been launched through the supervisor.
```

Prospective supervisor execution remains gated on deterministic tests and retrospective verification of all existing completed attempts.

This is an experiment-infrastructure change, not a treatment change.
