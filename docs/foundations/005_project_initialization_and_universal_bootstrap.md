# Project Initialization and Universal Bootstrap

**Status:** Foundational design memo  
**Date:** 2026-08-08  
**Maturity:** Strong design hypotheses, not final architecture

## Purpose

This memo preserves the reasoning developed after Checkpoint 4 about how a completely new data-science project should enter the Autonomous Data Science System.

Checkpoint 4 developed a typed, dependency-aware project-state model and a state-driven orchestration hypothesis. That raised a prior question: how does such a state exist in the first place when the initial user request, data, code, documentation, intended use, and constraints may be incomplete, contradictory, outdated, or wrong?

The current answer is not a one-shot intake form and not immediate modelling. The emerging hypothesis is **progressive state construction** supported by a small **universal bootstrap inspection**.

The bootstrap is intended to generate enough trustworthy structural state, conflicts, questions, and triggers for the adaptive system to take over. It is not intended to perform the entire EDA process or define one universal data-science pipeline.

---

## 1. Initial requests are evidence about the project, not automatically truth

A user may say:

> Predict which customers will churn next month. The dataset is clean and each row is one customer.

A weak system may immediately record:

```text
task = binary classification
target = churn
prediction_horizon = one month
observation_unit = customer
data_quality = clean
```

and treat those statements as established facts.

A stronger system should preserve two separate concepts:

```text
ORIGINAL PROJECT INPUT
What the user or source actually stated.

CURRENT PROJECT INTERPRETATION
What the system currently believes the project means.
```

The original input should remain provenance. The current interpretation may change as the system inspects the project.

A reported statement such as "each row represents one customer" may therefore begin as source-aware project state rather than immutable truth.

If the data later reveal repeated customer IDs, the appropriate state is not simply to overwrite the user's statement. The system should preserve the reported statement, record the observed structure, create an explicit conflict, and activate a question about the observation unit.

This is the first application of the broader principle that state should preserve epistemic role and provenance rather than flatten all information into one narrative.

---

## 2. New projects begin in a bootstrap state

The project may not have enough information at the beginning to construct a complete semantic model.

The current hypothesis is therefore:

```text
RAW INPUTS
    -> source registration
    -> reported statements / candidate facts
    -> provisional interpretation
    -> explicit uncertainties and conflicts
    -> high-value initialization questions
    -> safe initial investigations
    -> richer project state
```

Initialization is itself an adaptive reasoning process.

It should not require that every project variable, governance rule, deployment detail, metric preference, and operational threshold be known before any useful work begins.

Instead, the system should establish enough understanding for the next legitimate actions while making unresolved dependencies explicit.

---

## 3. Progressive semantic commitment

Different actions require different levels of project understanding.

For example, the system may not need exact false-negative cost before inspecting a dataset, but it may need that trade-off before choosing an operational decision threshold.

Likewise, unknown deployment latency may not block basic EDA, while unknown prediction timing may block a leakage-sensitive feature audit.

The emerging principle is:

> **The system should require only the semantic information necessary for the action it is about to take, while preventing actions whose material semantic prerequisites remain unresolved.**

This avoids two bad extremes:

```text
blindly begin modelling from the user's first description
```

and

```text
force the user through a very large intake questionnaire before any useful work occurs
```

Project understanding therefore remains active throughout the project rather than ending after an initial "business understanding" phase.

---

## 4. Source-aware initialization

A new project may contain many possible sources of knowledge:

```text
user request
README files
data dictionaries
datasets
schemas
notebooks
source code
configuration
saved models
existing reports
pipeline definitions
deployment documentation
external requirements
```

The bootstrap should first establish what material exists and what role each source may play.

A source may need conceptual properties such as:

```text
origin
authority domain
scope
version
recency
reliability
directness
information restrictions
```

No source should have universal precedence across every question.

For example:

- the project owner may be authoritative about the desired business objective;
- a schema owner may be more authoritative about the meaning of a database field;
- direct inspection is authoritative about what values are actually present in a file;
- deployment documentation may be authoritative about when a feature is operationally available;
- existing code is evidence of what the historical implementation does, not automatic proof that its methodology is correct.

A central hypothesis is therefore:

> **Authority is question-specific.**

---

## 5. Contradictions are useful project state

When credible sources disagree, the system should not arbitrarily choose one and continue.

A conflict should become explicit state, for example:

```text
Subject:
Prediction horizon

Source A:
User request = 30 days

Source B:
Requirements document = 90 days

Materiality:
High

Affected:
Target construction
Feature eligibility
Validation design
Metric interpretation

Resolution:
Unresolved
```

Contradiction should create a question automatically when it is material.

The system should generally become more cautious as high-authority sources disagree.

---

## 6. The universal bootstrap should be small and trigger-oriented

The bootstrap should not become a universal EDA checklist.

An early inspection belongs in the bootstrap only when it is broadly relevant, low-risk, relatively cheap, non-destructive, provenance-preserving, and likely to reveal facts that activate more specialized reasoning.

Useful criteria include:

```text
BROADLY RELEVANT
LOW SEMANTIC COMMITMENT
LOW RISK
HIGH TRIGGER VALUE
RELATIVELY CHEAP
NON-DESTRUCTIVE
PROVENANCE-PRESERVING
REVERSIBLE
```

The purpose is:

> **Generate enough trustworthy initial state that the adaptive system can determine which specialized questions should become active next.**

The bootstrap should therefore detect conditions and emit triggers rather than solving every condition itself.

---

## 7. Source inventory before EDA

Before substantial data inspection, the system should inventory available project material.

For example:

```text
SOURCE S-001
user request
role: stated project objective

SOURCE S-002
data dictionary
role: field semantics

SOURCE S-003
training dataset
role: empirical data

SOURCE S-004
existing notebook
role: historical implementation

SOURCE S-005
deployment configuration
role: operational evidence
```

Existing filenames should not be treated as guaranteed semantics.

A file named `test.csv` establishes that a file with that name exists. It does not prove whether it is a development holdout, final untouched test set, competition scoring file, or production batch.

The intended role should be inferred from better project evidence before inspection crosses information boundaries.

---

## 8. Bootstrap inspection must obey information legitimacy

The bootstrap itself is not exempt from epistemic integrity.

Before deeply inspecting a source, the system should determine what information is currently legitimate to consume.

Conceptually:

```text
AVAILABLE MATERIAL
        -> determine role and restrictions
        -> establish inspection envelope
        -> inspect only legitimate information
```

This matters especially for final test data.

A bootstrap may legitimately need to inspect metadata such as file existence, column names, schema compatibility, or row counts while still preventing access to labels or outcome associations that would contaminate later development.

A future execution architecture may need enforceable information barriers rather than merely relying on an agent to remember not to inspect restricted information.

No implementation has been selected.

---

## 9. Early structural facts

Once legitimate data sources have been identified, the universal bootstrap can establish low-commitment structural observations such as:

```text
row count
column count
column names
physical data types
parseability
missing-value presence
candidate identifiers
candidate timestamps
candidate target mentioned by project sources
basic cardinalities
partition structure
data coverage where safe
obvious malformed values or structural inconsistencies
```

These should be treated as structural observations rather than complete semantic interpretation.

For example:

```text
dtype = int64
```

should not imply:

```text
semantic type = continuous numeric variable
```

because the field may actually be an identifier, postal code, flag, or ordinal category.

---

## 10. Identifier discovery has high trigger value

Potential identifiers are especially valuable during bootstrap.

If a dataset has 24,000 rows and only 8,000 unique customer IDs, this immediately raises a structural question:

> Why does each entity appear multiple times?

Possible explanations include longitudinal observations, repeated transactions, multiple accounts, duplicates, or extraction errors.

The bootstrap should record the structural fact and activate an entity-structure investigation rather than immediately deciding how to handle the repeated rows.

This can have major downstream consequences for validation and interpretation.

---

## 11. Time structure should be detected early

The presence of timestamps, periods, sequence order, or event dates has high trigger value.

Time-like structure may activate questions about:

```text
forward-looking prediction
observation order
longitudinal structure
temporal leakage
feature construction through time
chronological validation
drift
deployment timing
forecast horizon
```

The bootstrap should not conclude that every timestamp implies a time-series model.

It should observe broadly and infer cautiously.

---

## 12. Target inspection should distinguish structure from semantics

If the project states that a column is the target, the bootstrap may inspect structural properties on legitimate development data, such as:

```text
missingness
number of unique values
encoding
class distribution
```

Those facts can activate classification, imbalance, label-quality, missing-label, or metric-selection reasoning.

However:

```text
Observed: target column is binary
Reported: target column is intended outcome
```

does not establish:

```text
Verified: the target correctly represents the desired future event and horizon
```

Target semantics remain a separate project question.

---

## 13. Missingness and duplicates: detect first, reason later

Missingness belongs in the universal bootstrap at the detection level because it has high trigger value.

The bootstrap may detect which columns have missing values and approximate rates, but should not immediately choose mean imputation, median imputation, deletion, or any universal threshold rule.

Instead:

```text
BOOTSTRAP:
Feature X has 42% missingness.

TRIGGER:
Activate missing-data reasoning.
```

The same applies to duplicate structure.

Exact duplicate rows, duplicate IDs, or repeated entities may be detected early, but the appropriate response depends on semantics.

The system should not turn "duplicate detected" directly into "delete duplicate."

This supports a broader design rule:

> **Bootstrap detects conditions. Specialized knowledge modules reason about responses.**

---

## 14. Structural inconsistencies should become conflicts

Cheap checks may reveal mismatches between documentation and empirical structure, for example:

```text
Documentation: one row per account
Observed: account IDs repeat heavily

Documentation: no missing values
Observed: one field is 18% missing

Documentation: target is binary
Observed: three values exist
```

These should be recorded as material conflicts when relevant rather than silently corrected or ignored.

This is one place where the system can outperform an obedient end-to-end LLM workflow: it actively tests whether the available sources tell a coherent story.

---

## 15. Bootstrap should remain more structural than predictive

The universal bootstrap should generally avoid automatically running target correlations, feature importance, broad target-rate analysis, or large predictive screens.

Those analyses may be valuable later, but they require more semantic context and can create information leakage or premature interpretation.

The bootstrap should optimize for structural trigger value rather than analytical completeness.

Basic distributions may be inspected selectively when they reveal obvious anomalies or useful semantic hypotheses, but exhaustive histogram generation is not itself a universal requirement.

---

## 16. Partition and split structure should be identified early

If multiple datasets or partitions exist, the bootstrap should determine their structural roles as far as available evidence allows.

Potential observations include:

```text
which partitions exist
schema compatibility
target presence
identifier overlap
time overlap
row counts
```

Entity overlap or temporal overlap across partitions has particularly high trigger value because it may activate validation and leakage investigations.

Detection should remain separate from interpretation.

For example, customer overlap between train and validation may be appropriate for predicting future outcomes for known customers but inappropriate for estimating generalization to unseen customers.

---

## 17. Existing code is historical evidence, not accepted methodology

If an existing repository contains code, the bootstrap may inspect structural properties such as:

```text
languages and environments
data loading paths
split logic
preprocessing order
models already implemented
output locations
random-state handling
test-data references
external services
credentials or secrets risk
dependency specification
```

A pattern such as fitting a scaler before splitting establishes that the historical implementation behaves that way. It does not establish that the methodology is acceptable.

Potential methodological issues should activate focused review.

This creates a distinction between:

```text
CURRENT IMPLEMENTATION STATE
```

and

```text
CURRENT ACCEPTED METHODOLOGICAL STATE
```

which may differ substantially in inherited projects.

---

## 18. Environment and executability are part of bootstrap state

The system cannot select executable work intelligently unless it knows basic operational capabilities.

Useful early facts may include:

```text
language/runtime
available dependency specification
execution environment
data accessibility
GPU availability where relevant
required credentials
database connectivity
Docker or container configuration
existing tests
```

These facts determine which actions can appear on the runnable frontier.

An analytically valuable action that cannot currently execute because a required database is unavailable remains blocked.

---

## 19. Admissibility and risk begin during bootstrap

The bootstrap should detect obvious governance-relevant facts and constraints where available, such as:

```text
potential personal identifiers
possible sensitive attributes
credentials
external API use
data-use restrictions
license information
explicit local-only processing requirements
production automation intent
human-impacting decisions
```

The bootstrap should not attempt to settle every legal or ethical question.

It should create triggers for the relevant admissibility and risk processes.

Similarly, risk should begin with risk-relevant facts and potential scenarios rather than an unexplained project-level score.

---

## 20. Project characterization should be multidimensional

The system should avoid compressing projects into one label such as:

```text
project_type = classification
```

A project may simultaneously be:

```text
supervised
binary classification
temporal
grouped by entity
forward-looking
sequence-derived
imbalanced
```

These structural characteristics activate different questions and knowledge modules.

The current hypothesis is therefore a project-characterization profile composed of multiple discovered facts and interpretations rather than a mutually exclusive taxonomy.

---

## 21. Intended use is a high-leverage initialization object

Intended use affects validation, feature legitimacy, metrics, calibration, interpretation, admissibility, risk, monitoring, and human gates.

The system should therefore try to establish intended use relatively early while allowing it to remain provisional and revisable.

A project may legitimately evolve from offline exploration to operational deployment. Such a change should trigger impact analysis and new assurance obligations rather than being treated as a simple metadata edit.

---

## 22. Analytical objective and deliverable should remain separate

A requested artifact is not the same as the analytical objective.

For example:

```text
Analytical objective:
Predict churn.

Deliverable:
PowerPoint presentation.
```

Or:

```text
Model objective:
Predict target.

Project objective:
Learning and portfolio quality.

Deliverables:
Code and detailed report.
```

This reinforces the earlier project-intent decomposition into objectives, constraints, deliverables, and human-control preferences.

---

## 23. Human questions should be selective and purposeful

The system should not ask the human everything it does not know.

It should first exploit available data, documentation, code, schemas, and authoritative sources when they can resolve the question cheaply and reliably.

Human clarification becomes valuable when:

- a material semantic question cannot be established elsewhere;
- the answer is normative or preference-based rather than empirical;
- an authority decision is required;
- unresolved ambiguity blocks important work;
- or the expected value of authoritative clarification exceeds further autonomous investigation.

A blocking question should ideally preserve why it is being asked and which downstream objects depend on the answer.

This supports selective human involvement without arbitrary interruption schedules.

---

## 24. Current project interpretation as a derived human view

A useful human-facing view may summarize the current interpretation without becoming the source of truth.

For example:

```text
CURRENT PROJECT INTERPRETATION

Objective:
Predict cancellation within 30 days.

Observation unit:
Customer-month.

Prediction point:
First day of each month.

Population:
Active subscribers.

Intended use:
Prioritize retention outreach.

Known constraints:
No external data.

Known uncertainties:
Production missingness not confirmed.

Active blockers:
None for exploratory modelling.
```

The user can then correct a high-leverage interpretation directly.

Corrections should preserve history, update current state, and trigger impact analysis through the Checkpoint 4 dependency mechanism.

---

## 25. Initialization is complete enough when a legitimate runnable frontier exists

Initialization should not require complete certainty about every future project decision.

The key threshold is:

> **There is at least one useful, admissible, methodologically legitimate action that can proceed, while important unresolved questions and blockers are explicitly represented.**

This means initialization is not globally complete or incomplete in a binary sense.

A project may be ready for data-quality investigation while still blocked from trustworthy model comparison.

Blocking is relative to an action or milestone.

---

## 26. Six universal bootstrap responsibilities

The current conceptual bootstrap can be compressed into six broad responsibilities:

1. **Register sources and information boundaries.**  
   Identify material, provenance, versions, likely roles, authority domains, and what information is legitimate to inspect.

2. **Establish structural facts.**  
   Inspect schemas, shapes, identifiers, timestamps, candidate target structure, missingness, duplicates, partitions, data coverage, environment, and executability.

3. **Compare sources for consistency.**  
   Detect contradictions among user descriptions, documentation, code, schemas, data, existing artifacts, and operational descriptions.

4. **Generate project-characterization hypotheses.**  
   Infer possibilities such as temporal structure, repeated entities, longitudinal data, imbalance, sequence structure, sensitive information, or inherited methodology without prematurely canonizing them.

5. **Emit triggers and questions.**  
   Convert discovered facts and conflicts into specialized questions and obligations such as leakage, missingness, validation, label quality, admissibility, risk, or semantic clarification.

6. **Construct the first runnable frontier.**  
   Determine which investigations can safely proceed and which remain blocked by semantics, permissions, dependencies, approvals, or resources.

This is intended as a conceptual protocol, not a final implementation workflow.

---

## 27. Observe broadly, infer cautiously

A concise behavioral rule for bootstrap reasoning is:

> **Observe broadly, infer cautiously.**

Examples:

```text
OBSERVE:
customer_id repeats.

DO NOT CONCLUDE:
delete duplicates.

HYPOTHESIZE:
repeated entity observations may exist.

ACTIVATE:
entity-structure investigation.
```

```text
OBSERVE:
timestamp exists.

DO NOT CONCLUDE:
time-series model required.

ACTIVATE:
temporal-structure reasoning.
```

```text
OBSERVE:
positive class rate = 2%.

DO NOT CONCLUDE:
SMOTE required.

ACTIVATE:
imbalance / metric / threshold reasoning.
```

This behavior preserves explicit knowledge without turning it into brittle universal rules.

---

## 28. Bootstrap should produce triggers, not a complete plan

A successful bootstrap may produce a state such as:

```text
Observed:
- binary target candidate
- repeated customer IDs
- monthly timestamp
- non-trivial missingness
- random existing split
- production description indicates periodic prediction

Activated questions:
- What does one row represent?
- Should validation be temporal, grouped, or both?
- Are features available at prediction time?
- How should production missingness be represented?
- Does entity overlap bias current evaluation?

Current safe actions:
- entity-history analysis
- prediction-timing documentation review
- missingness-pattern analysis on development data
- existing split audit

Blocked:
- trustworthy model comparison
```

That is more useful than declaring "EDA complete" and advancing to a fixed preprocessing stage.

---

## 29. Bootstrap stopping rule

The bootstrap itself should stop once additional universal inspection has lower value than handing activated questions to specialized reasoning.

A useful conceptual stopping criterion is:

> **Bootstrap inspection is sufficient once the system has enough trustworthy structural state to activate relevant specialized investigations and produce a legitimate runnable frontier.**

This prevents bootstrap from expanding into an exhaustive project-wide checklist.

---

## 30. Universal bootstrap followed by adaptive reasoning

The most important simplification from this checkpoint is that the system may not need a universal data-science workflow.

It may need only a relatively small universal entry protocol:

```text
NEW PROJECT
    -> source registration
    -> provisional interpretation
    -> information-boundary determination
    -> universal bootstrap inspection
    -> structural facts and conflicts
    -> characterization hypotheses
    -> triggers
    -> specialized questions / knowledge modules
    -> first runnable frontier
```

After that, the Checkpoint 4 control loop can take over:

```text
action
    -> evidence
    -> state update
    -> impact analysis
    -> new obligations
    -> new runnable frontier
```

This suggests a potentially much more manageable system than one attempting to enumerate every possible project workflow in advance.

The fixed portion can remain small, while most analytical depth emerges from state-triggered specialized knowledge.

---

## 31. Current strong design hypotheses

The following ideas have strong conceptual support after this discussion but remain hypotheses rather than final architecture:

- a new project begins as provisional, source-aware state rather than accepted truth;
- original source statements and current interpretation should remain distinct;
- authority is question-specific;
- contradictions should become explicit conflicts and questions;
- semantic commitment should be progressive and action-relative;
- the system should establish an information-legitimate inspection envelope before consuming restricted data;
- universal bootstrap inspection should remain small, cheap, structural, and trigger-oriented;
- bootstrap detects conditions while specialized modules reason about responses;
- project characterization should be multidimensional rather than one project-type label;
- intended use is a high-leverage, revisable state object;
- human clarification should be selective and used when authoritative information has high expected project value;
- initialization is sufficiently complete when a legitimate first runnable frontier exists;
- a small universal bootstrap protocol may replace the need for one universal end-to-end data-science workflow.

---

## 32. Explicit non-decisions

This checkpoint does not decide:

- the exact source schema;
- authority precedence rules;
- exact confidence or reliability representation;
- exact bootstrap checks;
- exact inspection-envelope enforcement mechanism;
- project-characterization schema;
- how much code inspection belongs in bootstrap;
- how sensitive-data detection is implemented;
- the final project-intent schema;
- which bootstrap operations are deterministic versus LLM-driven;
- how triggers select reusable knowledge modules;
- the implementation representation of triggers;
- the storage architecture;
- orchestration technology;
- agent roles or count.

---

## 33. Next conceptual problem

The next major design problem follows directly from bootstrap:

> **How should discovered facts, conflicts, questions, and project characteristics activate the correct reusable knowledge modules, rules, reviewers, or open-ended reasoning without creating one impossibly large centralized decision tree?**

This is the knowledge-activation problem.

Important questions include:

- What exactly is a trigger?
- What does a knowledge module receive and produce?
- Can several modules respond to the same fact?
- Can modules activate further modules through state changes?
- Which activations should be deterministic versus proposed by an LLM?
- How are missed activations detected?
- How does the system avoid activating too much irrelevant knowledge?
- Should modules subscribe to state patterns rather than call each other directly?
- How does module activation integrate with the runnable frontier and project-state dependency model?

This should be explored conceptually before selecting a rule engine, graph system, workflow framework, or agent architecture.
