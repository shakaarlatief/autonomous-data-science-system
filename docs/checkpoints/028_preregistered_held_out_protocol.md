# Checkpoint 28: Preregistered Held-Out Protocol

**Date:** 2026-08-09  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out protocol and implementation preparation  
**Scope:** Records the historical milestone described by this checkpoint: Preregistered Held-Out Protocol.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the pre-P0 registration of the Prototype V0 held-out evaluation contract after completing and semantically analyzing the full three-run B0 and three-run B1 development calibration.

The authoritative protocol is now:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

with a machine-readable companion:

```text
prototype_v0/configs/held_out_protocol_v0_1.json
```

This checkpoint does not implement P0 and does not change B0/B1 prompts or the development benchmark.

---

## Why this boundary exists

The development calibration revealed several facts that could otherwise tempt retrospective evaluation design:

```text
B0 and B1 already protect the final test very reliably;
B0 and B1 already repair the Phase 2 feature invalidation very reliably;
B1 improves explicit inherited-preprocessing diagnosis but only in 2/3 runs;
important row semantics can remain implicit despite correct operational behavior;
resource demand varies substantially from run to run;
one observed baseline trajectory used 19 of 20 provisional calls.
```

Therefore evaluation rules, budgets, and success thresholds must be chosen before observing P0 behavior.

---

## Registered held-out cases

H1 uses:

```text
member_key
scoring_period
lifecycle_flag
seed search starting at 811
```

H2 uses:

```text
account_ref
observation_period
profile_code
seed search starting at 1601
```

For each variant, the first seed at or above the registered start value that passes every benchmark self-test is selected. Seed choice is therefore based only on benchmark validity, not treatment performance.

The first passing bundles must be generated, self-tested, and fingerprinted before P0 implementation.

---

## Registered run protocol

Held-out execution remains:

```text
5 runs per condition on H1
5 runs per condition on H2
10 runs per condition total
30 treatment runs total
```

Condition order is pre-registered in a rotating interleaving schedule so B0, B1, and P0 are not systematically run in one fixed position.

---

## Registered common resource envelope

```text
maximum successful treatment-model calls: 24
maximum observed treatment tokens: 250,000
maximum Python execution attempts: 12
maximum output tokens per provider call: 30,000
maximum additional provider-generation retries: 2
Python timeout: 60 seconds
provider request timeout: 300 seconds
```

All P0 model calls, including state/repair reasoning calls, must count inside the same call/token envelope. Deterministic state operations do not create hidden reasoning budget.

Wall-clock runtime remains recorded but is diagnostic rather than a hard failure because provider latency is partly external and was not calibrated sufficiently for a defensible hard threshold.

---

## Registered semantic evaluator

The primary blinded semantic evaluator uses ten condition-neutral criteria scored 0/1/2:

```text
S1 row-unit correction
S2 validation/generalization reasoning
S3 inherited preprocessing contamination
S4 pre-Phase2 prediction-time feature eligibility
S5 authoritative timing-notice response
S6 repair completeness
S7 repair precision
S8 claim validity
S9 final validation rationale
S10 final conclusions answer the project question
```

The common interpretation is:

```text
0 = materially wrong/absent/invalid
1 = operationally acceptable but incomplete/implicit/weakly justified
2 = explicit, correct, scoped, and methodologically strong
```

Two independent condition-blinded judge passes are required for every behavior-evaluable run. Adjacent score disagreement is averaged; 0-versus-2 disagreement and any disagreement on semantic critical flags require blinded manual adjudication.

The primary judge sees only common external trajectory evidence and hidden benchmark truth. It does not receive P0 internal state, condition labels, or treatment prompts.

---

## Registered architecture-targeted outcome

The targeted architecture score is the mean of:

```text
S1 row semantics
S2 validation/generalization
S3 inherited preprocessing integrity
S6 repair completeness
S7 repair precision
```

A strong targeted pass requires all five consensus scores to equal 2.0.

This deliberately prevents P0 from receiving primary semantic credit merely because its internal state exists. The external project behavior must improve.

---

## Registered continuation threshold

P0 provides a continuation signal only if:

```text
it has no more critical failures than B1;
it has no critical architecture-induced false block/over-invalidation;
it shows either >=2 fewer critical failures than B1,
  or >=0.30 higher pooled targeted mean plus >=2 additional strong targeted passes;
it is not >0.10 worse than B1 on targeted mean in either individual variant;
it completes >=9/10 runs within budget and is not >1 completion below B1;
its median tokens/calls/Python attempts are each <=1.50 times B1;
it has <=1 budget-exhausted run;
noncritical architecture-induced friction appears in <=1/10 runs.
```

Strong falsification includes more critical failures than B1, critical false blocking/over-invalidation, architecture friction in at least 2/10 runs, held-out-specific hard coding, or B1 matching/exceeding reliability while P0 is at least 25 percent more expensive in median tokens or calls.

If neither continuation nor strong falsification thresholds are met, the result is classified as inconclusive/no demonstrated need for the architecture on this case family. The default response is to simplify or construct a harder falsification benchmark, not to expand architecture automatically.

---

## Infrastructure-versus-behavior rule

A terminal provider/infrastructure generation failure after registered retries is non-behavior-evaluable and may be replaced in the same replicate slot.

Behavioral failures are not replaced. These include:

```text
Python errors/timeouts
poor methodology
budget exhaustion
semantic failures
failure to finish the project
critical integrity failures
```

This prevents selective rerunning of disappointing treatment behavior.

---

## What is frozen now

Substantively registered before P0:

```text
held-out mechanisms and surface variants
seed-selection rule
run counts and order
actor model/configuration
resource envelope
semantic criteria and anchors
critical semantic triggers
judge blinding and two-pass combination
primary and diagnostic outcomes
continuation threshold
falsification threshold
replacement-run semantics
```

No P0 behavior has informed these choices.

---

## Remaining pre-P0 work

P0 is still blocked for two final experimental-control steps:

```text
1. Generate/self-test/fingerprint the first valid H1 and H2 bundles.
2. Implement the condition-neutral semantic normalizer/judge and calibrate it
   on the six already observed development baseline trajectories.
```

Only after those controls are recorded should P0 implementation begin.
