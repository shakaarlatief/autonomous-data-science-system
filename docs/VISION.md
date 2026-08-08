# Vision

## Purpose

The Autonomous Data Science System project aims to design a more rigorous way to conduct data science with large language models than a single end-to-end conversational workflow.

Modern LLMs can already perform substantial portions of a data project: inspect a dataset, write code, run analyses, perform exploratory data analysis, preprocess data, choose baseline models, fit multiple model classes, validate and compare models, evaluate results, generate predictions, and write reports.

That capability is powerful, but it does not imply that giving one LLM a broad task such as "complete this data project from A to Z" produces the best possible scientific or engineering process.

The project begins from the observation that data science contains many interacting decisions. A model can make a choice that is technically defensible but poorly suited to the project, overlook a relevant alternative, accept an assumption too quickly, interpret a pattern incorrectly, use an evaluation design that does not match deployment, fail to revisit earlier work after a later discovery, or generate a polished answer without enough empirical support.

The goal is therefore to improve the **structure of the reasoning process itself**.

## Working vision

The intended system is a rigorous, adaptive, semi-autonomous environment that can manage a data science project as a scientific process rather than as one long sequence of LLM responses.

A mature version should be able to:

- understand the project objective and intended use of predictions;
- characterize the dataset and the data-generating or collection process;
- identify relevant risks, assumptions, and unanswered questions;
- determine which analytical investigations are relevant to the specific project;
- plan and execute code-based experiments;
- compare reasonable alternatives rather than prematurely selecting one approach;
- distinguish claims supported by evidence from hypotheses or judgment;
- challenge important conclusions through review or independent analysis;
- revisit earlier stages when new findings change the interpretation of the problem;
- involve the human when goals, semantics, trade-offs, or other consequential judgments require human input;
- preserve decisions, assumptions, evidence, rejected alternatives, and unresolved questions;
- control the depth and cost of analysis according to the needs of the project;
- produce reproducible code, experiments, reports, and final artifacts;
- and learn from completed projects by extracting generalizable improvements into the system itself.

## Primary purpose: the best process for the particular project

The project now adopts the following working purpose:

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

This rejects the idea that every project should optimize the same universal objective.

Maximum predictive performance, maximum automation, maximum analytical depth, minimum cost, and maximum speed can all be valuable, but none is automatically the highest-level objective for every project.

A portfolio project may prioritize learning value, technical breadth, and detailed reporting. A production project may prioritize reliability, maintainability, latency, and deployment readiness. A rapid exploratory project may prioritize speed. A research-oriented project may prioritize robustness, uncertainty analysis, and methodological depth.

The system should therefore adapt the process to project intent rather than forcing every project through the same notion of success.

A strong current design hypothesis is that this configurability should operate **inside a non-negotiable methodological quality floor**. Project priorities may change the amount and type of work, but should not make invalid methodology acceptable. The exact content of this quality floor is not yet defined.

## Project intent as a structured concept

A promising conceptual direction is to distinguish several kinds of project instructions rather than compressing them into one vague mode.

Possible categories include:

- **objectives**, describing what the project should prioritize;
- **constraints**, describing limits the project must operate under;
- **deliverables**, describing the outputs that must be produced;
- **human-control preferences**, describing how and when the system should involve the user.

Named modes such as `QUICK`, `STANDARD`, or `RESEARCH` may later be useful as presets, but they should probably map to a richer project-intent profile rather than define the underlying architecture.

The project has also identified a potentially important distinction between project-level objectives, model-level objectives, and operational objectives. These can conflict, so a mature system should avoid reducing all project success to a single model metric.

These ideas are currently strong design hypotheses, not finalized schemas or implementation commitments.

## Not simply a collection of agents

The project is not based on the assumption that adding more agents automatically produces better data science.

A weak multi-agent system could simply generate several opinions and then ask another LLM to summarize them. That would reproduce many of the same weaknesses as a single-LLM workflow while adding cost and complexity.

The intended value should come from the combination of:

- explicit responsibilities;
- structured project state;
- reusable data science knowledge;
- empirical execution;
- deterministic or rule-based safeguards where appropriate;
- review and disagreement mechanisms;
- evidence requirements;
- provenance;
- and carefully chosen human decision points.

The LLMs are components of the system, not the system itself.

## A scientific-process perspective

A useful conceptual framing is:

> **An AI-managed scientific process for data projects.**

The system should repeatedly move through a pattern such as:

```text
question
  -> investigation
  -> execution
  -> evidence
  -> interpretation
  -> review
  -> decision
  -> updated project state
  -> new questions when necessary
```

This is intentionally different from a rigid sequence such as:

```text
EDA -> preprocessing -> modelling -> evaluation -> report
```

Those conventional stages remain useful organizational concepts, but they should not constrain the reasoning process. A finding during error analysis may require new EDA. A validation failure may require redefining the split strategy. A newly discovered repeated-entity structure may require group-aware validation. A production assumption may change the correct missing-data strategy. The system therefore needs to support iteration and backward movement.

## Project diversity as a central design problem

Different data science projects require different questions, assumptions, methods, and validation structures.

Examples include:

- ordinary IID tabular classification;
- regression;
- highly imbalanced classification;
- grouped or repeated-entity data;
- temporal prediction and forecasting;
- panel data;
- sequence modelling;
- recommender systems;
- causal analysis;
- image or text modelling;
- probabilistic modelling;
- and many other specialized settings.

Even apparently small topics can contain many conditional branches. Missing data is an early example: the appropriate action depends on whether features or labels are missing, whether missingness occurs in production, whether clean validation data can be obtained, whether deleting rows changes the effective population, the type of the variable, the amount and pattern of missingness, and the consequences for downstream evaluation.

The system therefore cannot simply encode one universal project pipeline.

## Working hypothesis: adaptive knowledge and reasoning

A promising direction is a hybrid system in which reusable knowledge structures encode recurring data science considerations, while open-ended reasoning remains available for novel or poorly structured situations.

A possible conceptual cycle is:

```text
observation
    -> project fact
    -> trigger
    -> relevant investigation or knowledge module
    -> evidence
    -> decision
    -> new project facts
    -> new triggers
```

This could allow the system to maintain a large universe of possible considerations without executing all of them for every project.

For example, discovery of a timestamp may activate temporal checks. Repeated entity identifiers may activate grouped validation checks. Missing values may activate a missing-data investigation. Unexpected performance decay over time may activate drift analysis and potentially force reconsideration of the validation design.

This is currently a **design hypothesis**, not a selected implementation architecture.

## Three broad forms of reasoning

The initial design discussion suggests that a mature system may need to combine three broad forms of knowledge or reasoning.

### 1. Hard constraints

Some practices should not depend on LLM creativity once their conditions are known.

Examples include preventing test-set information from leaking into training preprocessing, preserving temporal ordering where future information would otherwise leak backward, and avoiding repeated model selection on a final test set.

### 2. Explicit decision frameworks

Many questions do not have one universal answer, but the relevant considerations are known.

Missing-data handling is a good example. The system can explicitly represent the questions that should be asked, evidence that should be collected, reasonable strategies, and conditions under which different strategies become appropriate.

### 3. Open-ended reasoning

Some project questions cannot realistically be enumerated in advance.

Examples include understanding unusual domain-specific patterns, generating hypotheses for unexplained subgroup behaviour, interpreting surprising relationships, identifying hidden business-process semantics, or determining whether an external event could explain a structural change.

These situations require flexible reasoning, research, experimentation, and sometimes human input.

The long-term system will probably need all three.

## Human role

The objective is not to eliminate the human from the process.

A stronger objective is:

> **Use human attention where human judgment creates the most value.**

The system should be able to continue autonomously through routine or well-defined work while escalating questions that materially affect the meaning or validity of the project.

Possible human gates include:

- ambiguous prediction objectives;
- unclear production conditions;
- uncertain feature semantics;
- choices involving business or scientific trade-offs;
- decisions about acceptable false-positive and false-negative costs;
- ethical or policy considerations;
- choices among materially different modelling objectives;
- and situations where evidence remains genuinely inconclusive.

The exact boundary between autonomous and human-controlled decisions remains an open design question.

## Evidence over rhetorical agreement

An important ambition of the system is to reduce the tendency to settle analytical questions through persuasive language alone.

If one reasoning component proposes removing a feature and another component objects, the system should prefer an empirical comparison when the question can be tested. If two preprocessing strategies are plausible, the system should compare them under an appropriate validation design when feasible. If a model appears better, the system should examine whether the improvement is stable, meaningful, and obtained without leakage.

LLM reasoning is useful for proposing hypotheses, identifying risks, interpreting results, and planning experiments. It should not automatically be treated as the final evidence for empirical claims.

## Review and independent criticism

The system should make important conclusions challengeable.

Possible mechanisms include:

- a separate reviewer that inspects methodology rather than merely the final metric;
- specialized reviews for leakage, validation, statistics, or deployment assumptions;
- proposer-reviewer separation;
- independent re-analysis that does not receive the original conclusion;
- and automatic invalidation or rerunning of experiments when methodological flaws are discovered.

The correct amount of review should depend on risk, project depth, and resource budget.

## Persistent project state

A mature system should not depend on remembering a long conversational transcript.

A project state may eventually track concepts such as:

- objective and deployment setting;
- dataset and data version;
- assumptions;
- decisions and rationale;
- rejected alternatives;
- experiments and results;
- validation design;
- unresolved questions;
- evidence supporting important claims;
- confidence or uncertainty;
- human approvals;
- invalidated experiments;
- and current next actions.

The exact storage representation has not been selected.

## Configurable depth and efficiency

A sophisticated system should not equate quality with executing every imaginable analysis.

The system should eventually be able to vary depth according to project needs. A quick exploratory project may need basic checks and a few baselines. A serious research or production project may justify broad ablation studies, independent review, robustness analysis, calibration, subgroup evaluation, and more extensive documentation.

The current direction is that depth should emerge from project intent, resource constraints, risk, uncertainty, and expected analytical value rather than from one rigid universal workflow.

An important related hypothesis is that additional effort should be allocated where it is most likely to improve validity, reduce consequential uncertainty, or change downstream decisions. The system should not spend resources merely because more analysis is possible.

The specific prioritization mechanism remains open.

## Learning from projects

Real projects should play two roles:

1. produce useful project outputs; and
2. test the current data science system.

When a project reveals that the system missed an important issue, performed unnecessary work, asked the wrong question, or lacked an appropriate reasoning branch, the lesson should be examined for generality.

If generalizable, it should become a reusable improvement such as:

- a new knowledge module;
- a new trigger;
- a new review rule;
- a new test case;
- a new system constraint;
- or a revision to an existing decision framework.

This makes system development cumulative rather than project-specific.

## Long-term intellectual asset

The most valuable result may not be a particular orchestration framework or collection of agents.

Models and software frameworks will change. The durable asset could instead be an explicit and executable representation of data science reasoning:

- which questions matter;
- under which conditions they matter;
- what evidence is needed;
- what alternatives should be considered;
- what common mistakes should be prevented;
- when one finding should trigger another investigation;
- how uncertainty should be represented;
- and when human judgment is required.

This repository is intended to gradually develop that asset.

## Current boundary of the vision

This document describes the direction of the project, not a final specification.

The next design task is to define what belongs in the non-negotiable methodological quality floor and what should remain configurable according to project intent. The broader goals, requirements, success criteria, boundaries, and evaluation standards will continue to be developed before a concrete architecture and implementation stack are selected.
