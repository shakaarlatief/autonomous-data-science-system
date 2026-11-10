# Validation 311: Real 2,539-record task-independent source-world family coverage gate

**Date:** 2026-11-10
**Status:** LIVE_PINNED_GIT_AUDIT_AND_BYTE_RECOMPUTATION_PASS / 16_SYNTHETIC_INTEGRATED_REGRESSIONS_PASS / ZERO_AUTOMATIC_SOURCE_ADMISSIONS
**Research:** 625, 622, 590–593, 513. **Checkpoint:** 898 unchanged. **Specification:** 028 unchanged.

## 1. Real pinned-Git execution, distinct from synthetic tests

Executed:

```powershell
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.source_world_coverage_gate .
.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.source_world_coverage_gate . --verify-only
```

Both operations returned exit 0. The second printed `SOURCE_WORLD_COVERAGE_REPRODUCIBILITY=PASS` after independently reconstructing and byte-comparing both the complete local ledger and public-safe receipt from exact committed Git source bytes. There was no task/answer selection, owner-private source read or author-visible ZIP construction.

```text
SOURCE_PIN=c57556a8bf993a1d327e9197acb7b7c745071cd8
COMPLETE_ACCOUNTED_ROSTER=2539
PRELIMINARY_CANDIDATE=406_UNQUALIFIED
ADDITIONAL_HISTORICAL_REVIEW_ONLY_TEXT=2123
ADDITIONAL_HISTORICAL_UNSUPPORTED=10
ADDITIONAL_HISTORICAL_TOTAL=2133
ROSTER_SHA256=eb6c3686172a5848dc45370635d673c268b7676c5b6233475dbb58486861a750
WORLD_FROZEN=NO
AUTOMATIC_AUTHOR_ADMISSIONS=0
SCORED_PRIMARY_TASKS=NOT_STARTED
B0_B4_RESULTS=NONE
```

Critical task-independent path-family capacity flags observed:
- cold_start_current_orientation: `historical_status` only outside unqualified 406;
- impact_analysis_architecture_evolution: `historical_status` only outside unqualified 406;
- exact_source_authority_recovery: `historical_status` and `execution_evidence` only outside unqualified 406;
- cross_plane_discovery: product_source/project_source/verification have candidate path hints, but actual three-answer sufficiency is `NOT_PROVEN`.

These are **path-family hints, not evidence of complete authority or answerability**. Other source worlds and modalities are separately outside the 2,539 source-audit roster. This result must not be misrepresented as a successful science fixture freeze.

## 2. New source-free implementation and controls

- `experiments/r0_p03_navigation_probe/source_world_coverage_gate.py`: combines Research 590's existing 406 source-window construction with Research 591's exact pinned 2,133 historical inventory, validates source ref, existing exact Git object IDs and supported text digests, rejects overlaps and unsupported-text promotion, and records one explicit unadmitted status for every enumerated carrier.
- Complete per-source ledger written under ignored `.venv/.r0_p03_source_world_coverage/` with no overwrite; independent byte-rebuild verification. It is owner-local engineering diagnostic, not a future task-author packet.
- Aggregate safe receipt contains only family counts, required-capacity hints, source roster digest and `SCORED_AUTHOR_WORLD_NOT_READY`. No per-source paths or risk flags are printed in the receipt.
- Four source family categories are prospective diagnostics only and do not define the twelve primary tasks or alternative source-selection quotas.

## 3. Synthetic negative controls and fix

Test file `tests/unit/test_r0_p03_source_world_coverage_gate.py` verifies:
- disjoint candidate/review inventory, exact 8 synthetic sources and no automatic admission;
- category capacity deficits independent of lexical test flags;
- source pin mismatch, duplicate paths, unexpected already-admitted status, unsupported formats with fake text digest, malicious path, bad Git blob identity and source-role drift rejected;
- deterministic output across different insertion orders;
- source-specific risk strings do not appear in safe printed receipt; changing a private hint changes the source-roster commitment.

First synthetic invocation found one **validation-order issue**: an invalid source ref supplied against a non-Git temporary fixture raised "Not a Git checkout" before "Historical source pin changed." No invalid data was accepted, but the more specific prospective pin refusal should precede the check. It was corrected by verifying the required pin before the Git-directory check. The next test run combined nine new tests and seven existing historical/front-end candidate tests:

```text
16 passed in 9.21s
```

No real owner-private Wave0 documents were opened. New tests do not qualify any semantic decision.

## 4. Next concrete experiment-critical gate

Task-independent qualification is needed specifically for safe, sufficient historical status and execution-validation evidence, with separate independent non-arm source-status review/acceptance and actual missing-context/contamination attack. A safe lexical screen or exact Git provenance alone is insufficient. The reviewer pool can be risk-stratified and bounded based on demonstrated source-family needs rather than automatically repeating the ten-record Wave0 review process on every source.

Independently complete the author-facing source/role/authority closure and freeze its exact bytes before twelve scored primary task authoring. Neutralized nine legacy cases and reference custody remain separately guarded under Research 559. Common substrate mechanics can be prepared without minting J1/J2 semantic authority, exposing old gold or constructing/scoring B1–B4 before task freeze.

```text
VALIDATION_311=REAL_PINNED_SOURCE_COVERAGE_AUDIT_BYTE_REPRODUCIBLE
SYNTHETIC_NEGATIVE_AND_INTEGRATION_TESTS=16_OF_16_PASS
TASK_INDEPENDENT_FAMILY_DEFICITS=HISTORICAL_STATUS_AND_EXECUTION_EVIDENCE
COMPLETE_REVIEW_POPULATION=2539
SOURCE_ADMISSIONS=ZERO
SCORED_AUTHOR_WORLD=WORLD_UNFROZEN
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
