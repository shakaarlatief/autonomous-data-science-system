# Research 561: R0-P03 independent legacy reference intake and primary-task authorship method candidate

**Date:** 2026-10-13
**Status:** PREFREEZE INDEPENDENT-REFERENCE METHOD PREPARED / HISTORICAL INTAKE SCRUBBED / NO FRESH REVIEWER OR GOLD ASSIGNED
**Scope:** Establish a minimal, source-bound, mechanically reproducible reviewer input for owner-approved legacy-answer re-adjudication and specify the separate primary-task/answer custody method without authoring neutral questions, choosing tasks, editing old gold or scoring R0-P03.
**Parent:** Research 217, 503, 507, 512, 513, 556-560; Research 559 owner Option A; Research 560 / Checkpoint 896; Claude MC-0030 Message 062 and ChatGPT Message 063.
**Immutable coordination input:** `54b603c5fe550af963aac808b1fe7cacb516c6d4` (published Checkpoint 896).
**Historical source world:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` (original W5 T1 V02 corpus revision).
**Authority:** Proposal for independent reviewer *process*, not an accepted scored task packet, original historical W5 change, a new owner-scoring decision, verified reviewer assignment, or future production J1/J2/J3 mechanism.

## 1. Why the method needs explicit separation

Research 513 Section 6.5 requires twelve new tasks: three each for cold-start/current orientation, cross-plane discovery, impact/architecture evolution, and exact-source/authority/recovery. It permits either a fresh non-arm task author or a mechanically preregistered historical owner-query/event selector, with the latter preferred if fresh independence cannot be convincingly established.

Research 513 Section 6.6 retained nine historical Research 217 scenarios as separate legacy regression cases. Research 559 records the owner's express **Option A acceptance**, prospectively replacing the old B1-authored gold *basis* with independent arm-neutral re-adjudication before scoring, while preserving old W5 data, nine cases, >=8/9 gate, 12-primary gate and authority controls.

The original `navigation_scenarios_v02.json` does **not** contain independently authored natural-language owner questions: each of the nine scenario IDs is itself a B1 subject name, accompanied by its B1 candidate subjects, legacy topics, must-retrieve and must-not-retrieve lists. `corpus_annotations_v02.json` specifies `ChatGPT / chatgpt-27` with independence `NOT_CLAIMED` and supplies 65 B1-labeled carriers. Reusing those answer sets as neutral gold would reproduce Claude's F1 circularity.

An exposed ChatGPT or Claude critic who has inspected that old gold cannot restore fresh independence simply by writing a new paraphrase or "confirming" that the historical answers look reasonable. The valid task is therefore **preparing an isolated source and theme intake**, followed by a genuinely independent reviewer who authors the questions and source-backed answers. No such reviewer has yet been engaged.

## 2. Executable intake: historical world, not an answer key

New non-scored artifacts:

| Artifact | What it does |
|---|---|
| `experiments/r0_p03_navigation_probe/independent_reference_intake_candidate.py` | Reads immutable Git objects for two old W5 fixture files, extracts *only* the 65 carrier paths and nine source theme strings, resolves historic blob identities at the original source ref, and creates deterministic, scrubbed reviewer input. |
| `experiments/r0_p03_navigation_probe/legacy_blinded_intake_candidate.json` | Reproducible exact-Git manifest of **65 path@blob carriers** plus **nine neutral numbered case aliases** and subject-originated **theme hints**; no required/rejected source sets, B1 memberships, preferred subjects, answers or scorer outputs. |
| `experiments/r0_p03_navigation_probe/independent_reference_method_candidate.json` | Non-executing, prospective responsibilities, ordering, original thresholds, incomplete source/gold custody requirements and explicit fail-closed conditions. |
| `experiments/r0_p03_navigation_probe/INDEPENDENT_REFERENCE_INTAKE_BRIEF_CANDIDATE.md` | Input instructions for a future fresh neutralizer/annotator, with source-world restrictions, exposure attestation and output conditions, but **no invented answers or independent authorship claim**. |
| `tests/unit/test_r0_p03_independent_reference_intake.py` | Ten deterministic read-only checks for exact Git binding, scrubbed nonleakage, stable theme aliases, 65/9 counts and unchanged scientific gates. |

Immutable-Git source excerpt reference is not the same as "source role accepted." The 65 sources are those of the original historical W5 world, not automatically a representative new whole-system corpus. The source manifest is a **prepared review input** only. All nine case IDs are numbered `legacy-01` through `legacy-09`; the subject-derived hints are *not* presented as valid historical user questions or as relevance labels. The review-facing JSON records original-input **digests under neutral aliases** instead of exposing the paths to historical answer files.

The original Research 217/W5 fixtures remain untouched, including original historical 9/9 B1 and 4/9 comparator results. They do not become R0-P03 scores.

## 3. Actual independence limitations and the reviewer boundary

The scope of independence is source-based **reference interpretation**, not erasure of historical experimental design. There are two residual limitations that cannot be quietly declared solved:

1. The **historical 65-carrier universe itself was selected for B1's original experiment**, and the nine theme hints descend from B1 topics. Independently adjudicated answers within that fixed world are more defensible, but the nine-case regression still is **not** an independently sampled whole-system navigation benchmark. The twelve new tasks carry that broader role.
2. The original W5 materials remain retrievable from the public repository. A local sanitizing script cannot prevent a reviewer from opening the prior gold or arriving with earlier exposure. An admissible reviewer therefore needs both an **isolated historical source snapshot** without old subject annotations/gold or R0-P03 design, and a credible exposure declaration. Fresh reviewers must not be ChatGPT/chatgpt-38 or Claude/claude-04, who have already seen source labels.

Before any neutral answer is accepted, a fresh reviewer must transform *each* historic theme into an arm-neutral, independently grounded information need, explaining its historical meaning and scope without treating the B1 subject boundary as a rule. The reference must then judge required answer claims, source path@blob evidence, relevant and actually irrelevant evidence, ambiguous boundaries, negative authority assertions and any truly justified N/A. An extra relevant citation must not fail merely because old B1 annotations excluded it. A disagreement adjudicator/criterion must be prospectively declared; no after-the-score repair.

The person neutralizing questions and the person adjudicating can be the same genuinely unexposed non-arm actor **if the applicable independence/exposure and disagreement-review requirements remain satisfied**; the method does not automatically multiply reviewer roles. At least two fresh scored evaluators remain the separate Research 513 judgment requirement.

## 4. New twelve-task source and authoring method remains a separate readiness check

An exact-source read-only scan at the Checkpoint 896 ref observed **36 numbered D-xxx decision headings** in `docs/DECISIONS.md`. This supports the existence of a historical decision-event candidate pool but **not** the existence of twelve answerable, diverse, arm-neutral tasks. Decision headings alone also cannot demonstrate three suitable tasks each for cross-plane J2 evidence, AO/WARRANT-F, impacts or recovery.

The next prospective fixture must therefore select **one qualified Research 513-compliant authoring route**:

- **Fresh non-arm author**, demonstrably unexposed to comparator outputs, using a closed common source world; or
- **Prospectively frozen mechanical historical owner-query/event rule**, audited for genuine owner-event provenance, all four required task categories, exact source closure, ability to handle obsolete/superseded events, and no post-draw cherry-picking.

This Research deliberately selects **neither route** until independence or algorithmic eligibility is actually demonstrated. The exposed model may design and test source mechanics, but cannot choose the scored twelve or their correctness rubric by hand and present them as independent. The task source closure and authority verdicts must be established **before** task-conditioned BUILD selection; force inclusion of minimal task closure without hinting at it in arm-visible metadata. If a source closure cannot fit into the 60 build target, stop for prospective correction before score, rather than making an arm fail an unanswerable question.

## 5. Full gold custody is an access boundary, not an invented tool

Research 559 requires freezing and committing a separately versioned neutral answer packet **before arm construction**, while preventing arm authors from reading hidden reference answers. Committing plaintext gold to the same public branch as the arms would immediately violate the purpose.

A sound minimum future procedure is:

1. Independent reviewer prepares and **durably versions the entire scoring packet in an access-restricted boundary** not reachable by arm authors. Record reviewer/exposure, exact source blobs, content bytes and version ID.
2. Before any arm authoring, publicly commit a digest/commitment binding that exact complete packet, along with the prospective rule and permitted evaluator disclosure conditions. A digest alone, without the complete packet preserved in a verified restricted revision, is **insufficient**.
3. Arm authors may see the common build source world and method, **not** answer labels or task source-to-gold maps. All B0-B4 arm rules and authored build metadata freeze before the later public deterministic 20-carrier heldout draw.
4. A predeclared, independently fresh evaluator accesses the reference packet through the qualified scoring boundary, verifies its commitment and source revisions, and applies the unchanged 10/12 primary, >=8/9 historical and zero false-authority controls.

No access-restricted gold store, versioned answer packet, neutralizer, evaluator or independent mechanical selector has been qualified or activated here. They are **explicit blockers to actual scoring**, not grounds to invent a private-cryptographic infrastructure or claim a hypothetical reviewer was consulted. If a qualified low-cost existing private workspace cannot be established, fail closed and request a specific bounded decision rather than publishing gold prematurely.

## 6. Next bounded work

The historical scrubbed intake and non-scored contract are ready for **independence/custody feasibility**. Next validate that the reviewer can actually receive a closed historical source snapshot, perform the review without old B1 labels, and durably preserve independently authored answers. Concurrently evaluate whether the 12-primary task route can be mechanical with genuine owner-event category closure or needs a fresh author. Neither task route nor any numeric scoring rule is silently frozen here.

No new R0-P01 trial, R0-P02 reinterpretation, R0-P03 arm, original fixture edit, final filesystem topology or authority cutover. V03 remains the selected logical successor, GOVERNED_LEDGER_KERNEL_V02 the leading *unselected physical candidate*, and Specification 028/continuity the current operational authority.

```text
R0_P03_REFERENCE_INTAKE=SOURCE_BOUND_SCRUBBED_METHOD_CANDIDATE
SOURCE_COMMIT=54b603c5fe550af963aac808b1fe7cacb516c6d4
HISTORICAL_SOURCE_REF=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
LEGACY_SOURCE_CARRIERS=65_VERIFIED
LEGACY_THEME_HINTS=9_NON_GOLD
LEGACY_CASE_IDENTIFIERS=NEUTRAL_01_TO_09
RESEARCH217_HISTORICAL_FIXTURES=UNCHANGED
LEGACY_OPTION_A=AUTHORIZED_NOT_EXECUTED
FRESH_ANNOTATOR=UNASSIGNED
PRIMARY_TASK_AUTHORING_RULE=UNSELECTED
INDEPENDENT_GOLD=NOT_AUTHORED
GOLD_RESTRICTED_DURABLE_STORAGE=NOT_QUALIFIED
EXACT_FIXTURE=UNFROZEN
SCORING=NOT_EXECUTED
```
