# Checkpoint 47: Common Baseline Resource Envelope Deterministically Validated

**Date:** 2026-08-10

## Purpose

Record deterministic validation of the common B0/B1 resource-control layer before any held-out H1/H2 treatment execution.

P0 behavioral/controller logic remains frozen. No held-out treatment run has occurred.

## Validation result

After pulling the common baseline resource-envelope implementation, the complete local Prototype V0 suite passed:

```text
58 passed in 22.70s
```

This validates the condition-neutral B0/B1 implementation of the preregistered held-out resource envelope:

```text
24 successful model calls
250,000 observed total tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries per semantic turn
```

The baseline runner now has deterministic coverage for pre-call token checks, observable failed-attempt usage, crossing-call retention, terminal completion above the token ceiling, Python-attempt accounting, and blocking of execution beyond the Python ceiling.

B0/B1 still do not receive P0's protected-final-test prospective safeguard. The validated change is resource-control parity only.

## Experimental interpretation

The successful test suite removes the final known resource-envelope asymmetry between the baseline runner and P0 before held-out orchestration is built.

It does not provide held-out evidence and does not alter:

```text
B0/B1 prompts
P0 behavior
held-out bundles
run order
semantic rubric
judge configuration
continuation/falsification thresholds
```

## Next step

Implement execution-time verification of the frozen H1/H2 bundle identities and materialize the exact preregistered 30-slot run plan before implementing paid sequential execution.
