# Research 625: Real pinned source-world coverage and the critical family-closure objective

**Date:** 2026-11-10
**Status:** REAL_FULL_2539_ROSTER_ACCOUNTED / TASK-INDEPENDENT_FAMILY_GAPS_VERIFIED / NO_AUTO_ADMISSION / SCORED_WORLD_UNFROZEN
**Scope:** Exact pinned-Git, task-independent accounting of the existing source-world candidate and historical review population; identify critical family gaps without adjudication, source release, task selection or score.
**Authority:** Non-scored engineering observation. Neither an independent source-status judgment, source-world freeze, scored task, reference answer nor architecture comparison.
**Basis:** Research 513 Sections 6.2–6.10; 559 Option A; 576 Level B; 577, 579, 590–593, 622–624; owner-authenticated Wave0 ten-source review at Validation 310.
**Pin:** `c57556a8bf993a1d327e9197acb7b7c745071cd8`.
**Checkpoint/operational authority:** 898 and Specification 028 unchanged.

## 1. Why this is a material transition

The owner requested momentum toward the actual R0-P03 B0–B4 experiment. Wave0's real independent source reviews and protected adjudication produced ten *proposed* decisions and a readable owner-private review. That evidence does not establish safe, complete author admission for the wider repo. Repeating the same review format across all historical records as a default would be costly without evidence it is necessary. Neither over-conservative exclusion nor silent contaminated-source admission is acceptable.

We therefore executed a **task-independent, live pinned-Git coverage audit of the entire existing 406 + 2,133 source review population**. Unlike the earlier Wave0 report mechanism, it does not decrypt private evidence, perform model classification or request another owner cryptographic handoff. It identifies the missing evidence *families* that make experiment capacity especially fragile.

New implementation: `experiments/r0_p03_navigation_probe/source_world_coverage_gate.py`. It reconstructs the earlier candidate and historical-source populations from exact pinned Git blobs, checks each existing candidate's SHA-1 blob binding, validates historical text records and unsupported-format status, rejects duplicates, maintains a complete local evidence-status ledger, and emits only source-free aggregated counts plus a fixed identity digest. It is deliberately NOT a scientific authority classifier or scored-cohort sampler.

## 2. Actual live audit observations

```text
HISTORICAL_SOURCE_PIN=c57556a8bf993a1d327e9197acb7b7c745071cd8
NONSCORING_CANDIDATE_SOURCES=406
EXTRA_HISTORICAL_REVIEW_RECORDS=2133
HISTORICAL_TEXT_REVIEW_ONLY=2123
UNSUPPORTED_HISTORICAL_REPRESENTATIONS=10
COMPLETE_ACCOUNTED_SOURCE_ROSTER=2539
ROSTER_SHA256=eb6c3686172a5848dc45370635d673c268b7676c5b6233475dbb58486861a750
SOURCE_ADMISSIONS=0
AUTHOR_WORLD=WORLD_UNFROZEN
SCORED_TASKS=NOT_STARTED
B0_B4_SCORING=NOT_STARTED
```

Source family presence, **not authority, currentness, semantic eligibility or task answerability**:

| Path-family evidence hint | 406 preliminary candidate | Review-only historical / unsupported |
| --- | ---: | ---: |
| Orientation | 3 | 0 |
| Governing decision/specification | 29 | 0 |
| Product frontend source | 210 | 0 |
| Project runtime source | 35 | 0 |
| Verification/test source | 37 | 80 |
| Tooling/ scripts | 54 | 48 |
| Source schemas | 9 | 2 |
| Other candidate docs | 29 | 0 |
| Historical checkpoint/research status | 0 | 1,746 / 10 unsupported |
| Historical execution/validation | 0 | 247 |

This coverage partition is a deliberately simple, source-neutral *path-family diagnostic*. It must not be used as a model or source classifier. A checkpoint can be important historical evidence without being current authority; a specification can declare obligations without proving deployed realization; test code can exist without a passing receipt. Unsupported research representations are not irrelevant merely because they cannot be decoded as text.

The existing candidate has hints for every family in the **cross-plane** category, but *none* of those hints proves that three source-grounded independently answerable questions exist. The other three categories depend on historical status and/or execution evidence **found only in the currently unadmitted review population**:

- Cold-start/current orientation: historical status evidence unqualified.
- Impact/evolution: historical status evidence unqualified.
- Exact-source/authority/recovery: historical status **and** execution/validation evidence unqualified.
- Cross-plane discovery: preliminary role families exist, but authority/context/realization closure unproven.

No category passes a scored author readiness gate from this audit. All four have `task_answerability=NOT_PROVEN`.

## 3. Next bounded substantive source closure, not a new universal review machine

The minimal critical path now has a clearer scientific target:

1. Qualify a prospective **task-independent subset or representation of necessary historical status and execution/validation evidence**, while accounting for the entire 2,539-roster and rigorously preventing old W5/R217 answer, R0-P03 design/rubric or comparator leakage.
2. Resolve actual authority, scope, temporal qualifiers, supersession and selected linked-source context for that candidate evidence. Unsupported references remain explicit HOLD. An independent non-arm source-status decision is required before any author-facing admission. A clean lexical flag is not that decision.
3. Independently falsify **false exclusions**: if the restricted historical evidence is essential to legitimate current/evolution/recovery needs, missing context must be addressed rather than quietly selecting easier tasks. Independently falsify **false admissions**, including contamination without obvious strings and source family combined-exposure leakage.
4. Produce an exact prospective source-world manifest and independent bounded author-exposure contract, then **freeze** its bytes and admissible access before commissioning the genuinely fresh twelve-task author. Keep Research 559's nine legacy cases and the original 65-carrier world separate.
5. In parallel, prepare only **arm-neutral** adapters, source/lineage/authority-unknown representation and common view equality controls. Do not build B1–B4 variants in advance of the required twelve-task freeze under Research 513.

**No arbitrary finite review quota** or blanket exclusion is adopted here. Future cohort design must demonstrate sufficient Project/Product, accepted/proposed, implementation/validation, evolution/recovery and exact authority capacity at its prospectively specified scope. The 406 existing candidate files are also *unqualified*, not a freely authorable safe baseline.

## 4. Execution and evidence boundary

Real audit command:

```powershell
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.source_world_coverage_gate .
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.source_world_coverage_gate . --verify-only
```

The full `R0_P03_SOURCE_WORLD_COVERAGE_NON_ADMISSION_LEDGER.json` remains under ignored `.venv/.r0_p03_source_world_coverage/`. It contains exact source names and risk-flag hints and is **not** attached to a future blinded task author. A public-safe aggregate receipt is saved beside it. No private Wave0 report was accessed and no source-specific confidential classifications were copied to the public repository.

The new tests are entirely fictional; the live recomputation is separately observed against the real historical Git repository. Neither is a substitute for independent source-status adjudication.

```text
RESEARCH_625=REAL_COMPLETE_TASK_INDEPENDENT_SOURCE_FAMILY_AUDIT
HISTORICAL_FAMILY_CLOSURE=UNQUALIFIED_AND_MATERIAL
SCIENTIFIC_SOURCE_WORLD_FREEZE=NOT_STARTED
SOURCE_ADMISSIONS=ZERO
R0_P03_PROBE_RESULTS=NONE
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
