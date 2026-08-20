# Checkpoint 011: Prototype V0 Technical Specification

**Date:** 2026-08-08  
**Status:** Historical infrastructure record  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Controlled prototype specification complete  
**Scope:** Records the historical milestone described by this checkpoint: Prototype V0 Technical Specification.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Ready to begin benchmark-first implementation

## Why this checkpoint exists

Checkpoint 10 defined the minimum falsification experiment for the Autonomous Data Science System. Checkpoint 11 translates that experiment into a concrete technical specification that can now be implemented without choosing a production architecture.

The next useful evidence should come from code and benchmark behavior rather than further broad conceptual design.

## Experimental target

The prototype tests whether the same strong LLM becomes materially more reliable when supplied with:

```text
explicit typed project state
reusable knowledge activation
prospective methodological safeguards
dependency-aware repair
minimal state-driven action selection
```

compared with:

```text
B0: strong generic LLM workflow
B1: same LLM plus the same small knowledge set in static prompt form
```

B1 remains the most important control because it tests whether better prompting alone is sufficient.

## Common experiment harness

All conditions should use one benchmark harness responsible for:

```text
case generation
visible project workspace
hidden evaluator truth
dynamic Phase 2 revelation
instrumented artifact access
Python execution boundary
condition-neutral trace logging
resource accounting
evaluation
```

The benchmark world must be physically or operationally separated from evaluator-only truth.

## First synthetic case

The first project is a 24-month synthetic customer-month churn problem with approximately 4,000 underlying customers.

Partitions are:

```text
train:      months 1-16
validation: months 17-20
test:       months 21-24
```

Customers enter over time, so validation and test contain both previously observed and newly entering customers.

The row unit is actually customer-month, while a stale README incorrectly says one row is one customer.

Legitimate predictors include tenure, plan tier, monthly charge, support tickets, late payments, and usage change.

The target is next-30-day churn.

## Dynamic post-outcome feature

`account_state_code` is generated after the outcome with opaque categories `S1`, `S2`, and `S3`.

The initial README incorrectly describes it as a current scoring-time CRM field.

After Phase 1, an authoritative timing notice reveals that it is generated after the outcome window and retrospectively backfilled.

This creates the Version 0 belief-revision and dependency-repair event.

## Inherited baseline contamination

`baseline_model.py` deliberately fits learned preprocessing using concatenated train and validation information before evaluating validation performance.

The numerical effect need not be large. The benchmark tests whether the methodological information-boundary violation is recognized or avoided.

## Instrumented project access

All three conditions should use the same access interface.

Important concepts are:

```text
metadata-level artifact access
value-level artifact access
explicit declared inputs to Python execution
common action logging
```

P0 may prospectively block invalid actions. B0 and B1 do not receive that enforcement layer, allowing the evaluator to observe whether they voluntarily avoid the same failures.

## First deterministic prospective safeguard

The first enforceable P0 safeguard should be protected-final-evaluation access rather than arbitrary static analysis of preprocessing code.

During development:

```text
artifact role = protected final test
+ proposed value-level access
-> block
```

A safe alternative should direct the system toward validation or other legitimate development evidence.

## Minimal P0 state

Version 0 uses only:

```text
ARTIFACT
FACT
ASSUMPTION
QUESTION
EVIDENCE
CLAIM
DECISION
OBLIGATION
ACTION
```

and relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Typed status vocabularies are used rather than one universal status enum.

A simple append-only audit history records state transitions and their reasons without selecting event-sourcing architecture.

## Dependency repair

Invalidation should not blindly recurse through every downstream object.

Version 0 distinguishes:

```text
hard dependency loss
-> reopen/invalidate dependent state

support loss
-> remove invalid support
-> reassess whether remaining support is sufficient
```

Dependency discovery can be deterministic while materiality/sufficiency reassessment remains interpretive.

The evaluator must test under-propagation, correct propagation, and over-propagation.

## Minimal knowledge set

Version 0 keeps only:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001  Generalization-Regime Question
```

B1 receives all four upfront in ordinary prose.

P0 receives the same semantic content as structured knowledge with activation/applicability and enforcement where supported.

## Condition-neutral milestone reports

Every condition emits comparable reports at:

```text
PHASE_1_COMPLETE
FINAL_MODEL_LOCKED
FINAL REPORT
```

These reports allow evaluator comparison without awarding P0 points merely because it has richer internal state.

## Deterministic evaluation

Version 0 should directly detect at least:

```text
premature final-test value access
post-test development changes
final use of account_state_code after the authoritative notice
missing legitimate re-evaluation after a relied-upon invalid feature is removed
benchmark self-test failures
```

Semantic judging remains necessary for row-unit correction, validation rationale, inherited-contamination reasoning, repair quality, and claim validity.

## Semantic evaluator

Critical semantic criteria should initially receive at least two blinded judge passes.

Calibration disagreements should be adjudicated and used to clarify the evaluator before held-out rules are frozen.

A single opaque judge should not decide the experiment alone.

## Resource accounting

Common run logging includes:

```text
LLM calls
input/output tokens
Python executions
tool operations
runtime
artifact accesses
```

P0 additionally records diagnostic architecture overhead such as state updates, knowledge activations, blocked actions, and reopen events.

A common held-out budget envelope is frozen after calibration.

## Repository boundary

A provisional `prototype_v0/` area is now justified because implementation is no longer speculative.

It should contain only experiment-oriented assets such as:

```text
case specification
source code
tests
configuration
results / summaries
```

The layout is explicitly disposable and does not define the future production architecture.

## Implementation order

The benchmark must exist before P0 is tuned:

```text
DGP
-> visible artifacts
-> evaluator manifest
-> Phase 2 notice
-> benchmark self-tests
-> instrumented workspace / trace
-> deterministic evaluator
-> B0
-> B1
-> P0
-> paired experiment runner
-> semantic evaluator
-> calibration
-> freeze held-out protocol
-> held-out H1/H2
```

## Main design conclusion

The project has reached the point where additional broad abstraction is less valuable than implementation feedback.

The next code should be benchmark code, not agent code.

The first implementation milestone is:

```text
Generate one deterministic synthetic case
and prove mechanically that the visible artifacts,
hidden evaluator truth, dynamic notice, and self-tests
are internally consistent.
```

Detailed specification:

`docs/foundations/011_prototype_v0_technical_specification.md`
