# Open Questions

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, checkpoints, and Git history. Existing identifiers are retained for continuity even when a question has been substantially reframed.

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

---

## Q-004. How should data-science knowledge be represented?

**Status:** Substantially refined, not resolved

Current hypothesis: thin semantic packages containing typed, composable, provenance-aware reasoning components.

Final syntax, component boundaries, storage, querying, and executable attachments remain open.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially refined, not resolved

Current direction is hybrid: deterministic safeguards, explicit decision frameworks, interpretive reasoning, and open-ended concern discovery.

---

## Q-006. How should relevant investigations be activated?

**Status:** Substantially refined through Q-037

Activation is treated as a project-state relevance problem that creates questions, obligations, safeguards, reviews, or candidate actions rather than directly invoking a fixed workflow.

Large-scale implementation remains open.

---

## Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially refined, not resolved

Checkpoint 7 provides a thin-package plus typed-component model covering questions, invariants, principles, evidence requirements, investigations, alternatives, assumptions, failure modes, claim constraints, dependencies, and lifecycle semantics.

Exact schema/granularity remain open.

---

## Q-008. How should project state be represented?

**Status:** Substantially refined; entering Prototype V0 test

The final production schema and persistence/query architecture remain open. Prototype V0 intentionally uses a much smaller test vocabulary.

---

## Q-009. What agent or responsibility structure is useful?

**Status:** Reframed

Knowledge, capabilities, and actors should remain separate. Prototype V0 deliberately uses one reasoner to avoid agent-count confounding.

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

**Status:** Open

Mandatory obligations remain mandatory. Optional depth should depend on project value and resource constraints.

Prototype V0 now measures calls/tokens/tools but does not solve the general budgeting problem.

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

**Status:** Substantially advanced; Prototype V0 implementation underway

Behavioral trajectories, hidden evaluator truth, acceptance envelopes, dynamic repair, process/outcome separation, strong baselines, deterministic assertions, and resource accounting are now operational in the first benchmark.

Broader evaluation remains open.

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

**Status:** Substantially refined; planned Prototype V0 experiment

Theory distinguishes hard dependencies from support relations and targeted repair from blind recursive invalidation.

The dynamic feature-timing event will empirically test under-propagation, correct propagation, and over-propagation once P0 exists.

---

## Q-020. What should the execution environment look like?

**Status:** Open at production scale; narrow V0 boundary implemented

Prototype V0 now has instrumented artifact access, explicit Python inputs, hidden evaluator separation, trace logging, and optional prospective blocking.

Production sandboxing/recovery/dependency management remain open.

---

## Q-021. How should model and tool providers be selected?

**Status:** Open; first experiment configuration chosen provisionally

Provider choice remains separate from semantic architecture.

Prototype V0 now has a provider-neutral model protocol plus a provisional OpenAI GPT-5.6 Terra calibration adapter. This is not a production-provider decision.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Coupled to knowledge quality

Reusable knowledge needs proposition-specific provenance, authority, scope, limitations, freshness, and versioning.

Prototype V0 deliberately uses only four manually authored components.

---

## Q-023. Should raw conversations be archived?

**Status:** Open

Raw transcripts may provide provenance but contain duplication and obsolete reasoning.

---

## Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction should never imply automatic promotion into trusted reusable knowledge. Prototype V0 excludes automatic learning.

---

## Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined by Q-038, not resolved

Knowledge role, maturity, enforcement authority, challenge history, scope confidence, and operational coverage should remain distinct.

---

## Q-026. How should repository structure evolve?

**Status:** Partially answered for Prototype V0

A provisional `prototype_v0/` experiment boundary now exists. This does not define the future production repository architecture.

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

Current runnable-frontier concept separates blockers/repair from optional value-improving work. No final scoring mechanism exists.

---

## Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

They now inform executable Prototype V0 behavior but remain open to empirical revision.

---

## Q-031. What belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Full governance/admissibility remains outside Prototype V0.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Full assurance remains outside Prototype V0.

---

## Q-033. Should analytical questions and claims be primary state objects?

**Status:** Strong design hypothesis awaiting P0 implementation test

Prototype V0's planned P0 state keeps `QUESTION` and `CLAIM` distinct specifically to test this hypothesis.

---

## Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

General completion remains obligation/question driven. Prototype V0 uses narrower experimental milestones.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These remain full-system concepts and are intentionally omitted from V0 except for methodological blocking.

---

## Q-036. How should a new project be initialized?

**Status:** Substantially refined; narrow benchmark test pending real model

Prototype V0 exposes the brief, stale README, datasets, and inherited baseline to test whether a strong reasoner corrects initial project semantics before/while modeling.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined; P0 empirical test pending

V0 will use four components, direct checks for precise safeguards, simple state-pattern activation, scoped idempotent instances, and no retrieval infrastructure.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved

Checkpoint 8 establishes minimum justified generalization, staged promotion, role/maturity/enforcement separation, counterexample-driven scope discovery, and versioned challenge history.

Exact maturity/promotion/freshness/automatic-learning mechanisms remain open.

---

## Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Substantially refined; first benchmark operational

The first synthetic churn benchmark, hidden truth, dynamic revelation, deterministic assertions, and baseline runtime are implemented.

Blinded semantic judging, held-out H1/H2 execution, and broader benchmark diversity remain open.

---

## Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Status:** Substantially specified and under construction

The experiment contains one strong reasoner, Python, a small benchmark family, four knowledge concepts, strong B0/B1 controls, and a planned minimal P0.

The architecture should be simplified/rejected for this scale if B1 matches P0's reliability at materially lower complexity/cost.

Detailed reasoning: `docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`.

---

## Q-041. How should Prototype V0 be represented and implemented concretely?

**Status:** Substantially implemented through the real-baseline boundary

Foundation 011 defines the technical contract. Checkpoints 12-15 have now implemented:

```text
synthetic DGP and generated artifacts
hidden evaluator truth and benchmark self-tests
instrumented treatment workspace
project phases and protected-test semantics
condition-neutral trace
deterministic evaluator
provider-neutral model contract
strong B0 runner
static-knowledge B1 runner
model-call/token accounting
common generation retry semantics
provisional OpenAI real-model adapter
real-model calibration CLI
```

P0 remains deliberately unimplemented until real B0/B1 viability is observed.

Detailed reasoning: `docs/foundations/011_prototype_v0_technical_specification.md` and Checkpoints 012-015.

---

## Q-042. What do real B0/B1 calibration runs show, and what common baseline protocol should be frozen before P0?

**Current priority:** Highest  
**Status:** Awaiting empirical execution

The next decision must be based on real strong-model trajectories, not additional architecture speculation.

Development calibration should answer:

```text
Does the real model reliably follow the structured command protocol?
Does B0 complete the project within a reasonable budget?
Does B1 actually use the four static methodological concepts?
Do B0/B1 respect the protected final test voluntarily?
Do they identify the inherited preprocessing contamination?
Do they reason correctly about repeated entities and future deployment?
How do they react to the Phase 2 timing notice?
How many calls/tokens/tool actions are required?
Are retries or command-recovery semantics fair and reliable?
Which outputs must be retained for later blinded semantic judging?
What common development budget should be used when P0 is added?
```

Calibration may repair provider/interface defects affecting all conditions fairly. It must not be treated as held-out evidence.

The current assistant cannot execute paid calibration without a securely configured API credential and should not request that secret in chat.

After B0/B1 viability is established, the project can implement P0 against a baseline interface and budget that were fixed independently of P0.