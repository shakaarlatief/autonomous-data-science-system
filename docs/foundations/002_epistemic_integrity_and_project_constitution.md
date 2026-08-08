# Epistemic Integrity and the Project Constitution

**Status:** Foundational design memo  
**Date:** 2026-08-08  
**Origin:** Design Session 01, after Checkpoint 1  
**Authority:** Rationale and design history. Current canonical documents take precedence if later revisions conflict with this memo.

## Why this memo exists

After Checkpoint 1, the design discussion moved from the project's primary purpose to the question of what must remain non-negotiable when the system adapts itself to different project goals.

The starting point was a concern that configurability could accidentally make methodological validity configurable. A fast project may reasonably use fewer models, less extensive tuning, a shorter report, or less exploratory breadth. It should not become acceptable to leak validation information, tune repeatedly on a final test set, use an evaluation design that does not represent the intended use, or make claims stronger than the evidence supports merely because speed was prioritized.

The resulting discussion produced a more structured view of project quality. The current hypothesis is that the system should not use one flat mandatory checklist. Instead, it should operate inside a set of methodological, admissibility, and assurance constraints while optimizing project-specific value within those boundaries.

This memo preserves the detailed reasoning behind that hypothesis.

## 1. A quality floor should constrain validity rather than prescribe one workflow

A non-negotiable quality floor should not mean that every project performs the same analyses.

Two projects may legitimately differ in:

- number of models explored;
- hyperparameter-search depth;
- exploratory-data-analysis breadth;
- feature-engineering breadth;
- robustness-analysis depth;
- review intensity;
- reporting length;
- interpretability work;
- mathematical explanation depth;
- compute expenditure;
- and human involvement.

The project-relative objective established at Checkpoint 1 can therefore be expressed conceptually as:

```text
maximize project value
subject to methodological and other hard constraints
```

Project intent determines what is worth optimizing. The quality floor determines which processes and conclusions are admissible at all.

## 2. Universal requirements and conditional invariants

The discussion distinguished two different kinds of non-negotiable requirements.

### Universal integrity requirements

These apply broadly regardless of project type. Examples include not fabricating evidence, not hiding material uncertainty, and not presenting unsupported claims as established facts.

### Conditional methodological requirements

These become mandatory when project facts activate them.

Examples include:

- if prediction occurs through time, future information must not leak backward into the represented decision point;
- if repeated entities make ordinary random splitting optimistic relative to deployment, evaluation must account for the entity structure;
- if a final test set is intended to provide an unbiased final estimate, it must not repeatedly become part of the development feedback loop;
- if preprocessing learns parameters from data, those parameters must be estimated using only information legitimately available inside the relevant training portion of evaluation;
- if a causal conclusion is requested, evidence and assumptions must support a causal interpretation rather than only predictive association;
- if missingness is expected in production, the missing-data strategy must be compatible with that production setting.

This leads to an important principle of design: a rule can be non-negotiable when activated without being universally applicable to every project.

## 3. The initial search for deeper invariants

Rather than encoding hundreds of disconnected rules, the discussion searched for deeper principles that could explain why those rules exist.

A recurring conceptual chain emerged:

```text
project meaning
    -> legitimate information
    -> valid analytical procedure
    -> evidence
    -> claim
    -> traceable project state
```

If one link is invalid, a polished downstream result is not enough to rescue the conclusion.

The current strong design hypothesis is that five epistemic invariants may form the core of the system's methodological constitution.

## 4. Invariant 1: semantic validity

### Working definition

> **An analysis has semantic validity only when the analytical object being estimated, predicted, described, compared, or optimized corresponds sufficiently to the actual project question and intended use.**

The system therefore needs enough understanding, at the point where it matters, of questions such as:

- what one observation represents;
- what the target or analytical object means;
- who or what the analysis concerns;
- when prediction or inference occurs;
- what population or environment matters;
- what time horizon matters;
- what action or decision follows from the output;
- and what kind of conclusion is actually being requested.

The phrase "sufficiently" is deliberate. The system does not require complete domain knowledge before harmless descriptive operations such as reading column names. The required semantic certainty should increase with the consequence of the decision being made.

### Example

A churn model may be technically flawless while still answering the wrong question if the intended target is "will the customer churn within the next 30 days?" but the dataset label means "has the customer ever churned historically?"

The failure is semantic, not computational.

## 5. Invariant 2: information legitimacy

### Working definition

> **Every analytical step may use only information legitimately available to that step under the project conditions the step is intended to represent.**

Conceptually, each analytical step `s` has an allowed information set `I_s`. Inputs that influence the step should belong to that legitimate information set.

This unifies many forms of leakage that are often taught as separate rules:

- target leakage;
- future-information leakage;
- preprocessing fitted across validation folds;
- target encoding fitted using held-out outcomes;
- repeated use of a final test set for development decisions;
- inappropriate information sharing across groups;
- and some forms of post-treatment adjustment in causal analysis.

The deeper issue is not a library-specific rule. It is whether information entered the analytical process before it was legitimately available in the situation the analysis is meant to simulate.

### Important consequence

There is no universal rule that the complete dataset may never be used. A purely retrospective descriptive analysis may legitimately use the full observed dataset. A transformation intended to be applied to future observations may require a training/deployment distinction. Information legitimacy is therefore relative to the epistemic role of the analytical step.

## 6. Invariant 3: evidence validity

### Working definition

> **Evidence is valid only when the procedure used to produce it is appropriate for the question being investigated, its material assumptions are adequately satisfied or acknowledged, and the executed computation faithfully implements the intended procedure.**

The discussion identified several components:

```text
evidence validity
    = design fit
    + assumption adequacy
    + execution fidelity
    + appropriate uncertainty treatment
```

This is a conceptual decomposition rather than a numerical formula.

### Failure modes

**Wrong design:** random validation is used when the intended use is genuinely future forecasting.

**Assumption failure:** an inferential procedure relies on independence while material dependence is ignored.

**Execution failure:** the reasoning specifies fold-specific preprocessing but the code fits preprocessing globally.

**Uncertainty failure:** two methods are treated as meaningfully different although the evaluation design is too noisy to support that conclusion.

Execution fidelity was considered as a possible sixth invariant. The current view is that it may fit naturally inside evidence validity, but this should be tested further.

## 7. Invariant 4: claim validity

### Working definition

> **A claim is valid only when its content, strength, scope, and certainty do not exceed what is supported by the available evidence together with the assumptions on which that evidence depends.**

The discussion distinguished four dimensions.

### Content

Is the system claiming description, association, prediction, ranking quality, structural interpretation, or causality?

### Strength

Is the evidence suggestive, supportive, strong, or genuinely decisive?

### Scope

Does the evidence concern these observations, similar future observations, a target population, another geography, all subgroups, or a different deployment environment?

### Certainty

How confident should the system sound given the evidence and uncertainty?

This invariant is especially important because language models can transform weak or local evidence into authoritative prose. The system should actively prevent claims from outrunning the evidence.

Examples include:

- a cross-sectional association does not automatically establish causality;
- good cross-validation under one data-generating regime does not establish robustness to arbitrary distribution shift;
- strong average performance does not establish strong performance for every subgroup;
- a 0.001 metric difference with substantial fold variation does not automatically establish meaningful superiority;
- calibration on historical validation data does not guarantee future calibration after deployment drift.

## 8. Invariant 5: traceability and dependency integrity

### Working definition

> **Every consequential analytical result, claim, or decision should have sufficient provenance to identify the data, assumptions, procedures, computations, evidence, and upstream decisions on which it depends, and changes to those dependencies should make affected downstream conclusions discoverable.**

This contains two related ideas.

### Reproducibility

Can the result be reconstructed from its data, code, configuration, preprocessing, validation design, model, and other relevant state?

### Dependency integrity

If an upstream assumption, feature, data version, split, or analytical result becomes invalid, can the system determine which downstream experiments, decisions, claims, and artifacts may now be stale?

For example:

```text
leakage discovered in feature F-12
    -> preprocessing run P-03 becomes invalid
    -> experiments E-21 through E-47 become invalid
    -> model comparison D-08 must be reopened
    -> report claims C-14, C-15, and C-19 become stale
```

This is deeper than ordinary experiment logging. A revisable scientific process needs to know not only how to reproduce a result, but also what depends on it.

## 9. The five invariants answer different questions

The current boundaries are:

| Invariant | Core question |
| --- | --- |
| Semantic validity | Are we answering the right question? |
| Information legitimacy | Did we use only information we were legitimately allowed to use? |
| Evidence validity | Did our procedure validly generate evidence about that question? |
| Claim validity | Are we saying only what that evidence justifies? |
| Traceability and dependency integrity | Can we reconstruct why we believe this, and what depends on it? |

This separation appears to compress many concrete rules without reducing them to vague slogans.

## 10. Stress tests across project types

The five-invariant hypothesis was tested conceptually across several kinds of data-science work.

### Classification

Semantic validity defines the target, population, prediction point, and intended use. Information legitimacy governs target leakage, future information, fold leakage, and test feedback. Evidence validity governs validation design and execution. Claim validity limits performance claims to the evaluated setting. Traceability links the result to the data, split, preprocessing, model, and metric.

### Forecasting

Semantic validity defines the forecast variable, horizon, forecast origin, and intended use. Information legitimacy excludes information unavailable at forecast origin. Evidence validity requires a backtesting design appropriate to the forecast task. Claim validity prevents historical backtest performance from being treated as guaranteed future stability. Traceability links conclusions to windows, horizons, data versions, and model specifications.

### Causal inference

Semantic validity defines treatment, outcome, estimand, population, and intervention. Information legitimacy constrains inappropriate post-treatment information. Evidence validity concerns identification strategy, assumptions, specification, and inference. Claim validity prevents associations from being upgraded to causal effects without justification. Traceability links causal conclusions to identifying assumptions and specifications.

### Clustering

Semantic validity asks why the grouping is being produced. Information legitimacy depends on whether the goal is retrospective description or future assignment. Evidence validity concerns representation, distance, stability, sensitivity, and the suitability of the clustering procedure. Claim validity prevents an algorithmic partition from automatically being described as objectively existing natural customer types. Traceability connects the segmentation to preprocessing and clustering choices.

### Recommendation, anomaly detection, dimensionality reduction, and other settings

The same reasoning structure appears to generalize when the analytical question and intended use are explicitly specified.

This supports the view that the epistemic core should be expressed relative to analytical questions rather than particular model families.

## 11. The analytical question as a central object

A major consequence of the stress test is that validity is always validity **for a question**.

There is no universally valid model, split, metric, or experiment in isolation.

The system may therefore need an explicit conceptual representation of an analytical question containing information such as:

```text
What are we trying to learn or decide?
What analytical object is involved?
    prediction
    forecast
    parameter
    causal effect
    ranking
    grouping
    distribution
    anomaly
    other
For what population or environment?
At what time or horizon?
For what intended use?
What strength of conclusion is desired?
```

This is not yet a schema decision.

## 12. Questions and claims may be more fundamental than models and stages

The discussion produced a strong hypothesis that the system should primarily manage questions and claims rather than merely models or pipeline stages.

A conceptual project loop becomes:

```text
project
  -> important questions
  -> candidate investigations
  -> evidence
  -> claims and decisions
  -> new questions
```

Example:

```text
Question:
Does missingness contain predictive information?

Investigation:
Compare missingness patterns and evaluate missingness indicators.

Evidence:
Distribution analysis plus validation results.

Claim:
The indicator improves discrimination modestly under the current validation design.

Decision:
Retain the indicator.

New question:
Is the same missingness mechanism expected in production?
```

This view naturally supports backward movement and dynamic activation.

## 13. Possible question states

The discussion considered, but did not finalize, possible epistemic states for project questions:

```text
OPEN
ASSUMED
SUPPORTED
DISPUTED
INCONCLUSIVE
BLOCKED
INVALIDATED
CLOSED
```

A project may eventually be considered complete when all questions required by its validity, admissibility, assurance, and deliverable obligations are either sufficiently resolved, explicitly accepted as residual uncertainty, or documented as impossible to resolve under the available conditions.

This is a design hypothesis, not a finalized state machine.

## 14. Project-defining, validity, and value-improving questions

The discussion also identified three useful categories.

### Project-defining questions

These establish what the project actually means.

Examples include target definition, prediction timing, intended population, and intended action.

### Validity questions

These determine whether the available evidence can support the project.

Examples include feature availability at prediction time, split validity, repeated-entity leakage, or identifying assumptions.

### Value-improving questions

These may improve the project but need not always be pursued.

Examples include testing another boosting family, trying additional transformations, or building an ensemble.

This distinction could eventually help orchestration. The system should not spend large resources on optional value-improving work while unresolved project-defining or validity questions remain capable of invalidating the project.

## 15. What happens when validity cannot be established?

Autonomy should not mean always continuing.

The discussion identified several legitimate responses when an epistemic condition cannot currently be satisfied:

```text
RESOLVE
Gather more evidence or perform another investigation.

RESEARCH
Obtain external information.

ASK
Request human or domain clarification.

RESTRICT
Continue with a weaker or narrower claim.

BRANCH
Carry multiple plausible assumptions or interpretations forward.

STOP
Decline to make the requested conclusion because validity cannot be established.
```

A strong system may therefore reduce the scope of the requested deliverable rather than lower its methodological standard.

Example:

```text
Cannot responsibly provide:
"production-ready forecasting model"

Can provide:
"preliminary exploratory baseline"

Reason:
insufficient temporal history for credible production-oriented validation
```

This led to the candidate principle:

> **When project objectives and hard validity constraints conflict, degrade scope rather than integrity.**

This principle is not yet promoted to canonical status and should be tested on real cases.

## 16. Why the epistemic core is not the whole project constitution

The five invariants appear to capture many concerns that initially seemed separate.

Statistical uncertainty can often be handled through evidence validity and claim validity. Generalization and robustness depend on whether the evaluation represents the intended environment and whether claims exceed that evidence. Reproducibility is a component of traceability. Execution fidelity can likely be incorporated inside evidence validity.

However, ethics, law, privacy, policy, and some forms of safety expose a fundamentally different dimension.

A project can be epistemically excellent and still use prohibited information, violate privacy requirements, create unacceptable discriminatory consequences, or take an unsafe action.

The system therefore needs to distinguish:

```text
VALIDITY
Can we justify this belief or conclusion?

ADMISSIBILITY
Are we permitted or willing to perform this action or use the result in this way?
```

These can fail independently.

## 17. Admissibility, epistemic integrity, and assurance

The emerging conceptual hierarchy is:

```text
ADMISSIBILITY
    Is the action, data use, or intended outcome permissible?

EPISTEMIC INTEGRITY
    Is the reasoning and evidence defensible?

RISK-SENSITIVE ASSURANCE
    How much verification, review, replication, and control is required before proceeding?

PROJECT OPTIMIZATION
    Within those boundaries, how should project value be maximized?
```

Hard external project constraints may cut across these layers.

The distinction between correctness and assurance is especially important. The system cannot guarantee that every decision is correct. It can control how much justified confidence is required before proceeding.

Higher-risk projects may require stronger assurance through mechanisms such as:

- more extensive validation;
- independent review;
- replication;
- subgroup analysis;
- stronger robustness analysis;
- human approval;
- deployment safeguards;
- monitoring;
- fallback plans;
- and stricter documentation.

The exact risk model is not yet defined.

## 18. Fairness illustrates why layers should not be conflated

Fairness can contain multiple questions at once.

Whether a chosen fairness metric is satisfied is an evidence question. Whether that fairness criterion is appropriate is a normative or domain decision. Whether the resulting use is legally acceptable is a governance question. Whether subgroup estimates are too uncertain is an evidence-validity question.

This is a reason to avoid creating broad topic modules that silently conflate mathematical, legal, policy, ethical, and operational questions.

## 19. Current project-constitution hypothesis

The current high-level hypothesis is:

```text
Project constitution
    |
    +-- Admissibility constraints
    |     ethics, privacy, law, policy, safety, explicit user rules
    |
    +-- Epistemic integrity
    |     semantic validity
    |     information legitimacy
    |     evidence validity
    |     claim validity
    |     traceability and dependency integrity
    |
    +-- Risk-sensitive assurance
    |     required verification, review, replication, human control
    |
    +-- Hard project constraints
    |     external operational or resource constraints that cannot be violated
    |
    +-- Project optimization
          predictive quality, learning value, speed, interpretability,
          report depth, simplicity, compute, human effort, production quality,
          exploration breadth, and other project-relative objectives
```

"Project constitution" is currently a mental model rather than an implementation name.

## 20. Relationship to the original adaptive-system hypothesis

This reasoning strengthens the earlier idea that the system should not ask only "what pipeline stage comes next?"

A stronger process asks:

```text
What question are we trying to resolve?
What do we currently know?
What information is legitimate?
What validity and admissibility constraints apply?
What remains uncertain?
Which investigations are mandatory?
Which investigations are optional but valuable?
How much assurance does project risk require?
Given the remaining resources and objectives, where should additional effort be spent?
```

This is closer to an autonomous scientific process than a fixed modelling pipeline.

## 21. Current status of the ideas in this memo

### Strong design hypotheses

- The quality floor should be expressed as methodological constraints and conditional invariants rather than one mandatory checklist.
- Five invariants may form the epistemic core: semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.
- Execution fidelity likely belongs inside evidence validity rather than requiring a separate invariant.
- Analytical questions and claims may be more fundamental orchestration objects than models and stages.
- Questions may need explicit epistemic states.
- The broader project constitution may require separate admissibility, epistemic-integrity, and risk-sensitive-assurance layers.
- Project risk should primarily change required assurance, not the meaning of valid evidence.
- When hard validity requirements conflict with project objectives, the system should reduce scope rather than silently lower integrity.

### Not yet decided

- Whether the five invariants are complete.
- Exact definitions and machine representations.
- Exact admissibility scope.
- Whether the system itself reasons about law, ethics, privacy, policy, and safety or receives some of these as externally supplied constraints.
- Exact risk taxonomy or assurance levels.
- Exact question-state model.
- Exact project-completion rule.
- Exact dependency graph or provenance architecture.
- Exact implementation architecture.

## 22. Next design question

The next major question is the other half of the project constitution:

> **What exactly should the admissibility layer contain, and how much of ethics, privacy, law, safety, user policy, and external constraints should the data-science system itself reason about versus receive as hard constraints?**

This should be explored before the five-invariant epistemic framework is promoted from a strong design hypothesis into a more formal specification.
