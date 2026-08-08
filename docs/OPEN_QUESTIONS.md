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

The current hypothesis is that autonomy should be dynamic rather than one fixed project-wide level. Risk, admissibility, uncertainty, reversibility, authority requirements, and action type may determine when autonomy is permitted or restricted.

The exact autonomy model remains open.

---

## Q-003. What should the human's role be?

**Status:** Substantially refined

The project distinguishes preferred human involvement from required human involvement. Human input may be required for semantics, normative trade-offs, authority decisions, risk acceptance, unresolved admissibility, or consequential uncertainty even when the user otherwise prefers minimal interruption.

Checkpoint 5 strengthens the idea that the system should first attempt cheap, reliable autonomous resolution before interrupting the human, except where authoritative human input is intrinsically required.

The exact escalation and approval model remains open.

---

## Q-004. How should data science knowledge be represented?

Possible representations include decision modules, rules, structured documents, schemas, executable checks, graphs, or hybrids. No representation has been selected.

This is now tightly coupled to Q-037, because the representation must support activation from project state.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

The project continues to favor a hybrid of hard constraints, explicit decision frameworks, and open-ended reasoning.

Checkpoint 5 makes the activation boundary more concrete: some discovered conditions may deterministically activate required safeguards, others may invoke reusable decision frameworks, and novel or ambiguous states may require open-ended reasoning.

The exact boundary and implementation remain unresolved.

---

## Q-006. How should relevant investigations be activated?

**Current priority:** Highest, now substantially reframed as Q-037

The original activation question remains central.

Checkpoints 4 and 5 suggest that activation should probably create questions, obligations, reviews, or candidate actions in project state rather than directly invoke one fixed next step.

Important issues include deterministic versus LLM-generated triggers, false-negative activation detection, module cross-activation, state subscriptions, and avoiding irrelevant work.

Q-037 now develops this as the primary knowledge-activation problem.

---

## Q-007. What should a reusable decision or knowledge module contain?

Possible contents include activation conditions, questions, rationale, required evidence, diagnostics, alternatives, common failure modes, human gates, dependencies, outputs, and references.

Checkpoint 5 adds a stronger requirement: modules should likely consume relevant project state and produce state changes, questions, evidence requirements, reviews, or candidate actions rather than exist as isolated prose guides.

No declarative or executable schema has been selected.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined, not resolved

Checkpoint 4 developed a strong conceptual model of typed, dependency-aware persistent state.

Candidate first-class objects include project intent, facts, assumptions, questions, investigations, evidence, claims, decisions, risks, controls, approvals, constraints, actions, and artifacts.

Checkpoint 5 adds source registration, source-aware reported statements, current project interpretations, conflicts, and initialization state as possible concepts that may need explicit representation.

Current unresolved issues include exact object boundaries, schemas, status models, versioning, storage, query patterns, and which concepts are truly first-class after real-project testing.

Detailed reasoning is preserved in `docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md` and `docs/foundations/005_project_initialization_and_universal_bootstrap.md`.

---

## Q-009. What agent or responsibility structure is actually useful?

Potential responsibilities include problem understanding, analysis, experimentation, execution, methodological review, leakage review, admissibility review, risk review, and decision synthesis.

These are responsibilities, not accepted permanent agents.

The current direction is that agents should operate on shared project state rather than become authoritative memory, and that roles should be activated because current state requires them rather than because a fixed roster exists.

---

## Q-010. When is independent review required?

The current direction is risk- and value-sensitive review rather than reviewing everything.

Checkpoint 4 adds dependency-based triggers such as epistemic single points of failure, high-leverage weak assumptions, conclusions with only one independent support path, or multiple results sharing one vulnerable ancestor.

Q-037 must determine how such review triggers participate in the same activation mechanism as analytical knowledge modules.

---

## Q-011. What counts as sufficient evidence for a decision?

Different decisions may require different evidence standards. The project must distinguish descriptive observations, statistical estimates, cross-validation, robustness checks, theoretical arguments, domain assumptions, causal evidence, and LLM-generated hypotheses.

Checkpoint 4 adds the need to consider evidence independence and shared dependency ancestry rather than merely counting supporting results.

---

## Q-012. How should uncertainty and confidence be represented?

Open issues include numerical versus categorical versus structural representations, and how uncertainty should propagate through dependent claims, risks, decisions, and activation priorities.

Challenge history and surviving independent support paths may eventually provide more interpretable evidence of robustness than one generic confidence number.

---

## Q-013. How should analysis depth and resource budgets work?

Named modes may eventually be presets rather than fundamental architecture. The deeper problem is how intent, risk, uncertainty, expected value, compute cost, and human cost determine analytical depth.

Checkpoint 4 suggests that depth may primarily affect the stopping threshold for optional value-improving work after mandatory obligations are satisfied.

---

## Q-014. How should the system decide when further experimentation is no longer worth the cost?

**Status:** Substantially refined, not resolved

Current stopping reasons include sufficient evidence for the current decision, decision-irrelevant residual uncertainty, diminishing expected value, inability of available data to discriminate alternatives, and resource limits that do not violate mandatory integrity requirements.

The exact stopping policy remains open.

---

## Q-015. How should different project types be characterized?

**Status:** Substantially reframed

Checkpoint 5 strengthens the hypothesis that project characterization should be multidimensional rather than one mutually exclusive type label.

A project may simultaneously be supervised, binary, temporal, grouped, forward-looking, sequence-derived, imbalanced, or have other structural properties.

The unresolved problem is how these properties should be represented, inferred, revised, and used as activation signals without creating an unmanageable taxonomy.

---

## Q-016. How should system quality itself be evaluated?

The system should eventually be compared with strong single-LLM workflows, human-guided LLM workflows, and other meaningful baselines across process quality as well as final predictive performance.

Future evaluation should include bootstrap quality, missed activation, unnecessary activation, information-boundary violations, state correction, and whether the right questions become active.

---

## Q-017. How should real projects become regression tests for the system?

The project needs a way to preserve failure cases, expected behaviors, and reusable tests without overfitting the system to a small benchmark set.

Checkpoints 4 and 5 suggest future tests should include state propagation, project initialization, source contradictions, information barriers, trigger activation, and self-correction behavior, not only final analytical outputs.

---

## Q-018. How should the system handle interaction between modules?

Issues such as missingness, leakage, validation, imbalance, calibration, temporal structure, feature engineering, and risk can interact.

The current hypothesis is that modules may interact indirectly through typed project-state changes and triggers rather than primarily through hard-coded direct module-to-module calls.

Q-037 is the next place to develop this idea.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, not resolved

Checkpoint 4 developed a change-propagation hypothesis based on typed dependency semantics, separate validity and currency, materiality, impact analysis, reopening of questions and decisions, and generation of new obligations.

Important unresolved issues include exact propagation rules, deterministic versus review-required effects, materiality thresholds, versioning, repair automation, and circular or contaminated support.

---

## Q-020. What should the execution environment look like?

Isolation, dependency management, data access, artifact tracking, random-state control, failure recovery, compute limits, reproducibility, and enforceable information boundaries remain open.

Checkpoint 5 strengthens the requirement that the execution environment may need to prevent illegitimate inspection of restricted test or holdout information rather than relying only on instructions.

No execution architecture has been selected.

---

## Q-021. How should model and tool providers be selected?

Open issues include provider diversity, cost-quality trade-offs, independent viewpoints, model capability routing, and provider abstraction.

---

## Q-022. How should external knowledge and source material be integrated?

The project has not selected a permanent architecture for references, educational material, derived knowledge, provenance, updating, licensing, or retrieval.

Checkpoint 5 adds the need to represent source authority, scope, version, and question-specific relevance during project initialization.

---

## Q-023. Should raw conversations be archived, and if so, how?

Raw transcripts contain valuable provenance but also outdated ideas and duplication. Their future storage and safe use remain undecided.

---

## Q-024. How much of knowledge capture should eventually be automated?

The current manual process may later be partially automated, for example by detecting proposed decisions, hypotheses, gaps, open questions, conflicts, and source-derived facts for approval or structured persistence.

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

The exact statuses and transitions are not formalized.

---

## Q-026. How should the repository structure evolve as the project grows?

Possible future areas include knowledge modules, cases, experiments, evaluation suites, architecture, implementation, sources, session records, and gap logs. They should be introduced in response to actual need.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The project now prefers a project-constitution model over one flat checklist. The epistemic core currently centers on semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

Formal requirements and real-project validation remain necessary.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

A strong hypothesis distinguishes objectives, constraints, deliverables, and human-control preferences, with additional separation between project-level, model-level, and operational objectives.

Checkpoint 5 adds progressive initialization: project intent may begin as provisional source-aware interpretation and become more specific as evidence and human clarification accumulate.

The exact schema remains open.

---

## Q-029. How should the system prioritize analytical effort?

**Status:** Substantially refined, not resolved

Checkpoint 4 introduced the runnable-frontier concept and a distinction between hard obligations and prioritization among optional executable actions.

Candidate prioritization factors include blocking power, validity importance, risk reduction, probability of changing an important decision, uncertainty reduction, dependency leverage, deliverable relevance, urgency, compute and human cost, reversibility, parallelizability, and project intent.

A qualitative value-of-information view is promising, but no scoring or routing mechanism has been selected.

---

## Q-030. Are the five candidate epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests but still needs real-project testing, formal definitions, and translation into testable system behavior.

---

## Q-031. What exactly belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Current strong hypotheses are that admissibility should be action-specific, source-aware, authority-aware, and able to return states such as permitted, permitted with controls, approval required, unresolved, or prohibited.

Checkpoint 5 adds that admissibility-relevant facts and explicit processing restrictions should begin entering project state during bootstrap rather than only at deployment.

Still unresolved: final scope, authority precedence, legal/privacy/fairness governance model, and formal state representation.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors scenario-based multidimensional risk over an unexplained aggregate label. Candidate concepts include inherent risk, controls, residual risk, assurance requirements, and an explicit risk-acceptance authority.

Checkpoint 5 adds that risk-relevant project facts should begin to activate risk reasoning during initialization without requiring a premature aggregate risk score.

---

## Q-033. Should analytical questions and claims be primary project-state objects?

**Status:** Strong design hypothesis, substantially developed in Checkpoint 4

The current direction is yes at the conceptual level, but the exact question taxonomy, status model, support relationships, and real-project behavior still require testing.

Checkpoint 5 adds that bootstrap conflicts and structural observations should often create questions automatically.

---

## Q-034. How should project completion be defined in a question-driven system?

**Status:** Substantially refined, not resolved

The current hypothesis is that completion requires mandatory epistemic, admissibility, assurance, approval, and deliverable obligations to be sufficiently resolved, current critical state to be internally consistent, and no important current output to depend on known invalid state.

Optional work may stop when expected value is insufficient relative to project intent and remaining budget.

The exact completion rule remains open.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

Checkpoint 4 incorporates these concepts into the candidate typed project-state model and dependency structure.

Checkpoint 5 adds that obvious governance constraints, sensitive-data indicators, external-service use, licenses, and operational intent may be discovered during bootstrap and should activate the appropriate governance reasoning.

Still unresolved: exact schemas, authority provenance, control-effectiveness evidence, approval staleness rules, and how governance objects participate in automated impact analysis.

---

## Q-036. How should a new project be initialized into project state?

**Status:** Substantially refined, not resolved

Checkpoint 5 develops a strong conceptual answer based on progressive state construction and universal bootstrap inspection.

Current hypotheses include:

- treat initial user requests and documentation as source-aware reported information rather than automatic truth;
- distinguish original project input from current project interpretation;
- make authority question-specific;
- represent material contradictions explicitly;
- use progressive semantic commitment so only action-relevant unknowns block work;
- establish information-legitimate inspection boundaries before consuming restricted data;
- perform a small structural bootstrap rather than exhaustive EDA;
- characterize projects through multiple structural properties rather than one exclusive type;
- use bootstrap observations to emit triggers and questions;
- ask the human selectively when authoritative clarification has high expected value;
- consider initialization sufficiently advanced when a legitimate first runnable frontier exists.

Still unresolved: exact source schema, bootstrap checklist, authority representation, information-barrier enforcement, project-characterization representation, and deterministic versus LLM-driven bootstrap responsibilities.

Detailed reasoning is preserved in `docs/foundations/005_project_initialization_and_universal_bootstrap.md`.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Current priority:** Highest

Checkpoint 5 reveals a major next bottleneck. The system may have a small universal bootstrap and rich project state, but it still needs a scalable mechanism for turning discovered facts, conflicts, open questions, and structural properties into the right specialized reasoning.

The design should avoid one enormous centralized decision tree and should not rely on an LLM to remember the entire universe of data-science concerns on every step.

Important questions include:

- What exactly is a trigger?
- Should knowledge modules subscribe to state patterns or activation predicates?
- What state should a module receive?
- What can a module produce: questions, obligations, diagnostics, evidence requirements, candidate actions, review requests, constraints, or all of these?
- Can multiple modules activate from one state change?
- Can modules activate further modules indirectly through new state facts rather than direct calls?
- Which activations should be deterministic hard requirements versus LLM-proposed hypotheses?
- How should open-ended reasoning be activated when no explicit module fits?
- How should specialized reviewers participate in the same activation model?
- How should the system detect missed activations or false negatives?
- How should it avoid over-activation and running many irrelevant modules?
- How should activation priority interact with mandatory obligations, risk, expected value, and the runnable frontier?
- How should module knowledge evolve when real projects expose gaps?

This should be explored conceptually before selecting a rule engine, graph system, workflow framework, agent architecture, or module storage format.
