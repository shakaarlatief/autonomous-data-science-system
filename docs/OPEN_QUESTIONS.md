# Open Questions

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, checkpoints, and Git history. Existing identifiers are retained for continuity even when a question has been substantially reframed.

## Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The accepted primary purpose is project-relative: create the best defensible data-science process for the project's goals, constraints, deliverables, and desired human involvement.

Still open: final system-level success criteria and evidence standards across project classes.

---

## Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed

Autonomy should probably be dynamic and depend on risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state.

The exact autonomy model remains open.

---

## Q-003. What should the human's role be?

**Status:** Substantially refined

Preferred human involvement should remain distinct from required involvement. Human authority may be needed for semantics, normative choices, approvals, risk acceptance, unresolved admissibility, or consequential uncertainty.

The exact escalation policy remains open.

---

## Q-004. How should data-science knowledge be represented?

**Status:** Substantially refined, not resolved

Checkpoint 7 favors thin semantic packages containing typed, composable, provenance-aware components.

Still open: final representation syntax, component boundaries, composition, storage, querying, and executable attachments.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

The preferred direction is hybrid: deterministic safeguards, explicit decision frameworks, semantic interpretation, and open-ended concern discovery.

The knowledge library should remain open-world.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined through Q-037

Activation is treated as a project-state relevance problem. Activated knowledge normally creates questions, obligations, reviews, safeguards, or candidate actions rather than immediately executing a workflow.

Large-scale implementation remains open.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially refined, not resolved

Current hypothesis: thin packages plus typed components for questions, invariants, principles, evidence requirements, investigations, alternatives, assumptions, failure modes, claim constraints, dependencies, review hooks, resolution criteria, and reopen conditions.

Exact schema and granularity remain open.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined, entering prototype test

Checkpoint 4 develops typed dependency-aware state. Prototype V0 now gives a deliberately small implementation vocabulary.

The final system schema, persistence model, query model, and status semantics remain open.

---

## Q-009. What agent or responsibility structure is useful?

**Status:** Reframed

Knowledge, capabilities, and actors should remain separate. No permanent agent roster is accepted.

Prototype V0 deliberately uses one reasoner so agent structure does not confound the architecture experiment.

---

## Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include high risk, epistemic single points of failure, weak high-leverage assumptions, fragile consequential claims, governance requirements, and consequential use of low-maturity knowledge.

The final review policy remains open.

---

## Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Evidence sufficiency is decision-specific and may depend on methodological validity, uncertainty, independence, shared ancestry, risk, and whether further evidence could change the decision.

No universal sufficiency model exists yet.

---

## Q-012. How should uncertainty and confidence be represented?

**Status:** Open

Numerical, categorical, narrative, structural, and dependency-aware representations remain possible.

---

## Q-013. How should analysis depth and resource budgets work?

**Status:** Open

Mandatory integrity obligations remain mandatory. Project intent and budget should mainly control optional depth and evidence expansion.

Prototype V0 introduces experimental token/tool budgets but does not solve the general problem.

---

## Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant uncertainty, diminishing information value, unavailable discriminating evidence, or resource limits compatible with the quality floor.

---

## Q-015. How should project types be characterized?

**Status:** Substantially reframed

The project favors multidimensional characterization rather than one exclusive project-type label.

Exact representation remains open.

---

## Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced through Checkpoints 9-11

Behavioral trajectories, visible-versus-hidden evaluator state, acceptance envelopes, dynamic repair, process-versus-outcome separation, strong baselines, and resource accounting are now specified conceptually and technically for Prototype V0.

Broader benchmark design and long-term scoring remain open.

---

## Q-017. How should real projects become regression tests?

**Status:** Substantially advanced

Real failures should be distilled into mechanism-preserving behavioral cases rather than copied blindly.

Long-term case maintenance, privacy-safe extraction, diversity, and held-out strategy remain open beyond Version 0.

---

## Q-018. How should knowledge packages interact?

**Status:** Substantially refined, not resolved

The preferred model is shared-state interaction plus reusable cross-package components rather than direct hard-coded package calls.

Deduplication, composition, and cycle control remain open at scale.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, entering prototype test

Current theory distinguishes hard dependencies from support relationships, validity from currency, and targeted repair from blind recursive invalidation.

Prototype V0 will test under-propagation, correct propagation, and over-propagation after an authoritative feature-timing revision.

---

## Q-020. What should the execution environment look like?

**Status:** Open at production scale; narrowly specified for V0

Prototype V0 requires instrumented artifact access, explicit Python inputs, hidden evaluator separation, trace logging, and a prospective action gate.

Production isolation, dependency management, recovery, compute control, and sandbox architecture remain open.

---

## Q-021. How should model and tool providers be selected?

**Status:** Open

Provider choice should remain separate from semantic architecture.

Prototype experiments require the same underlying strong model across B0, B1, and P0 within paired comparisons.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Increasingly coupled to knowledge quality

Reusable knowledge needs proposition-specific provenance, authority, scope, limitations, freshness, and versioning.

Prototype V0 deliberately uses only four manually authored components.

---

## Q-023. Should raw conversations be archived?

**Status:** Open

Raw transcripts may be useful provenance but contain duplication and obsolete reasoning. Their long-term role remains undecided.

---

## Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction must not imply automatic promotion into trusted knowledge.

Prototype V0 excludes automatic knowledge learning.

---

## Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined by Q-038, not resolved

Knowledge role, maturity, enforcement authority, challenge history, scope confidence, and operational coverage should remain distinct.

Exact statuses remain open.

---

## Q-026. How should repository structure evolve?

**Status:** Partially answered for Prototype V0

A provisional `prototype_v0/` experiment boundary is now justified for case specification, source code, tests, configuration, and results.

This does not determine the future production repository architecture.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The current epistemic core remains semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance.

Prototype V0 operationalizes only a small subset.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

Objectives, constraints, deliverables, human-control preferences, and distinctions among project/model/operational objectives remain important.

Prototype V0 uses a narrow project brief rather than the final intent schema.

---

## Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

The runnable-frontier concept separates mandatory blockers from optional work.

Prototype V0 uses only a minimal qualitative order: hard blocker, blocking semantic/methodological question, repair obligation, then high-value optional analysis.

---

## Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests and now enters limited empirical testing.

---

## Q-031. What belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Admissibility is currently treated as action-specific, source-aware, and authority-aware.

Full governance/admissibility is outside Prototype V0.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors failure-scenario-based risk, inherent versus residual risk, credible controls, assurance obligations, and explicit risk-acceptance authority.

Full assurance is outside Prototype V0.

---

## Q-033. Should analytical questions and claims be primary state objects?

**Status:** Strong design hypothesis entering implementation test

Prototype V0 keeps `QUESTION` and `CLAIM` as distinct state types specifically so this hypothesis can be exercised.

---

## Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

General completion remains question/obligation driven. Prototype V0 uses narrower milestones: provisional development, repair after Phase 2, explicit final-model lock, then final evaluation.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These remain candidate state concepts for the full system but are intentionally outside the first prototype except for methodological blocking.

---

## Q-036. How should a new project be initialized?

**Status:** Substantially refined, entering narrow prototype test

Prototype V0 exercises only the minimum initialization behavior needed to ingest the brief, README, datasets, baseline code, structural facts, and contradictions.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined, entering empirical test

Prototype V0 uses four manually authored components, direct deterministic checks for precise safeguards, simple state-pattern activation for interpretive knowledge, idempotent scoped instances, and no retrieval infrastructure.

Large-scale semantic retrieval and coverage remain open.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved

Checkpoint 8 establishes minimum justified generalization, separation of project lessons from trusted reusable knowledge, different reasoning/reuse/enforcement thresholds, counterexample-driven scope discovery, staged promotion, versioning, and cross-project impact analysis.

Exact maturity, promotion, freshness, contradiction, and automatic-learning mechanisms remain open.

---

## Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Substantially refined; first implementation specified

Checkpoint 9 defines behavioral trajectories and acceptance envelopes. Checkpoints 10-11 instantiate those ideas in a concrete synthetic churn case with dynamic revelation, deterministic assertions, blinded semantic evaluation, held-out surface variants, and B0/B1/P0 controls.

Broader benchmark infrastructure remains open.

---

## Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Status:** Substantially specified for Version 0

The current experiment contains one strong reasoner, Python execution, nine minimal state types, five relations, four knowledge components, one deterministic prospective gate, interpretive activation, dependency repair, a synthetic churn case family, and strong B0/B1 baselines.

The architecture should be simplified or rejected for this project scale if B1 matches P0's critical-integrity and repair behavior at materially lower complexity/cost.

Detailed reasoning:

`docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`

---

## Q-041. How should Prototype V0 be represented and implemented concretely?

**Current priority:** Highest  
**Status:** Substantially specified; implementation evidence is now required

Foundation 011 defines the concrete technical contract.

Current Version 0 specification includes:

```text
common experiment harness
hard visible/evaluator information boundary
instrumented artifact access
metadata versus value-level access
explicit Python input declaration
three project phases
concrete 24-month customer-month DGP
fixed initial DGP equations and parameters
stale README semantics
post-outcome account_state_code mechanism
inherited preprocessing contamination
Phase 2 authoritative timing notice
machine-readable hidden evaluator manifest
benchmark self-tests
condition-neutral milestone reports
common action/trace model
nine typed P0 state objects
five explicit relations
typed Version 0 statuses
append-only audit history
dependency-aware repair
four minimal knowledge components
idempotent activation
minimal runnable-frontier behavior
deterministic evaluator assertions
blinded semantic judging
resource accounting
held-out surface variants
benchmark-first implementation order
```

Detailed reasoning:

`docs/foundations/011_prototype_v0_technical_specification.md`

The immediate unresolved task is no longer broad architecture design. It is to implement and mechanically validate the benchmark generator before P0 exists.

The first implementation milestone is:

> **Generate one deterministic synthetic case and prove that the visible artifacts, hidden evaluator truth, dynamic notice, inherited contamination, and benchmark self-tests are internally consistent.**

Only concrete implementation failures should now reopen the Version 0 specification.