# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-19

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current stage

docs/CURRENT_STATE.md
    concise present state and exact next priority

docs/KNOWLEDGE_MAP.md
    routing layer for important project knowledge

docs/VISION.md
    current system purpose and vision

docs/PRINCIPLES.md
    current design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved canonical questions

docs/DEVELOPMENT_METHOD.md
    how the project is developed and preserved

docs/CONTINUITY.md
    how work continues across sessions and the standardized new-chat prompt

docs/MAJOR_CHANGES.md
    selective structural history
```

Prototype V0 is complete. Its final classification is **strong falsification of the current P0 design**. It is no longer an active execution stage.

---

## System purpose and long-term vision

Read:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

Foundation 013 explains why the LLM is one reasoning component inside a wider system rather than the whole system.

Foundation 017 makes the target product concrete as a professional interactive data-science workspace that should carry much of the methodological-navigation burden while preserving deep human interaction and control.

Historical origin:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

---

## Professional interactive workspace

Primary source:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

The target product is not an upload-to-final-answer black box and not merely a prettier chat interface.

Key ideas include:

```text
professional project workspace
recommended analyses
relevant option space
full knowledge catalog
configurable human involvement
living project memory
living reports
project replay evaluation
```

EDA is the current concrete reference example.

---

## Product object model, developer workflow, VS Code, Git/GitHub, and execution

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

The candidate product model separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Candidate object families include:

```text
Project / IntentItem
Artifact / Dataset / Variable
Question / Assumption / Finding / Claim
Method / methodological knowledge
Proposal / Investigation / Run / Evidence / Decision
Report / ReportSection
Event / Relation
```

Important distinctions:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

Professional workflow principles:

```text
docs/PRINCIPLES.md, P-023 and P-024
```

Responsibility split:

```text
Autonomous Data Science System
    project/process control plane

VS Code
    developer workbench

Python / Docker / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration, and code provenance
```

Generated consequential code should remain independently runnable, professional, and maintainable. System-triggered and manually triggered runs should preferentially share the same reproducible execution contract.

Git/GitHub are first-class for source history and provenance, but not intended to store every large dataset or model artifact.

---

## Methodological-navigation brain and relevance architecture

**Read first for the current design task:**

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

This is the current promoted source for how the system may transform broad reusable data-science knowledge into a project-specific methodological horizon.

The brain is broader than a method registry. Candidate reusable knowledge types include:

```text
methods
question templates
decision frameworks
invariants / hard rules
failure modes
investigation patterns
interpretation knowledge
follow-up / dependency knowledge
```

Current relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Important concepts:

```text
methodological horizon
explicit prerequisite filtering where reliable
flexible reasoning for semantic relevance/tradeoffs
inspectable recommendation rationale
project-signal visibility
ranking by validity importance, information value, impact, cost, risk, redundancy, and user preference
knowledge provenance / scope / maturity / counterexamples
separation of methodological meaning from execution templates
open-world discovery of knowledge gaps
```

The full global catalog should not be sent to the LLM. Project-specific retrieval should produce a small relevant slice.

The next design exercise is to test the reusable representation against deliberately different examples:

```text
Histogram
Missing-data investigation
Temporal validation
Random Forest
Prediction-time feature eligibility
```

No V1 implementation stack has been accepted.

---

## Reusable knowledge foundations

Earlier theory:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Post-V0 product interpretation:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

B1 gained most of the semantic benefit from the four methodological concepts simply being explicitly available. P0's path-sensitive activation and always-on context did not earn their cost.

This does **not** reduce future reusable knowledge to a static prompt. Foundation 019 instead explores selective retrieval, explicit filtering, flexible semantic reasoning, and inspectable ranking.

---

## Project state, dependencies, and orchestration

Broad theory:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

V0 implementation:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
```

Final V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Interpretation:

```text
broad state/dependency theory remains an open design space
!=
current P0 always-on representation is justified

what the system persists
!=
what an LLM receives on every turn

current project state
!=
event history
```

---

## Epistemic integrity, admissibility, risk, and project constitution

Read:

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/VISION.md
docs/PRINCIPLES.md
```

These sources govern semantic validity, information legitimacy, evidence validity, claim validity, traceability/dependency integrity, admissibility, and risk-sensitive assurance.

---

## Project initialization

Read:

```text
docs/foundations/005_project_initialization_and_universal_bootstrap.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## System evaluation and behavioral regression

Read:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

For broader post-V0 evaluation, Foundation 017 introduces project replay and mixed quantitative/qualitative measures such as recommendation coverage, critical omissions, human reminder burden, state-recall failures, reproducibility, and expert judgment.

---

## Prototype V0 final result

Authoritative report:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Frozen protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Quick overview:

```text
prototype_v0/README.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Central comparison:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
incremental P0 gain: +0.05

B1 completed within budget: 10/10
P0 completed within budget: 3/10

P0/B1 median token ratio: 2.160
```

Do not tune or restart P0 against the completed V0 benchmark.

---

## Held-out supervision and mechanical verification

Read:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

These evaluation-infrastructure components are separate from the falsified P0 semantic treatment.

---

## Execution and observability separation

Canonical principle:

```text
docs/PRINCIPLES.md, P-022
```

Deep rationale:

```text
docs/foundations/016_execution_observability_separation.md
```

Pattern:

```text
execution / reasoning
    -> persisted state/events
    -> read-only observability
    -> human interface
```

---

## Knowledge preservation and session continuity

Current preservation method:

```text
docs/DEVELOPMENT_METHOD.md
```

Standardized new-chat procedure and first prompt:

```text
docs/CONTINUITY.md
```

Deep preservation rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

Current session rotation checkpoint:

```text
docs/checkpoints/099_methodological_navigation_brain_promoted_and_session_rotation_recommended.md
```

The current chat is intentionally being rotated before reaching the platform length limit. The repository is sufficient for reconstruction without a manual transcript handoff.

Recommended next chat title:

```text
02 - Methodological Brain & Knowledge Units
```

---

## Current unresolved questions

```text
docs/OPEN_QUESTIONS.md
```

Several older V0-related statuses still require the planned post-V0 reconciliation. `CURRENT_STATE.md` and the final V0 report govern current interpretation in the meantime.

---

## Repository authority model

Default order when documents disagree:

```text
1. frozen current specifications/contracts for their declared scope
2. current accepted decisions and canonical specifications
3. current vision/principles/current-state material
4. final experiment reports for their declared experiment scope
5. foundational design memos for rationale and durable hypotheses
6. checkpoints for historical state
7. raw historical material for provenance
```

---

## Exact next step

Open the next design chat and reconstruct from the repository.

Then design the reusable knowledge-unit representation using:

```text
Histogram
Missing-data investigation
Temporal validation
Random Forest
Prediction-time feature eligibility
```

Determine the common core, typed extensions, applicability/prerequisite representation, alternatives/complements/failure modes/follow-ups, and the boundary between methodological knowledge and executable implementation.

Do not select a database, retrieval engine, graph store, vector store, agent framework, or V1 backend yet.