# Vision

**Status:** Current canonical system vision  
**Last reviewed:** 2026-08-29  
**Authority:** Canonical high-level product/system direction. Detailed rationale, bounded evidence, scoped contracts, historical state and live project status belong in the referenced foundations, research, specifications, checkpoints and `CURRENT_STATE.md`.

## Purpose

The Autonomous Data Science System aims to build a rigorous, adaptive and professionally navigable environment for data-science projects in which a strong LLM is one reasoning component inside a wider system.

Modern LLMs can already inspect data, write and execute code, propose analyses, fit models, interpret results and produce reports. ADS therefore does not exist merely to place an agent around those capabilities.

The higher-level problem is:

> **Which parts of a high-quality data-science process should remain flexible model reasoning, which should become explicit system-owned state, reusable methodological knowledge or deterministic guarantees, and where should human judgment remain authoritative?**

The system should make substantial projects more reliable, inspectable, reusable and easier to navigate without building machinery whose complexity is not justified by evidence.

## Project-relative objective

ADS should create the best defensible data-science process for the particular project.

What "best" means depends on project intent, including goals, constraints, required outputs, risk and desired human involvement. Different projects may legitimately prioritize different combinations of:

```text
predictive or inferential quality
reliability
interpretability
learning value
speed
cost
reproducibility
production readiness
reporting depth
human control
analytical breadth
```

Project-relative optimization happens inside methodological, admissibility and assurance boundaries. A user preference may change the amount or presentation of work, but should not silently turn invalid methodology into acceptable methodology.

## The LLM is a component, not the system

The durable abstraction is:

```text
PROJECT INTENT
      |
      v
ADS-OWNED PROJECT STATE
      |
      +----------------------+----------------------+
      |                      |                      |
      v                      v                      v
methodological          deterministic          provenance /
knowledge               controls               governance
      |                      |                      |
      +----------------------+----------------------+
                             |
                             v
                  bounded methodological horizon
                             |
                             v
                    selective context
                             |
                             v
                      LLM reasoning
                             |
                             v
                    tools / execution
                             |
                             v
                         evidence
                             |
                             v
                    updated project state
                             |
                             v
                  continue / stop / ask human
```

The LLM should remain the flexible reasoning engine where interpretation, synthesis, planning, hypothesis generation, semantic understanding and trade-offs matter.

The surrounding system may own responsibilities that benefit from persistence, provenance, reproducibility, deterministic enforcement, retrieval, state transitions, governance and human inspection.

The useful boundary must be discovered empirically rather than assumed.

Primary source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

## Persistent project state is different from model context

Prototype V0 produced a strong falsification signal against the tested P0 architecture. The most important surviving lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

A serious project may need large persistent memory while any one reasoning call should receive only the context that is relevant to its task.

The system should therefore support:

```text
large persistent project state
    +
reusable methodological knowledge
    +
bounded project-specific retrieval
    +
explained MethodologicalHorizon
    +
selective task-specific context assembly
```

Specification 014 provides bounded evidence that selective exact-revision context can preserve the frozen reasoning obligations while materially reducing provider input. That result supports the direction, not a universal context budget or final retrieval strategy.

Authoritative V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

## The target product is a professional data-science operating environment

ADS is intended to become a persistent project environment rather than a one-shot analysis generator or a prettier chat interface.

A user should be able to provide project material such as:

```text
project briefs and documentation
datasets
existing notebooks or code
business or domain material
source evidence
other relevant artifacts
```

and work inside an environment that helps maintain:

```text
project intent and definitions
questions and unresolved ambiguity
methodological options
recommendations and required concerns
investigations and runs
evidence and findings
claims and decisions
provenance and history
artifacts and deliverables
living report content
```

Conversation remains important, but consequential project meaning should not exist only inside a transcript.

The interface should expose project objects, evidence and methodological state so that the user can inspect, challenge, approve, reject, redirect and deepen the work.

Primary sources:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

## Project Cockpit is the promoted active-work model

The Project Cockpit is the promoted V1 primary immersive active-work model.

Its core idea is:

```text
living project-process map
+
native system interaction
+
spatial focus into real analytical workspaces
```

The user should be able to move between a project-level process view and deeper analytical work without losing the feeling of one coherent project.

Direct specialist views remain useful as alternative inspection, entry and record paths. They should reuse the same substantive project state and analytical modules rather than become unrelated implementations.

The Cockpit is a project-process projection. It should not collapse all of the following into one graph:

```text
project process / reasoning map
data and artifact lineage
methodological knowledge relations
event history
```

Specification 008 governs the promoted interaction architecture. Exact current design-review state belongs in `docs/CURRENT_STATE.md`, not in this vision document.

Primary source:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

## The project model is scientific, not a rigid pipeline

Conventional areas such as Data, EDA, Validation, Features, Models, Experiments, Evaluation and Report remain useful orientation structures.

They should not define one mandatory one-way workflow.

The underlying analytical process is iterative:

```text
Question
    -> Investigation
    -> Run
    -> Evidence
    -> Finding
    -> Claim / Decision
    -> changed project state
    -> new or reopened questions when warranted
```

A later discovery may invalidate or weaken earlier evidence, alter project semantics or make a previously irrelevant methodological concern important.

The project model therefore distinguishes:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

and preserves distinctions such as:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
```

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

## Methodological navigation is the central intelligence problem

The hardest long-term problem is not mechanically fitting a model or generating a chart. It is deciding, given the current project state:

```text
what questions matter?
what methods or investigations exist?
which are applicable?
which are relevant?
which should be recommended now?
which are required for validity?
which are redundant or low value?
what context is missing?
what should be deferred?
what evidence is sufficient?
what changed enough to require re-evaluation?
when should the system stop?
when should the human be involved?
```

The current durable conceptual progression is:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

A broad methodological knowledge universe should be narrowed into a bounded project-specific `MethodologicalHorizon` before detailed prioritization and model-facing reasoning context are assembled.

The system should make it possible to distinguish what it knows, what is applicable, what is unresolved because context is missing, what is task-relevant, what is recommended, what is required and what was omitted or deferred and why.

Primary source:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

## Reusable methodological knowledge should be explicit without becoming rigid

A long-term intellectual asset of ADS is a governed representation of reusable data-science reasoning that is independent of any one model provider, agent framework or database.

Promoted concepts include:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
ExecutionCapability
```

Important separations include:

```text
intrinsic knowledge kind != reasoning function
asset != component != narrative facet
static relation != conditional methodological rule
retrieval cue != applicability predicate != required context != project relevance
methodological meaning != software implementation
global knowledge != project-specific state
internal representation != human-facing workflow
```

The system should formalize structure where structure improves reliability, provenance, governance, retrieval or deterministic behavior, while retaining narrative and flexible reasoning where formalization would be brittle.

Primary source:

```text
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

## The Methodological Knowledge Universe and Source Universe are distinct

ADS should distinguish the evidence artifacts it can consult from the reusable methodological knowledge it has accepted.

```text
SOURCE UNIVERSE
    external evidence artifacts and exact source provenance

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable methodological knowledge derived from evidence,
    reasoning and review
```

The Source Universe owns durable source identity, exact artifact identity, integrity, lineage, rights/access information and recoverable storage semantics. It does not automatically create accepted methodological authority.

The Methodological Knowledge Universe owns reusable methodological assets, relations, rules, narrative, revisions, provenance and governance.

This distinction allows source evidence to remain inspectable and exact while accepted reusable knowledge can evolve under explicit review.

Primary sources:

```text
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

## Deterministic software and model reasoning should be used selectively

The presence of an LLM does not imply that every responsibility should become an agent task.

Prefer deterministic software where requirements can be expressed reliably as:

```text
typed application logic
database integrity
explicit rule evaluation
reproducible execution
permission and control logic
mechanical validation
exact revision validation
canonical serialization
```

Use model reasoning where genuine ambiguity, interpretation, synthesis, prioritization or open-ended judgment makes it valuable.

The same complexity discipline applies to agent architecture. Begin with one capable reasoner plus bounded context and well-defined tools. Add specialist agents only when evidence shows the simpler design is insufficient.

Agent frameworks and interoperability protocols are infrastructure, not domain authority. ADS project semantics, methodological knowledge, governance and provenance remain behind ADS-owned boundaries.

The accepted initial V1 runtime uses the OpenAI Agents SDK behind an ADS-owned `ReasoningRuntime` port. That is an implementation decision, not a permanent claim that one framework or provider defines the system.

## Human involvement should be selective and valuable

The goal is not complete human removal.

Human involvement should depend on factors such as:

```text
project intent
semantic ambiguity
risk and consequence
admissibility
authority
uncertainty
reversibility
cost
user preference
```

The system should automate routine, well-defined work where appropriate while preserving strong human control over goals, definitions, consequential trade-offs, domain clarification, approvals, critique and intervention.

Exact autonomy and escalation policy remains an open design problem.

## The professional developer workbench remains first-class

ADS should complement, not replace, the professional developer environment.

A useful responsibility split is:

```text
Autonomous Data Science System
    project/process control, memory and methodological reasoning

VS Code or another professional IDE
    developer workbench

Python / containers / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration and code provenance
```

Generated analytical code should remain ordinary, readable, reproducible and independently runnable project code.

If ADS disappeared, the resulting project repository should still be a credible professional data-science project.

## Admissibility, epistemic integrity and risk-sensitive assurance remain constitutional concerns

The project continues to distinguish conceptually:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project-relative optimization
```

The current epistemic core centers on:

```text
semantic validity
information legitimacy
evidence validity
claim validity
traceability and dependency integrity
```

The exact admissibility model, assurance model, uncertainty representation, review policy and system-wide completion criteria remain open and should be developed through evidence rather than prematurely frozen.

Current unresolved questions are maintained in:

```text
docs/OPEN_QUESTIONS.md
```

## Evaluation must test scientific behavior and system value

ADS should not be evaluated only by final predictive performance.

Relevant system qualities include:

```text
methodological coverage
critical omissions
unnecessary work
claim/evidence integrity
reproducibility
repair after changing evidence
human reminders/interventions required
resource use and context cost
recommendation quality
project navigation quality
professional usability and accessibility
```

Appropriate evaluation may include:

```text
deterministic assertions
controlled experiments
behavioral trajectory analysis
blinded semantic review
retrieval and recommendation benchmarks
cross-platform technical gates
human product review
project replay
real-project regression cases
```

Mechanisms should be removed, simplified or revised when evidence does not justify their complexity.

## Current accepted V1 architectural direction

Without treating this section as live project status, the following are durable accepted V1 directions:

```text
local-first relational persistence
    D-028, D-029

reproducible Python/dependency tooling
    D-030

deterministic governed knowledge interchange
    D-031 / Specification 004

ADS-owned reasoning-runtime boundary
    D-032 / Specification 005

promoted Project Cockpit interaction architecture
    Specification 008

retrieval -> explained Horizon -> selective exact-revision context
    Specifications 009-014

ADS-owned private Source Universe substrate
    D-033 / Specification 023

governed provider-neutral development collaboration
    D-034 / Specification 024
```

These are scoped decisions, not declarations that the final production implementation is complete.

## Boundary of this document

This file should remain stable enough to explain the project even when the active branch, checkpoint, experiment or human-review gate changes.

Therefore:

```text
long-term system direction          -> VISION.md
cross-project working principles    -> PRINCIPLES.md
accepted explicit decisions         -> DECISIONS.md
important unresolved questions      -> OPEN_QUESTIONS.md
live project state and next action  -> CURRENT_STATE.md
semantic knowledge discovery        -> KNOWLEDGE_MAP.md
```

The vision should evolve when experiments, real projects, product testing or improved model capability materially change the target system. It should not be edited merely to follow every local development step.

## Primary durable sources

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md

docs/PRINCIPLES.md
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
```
