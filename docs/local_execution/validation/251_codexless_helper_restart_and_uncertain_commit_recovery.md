# Validation 251: Codexless helper-resolution recurrence, managed recovery, and uncertain Git receipt

**Date:** 2026-10-13
**Status:** RECOVERY VERIFIED / CHECKPOINT 898 PUBLISHED / RELIABILITY QUESTIONS PRESERVED
**Scope:** Record a Windows sandbox-helper recurrence, failed and successful managed restarts, cold-bootstrap release-dependency recovery, uncertain semantic Git receipt, tunnel deadline warnings, and a separate command-policy false positive.
**Authority:** Supporting local-execution incident evidence only. This record does not select an R0 physical architecture, qualify an R0-P03 reviewer, change evidence custody, authorize migration, or advance project authority. The evergreen recovery procedure remains `docs/local_execution/OPERATIONS.md`.

## 1. Existing evidence and classification

This incident recurred against the **exact helper-launch error** already reproduced in Validation 127 and Checkpoint 369 (2026-09-07):

```text
windows sandbox: orchestrator_helper_launch_failed
setup refresh failed to launch helper
helper=codex-windows-sandbox-setup.exe
error=program not found
```

Validation 209 preserves a **different** Windows sandbox failure, `helper_unknown_error: setup refresh had errors`, caused by validation of a Desktop-managed `cua_node` subtree. That separate defect was not established here, and no subtree was quarantined.

Validation 210 establishes that direct `codexless-http.cmd` launch is a cold-bootstrap path, not a substitute for a managed restart that rebinds active-release dependencies. Research 519/520 and Validations 212/213 document uncertain Git operation receipts, long-running duplicate deliveries, and the accepted exact-active semantic-Git coalescing repair. The present incident does not itself demonstrate regression of that specific repair.

## 2. Local observations of the sandbox helper

Model-free Runtime Bridge reads and GitHub reads initially worked, while `codex.command_exec` and guarded Git preflights failed before their requested commands ran. The owner's Windows sandbox log showed full-path launches from the complete installed generation around 13:28 local time, followed by failed bare-name helper launch attempts from approximately 13:31.

A read-only inventory showed that installed Desktop generation `2e5e00daee91c61d` contained `codex.exe`, `codex-command-runner.exe` and `codex-windows-sandbox-setup.exe`; two older generations contained `codex.exe` but not the helper or runner. A separate npm-based Codex App Server was running since October 4, while Desktop App Server and remote-execution server processes had started October 13. This coexistence does **not** prove that the older npm process was the source of the failing calls. Nor does the observed path transition prove that a Desktop update caused it.

Earlier `C:\Users\Default` access-denied warnings also occurred during otherwise successful setup and were not accepted as the blocker. No installation binaries or ACLs were changed.

## 3. First semantic restart failed

The managed tunnel was kept running. Runtime Bridge accepted/armed:

```text
action      restart_codexless
requestId   r0p03.win-helper-recovery.20261013.01
operationId rm_ccb293fb76a770542c1c2c5be0fd2191
```

Codexless then became unreachable. A local `http://127.0.0.1:7690/healthz` probe failed, no listener was found on port 7690, and the bounded process-name/command-line search found no running Codexless process. After cold bootstrapping restored bridge access, the **durable terminal status** for this first operation was read:

```text
status             failed
errorCode          RUNTIME_STARTUP_TIMEOUT
recoveryAttempted  false
```

An accepted or armed maintenance request is not evidence of a completed restart. The exact cause of the replacement-worker startup timeout was not isolated.

## 4. Cold bootstrap followed by dependency-aware restart succeeded

Because Codexless was fully unavailable, the owner used the runbook's approved cold/bootstrap fallback:

```powershell
$CodexlessLauncher = Join-Path $env:LOCALAPPDATA "Codexless\bin\codexless-http.cmd"
& $CodexlessLauncher
```

The service reported it was listening at `127.0.0.1:7690/mcp`. This restored MCP connectivity, but the GitHub read path returned:

```text
the OS-backed GitHub credential store is unavailable; plaintext fallback is forbidden
```

This is consistent with Validation 210's known release-dependency rebinding distinction. At this intermediate point, trivial model-free command probes also timed out. No credential fallback or reauthorization was attempted.

A **new** stable idempotency request for a semantic restart from the reachable bootstrap worker returned a durable success:

```text
action      restart_codexless
requestId   r0p03.manual-bootstrap-dependency-recovery.20261013.01
operationId rm_198b74b9b2c446af47db6c81f5269a5b
status      succeeded
errorCode   null
```

Afterward, one bounded GitHub branch read succeeded and a fresh read-only `git status --short --branch` through Runtime Bridge returned exit code 0. The same tunnel continued running. The recovered functionality is qualified by these post-restart observations; permanent elimination of the original helper-path issue is not proven.

## 5. Checkpoint 898: Git commit succeeded despite lost receipt

Before publication, the public ADS repository's expected parent was:

```text
159de980266e183cf24ee08d0ab2e9f7d4f1e1ba
```

There were exactly ten intended Checkpoint 898 changed paths and an empty index. Guarded fetch completed successfully. The guarded `codex.git_commit_paths` invocation returned an internal caller-visible error; subsequent calls initially met the single-operation concurrency ceiling.

**The commit was not retried blindly.** After the original operation settled, read-only Git reconciliation established:

```text
HEAD              b154de823443a52a39130d5acbb26a7a87d1a312
parent            159de980266e183cf24ee08d0ab2e9f7d4f1e1ba
changed paths     exactly the 10 authorized paths
index             empty
working tree      clean
tracking          ahead one commit before push
```

The guarded non-force `codex.git_push_ff_only` then reported `PUBLIC_REPOSITORY_INTEGRITY=PASS` and `postflightOk=true`. Independent GitHub read verified remote branch HEAD `b154de823443a52a39130d5acbb26a7a87d1a312`; final local status was synchronized and clean. The commit's existence is proven by repository reconciliation, **not** by a successful original commit-call receipt.

## 6. Tunnel response-deadline warnings and unresolved reliability

The owner's tunnel log screenshot contained messages of this form at around 14:18 and 14:23 local time:

```text
command response deadline reached; dropping without posting a response
```

This indicates that a command response missed the tunnel/client posting deadline. The warning alone does not prove that the underlying operation failed, stopped, or changed repository state. The screenshot evidence was insufficient to correlate those specific tunnel message IDs with the uncertain Git commit; no such causal match is claimed.

In later interaction, some `access=readOnly` `codex.command_exec` calls intermittently timed out while `codex.read_many` continued working, and `access=inherit` Git status succeeded. These are open command-execution profile/lifecycle or latency observations, **not** a proven root cause or reason to broaden permissions.

A separate conditional investigation is justified if deadlines or uncertain results recur in ordinary work. Capture correlated tunnel request IDs, Runtime Bridge operation IDs, host response deadlines, server-side completion, tool access profile, Codex process generation, and Git postflight evidence before changing timeout or concurrency settings. The previously qualified duplicate-delivery coalescing remains a distinct failure mechanism.

## 7. Separate command-policy false positive during incident documentation

An attempt to create this incident report initially used `codex.command_exec` with `node -e` and embedded the full Markdown document as a JavaScript string. Runtime Bridge rejected that request as a purported direct Codex model/control invocation. No file was created by the rejected request.

Read-only examination of the versioned private runtime source candidate's `public-command-policy.mjs` identified a regular-expression-based `Codex` executable-token check applied to inline Node.js source. A minimal live read-only reproduction confirmed the classification defect:

```text
node -e "process.stdout.write('Codex')"  -> blocked as model/control invocation
node -e "process.stdout.write('HELLO')"  -> exit 0, output HELLO
```

Neither reproduction invokes a Codex model. The lexical guard is valuable because the model-free command lane must not launch metered Codex work outside the approved agent workflow; the observed case is a **false positive on literal text**, not permission to weaken that guard. The inspected candidate source supports a plausible mechanism, but the exact deployed source revision and full scope of matching were not independently frozen here.

The documentation workaround uses a normal model-free file creation with a small inert placeholder, followed by the established bounded `codex.precise_edit` literal-text API. This does not run a model, bypass the explicit agent-call workflow, broaden host authority, or change the runtime implementation.

A future *separately qualified* reliability/guard regression should explicitly test legitimate quoted literals and genuine nested Codex executable invocations; any correction must continue blocking the latter.

## 8. Durable operational lessons and boundaries

1. Distinguish tunnel forwarding, Codexless HTTP availability, GitHub keyring/release-dependency health, and actual Codex App Server command execution.
2. On sandbox helper launch failure, inspect fresh logs and complete installation generations. `PATH` lookup failure alone does not prove absence of the helper. Do not assume unrelated npm/Desktop processes caused the failure without evidence.
3. Preserve a healthy tunnel. Use the bounded semantic restart when Codexless is reachable, and reconcile the **terminal** status with the same request ID.
4. If a managed restart fails and no Codexless HTTP process remains, use the documented cold/bootstrap fallback; once callable, perform a new semantic restart to bind active-release dependencies.
5. Verify GitHub-backed reads and fresh local command execution, not only a listener or healthy tool count.
6. If a semantic Git response is uncertain, check HEAD, parent, exact changed paths, index, local/remote branch state and GitHub before any retry. A dropped response can coexist with successful Git effects.
7. Do not equate the existence of response-deadline logs with a proved regression of duplicate-delivery coalescing; require correlated evidence.
8. For a tool guard false positive, reproduce the legitimate failure, preserve the security intent, and use documented authorized file-editing operations. Do not launch a Codex model through the model-free command route.

No tunnel restart, Codex reinstallation, broad process termination, sandbox disablement, ACL widening, private credential exposure, runtime guard modification, or architecture authority cutover occurred in this incident.

```text
VALIDATION_251=OPERATIONAL_EVIDENCE_PRESERVED
FIRST_MANAGED_RESTART=FAILED_RUNTIME_STARTUP_TIMEOUT
COLD_BOOTSTRAP=PASS
SECOND_MANAGED_RESTART=SUCCEEDED
GITHUB_READ_POST_RESTART=PASS
COMMAND_EXEC_POST_RESTART=PASS
CHECKPOINT_898_COMMIT=b154de823443a52a39130d5acbb26a7a87d1a312
CHECKPOINT_898_REMOTE_VERIFIED=true
COMMAND_POLICY_QUOTED_LITERAL_FALSE_POSITIVE=REPRODUCED
TUNNEL_DEADLINE_AND_STARTUP_ROOT_CAUSES=OPEN
R0_P03_AUTHORITY=UNCHANGED
```
