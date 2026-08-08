# Foundation 009: Behavioral Reasoning Regression and System Evaluation

## Purpose

This foundation develops a conceptual evaluation framework for the Autonomous Data Science System.

The central problem is that the system is not a static predictor whose quality can be judged from one final label or metric. It is an adaptive data-science process operating under incomplete information, changing project state, methodological constraints, governance constraints, and project-specific objectives.

A useful evaluation framework must therefore test whether the system notices important concerns, avoids invalid actions, resolves blocking uncertainty, updates state correctly, repairs mistakes, limits claims appropriately, uses human attention selectively, and still produces useful project outcomes. It must do this without prescribing one exact workflow or model family.

The strongest current formulation is:

> **A behavioral reasoning regression case should define a partially observable project world together with an acceptance envelope over system behavior, not one expected sequence of analytical steps.**

The evaluator should specify what must be noticed or resolved, what must not happen, which claims require which evidence, which state changes should cause reopening or invalidation, and which alternative analytical paths remain defensible.

## 1. The evaluated object is a trajectory

The object of evaluation is not merely a final report or model.

Conceptually:

```text
initial project state
    -> observations
    -> questions
    -> actions
    -> evidence
    -> decisions
    -> state updates
    -> revisions
    -> final claims / deliverables
```

Two strong systems may take different trajectories and still be valid. Two systems may reach similar numerical results while only one used legitimate evidence.

Therefore exact workflow matching is generally inappropriate.

## 2. Visible state versus evaluator truth

A serious reasoning case should distinguish:

```text
SYSTEM-VISIBLE INFORMATION
What the system is legitimately able to know at a given moment.

EVALUATOR-ONLY WORLD STATE
What the benchmark designer knows about the underlying project mechanism.
```

This allows evaluation of whether the system:

- distinguishes facts from assumptions;
- notices when important information is missing;
- investigates instead of inventing semantics;
- revises beliefs when contradictory evidence appears;
- avoids using evaluator-only hindsight as if it had been available earlier.

Evaluation should ask what the system was entitled to believe at the time of a decision, not whether later omniscient hindsight would have preferred another decision.

## 3. Behavioral acceptance envelopes

A case should not normally say:

```text
step 1: EDA
step 2: median imputation
step 3: logistic regression
...
```

Instead it should express a behavioral envelope containing concepts such as:

```text
MANDATORY OBLIGATION
A concern that must be sufficiently resolved before a dependent milestone.

PROHIBITED BEHAVIOR
An action or claim that must not occur under the represented conditions.

ACCEPTABLE RESOLUTION SET
Several defensible ways of satisfying an obligation.

OPTIONAL QUALITY OPPORTUNITY
Potentially useful work that should not be converted into a universal requirement.
```

This preserves methodological flexibility while still making quality testable.

## 4. Dependency-aware evaluation

Evaluation should usually constrain milestone relationships rather than total action ordering.

For example:

```text
validation legitimacy resolved
    -> comparative performance can become accepted evidence
    -> model-selection decision may depend on that evidence
```

The evaluator need not require that validation analysis occur before all descriptive work.

A strong evaluation framework can therefore operate over typed project-state dependencies.

## 5. Hybrid evaluation

Some assertions are suitable for deterministic checks:

- protected test labels influenced development;
- learned preprocessing used evaluation observations;
- an action executed despite a blocking governance state;
- a decision still depends on invalidated evidence;
- a required dependency is absent;
- a reopened question remained incorrectly marked resolved.

Other judgments are semantic:

- whether prediction timing was understood correctly;
- whether a validation design reasonably represents deployment;
- whether causal language exceeds the evidence;
- whether human clarification was necessary;
- whether a claim was appropriately weakened.

The future evaluator should therefore probably combine deterministic assertions, semantic judgment, and empirical outcomes rather than rely on one judge type.

## 6. Evaluation hierarchy

The current direction is against one early scalar score that allows methodological violations to be compensated by predictive performance.

A conceptual hierarchy is:

```text
1. admissibility and critical epistemic-integrity failures
2. mandatory reasoning and repair obligations
3. evidence and claim quality
4. project effectiveness / deliverable utility
5. efficiency, optional depth, and human cost
```

This is not a final scoring system.

The important requirement is that invalid evidence should not become acceptable merely because it produced a better predictive metric.

## 7. Epistemic invariants as evaluation dimensions

The five candidate epistemic invariants provide a natural evaluation backbone:

```text
SEMANTIC VALIDITY
Did the analysis answer the intended question?

INFORMATION LEGITIMACY
Did illegitimate information influence reasoning, fitting, evaluation, or selection?

EVIDENCE VALIDITY
Were the analytical procedures appropriate and faithfully executed?

CLAIM VALIDITY
Did conclusions stay within the scope and strength supported by evidence?

TRACEABILITY / DEPENDENCY INTEGRITY
Can consequential beliefs and decisions be reconstructed and repaired when dependencies change?
```

Admissibility, risk-sensitive assurance, and project optimization add further dimensions.

## 8. Self-correction should be evaluated explicitly

The system should not be required to infer every project fact correctly immediately.

A stronger capability is:

```text
provisional belief
    -> contradictory evidence
    -> conflict recognized
    -> relevant question reopened
    -> dependent state reconsidered
    -> repair completed
```

Cases should deliberately contain misleading or stale source material so that self-correction is tested rather than hidden.

## 9. Dynamic cases

Static datasets are insufficient for the intended system.

Cases should eventually support state changes such as:

- new deployment information;
- changed feature availability;
- new policy or approval state;
- discovery of upstream leakage;
- invalidation of a prior assumption;
- new data versions;
- revised intended use.

The evaluator can then assess whether only affected conclusions are reopened and whether unaffected work is preserved.

This tests both under-propagation and over-propagation.

## 10. Failure injection and harmless suspicious patterns

A useful suite should contain hidden traps, but it should also contain suspicious-looking facts that are ultimately legitimate.

Otherwise the easiest strategy is excessive paranoia.

Examples of true failure mechanisms include post-outcome fields, future leakage, preprocessing contamination, protected-test reuse, misleading documentation, missing-prerequisite claims, or prohibited transfers.

Examples of harmless suspicious patterns include timestamps unrelated to prediction ordering, repeated entities that legitimately occur in deployment, very high predictive performance from genuine signal, or small immaterial missingness.

The evaluator should therefore test both concern coverage and applicability selectivity.

## 11. Evaluator truth should encode mechanisms

A benchmark should not merely contain labels such as:

```text
feature X = leakage
```

It should preserve why:

```text
feature X is created after the prediction moment
or
feature X uses observations after the forecast origin
or
feature X contains outcome-derived information
```

Mechanistic evaluator truth enables legitimate alternative repairs and prevents the benchmark from becoming a dogmatic action lookup table.

## 12. Human-interaction evaluation

Some semantic or normative questions require authoritative human input, while others can be resolved from existing sources.

Benchmark cases can conceptually include simulated human authorities with bounded knowledge and authority.

Evaluation should distinguish:

```text
required authoritative clarification
useful optional clarification
unnecessary interruption
missed necessary interruption
```

The objective is not minimum question count. It is high-value use of human attention.

## 13. Process quality and outcome quality

Process quality and final empirical performance should remain separate.

A slightly worse stochastic test metric may arise from a much stronger process. Conversely, an invalid process can produce a lucky result.

The evaluator should therefore distinguish:

```text
EX ANTE DECISION QUALITY
Was the decision defensible given the evidence available at that time?

EX POST OUTCOME QUALITY
How well did the resulting system perform when later outcomes were observed?
```

Neither should automatically replace the other.

## 14. Efficiency means justified effort

The relevant question is not how few experiments were run.

A system may fail through both over-investigation and under-investigation.

The stronger concept is whether analytical cost was connected to:

- unresolved questions;
- mandatory obligations;
- material uncertainty;
- risk reduction;
- deliverable needs;
- likely decision improvement.

Orphaned actions are therefore a promising efficiency signal.

## 15. Detection latency

Eventually noticing an issue is not equivalent to noticing it before dependent work accumulates.

Cases should measure when a material concern is detected relative to the first consequential action that depends on it.

Late detection can imply wasted computation, contaminated evidence, additional repair work, and unreliable intermediate conclusions.

## 16. Repair quality

The evaluator should inspect whether the system:

```text
recognized the failure
identified affected dependencies
reopened the right state
avoided discarding unaffected work
created legitimate repair actions
updated evidence roles
weakened or revised claims
preserved provenance
```

Long-running autonomous systems should be evaluated partly by recovery quality rather than assuming perfect initial behavior.

## 17. Correct abstention

Some cases should have no defensible strong answer.

Examples include unidentified causal effects, insufficient history for a requested forecast, unresolved binding admissibility, or unavailable evidence needed for a consequential conclusion.

Correct outcomes may include:

```text
restrict scope
weaken claim
request required authority
identify missing evidence
return no defensible answer
```

This operationalizes the existing idea: degrade scope, not integrity.

## 18. Evaluation scales

A future suite will likely need several scales:

```text
atomic knowledge-component case
package interaction case
state-transition / invalidation case
mini-project case
full-project case
adversarial or novel open-world case
```

The exact suite is open.

Lower-level cases aid diagnosis. Full projects test interaction and emergent process quality.

## 19. Hidden and parameterized cases

Public development cases alone are vulnerable to benchmark overfitting.

A mature evaluation program may need public regression cases plus held-out evaluator-only cases.

Parameterized scenario families may further reduce lexical memorization by varying field names, timings, missingness, entity regimes, documentation quality, and failure strength while preserving the same underlying mechanism.

## 20. Benchmark provenance

Evaluator expectations themselves should be challengeable and versioned.

For each mandatory behavior or prohibition, the benchmark should preserve why the expectation is justified and what mechanism it represents.

A reasoning benchmark that cannot justify its own expected behavior would reproduce the exact epistemic weaknesses the autonomous system is intended to avoid.

## 21. Baselines and ablations

The most important baseline is likely a strong contemporary LLM with repository access, code execution, and a broad instruction to complete the project thoroughly.

Other useful comparisons may include simpler structured checklists, human-guided LLM workflows, and ablations of the proposed architecture.

Potential ablations include removing:

```text
persistent structured state
prospective proposal validation
knowledge activation
coverage review
dependency invalidation
independent review
```

The purpose is to determine which complexity produces measurable process improvement.

## 22. Concrete mini-project stress test

The conceptual case structure was stress-tested on a deliberately difficult tabular churn project.

### Visible initial project

The project asks for a model that predicts whether an active customer will churn within 30 days so that a retention team can contact at most 500 customers each month.

Visible materials include:

```text
README
train.csv
validation.csv
test.csv
baseline notebook
feature documentation
```

The README states that one row represents one customer and identifies `test.csv` as final evaluation data.

The development data visibly contain fields such as:

```text
customer_id
snapshot_date
income
support_calls_90d
cancellation_reason
churn_30d
```

Initial structural inspection can discover repeated customer IDs, missing Income values, temporal coverage, class imbalance, and overlap among entity identifiers.

### Hidden evaluator world

The evaluator knows that:

```text
rows are monthly customer snapshots, not unique customers;

cancellation_reason is recorded only after a cancellation event;

the production score is generated at the beginning of each monthly outreach cycle;

future deployment contains mostly previously observed customers but also some newly observed customers;

Income can be missing during production scoring;

the existing baseline fitted learned preprocessing before a clean validation boundary;

test outcomes are intended to remain untouched until final evaluation.
```

The misleading README is intentionally stale.

### Mandatory behavioral obligations

The system should eventually resolve the row-unit contradiction, establish the prediction moment, determine feature availability at that moment, resolve the temporal/entity validation regime relative to deployment, protect final-test outcome information, handle production-relevant missingness under legitimate validation, and connect evaluation/decision policy to the monthly outreach capacity.

The system need not resolve these in one predefined order.

### Important prohibitions

The system should not treat the stale README as unquestioned truth after direct structural contradiction appears. It should not retain the post-outcome cancellation feature once timing is established. It should not use protected test outcomes for iterative development. It should not accept evaluation evidence contaminated by learned preprocessing fitted across illegitimate partitions. It should not infer that class imbalance itself mandates a particular resampling method.

### Acceptable validation envelope

Because deployment includes future observations from both known and new customers, several validation approaches can be defensible.

A temporal forward evaluation that naturally preserves the deployment mix may be acceptable. A grouped-temporal approach with separate known/new-entity reporting may also be acceptable. Another approach may be accepted if it clearly justifies how it estimates the deployment quantity.

An all-unseen-entity GroupKFold is not automatically required merely because IDs repeat.

This tests the distinction between activation and applicability.

### Missing-data behavior

Income missingness should activate missing-data reasoning, but the system should not automatically choose one imputation strategy.

Once production missingness is established, evaluation should represent that intended-use condition and any learned imputation should respect training/evaluation information boundaries.

### Capacity and metric behavior

Because only 500 customers can be contacted each month, ordinary classification accuracy is not sufficient as the sole operational objective.

The system should reason about ranking or decision quality at the available intervention capacity, while remaining free to choose an appropriate project-specific metric or decision analysis.

The case does not prescribe one exact metric.

### Protected test behavior

The test set can expose only information legitimate for its role during development. The evaluator can deterministically check whether outcome information influenced feature engineering, model family choice, thresholds, or repeated tuning before final evaluation.

### Dynamic state change

After an initial model and missing-data strategy have been accepted, the case can introduce a revised deployment specification stating that missing Income is especially common among newly observed customers.

Expected behavior is not to restart the whole project. The system should reopen the affected missing-data and subgroup/generalization reasoning, reconsider whether previous validation evidence remains sufficient, and preserve unrelated valid work.

### Completion envelope

A defensible completion state requires that the critical semantic contradiction has been resolved, feature eligibility is legitimate, validation represents the intended deployment question sufficiently, protected test integrity is preserved, the selected preprocessing/model decision depends on valid evidence, operational decision behavior reflects outreach constraints, material residual uncertainty is stated, and no important final claim depends on known-invalid state.

The exact chosen model is intentionally not part of the required solution.

## 23. Stress-test result

The mini-project can be evaluated without prescribing one exact workflow.

The case structure successfully distinguishes:

```text
world truth from visible evidence
mandatory obligations from optional quality improvements
activation from applicability
valid alternative methods from invalid behavior
process quality from final predictive outcome
correct early uncertainty from later hindsight
self-correction from initial perfection
repair precision from blanket restart
```

This materially strengthens the behavioral-evaluation hypothesis.

## 24. Reasoning cases as partially observable state-transition environments

A useful abstract formulation is:

\[
\mathcal C = (\mathcal S, \mathcal O, \mathcal A, \mathcal T, \mathcal H, \mathcal E)
\]

where conceptually:

```text
S = underlying evaluator world state
O = observations legitimately visible to the system
A = possible system actions
T = project/world transitions and revelations
H = hidden evaluator mechanisms and facts
E = behavioral evaluation contracts
```

This is a conceptual framing, not an implementation choice.

## 25. Learning loop

Behavioral cases complete a three-way development loop:

```text
REAL PROJECT
    -> failure / lesson
    -> candidate reusable knowledge
    -> behavioral regression case
    -> knowledge or system revision
    -> future projects
```

Regression-case failures can themselves reveal missing knowledge, broken activation, poor state propagation, weak orchestration, or insufficient review.

Knowledge revisions can trigger reruns of the relevant regression suite.

This provides a plausible test-driven development methodology for autonomous data-science reasoning.

## Strong hypotheses after Checkpoint 9

The strongest current hypotheses are:

1. The evaluated object should be a behavioral project trajectory, not merely a final artifact.
2. Cases should separate visible project information from evaluator-only world truth.
3. Expected behavior should be represented as an acceptance envelope rather than one exact workflow.
4. Evaluation should be dependency- and milestone-aware rather than impose one total ordering.
5. Deterministic assertions, semantic evaluation, and empirical outcomes should be combined.
6. Critical methodological or admissibility violations should not be compensated by higher predictive performance.
7. Self-correction, invalidation, reopening, and repair precision should be tested directly.
8. Cases need both true failure mechanisms and harmless suspicious patterns to evaluate selectivity.
9. Human interruption should be evaluated for value and authority need, not minimized blindly.
10. Process quality, ex-ante decision quality, and ex-post outcome quality should remain distinguishable.
11. Correct abstention and scope restriction can be successful outcomes.
12. Behavioral cases should exist at multiple scales and eventually include held-out or parameterized variants.
13. Benchmark expectations themselves need provenance, challengeability, and versioning.
14. Strong simpler LLM workflows and architectural ablations should be meaningful baselines.
15. Behavioral regression cases can become the test-driven development substrate for both the knowledge library and the whole system.

## Important non-decisions

Checkpoint 9 does not select:

- an evaluation file format;
- a simulation framework;
- a judge model;
- a scalar score;
- a benchmark platform;
- a hidden-case hosting mechanism;
- exact severity weights;
- exact human-simulator implementation;
- exact project-state schema;
- exact baseline model/provider;
- an orchestration framework.

## Next conceptual bottleneck

The project now has substantial conceptual models for epistemic integrity, admissibility and assurance, project state, initialization, knowledge activation, reusable knowledge, knowledge evolution, and behavioral evaluation.

The next question is increasingly architectural:

> **What is the smallest end-to-end prototype that can falsify or validate these core hypotheses without prematurely committing to a full production architecture?**

The first prototype should be chosen to test the semantic loop, not to maximize feature completeness.