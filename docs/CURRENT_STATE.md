# Current State

## Checkpoint

**Checkpoint:** 8  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, analytical depth, speed, or low cost are project-dependent objectives rather than universal goals.

## Current project constitution

The current conceptual hierarchy remains:

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

These are strong design hypotheses rather than finalized requirements.

## Checkpoint 4: project state and state-driven orchestration

Project state is treated as a living representation of what the system is currently entitled to believe and do rather than passive memory.

Candidate state objects include:

```text
PROJECT INTENT
FACT
ASSUMPTION
QUESTION
INVESTIGATION
EVIDENCE
CLAIM
DECISION
RISK
CONTROL
APPROVAL
CONSTRAINT / RULE
ACTION
ARTIFACT
```

Strong hypotheses include typed dependencies, separate validity and currency, impact analysis, reopening of questions and decisions, computational plus information lineage, a runnable frontier, separation of mandatory obligations from optional value-improving work, and state-driven rather than plan-driven orchestration.

Detailed reasoning:

`docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md`

## Checkpoint 5: project initialization and universal bootstrap

A new project should enter through progressive state construction rather than one-shot problem definition.

The fixed project-entry process may be much smaller than a complete universal workflow:

```text
SMALL UNIVERSAL BOOTSTRAP
        +
ADAPTIVE STATE-DRIVEN REASONING
```

The bootstrap should register sources and information boundaries, establish structural facts, compare sources for consistency, generate characterization hypotheses, emit triggers and questions, and construct the first runnable frontier.

A concise bootstrap rule remains:

> **Observe broadly, infer cautiously.**

Detailed reasoning:

`docs/foundations/005_project_initialization_and_universal_bootstrap.md`

## Checkpoint 6: knowledge activation

Reusable analytical knowledge should activate from meaningful project-state patterns and contribute structured state rather than directly control one fixed workflow.

The project distinguishes:

```text
KNOWLEDGE
What should be considered?

CAPABILITY
How can it be investigated or enforced?

ACTOR
Who or what performs the work?
```

Activation may arise from observations, requested objectives, proposed methods/actions/claims, missing prerequisites, contradictions, risk, governance, dependency revisions, or novel open-ended concerns.

The system should support deterministic, interpretive, and open-ended activation, plus reactive and prospective activation.

Activated knowledge should normally create questions, obligations, safeguards, evidence requirements, reviews, or candidate actions in project state. Actual work still competes on the runnable frontier.

Coverage review may search for orphaned material facts and orphaned actions.

Detailed reasoning:

`docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`

## Checkpoint 7: reusable knowledge representation

The strongest current representation hypothesis is:

> **The reusable knowledge library should consist of versioned, provenance-aware, composable semantic reasoning components grouped into coherent knowledge packages. When applicable, packages instantiate scoped project-specific concerns that contribute typed questions, constraints, evidence requirements, assumptions, alternatives, claim limitations, review needs, resolution criteria, and reopen conditions to project state.**

The durable asset is therefore not an agent persona, prompt, or fixed workflow. It is an explicit representation of what good reasoning requires.

The current middle-ground representation is:

```text
REUSABLE KNOWLEDGE PACKAGE
        |
        +-- thin semantic shell
        |
        +-- typed composable components
```

Candidate component types include:

```text
question template
hard invariant
decision principle
evidence requirement
investigation template
strategy / repair alternative
assumption template
failure mode
detection hook
claim constraint
human / authority hook
review / assurance hook
dependency
resolution criterion
reopen condition
```

Important distinctions include activation versus applicability, evidence requirements versus investigation methods, component role versus generic recommendation, and reusable definitions versus scoped project-specific instances.

Important components should preserve their own rationale, provenance, scope, limitations, version, and maturity.

The architecture was stress-tested against Missing Data and Information Legitimacy. Missing Data showed decision-heavy branching, while Information Legitimacy showed hard safeguards, prospective proposal validation, computational and reasoning lineage, repair patterns, and claim invalidation.

Detailed reasoning:

`docs/foundations/007_reusable_knowledge_representation_and_composable_components.md`

## Major development since Checkpoint 7: knowledge quality and evolution

Checkpoint 8 addresses the second-order epistemic risk created by reusable knowledge.

A project-specific mistake may damage one project. An incorrect reusable component may affect many future projects.

The strongest current formulation is:

> **The knowledge library should itself be treated as an epistemic system whose reusable claims have explicit scope, evidential support, provenance, maturity, dependencies, limitations, challenge history, currency, and enforcement authority.**

The same core integrity ideas used in project reasoning apply recursively to reusable knowledge: semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

The additional central problem is generalization beyond the source project or source material.

## Minimum justified generalization

A strong new hypothesis is:

> **Promote the least-general reusable proposition that captures the mechanism and is actually supported by the evidence; expand scope only when additional evidence or reasoning justifies expansion.**

This protects against abstraction drift, where project-specific conditions are silently removed while the local conclusion is preserved.

Project learning should therefore often generalize the reasoning structure rather than the locally successful action.

Example:

```text
Local result:
A missingness indicator improved one project's validation performance.

Bad reusable rule:
Always add missingness indicators.

Safer reusable knowledge:
When missingness itself may carry information relevant to the objective,
a missingness indicator is a candidate strategy worth evaluating under
legitimate validation.
```

## Project knowledge and reusable knowledge are separated

The current conceptual boundary is:

```text
PROJECT-SPECIFIC KNOWLEDGE
        -> CANDIDATE GENERALIZABLE LESSON
        -> REUSABLE SYSTEM KNOWLEDGE
```

A project result should not directly mutate the trusted library.

Future automated lesson extraction should produce **knowledge change proposals** that can be challenged and validated before influencing future projects.

`NO REUSABLE KNOWLEDGE UPDATE` is an important valid outcome when a lesson is genuinely local.

## Knowledge role, maturity, and enforcement authority

Checkpoint 8 strongly separates:

```text
ROLE
What kind of reusable statement is this?

MATURITY
How well established is it within its claimed scope?

ENFORCEMENT AUTHORITY
How strongly may the system constrain project behavior with it?
```

A mature heuristic remains a heuristic. Repeated empirical usefulness does not turn it into a methodological invariant.

The current conceptual threshold ordering is:

```text
REASONING THRESHOLD
    < REUSE THRESHOLD
    < DETERMINISTIC ENFORCEMENT THRESHOLD
```

The system should reason more creatively than it learns permanently, and learn more liberally than it enforces.

## Evidence and knowledge assurance

Different knowledge roles require different evidence forms. Methodological derivation, authoritative technical documentation, empirical project evidence, counterexamples, domain review, and LLM-generated hypotheses are not interchangeable.

LLM generation can create valuable candidate knowledge without conferring independent authority.

Knowledge assurance should be consequence-sensitive. A component that can block actions, invalidate evidence, or constrain claims should require stronger justification than a component that merely suggests an optional investigation.

Deterministic enforcement should have a high bar: sufficiently precise applicability, strong methodological or governance justification, understood scope, and acceptably controlled consequences of false enforcement.

## One-sided evidence asymmetry

Checkpoint 8 identifies an important asymmetry:

- one project example does not establish a universal rule;
- one valid counterexample can refute a truly universal rule;
- one valid failure case can establish that a failure mechanism is possible under the observed conditions without establishing its prevalence;
- many similar projects do not automatically establish transfer to dissimilar project types;
- some broad invariants may be justified mainly by methodological reasoning, while project cases provide regression coverage rather than the logical proof.

Counterexamples are therefore especially valuable for discovering hidden scope conditions.

## Candidate knowledge lifecycle

The current conceptual lifecycle is:

```text
SOURCE / PROJECT LESSON / HYPOTHESIS
        -> CANDIDATE COMPONENT
        -> proposition clarified
        -> scope and limitations stated
        -> provenance attached
        -> duplicate / contradiction search
        -> challenge and counterexample search
        -> reasoning regression cases
        -> review appropriate to consequence
        -> LIMITED ACTIVE KNOWLEDGE
        -> heterogeneous project exposure
        -> maturity / scope revision
        -> ACTIVE
        -> CHALLENGED / REAFFIRMED / REVISED / SUPERSEDED / RETIRED
```

Exact states are not selected.

Different knowledge roles should have different admission paths. A software fact, methodological invariant, heuristic, domain claim, and binding governance rule do not require the same evidence or authority.

## Contradictions and challenge

Apparent contradictions may reflect different scopes, assumptions, or analytical objectives.

The system should first attempt to resolve conflict through applicability refinement before treating it as genuine epistemic disagreement.

Genuine disagreement should remain visible rather than being hidden by source ranking or forced consensus.

Challenged knowledge may lose enforcement power before it is revised or retired.

Rejected generalizations and counterexamples should be preserved because they prevent future rediscovery of attractive but invalid simplifications.

## Validity and currency for reusable knowledge

Knowledge validity and knowledge currency are distinct.

A methodological principle may remain valid for years. API behavior, software capabilities, regulation, policies, provider behavior, or operational infrastructure may become stale much faster.

The relevant freshness question is how sensitive a proposition is to external change, not simply the age of its source.

Material knowledge revisions should carry enough change semantics to determine whether dependent active projects require revalidation.

## Cross-project self-correction

Reusable knowledge versions can participate in dependency analysis:

```text
knowledge component changes
    -> dependent packages identified
    -> project-specific instances identified
    -> materiality assessed
    -> affected claims / decisions / actions reopened where necessary
```

A highly reused weak component may become a **knowledge-library single point of failure**.

A qualitative review-priority intuition is:

```text
review importance rises with
uncertainty x reuse centrality x consequence of error
```

No numeric formula is selected.

## Reasoning regression tests

Checkpoint 8 makes behavioral regression tests central to knowledge governance.

Candidate case types include:

```text
positive applicability
negative applicability
boundary / unresolved applicability
known failure
counterexample
repair
reopen
claim limitation
```

Tests should examine false positives as well as false negatives.

Knowledge quality should eventually be evaluated at several levels:

```text
component correctness
package coherence
activation quality
project-level effect
```

## Self-confirmation risk

Project evidence generated by a process already influenced by reusable knowledge is not automatically independent confirmation of that knowledge.

Information lineage should therefore preserve when knowledge affected experiment design, action selection, or interpretation.

Independent challenge is particularly important for consequential or highly reused components.

## Stress tests for project-to-library learning

Four contrasting cases were used.

### Broad invariant candidate

A project fits learned preprocessing on all observations before cross-validation. The correct reusable abstraction is not `never standardize before CV`, but a learned-transformation information-boundary safeguard. The project supplies a failure case; broad invariant status requires methodological justification beyond one incident.

### Heuristic candidate

A missingness indicator helps one project. The project can support a candidate strategy or question template, but not mandatory use.

### Project-specific lesson

An organization-specific account-ID prefix identifies a legacy cohort with unusual churn because of a one-time migration. The finding should remain local unless an independently supported broader mechanism appears.

### Rejected apparent rule

Repeated patient IDs make grouped validation appropriate for one unseen-patient deployment. The tempting rule `repeated IDs -> GroupKFold` fails when another application predicts future observations for known entities. The better reusable knowledge is a question and decision principle about the intended generalization regime.

The central lesson is:

> **Generalize the reasoning, not the outcome.**

## Strong design hypotheses currently active

Important active hypotheses now include:

- five candidate epistemic invariants;
- project constitution separating admissibility, epistemic integrity, assurance, and optimization;
- typed dependency-aware project state;
- runnable frontier and state-driven orchestration;
- progressive source-aware initialization and a small universal bootstrap;
- reusable knowledge separate from capabilities and actors;
- activation distinct from execution and applicability;
- open-world knowledge with coverage review;
- thin knowledge packages plus typed components;
- evidence requirements distinct from investigation methods;
- claim constraints, failure modes, assumptions, and reopen conditions as reusable knowledge;
- project-specific instances separate from reusable definitions;
- component-level provenance and versioning;
- minimum justified generalization;
- separate knowledge role, maturity, and enforcement authority;
- separate reasoning, reuse, and enforcement thresholds;
- staged and challengeable knowledge promotion;
- counterexample-driven scope discovery;
- project learning through knowledge-change proposals rather than direct library mutation;
- reasoning regression cases as knowledge-quality evidence;
- potential cross-project revalidation after material knowledge revisions.

## Explicit non-decisions

The project has not selected agent count, LLM providers, orchestration framework, workflow engine, database, graph technology, project-state schemas, trigger language, semantic retrieval technology, knowledge package/component schemas, exact component taxonomy, maturity states, numeric knowledge-confidence system, promotion authority, contradiction-resolution algorithm, regression-case representation, freshness schedule, deterministic enforcement tiers, execution sandbox, automatic knowledge-learning mechanism, or final system-evaluation framework.

## Current focus

The knowledge-quality work makes one previously broad question concrete:

> **How should behavioral reasoning regression cases and the overall evaluation framework test project understanding, knowledge activation, safeguards, state transitions, claims, repair, and self-correction without reducing data science to one expected workflow or overfitting the system to a small benchmark suite?**

This now couples Q-016 and Q-017 and is the next major conceptual design problem.

Important subquestions include:

- What should a reasoning regression case contain?
- What outputs should be exact versus behaviorally constrained?
- How should multiple valid analytical paths be accepted?
- How should hidden traps and expected concerns be represented without leaking them to the system being evaluated?
- How should cases test false-positive as well as false-negative activation?
- How should state transitions, invalidation, reopening, and claim weakening be scored?
- How should evaluation distinguish final model quality from process quality?
- Which baselines should be compared?
- How should project diversity and held-out cases reduce benchmark overfitting?
- How should real projects become durable regression cases without leaking private or project-specific information into reusable knowledge?

Detailed reasoning for Checkpoint 8:

`docs/foundations/008_knowledge_quality_generalization_and_evolution.md`

Historical snapshot:

`docs/checkpoints/008_knowledge_quality_and_generalization.md`

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

For detailed reasoning, also read the eight files currently under `docs/foundations/`.

Relevant historical checkpoints are Checkpoints 0 through 8 under `docs/checkpoints/`.

## Next step

Develop the behavioral reasoning-regression and system-evaluation framework before choosing implementation architecture.