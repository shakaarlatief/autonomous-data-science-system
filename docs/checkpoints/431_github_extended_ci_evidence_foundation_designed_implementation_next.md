# Checkpoint 431: Extended GitHub CI Evidence Foundation Designed, Implementation Next

**Date:** 2026-09-10
**Status:** PASS / CHECKS + COMMIT STATUS FOUNDATION FROZEN / SIX TOOLS / NO CI-EVIDENCE MUTATION
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Freeze the second beyond-parity GitHub extension family: bounded first-class Checks plus namespaced commit-status publication.
**Authority:** Validation 188 owns family selection, six-action caller contracts, annotation/status-transition safety rules, status-context namespace ownership, and explicit deferrals. Checkpoint 430 remains authoritative for completion of the first Repository Administration extension.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

The second beyond-parity GitHub extension family is frozen as **CI Evidence Publication**. It contains six actions: three Checks reads (`get_check_run`, `list_check_runs_for_ref`, `list_check_run_annotations`), two Checks writes (`create_check_run`, `update_check_run`), and one commit-status write (`create_commit_status`). The live GitHub App installation independently reports both `checks=write` and `statuses=write`.

The Checks write surface is deliberately narrower than GitHub's raw API. Caller-selectable states are only queued/in-progress/completed; GitHub-Action-only waiting/requested/pending are excluded; stale conclusion is excluded; completed requires a conclusion; timestamps remain server/GitHub-owned. Optional output supports bounded title/summary/text and at most 50 strict repository-relative line annotations. Images, requested actions, arbitrary details URLs and raw-details payloads are deferred.

Check-run updates are read-before-write and monotonic: queued may advance to in-progress/completed, in-progress may advance to completed, and completed cannot reopen. The exact check-run scope is re-read inside the serialized mutation boundary. Mutation uncertainty is never automatically replayed.

Commit-status publication is also narrowed. Caller supplies state plus `context_suffix`; Runtime Bridge owns the full context prefix and always writes `codexless/<suffix>`, preventing accidental impersonation/overwrite of unrelated CI status contexts. Arbitrary `target_url` is not exposed in the first slice. The commit SHA is first resolved inside installation-authorized repository scope and the exact SHA is used for the one mutation attempt.

Manual check-suite creation/preferences and rerequest actions are deferred. Check runs automatically create/associate their suite, while rerequest triggers webhook events that the current intentionally disabled App webhook receiver does not own end-to-end.

No CI-evidence mutation occurred. The next boundary is local implementation/publication of these six actions with fake-dependency tests and no positive Check/status write. Fresh-host qualification comes after live activation; positive CI-evidence writes remain separately owner-authorized for one exact commit SHA and visible evidence payload.

```text
CHECKPOINT431=GITHUB_EXTENDED_CI_EVIDENCE_FOUNDATION_DESIGNED
EXTENDED_CI_EVIDENCE_FOUNDATION_ACTIONS=6
EXTENDED_CI_EVIDENCE_READS=3
EXTENDED_CI_EVIDENCE_WRITES=3
CHECKS_PERMISSION=LIVE_WRITE_CONFIRMED
COMMIT_STATUSES_PERMISSION=LIVE_WRITE_CONFIRMED
CI_EVIDENCE_MUTATION_OCCURRED=false
RESEARCH123=ACTIVE
NEXT=IMPLEMENT_EXTENDED_CI_EVIDENCE_FOUNDATION
```
