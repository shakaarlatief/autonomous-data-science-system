# Checkpoint 26: Baseline Development Calibration Complete

**Date:** 2026-08-09  
**Status:** Historical mixed checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Prototype V0 development calibration  
**Scope:** Records the historical milestone described by this checkpoint: Baseline Development Calibration Complete.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record completion of the pre-specified real-model development calibration for the two baseline conditions.

Prototype V0 now has three behavior-evaluable B0 trajectories and three behavior-evaluable B1 trajectories under the same fixed development configuration. This closes the baseline execution phase. The next step is not another baseline run. It is full cross-run semantic and resource analysis before freezing the held-out protocol and implementing P0.

## Fixed development configuration

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max output tokens per call: 30,000
max additional generation retries: 2
request timeout: 300 seconds
strict Structured Outputs
multi-turn previous_response_id continuation
all-turn reasoning context
```

No prompt, benchmark, model, reasoning-effort, command-protocol, or runtime changes were made during the six behavior-evaluable baseline trajectories.

## Completed baseline trajectories

| Run | Condition | Successful calls | Generation failures | Total observed tokens | Critical deterministic assertions |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 0 | 103,240 | Pass |
| `dev-b0-04` | B0 | 18 | 0 | 147,482 | Pass |
| `dev-b0-05` | B0 | 19 | 0 | 182,271 | Pass |
| `dev-b1-01` | B1 | 15 | 0 | 117,606 | Pass |
| `dev-b1-02` | B1 | 16 | 0 | 112,683 | Pass |
| `dev-b1-03` | B1 | 17 | 0 | 143,014 | Pass |

Every behavior-evaluable baseline run:

```text
completed successfully
had zero generation failures
remained behavior-evaluable
passed all current critical deterministic assertions
finished within the 20-call development ceiling
```

## Resource observations

### B0

```text
calls: 15, 18, 19
mean calls: 17.33

tokens: 103,240; 147,482; 182,271
mean tokens: 144,331
range: 79,031
```

### B1

```text
calls: 15, 16, 17
mean calls: 16.00

tokens: 117,606; 112,683; 143,014
mean tokens: approximately 124,434
range: 30,331
```

The first matched B0/B1 pair had made B1 look more expensive. Across all three development replicates, the descriptive mean reverses: B0 used approximately 19,897 more observed tokens per run on average than B1, about 16 percent relative to the B1 mean.

This reversal is an important calibration lesson. Single-run cost comparisons are not reliable enough for protocol decisions.

No condition-level efficiency conclusion should yet be drawn from three runs. The raw trajectories must be decomposed because additional calls/tokens may represent useful depth, redundant work, longer accumulated context, or different action choices.

## Call-ceiling implication

The 20-call ceiling was sufficient for all six completed baseline trajectories, but `dev-b0-05` used 19 successful calls and therefore left only one call of margin.

This makes it unsafe to freeze a held-out call budget solely by taking a central tendency from the first few runs. The cross-run analysis must distinguish a fair common ceiling from unnecessary overprovisioning while preserving parity across B0, B1, and P0.

## What is already known semantically

The first fully reviewed matched pair, `dev-b0-03` versus `dev-b1-01`, showed:

```text
both conditions were strong on critical-integrity mechanics
B1 explicitly diagnosed inherited learned-preprocessing contamination
B1 made the customer-month observation unit explicit
B1 gave more explicit deployment/generalization-regime reasoning
B1 added known-versus-new customer subgroup analysis
both conditions repaired the Phase 2 feature-timing correction strongly
both conditions protected the final test
both conditions introduced row-level bootstrap uncertainty that ignored repeated-customer dependence
```

These findings remain development evidence only. The remaining four raw trajectories must now be inspected to determine which differences are stable and which were stochastic.

## Required cross-run analysis

The next analysis should reconstruct all six behavior-evaluable baseline trajectories and compare, condition-neutrally:

```text
row-unit correction
inherited preprocessing contamination diagnosis
validation/generalization-regime reasoning
prediction-time feature-eligibility reasoning
Phase 2 repair completeness and precision
final-test discipline
claim scope and limitations
optional methodological errors
action selection and redundant work
Python/tool usage
input/output/reasoning token distributions
run-to-run variability
provider-normalization events
```

Raw artifacts for `dev-b0-03` and `dev-b1-01` have already been reviewed. The remaining raw artifacts needed are from:

```text
dev-b0-04
dev-b0-05
dev-b1-02
dev-b1-03
```

## Experimental boundary

Do not run more B0/B1 development replicates unless the cross-run analysis reveals that one of the six completed trajectories is behavior-ineligible or otherwise unusable for a condition-neutral reason.

Do not implement P0 yet.

The correct sequence is now:

```text
1. inspect all remaining raw baseline trajectories
2. perform full six-run cross-run comparison
3. freeze semantic-evaluation rules and common held-out resource protocol
4. implement P0 against that independently fixed baseline boundary
```

This preserves the falsification design by preventing P0 from influencing the interface, evaluator rules, or resource envelope it will later be tested against.
