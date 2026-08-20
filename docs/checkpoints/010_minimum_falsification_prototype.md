# Checkpoint 010: Minimum Falsification Prototype

**Date:** 2026-08-08  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Transition from conceptual research to controlled prototype specification  
**Scope:** Records the historical milestone described by this checkpoint: Minimum Falsification Prototype.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Not started

## Why this checkpoint exists

Checkpoint 10 defines the first deliberately limited implementation experiment for the Autonomous Data Science System.

The project now has enough conceptual structure to test its core claims without building a production architecture.

The governing question is:

> **Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM materially more reliable across a changing data-science project than a simpler workflow using the same model and methodological knowledge?**

## Experimental treatment

Three conditions are proposed:

```text
B0
Strong generic LLM workflow.

B1
Same LLM plus the prototype's small knowledge set supplied
as static prompt guidance, but without structured state,
activation, action gates, or dependency repair.

P0
Same LLM plus the minimal semantic spine:
typed project state, tiny reusable knowledge set,
activation/applicability, prospective safeguards,
simple runnable frontier, and dependency-aware reopening.
```

B1 is especially important because it tests whether a static high-quality prompt is sufficient. If B1 matches P0 at lower cost, much of the stateful architecture may not be justified at this scale.

## Prototype case

The first case is a synthetic customer-month churn project.

Visible material includes:

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

The project asks the system to review an inherited baseline and produce a defensible model for predicting churn during the next 30 days while preserving the test set for final evaluation.

The case contains:

```text
repeated customers;
time-indexed snapshots;
a stale README claiming one row per customer;
a post-outcome account_state_code whose timing is initially
misdescribed by stale documentation;
an inherited baseline that fits a learned transformation
using validation information;
a protected final test set.
```

The temporal partitions are approximately:

```text
train: months 1-16
validation: months 17-20
test: months 21-24
```

Deployment contains future observations of both known and newly entering customers, so repeated IDs should trigger generalization reasoning but should not mechanically imply a pure unseen-entity split.

## Dynamic state-change event

After the system reaches a provisional model/validation milestone, the evaluator reveals an authoritative `crm_field_timing_notice.md` stating that `account_state_code` is populated only after the monthly outcome and retrospectively backfilled.

The feature is therefore not legitimate at the represented beginning-of-month prediction time.

This event is intended to test whether the system can:

```text
revise an earlier assumption;
identify dependent models/evidence/decisions/claims;
reopen only materially affected state;
repair the model/evaluation;
preserve unrelated valid work;
weaken or invalidate stale claims.
```

## Minimal project-state vocabulary

Version 0 currently requires only:

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

Candidate minimal relations are:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

This is deliberately smaller than the full candidate state ontology.

## Minimal reusable knowledge

The first prototype should contain only four manually authored components:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001  Generalization-Regime Question
```

These components provide both hard safeguards and interpretive reasoning without requiring a large knowledge library or retrieval system.

## Evaluated behavior

The acceptance envelope should test whether the system:

```text
detects the row-semantics contradiction;
uses a deployment-relevant validation rationale;
detects inherited preprocessing contamination;
protects final-test outcomes during development;
reacts correctly to the feature-timing revelation;
repairs all materially affected dependencies;
preserves unrelated valid work;
keeps final claims within current valid evidence;
avoids unnecessary or premature work.
```

The evaluator should allow multiple valid model families and validation implementations.

Critical integrity failures should not be compensated by marginally better predictive performance.

## Development and held-out variants

The development case can be used for implementation debugging.

Two held-out surface variants should preserve the same underlying mechanisms while changing names, wording, random seeds, and some nonessential DGP details.

Examples include:

```text
customer_id        -> member_key / account_ref
snapshot_month     -> scoring_period / observation_period
account_state_code -> lifecycle_flag / profile_code
```

This is intended to reduce lexical benchmark overfitting.

A reasonable first run plan is:

```text
Calibration:
3 runs per condition on the development case.

Held-out:
5 paired runs per condition on H1.
5 paired runs per condition on H2.
```

Calibration is for debugging, budget setting, and evaluator clarification. Quantitative continuation thresholds must be frozen before held-out evaluation.

## Falsification logic

The prototype is explicitly allowed to fail as an architectural hypothesis.

Strong evidence against P0 would be obtained if B1 matches P0 across critical integrity behavior, repair completeness, repair precision, and held-out variants while using materially less reasoning/state-management cost.

Architecture-induced false blockers, duplicate obligations, unnecessary reopening, or case-specific hard-coded rules also count against P0.

Higher predictive performance alone is not evidence for the architecture.

The strongest continuation signal would be a repeated held-out pattern where P0 prevents or repairs critical methodological failures more reliably than B1 without unacceptable cost or false blocking.

## Explicitly deferred

Version 0 does not require:

```text
multi-agent architecture;
provider routing;
vector or graph databases;
large knowledge retrieval;
automatic knowledge evolution;
full admissibility/risk/assurance implementation;
external research;
production deployment;
monitoring;
workflow engines;
UI.
```

## Development-stage transition

Checkpoint 10 marks an important but limited phase transition.

The project is no longer blocked on broad conceptual exploration before any code can exist. It now has a concrete falsification experiment that can justify a first prototype.

This does **not** mean the conceptual architecture is accepted as correct. Prototype V0 exists precisely to challenge it.

Detailed reasoning is preserved in:

`docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`

## Next step

Specify the implementation contract for Prototype V0 and then build the benchmark/evaluator before building the autonomous treatment.

The next implementation-focused questions include:

```text
exact synthetic case generator;
exact visible file contents;
minimal state serialization;
status vocabulary;
relation representation;
action proposal/gate interface;
baseline harness;
P0 control loop;
evaluator assertions and run logs;
resource instrumentation;
repository structure for prototype code and cases.
```

The benchmark world and evaluator should be implemented before tuning P0 behavior so that the prototype is not evaluated against a benchmark designed retrospectively around its own outputs.
