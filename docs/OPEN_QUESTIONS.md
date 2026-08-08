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

The project now distinguishes preferred human involvement from required human involvement. Human input may be required for semantics, normative trade-offs, authority decisions, risk acceptance, unresolved admissibility, or consequential uncertainty even when the user otherwise prefers minimal interruption.

The exact escalation and approval model remains open.

---

## Q-004. How should data science knowledge be represented?

Possible representations include decision modules, rules, structured documents, schemas, executable checks, graphs, or hybrids. No representation has been selected.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

The project continues to favor a hybrid of hard constraints, explicit decision frameworks, and open-ended reasoning. The exact boundary and implementation remain unresolved.

---

## Q-006. How should relevant investigations be activated?

Open issues include deterministic versus LLM-generated triggers, module cross-activation, false-negative activation detection, and avoiding irrelevant work.

---

## Q-007. What should a reusable decision module contain?

Possible contents include activation conditions, questions, rationale, required evidence, diagnostics, alternatives, common failure modes, human gates, dependencies, outputs, and references.

No declarative or executable schema has been selected.

---

## Q-008. How should project state be represented?

**Current priority:** Highest

The project now needs a coherent conceptual model for analytical questions, facts, observations, assumptions, evidence, claims, decisions, risks, controls, approvals, assurance requirements, dependencies, unresolved issues, and next actions.

This should be solved conceptually before selecting storage technology.

---

## Q-009. What agent or responsibility structure is actually useful?

Potential responsibilities include problem understanding, analysis, experimentation, execution, methodological review, leakage review, admissibility review, risk review, and decision synthesis.

These are responsibilities, not accepted permanent agents.

---

## Q-010. When is independent review required?

The current direction is risk- and value-sensitive review rather than reviewing everything. Open questions include triggers for lightweight critique, specialized review, independent replication, multiple-model review, and mandatory human approval.

---

## Q-011. What counts as sufficient evidence for a decision?

Different decisions may require different evidence standards. The project must distinguish descriptive observations, statistical estimates, cross-validation, robustness checks, theoretical arguments, domain assumptions, causal evidence, and LLM-generated hypotheses.

---

## Q-012. How should uncertainty and confidence be represented?

Open issues include numerical versus categorical versus structural representations, and how uncertainty should propagate through dependent claims, risks, and decisions.

---

## Q-013. How should analysis depth and resource budgets work?

Named modes may eventually be presets rather than fundamental architecture. The deeper problem is how intent, risk, uncertainty, expected value, compute cost, and human cost determine analytical depth.

---

## Q-014. How should the system decide when further experimentation is no longer worth the cost?

Potential stopping reasons include diminishing expected value, stable conclusions, insufficient information to distinguish alternatives, acceptable residual uncertainty, and resource limits.

---

## Q-015. How should different project types be characterized?

The system needs enough characterization to activate appropriate reasoning without creating an impossible rigid taxonomy. Candidate dimensions include predictive versus causal, temporal versus IID, grouped, panel, sequence, ranking, spatial, structured versus unstructured, and others.

---

## Q-016. How should system quality itself be evaluated?

The system should eventually be compared with strong single-LLM workflows, human-guided LLM workflows, and other meaningful baselines across process quality as well as final predictive performance.

---

## Q-017. How should real projects become regression tests for the system?

The project needs a way to preserve failure cases, expected behaviors, and reusable tests without overfitting the system to a small benchmark set.

---

## Q-018. How should the system handle interaction between modules?

Issues such as missingness, leakage, validation, imbalance, calibration, temporal structure, feature engineering, and risk can interact. Cross-triggering and dependencies must remain manageable.

---

## Q-019. How should invalidation work?

If an upstream assumption, dataset, procedure, or control becomes invalid, which downstream experiments, claims, decisions, risks, approvals, and artifacts should automatically become stale or require reconsideration?

---

## Q-020. What should the execution environment look like?

Isolation, dependency management, data access, artifact tracking, random-state control, failure recovery, compute limits, and reproducibility remain open. No execution architecture has been selected.

---

## Q-021. How should model and tool providers be selected?

Open issues include provider diversity, cost-quality trade-offs, independent viewpoints, model capability routing, and provider abstraction.

---

## Q-022. How should external knowledge and source material be integrated?

The project has not selected a permanent architecture for references, educational material, derived knowledge, provenance, updating, licensing, or retrieval.

---

## Q-023. Should raw conversations be archived, and if so, how?

Raw transcripts contain valuable provenance but also outdated ideas and duplication. Their future storage and safe use remain undecided.

---

## Q-024. How much of knowledge capture should eventually be automated?

The current manual process may later be partially automated, for example by detecting proposed decisions, hypotheses, gaps, and open questions for human approval.

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

A strong hypothesis distinguishes objectives, constraints, deliverables, and human-control preferences, with additional separation between project-level, model-level, and operational objectives.

The exact schema remains open.

---

## Q-029. How should the system prioritize analytical effort?

Potential drivers include relevance, risk if ignored, uncertainty reduction, expected information value, computational cost, human cost, and downstream impact.

No scoring or routing mechanism has been selected.

---

## Q-030. Are the five candidate epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests but still needs real-project testing, formal definitions, and translation into testable system behavior.

---

## Q-031. What exactly belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Current strong hypotheses are that admissibility should be action-specific, source-aware, authority-aware, and able to return states such as permitted, permitted with controls, approval required, unresolved, or prohibited.

The system may reason about rules but should not treat uncertain interpretation as self-authorizing permission.

Still unresolved: final scope, authority precedence, legal/privacy/fairness governance model, and formal state representation.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors scenario-based multidimensional risk over an unexplained aggregate label. Candidate concepts include inherent risk, controls, residual risk, assurance requirements, and an explicit risk-acceptance authority.

Still unresolved: final risk dimensions, control-effectiveness model, assurance levels, routing rules, and whether aggregate scores are useful.

---

## Q-033. Should analytical questions and claims be primary project-state objects?

**Status:** Strong design hypothesis; now part of Q-008 work

Open issues include question generation, question categories, epistemic states, links from evidence to claims, contradiction, dependencies, and downstream activation.

---

## Q-034. How should project completion be defined in a question-driven system?

A project may eventually be complete when mandatory questions and obligations are sufficiently resolved, accepted as residual uncertainty by an appropriate authority, or explicitly documented as unresolvable.

The exact completion rule remains open.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Current priority:** High and coupled to Q-008

The project now needs to determine whether risk scenarios, controls, admissibility constraints, approvals, assurance obligations, and residual-risk decisions should be first-class state objects and how they depend on claims, assumptions, intended uses, and actions.

Important questions include:

- How should authority and constraint provenance be represented?
- How should a control's effectiveness be evidenced?
- How does a change in intended use invalidate or strengthen assurance obligations?
- How should approvals become stale when upstream evidence changes?
- How should risk and governance affect next-action selection and autonomy?

Detailed reasoning is preserved in `docs/foundations/003_admissibility_risk_and_assurance.md`.
