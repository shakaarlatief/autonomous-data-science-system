# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-18  
**Reconciliation context:** Development Method v0.3 preservation update and active Prototype V0 held-out execution

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, checkpoints, experiment records, and Git history. Existing identifiers are retained for continuity even when a question has been substantially reframed or answered.

## Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The primary purpose is project-relative: create the best defensible data-science process for the project's goals, constraints, deliverables, and desired human involvement.

Still open: final system-level success criteria across project classes.

---

## Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed

Autonomy should probably vary with risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state.

The final autonomy model remains open.

---

## Q-003. What should the human's role be?

**Status:** Substantially refined

Preferred involvement should remain distinct from required authoritative involvement. Exact escalation policy remains open.

Foundation 013 now provides the current system-level LLM-system-human framing.

---

## Q-004. How should data-science knowledge be represented?

**Status:** Substantially refined, not resolved

Current hypothesis: thin semantic packages containing typed, composable, provenance-aware reasoning components.

Final syntax, component boundaries, storage, querying, and executable attachments remain open.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

Current direction is hybrid: deterministic safeguards, explicit decision frameworks, interpretive reasoning, and open-ended concern discovery.

Prototype V0 tests only a narrow four-component version of this interaction.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined; narrow V0 mechanism under held-out evaluation

Activation is treated as a project-state relevance problem that creates questions, obligations, safeguards, reviews, or candidate actions rather than directly invoking a fixed workflow.

Large-scale implementation remains open.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially refined, not resolved

Foundation 007 provides a thin-package plus typed-component model covering questions, invariants, principles, evidence requirements, investigations, alternatives, assumptions, failure modes, claim constraints, dependencies, and lifecycle semantics.

Exact production schema and granularity remain open.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined; minimal representation implemented in Prototype V0

The final production schema and persistence/query architecture remain open. Prototype V0 intentionally uses a much smaller test vocabulary and is currently under held-out evaluation.

---

## Q-009. What agent or responsibility structure is useful?

**Status:** Reframed

Knowledge, capabilities, and actors should remain separate. Prototype V0 deliberately uses one reasoner to avoid agent-count confounding.

The eventual responsibility architecture remains open.

---

## Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include high risk, epistemic single points of failure, weak high-leverage assumptions, fragile consequential claims, governance requirements, and consequential use of low-maturity knowledge.

---

## Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Evidence sufficiency remains decision-specific and may depend on validity, uncertainty, independence, shared ancestry, risk, and the probability that more evidence changes the decision.

---

## Q-012. How should uncertainty and confidence be represented?

**Status:** Open

No final numerical, categorical, narrative, or structural representation has been selected.

---

## Q-013. How should analysis depth and resource budgets work?

**Status:** Open; Prototype V0 producing empirical evidence

Mandatory obligations remain mandatory. Optional depth should depend on project value and resource constraints.

Prototype V0 measures calls, tokens, tools, completion, and budget exhaustion, but does not solve the general budgeting problem.

---

## Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant residual uncertainty, diminishing information value, unavailable discriminating evidence, or compatible resource limits.

---

## Q-015. How should project types be characterized?

**Status:** Substantially reframed

The system should use multidimensional project characterization rather than one exclusive type label.

Exact representation remains open.

---

## Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced; first held-out evaluation active

Behavioral trajectories, hidden evaluator truth, acceptance envelopes, dynamic repair, process/outcome separation, strong baselines, deterministic assertions, resource accounting, a preregistered held-out design, and a calibrated blinded semantic judge now exist for Prototype V0.

Broader evaluation across more project families remains open.

---

## Q-017. How should real projects become regression tests?

**Status:** Substantially advanced

Real failures should be distilled into mechanism-preserving behavioral cases rather than copied blindly.

Long-term privacy-safe case extraction, diversity, and maintenance remain open.

---

## Q-018. How should knowledge packages interact?

**Status:** Substantially refined, not resolved

Preferred direction: shared-state composition plus reusable cross-package components. Large-scale deduplication, composition, and cycle control remain open.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined; minimal mechanism under held-out evaluation

Theory distinguishes hard dependencies from support relations and targeted repair from blind recursive invalidation.

Prototype V0 now exercises the dynamic feature-timing event empirically. Final conclusions about whether the explicit mechanism earns its complexity await completion and blinded judging of the held-out experiment.

---

## Q-020. What should the execution environment look like?

**Status:** Open at production scale; narrow V0 boundary implemented

Prototype V0 has instrumented artifact access, explicit Python inputs, hidden evaluator separation, trace logging, protected final-test semantics, and one-attempt-at-a-time held-out execution.

Production sandboxing, recovery, dependency management, and execution isolation remain open.

---

## Q-021. How should model and tool providers be selected?

**Status:** Open; one experiment configuration frozen provisionally

Provider choice remains separate from semantic architecture.

Prototype V0 uses a provider-neutral model protocol plus a frozen OpenAI GPT-5.6 Terra held-out configuration. This is not a production-provider decision.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Coupled to knowledge quality

Reusable knowledge needs proposition-specific provenance, authority, scope, limitations, freshness, and versioning.

Prototype V0 deliberately uses only four manually authored components.

---

## Q-023. Should raw conversations be archived?

**Status:** Open; explicitly deferred in preservation architecture v0.3

Raw transcripts may provide valuable provenance but contain duplication, sensitive conversational context, and obsolete reasoning.

Foundation 014 preserves a provenance-aware raw-conversation archive as a possible future extension, not a current requirement.

---

## Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive; current stage favors curated assistance

Automatic extraction should never imply automatic promotion into trusted reusable knowledge.

Development Method v0.3 now supports explicit promotion audits and periodic reconciliation manually or with AI assistance. Future generated indexes, promotion queues, contradiction detection, and reconciliation assistants are plausible, but are deferred until demonstrated need justifies them.

---

## Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined by Q-038, not resolved

Knowledge role, maturity, enforcement authority, challenge history, scope confidence, and operational coverage should remain distinct.

Development Method v0.3 adds lightweight authority/maturity metadata conventions for project documents, but this is not yet a formal universal schema.

---

## Q-026. How should repository structure evolve?

**Status:** Substantially advanced for current project-development needs; production architecture remains open

The repository now has:

```text
canonical project documents
foundational design memos
historical checkpoints
prototype_v0/ experiment boundary
KNOWLEDGE_MAP routing layer
MAJOR_CHANGES structural ledger
experiment-specific status ledgers
```

This is the current project-development preservation architecture, not the final production repository or data-store architecture of the Autonomous Data Science System.

Detailed rationale: Foundation 014.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

Current epistemic core: semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

Objectives, constraints, deliverables, human-control preferences, and project/model/operational distinctions remain important.

Prototype V0 uses a narrow brief rather than the final intent schema.

---

## Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

Current runnable-frontier concept separates blockers and repair from optional value-improving work. No final general scoring mechanism exists.

---

## Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

They inform Prototype V0 behavior and evaluation but remain open to empirical revision across broader projects.

---

## Q-031. What belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Full governance and admissibility remain outside Prototype V0.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Full assurance remains outside Prototype V0.

---

## Q-033. Should analytical questions and claims be primary state objects?

**Status:** Strong design hypothesis; minimal form implemented in P0 and under held-out evaluation

Prototype V0 keeps `QUESTION` and `CLAIM` distinct as part of the minimal typed-state experiment.

The broader production-level orchestration question remains open.

---

## Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

General completion remains obligation/question driven. Prototype V0 uses narrower experimental milestones and hard resource limits.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These remain full-system concepts and are intentionally omitted from V0 except for narrow methodological blocking.

---

## Q-036. How should a new project be initialized?

**Status:** Substantially refined; narrow benchmark mechanism implemented and under held-out evaluation

Prototype V0 exposes the brief, stale README, datasets, and inherited baseline to test whether a strong reasoner corrects initial project semantics before or during modelling.

The general initialization architecture remains open.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined; minimal P0 mechanism implemented and under held-out evaluation

V0 uses four components, direct checks for precise safeguards, simple state-pattern activation, scoped idempotent instances, and no large-scale retrieval infrastructure.

Whether this architecture earns its added cost versus B1 remains an active empirical question.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved

Foundation 008 establishes minimum justified generalization, staged promotion, role/maturity/enforcement separation, counterexample-driven scope discovery, and versioned challenge history.

Development Method v0.3 independently applies a related promotion concept to the project repository itself.

Exact production knowledge maturity, promotion, freshness, and automatic-learning mechanisms remain open.

---

## Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Substantially refined; first held-out benchmark active

The synthetic churn benchmark, hidden truth, dynamic revelation, deterministic assertions, strong controls, held-out variants, resource rules, and blinded judge protocol are implemented.

Completion of H1/H2, semantic judging, broader benchmark diversity, and later real-project regression families remain open.

---

## Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Status:** Answered for Prototype V0; empirical verdict pending

The implemented experiment contains one strong reasoner, Python, a small benchmark family, four knowledge concepts, strong B0/B1 controls, and minimal P0 semantic machinery.

The held-out experiment is now testing whether that machinery earns its added complexity and resource cost.

Detailed contract: `docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`.

---

## Q-041. How should Prototype V0 be represented and implemented concretely?

**Status:** Answered and frozen for the current held-out experiment

Foundation 011 defines the technical contract. The implemented V0 includes:

```text
synthetic benchmark generation and self-validation
hidden evaluator truth
instrumented treatment workspace
project phases and protected-test semantics
condition-neutral traces
common deterministic evaluator
provider-neutral model contract
B0 and B1 runners
P0 typed-state/controller/knowledge machinery
OpenAI model adapter
resource accounting and retry semantics
semantic judge tooling
held-out execution plan and one-attempt-at-a-time runner
```

The current implementation is frozen for held-out treatment behavior except for a genuine common infrastructure defect handled under the preregistered protocol.

Future architecture beyond V0 remains open.

Detailed source: `docs/foundations/011_prototype_v0_technical_specification.md` and `prototype_v0/README.md`.

---

## Q-042. What do real B0/B1 calibration runs show, and what common baseline protocol should be frozen before P0?

**Status:** Answered for Prototype V0

The six-run development calibration established viable strong-model B0/B1 behavior, resource distributions, a useful B1 control, and the common provider/runtime interface needed to preregister the held-out protocol before P0 implementation.

The held-out resource envelope, model/provider configuration, failure semantics, semantic rubric, run order, and comparison criteria were subsequently frozen in Foundation 012.

Development calibration remains non-held-out evidence and is not used as a substitute for the active H1/H2 experiment.

Detailed records include:

```text
docs/checkpoints/027_full_six_run_baseline_calibration_analysis.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

---

## Q-043. When should the project move beyond Git and Markdown for knowledge preservation?

**Status:** Open, with explicit current deferral criteria

Development Method v0.3 keeps Git + Markdown as the current preservation substrate while adding promotion audits, a knowledge map, reconciliation, authority metadata, experiment ledgers, and a major-changes history.

More advanced infrastructure may become justified if observed problems include:

```text
unreliable manual knowledge-map maintenance;
frequent failure to discover relevant existing knowledge;
repeated contradictory canonical statements;
large dependency networks that cannot be maintained safely in prose;
manual reconciliation becoming too expensive;
multiple concurrent contributors requiring stronger transaction semantics;
or a demonstrated need for semantic/hybrid retrieval beyond repository navigation.
```

Possible future mechanisms include machine-readable metadata, generated indexes, semantic retrieval, dependency graphs, graph/database storage, promotion queues, contradiction detection, and reconciliation assistants.

Detailed rationale: `docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`.
