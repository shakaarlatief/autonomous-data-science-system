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

The project distinguishes preferred human involvement from required human involvement. Human input may be required for semantics, normative trade-offs, authority decisions, risk acceptance, unresolved admissibility, or consequential uncertainty.

The system should generally attempt cheap, reliable autonomous resolution before interrupting the human unless authoritative human input is intrinsically required.

The exact escalation and approval model remains open.

---

## Q-004. How should data science knowledge be represented?

**Status:** Active and now coupled strongly to Q-007 and Q-037

Possible representations include decision modules, rules, structured documents, schemas, executable checks, graphs, or hybrids.

Checkpoint 6 establishes strong semantic requirements for activation but does not select a representation technology.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

The project favors a hybrid of deterministic safeguards, explicit decision frameworks, semantic retrieval, interpretive reasoning, and open-ended discovery.

Checkpoint 6 strengthens the requirement that the knowledge library remain open-world rather than treating predefined modules as exhaustive.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined through Q-037

Checkpoint 6 reframes activation as a project-state relevance problem rather than a direct workflow transition.

Activation may arise from observations, proposals, missing prerequisites, contradictions, risk, governance, or dependency revisions. Activated knowledge should normally create questions, obligations, reviews, safeguards, or candidate actions in state rather than execute immediately.

The implementation mechanism remains open.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Current priority:** Highest

Checkpoint 6 establishes what activated knowledge should accomplish, but not the internal semantic representation that makes this reliable across projects.

Important unresolved questions include:

- What core fields or components are necessary?
- How should activation conditions differ from applicability conditions?
- How should hard invariants, conditional decision frameworks, and open-ended reasoning coexist?
- How should evidence requirements be expressed independently of preferred methods?
- How should candidate investigations, alternatives, common failure modes, human gates, and review hooks be represented?
- How should scope, dependencies, sufficient-resolution criteria, and reopen conditions be encoded?
- How should rationale, references, examples, known limitations, version, and maturity be stored?
- How should modules compose without becoming excessively fragmented?
- Which parts should eventually be executable or machine-checkable?
- How should project-derived lessons revise reusable knowledge safely?

No declarative or executable schema has been selected.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed, dependency-aware state. Checkpoint 5 adds source registration, source-aware reported statements, current interpretations, and conflicts. Checkpoint 6 adds project-specific knowledge instances and activation provenance as candidate state concepts.

Still unresolved: exact object boundaries, schemas, status models, versioning, storage, and query patterns.

---

## Q-009. What agent or responsibility structure is actually useful?

**Status:** Reframed

Potential responsibilities include problem understanding, analysis, experimentation, execution, methodological review, leakage review, admissibility review, risk review, and decision synthesis.

Checkpoint 6 strengthens the view that knowledge, capabilities, and actors should be separate. Agents should operate on shared state and be activated because current work requires them rather than because a fixed roster exists.

---

## Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

The current direction is risk- and value-sensitive review. Candidate triggers include epistemic single points of failure, high-leverage weak assumptions, consequential claims with one support path, shared vulnerable ancestry, governance requirements, or high residual risk.

Checkpoint 6 incorporates review into the same state-driven activation model as analytical knowledge.

---

## Q-011. What counts as sufficient evidence for a decision?

Different decisions require different evidence standards. The system must distinguish descriptive observations, statistical estimates, validation results, robustness checks, theoretical arguments, domain assumptions, causal evidence, and hypotheses.

Evidence independence and shared ancestry matter in addition to the count of supporting results.

---

## Q-012. How should uncertainty and confidence be represented?

Open issues include numerical, categorical, narrative, and structural representations, plus propagation through dependent claims, risks, decisions, and activation priorities.

Challenge history and independent support paths may be more informative than one generic confidence number.

---

## Q-013. How should analysis depth and resource budgets work?

Named modes may become presets rather than core architecture.

Current direction: mandatory obligations remain mandatory, while project intent and budget primarily affect how far the system pursues optional value-improving work.

---

## Q-014. How should the system decide when further experimentation is no longer worth the cost?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence for the current decision, decision-irrelevant residual uncertainty, diminishing expected value, unavailable information, or resource limits that do not violate mandatory integrity requirements.

---

## Q-015. How should different project types be characterized?

**Status:** Substantially reframed

Checkpoint 5 favors multidimensional characterization rather than one mutually exclusive project type.

Checkpoint 6 adds that analytical objective and desired claim type are activation-relevant properties alongside structural data properties.

The exact characterization representation remains open.

---

## Q-016. How should system quality itself be evaluated?

The system should eventually be compared with strong single-LLM workflows, human-guided LLM workflows, and other meaningful baselines.

Future evaluation should include project initialization, state correction, leakage prevention, activation precision and recall, unnecessary work, coverage recovery, evidence quality, reproducibility, human effort, and final analytical performance.

---

## Q-017. How should real projects become regression tests for the system?

Real projects should preserve failure cases, expected behaviors, and reusable system tests without overfitting the system to a small benchmark set.

Checkpoints 4 through 6 suggest testing state propagation, source contradictions, information barriers, activation behavior, coverage review, self-correction, and final outputs.

---

## Q-018. How should the system handle interaction between modules?

**Status:** Substantially refined, not resolved

Checkpoint 6 favors indirect interaction through typed project-state changes rather than primary reliance on direct module-to-module calls.

Shared analytical questions may reconcile overlapping modules. Composition, deduplication, scope, and cycle control remain open.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, not resolved

Checkpoint 4 develops typed dependency semantics, separate validity and currency, materiality, impact analysis, reopening, and generation of new obligations.

Checkpoint 6 adds that resolved knowledge instances may need to reopen when relevant dependencies change.

Exact propagation rules and repair automation remain open.

---

## Q-020. What should the execution environment look like?

Isolation, dependency management, data access, artifact tracking, random-state control, failure recovery, compute limits, reproducibility, and enforceable information boundaries remain open.

No execution architecture has been selected.

---

## Q-021. How should model and tool providers be selected?

Open issues include provider diversity, cost-quality trade-offs, independent viewpoints, capability routing, and provider abstraction.

Checkpoint 6 reinforces that provider choice should remain separate from the semantic knowledge architecture.

---

## Q-022. How should external knowledge and source material be integrated?

The project has not selected a permanent architecture for references, educational material, derived knowledge, provenance, updating, licensing, or retrieval.

Reusable knowledge units may eventually need rationale, references, scope, known limitations, maturity, and version information.

---

## Q-023. Should raw conversations be archived, and if so, how?

Raw transcripts contain valuable provenance but also outdated ideas and duplication. Their future storage and safe use remain undecided.

---

## Q-024. How much of knowledge capture should eventually be automated?

The current manual process may later be partially automated, including detection of proposed decisions, hypotheses, gaps, conflicts, activation candidates, and generalizable project lessons.

---

## Q-025. What maturity model should be used for ideas and knowledge?

The current conceptual path remains:

```text
raw thought
  -> candidate idea
  -> active design hypothesis
  -> tested
  -> accepted principle or decision
  -> challenged
  -> revised / superseded / rejected
```

Checkpoint 6 suggests that reusable analytical knowledge itself may eventually need maturity and project-test history.

---

## Q-026. How should the repository structure evolve as the project grows?

Possible future areas include knowledge modules, cases, experiments, evaluation suites, architecture, implementation, sources, session records, and gap logs.

They should be introduced in response to actual needs rather than speculative completeness.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The project now prefers a project-constitution model over one flat checklist. The epistemic core currently centers on semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

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

No scoring mechanism has been selected.

---

## Q-030. Are the five candidate epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests but still needs real-project testing, formal definitions, and translation into testable system behavior.

---

## Q-031. What exactly belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Admissibility is currently hypothesized to be action-specific, source-aware, authority-aware, and capable of returning states such as permitted, permitted with controls, approval required, unresolved, or prohibited.

Checkpoint 6 shows that governance knowledge may activate prospectively from proposed actions as well as reactively from discovered facts.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors scenario-based multidimensional risk, inherent versus residual risk, credible controls, assurance requirements, and explicit risk-acceptance authority.

Checkpoint 6 adds that risk can trigger specialized knowledge and review intensity through the same activation architecture.

---

## Q-033. Should analytical questions and claims be primary project-state objects?

**Status:** Strong design hypothesis

Checkpoint 6 strengthens this view further: questions can act as integration points where several activated knowledge units contribute to one shared issue, while proposed claims themselves may activate evidence or validity checks.

The exact question and claim schemas remain open.

---

## Q-034. How should project completion be defined in a question-driven system?

**Status:** Substantially refined, not resolved

Current completion thinking requires mandatory epistemic, admissibility, assurance, approval, and deliverable obligations to be sufficiently resolved, important current state to be internally consistent, and no material current output to depend on known invalid state.

Checkpoint 6 adds a likely coverage check for orphaned material facts before completion.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These concepts now participate in the candidate typed project-state and activation model.

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

Checkpoint 6 develops a strong conceptual answer.

Current hypotheses include:

- separate knowledge from capabilities and actors;
- distinguish reusable definitions from project-specific instances;
- activation updates project state rather than automatically executing a workflow;
- support deterministic, interpretive, and open-ended activation;
- react to observations, combinations of facts, requested claim types, proposed actions, proposed methods, proposed claims, missing prerequisites, contradictions, risk, governance, and dependency revisions;
- support both reactive and prospective activation;
- use relevant state slices as module context;
- let modules contribute typed questions, obligations, safeguards, evidence needs, reviews, and candidate actions;
- prefer module interaction through shared state;
- use shared questions to reconcile overlapping modules;
- distinguish candidate relevance from established applicability;
- support scoped, reopenable knowledge instances;
- treat the library as open-world and compositional;
- use coverage review to detect missed concerns;
- detect orphaned material facts and orphaned actions;
- evaluate false-positive and false-negative activation explicitly.

Still unresolved: exact trigger representation, semantic retrieval strategy, applicability protocol, scope model, deduplication, coverage implementation, and integration with the future knowledge-unit schema.

Detailed reasoning is preserved in `docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`.
