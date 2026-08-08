# Current State

## Checkpoint

**Checkpoint:** 11  
**Date:** 2026-08-08  
**Development stage:** Controlled prototype specification complete; benchmark-first implementation is next  
**Implementation status:** Not started

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, analytical depth, speed, or low cost remain project-dependent objectives rather than universal goals.

## Current project constitution

The conceptual hierarchy remains:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

The five candidate epistemic invariants remain:

1. semantic validity;
2. information legitimacy;
3. evidence validity;
4. claim validity;
5. traceability and dependency integrity.

These remain strong design hypotheses under empirical validation.

## Foundations established before implementation

The project has developed architecture-neutral theories for:

```text
Checkpoint 4  dependency-aware project state and state-driven orchestration
Checkpoint 5  progressive project initialization and universal bootstrap
Checkpoint 6  knowledge activation and open-world reasoning
Checkpoint 7  reusable knowledge packages and typed components
Checkpoint 8  knowledge quality, generalization, and evolution
Checkpoint 9  behavioral reasoning regression and system evaluation
Checkpoint 10 minimum falsification prototype and experimental contract
Checkpoint 11 concrete Prototype V0 technical specification
```

Detailed reasoning lives in `docs/foundations/004_...` through `docs/foundations/011_...`.

## Checkpoint 10 experimental question

The first implementation is a falsification experiment rather than a production system.

The central question is:

> **Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than equally capable simpler workflows?**

The three conditions are:

```text
B0
Strong generic LLM workflow.

B1
Same model and tools plus the same small methodological knowledge set
supplied statically in the prompt.

P0
Same model and tools plus minimal typed project state, structured knowledge,
activation/applicability, prospective safeguards, dependency-aware reopening,
and minimal state-derived action selection.
```

B1 is the most important control. If static guidance matches P0 at materially lower complexity or cost, the explicit semantic runtime is not justified for this project scale.

## Checkpoint 11 technical specification

Foundation 011 makes the experiment implementable while deliberately avoiding production architecture.

Detailed specification:

`docs/foundations/011_prototype_v0_technical_specification.md`

Historical snapshot:

`docs/checkpoints/011_prototype_v0_technical_specification.md`

## Benchmark world

The first case is a synthetic customer-month churn project.

Fixed conceptual structure:

```text
24 monthly periods
approximately 4,000 underlying customers
train: months 1-16
validation: months 17-20
test: months 21-24
prediction moment: beginning of month
target: churn during the following 30 days
```

Customers enter over time and remain observable until churn, creating repeated customer snapshots plus newly entering customers in validation and test.

The actual row unit is customer-month, while a stale README incorrectly says one row is one customer.

## Synthetic DGP

The DGP is now concretely specified.

Persistent customer heterogeneity is represented by a random effect `u_i ~ N(0, 0.65^2)`.

Visible legitimate features include:

```text
customer_id
snapshot_month
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

The target is generated through a logistic hazard using these features, customer heterogeneity, plan effects, and mild time evolution. The current intercept and coefficients are intended to produce roughly 10 percent monthly churn prevalence with meaningful but nontrivial predictive signal.

Exact Version 0 equations and parameters are recorded in Foundation 011.

## Dynamic feature-legitimacy event

`account_state_code` is generated after observing the churn outcome, with opaque values `S1`, `S2`, and `S3`.

Its relationship with churn is deliberately useful but imperfect so illegitimacy must be established through timing/provenance rather than a perfect target proxy.

The stale README incorrectly describes the field as available during monthly scoring.

After the system reaches a provisional Phase 1 position, the harness reveals an authoritative timing notice establishing that the field is created after the outcome window and retrospectively backfilled.

The system must then revise feature eligibility and repair materially dependent reasoning without discarding unrelated valid work.

## Inherited preprocessing contamination

`baseline_model.py` deliberately fits learned preprocessing using combined train and validation information before evaluating on validation.

This tests the `Learned Transformation Evaluation Boundary` knowledge component.

Version 0 does not attempt arbitrary static program analysis. The LLM inspects the simple baseline code and applies the explicit reusable invariant.

## Information boundary and instrumented workspace

Visible project material and evaluator-only truth must be operationally separated.

All three experimental conditions use the same instrumented project-access interface.

Important distinctions are:

```text
metadata-level artifact access
value-level artifact access
explicitly declared Python input artifacts
condition-neutral action and artifact-access logging
```

Evaluator-only files must never become ordinary runtime-visible project artifacts.

## Project phases

Version 0 uses only:

```text
PHASE 1: provisional development
PHASE 2: revised development after authoritative timing notice
FINAL EVALUATION: after explicit final-model lock
```

The dynamic notice is milestone-triggered rather than released after an arbitrary fixed number of LLM calls.

Value-level final-test access is methodologically legitimate only after explicit final-model lock.

## First deterministic prospective safeguard

The first genuinely enforced P0 action gate is `K-INFO-001 Protected Final Evaluation`.

During development:

```text
protected final-test role
+ proposed value-level access
-> block
```

B0 and B1 use the same workspace interface but do not receive this enforcement layer. Invalid accesses are logged and executed so the evaluator can observe whether they voluntarily respect the same rule.

## Minimal P0 state

Version 0 keeps:

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

with only:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Typed status vocabularies are used rather than one universal state enum.

A simple append-only audit history preserves state changes and reasons without selecting event-sourcing architecture.

## Dependency repair

Version 0 explicitly rejects blind recursive invalidation.

Current repair semantics are:

```text
hard dependency becomes invalid
-> reopen or invalidate dependent state

support becomes invalid
-> remove that support
-> reassess whether remaining support is sufficient
```

Dependency discovery can be deterministic while materiality/sufficiency reassessment remains interpretive.

The evaluator should distinguish under-propagation, correct propagation, and over-propagation.

## Minimal knowledge set

P0 contains only:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001  Generalization-Regime Question
```

B1 receives the same substantive knowledge upfront in static prose.

No embeddings, vector database, graph database, large knowledge library, or automatic knowledge learning are required.

## Evaluation

Primary scoring should rely on condition-neutral observable behavior wherever possible rather than awarding P0 points for possessing structured internal state.

Deterministic assertions should cover at least:

```text
premature final-test value access
post-test development changes
final use of account_state_code after the timing notice
required legitimate re-evaluation after material feature invalidation
benchmark self-test validity
```

Blinded semantic evaluation remains necessary for:

```text
row-unit correction
validation/generalization reasoning
handling of inherited preprocessing contamination
response to the timing notice
repair completeness and precision
claim validity
```

Critical semantic criteria should initially use at least two independent judge passes, with calibration-time adjudication for disagreement.

## Resource accounting

Every condition logs:

```text
LLM calls
input/output tokens
Python executions
tool operations
runtime
artifact accesses
```

P0 additionally logs architecture diagnostics such as state updates, activations, blocks, and reopen events.

A common held-out resource envelope and continuation thresholds must be frozen after calibration and before held-out evaluation.

## Case validation and held-out variants

The case generator must automatically produce visible artifacts and hidden evaluator truth from one underlying case specification.

Before any LLM run, deterministic benchmark self-tests verify row uniqueness semantics, temporal partitioning, later-entry customers, post-outcome feature generation, documentation contradictions, timing-notice correctness, baseline contamination, final-test role, prevalence, and predictive-signal sanity.

The development case is followed by held-out H1/H2 surface variants with changed names, wording, seeds, and nonessential DGP details while preserving underlying mechanisms.

## Prototype repository boundary

A provisional `prototype_v0/` area is now justified.

It may contain:

```text
README.md
case_spec/
src/
tests/
configs/
results/
```

This is explicitly an experiment boundary rather than a commitment to the eventual production repository architecture.

## Explicit non-decisions

The project still has not selected a production agent architecture, permanent state database, graph technology, vector retrieval system, workflow framework, provider strategy, automatic knowledge-learning mechanism, full admissibility engine, full risk/assurance implementation, deployment architecture, UI, or monitoring stack.

Prototype conveniences such as plain Python records, JSON, simple audit logs, and local configuration files must not be interpreted as final architectural choices.

## Implementation order

The benchmark must be implemented before P0 is tuned:

```text
1. synthetic DGP
2. visible artifact generation
3. hidden evaluator manifest
4. Phase 2 notice
5. benchmark self-tests
6. instrumented workspace and trace
7. deterministic evaluator
8. B0
9. B1
10. P0 state / knowledge / gate / repair
11. experiment runner
12. semantic evaluator
13. calibration
14. freeze held-out protocol
15. held-out H1/H2
```

## Current focus

Broad conceptual design should now stop expanding unless implementation exposes a concrete gap.

The immediate task is:

> **Implement the benchmark generator, visible case artifacts, hidden evaluator manifest, Phase 2 notice, and benchmark self-tests before implementing P0.**

This is the first real construction milestone.

## Required context for a new chat

A new implementation chat should read, at minimum:

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/VISION.md`
4. `docs/PRINCIPLES.md`
5. `docs/DECISIONS.md`
6. `docs/OPEN_QUESTIONS.md`
7. `docs/DEVELOPMENT_METHOD.md`
8. `docs/CONTINUITY.md`
9. `docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md`
10. `docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`
11. `docs/foundations/011_prototype_v0_technical_specification.md`

Deeper foundations should be consulted only when implementation questions require their rationale.

## Next step

Begin benchmark-first implementation with the deterministic synthetic DGP and case self-tests.