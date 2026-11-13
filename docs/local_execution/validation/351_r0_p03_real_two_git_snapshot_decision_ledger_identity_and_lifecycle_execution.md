# Validation 351: Real two-snapshot decision ledger status, temporal and scope qualification

**Date:** 2026-11-13
**Status:** REAL_V03_EXECUTED_AND_EXACT_GIT_SOURCE_REPLAY_VERIFIED / POSTDOCUMENT_FULL_INTEGRITY_PENDING
**Scope:** Actual original Git source evidence at two public revisions, 35+36 decision sections, 94 fixed request templates, false snapshot leakage, false operational interpretation, conflicting decision identity and supersession scope.
**Research:** Research 652.
**Authority:** Fixed T2 V03 method contract, exact original source sections/result, Research 652, Checkpoint 915; earlier formal Research 513/559/576 remains unscored.

## Original Git and executed evidence

Two original `docs/DECISIONS.md` Git blobs are read directly, never from mutable worktree, at exact revisions S0 `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, S1 `6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3`. All 71 source section identities, original Status and scope/date witness lines and source blob digests are recorded.

The first complete V03 method run produced an exclusive-create JSON without prior result failure. Exact artifact **710228 bytes**, SHA-256 `c22d6b1e62616066f55e22b8811feb21e383e6a568de36a06faf38de7d6d8a27`. It contains 94 original query/results, all candidate rankings, evidence-guarded statuses, deliberate naive baseline errors and source snippets. No case was dropped or rescored.

- **72** original-source status requests: 71 correct source-recorded statuses plus one correct bounded absence (D-036 at S0).
- **8** unknown IDs (D-900 to D-903 repeated): all return not recorded in this examined snapshot, not global nonexistence.
- **10** source ID/title conflicts: all refuse source Status.
- **4** governing requests (D-035/D-036 × two snapshots): three return a verbatim `not yet operational authority` source statement, one reports bounded source absence. **No asserted positive operative-governing fact.**
- **6** superseded-and-scope witnesses preserved (D-003/D-011/D-015 both revisions).
- **1** naive latest-only time leakage and **1** naive accepted-is-operative false claim against directly contradictory source text.
- Section lexical top-one wrong section for **39 of 94** requests overall, including **19 of 72** original status requests. This lexical OR/BM25 comparator is not optimized exact-ID retrieval and is not a full capable architecture B0/B4 arm.

The dedicated **9/9** tests passed (0.37 seconds): byte-exact two-snapshot rerun, original Git blob identity and every recorded line witness, section uniqueness/error controls, scope qualifiers, D-036 temporal introduction, conflicting title and unknown decision ID controls, negative operative state and 94-request matrix invariants.

## Observed final precommit validation

All selected test suites below actually completed successfully in separate bounded runs (not inferred from previous checkpoints):

| Actual focused suite | Observed |
| --- | --- |
| New T2 V03 real 94 decision questions, two exact Git blobs, record/section/line source integrity, conflicts, scopes and status | **9/9 PASS** (0.37s) |
| Previous T2 V02 118-request exact source-identity and challenge regression | **10/10 PASS** (0.82s) |
| Previous V03 native Specification 025/028 declarations and collaboration identity/state validation | **41/41 PASS** (7.15s) |
| Previous T2 V01 120-source manifest/titles reconstructed from original Git | **2/2 PASS** (19.31s) |
| Previous T2 V01 full original Git-source rerun and immutable result comparison | **1/1 PASS** (19.32s) |
| Remaining previous T2 V01 synthetic and saved output safety controls | **5/5 PASS** (0.20s) |
| Protected C02 evidence-boundary/source-identity regression (no private source access) | **15/15 PASS** (0.18s) |
| **All nonoverlapping successful groups** | **83/83 PASS** |

Additional actual checks:
- `scripts/check_current_routing.py`: **PASS**, Checkpoint **915**, boundary `p-three-t-two-real-decision-ledger-snapshot-and-scope-tested`, original R0-P03 outcome `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **652**, **916** numbered checkpoint records, 19 subject groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **916/916** numbered checkpoints compliant.
- `git check-attr text`: **unset** for the complete original 710228-byte result, preventing Git line-ending translation.
- `git diff --check`: successful exit 0 after removing one observed trailing whitespace defect in new `CURRENT_STATE.md` text. Routine Windows tracked text line-ending warnings are not integrity failures.
- Complete `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including family-aware contracts, Project Knowledge validation, Checkpoint, Knowledge Map, collaboration and routing.
- Exact original V03 saved file SHA-256/length: **PASS**, 710228 bytes, hash `c22d6b1e62616066f55e22b8811feb21e383e6a568de36a06faf38de7d6d8a27`.

**Not verified:** independent model/human scoring, actual physical deployment authority, neutral currentness truth, production architecture, and the formal Research 513/559/576 R0-P03 experiment. Published Git SHA, branch matching and committed Git blob identities must be checked after actual commit and push, not inferred from precommit tests.
