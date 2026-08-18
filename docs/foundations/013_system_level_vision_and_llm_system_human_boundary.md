# Foundation 013: System-Level Vision and the LLM-System-Human Boundary

**Date:** 2026-08-18  
**Status:** Foundational system-level synthesis  
**Origin:** Promotes the stable architectural synthesis first made explicit in Checkpoint 22 while preserving that checkpoint as historical provenance.

## Purpose

This foundation clarifies why the Autonomous Data Science System is intended to exist as a system around one or more strong reasoning models rather than as a single long LLM conversation, and it defines the current working boundary among:

```text
LLM reasoning
system-managed process intelligence
human judgment and control
```

This document does not prescribe a final implementation architecture. It does not commit the project to multi-agent orchestration, a specific model provider, a graph database, a workflow framework, or the exact mechanisms currently implemented in Prototype V0.

Its purpose is more durable: preserve the system-level problem the project is trying to solve so that local prototype results are interpreted in the correct broader context.

The central working principle is:

> Build only the system mechanisms that demonstrably improve the reliability, coverage, efficiency, reuse, or human-navigation burden of real data-science work beyond what strong simpler workflows already achieve.

This principle has two equally important consequences:

```text
A strong LLM is not evidence that system-level process machinery is unnecessary.

A broad system vision is not evidence that any particular piece of machinery is justified.
```

The project must determine the useful boundary empirically.

---

## 1. The three levels of project execution

A useful system-level abstraction distinguishes three ways to execute the same substantial data-science project.

### 1.1 Human-executed project

A person or team performs the project directly.

The human process carries responsibilities such as:

```text
understanding the objective
investigating data semantics
choosing what to analyze next
selecting validation strategies
considering methodological alternatives
challenging weak conclusions
tracking assumptions and dependencies
revising prior work when information changes
balancing depth, time, risk, and project value
maintaining project memory
```

The quality of the project depends not only on technical skill, but also on the quality of this process navigation.

### 1.2 Human plus interactive LLM project

A strong LLM becomes a powerful collaborator.

The project may proceed through a long conversation in which the model can:

```text
inspect data
write and execute code
suggest analyses
compare models
explain methods
identify risks
criticize an approach
interpret results
write reports
```

This is already a major increase in capability.

However, the human still commonly performs a large amount of process navigation. The human may need to:

```text
ask whether another approach should be considered
notice that a methodological issue has not been discussed
challenge a validation design
introduce another model or diagnostic
ask for a deeper investigation
clarify project semantics
remember an unresolved assumption
notice that new information affects an earlier conclusion
decide when enough analysis has been performed
keep the project coherent across a long conversation
```

A sufficiently capable LLM may perform many of these tasks proactively, sometimes extremely well. The system-level question is not whether the model can ever do them. It is whether a long-running project should rely on the model surfacing, maintaining, and repairing every material concern correctly through conversational reasoning alone.

### 1.3 System-mediated data-science project

The Autonomous Data Science System operates one level above an ordinary interactive LLM workflow.

The system attempts to externalize and operationalize process intelligence that would otherwise remain implicit in the human-LLM conversation.

Conceptually:

```text
project goals and constraints
        ↓
structured project understanding
        ↓
relevant questions / risks / obligations
        ↓
selected investigations and actions
        ↓
execution and evidence
        ↓
claims and decisions
        ↓
state update and dependency impact
        ↓
next project action or human escalation
```

The important distinction is not simply that more software or more agents exist.

The distinction is that the process itself becomes an explicit object that can be remembered, inspected, constrained, reused, repaired, and improved.

---

## 2. The LLM is not the system

The current project abstraction is:

> The LLM is one reasoning component inside the system, not the complete system itself.

This remains true even if future models become much stronger.

The model may be the most important source of flexible reasoning, but the broader system may still own responsibilities that benefit from persistence, explicit structure, deterministic guarantees, or reusable process knowledge.

A useful conceptual separation is:

```text
                    PROJECT
                       │
                       ▼
              SYSTEM-MANAGED STATE
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     LLM REASONING   CONTROLS    EXECUTION
          │            │            │
          └────────────┼────────────┘
                       ▼
                    EVIDENCE
                       │
                       ▼
                UPDATED PROJECT
                       │
                       ▼
                 HUMAN AS NEEDED
```

The exact boundary can change as model capability changes. That is expected.

If a future LLM reliably performs some task that currently requires explicit system machinery, that machinery may become unnecessary. Conversely, if real projects reveal persistent failures in conversational reasoning, the surrounding system may need stronger explicit support.

The architecture should therefore adapt to evidence rather than defend a fixed design.

---

## 3. What the system is trying to internalize

The long-term goal is not merely to automate Python execution or preserve a chat transcript.

The system should progressively internalize parts of the process-navigation intelligence that a skilled human currently contributes.

Candidate responsibilities include:

```text
methodological memory
project-state maintenance
explicit assumptions and unresolved questions
claim-evidence relationships
dependency tracking
validation and evaluation decision support
feature-eligibility reasoning
prospective safeguards
alternative-analysis generation
state-triggered investigations
repair after evidence or assumptions change
stopping criteria
resource-aware prioritization
selective human escalation
persistent cross-session project memory
reusable knowledge across projects
```

These are not all guaranteed to require dedicated machinery. They are the responsibilities whose useful implementation boundary must be discovered.

The system should not duplicate reasoning merely because it can. If the LLM handles a responsibility reliably and efficiently, explicit orchestration may add no value.

---

## 4. Why an ordinary LLM conversation may still be insufficient

The strongest case for a system is not that an LLM lacks data-science knowledge.

Modern models can already reason about many statistical and machine-learning problems at a high level.

The harder problem is maintaining a high-quality project process over time.

A substantial project may require the system to remember and act on questions such as:

```text
What exactly is the prediction moment?
Which information is available at that moment?
Which population must the validation design represent?
Which assumptions remain unresolved?
Which evidence supports the current model choice?
Which conclusions depend on a now-disputed source?
Which analysis was already tried and rejected?
Which results are valid but stale?
Which artifact supersedes which prior artifact?
Which unresolved issue blocks a downstream claim?
Which further analysis would materially improve the project?
When should the system stop rather than continue experimenting?
```

An interactive LLM can answer each of these questions when prompted.

The system-level challenge is whether the project can maintain them coherently without requiring the human to remember when to ask.

That distinction is fundamental.

---

## 5. Reusable process intelligence

One of the central motivations for the system is that valuable reasoning should not need to be recreated from scratch in every project.

Suppose one project develops a careful understanding of validation choices involving:

```text
chronological holdouts
rolling-origin validation
grouped validation
repeated cross-validation
nested cross-validation
deployment-specific mixtures of known and new entities
```

In a normal conversation, the user may need to remember to raise these possibilities again in a future project.

The intended system should be able to preserve reusable methodological knowledge and activate the relevant parts when project state makes them applicable.

This is not the same as executing every known technique.

The desired process is:

```text
project state
    -> relevant methodological possibilities
    -> applicability reasoning
    -> selected investigation
    -> evidence
    -> decision
```

The durable asset may therefore be less about one orchestration framework and more about an explicit, reusable representation of good data-science reasoning.

---

## 6. The human role is reduced selectively, not eliminated

The project does not define success as complete human removal.

The amount of human involvement should be configurable according to project goals, risk, ambiguity, cost, governance, and user preference.

A useful current abstraction is:

```text
ordinary human + LLM workflow

human = primary process navigator and methodological memory
LLM   = powerful reasoning collaborator


intended system workflow

system = increasingly responsible for process navigation,
         state maintenance, methodological activation,
         safeguards, and repair

LLM    = flexible reasoning engine inside the system

human  = goals, constraints, preferences, authoritative domain input,
         high-value critique, approvals, and intervention where useful
```

The system should escalate when human judgment creates meaningful value, especially when a question is about intent, domain semantics, acceptable tradeoffs, governance, or unresolved consequential ambiguity.

Autonomy should therefore be selective rather than ideological.

---

## 7. What should remain with the LLM

The LLM is particularly valuable for open-ended reasoning where exhaustive hard-coded logic is unrealistic.

Examples include:

```text
understanding ambiguous project language
forming hypotheses
interpreting unusual patterns
generating candidate analyses
reasoning about tradeoffs
explaining results
connecting methodological concepts
recognizing plausible domain mechanisms
suggesting alternatives
synthesizing evidence into conclusions
```

The system should avoid replacing this flexible reasoning with giant deterministic decision trees.

The goal is not to encode all of data science as rules.

A mature architecture is more likely to combine:

```text
LLM reasoning
+ explicit project state
+ reusable methodological knowledge
+ deterministic guarantees where rules are precise
+ executable empirical investigation
+ human judgment where necessary
```

---

## 8. What may belong outside the LLM

Some responsibilities may benefit from system-level guarantees rather than conversational recall.

Examples include:

```text
persistent project state
artifact provenance
final-test protection
permission boundaries
resource limits
state-change history
hard dependency invalidation
execution accounting
reproducible experiment identity
known project constraints
```

The reason is not that the LLM cannot understand these ideas.

The reason is that some properties are easier to guarantee through explicit system structure than through repeated natural-language instruction.

Prototype V0 tests a small subset of this hypothesis.

Future prototypes should continue separating:

```text
things the LLM can reason about reliably
from
things the surrounding system should guarantee or remember explicitly
```

This boundary is one of the central research questions of the project.

---

## 9. Local treatment question versus system-level question

This distinction is essential for interpreting experiments.

### Local treatment question

A controlled prototype can ask:

> For this benchmark mechanism, does explicit operational machinery improve behavior beyond a strong LLM with excellent static prompting?

Prototype V0 is primarily designed to answer this kind of question.

Its B1 condition is deliberately strong because it receives the same methodological principles as P0 without P0's explicit architecture.

If B1 performs just as reliably with substantially lower cost, P0 should not claim that the tested machinery was necessary.

### System-level question

The broader project asks:

> Across substantial, changing, long-running data-science projects, can the system make high-quality project navigation, methodological coverage, state maintenance, repair, and knowledge reuse less dependent on the user remembering and supplying the right reasoning at the right time?

This is a larger question than Prototype V0 can answer.

A local P0 failure may therefore imply:

```text
this mechanism is unnecessary
this mechanism is too expensive
this mechanism is poorly implemented
this benchmark is already easy for a strong LLM
```

It does not automatically imply:

```text
system-level process intelligence has no value
```

Likewise, a local P0 win does not prove the full architecture is generally correct.

It only justifies preserving and testing the mechanisms that earned their complexity.

---

## 10. Why B1 is adversarial to unnecessary architecture

B1 is one of the most important design choices in Prototype V0 because it protects the project from attributing ordinary prompting gains to architecture.

Conceptually:

```text
B0
strong LLM + strong generic instructions

B1
B0 + explicit methodological knowledge in the prompt

P0
same model + explicit system machinery around the same knowledge
```

If P0 only beats B0, the explanation could be that P0 was given better methodological guidance.

If P0 materially beats B1, the case for explicit machinery is stronger.

If B1 matches or beats P0 at lower cost, that is evidence to simplify.

This makes B1 an intentionally difficult control, which is desirable.

---

## 11. Simplification does not mean shrinking the vision

The project should distinguish two very different ideas:

```text
simplify the architecture

versus

reduce the ambition of the system
```

They are not the same.

The long-term vision can remain ambitious while the architecture becomes simpler.

For example, an experiment may reveal that:

```text
explicit dependency tracking is useful
but dynamic knowledge activation adds little
```

A later version should keep dependency tracking and remove or redesign the activation machinery.

Another result may show that:

```text
typed project state is useful
but a complicated runnable-frontier mechanism adds cost without benefit
```

Then the state representation should remain while the frontier is simplified.

The destination remains a high-quality autonomous or semi-autonomous data-science system. The route should become simpler whenever evidence permits.

---

## 12. A likely long-term architecture class

No final architecture is fixed, but the current system-level direction can be summarized as:

```text
                    STRONG LLM
              reasoning and planning
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
 structured project memory   deterministic controls
 facts / assumptions         information boundaries
 questions / evidence        permissions
 claims / decisions          execution limits
 provenance / dependencies   reproducibility rules
          │                         │
          └────────────┬────────────┘
                       ▼
               execution environment
             Python / SQL / tools / data
                       │
                       ▼
                project artifacts
                       │
                       ▼
                 human as needed
```

This diagram should be read as a design class, not a commitment to the exact boxes.

The strongest design principle is that the system should own only the responsibilities that benefit from being explicit outside the LLM.

---

## 13. Questions and claims may be more fundamental than models

A recurring system-level insight is that the system should probably not primarily manage models.

It should manage the evolving analytical questions and claims of the project.

Models are one type of evidence-producing artifact inside that process.

A useful abstraction is:

```text
PROJECT MEANING
    -> LEGITIMATE INFORMATION
    -> VALID ANALYTICAL PROCEDURE
    -> EVIDENCE
    -> CLAIM
    -> TRACEABLE PROJECT STATE
```

This aligns the system with the actual epistemic structure of data science rather than with a narrow model-training pipeline.

The central quality dimensions therefore include:

```text
semantic validity
information legitimacy
evidence validity
claim validity
traceability and dependency integrity
```

These dimensions should survive changes in model family, data modality, provider, or orchestration technology.

---

## 14. The system should learn from project failures

The long-term value of reusable process intelligence becomes strongest across projects.

When one project reveals a systematic weakness, the goal should not be merely to patch that individual project.

The project should ask:

```text
Was this failure project-specific?
Or does it reveal a reusable methodological lesson?
```

Reusable lessons may become:

```text
knowledge components
checks
questions
activation conditions
dependency patterns
evaluation cases
human-escalation rules
```

Over time, diverse projects can therefore expand the system's coverage of good data-science practice.

This remains a hypothesis to test. Knowledge accumulation must itself be governed so the system does not turn isolated mistakes or idiosyncratic cases into universal rules.

---

## 15. Development strategy after Prototype V0

The intended progression is experimental rather than feature-accumulative.

Conceptually:

```text
V0
Which explicit mechanisms add value at all?
        ↓
V1
Keep only mechanisms supported by V0 evidence.
Test broader and harder project situations.
        ↓
V2+
Add or redesign capabilities where new failures demonstrate a need.
        ↓
Long-term system
General project navigation across diverse data-science work.
```

Future coverage should become progressively broader, potentially including:

```text
regression
time series and forecasting
grouped and panel data
class imbalance
feature engineering
unstructured data
causal questions
multiple datasets
external information
human approval points
changing requirements
long-running projects
```

No single prototype should be treated as the final system.

---

## 16. Evidence can justify a smaller architecture

A central success condition of the research process is that experiments must be allowed to produce evidence against the architecture already built.

A useful outcome may be:

```text
B1 is nearly as reliable as P0
P0 uses substantially more tokens
P0 occasionally fails to finish
explicit dependency repair still appears useful
```

The correct response would not be to defend P0 as a whole.

It would be to isolate the mechanism that appears valuable and construct a smaller next architecture around it.

A negative or mixed result can therefore be highly informative.

The prototype is an instrument for discovering the system, not a product that must be preserved.

---

## 17. Preservation hierarchy

This foundation also clarifies how system-level knowledge should be preserved in the repository.

The project already uses layered preservation:

```text
FOUNDATIONS
Durable design knowledge and accepted system-level reasoning.

CHECKPOINTS
Historical records of what was learned, changed, or decided at a moment in time.

CURRENT_STATE
Operational continuity and the immediate next step.

PROTOTYPE README FILES
Simple entry points into a current implementation or experiment.
```

Checkpoint 22 remains valuable because it preserves the historical moment when the distinction among human-executed, human-plus-LLM, and system-mediated projects became explicit.

This foundation promotes that synthesis into the durable design layer so future readers do not need to reconstruct the long-term vision from historical checkpoint logs.

The relationship is therefore:

```text
Checkpoint 22
    historical provenance and original synthesis

Foundation 013
    durable canonical system-level interpretation
```

Neither replaces the other.

---

## 18. Relationship to earlier foundations

This foundation is a synthesis, not a replacement for the earlier conceptual documents.

Relevant foundations include:

```text
docs/foundations/001_initial_vision_and_reasoning.md
    Original broad vision, human gates, reusable modules, adaptive activation,
    persistent state, and development philosophy.

docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
    Detailed project-state and dependency reasoning.

docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
    Knowledge activation and the limits of exhaustive fixed reasoning.

docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
    Reusable knowledge representation.

docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
    Evaluation of trajectories, repair, claims, and changing project state.

docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
    Prototype V0 falsification question and semantic spine.

docs/foundations/012_preregistered_held_out_evaluation_protocol.md
    Frozen held-out comparison of B0, B1, and P0.
```

Foundation 013's role is to keep the broad system-level purpose visible while increasingly narrow prototypes test individual mechanisms.

---

## 19. Current canonical stance

The current project stance can be summarized in five statements.

### 1. A strong LLM can already perform substantial data-science reasoning.

The project should start from this fact rather than design around an artificially weak baseline.

### 2. The remaining opportunity is partly process-level.

Long-running analytical quality depends on navigation, memory, evidence, dependencies, repair, and selective depth, not only on isolated reasoning quality.

### 3. The LLM should remain the flexible reasoning engine where flexibility is valuable.

The system should not attempt to hard-code the entire discipline of data science.

### 4. The surrounding system should earn every responsibility it takes away from ordinary LLM reasoning.

Explicit architecture is justified only when it improves reliability, coverage, efficiency, reuse, traceability, or human-navigation burden enough to warrant its cost and complexity.

### 5. The useful boundary must be discovered empirically.

Prototype V0 and future prototypes exist to learn where that boundary lies.

---

## 20. Governing principle

The project should continue to resist two opposite errors:

```text
ERROR 1
A strong LLM can reason impressively, therefore a larger system adds no value.

ERROR 2
The long-term system vision is ambitious, therefore every orchestration mechanism
is automatically worth keeping.
```

The correct stance remains empirical:

> Build only the system mechanisms that demonstrably improve the reliability, coverage, efficiency, reuse, or human-navigation burden of real data-science work beyond what strong simpler workflows already achieve.

That principle should govern interpretation of Prototype V0, design of subsequent prototypes, and the eventual architecture of the Autonomous Data Science System.
