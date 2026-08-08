# Current State

## Checkpoint

**Checkpoint:** 2  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Working project definition

The Autonomous Data Science System is intended to become a rigorous, adaptive, semi-autonomous system for carrying out data science projects with multiple reasoning responsibilities, executable tools, persistent knowledge, explicit review processes, empirical evidence, and human judgment.

The system should eventually be able to begin with a new data project, understand the problem, inspect and characterize the data, determine which questions and risks are relevant, plan investigations, execute code, evaluate evidence, compare alternatives, revisit earlier assumptions when necessary, involve the human at appropriate decision points, preserve project state, and produce reproducible analytical and reporting artifacts.

The accepted primary purpose remains:

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed are therefore not universal objectives. They are project-dependent priorities or means that should serve the broader project intent.

## Major development since Checkpoint 1

The project has substantially refined the idea of a non-negotiable methodological quality floor.

The current strong hypothesis is that project-specific optimization should occur inside a broader project constitution rather than inside one flat mandatory checklist.

The emerging hierarchy is:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

Hard external project constraints may cut across these layers.

This is a conceptual design hypothesis, not a selected implementation architecture.

## Candidate epistemic core

The project currently has a strong five-invariant hypothesis for epistemic integrity.

### 1. Semantic validity

The analytical object being predicted, estimated, described, compared, or optimized should correspond sufficiently to the actual project question and intended use.

Core question:

> **Are we answering the right question?**

### 2. Information legitimacy

Every analytical step should use only information legitimately available to that step under the conditions the analysis is intended to represent.

Core question:

> **Did we use only information we were legitimately allowed to use?**

This concept may unify target leakage, temporal leakage, preprocessing leakage, test-set feedback, and several related failures.

### 3. Evidence validity

The procedure should be appropriate for the question, its material assumptions should be adequately satisfied or acknowledged, and the executed computation should faithfully implement the intended procedure.

Core question:

> **Did our procedure validly generate evidence about that question?**

Execution fidelity is currently treated as a likely component of evidence validity rather than a separate invariant.

### 4. Claim validity

The content, strength, scope, and certainty of a claim should not exceed what the evidence and supporting assumptions justify.

Core question:

> **Are we saying only what the evidence justifies?**

### 5. Traceability and dependency integrity

Consequential results, claims, and decisions should be reconstructable and connected to the data, assumptions, procedures, computations, evidence, and upstream decisions on which they depend.

Core question:

> **Can we reconstruct why we believe this, and what depends on it?**

The dependency aspect matters because later discoveries may invalidate earlier results and require downstream conclusions or artifacts to become stale.

## Status of the five-invariant framework

The framework has survived conceptual stress tests across classification, forecasting, causal inference, clustering, anomaly detection, dimensionality reduction, and recommendation-style settings.

It has not yet been systematically tested on real projects or converted into precise requirements.

It therefore remains a **strong design hypothesis**, not a finalized specification.

Detailed reasoning is preserved in:

`docs/foundations/002_epistemic_integrity_and_project_constitution.md`

## Universal requirements versus conditional obligations

The quality floor should not become a universal checklist of analyses.

The current view distinguishes:

1. **Universal integrity requirements**, which apply broadly.
2. **Conditional methodological obligations**, which become mandatory when project facts activate them.

For example, temporal-information restrictions are mandatory when the project represents prediction through time but are irrelevant to a purely static retrospective description.

This preserves both rigor and adaptivity.

## Analytical questions as a possible central abstraction

A strong design hypothesis is that the system should primarily manage analytical questions and claims rather than merely models or pipeline stages.

Conceptually:

```text
project
  -> important questions
  -> investigations
  -> evidence
  -> claims and decisions
  -> new questions
```

A future analytical-question representation may need concepts such as:

- what is being learned or decided;
- analytical object;
- population or environment;
- time or horizon;
- intended use;
- desired strength of conclusion.

No machine representation has been selected.

## Candidate question categories and states

Three conceptual question categories have emerged:

- **project-defining questions**, which establish what the project means;
- **validity questions**, which determine whether available evidence can support the project;
- **value-improving questions**, which may improve outcomes but are not always mandatory.

Possible question states discussed include:

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

These are design hypotheses, not a finalized state machine.

## When validity cannot be established

Autonomy should not mean always continuing.

The system may need to respond by:

- resolving the uncertainty with more evidence;
- researching external information;
- asking the human or a domain source;
- restricting the intended conclusion;
- branching over multiple plausible assumptions;
- stopping when the requested conclusion cannot be made defensibly.

A candidate principle is:

> **When project objectives and hard validity requirements conflict, degrade scope rather than integrity.**

This has not yet been promoted to a canonical principle.

## Admissibility is distinct from epistemic validity

The project has identified a major distinction:

```text
VALIDITY
Can the conclusion be justified?

ADMISSIBILITY
Is the action, data use, or intended application permissible?
```

An analysis may be methodologically excellent while still violating privacy, legal, policy, ethical, or operational-safety constraints.

These should not be conflated with epistemic validity.

## Risk-sensitive assurance

Project risk appears to affect how much verification, review, replication, and control is required before proceeding rather than changing what valid evidence means.

Higher-risk projects may require stronger assurance through mechanisms such as:

- additional validation;
- specialized review;
- independent replication;
- subgroup analysis;
- robustness analysis;
- human approval;
- monitoring requirements;
- fallback or rollback mechanisms;
- stricter reproducibility and documentation.

The exact risk and assurance model remains unresolved.

## Established working principles

The following continue to have strong support. Detailed formulations are maintained in `PRINCIPLES.md`.

1. The repository, not conversational memory, is the persistent source of truth.
2. Important reasoning should be preserved at multiple levels of detail.
3. Empirical evidence should dominate unsupported LLM judgment when a question can be tested.
4. Data science should be represented as an adaptive, revisitable process rather than a globally fixed linear pipeline.
5. The system should combine hard constraints, explicit decision frameworks, and open-ended reasoning.
6. Investigations should activate dynamically according to project facts rather than running every possible check.
7. Important decisions should expose assumptions, evidence, uncertainty, and alternatives.
8. Human involvement should be concentrated where human judgment materially improves the project.
9. Review, criticism, and where useful independent replication should be possible for important conclusions.
10. Real data projects should be used as coverage tests for the evolving system.
11. Generalizable lessons from project failures or omissions should become reusable system knowledge rather than project-specific patches.
12. Both the target system and the methodology used to build it should remain evolvable.
13. The meaning of a good project is project-relative.

## Accepted project-development decisions since Checkpoint 1

The user has explicitly delegated repository checkpoint timing to the AI design collaborator.

The AI should therefore decide proactively when substantial conceptual progress, a major transition, continuity risk, or another natural checkpoint makes repository preservation worthwhile. The user should not need to request every update.

The project also uses a numbered, content-specific chat naming convention inside the ChatGPT project. Chat titles are provenance and navigation aids, not dependencies of the system.

## Strong design hypotheses, not yet validated architecture

Important active hypotheses now include:

- reusable decision or knowledge modules;
- a trigger mechanism that activates relevant modules when project facts are discovered;
- a revisitable project reasoning graph;
- specialized reasoning and review responsibilities;
- proposer-reviewer separation;
- independent replication for selected high-risk findings;
- configurable analysis depth and resource budgets;
- explicit state for decisions, assumptions, experiments, evidence, uncertainty, and unresolved questions;
- a project-intent representation distinguishing objectives, constraints, deliverables, and human-control preferences;
- named modes as possible presets rather than the underlying representation;
- separation of project-level, model-level, and operational objectives;
- allocation of additional analytical effort according to expected value, uncertainty reduction, risk, and downstream impact;
- a project constitution separating admissibility, epistemic integrity, risk-sensitive assurance, and project optimization;
- five candidate epistemic invariants;
- analytical questions and claims as more fundamental orchestration objects than pipeline stages;
- explicit epistemic states for questions;
- completion based on sufficient resolution of required questions rather than fixed stage completion;
- reducing scope rather than silently lowering integrity when hard validity requirements conflict with project objectives.

These remain hypotheses to test and refine.

## Explicit non-decisions

The following remain undecided:

- number and permanence of agents;
- LLM providers and model strategy;
- orchestration or agent framework;
- workflow engine;
- database, knowledge graph, or rule-engine technology;
- exact representation of decision modules;
- experiment-tracking platform;
- execution sandbox architecture;
- deployment and UI architecture;
- final repository structure;
- final taxonomy of project types;
- exact autonomy levels and human gates;
- exact system-evaluation framework;
- final epistemic-invariant set and formal definitions;
- exact admissibility layer;
- exact treatment of ethics, privacy, law, policy, and operational safety;
- exact risk taxonomy and assurance requirements;
- exact analytical-question schema;
- exact question-state machine;
- exact project-completion rule;
- exact provenance and dependency representation;
- exact analytical-effort prioritization mechanism.

## Current knowledge-preservation approach

The project continues to use:

1. canonical documents for concise current state;
2. foundational design memos for detailed reasoning;
3. checkpoints and session records for historical snapshots;
4. raw conversation material, if archived later, as provenance rather than authority.

The project-development methodology has now evolved from version 0.1 to version 0.2. Version 0.2 makes proactive checkpoint detection an explicit responsibility of the AI design collaborator and records the session-naming convention used for continuity and navigation.

## Current external/source material

The ChatGPT project contains machine-learning and time-series/econometrics material that may later help develop knowledge modules and test reasoning coverage. It also contains an existing `Missing_Data.md` decision tree that has served as a useful miniature example of conditional data-science reasoning.

These materials have not yet been copied into the repository. The permanent source architecture remains undecided.

## Relationship to existing data projects

Individual data projects remain separate and are expected to become test environments for the system.

The five-invariant framework and wider project-constitution hypothesis must eventually be stress-tested on heterogeneous real projects rather than accepted from conceptual elegance alone.

## Current focus

The next major conceptual question is:

> **What exactly should the admissibility layer contain, and how much of ethics, privacy, law, safety, user policy, and external constraints should the data-science system itself reason about versus receive as hard constraints?**

Important subquestions include:

- Which admissibility constraints are universal system rules versus project-specific rules?
- Which legal or regulatory questions should trigger human or expert escalation rather than autonomous judgment?
- How should privacy, fairness, ethics, organizational policy, user instructions, and operational safety interact?
- How should uncertainty about admissibility be represented?
- Can admissibility rules conflict with each other?
- Which admissibility failures should block a project, restrict its scope, or require explicit approval?
- How should risk-sensitive assurance relate to admissibility?

## Required context for a new chat

A new design chat should read, at minimum:

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/VISION.md`
4. `docs/PRINCIPLES.md`
5. `docs/DECISIONS.md`
6. `docs/OPEN_QUESTIONS.md`
7. `docs/DEVELOPMENT_METHOD.md`
8. `docs/CONTINUITY.md`

For detailed reasoning, also read:

9. `docs/foundations/001_initial_vision_and_reasoning.md`
10. `docs/foundations/002_epistemic_integrity_and_project_constitution.md`

Relevant historical checkpoints are:

11. `docs/checkpoints/000_checkpoint_0.md`
12. `docs/checkpoints/001_primary_purpose_and_project_intent.md`
13. `docs/checkpoints/002_epistemic_integrity_and_project_constitution.md`

## Next step

Develop the first rigorous conceptual boundary of the admissibility layer before promoting the epistemic-core hypothesis into formal system requirements or choosing implementation architecture.
