# Open Questions

This document records important unresolved questions. It is intentionally canonical and current rather than a complete historical transcript. Detailed reasoning is preserved in foundations, checkpoints, and Git history.

Questions may later be answered, split, merged, reframed, or marked obsolete. Existing identifiers are retained for continuity.

## Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The accepted primary purpose is to create the best data-science process for the particular project, where "best" depends on project goals, constraints, deliverables, and desired human involvement.

Still unresolved: explicit success criteria, requirements, boundaries, and evaluation standards.

---

## Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed

The current hypothesis is that autonomy should be dynamic rather than one fixed project-wide level. Risk, admissibility, uncertainty, reversibility, authority requirements, action type, and current assurance state may determine when autonomy is permitted or restricted.

The exact autonomy model remains open.

---

## Q-003. What should the human's role be?

**Status:** Substantially refined

The project distinguishes preferred human involvement from required human involvement. Human input may be required for semantics, normative trade-offs, authority decisions, risk acceptance, unresolved admissibility, consequential uncertainty, or knowledge-quality review.

The system should generally attempt cheap, reliable autonomous resolution before interrupting the human unless authoritative human input is intrinsically required.

The exact escalation and approval model remains open.

---

## Q-004. How should data science knowledge be represented?

**Status:** Substantially refined, not resolved

Checkpoint 7 develops a strong semantic representation hypothesis based on thin knowledge packages containing versioned, provenance-aware, typed composable reasoning components.

Candidate component types include question templates, invariants, decision principles, evidence requirements, investigation templates, alternatives or repairs, assumptions, failure modes, detection hooks, claim constraints, human/review hooks, dependencies, resolution criteria, and reopen conditions.

Still unresolved: exact representation syntax, package/component boundaries, composition semantics, storage, querying, executable attachments, and validation rules.

Detailed reasoning is preserved in `docs/foundations/007_reusable_knowledge_representation_and_composable_components.md`.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

The project favors a hybrid of deterministic safeguards, explicit decision frameworks, semantic retrieval, interpretive reasoning, and open-ended discovery.

Checkpoint 7 adds that components may differ in force, for example hard invariants, decision principles, heuristics, candidate strategies, or open hypotheses.

The knowledge library remains intentionally open-world.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined through Q-037

Checkpoint 6 reframes activation as a project-state relevance problem rather than a direct workflow transition.

Activation may arise from observations, proposals, missing prerequisites, contradictions, risk, governance, or dependency revisions. Activated knowledge should normally create questions, obligations, reviews, safeguards, or candidate actions in state rather than execute immediately.

Checkpoint 7 further distinguishes package activation from component applicability.

The implementation mechanism remains open.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially refined, not resolved

Checkpoint 7 develops the strongest answer so far.

The current hypothesis is a thin semantic knowledge package containing typed composable components. A package may carry identity, purpose, scope, activation/applicability metadata, version, and maturity, while components express questions, invariants, principles, evidence needs, investigations, alternatives, assumptions, failure modes, claim constraints, review hooks, dependencies, resolution criteria, and reopen conditions.

Important refinements include:

- activation differs from applicability;
- evidence requirements differ from investigation methods;
- knowledge statements have different force;
- important components should have component-level provenance;
- assumptions selected by project decisions should instantiate into project state;
- claim constraints are first-class reusable knowledge;
- cross-cutting components should be shared across packages rather than duplicated;
- knowledge may be declarative with optional executable validators or diagnostics;
- package instances should be scoped, resolvable, and reopenable;
- knowledge versions should remain traceable to dependent projects.

The architecture was stress-tested against Missing Data and Information Legitimacy, which have very different reasoning shapes.

Still unresolved: exact schema, component granularity, composition/inheritance rules, maturity transitions, contradiction handling, quality gates, executable attachment semantics, and storage.

Detailed reasoning is preserved in `docs/foundations/007_reusable_knowledge_representation_and_composable_components.md`.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed dependency-aware state. Checkpoint 5 adds source registration and conflicts. Checkpoint 6 adds knowledge instances and activation provenance. Checkpoint 7 adds component/version dependencies and project assumptions or claim constraints instantiated from reusable knowledge.

Still unresolved: exact object boundaries, schemas, status models, versioning, storage, and query patterns.

---

## Q-009. What agent or responsibility structure is actually useful?

**Status:** Reframed

Potential responsibilities include problem understanding, analysis, experimentation, execution, methodological review, leakage review, admissibility review, risk review, and decision synthesis.

The current direction strongly separates knowledge, capabilities, and actors. Agents should operate on shared state and be activated because current work requires them rather than because a fixed roster exists.

---

## Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

The current direction is risk- and value-sensitive review. Candidate triggers include epistemic single points of failure, high-leverage weak assumptions, consequential claims with one support path, shared vulnerable ancestry, governance requirements, high residual risk, or low-maturity reusable knowledge used consequentially.

The exact review policy remains open.

---

## Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Different decisions require different evidence standards. Evidence independence and shared ancestry matter in addition to the count of supporting results.

Checkpoint 7 adds that reusable knowledge may need explicit evidence requirements and context-sensitive sufficiency criteria that help determine when a concern is adequately resolved.

The exact sufficiency model remains open.

---

## Q-012. How should uncertainty and confidence be represented?

Open issues include numerical, categorical, narrative, and structural representations, plus propagation through dependent claims, risks, decisions, knowledge instances, and activation priorities.

Checkpoint 7 adds that reusable knowledge can itself specify uncertainty-handling and claim-scope constraints.

---

## Q-013. How should analysis depth and resource budgets work?

Named modes may become presets rather than core architecture.

Current direction: mandatory obligations remain mandatory, while project intent and budget primarily affect how far the system pursues optional value-improving work and how many candidate investigations from a knowledge package are instantiated.

---

## Q-014. How should the system decide when further experimentation is no longer worth the cost?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence for the current decision, decision-irrelevant residual uncertainty, diminishing expected value, unavailable information, or resource limits that do not violate mandatory integrity requirements.

Checkpoint 7 adds package-specific resolution and evidence-sufficiency criteria.

---

## Q-015. How should different project types be characterized?

**Status:** Substantially reframed

Checkpoint 5 favors multidimensional characterization rather than one mutually exclusive project type.

Analytical objective and desired claim type are activation-relevant properties alongside structural data properties.

The exact characterization representation remains open.

---

## Q-016. How should system quality itself be evaluated?

The system should eventually be compared with strong single-LLM workflows, human-guided LLM workflows, and other meaningful baselines.

Future evaluation should include project initialization, state correction, leakage prevention, activation precision and recall, unnecessary work, coverage recovery, knowledge-quality failures, evidence quality, reproducibility, human effort, and final analytical performance.

---

## Q-017. How should real projects become regression tests for the system?

**Status:** Increasingly important

Real projects should preserve failure cases, expected behaviors, and reusable system tests without overfitting the system to a small benchmark set.

Checkpoint 7 adds that real projects should also act as regression tests for reusable knowledge components themselves, including applicability, generated questions, safeguards, claim constraints, repair behavior, and reopen conditions.

Still unresolved: case representation, expected behaviors, coverage strategy, test maintenance, and generalization beyond the observed project set.

---

## Q-018. How should the system handle interaction between modules?

**Status:** Substantially refined, not resolved

Modules should primarily interact through typed project-state changes and shared questions rather than direct module calls.

Checkpoint 7 adds cross-package reuse of smaller shared knowledge components, such as a learned-transformation information-boundary safeguard used by imputation, scaling, PCA, and feature selection.

Composition, deduplication, granularity, and cycle control remain open.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed dependency semantics, separate validity and currency, materiality, impact analysis, reopening, and generation of new obligations.

Checkpoint 7 extends this concept to reusable knowledge itself: a revised or invalidated knowledge component may need to reopen dependent project decisions or claims.

Exact propagation rules and repair automation remain open.

---

## Q-020. What should the execution environment look like?

Isolation, dependency management, data access, artifact tracking, random-state control, failure recovery, compute limits, reproducibility, and enforceable information boundaries remain open.

Checkpoint 7 adds the possibility that semantic knowledge components may eventually have executable validators or diagnostics, but no execution architecture has been selected.

---

## Q-021. How should model and tool providers be selected?

Open issues include provider diversity, cost-quality trade-offs, independent viewpoints, capability routing, and provider abstraction.

Provider choice should remain separate from the semantic knowledge architecture.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Increasingly coupled to knowledge quality

The project has not selected a permanent architecture for references, educational material, derived knowledge, provenance, updating, licensing, or retrieval.

Checkpoint 7 adds a requirement for component-level provenance, source-supported scope, limitations, version, and maturity.

The relationship between source authority, empirical project evidence, LLM synthesis, and reusable knowledge admission is now central to Q-038.

---

## Q-023. Should raw conversations be archived, and if so, how?

Raw transcripts contain valuable provenance but also outdated ideas and duplication. Their future storage and safe use remain undecided.

---

## Q-024. How much of knowledge capture should eventually be automated?

**Status:** Open and now risk-sensitive

The current manual process may later be partially automated, including detection of proposed decisions, hypotheses, gaps, conflicts, activation candidates, reusable failure cases, and generalizable project lessons.

Checkpoint 7 makes clear that automatic extraction should not imply automatic promotion into trusted reusable knowledge.

---

## Q-025. What maturity model should be used for ideas and knowledge?

**Status:** High relevance to Q-038

The original conceptual path remains:

```text
raw thought
  -> candidate idea
  -> active design hypothesis
  -> tested
  -> accepted principle or decision
  -> challenged
  -> revised / superseded / rejected
```

Checkpoint 7 establishes that reusable analytical components themselves need maturity, versioning, challenge history, limitations, and project-test evidence.

The exact maturity states and promotion criteria remain open.

---

## Q-026. How should the repository structure evolve as the project grows?

Possible future areas include knowledge packages/components, cases, experiments, evaluation suites, implementation, sources, session records, and gap logs.

They should be introduced in response to actual needs rather than speculative completeness.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The project favors a project-constitution model over one flat checklist. The epistemic core currently centers on semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

Checkpoint 7 shows how some of these invariants may eventually be expressed through shared reusable components.

Formal requirements and real-project validation remain necessary.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

A strong hypothesis distinguishes objectives, constraints, deliverables, and human-control preferences, with additional separation between project-level, model-level, and operational objectives.

Project intent may begin as provisional source-aware interpretation and become more specific as evidence and clarification accumulate.

---

## Q-029. How should the system prioritize analytical effort?

**Status:** Substantially refined, not resolved

Checkpoint 4 introduces the runnable frontier and separates hard obligations from optional prioritization.

Candidate factors include blocking power, validity importance, risk reduction, probability of changing an important decision, uncertainty reduction, dependency leverage, deliverable relevance, urgency, compute and human cost, reversibility, parallelizability, and project intent.

Checkpoint 7 adds that one package may expose many legitimate investigations without requiring all of them to be executed.

No scoring mechanism has been selected.

---

## Q-030. Are the five candidate epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests but still needs real-project testing, formal definitions, and translation into testable system behavior.

Checkpoint 7 provides candidate reusable representations for implementing parts of information legitimacy and claim validity without claiming the invariant set is final.

---

## Q-031. What exactly belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Admissibility is hypothesized to be action-specific, source-aware, authority-aware, and capable of returning states such as permitted, permitted with controls, approval required, unresolved, or prohibited.

Governance knowledge may activate prospectively from proposed actions as well as reactively from discovered facts.

The final scope and authority model remain unresolved.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors scenario-based multidimensional risk, inherent versus residual risk, credible controls, assurance requirements, and explicit risk-acceptance authority.

Risk can trigger specialized knowledge, review intensity, and stricter evidence sufficiency through the same state-driven architecture.

---

## Q-033. Should analytical questions and claims be primary project-state objects?

**Status:** Strong design hypothesis

Questions can act as integration points where several knowledge packages contribute to one shared issue, while proposed claims may activate evidence or validity checks.

Checkpoint 7 strengthens this by making reusable question templates and claim constraints central knowledge components.

The exact question and claim schemas remain open.

---

## Q-034. How should project completion be defined in a question-driven system?

**Status:** Substantially refined, not resolved

Current completion thinking requires mandatory epistemic, admissibility, assurance, approval, and deliverable obligations to be sufficiently resolved, important current state to be internally consistent, and no material current output to depend on known invalid state.

Checkpoint 7 adds package-specific resolution criteria and a likely coverage check for unresolved or orphaned material concerns.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These concepts participate in the candidate typed project-state and activation model.

Still unresolved: exact schemas, authority provenance, control-effectiveness evidence, approval staleness rules, and automated impact semantics.

---

## Q-036. How should a new project be initialized into project state?

**Status:** Substantially refined, not resolved

Checkpoint 5 develops progressive state construction, question-specific authority, conflict representation, information-legitimate bootstrap inspection, multidimensional project characterization, selective human clarification, and initialization based on reaching a legitimate first runnable frontier.

Still unresolved: exact source schema, bootstrap checklist, information-barrier enforcement, and division between deterministic and interpretive bootstrap responsibilities.

Detailed reasoning is preserved in `docs/foundations/005_project_initialization_and_universal_bootstrap.md`.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined, not resolved

Checkpoint 6 develops a strong activation model based on reusable definitions, project-specific instances, deterministic and interpretive activation, prospective checks, missing-prerequisite activation, open-ended discovery, shared state, coverage review, and orphaned-state detection.

Checkpoint 7 adds a stronger distinction between package activation and component applicability and provides a more precise target for what activation retrieves.

Still unresolved: exact trigger representation, semantic retrieval strategy, applicability protocol, scope model, deduplication, and coverage implementation.

Detailed reasoning is preserved in `docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Current priority:** Highest

Checkpoint 7 creates an explicit reusable knowledge architecture, which introduces a new major risk: the system can accumulate knowledge that is wrong, weakly supported, contradictory, stale, over-generalized, or accidentally promoted from one unusual project.

The project therefore needs a rigorous knowledge lifecycle before implementing automatic knowledge capture or a persistent knowledge store.

Important questions include:

- How does a candidate reusable component enter the library?
- What distinguishes an external-source statement, project observation, LLM-generated hypothesis, project-derived lesson, tested heuristic, and hard invariant?
- What evidence or review is required before a component can be promoted to a stronger maturity level?
- When is deterministic enforcement justified?
- How should source authority, methodological reasoning, empirical project evidence, and independent review interact?
- How should contradictions among reusable components be represented and resolved?
- How should known limitations and scope boundaries be tested?
- What regression cases should accompany a knowledge component?
- How should a component update be evaluated before becoming the default version?
- How should active projects depending on an older version be impacted by a material knowledge revision?
- When can a project-specific lesson be generalized safely across projects?
- How should the system avoid overfitting reusable knowledge to a small or unrepresentative project set?
- How should incorrect knowledge be challenged, downgraded, superseded, or retired without erasing provenance?
- How should knowledge quality itself be audited over time?

This should be developed conceptually before choosing an automatic knowledge-learning loop or storage implementation.
