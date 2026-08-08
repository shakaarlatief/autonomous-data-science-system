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

**Status:** Substantially advanced through Q-039 and Q-040

Checkpoint 9 develops behavioral-trajectory evaluation, acceptance envelopes, visible-versus-hidden evaluator state, repair testing, process-versus-outcome separation, and meaningful simpler baselines. Checkpoint 10 turns these ideas into a first falsification experiment with B0, B1, and P0 conditions.

Still unresolved: exact evaluator implementation, semantic-judge assurance, final metrics, broader benchmark diversity, and later system-level scoring.

---

## Q-017. How should real projects become regression tests?

**Status:** Substantially advanced through Q-038, Q-039, and Q-040

Real failures can be distilled into reusable behavioral cases without copying private project circumstances. Cases should test applicability, safeguards, claim constraints, repair, reopening, and interaction.

Checkpoint 10 adds a first synthetic partially observable project family with held-out surface variants.

Still unresolved: long-term case representation, maintenance, diversity, and expansion beyond the first prototype family.

---

## Q-018. How should knowledge modules/packages interact?

**Status:** Substantially refined, not resolved

The preferred model is interaction through shared project state and shared questions, with cross-package reuse of smaller components. Direct hard-coded module calls should not be the primary integration mechanism.

Deduplication, composition, and cycle control remain open.

---

## Q-019. How should invalidation work?

**Status:** Substantially refined, not resolved

Typed dependency semantics, validity versus currency, materiality, reopening, and repair obligations are established conceptually. Later checkpoints extend invalidation to reusable knowledge and cross-project effects.

Checkpoint 10 provides the first concrete prototype event that must exercise dependency-aware reopening after an authoritative feature-timing revision.

Exact general propagation rules and automation beyond the prototype remain open.

---

## Q-020. What should the execution environment look like?

**Status:** Open, now entering prototype implementation

Isolation, dependencies, data access, artifact tracking, random-state control, failure recovery, compute limits, reproducibility, information barriers, and executable validators remain unresolved at production scale.

Checkpoint 10 narrows Version 0 to local file inspection, Python execution, simple model evaluation, project-state updates, and a controlled evaluator event.

---

## Q-021. How should model and tool providers be selected?

**Status:** Open

Provider diversity, quality/cost trade-offs, independent viewpoints, capability routing, and provider abstraction remain open. Provider choice should not determine the semantic architecture.

Checkpoint 10 requires the same strong underlying model across B0, B1, and P0 to isolate architecture from model capability.

---

## Q-022. How should external knowledge and source material be integrated?

**Status:** Increasingly coupled to knowledge quality

Reusable components need proposition-specific provenance, source scope, limitations, authority, version, and freshness handling.

The permanent source architecture remains open. Prototype V0 uses manually authored knowledge and therefore deliberately defers large-scale source integration.

---

## Q-023. Should raw conversations be archived?

**Status:** Open

Raw transcripts contain provenance but also duplication and obsolete reasoning. Their long-term role remains undecided.

---

## Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction of lessons, failures, candidate components, conflicts, or activation signals may become useful, but extraction must not imply automatic promotion into trusted knowledge.

Checkpoint 10 deliberately excludes automatic knowledge learning from Version 0.

---

## Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined by Q-038, not resolved

Knowledge role, maturity, and enforcement authority should remain separate. Challenge history, scope confidence, operational coverage, and independent review may matter more than one scalar confidence score.

Exact statuses remain open.

---

## Q-026. How should repository structure evolve?

**Status:** Open and now implementation-relevant

Future areas may include knowledge components, cases, experiments, evaluation suites, implementation, and sources. They should be added in response to real needs rather than speculative completeness.

Checkpoint 10 creates a concrete need to decide where prototype code, benchmark cases, evaluator assets, run logs, and treatment definitions should live.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not resolved

The current project constitution centers on semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance.

Prototype V0 operationalizes only a small subset through protected-final-evaluation, learned-transformation, feature-eligibility, and generalization-regime knowledge.

Formalization and broader project testing remain necessary.

---

## Q-028. How should project intent be represented?

**Status:** Substantially refined, not resolved

Objectives, constraints, deliverables, human-control preferences, and distinctions among project/model/operational objectives are important. Intent may begin provisionally and become more specific with evidence.

Prototype V0 uses only a narrow project brief rather than attempting the final intent schema.

---

## Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

The runnable-frontier concept separates mandatory obligations from optional work. Candidate factors include blocking power, risk reduction, decision impact, uncertainty reduction, dependency leverage, deliverable relevance, cost, reversibility, and project intent.

Checkpoint 10 deliberately uses only a minimal priority policy: satisfy hard blockers, resolve blocking questions, then use contextual LLM judgment among remaining legitimate high-value actions.

No general scoring mechanism is selected.

---

## Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under validation

The framework has survived conceptual stress tests and now informs knowledge components and behavioral evaluation. Prototype V0 begins empirical testing of a small subset rather than claiming the invariant set is complete.

---

## Q-031. What belongs in the admissibility layer?

**Status:** Substantially refined, not resolved

Admissibility is action-specific, source-aware, authority-aware, and may yield permitted, permitted-with-controls, approval-required, unresolved, or prohibited states.

Final authority and governance models remain open. Full admissibility is intentionally excluded from Prototype V0.

---

## Q-032. How should risk-sensitive assurance be represented?

**Status:** Substantially refined, not resolved

Current direction favors failure-scenario-based risk, inherent versus residual risk, credible controls, assurance obligations, and explicit risk acceptance authority.

Exact representation remains open and is intentionally outside Prototype V0.

---

## Q-033. Should analytical questions and claims be primary state objects?

**Status:** Strong design hypothesis entering implementation test

Questions act as integration points for modular reasoning. Proposed claims can activate evidence and validity checks. Reusable knowledge includes question templates and claim constraints.

Prototype V0 includes both `QUESTION` and `CLAIM` as distinct state types so this hypothesis can be exercised.

---

## Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

Completion likely requires all mandatory epistemic, admissibility, assurance, approval, and deliverable obligations to be sufficiently resolved; critical state to be consistent; no important output to depend on known-invalid state; and optional work to have insufficient marginal value.

Prototype V0 uses a much narrower milestone model: provisional development, repair after the authoritative notice, explicit readiness for final test, then final evaluation.

---

## Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Substantially refined, coupled to Q-008

These concepts belong in the candidate typed state and activation model. Exact schemas, authority provenance, control-effectiveness evidence, and approval staleness remain unresolved.

They are outside the first prototype except for methodological action blocking.

---

## Q-036. How should a new project be initialized?

**Status:** Substantially refined, not resolved

Checkpoint 5 develops progressive state construction, source-aware interpretation, information boundaries, structural bootstrap, multidimensional characterization, selective human clarification, and a stopping condition based on reaching a legitimate runnable frontier.

Prototype V0 will exercise only the minimum needed to ingest the project brief, README, files, code, structural facts, and contradictions.

---

## Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Substantially refined, entering empirical test

Checkpoint 6 develops reusable definitions, project-specific instances, deterministic/interpretive/open activation, prospective checks, missing-prerequisite activation, shared questions, coverage review, and orphaned-state detection. Checkpoint 7 adds component applicability.

Prototype V0 narrows this to four manually authored components and a combination of deterministic safeguards plus interpretive relevance/applicability reasoning.

Large-scale retrieval, deduplication, and coverage implementation remain open.

---

## Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved

Checkpoint 8 establishes a strong governance model: epistemic discipline applies to the knowledge library itself; project-specific results must be separated from candidate generalizations; minimum justified generalization should be preferred; reasoning mechanisms should be generalized rather than local winners; knowledge role, maturity, and enforcement authority are distinct; reasoning, reuse, and enforcement thresholds should rise progressively; counterexamples should challenge scope; negative and superseded knowledge should retain provenance; validity and currency are separate; staged change proposals should precede trusted mutation; material revisions may create cross-project revalidation obligations; and `no reusable knowledge update` is a valid outcome.

Still unresolved: exact maturity model, promotion authority, contradiction-resolution implementation, freshness policies, automatic learning architecture, and quantitative quality representation.

Detailed reasoning: `docs/foundations/008_knowledge_quality_generalization_and_evolution.md`.

---

## Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Substantially refined, not resolved

Checkpoint 9 develops behavioral project trajectories, visible versus hidden evaluator truth, acceptance envelopes, dynamic state changes, self-correction, repair precision, claim evaluation, selectivity tests, human-effort evaluation, process-versus-outcome separation, held-out cases, and strong simpler baselines.

Checkpoint 10 translates this into the first concrete synthetic churn case family and B0/B1/P0 comparison.

Still unresolved beyond Version 0: exact general case schema, semantic-judge assurance, system-wide scoring, larger benchmark diversity, human simulation, and long-term evaluator tooling.

Detailed reasoning: `docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md`.

---

## Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Status:** Substantially refined and specified for Version 0

Checkpoint 10 develops a concrete falsification experiment.

Current Version 0 hypothesis:

```text
one strong LLM
+ Python execution
+ nine minimal state object types
+ five minimal relation types
+ four manually authored knowledge components
+ deterministic prospective safeguards
+ interpretive activation/applicability
+ simple state-derived action selection
+ dependency-aware invalidation/reopening
+ one synthetic partially observable churn case family
```

Three experimental conditions should be compared:

```text
B0 = strong generic LLM workflow
B1 = same LLM plus the same small knowledge set as static prompt guidance
P0 = same LLM plus the structured semantic spine
```

The project includes repeated customer snapshots, temporal deployment, stale documentation, inherited preprocessing contamination, a protected final test, and an `account_state_code` whose legitimacy changes after an authoritative field-timing notice.

The central repair test is whether materially dependent models, evidence, decisions, and claims are reopened while unrelated valid work is preserved.

A development case plus two held-out surface variants should be used. Calibration may set budgets and remove evaluator ambiguity, but evaluation rules and numerical continuation thresholds must be frozen before held-out runs.

Strong evidence against P0 would occur if B1 matches its critical-integrity and repair behavior at materially lower complexity/cost, or if P0 introduces systematic false blockers, duplicate obligations, excessive reopening, or case-specific rules.

The strongest continuation signal would be reliable held-out reduction of critical methodological failures or stale conclusions without unacceptable overhead.

Detailed reasoning: `docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`.

---

## Q-041. How should Prototype V0 be represented and implemented concretely?

**Current priority:** Highest

Checkpoint 10 establishes what the first experiment must test while deliberately leaving production architecture unresolved.

The immediate implementation task is to build the benchmark/evaluator first and then the smallest P0 treatment needed to execute the pre-specified experiment.

Important unresolved questions include:

- What exact synthetic data generator and fixed DGP version should be implemented?
- What should the visible contents and provenance metadata of `project_brief.md`, `README.md`, and the authoritative Phase 2 notice be?
- How should the hidden evaluator truth and acceptance assertions be represented?
- What exact baseline-model contamination should be encoded?
- What minimal status vocabulary is required for the nine state object types?
- How should objects and the five dependency relations be serialized for Version 0?
- How should state history be preserved without introducing a premature event-sourcing architecture?
- How should actions be proposed, checked, allowed, blocked, executed, and logged?
- How should deterministic safeguards and interpretive knowledge activation share one control loop?
- How should the four knowledge components be represented minimally?
- How should B0, B1, and P0 receive comparable model/tool budgets?
- How should run traces, token/tool cost, critical violations, repair completeness, repair precision, detection latency, and project utility be logged?
- Which evaluator assertions can be deterministic and which require semantic judgment?
- What repository structure is appropriate for prototype code, cases, evaluators, treatment definitions, and run results?
- Which implementation choices should be treated explicitly as disposable prototype conveniences rather than architectural commitments?

The benchmark world and evaluator should be implemented before tuning P0 behavior so that the treatment is not judged against a benchmark retrospectively designed around its own trajectory.