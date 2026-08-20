# Checkpoint 006: Knowledge Activation and Open-World Reasoning

**Date:** 2026-08-08  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Conceptual research and system definition  
**Scope:** Records the historical milestone described by this checkpoint: Knowledge Activation and Open-World Reasoning.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Not started

## Scope of this checkpoint

Checkpoint 6 records the first coherent conceptual model for how project state should activate reusable data-science knowledge without relying on one enormous centralized workflow or assuming that one LLM will remember every possible concern.

Detailed reasoning is preserved in:

`docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`

## Core hypothesis

> **Reusable data-science knowledge should be activated from patterns in project state and should contribute structured questions, obligations, safeguards, evidence requirements, review needs, and candidate actions back into that state rather than directly controlling one fixed workflow.**

This extends the Checkpoint 4 state-driven orchestration model and the Checkpoint 5 universal bootstrap protocol.

## Knowledge is not an agent

The project now strongly distinguishes:

```text
KNOWLEDGE
What should be considered?

CAPABILITY
How can it be investigated or enforced?

ACTOR
Who or what performs the work?
```

Reusable analytical knowledge should therefore not be bound prematurely to permanent agents.

## Reusable definitions and project instances

The system-level knowledge library should contain reusable definitions.

Projects should contain scoped instances created when that knowledge becomes relevant to particular facts, questions, actions, claims, datasets, features, models, or deployment contexts.

Project instances can then be resolved, reopened, or revised without changing the reusable definition itself.

## Activation does not mean immediate execution

Activation means that a concern is relevant enough to become represented in project state.

Actual execution remains governed by the runnable frontier, mandatory obligations, risk, project intent, dependencies, and expected value.

The project therefore distinguishes activation priority from execution priority.

## Candidate activation strengths

The discussion identified a useful conceptual distinction between:

```text
ENFORCE
mandatory once established

INVESTIGATE
applicability or consequences need resolution

CONSIDER
potentially useful but not currently mandatory
```

The exact labels are not final.

## Activation mechanisms

Checkpoint 6 favors a hybrid model:

1. deterministic activation for precise hard safeguards;
2. interpretive activation for state patterns whose relevance requires reasoning;
3. open-ended discovery for novel concerns that are not represented by the current knowledge library.

## Trigger sources

Activation is broader than reacting to raw observations.

Knowledge may activate because of:

- observed facts;
- combinations of facts;
- requested analytical objectives;
- desired claim types;
- proposed actions;
- proposed methods;
- proposed decisions;
- proposed claims;
- missing prerequisites;
- contradictions;
- risk or governance state;
- dependency revisions;
- novel open-ended concerns.

This is a major refinement of the original fact-trigger concept.

## Reactive and prospective activation

The system should support both:

```text
REACTIVE ACTIVATION
something important was discovered
```

and:

```text
PROSPECTIVE ACTIVATION
something is about to be claimed, decided, or executed
```

Prospective activation may allow methodological and governance knowledge to validate proposals before execution.

Examples include protecting a final test set, checking target encoding for leakage, or evaluating a sensitive-data transfer before it occurs.

## Missing prerequisites can trigger knowledge

The absence of required state can itself create an obligation.

Examples include causal claims without identification assumptions, deployment without monitoring requirements, model selection without a defensible validation design, or external transfer without established permission.

## Module inputs and outputs

Activated knowledge should receive a relevant state slice rather than a complete conversational transcript.

It may contribute typed objects such as:

- questions;
- semantic or methodological obligations;
- safeguards;
- evidence requirements;
- candidate investigations;
- risks;
- review requests;
- human clarification requests;
- candidate decisions;
- sufficient-resolution conditions.

The output should become project state rather than an isolated prose answer.

## Indirect module interaction

Modules should normally interact through shared state:

```text
MODULE A
    -> state update
    -> activation layer
    -> MODULE B becomes relevant
```

rather than primarily through direct module-to-module calls.

This reduces coupling and preserves activation provenance.

## Shared questions as integration points

Several modules may contribute to the same analytical question.

Temporal structure, repeated entities, and leakage concerns may all motivate one question about whether validation represents deployment.

Shared questions can therefore prevent modular reasoning from fragmenting into duplicated workflows.

## Evidence frameworks rather than recipes

Knowledge units should encode distinctions, evidence requirements, failure modes, and conditional strategies rather than rules such as:

```text
missing values -> median imputation
imbalance -> SMOTE
```

A module should help determine what response is justified from project evidence.

## Scope and applicability

Knowledge instances need a scope and should distinguish candidate relevance from established applicability.

A possible sequence is:

```text
state pattern
    -> candidate relevance
    -> applicability check
    -> project-specific knowledge instance
```

Precise deterministic safeguards may skip the interpretive applicability stage.

## Open-world and compositional knowledge

The knowledge library should be assumed incomplete.

Novel concerns must be representable through open-ended reasoning even when no exact reusable module exists.

Multiple partially relevant knowledge units may be composed for one concern.

The project has therefore not committed to one homogeneous module granularity or taxonomy.

## Coverage review

Because false-negative activation is possible, the system likely needs a residual coverage process that asks whether important project facts remain unrepresented by active reasoning, accepted resolution, explicit irrelevance, or acknowledged residual uncertainty.

This produced the concept of an **orphaned material fact**.

## Orphaned actions

The complementary problem is a consequential action with no project-state justification.

A useful integrity pair is therefore:

```text
ORPHANED MATERIAL FACT
important state with no reasoning consequence

ORPHANED ACTION
consequential work with no state-based justification
```

## Review uses the same activation model

Independent review, replication, privacy review, leakage review, or other specialist checks can be activated from risk, dependency fragility, weak evidence, governance state, or assurance requirements rather than existing as an always-on fixed reviewer roster.

## Stress-test result

The activation model was stress-tested conceptually against:

- missing data;
- temporal structure;
- repeated entities / group dependence;
- target leakage and test-set integrity;
- class imbalance;
- causal inference;
- clustering;
- privacy and admissibility;
- novel feedback-loop / domain-specific concerns.

The abstraction survived these tests but required the refinements documented above.

## Current conceptual loop

```text
CURRENT PROJECT STATE
        |
        +--> observation
        +--> proposed action / method / claim / decision
        +--> missing prerequisite
        +--> contradiction
        +--> risk / governance condition
        +--> dependency revision
        +--> novel concern
                    |
                    v
             RELEVANCE DETECTION
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
```

Coverage review surrounds this loop to search for missed material concerns.

## Strong hypotheses preserved by this checkpoint

Checkpoint 6 records the following as strong design hypotheses rather than accepted implementation decisions:

1. reusable knowledge should be separate from agents and tools;
2. reusable definitions and project-specific instances should be distinct;
3. activation should update state rather than directly execute fixed workflows;
4. activation can be deterministic, interpretive, or open-ended;
5. proposed actions, methods, decisions, and claims should support prospective activation;
6. missing prerequisites can activate obligations;
7. modules should consume relevant state slices and produce typed state contributions;
8. modules should interact primarily through project state;
9. shared questions should reconcile overlapping knowledge;
10. knowledge should encode evidence frameworks rather than cookbook prescriptions;
11. knowledge needs scope, applicability, satisfaction, and reopen behavior;
12. the library should be open-world and compositional;
13. coverage review should search for missed concerns;
14. orphaned facts and actions are promising integrity checks;
15. activation quality itself should become an evaluation target.

## Explicit non-decisions

No trigger language, rule engine, retrieval technology, module schema, module taxonomy, graph database, agent framework, workflow engine, activation threshold, scope representation, coverage implementation, or module versioning format has been selected.

## Continuation point

The next conceptual question is:

> **What should a reusable knowledge unit contain internally so that, once activated, it can reliably generate the right questions, safeguards, evidence requirements, candidate investigations, review behavior, resolution criteria, and state transitions across heterogeneous projects?**

This is the next step toward a concrete representation of reusable data-science reasoning.