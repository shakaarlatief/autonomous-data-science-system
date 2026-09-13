# Research 132: Cross-Model ICM Reconciliation and Architecture-Synthesis Readiness

**Date:** 2026-09-13
**Status:** CROSS-MODEL OWNER-SOURCE RECONCILIATION COMPLETE / REQUIREMENTS V0.2 UNCHANGED / MC-0012 RESOLVED / CANDIDATE ARCHITECTURE SYNTHESIS READY / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Reconcile ChatGPT Research 131 with Claude MC-0012 Message 003 after independently staged ICM exposure, preserve convergent and complementary findings, classify remaining uncertainties, and decide whether additional Claude dialogue is needed before Research 124 resumes architecture synthesis.
**Authority:** Supporting Research 124 synthesis evidence only. This record does not amend Requirements V0.2, select a target architecture, or authorize migration.
**Declared references:** `research:124`, `research:131`, `path:docs/model_collaboration/threads/MC-0012/RESOLUTION.md`, `checkpoint:470`, `checkpoint:473`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`

## 1. Comparison integrity

The staged comparison remained usable.

Claude Message 001 froze the post-evidence/pre-owner-source position. Message 002 then exposed the owner-provided ICM source while explicitly withholding ChatGPT's post-source Research 131 interpretation. Claude Message 003 states that it did not read Research 131, Checkpoint 471 or Research 124 Section 71 before writing its assessment.

Claude inspected the full ICM paper and the principal current `RinDig/icm-architect` method/reference files, including `SKILL.md`, `references/core.md`, `references/forms.md`, `references/system-map.md` and `references/reference-integrity.md`. It disclosed that it did not directly open the repository README or template files. ChatGPT's Research 131 had already inspected those additional surfaces, so the combined source coverage is broader than either pass alone.

Both models were unable to use the supplied Instagram reel as substantive evidence and both refused to infer unseen video content.

```text
CROSS_MODEL_SOURCE_COMPARISON=VALID
CLAUDE_POST_SOURCE_CONTAMINATION=NO_EVIDENCE_OF_CONTAMINATION
INSTAGRAM_CONTENT_USED_AS_EVIDENCE=NO
```

## 2. Strong convergence

The independent post-source assessments converge on the important architectural conclusions. Both conclude that ICM is highly relevant as incremental evidence, is not a ready-made ADS successor, should not reopen Requirements V0.2, and should not be privileged because the owner supplied it. Both strongly reinforce a small stable routing/bootstrap core, task-shaped progressive context loading, one-home-per-fact and source/derived separation, cold-agent behavioral reconstruction tests, dependency-local change-impact reasoning, and concrete move/reference-integrity mechanisms. Both also conclude that the current repository has materially evolved beyond the paper, that the empirical evidence is preliminary rather than controlled universal proof, and that ICM's sequential human-reviewed target class is substantially narrower than ADS on authority, temporal semantics, concurrency, public/private governance and multi-workstream continuation.

```text
REQUIREMENTS_V02_AMENDMENT=NO
REQUIREMENTS_COUNT=50
INVARIANTS_COUNT=17
ICM_TARGET_SELECTION=NO
TARGET_ARCHITECTURE=NOT_SELECTED
```

This convergence is especially useful because Claude formed the judgment before reading Research 131.

## 3. Complementary findings from Claude

### 3.1 L0/L1 token calibration

Current `references/core.md` gives concrete routing-layer sizes: L0 `CLAUDE.md` at 300-800 tokens and L1 root `CONTEXT.md` at 200-500 tokens. Together this is a rough 500-1,300 token routing/bootstrap calibration point. `SKILL.md` separately says the root entry file should target under roughly 60 lines. This is useful external calibration for KA-R32 / KA-I12 and later active-core budgeting, but not evidence for a universal ADS constant. ADS should measure its own task classes and treat the ICM numbers as one comparator.

### 3.2 Verified/stale provenance pattern

The current System-map form states that `status: verified` requires a date, a branch/commit or vault revision, and citations; `stale` is an allowed visible state. This sharpens Research 131's more general observation about source citations and freshness coordinates. The design question is whether a derived knowledge/card surface can make freshness and verification state explicit without pretending that a confident narrative is current merely because it exists. This remains a candidate mechanism under KA-R18, KA-R23 and KA-R35.

### 3.3 Recurrence before structural pattern claims

ICM's guardrails include a concrete anti-pattern heuristic: one local complaint is not enough to declare a structural pattern; recurrence across independent instances is stronger evidence. Claude correctly links this to its own earlier overgeneralization from the dispatch incident. The exact ICM threshold should not become an ADS law. Its value is the epistemic discipline that a single memorable incident is not equivalent to a proven recurring architecture mechanism.

### 3.4 ICM often sidesteps dispatch/fidelity rather than solving it

Research 131 already states that ICM does not substantially solve KA-R09 and related authority problems. Claude sharpens why: ICM's reliability model assumes explicit stage contracts plus human review at every boundary, so it does not test the same autonomous situation-dispatch and post-activation contract-fidelity mechanisms exposed by ADS baselines. Absence of contradiction from ICM is therefore not ICM validation of ADS dispatch/fidelity behavior.

### 3.5 Factory/product is distinct from source/derived authority

Claude usefully separates ICM's factory/product axis, stable reference/configuration versus per-run working/output material, from ADS's source/derived axis, authoritative knowledge versus rebuildable/projection representation. The axes can correlate in some workflows but are not equivalent. Candidate architectures should avoid mapping one directly onto the other without evidence.

### 3.6 Move safety does not solve semantic merge/split identity

ICM's move procedure gives a good operational answer for preserving references across rename/move and path-carrier migration. It does not answer the harder Research 126 question of deciding whether two historical records represent the same underlying semantic object, or when one object should split into several identities. Identity merge/split governance therefore remains a candidate-design risk under KA-R46 rather than a solved ICM problem.

## 4. Research 131 findings not displaced by Claude

Claude's Message 003 does not challenge several Research 131 additions, so they remain in the candidate mechanism pool:

```text
positive + negative context contracts, including explicit do-not-load boundaries
routing-payload pressure as an active-surface smell
repeating-unit-first representation/form selection
source-improvement proposals from repeated downstream correction
source-map-like semantic provenance for selected high-consequence transformations
cross-stage Verify contracts
explicit forward + reverse dependency/reference walks
case-fold collision checks and copy -> verify parity -> remove migration discipline
```

Claude independently reinforces several indirectly through the walk test, System-map form and reference-integrity procedure, but supplies no counter-evidence against the rest.

## 5. Evidence calibration after both reviews

ICM is credible prior art and practitioner-engineering evidence. It contains operational mechanisms already used in real workspaces and a current repository more developed than the original paper. At the same time, the paper explicitly acknowledges self-selection, informal practitioner reporting, single-model-family testing and absence of a controlled ICM-versus-monolithic comparison.

Research 124 therefore keeps the hierarchy:

```text
ICM mechanism/example evidence
    useful for candidate construction and qualification probes

ICM universal performance claims
    not established

ADS frozen requirements
    remain grounded in the broader combined field:
    owner constitution + historical evidence + blind ChatGPT baselines + D1-D8
```

The symmetry matters: ADS's blind historical baseline also remains ChatGPT-only. Neither evidence program should be generalized beyond what it actually tested.

## 6. Remaining named risks entering synthesis

No remaining item justifies more broad research before candidate construction, but several risks should stay visible:

```text
identity merge/split/entity-resolution governance
single-model historical baseline limitation
KA-R07 governing/risk-bearing discovery circularity
evidence-class visibility at consumption time
dispatch reliability as a repeated-trial qualification metric
consequence-aware C_failure calibration
representation-observability bias against radically simple candidates
```

These are candidate-design and qualification pressures, not unresolved requirement-definition blockers.

## 7. Is another Claude turn needed now?

No. A further MC-0012 round has low expected epistemic value at this boundary because the independent post-source comparison already produced strong convergence, the remaining differences are complementary mechanism details rather than unresolved contradictions, Claude accepted the important Phase-1 correction, and both models agree V0.2 should remain frozen. Revealing Research 131 now could produce comparative commentary, but there is no material disagreement that needs adjudication before synthesis.

The better use of a future Claude turn is after concrete candidate architecture work exists and there is something falsifiable or design-specific to challenge.

```text
ADDITIONAL_MC0012_DIALOGUE_REQUIRED=NO
MC0012_PURPOSE=SATISFIED
```

## 8. Architecture-synthesis readiness

The evidence program is now ready to move into architecture synthesis. Readiness does not mean the answer is known. It means the project now has a measured current-state baseline, bounded historical failure evidence, blind current-architecture ChatGPT baselines, broad cross-disciplinary evidence, D1-D8 targeted deep dives, the owner-frozen 50 KA-R / 17 KA-I acceptance boundary, ChatGPT's independent ICM evaluation, Claude's post-evidence/pre-ICM reassessment, Claude's independent post-ICM evaluation, and cross-model reconciliation of the source's incremental contribution.

The next phase should construct materially different serious architecture families or mechanism combinations and reason from the complete evidence field. Alternatives exist to expose assumptions, trade-offs and falsifiable claims, not to create a shallow score-and-pick tournament. ICM-derived mechanisms are now part of that design vocabulary alongside materially different possibilities; they are not the default target.

```text
RESEARCH132=CROSS_MODEL_ICM_RECONCILIATION_COMPLETE
REQUIREMENTS_V02_AMENDMENT=NO
MC0012=RESOLVED
TARGET_ARCHITECTURE=NOT_SELECTED
ARCHITECTURE_SYNTHESIS_READINESS=READY
NEXT=CANDIDATE_ARCHITECTURE_SYNTHESIS
```
