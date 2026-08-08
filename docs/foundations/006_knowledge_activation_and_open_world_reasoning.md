# Foundation 006: Knowledge Activation and Open-World Reasoning

**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Status:** Strong design hypotheses, not implementation architecture

## 1. Why this foundation exists

Checkpoint 5 established a small universal bootstrap protocol that turns a new project into provisional, source-aware project state and a first runnable frontier. Checkpoint 4 established that the ongoing system should be driven by typed, dependency-aware state rather than a fixed global pipeline.

The next bottleneck is scalability of data-science knowledge.

A mature system may eventually need to reason about hundreds of recurring concerns: missingness, temporal dependence, grouped observations, leakage, class imbalance, metric selection, calibration, feature availability, causal identification, clustering purpose, privacy, deployment monitoring, model-specific assumptions, and many more.

The system should not solve this by:

- executing every possible analytical check on every project;
- encoding one enormous centralized decision tree;
- assigning one permanent agent to every topic;
- or assuming a single LLM will reliably remember the entire universe of data-science concerns at every step.

The emerging alternative is a reusable knowledge library whose relevant portions become active from project state.

The central hypothesis is:

> **Reusable data-science knowledge should be activated from patterns in project state and should contribute structured questions, obligations, safeguards, evidence requirements, review needs, and candidate actions back into that state rather than directly controlling one fixed workflow.**

This foundation develops that hypothesis and stress-tests it across heterogeneous analytical concerns.

---

## 2. Knowledge, capability, and actor should be separate

A reusable knowledge module is not the same thing as an agent.

For example, a `Missing Data` knowledge unit should represent what must be considered when missingness is relevant. It may contain applicability conditions, important distinctions, questions, methodological constraints, evidence requirements, common failure modes, candidate strategies, human gates, and conditions for sufficient resolution.

The capability used to investigate those questions may instead involve Python execution, statistical analysis, document retrieval, external research, or human clarification.

The actor may be a general reasoning model, a specialized reviewer, deterministic code, or a future agent role.

Conceptually:

```text
KNOWLEDGE
What should be considered?

CAPABILITY
How can the issue be investigated or enforced?

ACTOR
Who or what performs the work?
```

Keeping these separate prevents the knowledge architecture from becoming a rigid roster of permanent agents such as `MissingDataAgent`, `TemporalAgent`, `LeakageAgent`, and many others.

The durable intellectual asset should be the reasoning specification, not the agent persona.

---

## 3. Reusable definitions versus project-specific instances

The system-level knowledge library and project state should not collapse into one object.

A reusable definition may be:

```text
Knowledge unit:
Missing Data
Version:
0.x
```

A particular project may then instantiate that knowledge for a specific scope:

```text
Project-specific knowledge instance

Triggered by:
Income missingness
Target missingness
Production-scoring requirement

Current questions:
...

Current evidence:
...

Current resolution:
...
```

This distinction enables reuse and cumulative learning:

```text
reusable knowledge
    -> applied in project
    -> project exposes gap or failure
    -> generalizable lesson extracted
    -> reusable knowledge revised
```

A module definition can therefore evolve across projects while each project instance preserves what happened under the specific project state that activated it.

---

## 4. Activation is relevance detection, not automatic execution

A trigger should not normally mean "execute the whole module now."

Instead:

> **A trigger means that current project state has created sufficient reason for some reusable knowledge to be considered, investigated, or enforced.**

Conceptually:

```text
PROJECT STATE
    -> relevance condition becomes true
    -> knowledge activates
    -> questions / obligations / safeguards enter state
    -> runnable-frontier logic decides what actually executes
```

This distinction is important because a concern may be relevant while another issue remains a higher-priority blocker.

For example, missingness reasoning can be active while target semantics remain unresolved. Activation priority and execution priority are therefore distinct.

---

## 5. Activation strength should not be purely binary

The stress tests show that `ACTIVE` versus `INACTIVE` is too crude.

A useful conceptual distinction is:

```text
ENFORCE
A sufficiently established state pattern creates a mandatory requirement.

INVESTIGATE
The issue is plausibly relevant and applicability or consequences need to be established.

CONSIDER
The topic may improve the project but is not currently mandatory.
```

The names remain provisional.

For example, merely discovering a timestamp may justify investigating temporal relevance. Discovering a timestamp together with a future-facing prediction task may make temporal validation constraints substantially stronger. A known attempt to use future information in a historical prediction may activate a hard information-legitimacy rule.

Activation strength can therefore change as project state becomes more specific.

---

## 6. Three broad activation mechanisms

The project currently favors a hybrid activation model.

### 6.1 Deterministic activation

Some conditions are precise enough that once relevant facts are established, a safeguard or obligation should activate automatically.

Examples include:

- a final test set designated for untouched evaluation plus a proposed development action using its outcomes;
- learned preprocessing used in evaluation while fitted outside the legitimate training portion;
- a required approval being absent for an action whose governance rule explicitly requires it.

These should not depend on persuasive LLM judgment once their conditions are known.

### 6.2 Interpretive or conditional activation

Many facts suggest relevance without determining the methodological response.

Examples include:

- repeated customer identifiers;
- timestamps whose analytical role is unclear;
- severe target imbalance;
- a variable that may be post-outcome;
- apparent outliers with uncertain domain meaning.

These patterns should activate applicability reasoning rather than a fixed prescription.

### 6.3 Open-ended discovery

The knowledge library is intentionally incomplete.

Novel domain structures, feedback loops, unusual data-generating processes, or unexpected interactions may not match any existing reusable unit cleanly.

Open-ended reasoning must therefore be able to introduce a new concern into project state even when no explicit module exists.

This keeps the architecture open-world rather than treating the current knowledge library as exhaustive.

---

## 7. Trigger sources are broader than observed data facts

The stress tests substantially broadened the activation concept.

Knowledge may become relevant because of:

- an observed fact;
- a combination of facts;
- a requested analytical objective;
- a desired claim type or strength;
- a proposed action;
- a proposed method;
- a proposed decision;
- a proposed claim;
- a missing prerequisite;
- a contradiction between sources or state objects;
- a risk or governance condition;
- a dependency revision;
- or an open-ended novel concern.

This means the activation layer should monitor project-state transitions broadly rather than only raw data observations.

---

## 8. Reactive versus prospective activation

A particularly important distinction emerged from leakage and governance examples.

### Reactive activation

Something has been observed or discovered.

Example:

```text
Repeated entity identifiers detected
    -> activate group-dependence reasoning
```

### Prospective activation

Something is being proposed and must be checked before execution or acceptance.

Example:

```text
Proposed action:
Inspect final test outcomes during model development

Existing state:
Test set is reserved for final untouched evaluation

Result:
Information-legitimacy safeguard activates before the action occurs
```

Prospective activation may apply to proposed methods, actions, claims, decisions, and state transitions.

This suggests that reusable knowledge can act as a semantic validation layer around consequential proposals, not merely as a scheduler reacting to past observations.

---

## 9. Missing prerequisites can themselves trigger obligations

Causal inference exposed another important trigger type.

Suppose a project requests a strong causal claim but contains no explicit treatment definition, estimand, temporal ordering, identification assumptions, or assignment mechanism.

The absence of required state is itself meaningful.

Conceptually:

```text
requested causal claim
AND
required identification state absent
    -> causal-identification knowledge activates
    -> strong causal conclusion blocked
    -> missing questions and obligations created
```

The same pattern appears elsewhere:

```text
deployment proposed
but no monitoring requirement satisfied
```

```text
final model selection proposed
but no accepted validation design exists
```

```text
external transfer proposed
but permission state unresolved
```

```text
operational threshold proposed
but utility or error-cost tradeoff undefined
```

The activation mechanism should therefore support unsatisfied-prerequisite patterns, not only positive observations.

---

## 10. Modules should consume relevant state slices

A knowledge unit should not need the entire project transcript.

Instead, activation should produce a context slice containing the state relevant to that concern, potentially including:

- project intent;
- intended use;
- triggering facts;
- relevant assumptions;
- active questions;
- constraints and rules;
- relevant evidence;
- affected artifacts;
- downstream dependencies;
- risk and assurance context;
- prior resolution history.

This improves context efficiency and reduces distraction from unrelated project material.

It also makes specialized review and controlled independence easier because different actors can receive different derived views of the same authoritative state.

---

## 11. Modules should write typed contributions back into state

A knowledge unit should not merely return a large prose answer.

Depending on the concern, it may contribute:

- new analytical questions;
- semantic obligations;
- methodological obligations;
- evidence requirements;
- candidate investigations;
- hard constraints or safeguards;
- risk scenarios;
- review requests;
- human clarification requests;
- candidate decisions or alternatives;
- conditions for sufficient resolution.

These contributions should preserve their epistemic and governance role rather than collapsing into one recommendation blob.

A module may therefore enrich project state without directly executing any analysis.

---

## 12. Modules should interact primarily through shared state

Direct module-to-module calling risks creating another tightly coupled decision tree.

The stronger direction is:

```text
MODULE A
    -> project-state update
    -> new fact / question / obligation
    -> activation layer evaluates state
    -> MODULE B becomes relevant
```

rather than:

```text
MODULE A directly calls MODULE B
```

Example:

```text
Missingness investigation discovers strong time variation
    -> fact recorded in project state
    -> temporal reasoning becomes relevant
```

This makes cross-module behavior auditable, revisable, and less coupled.

---

## 13. Shared questions can reconcile overlapping knowledge

One observation may activate several knowledge units.

Repeated customers over time may be relevant to:

- group dependence;
- temporal structure;
- leakage;
- validation design;
- longitudinal modelling.

These units should not automatically create duplicate workflows.

Instead, several may contribute to one shared analytical question such as:

> Does the current validation design represent the intended deployment regime?

The question can preserve multiple motivations:

```text
motivated_by:
- temporal structure
- repeated entities
- potential information overlap
```

This suggests that questions may be an important integration interface between otherwise composable knowledge units.

---

## 14. Knowledge should encode evidence requirements, not recipes

A weak library would become a cookbook:

```text
if imbalance -> use SMOTE
if missing values -> median-impute
if high cardinality -> target-encode
```

The intended design is fundamentally different.

A strong knowledge unit encodes which distinctions matter and what evidence can establish them.

For class imbalance, for example, the important questions may involve:

- target prevalence;
- relevant error costs;
- metric choice;
- whether calibrated probabilities matter;
- threshold policy;
- whether resampling improves the relevant validation outcome;
- whether resampling damages calibration;
- whether prevalence is stable in deployment.

The response strategy should emerge from evidence rather than from one unconditional recommendation.

---

## 15. Hard rules, decision frameworks, and open reasoning can coexist within one knowledge area

The hybrid architecture does not require every knowledge area to be purely declarative or purely generative.

A missing-data unit may contain:

### Hard requirement

Any learned imputation procedure used in evaluation must be fitted only on information legitimate for the corresponding training portion.

### Conditional decision framework

Questions about production missingness, retention of the feature, row deletion, missingness indicators, native model handling, and comparative validation.

### Open-ended reasoning

Could the missingness pattern reflect an unmodeled domain process?

This makes the knowledge unit a richer reasoning specification rather than a single rule type.

---

## 16. Knowledge needs scope

Concerns do not always apply project-wide.

Possible scopes include, conceptually:

- project;
- dataset;
- partition;
- feature;
- feature set;
- target;
- subgroup;
- model;
- claim;
- decision;
- action;
- deployment environment.

The exact scope model remains unresolved.

Scope is necessary to avoid vague global states such as `missing_data_active = true` when target missingness, one severely incomplete feature, and negligible missingness in another feature require different reasoning.

---

## 17. Candidate relevance versus established applicability

To control over-activation, semantic retrieval should not necessarily instantiate a full concern immediately.

A useful two-step concept is:

```text
candidate relevance
    -> applicability determination
    -> project-specific knowledge instance
```

Example:

```text
timestamp detected
    -> temporal knowledge retrieved
    -> applicability check
    -> timestamp is merely database-ingestion metadata
    -> deeper temporal concern dismissed for current purpose
```

Deterministic hard rules may skip this applicability stage when their predicates are already sufficiently precise.

---

## 18. Stress test: missing data

Observed feature missingness cleanly activates missing-data reasoning.

The knowledge unit contributes questions about production missingness, feature value, population effects of deletion, missingness signal, and leakage-safe transformation fitting.

The module does not automatically choose median imputation or deletion.

This case strongly supports the architecture.

---

## 19. Stress test: temporal structure

A timestamp alone creates candidate temporal relevance rather than a mandatory time-series workflow.

Combining a timestamp with future-facing intended use substantially strengthens applicability and can activate temporal validation obligations.

This case demonstrates that activation often depends on combinations of state objects rather than single events.

---

## 20. Stress test: group or entity dependence

Repeated entities activate questions about the intended generalization regime.

The correct response may differ depending on whether deployment predicts new observations for known entities, unseen entities, future observations, or some combination.

Temporal and entity-dependence knowledge may converge on the same validation-design question, validating shared questions as an integration mechanism.

---

## 21. Stress test: target leakage and information legitimacy

Potential post-outcome features initially activate investigation.

Once prediction timing and feature-generation timing are established, the same concern may become a hard constraint.

Proposed use of final-test outcomes shows that activation must also operate prospectively on intended actions before execution.

This case strongly supports proposal-validation semantics.

---

## 22. Stress test: class imbalance

A rare positive class activates reasoning about metrics, error costs, calibration, thresholding, and resampling.

The rarity itself is not automatically a defect and does not imply SMOTE or another fixed treatment.

This supports the interpretation of knowledge modules as structured question generators rather than problem-response recipes.

---

## 23. Stress test: causal inference

Causal reasoning may activate because of the requested claim type even when the dataframe resembles ordinary supervised learning data.

This demonstrates that project characterization must include analytical purpose and desired claim type, not only structural data properties.

Causal inference also reveals missing-prerequisite activation when identification assumptions or estimands are absent.

---

## 24. Stress test: clustering

A segmentation request activates questions about the meaning of similarity, purpose of the clusters, variables that should define similarity, scale, stability, interpretability, and usefulness.

There may be no supervised target and no conventional predictive evaluation.

This case supports the question-centered architecture and shows that modules may create semantic obligations, not merely computational investigations.

---

## 25. Stress test: privacy and admissibility

Sensitive data alone may create candidate governance relevance.

Sensitive data plus a proposed external transfer plus unresolved permission creates a much stronger action-specific admissibility concern.

The output may be a blocked action, approval requirement, or required control rather than an analysis.

This case demonstrates that activated contributions have different authority and must remain governed by the project constitution rather than being treated as equal module opinions.

---

## 26. Stress test: novel domain-specific feedback loop

A system may discover that predictions influence interventions which then affect future training data.

No current module may fully represent the concern.

Open-ended reasoning should be able to create a novel concern and retrieve partially relevant reusable knowledge such as:

- distribution shift;
- selection bias;
- causal reasoning;
- monitoring;
- feedback systems.

If the concern recurs across projects, it may later justify a new reusable knowledge unit.

This validates the open-world design.

---

## 27. Knowledge retrieval may be compositional

A concern need not map to exactly one perfect module.

A temporal missingness problem may need both missing-data and temporal knowledge. A feedback-loop problem may combine causal, selection-bias, shift, and monitoring knowledge.

The library should therefore support compositional retrieval.

This also means the library may contain knowledge units at different granularities, including broad frameworks, cross-cutting safeguards, structural concerns, decision frameworks, governance knowledge, assurance knowledge, method-specific knowledge, and micro-rules.

`Knowledge module` should remain an umbrella concept until real projects reveal the most useful taxonomy.

---

## 28. Coverage review is required because the library is incomplete

A hybrid trigger system can still miss important concerns.

The project therefore needs a broad residual coverage mechanism that periodically asks:

> Given the current material project state, which important concerns are not represented by an active question, obligation, review, accepted resolution, or explicit irrelevance rationale?

This is not equivalent to executing every module.

It is an omission search.

Examples include:

- repeated patients with no active dependence reasoning;
- fully automated deployment with no operational risk reasoning;
- a long time span in a future-facing project with no temporal validity consideration.

This leads to the concept of an **orphaned material fact**: an important state fact with no reasoning consequence and no explicit explanation for why it is irrelevant.

---

## 29. Orphaned actions are the complementary failure mode

The inverse problem also matters.

A consequential action such as training a complex model should normally trace to a question, objective, obligation, risk reduction need, deliverable requirement, or accepted decision.

If it does not, it is conceptually an **orphaned action**.

Together these provide two powerful integrity checks:

```text
ORPHANED MATERIAL FACT
Important observation with no reasoning consequence.

ORPHANED ACTION
Consequential work with no state-based justification.
```

This links activation integrity with state-driven orchestration.

---

## 30. Review can use the same activation mechanism

Specialized reviewers need not form a fixed roster.

State patterns may activate review actions, for example:

```text
high-leverage weak validation assumption
    -> independent validation review
```

```text
consequential claim with one evidence path
    -> replication or independent review
```

```text
sensitive data plus external model API
    -> privacy/admissibility review
```

Review therefore becomes another state-driven action class subject to risk, assurance, and runnable-frontier logic.

---

## 31. Activation should interact with assurance and project intent

Knowledge determines what concerns and opportunities exist.

Risk-sensitive assurance determines how strongly consequential concerns need to be verified.

Project intent determines how far optional opportunities are explored.

For example, calibration reasoning may be relevant in two projects, but a high-impact automated intervention may require subgroup calibration, temporal stability checks, independent review, and monitoring, while a low-stakes exploratory analysis may not.

Similarly, a learning-focused project may intentionally explore many model families, while a speed-focused project may pursue only a small set of materially distinct alternatives.

Thus:

> **Knowledge defines the relevant analytical opportunity and obligation set; assurance and project optimization determine depth, review intensity, and resource allocation.**

---

## 32. Knowledge instances need reopen and satisfaction conditions

A concern should not remain permanently active once sufficiently resolved.

A project-specific knowledge instance may become satisfied for its current scope when its required questions, evidence, methodological safeguards, and decisions are adequately resolved.

It should still be reopenable when relevant dependencies change.

For example, a missing-data concern resolved under a complete production-data assumption should reopen if the production API later begins permitting missing values.

This is compatible with the dependency-aware change-propagation model from Checkpoint 4.

---

## 33. Activation must avoid recursive explosion

Because state updates can activate further knowledge, the system needs conceptual safeguards against uncontrolled expansion.

Candidate requirements include:

- deduplication;
- scope awareness;
- reuse of existing project-specific instances;
- cycle detection;
- idempotent activation where appropriate;
- distinction between candidate relevance and established applicability;
- already-satisfied applicability checks;
- importance or materiality thresholds;
- budget-aware expansion.

The goal is not to suppress legitimate cross-triggering, but to prevent the system from generating an ever-growing duplicate concern graph.

---

## 34. Activation provenance should be preserved

Every project-specific knowledge instance should be explainable.

The system should eventually be able to answer:

- what state triggered the concern;
- which activation mechanism detected it;
- what scope it applies to;
- whether applicability was established or merely suspected;
- which questions and obligations it created;
- how it was resolved;
- whether it later reopened.

This will be important for evaluating both false-positive and false-negative activation.

---

## 35. Activation quality itself becomes an evaluation target

A trigger system has symmetrical failure modes:

```text
false-positive activation
irrelevant concern activated and resources wasted

false-negative activation
important concern never becomes represented
```

Future system evaluation should therefore include:

- important concerns correctly activated;
- important concerns missed;
- irrelevant knowledge activated;
- time and compute spent on unnecessary investigations;
- delay before critical issues are detected;
- whether coverage review recovers missed concerns.

Real projects should eventually become regression tests for this behavior.

---

## 36. Reusable knowledge itself needs provenance and maturity

The system should not treat its own knowledge library as unquestionable truth.

Reusable knowledge may eventually need metadata such as:

- rationale;
- references;
- scope;
- known limitations;
- version;
- maturity;
- project cases in which it was tested;
- known failure modes;
- supersession history.

This connects the project's design-maturity model to the future analytical knowledge library.

The exact representation remains unresolved and becomes the next design frontier.

---

## 37. Current conceptual activation loop

The strongest current formulation is:

```text
CURRENT PROJECT STATE
        |
        +--> new observation
        +--> proposed action / method / claim / decision
        +--> missing prerequisite
        +--> contradiction
        +--> risk or governance condition
        +--> dependency revision
        +--> novel concern
                    |
                    v
             RELEVANCE DETECTION
      deterministic rules + semantic retrieval
            + interpretive reasoning
                    |
                    v
            APPLICABILITY CHECK
                    |
                    v
       PROJECT-SPECIFIC KNOWLEDGE INSTANCE
                    |
                    v
       questions / obligations / safeguards /
       evidence needs / reviews / candidate actions
                    |
                    v
               PROJECT STATE
                    |
                    v
            RUNNABLE FRONTIER
                    |
                    v
       execution / reasoning / review / human input
                    |
                    v
            evidence and state revision
```

A coverage-review process surrounds this loop to search for missed material concerns.

---

## 38. Emerging durable semantic layers

Without selecting implementation technology, the system now appears to need at least these conceptual layers:

```text
PROJECT STATE
What is currently true, uncertain, required, decided,
risky, invalid, blocked, and unresolved?

KNOWLEDGE LIBRARY
What recurring concerns, safeguards, decision frameworks,
failure modes, and evidence requirements exist?

ACTIVATION LAYER
Which pieces of reusable knowledge are relevant to the
current state or proposed transition?

ORCHESTRATION
Which resulting runnable action should happen next?

EXECUTION / REASONING / REVIEW
Perform the work and produce evidence.

STATE UPDATE
Record results, propagate impact, and recompute relevance.
```

The project still has not selected any rule engine, retrieval system, graph technology, agent framework, workflow engine, or module storage format.

---

## 39. Strong hypotheses resulting from this foundation

The following are now strong design hypotheses:

1. Reusable knowledge should be separate from actors and tools.
2. Reusable definitions and project-specific knowledge instances should be distinct.
3. Activation should add structured reasoning obligations to state rather than directly execute workflows.
4. Activation may be deterministic, interpretive, or open-ended.
5. Activation can originate from observations, proposals, missing prerequisites, contradictions, risk, governance, or state revisions.
6. Prospective activation should validate consequential proposed actions, methods, decisions, and claims before they are accepted or executed.
7. Knowledge units should consume relevant state slices and write typed contributions back into state.
8. Modules should interact primarily through shared state rather than direct calls.
9. Shared questions should reconcile overlapping module contributions.
10. Knowledge should encode evidence requirements and conditional reasoning rather than cookbook prescriptions.
11. Knowledge instances need explicit scope, applicability, satisfaction, and reopen behavior.
12. The knowledge library must be open-world and compositional.
13. Coverage review is needed to detect missed activations.
14. Orphaned material facts and orphaned actions are promising integrity checks.
15. Review can participate in the same state-driven activation model.
16. Activation quality must itself be evaluated and improved through project cases.

These remain design hypotheses pending real-project stress testing and eventual implementation experiments.

---

## 40. Explicit non-decisions

This foundation does **not** select:

- a formal module schema;
- a module taxonomy;
- a trigger language;
- a rule engine;
- semantic retrieval technology;
- an embedding model;
- a graph database;
- a workflow framework;
- an agent framework;
- activation thresholds;
- relevance scores;
- scope representation;
- deduplication algorithm;
- coverage-review implementation;
- module versioning format;
- or a final knowledge maturity model.

---

## 41. Next conceptual question

The next design problem is the internal representation of reusable knowledge itself:

> **What should a reusable knowledge unit contain so that, once activated, it can reliably generate the right questions, safeguards, evidence requirements, candidate investigations, review behavior, resolution criteria, and state transitions across heterogeneous projects?**

This should be developed before selecting the concrete storage or execution format for knowledge modules.
