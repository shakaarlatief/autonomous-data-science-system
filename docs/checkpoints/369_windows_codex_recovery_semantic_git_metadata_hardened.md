# Checkpoint 369: Windows Codex Helper Recovery and Semantic Git Metadata Lane Hardened

**Date:** 2026-09-07
**Status:** PASS / RUNTIME RECOVERED / SEMANTIC GIT HOST-METADATA ROUTING LIVE-QUALIFIED
**Checkpoint class:** OPERATIONAL RECOVERY + NARROW AUTHORITY HARDENING
**Project stage:** Research 113 upstream ecosystem architecture survey
**Scope:** Records recovery from a reproduced Windows Codex installation-generation helper failure, live qualification of the bounded semantic restart recovery path, and activation of the semantic-Git correction that keeps `.git` metadata writes on the existing bounded host Git substrate.
**Authority:** Validation 127 owns the detailed incident and release evidence; the public operations runbook owns the durable recovery sequence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

## 1. Runtime recovery

A Windows Codex installation-generation transition left the running Codex process unable to resolve `codex-windows-sandbox-setup.exe`. Tunnel forwarding remained healthy, but command execution failed before the requested command started.

Filesystem and sandbox-log evidence localized the problem to an orphaned generation: the running generation retained `codex.exe` while its sandbox helper/runner were absent, whereas another installed generation retained the complete helper set.

The already-qualified bounded restart path recovered the system:

```text
codex.runtime_maintenance restart_codexless
requestId  r122.sandbox-helper-recovery.20260907.01
status     succeeded
```

Fresh command execution then resolved the helper from the complete generation and passed again. Opening the visible desktop app had not fixed the failure, so desktop-window state is not part of the accepted recovery contract.

## 2. Semantic Git correction

The remaining semantic Git risk was architectural: `git add` and `git commit` were still sent through the ordinary Codex command sandbox even though they are repository-metadata mutations. The corrected implementation routes only those bounded metadata mutations through the pre-existing host Git substrate while keeping all semantic guards intact.

Focused regression:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
```

No `.git` ACL broadening, workspace-root expansion, force operation, arbitrary remote/refspec, credentials, configuration, shell or generic host-process authority was added.

## 3. Live release qualification

The corrected release bundle `semantic-git-host-metadata-v2` was preserved at private head:

```text
069d05a0dd1e79c95b5ee5abe53f9b83fbeb0395
```

The release sequence passed:

```text
prepare                prepared
pre-publish verify     mismatchCount=2 as expected
publish                succeeded
restart activation     succeeded
post-activation verify verified / mismatchCount=0
```

The public runtime contract remains preview.20 / 63 tools. This was an internal authority-routing hardening, not a public tool-surface expansion.

## 4. Durable operational lesson

`docs/local_execution/OPERATIONS.md` now records the reproduced helper-generation failure class and recovery order. In particular:

```text
PATH miss alone does not prove helper absence
preserve the managed tunnel when it remains healthy
prefer bounded semantic Codexless restart for an orphaned Codex generation
verify durable restart status plus a fresh read-only command
never broaden .git ACLs merely to restore semantic Git
route bounded repository-metadata mutations through the host Git substrate
```

## 5. Current boundary

Research 122 remains closed. AB-002 remains closed because its accepted runtime self-maintenance architecture performed the recovery and semantic publication needed here. Research 113 remains active, and Source Vault remains paused pending that broader Level-2 survey.

```text
CHECKPOINT_369=WINDOWS_CODEX_RECOVERY_SEMANTIC_GIT_HARDENED
RUNTIME_HELPER_RECOVERY=PASS
SEMANTIC_GIT_METADATA_LANE=PASS
AB002=CLOSED
RESEARCH122=CLOSED
NEXT=RESUME_RESEARCH113_UPSTREAM_SURVEY
```
