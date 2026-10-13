# Checkpoint 898: R0-P03 source-only legacy capsule and independent-reference execution readiness

**Date:** 2026-10-13
**Status:** SOURCE_CAPSULE_PREPARED / REVIEWER_EXECUTION_AND_GOLD_CUSTODY_UNQUALIFIED / EXACT_FIXTURE_UNFROZEN
**Checkpoint class:** MIXED / ENGINEERING_VERIFICATION_AND_CONTINUITY
**Project stage:** R0-P03 prefixture independent-reference execution and authority qualification
**Scope:** Independently inspect the existing capsule implementation, repair demonstrated path/readback defects, verify immutable source content, and preserve the unresolved reference execution/custody boundary.
**Authority:** Local engineering evidence for ChatGPT's independent inspection and acceptance; not an independent reference annotation, scored probe, experiment freeze, private-repository charter change or physical-target decision.
**Interaction environment:** Codex desktop
**Project / workspace:** Autonomous Data Science System
**Interaction session:** codex-01
**Conversation title:** 01 - R0-P03 Source Capsule Verification
**Primary collaborator:** Codex; ChatGPT/chatgpt-38 retains task ownership and subsequent acceptance
**Research:** Research 562
**Validation:** Validation 250
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `159de980266e183cf24ee08d0ab2e9f7d4f1e1ba`

The existing two untracked capsule files were inspected without discarding them. The original 36-test P03 suite passed. Targeted regressions then demonstrated raw-path normalization/Windows handling gaps and a missing saved-byte verification step. Bounded repairs validate raw relative paths and compare each closed saved source with its immutable Git input before issuing an integrity receipt. Validation 250 records the actual final checks and preservation scope.

The prepared capsule reconstructs **65 original historical source carriers** at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, totaling **1,725,920 bytes**, plus nine neutral numbered theme aliases. It exports only `sources/`, `reviewer_intake.json` and `capsule_integrity.json`, excluding original B1 relevance annotations, required/rejected sets, answer fixtures and Git history. Its independently recomputed source-content digest is `baf2b893435c1951b52814a3de897f7684890b1449bb437b46948cc868d304d3`. Scratch exports remain under ignored `.venv`, with no overwrite of existing destinations.

This is successful **source-content preparation**, not reviewer confinement. Codex has access to the full public repository/history/design and is not a fresh reference writer or evaluator. No reviewer execution surface, exposure attestation, restricted complete-gold custody, independent legacy answers, primary-task authoring/selection route or exact experimental freeze has been qualified. The existing private companion remains knowledge preservation only; no private repository or charter was changed. Thirty-six decision headings verify a possible owner-event population, not twelve suitable tasks.

Original Research 217/W5 evidence and scores, Research 513, previous accepted checkpoints and unrelated executable code remain unchanged. Owner-approved Option A remains prospective and unexecuted; retain nine legacy cases with >=8/9, twelve primary cases with >=10/12, and zero false-authority tolerance. R0-P01 AMEND/deferred, R0-P02 PASS, V03 logical selection and Specification 028 operational authority remain. No score, task/answer key, held-out draw, physical architecture selection or cutover occurred.

**Next:** ChatGPT independently inspects this uncommitted unit, then qualifies a concrete fresh reviewer execution boundary, authorized restricted complete-gold preservation and one permitted primary-task route before any exact experiment freeze. No automatic Claude review or new evaluator launch. Commit and push are intentionally left to the governed task-owner workflow.

## Promotion audit

Research 562 and Validation 250 preserve the evidence; current routing, Current State, Knowledge Map and MC-0030 carry the new boundary. No new foundation, specification, decision, architecture acceptance or private authority is warranted by these local source-copy mechanics. Independent task-owner review and publication remain pending.

```text
CHECKPOINT_898=R0_P03_SOURCE_ONLY_LEGACY_CAPSULE_PREPARED
NEXT_ACTOR=chatgpt
NEXT_BOUNDARY=p-three-reviewer-execution-authority-qualification
LEGACY_SOURCES=65_BYTE_VERIFIED
LEGACY_TOPIC_HINTS=9_NOT_AUTHORED_QUESTIONS
FRESH_REVIEWER_EXECUTION=NOT_QUALIFIED
RESTRICTED_COMPLETE_GOLD=NOT_QUALIFIED
PRIMARY_TASKS=NOT_AUTHORED
LEGACY_OWNER_OPTION_A=APPROVED_NOT_EXECUTED
HISTORICAL_W5=UNCHANGED
P03_FIXTURE=UNFROZEN
P03_SCORE=NOT_OBSERVED
R0_P01=AMEND_DEFERRED
R0_P02=PASS
PHYSICAL_TARGET_SELECTED=false
PUBLICATION=NOT_PERFORMED
```
