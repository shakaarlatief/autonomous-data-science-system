# Validation 312: Pinned historical dependency frontier and shared lexical preflight

**Date:** 2026-11-10
**Status:** REAL_GIT_SOURCE_DEPENDENCY_V2_REPRODUCIBLE / REAL_NEUTRAL_LEXICAL_INDEX_DELETE_REBUILD_PASS / NO_SOURCE_ADMISSIONS_OR_SCORES
**Research:** 626, 625 and 513 Section 6. **Previous validation:** 311.
**Scope:** Verify real historical source citation-frontier accounting and common read-only lexical engineering, explicitly without deciding semantic authority or exposing unadmitted materials to future experimental actors.
**Source pin:** `c57556a8bf993a1d327e9197acb7b7c745071cd8`.
**Checkpoint:** 898 unchanged. **Specification:** 028 unchanged.

## Real historical evidence experiment

Executed against the pinned public Git tree:

```powershell
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.historical_evidence_dependency_frontier .
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.historical_evidence_dependency_frontier . --verify-only
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.historical_evidence_dependency_frontier . --cross-family
```

The final `--cross-family` calls the same independent byte-identity regeneration before reading the saved local graph. `HISTORICAL_DEPENDENCY_FRONTIER_REPRODUCIBILITY=PASS` was observed. A first exploratory V1 local artifact was superseded by a new no-overwrite V2 after tests showed a relative-link parsing omission. No old artifact was overwritten or silently accepted as V2.

```text
COMPLETE_PINNED_SOURCE_POPULATION=2539
CRITICAL_HISTORICAL_AND_VALIDATION_SOURCES=2003
DOCUMENT_TEXT_SCANNED=1855
OTHER_TEXT_NOT_SCANNED_AS_DOCUMENT=674
UNSUPPORTED_NOT_READ=10
DIRECT_CORE_CITED_HISTORICAL_RECORDS=82
ADDITIONAL_TWO_HOP_HISTORICAL_RECORDS=133
DIRECT_CORE_CITED_VALIDATION_RECORDS=0
ADDITIONAL_TWO_HOP_VALIDATION_RECORDS=3
EXACT_RESOLVED_TEXTUAL_REFERENCE_EDGES=7262
STATUS_TO_VALIDATION_MENTION_EDGES=642
VALIDATION_TO_STATUS_MENTION_EDGES=427
RECIPROCAL_MENTION_PAIRS=199
VALIDATION_RECORDS_WITH_STATUS_REFERENCE_EITHER_DIRECTION=239_OF_247
VALIDATION_RECORDS_WITH_NO_DETECTED_STATUS_REFERENCE=8_OF_247
V2_FRONTIER_SHA256=7a582f743bf183a826c01cb02a6e570e5914569458842beecc205c33838076de
NO_AUTOMATIC_SOURCE_ADMISSIONS=PASS
```

These counts describe only literal reference mentions and exact pinned source identities. They do **not** establish accepted authority, source sufficiency, validation outcome, temporal currentness or a semantic dependency. The 239/247 wider cross-family finding is a particularly important falsification of a proposed narrow two-hop author-source inclusion shortcut. The full per-source reference graph is in ignored `.venv/.r0_p03_historical_dependency_frontier_v02/`, not a future source author packet or public model-scoring input.

## Real common retrieval engineering preflight

Executed:

```powershell
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.neutral_readonly_retrieval_candidate .
```

Returned exit 0. SQLite FTS5 3.45.3 indexed all 2,529 source-readable pinned Git text files with exact blob/size/SHA-256 verification, preserved ten unsupported files explicitly outside the text surface, and independently rebuilt the disposable in-memory index after deletion:

```text
READABLE_GIT_TEXT=2529
UNSUPPORTED=10
SOURCE_WORLD_ROSTER_SHA256=eb6c3686172a5848dc45370635d673c268b7676c5b6233475dbb58486861a750
TEXT_SUBSET_SHA256=7a97f5c1b2fb825f981d8805a55f807a4772ae186ff52f8027a8ee43e531ab02
EPHEMERAL_DELETE_AND_REBUILD_PARITY=PASS
CONNECTOR_READABLE_DERIVED_ORIENTATION_EQUAL=TRUE
SEMANTIC_GOVERNING_CURRENTNESS=UNKNOWN_UNQUALIFIED
AUTHOR_RELEASE=NONE
SCORED_ARM_OR_TASK=NONE
```

This is a common substrate *engineering* candidate, not the completed Research 513 V03 common semantic substrate: accepted effects, roles/owners, lineage, J2 coverage, receipts and meaningful derived entry points remain unqualified, and are explicitly marked unknown. No scored task/query, B1–B4 metadata, comparator result or claim of B0 advantage has been made.

## Synthetic tests and negative controls

New tests:

- `tests/unit/test_r0_p03_historical_evidence_dependency_frontier.py`: invented-only first/second-hop, exact relative and numbered references, ambiguity, missed citations, source unadmitted state, unsupported media, malicious path and exact Git blob vs mutable worktree identity, cross-family count neutrality.
- `tests/unit/test_r0_p03_neutral_readonly_retrieval_candidate.py`: invented-only lexical matching with provenance/unknown labels, derived orientation common capability boundary, in-memory rebuild parity, lexical query/operator escaping, query-only SQLite, tampering, missing/unsupported bytes and prohibited auto-admission.

An early synthetic frontier run caught the missing unadorned relative-reference parser case, which was repaired and written under a new V2 output identity. No actual source world or experimental tasks were selected as a result.

Combined regression included the prior Research 625 full roster audit and frontend/historical census suites. The final integrated test execution returned **34/34 PASS**, with exit code 0. The separate real pinned-V2 frontier `--cross-family` recheck returned `HISTORICAL_DEPENDENCY_FRONTIER_REPRODUCIBILITY=PASS` and the full real neutral FTS5 delete/rebuild returned PASS. Repository integrity returned `PUBLIC_REPOSITORY_INTEGRITY=PASS`; Git `diff --check` returned exit 0 for tracked changes. Publication remains separately checked.

## Scientific consequence

Real linked historical status and validation evidence exists and the common lexical transport is technically feasible, but the independence/eligibility and authority/source-world gates remain OPEN. Next, perform substantive, proportionate independent source-family qualification with linked evidence and false-exclusion controls, then a prospectively frozen author source world, independent twelve-task author and separate nine-case neutralization, followed by protected gold and actual equal-source B0–B4 comparison.

```text
VALIDATION_312=REAL_HISTORICAL_FRONTIER_AND_COMMON_LEXICAL_PREFLIGHT
HISTORICAL_FRONTIER_V2=BYTE_VERIFIED
CROSS_FAMILY_CITATION_AGGREGATE=REPRODUCED
COMMON_FTS5_EPHEMERAL_REBUILD=PASS
SOURCE_ADMISSIONS=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
