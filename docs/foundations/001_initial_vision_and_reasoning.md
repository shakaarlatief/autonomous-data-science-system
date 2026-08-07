# Foundation 001: Initial Vision and Reasoning

**Date:** 2026-08-07  
**Status:** Foundational design memo  
**Purpose:** Preserve the detailed reasoning behind the initial conception of the Autonomous Data Science System.

## 1. Origin of the idea

The project began from a simple but important observation.

A modern large language model can already perform much of a data science project from beginning to end. Given a dataset, target, and broad objective, an LLM can inspect the data, perform exploratory analysis, write preprocessing code, choose baselines, select model families, validate and compare models, evaluate results, generate predictions, and write reports.

This creates the possibility of asking one model to complete an entire project in one long workflow.

However, capability is not the same as process quality.

If a single LLM is given the broad instruction to complete a project from A to Z, many parts can go well while other parts remain weaker than they should be. The model may make a decision too quickly, interpret a pattern incorrectly, choose one reasonable preprocessing strategy without exploring alternatives, use a validation scheme that is not ideal for the deployment setting, fail to recognize a project-specific issue, or settle a question by plausible explanation rather than evidence.

The problem is not necessarily that every such decision is obviously wrong. Many decisions are context-dependent. A choice can be technically valid and still be suboptimal because another path would have been more appropriate for the specific project.

This led to the central idea: instead of treating one LLM as the data scientist, build a larger system that manages the data science process itself.

## 2. From one-dimensional assistance to an organized scientific process

The conventional LLM-assisted workflow can be represented roughly as:

```text
project request
    -> one model or one conversation
    -> EDA
    -> preprocessing
    -> models
    -> evaluation
    -> final output
```

The proposed direction is different:

```text
project
    -> structured understanding
    -> questions and hypotheses
    -> targeted investigations
    -> executable experiments
    -> evidence
    -> independent criticism where useful
    -> explicit decisions
    -> human involvement where needed
    -> updated project state
    -> further investigations
```

The important change is not merely that more LLMs are involved. The change is that the project becomes an explicit process with roles, state, evidence, review, and decision protocols.

A weak multi-agent system could ask five agents for opinions and then ask a sixth to summarize them. That might create more text without creating more reliability.

The system should instead be designed so that different components have clear responsibilities and can challenge one another through evidence.

## 3. Specialized responsibilities

One early conceptual sketch separated responsibilities such as:

```text
                         HUMAN
                           |
                           v
                    ORCHESTRATOR
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
   Problem Analyst     Data Analyst     Research Role
          |                |                |
          +----------------+----------------+
                           |
                           v
                    Experiment Planner
                           |
                           v
                     Coding / Execution
                           |
                           v
                       Evidence
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
 Statistical Review   ML Review      Leakage Review
          |                |                |
          +----------------+----------------+
                           |
                           v
                    Decision Synthesis
                           |
                    continue / ask human
```

This diagram was never intended as a final agent architecture. Its value was conceptual: important responsibilities can be separated so that the component proposing an action is not automatically the same component validating it.

The eventual implementation might use permanent agents, temporary roles, deterministic checks, or one model taking different roles at different times. The underlying principle is more important than the number of processes.

## 4. Start with questions, not only stages

A major insight was that the system should reason in terms of questions and evidence, not merely progress through project stages.

Consider preprocessing. A shallow workflow may detect missing values and immediately choose median imputation for numerical features and mode imputation for categorical features.

A stronger process asks questions first:

```text
Why are values missing?
Will missingness also occur in production?
Is missingness informative?
Does missingness differ across important groups?
Would deleting incomplete rows change the sample distribution?
Which variables are affected?
Can a model handle missing values directly?
Does the choice need to happen inside cross-validation?
Would a missingness indicator help?
Are several approaches close enough that simplicity should decide?
```

The project stage "preprocessing" is therefore not a single action. It is a collection of conditional scientific questions.

This principle generalizes far beyond missingness.

## 5. Disagreement should produce tests when possible

One of the most important early examples concerned feature removal.

Suppose one reasoning component says:

```text
Remove TotalCharges because it is highly correlated with tenure.
```

A reviewer may respond:

```text
High correlation between predictors is not, by itself, a sufficient
reason to remove a feature in a predictive modelling problem.
```

A weak system might ask another LLM which argument sounds better.

A stronger system asks whether the question can be tested.

For example:

```text
Model with feature:
CV score = ...

Model without feature:
CV score = ...
```

The final decision can then incorporate empirical evidence, uncertainty, model type, interpretability, and deployment cost.

The principle is that LLM reasoning should often propose and critique hypotheses, while executable experiments resolve empirical questions where possible.

## 6. Human decision gates

The system should not interpret autonomy as removing the human from every decision.

Some questions are fundamentally about project intent or semantics rather than statistical optimization.

For example:

```text
Should churn mean:
A. customer churns within the next 30 days
B. customer eventually churns
```

That decision changes target construction, prediction timing, leakage definitions, validation, and practical meaning.

If the project objective is genuinely ambiguous, the system should not silently choose one interpretation simply because it can continue faster.

This suggests explicit human gates for consequential ambiguity.

Other examples may include:

- what information is truly available at prediction time;
- what false-negative cost matters operationally;
- whether a feature is ethically or legally acceptable;
- whether interpretability is more important than a small predictive gain;
- whether a project is exploratory or production-oriented;
- or whether an unresolved uncertainty is acceptable.

The intended goal is not "remove the human."

It is closer to:

> **Use the human only where human judgment creates meaningful value.**

## 7. Configurable project depth

Not every project deserves the same amount of work.

An exploratory prototype and a production-critical scientific analysis should not execute identical processes.

An early idea was to support modes such as:

```text
QUICK
- basic audit
- a few baselines
- limited validation
- short report

STANDARD
- thorough EDA
- multiple preprocessing alternatives
- several model families
- robust validation
- full report

RESEARCH
- broad hypotheses
- ablation studies
- robustness checks
- statistical comparisons
- calibration
- subgroup analysis
- independent review
- detailed technical report
```

The exact mode system is not decided. Another possibility is explicit budgets:

```text
maximum compute time
maximum model fits
prioritize interpretability
ask before feature removal
broad model exploration allowed
```

The deeper principle is that the system should allocate effort intelligently rather than assuming that sophistication means running everything.

## 8. Persistent project state

A long project should not depend on conversational memory.

An early imagined project state looked like:

```text
PROJECT STATE

Objective
---------
Predict customer churn.

Current data version
--------------------
v1.3

Decisions
---------
D001: Use stratified validation.
Reason: binary target with class imbalance.

D002: Do not remove TotalCharges.
Evidence: ablation reduced validation performance.

Rejected ideas
--------------
R001: SMOTE before splitting.
Reason: leakage.

Outstanding questions
---------------------
Q004: What false-negative cost should be assumed?

Experiments
-----------
EXP_001 logistic regression baseline
EXP_002 random forest
EXP_003 gradient boosting
```

This was not intended as the final schema. It illustrated a broader requirement: the system should have institutional memory for the project.

Every reasoning component should be able to know what has already been tried, why decisions were made, which assumptions remain uncertain, and which experiments have been invalidated.

## 9. Reporting as a product of the reasoning process

A common workflow completes the analysis first and then asks an LLM to "write the report."

That approach risks reconstructing reasoning after the fact.

A stronger system would create structured artifacts throughout the project:

```text
problem_definition
validation_strategy
data_audit
missingness_analysis
feature_engineering_log
experiment_registry
model_comparison
error_analysis
final_model_card
technical_report
executive_summary
```

The specific filenames are not important. The key idea is that the report should be assembled from evidence and decisions already documented during the analysis.

This improves reproducibility and reduces the chance that the narrative becomes disconnected from the actual process.

## 10. The system must be able to go backward

Data science is iterative.

Suppose evaluation reveals:

```text
Performance collapses for customers with tenure below three months.
```

That finding may require returning to EDA and investigating new customers as a separate population.

The result might reveal a new feature, a data collection issue, or a different deployment condition.

The system may then need to revisit feature engineering, model selection, or validation.

Therefore, a workflow like:

```text
understand -> EDA -> preprocess -> model -> evaluate -> finish
```

is too restrictive.

A better process permits:

```text
evaluate
   -> detect problem
   -> return to EDA
   -> form new hypothesis
   -> engineer or audit data
   -> rerun experiment
   -> reevaluate
```

Later evidence should be able to invalidate earlier work.

## 11. Independent replication

Another early idea was independent replication for important findings.

Suppose one analysis reports a large improvement from a random forest.

A second analysis receives the dataset and experiment definition but not the original conclusion.

If the second analysis finds a much smaller improvement, the disagreement becomes informative.

Perhaps the first analysis accidentally fitted preprocessing before cross-validation, creating leakage.

A strong system could then record:

```text
Disagreement detected.

Original experiment invalidated.
Reason: preprocessing leaked information across folds.

Corrected experiment accepted.
```

This illustrates how independent analysis can uncover methodological errors that a purely conversational review may miss.

Independent replication should not necessarily be used for every result because it costs time and compute. The system needs a risk-sensitive way to decide when it is worthwhile.

## 12. Separate proposing from approving

A related idea is proposer-reviewer separation.

Example:

```text
Proposer:
Recommend log-transforming income because the distribution is right-skewed.

Reviewer:
Skewness alone is not sufficient evidence that this transformation helps all model families.

Experiment:
Compare raw, log, and Yeo-Johnson representations across relevant models.

Result:
Transformation helps logistic regression and kNN, but has little effect on tree ensembles.

Decision:
Use the transformation only in pipelines where it improves validation performance or is otherwise justified.
```

The point is not that every transformation needs a committee.

The point is that consequential reasoning should be open to criticism, and criticism should often lead to tests rather than endless debate.

## 13. The deeper problem: project diversity

The next major insight was that different data science projects require fundamentally different reasoning paths.

A tabular IID classification problem, a time-series forecast, a grouped medical dataset, a recommender system, and a causal study do not merely use different models. They require different questions about data structure, splitting, assumptions, interpretation, evaluation, and deployment.

This makes a single global decision tree impractical.

However, allowing an LLM to improvise every decision from scratch also seems too fragile.

This created the central architecture problem:

> **How can the system represent an enormous space of possible data science decisions without either hard-coding an impossible giant workflow or allowing unrestricted improvisation?**

## 14. Missing data as a miniature prototype

An existing `Missing_Data.md` decision tree became a useful example.

Missing data appears to be a small preprocessing topic, yet even it contains many branches:

- Are feature values missing or target labels missing?
- Is the feature worth keeping?
- Will missing feature values occur in production?
- Can clean validation and test data be obtained?
- Is row deletion being considered?
- Is missingness roughly uniform or systematic?
- Is the feature numerical or categorical?
- Should the strategy use mean, median, mode, a missing category, predictive imputation, a missingness indicator, or a model that handles missing values directly?
- If target labels are missing, is supervised training on labeled cases adequate or is semi-supervised learning relevant?
- If test labels are missing, how should uncertainty in evaluation be reported?

The tree demonstrates that even simple topics can have many conditional lines.

It also demonstrates the value of explicit knowledge: a future system should not need to rediscover every missing-data consideration from scratch in every project.

## 15. From giant workflow to reusable decision modules

This led to the idea of **decision modules** or **knowledge modules**.

Instead of one enormous workflow, the system might maintain reusable units such as:

```text
Missing Data
Class Imbalance
Outliers
Feature Scaling
Categorical Encoding
High Cardinality
Leakage
Duplicates
Target Definition
Train/Test Splitting
Temporal Structure
Grouped Observations
Feature Transformations
Feature Selection
Metric Selection
Threshold Selection
Calibration
Model Family Selection
Hyperparameter Search
Residual Diagnostics
Error Analysis
Interpretability
Robustness
```

A module could contain concepts such as:

```text
activation conditions
inputs
questions
rationale
required evidence
possible actions
human gates
common mistakes
dependencies
outputs
```

For missing data, a conceptual module might ask whether missingness exists, whether it is expected in production, whether deletion changes the sample distribution, and which imputation approaches are worth testing.

The exact module format remains undecided. The importance of the idea is modularity and conditional activation.

## 16. Adaptive activation

If the system eventually contains hundreds of modules, running all of them on every project would be inefficient and often nonsensical.

Instead, an early proposed cycle was:

```text
OBSERVATION
    -> FACT
    -> TRIGGER
    -> MODULE
    -> INVESTIGATION
    -> EVIDENCE
    -> DECISION
    -> NEW FACTS
    -> NEW TRIGGERS
```

Example:

```text
Observation: customer_id appears multiple times.
Fact: repeated entities exist.
Trigger: grouped-data concerns.
Investigations:
- group leakage
- group-aware splitting
- within-entity temporal ordering
```

This means the project constructs its own reasoning graph as it proceeds.

The system begins with broad characterization, activates only relevant reasoning, and can activate new branches later as new facts are discovered.

## 17. Three forms of knowledge

The discussion then distinguished three broad categories.

### Hard rules

Some constraints should not be creatively re-decided in every project once their conditions are known.

Examples include preventing test information from entering training preprocessing, avoiding final-test hyperparameter tuning, and preserving temporal direction where future information would otherwise leak backward.

### Decision frameworks

Some situations have known considerations but no universal answer.

Missing-data handling is the canonical early example.

The system can encode the questions to ask and strategies to consider without pretending that one strategy always wins.

### Open-ended reasoning

Some issues cannot realistically be exhaustively represented.

Examples include understanding why one customer segment behaves unexpectedly, whether a strange feature reflects a business process, whether an external event explains drift, or whether a domain-specific pattern has been misunderstood.

These require LLM reasoning, research, experimentation, and human judgment.

The combination appears more promising than either a fully fixed or fully generative architecture.

## 18. Real projects as coverage tests

Trying to write the complete data science decision universe before running the system would likely fail.

A better development strategy is to test increasingly diverse projects.

Examples might include:

```text
Project A: ordinary tabular binary classification
Project B: regression
Project C: energy forecasting
Project D: severe class imbalance
Project E: grouped or panel data
Project F: NLP
Project G: recommendation
```

Each project tests the system itself:

```text
Did it identify the relevant issue?
Did it activate the correct investigation?
Did it miss an important branch?
Did it ask the human when necessary?
Did it waste effort on irrelevant work?
Did it accept a conclusion without enough evidence?
Did interacting issues expose a missing dependency?
```

The system grows through real coverage rather than speculative completeness.

## 19. Generalize every useful failure

A project should not merely be fixed locally when the system fails.

Suppose a medical dataset has blood pressure missing mostly for one hospital and the system performs simple median imputation without investigating the collection process.

After discovering the weakness, the lesson might become:

```text
When missing feature values exist, test whether missingness differs
across important groups or data sources.
```

That lesson becomes reusable.

Another project may teach a grouped-validation rule. Another may reveal a calibration issue. Another may expose rare category handling. Another may reveal structural breaks in forecasting.

Over time, each project contributes to a growing representation of good data science practice.

## 20. Modules can interact

The system should not assume that reasoning modules are independent.

For example:

```text
Missing values
    -> row deletion proposed
    -> activate selection-bias investigation
```

or:

```text
Class imbalance
    -> probabilities needed
    -> operational threshold matters
    -> activate PR metrics
    -> activate calibration
    -> activate threshold analysis
    -> activate cost-sensitive evaluation
```

or:

```text
Timestamp detected
    -> temporal dependence plausible
    -> temporal validation
    -> drift analysis
    -> autocorrelation checks
    -> forecasting branch where relevant
```

This strengthens the case for a graph-like reasoning model, while also creating a future engineering challenge: how to keep dependencies understandable and efficient.

## 21. Efficiency through selective depth

The system may eventually contain a very large universe of possible reasoning modules.

The goal is not:

```text
500 possible modules -> execute all 500
```

A more intelligent process might look conceptually like:

```text
available modules: 500
initial characterization activates: 35
cheap screening eliminates: 20
deeper investigation needed: 8
experiments worth running: 5
human decisions needed: 2
```

The numbers are illustrative.

The principle is that sophistication should come from selecting the right work, not from brute-force completeness.

## 22. Different depth inside the same module

A missing-data module may itself support different depths.

A quick project might perform:

```text
missing percentage
missing columns
basic production check
simple imputation baseline
```

A deep project might perform:

```text
conditional missingness
subgroup missingness
association with target
collection-process analysis
multiple imputation candidates
missingness indicators
ablation studies
sensitivity analysis
```

Therefore, project depth need not require completely different systems. The same reasoning architecture can expand or contract according to budget and risk.

## 23. The system should be allowed to remain uncertain

Not every analysis should end in a confident binary decision.

A mature conclusion might be:

```text
Median and model-based imputation perform similarly.
The difference is smaller than validation uncertainty.
Prefer median imputation because it is simpler.
Confidence: moderate.
```

Another might be:

```text
Two validation schemes remain plausible because intended deployment
has not been clarified.
Human input required.
```

The system should track uncertainty rather than hiding it behind polished language.

## 24. The long-term asset is explicit data science reasoning

One of the strongest conclusions from the discussion is that the durable asset may not be the orchestration software itself.

LLMs will change. Agent frameworks will change. Tooling will change.

The deeper asset could be an explicit representation of:

```text
what questions matter
when they matter
what evidence is required
which alternatives should be considered
which mistakes should be prevented
what should trigger another investigation
when conclusions are uncertain
when a human should decide
```

If that knowledge is well represented, future models can be swapped into the system while retaining the process intelligence.

## 25. How the system should be developed

The conversation then turned from "what should the system look like?" to a more fundamental question:

> **How do we want to make it?**

The decision was not to immediately choose LangGraph, multiple model providers, a graph database, or a fixed number of agents.

Instead, the project should begin as conceptual research and design.

The initial development method is:

1. discuss freely and explore the problem from first principles;
2. preserve stable insights in a repository;
3. distinguish decisions from hypotheses and open questions;
4. test ideas on real projects;
5. record gaps and generalize lessons;
6. only choose implementation architecture after the required behavior is sufficiently understood;
7. iterate between specification, implementation, and real projects thereafter.

This deliberately delays technical commitment.

## 26. Knowledge preservation became part of the design problem

A practical problem appeared immediately.

The initial conversation itself contained long, detailed reasoning that would eventually fall out of chat context.

This led to a distinction:

> **The chat is where we think. The repository is where the system remembers.**

However, another subtle issue appeared.

If every long discussion were compressed into a few bullet points, important intellectual context would be lost.

For example, the principle:

```text
Evidence should dominate unsupported LLM judgment.
```

is useful, but the correlated-feature example explains what that principle means in practice and why it matters.

Therefore, the project adopted layered preservation.

### Canonical knowledge

Concise, current, authoritative enough for routine use.

### Foundational design memos

Long-form explanations that preserve reasoning and examples.

### Checkpoints and session records

Historical state and development progression.

### Raw conversation archive

Potential future provenance layer, not current canonical truth.

This memo is the first example of the foundational layer.

## 27. The preservation method must also evolve

Another important realization followed.

The project is not only designing the Autonomous Data Science System. It is simultaneously discovering how to design, document, and preserve the system.

Initially the idea was simply to save important conclusions.

Then the need for a structured repository became clear.

Then the risk of over-compression became clear.

That produced the foundational-memo layer.

Future use may reveal further problems:

- one decisions file may become too large;
- current-state updates may become repetitive;
- duplicated knowledge may drift out of sync;
- foundational memos may need an index;
- knowledge modules may require machine-readable schemas;
- conversation capture may become partly automated.

The development methodology should therefore be treated as versioned and provisional.

This mirrors the philosophy of the target system itself:

```text
observe
 -> reason
 -> test
 -> discover weakness
 -> update process
 -> preserve lesson
```

## 28. New-chat continuity is a design requirement

Because chats have finite capacity, continuation in a new session cannot be an improvised emergency procedure.

A future chat should be able to read the repository and reconstruct:

- what the project is;
- what has been decided;
- what remains speculative;
- what questions are unresolved;
- what the current focus is;
- and what should happen next.

This is why `CURRENT_STATE.md` and `CONTINUITY.md` were created at Checkpoint 0.

The same concept may later inform the system itself: long-running data projects need persistent state so that a different model, agent, process, or human can resume work without reconstructing everything from memory.

## 29. Why the project was separated from individual Data Projects

The initial discussion took place inside a broader Data Projects area.

It became clear that the Autonomous Data Science System belongs at a different conceptual level.

Individual projects are things the system may eventually analyze, guide, review, or learn from.

The system itself therefore received a dedicated project folder and GitHub repository.

This separation also makes it easier to use existing projects as test cases without confusing system-level knowledge with project-specific code.

## 30. What has deliberately not been decided

This memo preserves several promising directions, but Checkpoint 0 intentionally does not decide:

- the number of agents;
- which LLM providers to use;
- whether multiple providers are necessary;
- whether modules are Markdown, YAML, code, graph nodes, or database records;
- the orchestration framework;
- the state database;
- the rule engine;
- the execution environment;
- the final project taxonomy;
- the final autonomy model;
- or the final evaluation framework.

Those decisions should follow requirements rather than lead them.

## 31. The next question

After preserving Checkpoint 0, the next substantive design question is:

> **What exactly are we trying to create, and what properties must it have for us to consider it successful?**

This requires moving from an inspiring broad vision to a more rigorous definition of goals, requirements, boundaries, success criteria, autonomy, human role, quality, efficiency, and evaluation.

Only after that should implementation architecture become the central topic.

## 32. Status of the concepts in this memo

This memo intentionally contains concepts at different maturity levels.

### Strong working principles

- evidence over unsupported LLM assertion;
- adaptive and revisitable reasoning;
- explicit assumptions and project state;
- human involvement where judgment matters;
- project-driven system development;
- generalizing lessons from failures;
- layered knowledge preservation;
- repository-based continuity.

### Strong design hypotheses

- reusable decision modules;
- trigger-based activation;
- reasoning graphs;
- specialized review roles;
- proposer-reviewer separation;
- independent replication;
- configurable depth.

### Explicitly unresolved implementation questions

- concrete agent architecture;
- concrete knowledge representation;
- orchestration technology;
- database and graph choices;
- model-provider strategy;
- execution infrastructure.

Future work should preserve these distinctions.

---

This memo is intentionally detailed. Its role is not to be the fastest document to read. Its role is to preserve the foundational reasoning that the shorter canonical documents necessarily compress.
