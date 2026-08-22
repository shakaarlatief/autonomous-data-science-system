# Vision

**Status:** Current canonical system vision  
**Last reviewed:** 2026-08-22  
**Authority:** Canonical high-level product/system direction. Detailed rationale and narrower design contracts live in the referenced foundations, decisions, research memos, specifications, checkpoints, and current-state documents.

## Purpose

The Autonomous Data Science System project aims to build a more rigorous, adaptive, reusable, and professionally navigable way to conduct data science with large language models than a single end-to-end conversational workflow.

Modern LLMs can already perform substantial parts of a data-science project. They can inspect data, write and execute code, propose analyses, fit models, interpret results, compare alternatives, and produce reports.

That capability is the starting point, not the problem statement.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The system exists to make the process itself more reliable, inspectable, reusable, and easier to navigate across substantial projects without building unnecessary machinery around tasks a strong simpler workflow already handles well.

---

## Working purpose

The current working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The system therefore does not optimize one universal objective such as maximum predictive performance, maximum automation, maximum analytical breadth, minimum cost, or minimum completion time.

Different projects may legitimately prioritize different combinations of:

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

Project-relative optimization occurs inside validity, admissibility, and assurance boundaries. User preference may change how much work is performed or how it is presented, but it should not silently make invalid methodology acceptable.

---

## The LLM is a component of the system, not the whole system

The current system-level abstraction is:

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

The LLM should remain the flexible reasoning engine where interpretation, synthesis, planning, hypothesis generation, semantic understanding, trade-offs, and open-ended judgment matter.

The surrounding system may own responsibilities that benefit from explicit persistence, provenance, reproducibility, deterministic enforcement, bounded retrieval, selective context construction, or durable project semantics.

The useful boundary must be discovered empirically rather than assumed.

Primary source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## The strongest empirical constraint from Prototype V0

Prototype V0 directly tested one explicit architecture against strong simpler controls and produced a strong falsification signal against the tested P0 design.

The most important architectural lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Persistent project memory and reusable methodological knowledge remain central hypotheses.

What should not be carried forward unchanged is P0's expensive pattern of repeatedly serializing large structured state, broad relation/frontier context, path-sensitive activation machinery, and generic recursive reopening logic into the reasoning loop when a strong simpler baseline achieved nearly the same semantic result at far lower cost.

The system should therefore prefer selective context assembly and mechanism-specific evidence over large always-on orchestration machinery.

Authoritative V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Target product experience

The intended product is a **professional interactive data-science operating environment** rather than a one-shot analysis generator or a prettier chat interface.

A user should be able to provide project material such as:

```text
project brief
README / documentation
datasets
existing notebooks or code
business/domain material
other relevant artifacts
```

and enter a persistent project environment in which the system helps maintain:

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

The product should expose data-science objects and methodological state directly so the user can inspect, challenge, approve, reject, redirect, and deepen the work.

Primary sources:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

---

## Project Cockpit as the current primary active-work direction

The current product direction uses the **Project Cockpit** as the promoted V1 primary immersive active-work model.

The Cockpit combines:

```text
living project-process map
+
native system interaction
+
spatial focus into real analytical workspaces
```

The user should be able to move from the project map into Data, EDA, Validation, Features, Modeling, Evaluation, evidence, decisions, and other deep work while retaining the feeling of one continuous project environment.

Direct specialist views remain useful as alternative inspection, entry, and record paths. They should reuse the same substantive analytical modules rather than becoming separate implementations.

The Cockpit is a derived project-process projection. It should not collapse all of these into one graph:

```text
project process / reasoning map
data and artifact lineage
methodological knowledge relations
event history
```

Specification 008 is the promoted interaction contract. It includes bounded 2D navigation, geometric zoom and recovery, native laptop pinch capability, viewport-aware orientation, scalable Jump/search, compact immersive chrome, collision-safe floating surfaces, true fullscreen, URL-addressable focus state, keyboard accessibility, reduced-motion support, and restrained world-owned ambient depth.

Checkpoint 130 records later bounded normal-window/pinch polish that is accepted as good enough to continue. Final visual identity, canvas/gesture libraries, auto-layout, semantic zoom, minimap, final stage taxonomy, final URL contract, production project-search backend, final frontend stack, and final chart library remain intentionally open.

Primary source:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

---

## The project should be organized around scientific meaning, not a rigid pipeline

Conventional areas such as:

```text
Data
EDA
Validation
Features
Models
Experiments
Evaluation
Report
```

remain useful user-facing workspaces and orientation structures.

They should not define one mandatory one-way project pipeline.

The underlying process is expected to be iterative:

```text
Question
    -> Investigation
    -> Run
    -> Evidence
    -> Finding
    -> Claim / Decision
    -> changed project state
    -> new or reopened Questions when warranted
```

A later discovery may invalidate or weaken earlier evidence, alter project semantics, or make a previously irrelevant methodological concern important.

The project model therefore distinguishes Objects, Relations, Events, and Views rather than treating stages as independent backend silos.

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## Methodological navigation is the central intelligence problem

The hardest long-term problem is not mechanically computing a histogram, fitting a Random Forest, or running a statistical test.

It is deciding, given the current project state:

```text
what questions matter?
what methods or investigations exist?
which are applicable?
which are relevant?
which should be recommended now?
which are required for validity?
which are redundant or low value?
what context is still missing?
what should be deferred?
what evidence is sufficient?
what changed enough to require re-evaluation?
when should the system stop?
when should the human be involved?
```

The current relevance architecture is:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

A large global methodological knowledge universe should be narrowed into a bounded project-specific **MethodologicalHorizon** before detailed prioritization and reasoning context are assembled.

The user should be able to distinguish at least:

```text
what the system knows
what is applicable
what is unresolved because context is missing
what is task-relevant
what is recommended
what is required
what was omitted or deferred and why
```

Primary source:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

---

## Reusable methodological knowledge should be explicit but not rigid

The long-term intellectual asset may be an explicit, governed representation of reusable data-science reasoning rather than any particular LLM provider, agent framework, or database.

Current promoted concepts include:

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
static semantic relation != conditional methodological rule
retrieval cue != applicability predicate != required context != project relevance
methodological meaning != software implementation
global knowledge != project-specific state
internal representation != human-facing workflow/tree
```

The system should be structured where structure improves reliability, provenance, governance, retrieval, or deterministic behavior, and retain narrative/flexible reasoning where formalization would be brittle or artificial.

Primary source:

```text
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## Retrieval, horizon construction, and selective context are separate responsibilities

Current V1 evidence supports an explicit staged boundary rather than one monolithic knowledge call:

```text
accepted global methodological knowledge
    -> retrieval candidates
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> task-specific relevance selection
    -> exact MethodologicalContextPack
```

The first production lexical channel passed its frozen lexical benchmark. An exact dense comparator demonstrated complementary semantic signal rather than replacement of lexical retrieval. A bounded RRF comparator preserved both measured semantic signals. The first MethodologicalHorizon then validated accepted-current one-hop relation expansion and three-valued applicability with the executable invariant:

```text
unknown != false
```

The first RH-C selector subsequently demonstrated that, on a deliberately wide ten-asset Horizon, explicit task reasoning functions plus bounded `REQUIRES_CONCEPT` support could preserve all frozen required exact revisions while reducing canonical model-facing context by approximately 65% to 84%.

The important architecture is:

```text
SYSTEM
    may retain wider project/methodological state
    may retain omission and audit evidence

MODEL-FACING CONTEXT
    receives only selected exact methodological revisions
```

Specification 013 v1.0 accepts this bounded seam.

This does **not** establish that reasoning functions solve general relevance, that the benchmark budget is universal, or that selective context improves real reasoning. Those are downstream questions.

Primary evidence:

```text
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

---

## Evidence requirements and methods are different things

A recurring design conclusion is:

```text
what must become known or demonstrated
    !=
which method can produce that evidence
```

For example, the project may need to understand a variable's empirical distribution without requiring a histogram specifically. A project may need deployment-representative evaluation evidence without prescribing one universal validation algorithm.

This separation allows the system to reason about alternatives and avoid turning methodological requirements into rigid recipes.

---

## Deterministic software and agent reasoning should be used selectively

The system should not turn every responsibility into an LLM or agent task.

Prefer deterministic software where the requirement can be expressed reliably as:

```text
typed application logic
database integrity
explicit rule evaluation
reproducible execution
permission/control logic
mechanical validation
exact revision validation
canonical serialization
```

Use LLM/agent reasoning where genuine ambiguity, interpretation, synthesis, prioritization, or open-ended judgment makes it valuable.

This principle also applies to agent architecture itself. Begin with one capable reasoner plus bounded context and well-defined tools. Add specialist agents only when evaluation demonstrates that the simpler design is insufficient.

Agent frameworks, MCP, AG-UI, A2A, and runtime checkpointing are infrastructure/interoperability mechanisms. They must not become the authority for ADS project objects or methodological semantics.

Current runtime decision:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port
```

Direct model calls remain the fallback/reference path. LangGraph remains a future stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

Primary sources:

```text
docs/PRINCIPLES.md, P-027 through P-029
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

---

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

The system should automate routine, well-defined work where appropriate while preserving strong human control over goals, definitions, consequential trade-offs, domain clarification, approvals, critique, and intervention.

Guided, semi-autonomous, and more autonomous interaction remain useful product concepts, but the final autonomy/escalation policy is still open.

---

## Project memory, LLM context, and historical provenance are distinct

A mature project may contain large amounts of durable information:

```text
facts
Definitions
Questions
Assumptions
Investigations
Runs
Evidence
Findings
Claims
Decisions
artifacts
knowledge revision references
history
```

That information may be necessary for project reconstruction without being relevant to every reasoning call.

The system should therefore support:

```text
large persistent memory
    +
bounded project-specific retrieval
    +
explained methodological horizon
    +
selective task-specific context assembly
```

Consequential reasoning should preserve enough provenance to identify which project state and methodological knowledge revisions influenced it.

The successful RH-C gate strengthens this direction mechanically, but the next experiment must still establish its effect on actual model reasoning quality and exact provider-token burden.

---

## Professional developer workflow should remain first-class

ADS should complement, not replace, the professional developer workbench.

Current conceptual responsibility split:

```text
Autonomous Data Science System
    project/process control and reasoning environment

VS Code
    developer workbench

Python / containers / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration, and code provenance
```

Generated project code should remain ordinary, readable, reproducible, independently runnable code.

System-triggered execution and manual execution should preferentially share the same reproducible run contract.

If the ADS interface disappeared, the resulting project repository should still be a credible professional data-science project.

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## Admissibility, epistemic integrity, and risk-sensitive assurance remain part of the long-term constitution

The project continues to distinguish conceptually:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project-relative optimization
```

The current epistemic core is organized around strong hypotheses concerning:

```text
semantic validity
information legitimacy
evidence validity
claim validity
traceability and dependency integrity
```

The exact admissibility model, assurance model, uncertainty representation, review policy, and system-wide completion criteria remain open and should be developed through later evidence rather than prematurely frozen.

These unresolved areas remain visible in:

```text
docs/OPEN_QUESTIONS.md
```

---

## Evaluation must test both scientific behavior and system value

The project should not evaluate success only through final predictive performance.

Relevant system qualities include:

```text
methodological coverage
critical omissions
unnecessary work
claim/evidence integrity
reproducibility
repair after changing evidence
human reminders/interventions required
resource use
context cost
recommendation quality
project navigation quality
professional usability
accessibility
```

Evaluation should combine methods appropriate to the question:

```text
deterministic assertions
controlled experiments
behavioral trajectory analysis
blinded semantic review
retrieval/recommendation benchmarks
cross-platform technical gates
human product review
project replay
real-project regression cases
```

A mechanism should be removed or simplified when evidence does not justify its complexity.

The immediate next experiment should directly test whether selective methodological context earns value at the model-reasoning layer rather than assuming that mechanical compression is sufficient.

---

## Current V1 implementation boundary

The project has moved beyond purely conceptual design, but V1 remains deliberately bounded.

Accepted V1 boundaries currently include:

```text
D-028
    SQLite-centered local-first operational persistence

D-029
    SQLAlchemy Core + Alembic

D-030
    pyproject.toml + uv + committed uv.lock + uv_build

D-031
    JSON + JSON Schema + semantic validation
    + deterministic knowledge interchange

D-032
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Specification 008
    promoted Project Cockpit interaction architecture

Specification 012 v1.0
    accepted first explained MethodologicalHorizon seam

Specification 013 v1.0
    accepted first deterministic selective MethodologicalContextPack seam
```

Still deliberately unselected or under evaluation are major areas such as:

```text
final LLM provider/model
natural-language task -> reasoning-function mapping
final semantic relevance mechanism
recommendation / REQUIRED-BLOCKING policy
final Horizon and context budgets
production semantic retrieval/fusion stack
embedding/reranking infrastructure
final frontend stack promotion
chart system
Cockpit canvas/gesture implementation dependencies
complete project schema
execution backend at production scale
artifact storage and job infrastructure
multi-agent architecture
```

Current accepted decisions are recorded in:

```text
docs/DECISIONS.md
```

Current implementation and product priorities are recorded in:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

---

## Current boundary of the vision

The long-term ambition remains broad: a professional autonomous or semi-autonomous data-science system that can navigate heterogeneous projects while preserving methodological integrity, evidence, provenance, human control, and reusable learning.

The development strategy remains deliberately incremental:

```text
clarify product/system responsibility
    -> derive requirements
    -> compare alternatives
    -> implement the smallest justified slice
    -> falsify/test it
    -> preserve evidence
    -> promote only what survives
    -> repeat on harder and broader project situations
```

The immediate methodological boundary is now a real reasoning vertical slice. It should hold the project/task evidence and model configuration constant while comparing the accepted selective `MethodologicalContextPack` against a strong full-Horizon/simple control. That experiment should measure reasoning quality, exact supplied knowledge revisions, exact model/provider tokens, latency/cost where observable, and whether context omission or context overload creates real failures.

The vision should continue to evolve when experiments, real projects, product testing, or improved model capability show that a responsibility belongs somewhere else.

## Primary durable sources

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/PRINCIPLES.md
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```
