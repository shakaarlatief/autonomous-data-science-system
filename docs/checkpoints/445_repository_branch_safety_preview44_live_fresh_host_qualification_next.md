# Checkpoint 445: Repository Branch-Safety Preview.44 Live, Fresh-Host Qualification Next

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.44 LIVE / LOCAL QUALIFICATION COMPLETE / FRESH HOST NEXT
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve implementation, immutable release, activation, wire qualification, canonical branch reads, and deterministic no-write guards for Repository Branch-Safety Governance.
**Authority:** Validation 202 owns preview.44 implementation and local-live qualification. Validation 201 remains authoritative for the frozen family design and permanent canonical protection authorization boundary.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-22
**Conversation title:** 22 - GitHub CI Evidence Publication and Qualification
**Primary collaborator:** ChatGPT

The fifth and intended-final important GitHub extension family is now implemented and live locally.

Runtime state:

```text
releaseId       github-repository-branch-safety-governance-v1
version         0.1.1-preview.44-github-repository-branch-safety-governance
surface         codexless-public-preview-v2
public tools    172
GitHub tools    108
local-runtime   4e02b105e698265b72e449b8211a20aa20a22b14
manifest SHA256 7d9c84c5aef0994f8515f43d256b0c9836d4970b461207f189a8e81e74037ba3
```

The dedicated fake-dependency suite passes 13/13 and the immutable release published without recovery. Postpublication and postactivation verification both report zero mismatches. Health and readiness both identify preview.44 with 172 tools.

Fresh local MCP discovery exposes exactly:

```text
github.get_branch_protection
github.create_branch_safety_protection
github.delete_branch_safety_protection
```

with the frozen strict caller contracts. The read action requires only repository + branch. Both mutation actions require only repository + branch + expected head SHA. No general protection body, ruleset, check/review requirement, bypass actor, force/deletion allowance, credential or transport authority is projected.

The live canonical read baseline is:

```text
main
  3c7bcc51b10bfac787aee4b12cc3cd0f6b553400
  protected=false

v1-frontend-spike
  2480109fadeee1e480ef03b82e335aacdf9adf91
  protected=false
```

Two deterministic invalid local calls then proved the write boundary without changing GitHub policy. Stale `expected_head_sha=0000000` on create returned `GITHUB_BRANCH_HEAD_CHANGED` before PUT. Exact-head removal while no protection existed returned `GITHUB_BRANCH_SAFETY_PROTECTION_NOT_FOUND` before DELETE. Both were definite, non-retryable and non-uncertain. Postflight reads returned the same branch SHAs and protection states.

The implementation also fails closed when GitHub reports a branch protected while the classic protection endpoint is absent, and signed-commit protection is treated as a stronger non-baseline policy that the removal action must not delete.

No positive protection mutation has occurred. In particular, neither `main` nor `v1-frontend-spike` has been changed.

The next gate is a **fresh disposable ChatGPT-host qualification** because this persistent host predates preview.44 and may retain a stale projected tool surface. The fresh host should qualify all three exact schemas, read both canonical branches, and run deterministic invalid no-write guards only.

Only after that fresh-host gate passes may the disposable positive sequence be frozen and owner-authorized. Positive capability qualification must use a new temporary branch and must cleanly return the branch to unprotected state before deleting the branch itself.

Permanent application of the safety baseline to `main` and `v1-frontend-spike` remains a later separate owner decision after end-to-end capability qualification.

AB-030 remains parked unchanged.

```text
CHECKPOINT445=REPOSITORY_BRANCH_SAFETY_PREVIEW44_LIVE
FIFTH_FAMILY_IMPLEMENTATION=PASS
FIFTH_FAMILY_FAKE_TESTS=PASS_13_OF_13
FIFTH_FAMILY_LOCAL_WIRE=PASS_3_OF_3
FIFTH_FAMILY_LOCAL_READS=PASS_2_OF_2
FIFTH_FAMILY_LOCAL_NO_WRITE_GUARDS=PASS_2_OF_2
FIFTH_FAMILY_POSITIVE_WRITES=0
CANONICAL_BRANCH_PROTECTION_MUTATION=NOT_AUTHORIZED
AB030=PARKED_UNCHANGED
RESEARCH123=ACTIVE
NEXT=FRESH_CHAT_REPOSITORY_BRANCH_SAFETY_SCHEMA_GUARD_QUALIFICATION
```
