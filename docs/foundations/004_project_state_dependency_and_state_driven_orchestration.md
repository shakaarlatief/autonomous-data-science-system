# Project State, Dependency Integrity, and State-Driven Orchestration

**Date:** 2026-08-08  
**Status:** Foundational design memo  
**Maturity:** Strong design hypotheses, not implementation commitments

## Purpose

This memo preserves the conceptual reasoning developed after Checkpoint 3 about persistent project state, dependency-aware revision, invalidation, staleness, and the selection of next actions.

The central shift is that project state should not be treated as passive memory. It should represent the current epistemic and operational situation of the project strongly enough that the system can determine what it is still entitled to believe, what has become stale or invalid, what obligations have been created by new information, and what work should happen next.

The exact storage technology, schema, graph representation, workflow engine, and orchestration framework remain intentionally undecided.

## 1. Project state is more than memory

A conversational system can retain a project summary, recent messages, and a plan. That may help continuity but does not provide enough structure for a rigorous long-running analytical process.

At any point, the future system should be able to answer questions such as:

- What is the project trying to accomplish?
- What facts are currently established?
- What is only assumed?
- What questions remain unresolved?
- What evidence supports important claims?
- What evidence contradicts them?
- Which decisions were made and why?
- Which alternatives were rejected and for what reason?
- Which risks are active?
- Which controls and approvals are required?
- Which artifacts and experiments are current, stale, superseded, or invalid?
- Which conclusions depend on assumptions that have changed?
- Which actions are currently blocked?
- What should the system investigate or execute next?

The current strong hypothesis is therefore that persistent project state should represent the project's evolving epistemic and operational structure rather than only narrative memory.

## 2. Candidate typed state objects

A minimal conceptual vocabulary currently appears likely to require distinct object types such as:

- **Project intent**: objectives, constraints, deliverables, intended use, and human-control preferences.
- **Fact**: something established about the project, data, environment, process, or authoritative context.
- **Assumption**: something provisionally treated as true without sufficient direct evidence.
- **Question**: something that the project must or may benefit from resolving.
- **Investigation**: a planned analytical activity intended to answer one or more questions.
- **Evidence**: the output of an observation, experiment, diagnostic, test, external source, human clarification, review, simulation, or other evidence-producing procedure.
- **Claim**: a proposition supported to some degree by evidence and assumptions.
- **Decision**: a selected course of action among alternatives.
- **Risk**: a possible failure scenario with consequences, uncertainty, and exposure.
- **Control**: a mechanism intended to reduce risk or satisfy a constraint.
- **Approval**: authorization from an appropriate authority.
- **Constraint or rule**: a binding methodological, admissibility, governance, project, or operational requirement.
- **Action**: a proposed, approved, running, completed, failed, blocked, or cancelled operation.
- **Artifact**: a model, dataset version, code object, configuration, report, plot, prediction file, or other produced object.

This vocabulary is not final. The point is to prevent important epistemic distinctions from collapsing into prose.

A fact is not an assumption. Evidence is not a claim. A claim is not a decision. A decision is not an approval. A risk is not a control. These distinctions become necessary once the system must review, revise, invalidate, and explain its own reasoning.

## 3. Facts, assumptions, evidence, claims, and decisions should remain distinct

An important example is:

```text
OBSERVATION / FACT
18.2% of values in a feature are missing.
        |
        v
CLAIM / HYPOTHESIS
Missingness may contain useful information.
        |
        v
QUESTION
Does a missingness indicator improve the intended predictive objective?
        |
        v
INVESTIGATION
Compare strategies under the accepted validation design.
        |
        v
EVIDENCE
Cross-validation results and uncertainty.
        |
        v
DECISION
Retain or reject the indicator for the current modelling process.
```

Narrative workflows often compress all of these into one paragraph. The current design direction is to preserve the distinctions explicitly so later review can determine which part of the chain changed.

Consequential assumptions are especially important because they can become hidden dependency roots. If an assumption such as production missingness, prediction timing, population stability, or feature availability is later contradicted, the system should be able to identify what downstream work relied on it.

## 4. Questions as an orchestration backbone

A strong hypothesis is that analytical questions may be more fundamental orchestration objects than conventional pipeline stages.

A question may contain conceptually relevant information such as:

- what is being asked;
- why it matters;
- which object, population, environment, time, or intended use it concerns;
- whether it is project-defining, validity-related, assurance-related, or value-improving;
- whether it blocks dependent work;
- what evidence would count toward resolution;
- which investigations could answer it;
- which claims or decisions depend on it;
- whether it is open, assumed, supported, disputed, inconclusive, blocked, invalidated, reopened, or sufficiently resolved.

The exact categories and states are not final.

A question does not always require a definitive answer. A valid resolution can be that available evidence cannot distinguish two alternatives and that the remaining uncertainty is acceptable for the current project. This is important for stopping rather than experimenting indefinitely.

## 5. Decisions should preserve rationale and rejected alternatives

A decision should not merely store the selected option.

Important decisions may need to preserve:

- the alternatives considered;
- the supporting evidence and assumptions;
- the objective or requirement the decision serves;
- reasons rejected alternatives were not selected;
- uncertainty or review status;
- which later objects depend on the decision;
- whether the decision is current, reopened, reaffirmed, or superseded.

Preserving rejected alternatives prevents later agents from repeatedly proposing the same discarded path without understanding why it was previously rejected.

## 6. Artifacts need semantic identity and provenance

A model or report should not be identified primarily by a filename such as `model_final2.pkl`.

Conceptually, an important artifact should be tied to the process that produced it, such as:

- dataset version;
- preprocessing and feature representation;
- validation design;
- configuration;
- experiment or action;
- code version where relevant;
- intended use;
- current status;
- object it supersedes or derives from.

This supports reproducibility, stale-state detection, invalidation, and later auditing.

## 7. State and history are different requirements

The system needs both:

1. a usable current view of what should be believed and acted upon now; and
2. historical preservation of how the state changed.

Overwriting a claim from `supported` to `invalidated` without retaining the prior state loses important provenance. A mature project should be able to reconstruct what was believed, why it was believed, what changed, and which downstream actions used that earlier state.

This does not imply a particular event-sourcing architecture. The conceptual requirement is simply that important transitions remain reconstructable.

## 8. Validity and currency should be separate concepts

An old result can remain methodologically valid while no longer representing the current project state.

For example:

- a correct experiment on dataset version 3 may be **valid but stale** when version 4 arrives;
- a leakage-contaminated experiment is **invalid**;
- an older accepted model may be **valid but superseded**;
- a result affected by a newly challenged assumption may be **under review**.

The current direction is therefore to avoid one overloaded universal status such as `invalid` for all objects that are no longer current.

## 9. Project state is dependency-aware

The objects are not independent records. They form a network of typed relationships.

Candidate relationship meanings include:

- `supports`;
- `contradicts`;
- `depends_on`;
- `hard_depends_on`;
- `derived_from`;
- `informed_by`;
- `answers`;
- `motivates`;
- `blocks`;
- `invalidates`;
- `supersedes`;
- `requires`;
- `implements`;
- `mitigates`;
- `approves`;
- `generated_by`.

The exact vocabulary is not final. The important requirement is that relationship semantics should be strong enough to determine how an upstream change affects downstream objects.

## 10. Different dependencies should propagate differently

A generic `depends_on` relationship is insufficient.

Several conceptual dependency classes currently appear useful:

### Hard validity dependency

A downstream object's validity requires an upstream assumption, fact, procedure, or condition to hold.

If the upstream object is invalidated, the downstream object may need deterministic invalidation.

### Support dependency

Evidence contributes support to a claim. If one evidence item is invalidated, the claim should be reassessed rather than automatically declared false when other support remains.

### Provenance or derivation dependency

An artifact was derived from a particular dataset or configuration version. A new upstream version may make it stale rather than invalid.

### Requirement dependency

An action may require an approval, constraint satisfaction, or prerequisite. If the prerequisite disappears, the action becomes blocked while unrelated analytical evidence may remain valid.

### Mitigation dependency

A control reduces a risk. If the control becomes ineffective, residual risk should be reassessed rather than marking the risk itself invalid.

This distinction supports object-specific propagation rather than indiscriminate invalidation.

## 11. Change should trigger impact analysis

Whenever a consequential object changes, the system should determine its downstream blast radius.

Conceptually:

```text
NEW FACT / REVISION / INVALIDATION / NEW VERSION
                    |
                    v
          identify changed object
                    |
                    v
       traverse typed dependencies
                    |
                    v
       determine impact semantics
                    |
                    v
    apply deterministic consequences
                    |
                    v
mark ambiguous dependents for reassessment
                    |
                    v
       reopen affected questions
                    |
                    v
          generate obligations
                    |
                    v
      prioritize repair or revalidation
```

This change-processing loop is a central part of the current self-correcting-system hypothesis.

## 12. Propagation should identify reconsideration, not always determine the conclusion

If one supporting experiment becomes invalid, the system may know deterministically that the claim's support set has changed. It may not know automatically whether the claim remains strongly supported, becomes weakly supported, or should be retracted.

Therefore the current direction distinguishes deterministic propagation from review-triggering propagation.

Possible conceptual effects include:

- automatically invalidate;
- mark stale;
- block;
- reopen;
- require reassessment;
- no material effect.

The exact statuses are not final.

## 13. Questions and decisions should reopen when premises change

If a previously closed validation question was resolved under an independence assumption and a later fact reveals repeated entities, the question should be reopenable.

Similarly, an earlier decision should remain historically visible while its current status changes to reopened, superseded, or reaffirmed.

The system should be able to explain:

> The earlier decision was defensible under the information available at the time, but new information changed the dependency structure and required reconsideration.

This is a stronger form of auditability than simply overwriting the current answer.

## 14. Invalidation creates new obligations

Marking an object invalid is not sufficient.

An invalidated validation experiment may create obligations to:

- reopen model comparison;
- define a new validation procedure;
- rerun affected candidate models;
- reconsider model selection;
- update risk assessment;
- mark dependent report claims stale;
- reopen an approval if conditions materially changed.

Conceptually:

```text
STATE CHANGE
    -> IMPACT ANALYSIS
    -> NEW OBLIGATIONS
    -> PRIORITIZATION
    -> NEXT ACTIONS
```

This closes the loop from self-correction back into orchestration.

## 15. Not every affected object should be repaired immediately

A dependency change may affect many historical objects, but repair priority should depend on whether the object still matters to current decisions or deliverables.

The system should distinguish:

- affected;
- must be repaired now;
- should be reviewed later;
- historical only.

Priority may depend on downstream importance, risk, deliverable relevance, cost, and expected value.

This avoids turning dependency tracking into an expensive automatic rerun of the entire project after every change.

## 16. Materiality matters

Not every upstream change is equally consequential.

A target-definition change may invalidate much of a predictive project. A one-row update to a dataset with millions of rows may be immaterial to many conclusions. A documentation typo may have no analytical effect.

The system therefore needs a concept of materiality: does this change matter to a particular dependent object strongly enough to require staleness, invalidation, review, or re-execution?

Some materiality rules may be deterministic. Others may require analysis or judgment.

## 17. Computational lineage is not enough

One of the strongest insights from this design step is that information can influence a project without appearing in code or data lineage.

For example, a final test result may be viewed by a human or LLM, which then proposes new feature engineering. The resulting model may technically be trained only on training data while its development was still informed by test feedback.

Therefore the system may need both:

### Computational or provenance lineage

```text
dataset -> transformation -> model -> prediction
```

### Epistemic or information lineage

```text
fact -> question -> evidence -> claim -> decision -> action
```

and governance lineage such as:

```text
constraint -> control -> approval -> action
```

This is particularly important for leakage auditing, independent review, and reasoning provenance.

## 18. Evidence independence can be evaluated through dependencies

Two agreeing analyses are not genuinely independent if they share the same vulnerable ancestor.

For example, two models evaluated under the same flawed validation procedure do not provide independent evidence that the project conclusion is robust.

A dependency-aware system could identify:

- shared validation assumptions;
- shared datasets or splits;
- shared information contamination;
- claims with only one independent support path;
- assumptions with very large downstream blast radius.

This creates the concept of **epistemic single points of failure**. High-leverage, weakly supported dependency roots may deserve targeted review or independent evidence, especially in higher-risk projects.

## 19. Plans should be derived views, not the deepest source of truth

A static project plan becomes stale whenever important state changes.

The stronger current hypothesis is that plans should be generated from current project state.

A derived current view might contain:

- active blocking questions;
- mandatory unresolved obligations;
- accepted decisions;
- current validation design;
- active risks and controls;
- stale or invalid high-impact objects;
- pending approvals;
- candidate next actions.

The rich state remains authoritative. The plan is a convenient current projection.

## 20. Candidate actions should arise from unresolved state

Every consequential action should ideally be traceable to at least one unresolved question, obligation, risk, requirement, deliverable, repair need, or accepted decision.

This helps prevent method-first activity such as training a neural network merely because it is available.

An action can conceptually preserve:

- why it is being proposed;
- which state objects motivate it;
- what state change or evidence it is expected to produce;
- prerequisites;
- admissibility status;
- estimated resource cost;
- risk or reversibility considerations;
- whether human approval is required;
- stopping or completion condition.

The exact action schema remains open.

## 21. The runnable frontier

A useful conceptual abstraction is the **runnable frontier**: the set of currently useful candidate actions whose prerequisites are satisfied and which are not blocked by admissibility, unresolved dependencies, approvals, resource constraints, or mutually exclusive work.

The orchestrator does not need to ask what fixed pipeline stage comes next. It can ask:

> Which currently executable action or set of actions best advances the project from its present state?

This makes orchestration state-driven.

## 22. Hard gates should be separated from priority

The system should not use one weighted score to decide whether a mandatory validity issue competes with optional hyperparameter tuning.

A more defensible conceptual policy is:

1. identify hard blockers and mandatory obligations;
2. filter actions that are not currently admissible or executable;
3. satisfy prerequisites needed to unlock high-impact dependent work;
4. prioritize among the remaining candidates using expected project value.

This preserves the distinction between requirements and preferences.

A user preference for speed may reduce optional exploration but should not cause a blocking leakage question to lose against a cheap model-tuning action.

## 23. Candidate prioritization factors

Among admissible and executable candidate actions, current candidate factors include:

- blocking power;
- methodological or admissibility importance;
- risk reduction;
- expected probability of changing a consequential decision;
- expected information or uncertainty reduction;
- downstream dependency leverage;
- deliverable relevance;
- urgency or external deadline;
- resource cost;
- human cost and interruption cost;
- reversibility;
- parallelizability;
- project objectives and depth preferences.

The project should not prematurely compress these into a false-precision scalar score.

A useful qualitative value-of-information intuition is:

```text
Value of investigation
    ~ probability it changes an important decision
      x importance of that decision
      - cost of obtaining the information
```

Risk reduction and high dependency leverage can substantially increase that value.

## 24. High-leverage uncertainty should be prioritized

If one uncertain assumption affects validation, all model comparisons, deployment claims, and risk assessment, clarifying that assumption may be far more valuable than another model experiment.

Dependency structure can therefore help determine investigation value.

A strong current hypothesis is that the system should prioritize uncertainty not only by how uncertain it is, but also by how much consequential downstream state depends on it.

## 25. Parallel work should follow dependency structure

Several investigations can run in parallel when they are independent, admissible, resource-compatible, and do not compromise desired reviewer independence.

Other work should wait when prerequisites matter. For example, broad model comparison may need to wait until a disputed validation design is resolved.

The dependency model can therefore tell the system:

- what is runnable now;
- what is blocked;
- what can run concurrently;
- what must remain isolated for independent review;
- what should be cancelled because upstream state made it irrelevant.

## 26. Human questions are also candidate actions

`Ask the human` should not be treated as a fallback outside the orchestration system.

When a semantic, normative, authority, or domain question cannot be resolved reliably through available evidence, requesting human input can itself be the highest-value next action.

The system may still gather cheap evidence first if that is likely to avoid unnecessary interruption.

This supports the distinction between preferred and required human involvement.

## 27. Plans and actions should be dynamically revisable

An action that was high priority may become unnecessary after new evidence arrives. A blocked action may become runnable after approval. A low-value investigation may become mandatory when intended use changes.

Therefore planning should be treated as provisional.

The system should repeatedly recompute what matters from current state rather than following an obsolete plan simply because it was generated earlier.

## 28. Local stopping and project completion

The system needs both local and global stopping concepts.

### Local stopping

A question or line of investigation can stop when, for the current project:

- evidence is sufficient to support a decision;
- remaining uncertainty is decision-irrelevant;
- further work has low expected value;
- available data cannot discriminate alternatives;
- a valid simpler decision rule resolves the issue;
- a resource constraint is reached without violating integrity.

### Project completion

A project may be ready to complete when:

- no blocking epistemic or admissibility questions remain unresolved;
- mandatory assurance obligations are satisfied or appropriately accepted;
- required approvals are current;
- deliverables are complete;
- critical state is internally consistent;
- no important current artifact depends on known invalid state;
- residual uncertainty is documented and acceptable for the intended use;
- remaining optional actions have insufficient expected value relative to project goals and budget.

This remains a hypothesis, not a finalized completion rule.

## 29. Project depth affects optional stopping, not validity gates

A quick project and a research-depth project may stop at different points.

A quick project may pursue only high-value optional investigations after satisfying mandatory validity and admissibility obligations. A research project may continue through robustness analysis, replication, ablations, and broader alternatives because its project intent gives those actions higher value.

This is a clean mechanism for configurable depth without making methodological integrity configurable.

## 30. The resulting control loop

The current strongest conceptual orchestration loop is:

```text
CURRENT PROJECT STATE
        |
        v
identify unresolved questions, obligations, risks,
stale/invalid objects, deliverable needs, approvals
        |
        v
generate candidate actions
        |
        v
filter by admissibility, prerequisites, resources,
and required independence
        |
        v
identify hard blockers and mandatory work
        |
        v
rank remaining runnable candidates by expected project value
        |
        v
select one action or compatible parallel action set
        |
        v
execute / investigate / review / ask human
        |
        v
produce evidence, artifacts, decisions, approvals, or changes
        |
        v
update dependencies and run impact analysis
        |
        v
recompute project state and runnable frontier
```

This is not a commitment to a specific orchestrator implementation. It is a behavioral hypothesis about how the future system should control work.

## 31. Project state may be more fundamental than the orchestrator

An earlier framing placed the orchestrator at the center of the architecture.

The current reasoning suggests a deeper view:

```text
                 PROJECT STATE
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      reasoning    execution    review
          |           |           |
          +-----------+-----------+
                      |
                      v
                STATE UPDATE
                      |
                      v
             NEW ACTIVE FRONTIER
```

Under this view, the orchestrator is a mechanism that reads the state, identifies admissible transitions, chooses actions, and updates the state. The durable intellectual core is the explicit representation of project knowledge, obligations, dependencies, and revision rules.

## 32. Implementation remains intentionally open

The conceptual structure appears graph-like because objects have typed relationships, but this does not imply a graph database.

Possible future implementations could use relational storage, document records, event logs, JSON, graph storage, or hybrids.

Likewise, the control loop does not imply a specific agent framework, workflow engine, scheduler, or LLM provider.

The current goal is to preserve semantic requirements before choosing technology.

## 33. Current consolidated hypothesis

The strongest current project-state hypothesis is:

> **The system should maintain an explicit, typed, dependency-aware, historically traceable project state representing the evolving facts, assumptions, questions, investigations, evidence, claims, decisions, risks, controls, constraints, approvals, actions, artifacts, and obligations of the project.**

And the strongest orchestration hypothesis is:

> **Next actions should be generated and prioritized from unresolved or changed project state rather than from a globally fixed pipeline, with hard validity and admissibility obligations separated from optional value-improving work.**

Together, these hypotheses transform state from passive memory into an active control mechanism.

## 34. Next conceptual transition

This design step completes a coherent conceptual unit around state, revision, and action selection.

The next natural question is how a new project enters this system in the first place:

> **How should the system initialize project state from a user's request, available files and data, project documentation, external constraints, and early inspection without assuming that the initial problem statement is complete or correct?**

This question connects project intent, semantic validity, project characterization, admissibility, initial risk, human clarification, and early question generation.

It should be explored conceptually before selecting implementation technology.