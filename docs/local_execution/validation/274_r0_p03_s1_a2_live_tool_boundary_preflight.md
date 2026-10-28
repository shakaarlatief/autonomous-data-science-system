# Validation 274: Direct S1 A2 public-route authority probes and candidate-intake preparation

**Date:** 2026-10-28
**Status:** LIVE_BOUNDARY_OBSERVATIONS_COMPLETE / PUBLIC_CWD_ROUTE_ONLY / ACTUAL_REVIEWER_ENVIRONMENT_NOT_YET_TESTED
**Scope:** Verify concrete, source-free Runtime Bridge tool-cwd access behavior and the exact initial model-facing reviewer intake artifact. Do not claim OS filesystem security, unseen provider histories, actual neutral-author isolation or non-arm actor qualification.
**Basis:** Research 606–608; Validation 272–273; S1 A2 R01–R08 requirements; Checkpoint 898 and Specification 028.

## Observed probes, not simulated tests

The current Runtime Bridge `codex_project_context` returned an active Codex project-root context, locally resolved project permission profile and a project-attached model environment. The read-only workspace registry showed multiple independently authorized roots. Publicly preserving this capability observation does not expose their concrete private paths or contents.

All `codex_read_many` checks used `cwd=C:\Projects_Data\autonomous-data-science-system`, bounded output, and no model-agent execution:

```text
A2_PUBLIC_CWD_KNOWN_PUBLIC_FILE_READ=PASS
A2_PUBLIC_CWD_SIBLING_REGISTERED_ROOT_READ=REFUSED_OUTSIDE_TRUSTED_ROOT
A2_PUBLIC_CWD_UNREGISTERED_OS_FILE_READ=REFUSED_OUTSIDE_TRUSTED_ROOT
A2_PRIVATE_SIBLING_FILE_BYTES_RETURNED=NO
A2_OS_CONFIGURATION_BYTES_RETURNED=NO
A2_OS_ACL_ISOLATION=NOT_TESTED
A2_FUTURE_BLIND_AUTHOR_ACTUAL_TOOL_ROUTE=NOT_TESTED
A2_PROJECT_ATTACHED_ENGINEERING_SESSION_REVIEWER_INDEPENDENCE=NOT_QUALIFIED
```

The negative tests checked only the *public cwd* trust boundary and did not assert target-file existence, denial by actual filesystem ACLs, denial under a different registered workspace authority, or behavior of ChatGPT/Claude/author-facing connectors. The review of the tool registry and project bootstrap is not equivalent to an independent reviewer's self-inventory.

## Follow-on artifact and self-consistency preflight

New single-file, source-free candidate-session text:

`experiments/r0_p03_navigation_probe/S1_A2_CANDIDATE_REVIEWER_LIVE_ENVIRONMENT_INTAKE_V01.md`

The artifact directs a separate future session to inspect only the capabilities it actually sees without reading connected files, private directories, repository contents, historical sources, or other conversations. It requires TESTED / VISIBLE_UNTESTED / UNAVAILABLE / UNKNOWN separation and prohibits promoting self-reported separation to independent identity certification or author-release authority. It is **prepared, not sent**. Its bytes/SHA-256 are independently checked in the final repository preflight.

**Critical nonpromotion:** A real prospective reviewer-session response must be owner-relayed and separately assessed. Its self-report can establish at most observed/reportable context and provisional fit. An **independent challenger and actual authorization to deliver a pinned historical batch remain absent**, and the project-attached current coordinator is not appointed as either.

## Scientific holds

```text
VALIDATION_274=LIVE_PUBLIC_CWD_TOOL_BOUNDARY_PRELIMINARY_WITNESS
PUBLIC_CWD_POSITIVE_READ=PASS
PUBLIC_CWD_CROSS_WORKSPACE_READ=DENIED_BY_TOOL
PUBLIC_CWD_OUT_OF_ROOT_READ=DENIED_BY_TOOL
REAL_REVIEWER_EXTERNAL_INTAKE=NOT_EXECUTED
ACTUAL_REVIEWER_OR_CHALLENGER_ADMISSION=NO
ACTUAL_BLIND_AUTHOR_ISOLATION_TEST=NOT_EXECUTED
ACTUAL_REAL_SOURCE_RECORDS_DELIVERED=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
