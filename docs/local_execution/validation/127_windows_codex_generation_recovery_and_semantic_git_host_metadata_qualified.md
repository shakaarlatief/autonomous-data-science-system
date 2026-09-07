# Validation 127: Windows Codex Generation Recovery and Semantic Git Host Metadata Lane Qualified

**Date:** 2026-09-07
**Status:** PASS / CODEX HELPER RECOVERY + SEMANTIC GIT HOST-METADATA ROUTING LIVE-QUALIFIED
**Research:** post-Research 122 operational hardening; Research 113 remains active
**Scope:** Preserve the reproduced Windows Codex helper-resolution failure, bounded recovery, semantic-Git metadata-routing correction, and live release activation.

## 1. Reproduced failure and localization

Tunnel forwarding remained healthy while Codex App Server command execution failed before the requested command started:

```text
windows sandbox: orchestrator_helper_launch_failed
setup refresh failed to launch helper
helper=codex-windows-sandbox-setup.exe
error=program not found
```

The sandbox log first showed a successful full generation-qualified helper launch and, seconds later, a bare-name helper lookup failure. Filesystem inspection then showed:

```text
9ba750cce02d5e5c  codex.exe present; sandbox helper and command runner absent
8e5b6932251c2c1c  codex.exe, command runner, sandbox helper and code-mode host present
c60635126245daef  no required Codex binaries present
```

This supports an installation-generation transition that orphaned the already-running Codex process from a complete helper set. It does not prove which desktop UI action or product update initiated the transition. A failed global `where.exe codex-windows-sandbox-setup.exe` is not decisive because healthy Codex resolves the helper relative to its own installation generation rather than requiring it on `PATH`.

## 2. Bounded restart recovered execution

The accepted semantic maintenance path was used with requestId `r122.sandbox-helper-recovery.20260907.01`. Durable status returned `restart_codexless / succeeded`, `errorCode=null`, and `recoveryAttempted=false`.

After restart, fresh Codex processes selected the complete `8e5b6932251c2c1c` generation. The sandbox log again showed full-path helper resolution and copied command-runner launch. Fresh read-only `command_exec` succeeded. Opening the visible desktop app had not fixed the failure, so desktop-window state is not part of the recovery contract.

## 3. Semantic Git metadata lane hardening

A separate issue remained: `git add` and `git commit` were still routed through the ordinary Codex command sandbox, where current Windows policy can deny writes to existing `.git` metadata.

The corrected `commitPaths` implementation now requires the existing bounded host-process substrate and routes only exact `git add` and `git commit` mutations through `#runHostGit`. Read-only preflight/postflight remain on the ordinary authority executor. Existing expected-HEAD, attached-branch, exact-upstream, transient-state, empty-index, protected-path, exact-staging, diff-check, parent and clean-index postconditions remain intact.

No `.git` ACL broadening, workspace-root expansion, force operation, arbitrary remote/refspec, credentials, configuration, shell or generic host-process authority was added.

Focused qualification returned:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
SEMANTIC_GIT_CANDIDATE_REGRESSION=PASS
```

## 4. Live corrected release

The final bundle is `semantic-git-host-metadata-v2`, preserved at private source HEAD `069d05a0dd1e79c95b5ee5abe53f9b83fbeb0395`.

```text
semantic-git target  7a423b1032cac099c40b19abf38f210a9df986f34d31830003403f9d744ce3e7
regression target    bba54d73323dd4b3dceb0e149983ffbc85e4ead5aec50c55c5c1222323a7aea7
```

The regression target is correctly modeled as `add` because it was absent from the installed preview.20 tree. An earlier v1 attempt modeled it as `replace`; the runtime-release baseline guard rejected that attempt before live mutation.

The corrected v2 lifecycle passed:

```text
prepare                    prepared
pre-publication verify     verification_failed / mismatchCount=2 (expected baseline evidence)
publish                    succeeded
restart activation         succeeded
post-activation verify     verified / mismatchCount=0
```

The public contract remains `0.1.1-preview.20-runtime-release`, `codexless-public-preview-v2`, 63 tools. Only internal semantic-Git implementation and regression coverage changed.

## 5. Post-activation semantic commit proof

After activation and post-activation release verification, the repaired `codex.git_commit_paths` surface was used again on the public repository with one exact declared documentation path, expected-HEAD binding, empty-index precondition, exact staging, diff and parent checks. The commit succeeded through the semantic surface, providing a real post-activation proof that repository metadata mutation no longer depends on the ordinary Codex command sandbox.

```text
SEMANTIC_GIT_POSTACTIVATION_COMMIT=PASS
```

## 6. Durable recovery rule

For the same failure class:

```text
1. distinguish tunnel reachability from Codex App Server command execution;
2. inspect the sandbox log for full-path helper launch versus bare-name fallback;
3. inspect Codex installation generations for codex.exe plus helper/command runner;
4. do not infer helper absence from PATH lookup alone;
5. if a complete generation exists but the running process is orphaned, use bounded semantic Codexless restart;
6. require durable restart success plus one fresh read-only command;
7. if semantic Git alone fails on .git metadata, keep .git protected and use the bounded host Git substrate rather than ACL broadening.
```

The public operations runbook owns this procedure going forward.

## 7. Disposition

This incident does not reopen Research 122 or AB-002. The already-qualified self-maintenance architecture performed the recovery and semantic publication used here. Research 113 remains active.

```text
WINDOWS_CODEX_HELPER_GENERATION_RECOVERY=PASS
SEMANTIC_GIT_HOST_METADATA_ROUTING=PASS
RUNTIME_RELEASE_V2=VERIFIED
AB002=REMAINS_CLOSED
RESEARCH122=REMAINS_CLOSED
NEXT=RESEARCH113_UPSTREAM_SURVEY
```
