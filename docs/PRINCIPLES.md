# Principles

These are the current working principles of the Autonomous Data Science System project.

They are more stable than raw ideas or design hypotheses, but they are not immutable. If later projects or experiments show that a principle is incomplete or wrong, it should be revised explicitly rather than silently ignored.

## P-001. The repository is the persistent source of truth

Chat is used for thinking, exploration, criticism, and design work. The repository preserves the current accepted state of the project.

A future session must be able to reconstruct the project from repository artifacts without depending on hidden memory or access to the full original conversation.

## P-002. Preserve both distilled knowledge and rich reasoning

Important ideas should be represented at more than one level of detail.

Canonical documents should make the current state easy to consume. Foundational design memos should preserve the deeper reasoning, examples, distinctions, motivations, and failure modes that explain why important ideas were introduced.

Compression should improve usability without destroying intellectual context.

## P-003. Historical material is provenance, not automatic authority

Old conversations, session records, and earlier design memos are valuable because they explain how the project evolved.

They should not automatically override current canonical documents. When historical material conflicts with later accepted decisions, the current accepted state takes precedence.

## P-004. Evidence should dominate unsupported LLM judgment when a question is empirically testable

LLM reasoning is useful for proposing hypotheses, identifying risks, designing analyses, and interpreting results.

When an important question can be resolved through a valid experiment or diagnostic, the system should prefer evidence over rhetorical agreement between agents or models.

## P-005. Important assumptions should be explicit

Analytical decisions often depend on assumptions about the data-generating process, deployment environment, target definition, prediction timing, missingness, group structure, costs, or other project conditions.

The system should expose consequential assumptions rather than silently embedding them in code or prose.

## P-006. The workflow should be adaptive rather than globally linear

Conventional project stages such as problem understanding, EDA, preprocessing, modelling, evaluation, and reporting remain useful organizational concepts.

They should not become a rigid one-way pipeline. Later findings must be able to trigger earlier investigations, invalidate prior experiments, or change the interpretation of the problem.

## P-007. Relevant investigations should be activated by project facts

The system should maintain broad analytical capability without executing every possible check on every project.

Project characteristics and discoveries should determine which questions, modules, tests, and reviewers become relevant.

This principle supports both quality and efficiency.

## P-008. Use a hybrid reasoning architecture

Not all data science knowledge should be handled in the same way.

The system should be able to combine:

1. hard constraints or invariants for practices that should not depend on creative judgment once their conditions are known;
2. explicit decision frameworks for recurring situations with multiple legitimate branches;
3. open-ended reasoning for novel, ambiguous, or domain-specific questions that cannot be exhaustively enumerated in advance.

The exact implementation of this hybrid architecture remains undecided.

## P-009. Important decisions should be challengeable

Consequential analytical choices should be reviewable rather than accepted solely because the component that proposed them sounded confident.

Depending on project depth and risk, review may include methodological criticism, specialized checks, proposer-reviewer separation, or independent replication.

## P-010. The system should distinguish claims, hypotheses, decisions, and uncertainty

A plausible idea is not the same as an established fact.

The system should preserve the status of important conclusions and, where useful, their confidence, evidence, alternatives, dependencies, and unresolved uncertainty.

## P-011. Human attention should be used where it creates value

The purpose of autonomy is not to eliminate the human.

Routine and well-defined work should be automated where appropriate. Human involvement should be concentrated on questions where semantics, objectives, trade-offs, domain knowledge, ethics, or genuinely ambiguous evidence make human judgment valuable.

## P-012. The system should be project-aware, not method-first

The correct analysis depends on what one observation represents, how the data were collected, when predictions are made, what information is available at prediction time, and how the output will be used.

Methods should follow from the project structure rather than being applied merely because they are available.

## P-013. Evaluation design is part of the scientific question

Train, validation, and test construction should reflect the actual inference or deployment problem.

Random splitting, grouped splitting, temporal splitting, rolling validation, or other schemes are not interchangeable implementation details. The system should reason explicitly about which evaluation design matches the project.

## P-014. Reproducibility and provenance should be built into the process

Important results should be traceable to the data version, code, configuration, preprocessing, validation design, model, random state where relevant, and decision context that produced them.

The final report should not be the only record of how a result was obtained.

## P-015. Reporting should emerge from documented reasoning

The system should create evidence, decisions, interpretations, and experiment records throughout the project.

Final reports should be assembled from an already documented analytical process rather than reconstructed from memory after modelling is complete.

## P-016. Real projects are coverage tests for the system

The system should be tested on heterogeneous real or realistic projects.

Each project should reveal whether the current reasoning process identifies the right questions, activates the right investigations, avoids irrelevant work, requests human input appropriately, and produces reliable conclusions.

## P-017. Generalize lessons instead of patching only one project

When a project exposes a system weakness, the first question should be whether the lesson is generalizable.

General lessons should become reusable knowledge, triggers, safeguards, tests, or design revisions so that future projects benefit.

## P-018. Efficiency should come from selective depth, not from premature simplification

A sophisticated system does not need to run every possible analysis.

It should spend effort where evidence, uncertainty, risk, and expected value justify it. Quick, standard, and research-depth work may require different levels of investigation, review, and compute while following the same underlying reasoning principles.

## P-019. Simplicity is preferred when evidence does not justify complexity

When two approaches perform similarly within relevant uncertainty and one is materially simpler, easier to reproduce, easier to interpret, or easier to deploy, the system should be able to prefer the simpler option.

Complexity should have an evidential reason.

## P-020. The system must be able to revise itself

Both the target data science system and the methodology used to design it are expected to evolve.

New project cases, failures, tools, research findings, and better abstractions may require changes to the architecture, documentation method, knowledge representation, or principles themselves.

Evolution should be explicit and traceable rather than accidental.

## P-021. The meaning of a good project is project-relative

The system should create the best data-science process for the particular project rather than optimize one universal objective across all projects.

What "best" means should depend on project intent, including goals, constraints, required outputs, and desired human involvement. Predictive performance, autonomy, speed, cost, interpretability, learning value, production readiness, and analytical depth may all matter, but their relative importance can differ by project.

Project-specific priorities should shape the process without silently redefining invalid methodology as acceptable. The exact boundary between configurable priorities and non-negotiable methodological standards remains under active design.

## P-022. Separate execution from observability

Long-running reasoning, analytical execution, orchestration, and evaluation processes should persist structured state or events that can be observed by separate read-only interfaces.

The execution path should own correctness, state transitions, and safety decisions. Observability should own timestamps, heartbeats, progress rendering, elapsed-time display, dashboards, and other human-facing presentation.

An observer should be startable, stoppable, replaceable, or allowed to fail without changing execution semantics. It must also respect information boundaries such as experimental blinding and must not expose privileged state merely because it is convenient to display.

Minimal lifecycle output from an execution process remains acceptable, but detailed monitoring should preferentially be a downstream projection of persisted state rather than part of the trusted execution surface.

See `docs/foundations/016_execution_observability_separation.md`.

## P-023. The system should complement the professional developer workbench rather than replace it

The Autonomous Data Science System should own project understanding, methodological navigation, process orchestration, provenance, and interactive project control without trying to recreate a full code editor and debugging environment inside the product.

Professional tools such as VS Code should remain first-class ways to inspect, edit, debug, and manually execute the same underlying project. The system workspace and the developer workbench should therefore interoperate around one coherent project rather than create unrelated copies or competing sources of truth.

Project orchestration, code editing, execution, and version control are distinct responsibilities even when they are tightly integrated in the user experience.

See `docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md`.

## P-024. Generated project code should remain independently runnable and professionally maintainable

Analytical code created or maintained by the system should remain normal project code rather than hidden logic that only functions through the system UI.

Where consequential work is promoted into project code, it should aim to be readable, modular, reproducible, configurable, documented, tested where appropriate, and version controlled. The same reproducible run contract should preferentially support both system-triggered execution and manual execution from a terminal or developer environment.

If the Autonomous Data Science System were removed, the resulting repository should still be a credible professional data-science project.

See `docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md`.

## P-025. Reusable knowledge identity and granularity should be separate from reasoning function

A reusable methodological unit should not be forced into one overloaded semantic-role label merely because the system needs a common representation.

The representation should distinguish the intrinsic form of knowledge, such as a Concept, Method, Framework, Question Template, Rule, or Investigation Pattern, from the reasoning functions that knowledge can play, such as validity constraint, evidence requirement, interpretation guidance, failure mode, repair option, or human escalation hook.

Knowledge granularity should also support independently addressable assets, stably identifiable components inside those assets, and non-addressable narrative facets. This allows provenance, versioning, relation targeting, and reuse where they add value without turning every sentence into a top-level object.

See `docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md`.

## P-026. Static methodological relationships and conditional guidance rules should remain distinct

A stable semantic relationship between knowledge units is not the same thing as a guarded methodological implication.

Relations should express meanings such as composition, alternatives, complements, or conceptual dependency. Conditional rules should express reasoning such as what becomes relevant, required, constrained, or worth asking when project conditions hold.

Rules should normally guide project reasoning, horizon construction, questions, proposals, claim validity, and revalidation rather than silently execute analytical decisions as a rigid hidden workflow. Hard constraints may block incompatible claims or actions within their scope, while conflicting soft guidance should remain inspectable and be resolved through project-specific relevance and trade-off reasoning.

See `docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md`.