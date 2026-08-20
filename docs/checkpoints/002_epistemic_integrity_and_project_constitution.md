# Checkpoint 2: Epistemic Integrity and the Project Constitution

**Date:** 2026-08-08  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Conceptual research and system definition  
**Scope:** Records the historical milestone described by this checkpoint: Epistemic Integrity and the Project Constitution.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Not started

## Why this checkpoint was created

Since Checkpoint 1, the project has made substantial conceptual progress on the question of what should remain non-negotiable when the system adapts itself to different project goals.

The discussion has moved beyond a generic "quality floor" toward a more structured hypothesis about epistemic integrity, admissibility, risk-sensitive assurance, analytical questions, and dependency-aware project state.

The checkpoint is being created now because the material is foundational and sufficiently developed that continuing without preservation would risk losing important distinctions.

## Accepted context from Checkpoint 1

The project continues to accept the primary purpose established at Checkpoint 1:

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Configurability therefore remains central. However, project preferences should not be able to redefine invalid methodology as acceptable.

## Major conceptual advance: optimization inside a constitution

The current strong hypothesis is that project-specific optimization should occur only inside a set of non-negotiable boundaries.

The emerging hierarchy is:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

Hard external project constraints may cut across these layers.

This is not a selected implementation architecture. It is a conceptual model for separating different kinds of obligations.

## Epistemic integrity: five candidate invariants

The discussion produced five candidate invariants that may form the deepest methodological core of the system.

### 1. Semantic validity

The analytical object being predicted, estimated, described, compared, or optimized must correspond sufficiently to the actual project question and intended use.

Core question:

> **Are we answering the right question?**

### 2. Information legitimacy

Every analytical step may use only information legitimately available to that step under the conditions the analysis is intended to represent.

Core question:

> **Did we use only information we were legitimately allowed to use?**

This concept unifies target leakage, temporal leakage, preprocessing leakage, test-set feedback, some group leakage, and related failures.

### 3. Evidence validity

The procedure must be appropriate for the question, its material assumptions must be adequately satisfied or acknowledged, and the executed computation must faithfully instantiate the intended procedure.

Core question:

> **Did our procedure validly generate evidence about that question?**

Execution fidelity is currently treated as a likely component of evidence validity rather than a separate sixth invariant.

### 4. Claim validity

The content, strength, scope, and certainty of a claim must not exceed what the evidence and supporting assumptions justify.

Core question:

> **Are we saying only what the evidence justifies?**

### 5. Traceability and dependency integrity

Consequential results, claims, and decisions should be reconstructable and connected to the assumptions, data, procedures, computations, and upstream decisions on which they depend.

Core question:

> **Can we reconstruct why we believe this, and what depends on it?**

The dependency aspect matters because later discoveries may invalidate earlier results and require downstream claims or artifacts to become stale automatically.

## Why these are not yet canonical invariants

The five-invariant framework has survived conceptual stress tests across classification, forecasting, causal inference, clustering, anomaly detection, dimensionality reduction, and recommendation-style settings.

However, it has not yet been tested systematically on real projects, formalized into precise requirements, or demonstrated to be complete.

It therefore remains a strong design hypothesis rather than a finalized specification.

## Universal quality rules versus conditional obligations

A quality floor should not become a giant mandatory checklist.

The project now distinguishes between:

- **universal integrity requirements**, which apply broadly; and
- **conditional methodological obligations**, which become mandatory when project facts activate them.

For example, temporal information constraints are mandatory when the project represents prediction through time but irrelevant to a genuinely static retrospective description.

This distinction is important for preserving both rigor and adaptivity.

## Analytical questions may be more fundamental than models or stages

Another strong hypothesis is that the system should primarily manage analytical questions and claims rather than merely pipeline stages or model objects.

Conceptually:

```text
project
  -> important questions
  -> investigations
  -> evidence
  -> claims and decisions
  -> new questions
```

The project may eventually need an explicit analytical-question representation containing concepts such as:

- what is being learned or decided;
- the analytical object;
- the relevant population or environment;
- time or horizon;
- intended use;
- desired strength of conclusion.

No representation format has been selected.

## Possible question categories

The discussion identified three useful conceptual categories:

### Project-defining questions

Questions that establish what the project actually means, such as target definition, prediction timing, population, or intended action.

### Validity questions

Questions that determine whether available evidence can support the project, such as leakage, split validity, dependence, feature availability, or identification assumptions.

### Value-improving questions

Optional questions that may improve the result, such as exploring additional model families or transformations.

A future orchestrator should probably not spend substantial resources on value-improving work while unresolved project-defining or validity questions remain capable of invalidating the project.

## Possible epistemic states for questions

The following states were discussed but not finalized:

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

This could help the system understand what remains unresolved instead of merely marking workflow stages complete.

## Responses when validity cannot be established

The system should not equate autonomy with always continuing.

Legitimate responses may include:

- **RESOLVE** by gathering more evidence;
- **RESEARCH** by obtaining external information;
- **ASK** for human or domain clarification;
- **RESTRICT** the intended conclusion;
- **BRANCH** over multiple plausible assumptions;
- **STOP** if the requested conclusion cannot be made defensibly.

A candidate principle emerged:

> **When project objectives and hard validity requirements conflict, degrade scope rather than integrity.**

This has not yet been promoted to a canonical principle.

## Why epistemic integrity is not the whole quality floor

The five invariants appear to absorb many concerns such as statistical uncertainty, generalization, robustness, reproducibility, and execution fidelity.

However, the project identified a distinct dimension:

```text
VALIDITY
Can the conclusion be justified?

ADMISSIBILITY
Is the action, data use, or intended application permissible?
```

An analysis can be epistemically sound while still violating privacy, law, policy, ethical constraints, or operational safety requirements.

These should not be forced into the same conceptual category.

## Risk-sensitive assurance

Project risk appears to change how strongly the system must verify its conclusions rather than changing what valid evidence means.

Higher-risk projects may require stronger assurance through mechanisms such as:

- additional validation;
- specialized review;
- independent replication;
- subgroup analysis;
- robustness analysis;
- human approval;
- monitoring requirements;
- rollback or fallback mechanisms;
- stricter reproducibility and documentation.

The exact risk and assurance model remains open.

## Detailed reasoning preserved separately

The full rationale, examples, domain stress tests, and conceptual development are preserved in:

`docs/foundations/002_epistemic_integrity_and_project_constitution.md`

That memo should be consulted when the concise checkpoint is insufficient.

## Development-method update at this checkpoint

The user has explicitly delegated checkpoint timing to the AI design collaborator rather than requiring the user to request every repository update.

The development method should therefore now treat checkpoint detection as a proactive responsibility: continue discussion while it is fluid, but initiate repository preservation when substantial progress, a major conceptual transition, or continuity risk makes it valuable.

This is the first explicit revision to the project-development methodology based on actual use.

## Active design hypotheses after Checkpoint 2

The following are strong but not finalized:

- five epistemic invariants form the core methodological constitution;
- execution fidelity belongs inside evidence validity;
- the wider project constitution separates admissibility, epistemic integrity, risk-sensitive assurance, and project optimization;
- analytical questions and claims are more fundamental orchestration objects than models and stages;
- questions need explicit epistemic status;
- project completion should depend on resolution of required questions rather than completion of fixed stages;
- hard validity conflicts should narrow scope rather than silently lower integrity.

## Explicit non-decisions

Checkpoint 2 does not select:

- final invariant definitions;
- machine schemas for questions, claims, evidence, or dependencies;
- exact admissibility rules;
- exact legal, ethical, privacy, or policy reasoning responsibilities;
- exact risk taxonomy or assurance levels;
- exact question-status state machine;
- exact stopping/completion rule;
- orchestration framework;
- agent structure;
- model providers;
- database or graph technology;
- implementation architecture.

## Next conceptual focus

The next major design question is:

> **What exactly should the admissibility layer contain, and how much of ethics, privacy, law, safety, user policy, and external constraints should the data-science system itself reason about versus receive as hard constraints?**

This should be explored before promoting the five-invariant epistemic framework into a more formal requirements specification.
