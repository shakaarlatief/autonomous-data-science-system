# Open Questions

This document records important unresolved questions. It is canonical and current rather than a complete historical transcript. Detailed reasoning is preserved in foundations, checkpoints, and Git history.

Existing identifiers are retained for continuity even when a question is reframed or substantially answered.

## Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The accepted primary purpose is to create the best data-science process for the particular project, where "best" depends on project goals, constraints, deliverables, and desired human involvement.

Still unresolved: explicit end-to-end success criteria and how they are operationalized in evaluation.

---

## Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed

Autonomy is currently hypothesized to be dynamic rather than one project-wide level. Risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state may restrict autonomy locally.

The exact autonomy model remains open.

---

## Q-003. What should the human's role be?

**Status:** Substantially refined

The project distinguishes preferred human involvement from required human involvement. Humans may be required for semantic clarification, normative trade-offs, authority decisions, risk acceptance, unresolved admissibility, consequential uncertainty, or knowledge-quality review.

The system should usually attempt cheap reliable autonomous resolution before interrupting the human unless authoritative human input is intrinsically required.

---

## Q-004. How should data-science knowledge be represented?

**Status:** Substantially refined, not resolved

Checkpoint 7 develops a strong architecture-neutral hypothesis based on thin knowledge packages containing versioned, provenance-aware, typed composable reasoning components.

Still unresolved: exact representation syntax, package/component boundaries, storage, querying, composition semantics, executable attachments, and formal validation rules.

Detailed reasoning: `docs/foundations/007_reusable_knowledge_representation_and_composable_components.md`.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

The project favors a hybrid of deterministic safeguards, explicit decision frameworks, semantic retrieval, interpretive reasoning, and open-ended discovery.

Checkpoint 8 adds progressively stronger thresholds for reasoning, reusable knowledge, and deterministic enforcement.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined through Q-037

Activation is treated as a project-state relevance problem rather than a direct workflow transition. It may arise from observations, proposals, missing prerequisites, contradictions, risk, governance, or dependency revisions.

Still unresolved: implementation of triggers, retrieval, applicability, deduplication, and coverage.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially refined, not resolved

Checkpoint 7 develops the strongest answer so far: a thin semantic package plus typed components such as question templates, invariants, decision principles, evidence requirements, investigations, alternatives, assumptions, failure modes, detection hooks, claim constraints, review hooks, dependencies, resolution criteria, and reopen conditions.

Checkpoint 8 adds that each important component also needs explicit knowledge role, evidential status, scope, provenance, maturity, challenge history, currency, and enforcement authority.

Still unresolved: final schema, granularity, composition rules, executable semantics, and storage.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed dependency-aware state. Later checkpoints add source registration, conflicts, knowledge instances, activation provenance, component/version dependencies, instantiated assumptions, and claim constraints.

Still unresolved: exact object boundaries, schemas, status models, versioning, storage, and query patterns.

---

## Q-009. What agent or responsibility structure is actually useful?

**Status:** Reframed

Knowledge, capabilities, and actors are now conceptually separate. Agents should operate on shared state and be activated because current work requires them rather than because a fixed roster exists.

No permanent agent architecture has been selected.

---

## Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include epistemic single points of failure, high-leverage weak assumptions, consequential claims with limited independent support, governance requirements, high residual risk, or low-maturity reusable knowledge used consequentially.

Checkpoint 8 adds knowledge-library centrality and consequence of incorrect reusable knowledge as review factors.

---

## Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Different decisions require different evidence standards. Evidence independence and shared ancestry matter in addition to the number of supporting results.

Reusable knowledge may specify evidence requirements and context-sensitive sufficiency conditions, but the general sufficiency model remains open.

---

## Q-012. How should uncertainty and confidence be represented?

**Status:** Open

The system may need numerical, categorical, narrative, and structural uncertainty representations, plus propagation through claims, risks, decisions, knowledge instances, and activation priorities.

Checkpoint 8 argues against collapsing reusable-knowledge quality into one generic confidence score.

---

## Q-013. How should analysis depth and resource budgets work?

**Status:** Substantially reframed

Mandatory obligations remain mandatory. Project intent and budget primarily affect how far optional value-improving work is pursued and how many candidate investigations exposed by knowledge packages are instantiated.

The final policy remains open.

---

## Q-014. How should the system decide when further experimentation is no longer worth the cost?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant residual uncertainty, diminishing expected value, unavailable information, or resource limits that do not violate integrity requirements.

Package-specific resolution and evidence-sufficiency criteria now participate in this reasoning.

---

## Q-015. How should different project types be characterized?

**Status:** Substantially reframed

Checkpoint 5 favors multidimensional characterization rather than one exclusive project type. Analytical objective and desired claim type are activation-relevant alongside data structure.

The exact characterization representation remains open.

---

## Q-016. How should system quality itself be evaluated?

**Status:** Highest priority through Q-039

The system should eventually be compared with strong single-LLM workflows, human-guided LLM workflows, and other meaningful baselines across process quality as well as final analytical outputs.

Checkpoint 8 makes behavioral reasoning regression tests central to this problem.

---

## Q-017. How should real projects become regression tests for the system?

**Status:** Highest priority through Q-039

Real projects should preserve failure cases, expected behaviors, state transitions, and reusable tests without overfitting the system to a small benchmark set.

Checkpoint 8 adds that project cases should test reusable knowledge applicability, false positives, false negatives, repair behavior, reopening, and claim constraints.

---

## Q-018. How should the system handle interaction between modules?

**Status:** Substantially refined, not resolved

Modules should primarily interact through typed project-state changes and shared questions rather than direct calls. Cross-package reuse of smaller components is also supported.

Composition, deduplication, granularity, and cycle control remain open.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed dependency semantics, separate validity and currency, impact analysis, reopening, and repair obligations.

Checkpoints 7 and 8 extend this to reusable knowledge: a material knowledge revision may reopen dependent project decisions or claims.

Exact propagation rules remain open.

---

## Q-020. What should the execution environment look like?

**Status:** Open

Isolation, dependency management, data access, artifact tracking, random-state control, failure recovery, compute limits, reproducibility, enforceable information boundaries, and executable knowledge validators remain unresolved.

---

## Q-021. How should model and tool providers be selected?

**Status:** Open

Provider diversity, cost-quality trade-offs, independent viewpoints, capability routing, and provider abstraction remain unresolved.

Provider choice should remain separate from the semantic knowledge architecture.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Increasingly coupled to knowledge quality

Reusable components require proposition-specific provenance, source-supported scope, limitations, version, and currency.

Checkpoint 8 adds that source authority is proposition-specific and external guidance should not automatically become a hard reusable rule.

The permanent source architecture remains open.

---

## Q-023. Should raw conversations be archived, and if so, how?

**Status:** Open

Raw transcripts contain valuable provenance but also outdated ideas and duplication. Their future storage and safe use remain undecided.

---

## Q-024. How much of knowledge capture should eventually be automated?

**Status:** Reframed and risk-sensitive

Automatic extraction may identify candidate lessons, failure cases, counterexamples, or gaps, but should not directly promote them into trusted reusable knowledge.

Checkpoint 8 favors automated **knowledge change proposals** rather than automatic library mutation.

---

## Q-025. What maturity model should be used for ideas and knowledge?

**Status:** Substantially refined, not resolved

Checkpoint 8 distinguishes knowledge role, maturity, and enforcement authority and argues that maturity may itself be multidimensional.

Exact maturity states, transitions, review requirements, and any quantitative representation remain open.

---

## Q-026. How should the repository structure evolve as the project grows?

**Status:** Open

Possible future areas include knowledge packages/components, reasoning cases, experiments, evaluation suites, implementation, sources, and gap logs. They should be introduced in response to actual needs.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The project favors a project-constitution model over one flat checklist. The epistemic core currently centers on semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

Formal requirements and real-project validation remain necessary.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

A strong hypothesis distinguishes objectives, constraints, deliverables, and human-control preferences, with additional separation between project-level, model-level, and operational objectives.

The exact schema remains open.

---

## Q-029. How should the system prioritize analytical effort?

**Status:** Substantially refined, not resolved

Checkpoint 4 introduces the runnable frontier and separates hard obligations from optional prioritization.

Candidate factors include blocking power, validity importance, risk reduction, probability of changing an important decision, uncertainty reduction, dependency leverage, deliverable relevance, urgency, compute/human cost, reversibility, parallelizability, and project intent.

No scoring mechanism has been selected.

---

## Q-030. Are the five candidate epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests but still needs formalization and real-project testing.

Checkpoint 8 shows that the same integrity ideas can recursively govern reusable knowledge without proving that the invariant set is complete.

---

## Q-031. What exactly belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Admissibility is hypothesized to be action-specific, source-aware, authority-aware, and capable of returning states such as permitted, permitted with controls, approval required, unresolved, or prohibited.

The final scope and authority model remain open.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors scenario-based multidimensional risk, inherent versus residual risk, credible controls, assurance requirements, and explicit risk-acceptance authority.

Checkpoint 8 applies the same logic to reusable knowledge: consequential enforcement requires stronger knowledge assurance.

---

## Q-033. Should analytical questions and claims be primary project-state objects?

**Status:** Strong design hypothesis

Questions act as integration points for activated knowledge, while proposed claims can activate evidence and validity checks. Reusable question templates and claim constraints strengthen this architecture.

Exact schemas remain open.

---

## Q-034. How should project completion be defined in a question-driven system?

**Status:** Substantially refined, not resolved

Completion likely requires mandatory epistemic, admissibility, assurance, approval, and deliverable obligations to be sufficiently resolved, critical state to be internally consistent, and no material current output to depend on known invalid state.

A coverage check for unresolved or orphaned material concerns is likely.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These concepts participate in the candidate typed project-state and activation model.

Exact schemas, authority provenance, control-effectiveness evidence, approval staleness, and impact semantics remain open.

---

## Q-036. How should a new project be initialized into project state?

**Status:** Substantially refined, not resolved

Checkpoint 5 develops progressive state construction, question-specific authority, conflict representation, information-legitimate bootstrap inspection, multidimensional characterization, selective human clarification, and initialization based on reaching a legitimate first runnable frontier.

Detailed reasoning: `docs/foundations/005_project_initialization_and_universal_bootstrap.md`.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined, not resolved

Checkpoint 6 develops reusable definitions, project-specific instances, deterministic and interpretive activation, prospective checks, missing-prerequisite activation, open-ended discovery, shared state, and coverage review.

Checkpoint 7 adds package activation versus component applicability.

Still unresolved: exact trigger representation, semantic retrieval, applicability protocol, scope model, deduplication, and coverage implementation.

Detailed reasoning: `docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved

Checkpoint 8 develops a strong conceptual governance model.

Current hypotheses include:

- the knowledge library should itself obey epistemic-integrity principles;
- project-specific knowledge, candidate generalizable lessons, and trusted reusable knowledge should remain distinct;
- use **minimum justified generalization** and expand scope gradually;
- generalize reasoning mechanisms rather than local winners;
- distinguish knowledge role, maturity, and enforcement authority;
- use progressively higher thresholds for reasoning, reuse, and deterministic enforcement;
- treat LLM-generated knowledge as low-authority candidate knowledge until independently justified;
- use counterexamples actively for scope discovery and rejection of over-broad rules;
- preserve challenged, rejected, superseded, and negative knowledge with provenance;
- distinguish knowledge validity from currency;
- use staged promotion and knowledge change proposals rather than direct automatic mutation;
- use behavioral regression cases at component, package, activation, and project levels;
- account for self-confirmation when project evidence was generated under the influence of the knowledge being assessed;
- allow material knowledge revisions to create cross-project revalidation obligations;
- prioritize review of uncertain, highly reused, consequential components;
- treat `no reusable knowledge update` as a valid lesson-extraction outcome.

Four project-to-library stress tests covered a broad invariant candidate, a heuristic candidate, a genuinely project-specific lesson, and an apparent general rule rejected by a counterexample.

Still unresolved: exact maturity/status model, promotion authorities, quantitative quality representation, review workflow, contradiction-resolution implementation, freshness policy, and automatic learning architecture.

Detailed reasoning: `docs/foundations/008_knowledge_quality_generalization_and_evolution.md`.

---

## Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Current priority:** Highest

Checkpoint 8 makes behavioral regression testing a prerequisite for trustworthy knowledge evolution and for evaluating the autonomous system itself.

The system must be testable without assuming that every good data-science project follows one exact workflow or produces one exact model.

Important unresolved questions include:

- What should a reasoning regression case contain?
- What project information is visible to the system and what evaluator-only truth should remain hidden?
- Which expected behaviors are mandatory versus merely acceptable alternatives?
- How should the evaluator allow multiple valid analytical paths?
- How should cases test activation precision and recall?
- How should hidden leakage, semantic ambiguity, missing prerequisites, admissibility constraints, or state changes be represented?
- How should state transitions, invalidation, reopening, repair, and claim weakening be evaluated?
- How should process quality be separated from final model performance?
- How should efficiency, unnecessary work, and human interruption be measured?
- How should independent review behavior be tested?
- Which baseline systems should be compared?
- How should project diversity, held-out cases, and case generation reduce benchmark overfitting?
- How should real project failures become reusable regression cases without leaking private or organization-specific information?
- How should knowledge-component regression tests connect to full-project system evaluation?

This should be developed conceptually before selecting an evaluation framework or implementation harness.