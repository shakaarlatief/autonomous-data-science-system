# Open Questions

This document records important unresolved questions. It is intentionally canonical and current rather than a complete historical transcript. Detailed reasoning is preserved in foundations, checkpoints, and Git history.

Questions may later be answered, split, merged, reframed, or marked obsolete. Existing identifiers are retained for continuity.

## Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The accepted primary purpose is to create the best data-science process for the particular project, where "best" depends on project goals, constraints, deliverables, and desired human involvement.

Still unresolved: final system-level success criteria and evaluation standards.

---

## Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed

Autonomy should probably be dynamic rather than fixed project-wide. Risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state may determine when autonomy is permitted or restricted.

The exact model remains open.

---

## Q-003. What should the human's role be?

**Status:** Substantially refined

Preferred human involvement should remain distinct from required human involvement. Human input may be necessary for semantic authority, normative choices, approvals, risk acceptance, unresolved admissibility, consequential uncertainty, or knowledge-quality review.

The system should generally attempt cheap reliable autonomous resolution before interrupting a human unless authoritative input is intrinsically required.

---

## Q-004. How should data-science knowledge be represented?

**Status:** Substantially refined, not resolved

Checkpoint 7 develops a thin-package plus typed-component hypothesis. Candidate components include questions, invariants, decision principles, evidence requirements, investigations, alternatives, assumptions, failure modes, detection hooks, claim constraints, review/authority hooks, dependencies, resolution criteria, and reopen conditions.

Still unresolved: exact schema, package/component boundaries, composition, querying, executable attachments, and storage.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

The project favors a hybrid of deterministic safeguards, explicit decision frameworks, semantic retrieval, interpretive reasoning, and open-ended discovery.

The reusable library should remain open-world rather than becoming an exhaustive closed rule base.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined through Q-037

Activation is now treated as a project-state relevance problem rather than a direct workflow transition. Activated knowledge should normally create state objects such as questions, obligations, reviews, safeguards, or candidate actions rather than execute automatically.

Implementation remains open.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially refined, not resolved

Checkpoint 7 provides the strongest answer so far: thin semantic packages containing typed, composable, provenance-aware components. Activation differs from applicability; evidence requirements differ from investigation methods; claim constraints, failure modes, assumptions, lifecycle conditions, and cross-package reusable safeguards are first-class.

Still unresolved: exact schema, component granularity, composition rules, executable semantics, and storage.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed dependency-aware state. Later checkpoints add source registration, project-specific knowledge instances, activation provenance, component/version dependencies, and state instantiated from reusable knowledge.

Still unresolved: exact object boundaries, schemas, status machines, persistence, querying, and implementation.

---

## Q-009. What agent or responsibility structure is useful?

**Status:** Reframed

Knowledge, capabilities, and actors should remain separate. Responsibilities may include analysis, execution, methodological review, admissibility review, risk review, and synthesis, but no permanent agent roster is accepted.

---

## Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include high-risk use, epistemic single points of failure, weak high-leverage assumptions, consequential claims with fragile support, governance requirements, or consequential reliance on low-maturity reusable knowledge.

Exact review policy remains open.

---

## Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Evidence standards are decision-specific. Evidence independence, shared ancestry, uncertainty, methodological validity, and whether more information could change the decision may matter.

Exact sufficiency semantics remain open.

---

## Q-012. How should uncertainty and confidence be represented?

**Status:** Open

Possible numerical, categorical, narrative, and structural representations remain under consideration. Uncertainty may need to propagate through claims, decisions, risks, knowledge instances, and activation priorities.

---

## Q-013. How should analysis depth and resource budgets work?

**Status:** Open

Mandatory integrity obligations remain mandatory. Project intent and budget should mainly influence optional value-improving work and evidence depth.

No final depth or budget policy exists.

---

## Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant uncertainty, diminishing expected value, lack of discriminating information, or resource limits that do not violate mandatory obligations.

---

## Q-015. How should project types be characterized?

**Status:** Substantially reframed

The project favors multidimensional characterization rather than one exclusive project-type label. Structural properties, analytical objective, desired claim type, intended use, and deployment regime may all matter.

Exact representation remains open.

---

## Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced through Q-039

Checkpoint 9 develops behavioral-trajectory evaluation, acceptance envelopes, visible-versus-hidden evaluator state, repair testing, process-versus-outcome separation, and meaningful simpler baselines.

Still unresolved: exact metrics, evaluator implementation, benchmark suite, scoring, and held-out-case strategy.

---

## Q-017. How should real projects become regression tests?

**Status:** Substantially advanced through Q-038 and Q-039

Real failures can be distilled into reusable behavioral cases without copying private project circumstances. Cases should test applicability, safeguards, claim constraints, repair, reopening, and interaction.

Still unresolved: exact case representation, maintenance, diversity, and held-out evaluation.

---

## Q-018. How should knowledge modules/packages interact?

**Status:** Substantially refined, not resolved

The preferred model is interaction through shared project state and shared questions, with cross-package reuse of smaller components. Direct hard-coded module calls should not be the primary integration mechanism.

Deduplication, composition, and cycle control remain open.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, not resolved

Typed dependency semantics, validity versus currency, materiality, reopening, and repair obligations are established conceptually. Later checkpoints extend invalidation to reusable knowledge and cross-project effects.

Exact propagation rules and automation remain open.

---

## Q-020. What should the execution environment look like?

**Status:** Open

Isolation, dependencies, data access, artifact tracking, random-state control, failure recovery, compute limits, reproducibility, information barriers, and executable validators remain unresolved.

---

## Q-021. How should model and tool providers be selected?

**Status:** Open

Provider diversity, quality/cost trade-offs, independent viewpoints, capability routing, and provider abstraction remain open. Provider choice should not determine the semantic architecture.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Increasingly coupled to knowledge quality

Reusable components need proposition-specific provenance, source scope, limitations, authority, version, and freshness handling.

The permanent source architecture remains open.

---

## Q-023. Should raw conversations be archived?

**Status:** Open

Raw transcripts contain provenance but also duplication and obsolete reasoning. Their long-term role remains undecided.

---

## Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction of lessons, failures, candidate components, conflicts, or activation signals may become useful, but extraction must not imply automatic promotion into trusted knowledge.

---

## Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined by Q-038, not resolved

Knowledge role, maturity, and enforcement authority should remain separate. Challenge history, scope confidence, operational coverage, and independent review may matter more than one scalar confidence score.

Exact statuses remain open.

---

## Q-026. How should repository structure evolve?

**Status:** Open

Future areas may include knowledge components, cases, experiments, evaluation suites, implementation, and sources. They should be added in response to real needs rather than speculative completeness.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The current project constitution centers on semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance.

Formalization and project testing remain necessary.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

Objectives, constraints, deliverables, human-control preferences, and distinctions among project/model/operational objectives are important. Intent may begin provisionally and become more specific with evidence.

Exact schema remains open.

---

## Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

The runnable-frontier concept separates mandatory obligations from optional work. Candidate factors include blocking power, risk reduction, decision impact, uncertainty reduction, dependency leverage, deliverable relevance, cost, reversibility, and project intent.

No scoring mechanism is selected.

---

## Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests and now informs knowledge components and behavioral evaluation, but still requires formalization and real-project testing.

---

## Q-031. What belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Admissibility is action-specific, source-aware, authority-aware, and may yield permitted, permitted-with-controls, approval-required, unresolved, or prohibited states.

Final authority and governance models remain open.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors failure-scenario-based risk, inherent versus residual risk, credible controls, assurance obligations, and explicit risk acceptance authority.

Exact representation remains open.

---

## Q-033. Should analytical questions and claims be primary state objects?

**Status:** Strong design hypothesis

Questions act as integration points for modular reasoning. Proposed claims can activate evidence and validity checks. Reusable knowledge includes question templates and claim constraints.

Exact schemas remain open.

---

## Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

Completion likely requires all mandatory epistemic, admissibility, assurance, approval, and deliverable obligations to be sufficiently resolved; critical state to be consistent; no important output to depend on known-invalid state; and optional work to have insufficient marginal value.

Coverage review may search for orphaned material concerns before completion.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These concepts belong in the candidate typed state and activation model. Exact schemas, authority provenance, control-effectiveness evidence, and approval staleness remain unresolved.

---

## Q-036. How should a new project be initialized?

**Status:** Substantially refined, not resolved

Checkpoint 5 develops progressive state construction, source-aware interpretation, information boundaries, structural bootstrap, multidimensional characterization, selective human clarification, and a stopping condition based on reaching a legitimate runnable frontier.

Exact bootstrap representation and enforcement remain open.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined, not resolved

Checkpoint 6 develops reusable definitions, project-specific instances, deterministic/interpretive/open activation, prospective checks, missing-prerequisite activation, shared questions, coverage review, and orphaned-state detection. Checkpoint 7 adds component applicability.

Exact trigger representation, semantic retrieval, applicability protocol, deduplication, and coverage implementation remain open.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved

Checkpoint 8 establishes a strong governance model: epistemic discipline applies to the knowledge library itself; project-specific results must be separated from candidate generalizations; minimum justified generalization should be preferred; reasoning mechanisms should be generalized rather than local winners; knowledge role, maturity, and enforcement authority are distinct; reasoning, reuse, and enforcement thresholds should rise progressively; counterexamples should challenge scope; negative and superseded knowledge should retain provenance; validity and currency are separate; staged change proposals should precede trusted mutation; material revisions may create cross-project revalidation obligations; and `no reusable knowledge update` is a valid outcome.

Still unresolved: exact maturity model, promotion authority, contradiction-resolution implementation, freshness policies, automatic learning architecture, and quantitative quality representation.

Detailed reasoning: `docs/foundations/008_knowledge_quality_generalization_and_evolution.md`.

---

## Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Substantially refined, not resolved

Checkpoint 9 develops the first coherent evaluation model.

Current hypotheses include:

- evaluate project trajectories, not just final artifacts;
- separate system-visible information from evaluator-only world truth;
- specify behavioral acceptance envelopes rather than one expected workflow;
- distinguish mandatory obligations, prohibited behavior, acceptable resolutions, and optional quality opportunities;
- evaluate dependency and milestone relationships rather than exact step order;
- combine deterministic assertions, semantic judgment, and empirical outcomes;
- prevent critical integrity/admissibility failures from being compensated by higher predictive performance;
- test self-correction, dynamic state changes, invalidation, reopening, repair precision, and claim weakening;
- include both genuine hidden failures and harmless suspicious patterns to test selectivity;
- evaluate human interaction for value and authority need rather than minimum interruption count;
- separate process quality, ex-ante decision quality, and ex-post outcome quality;
- treat correct abstention or scope reduction as valid outcomes;
- evaluate justified effort rather than minimum work;
- include multiple case scales and eventually held-out or parameterized cases;
- version and challenge evaluator expectations themselves;
- compare against strong simpler LLM workflows and architectural ablations.

A difficult churn mini-project stress test showed that the acceptance-envelope approach can evaluate repeated entities, timestamps, post-outcome features, missingness, stale documentation, protected test data, validation ambiguity, inherited preprocessing contamination, and deployment-capacity constraints without prescribing one exact model or workflow.

Still unresolved: exact case schema, evaluator implementation, semantic judge assurance, scoring, hidden-case infrastructure, scenario generation, benchmark diversity, human simulation, and tooling.

Detailed reasoning: `docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md`.

---

## Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Current priority:** Highest

The project now has substantial conceptual theories for project constitution, persistent state, bootstrap initialization, knowledge activation, reusable knowledge representation, knowledge evolution, and behavioral evaluation.

The next step should not be a production implementation. It should be the smallest prototype capable of testing whether these semantic ideas materially outperform a strong simpler workflow.

Important questions include:

- What exact subset of project-state objects is required for a first prototype?
- What is the smallest knowledge representation needed to exercise activation and applicability?
- Which deterministic safeguard should be implemented first?
- Which interpretive knowledge package should be implemented first?
- What minimal runnable-frontier/orchestration behavior is necessary?
- How should one behavioral mini-project drive the prototype end to end?
- Which state changes and repair scenario must be included so dependency invalidation is genuinely tested?
- What should remain manual or mocked in version 0?
- Which architecture choices can be deliberately deferred?
- What baseline should the prototype be compared against?
- What result would falsify the need for a more complex state/knowledge architecture?
- What result would justify moving to a broader implementation?

This should be developed before choosing a production framework, database, agent roster, provider architecture, or large-scale execution system.