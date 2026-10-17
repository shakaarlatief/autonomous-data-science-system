# Research 581: Windows Codex helper-generation restart with functional postflight recovery

**Date:** 2026-10-17
**Status:** COMMAND_EXEC_FUNCTIONALLY_RECOVERED / RESTART_MAINTENANCE_RECEIPT_FAILED_STARTUP_TIMEOUT / NO_RELEASE_OR_SECURITY_CHANGE
**Scope:** Record the recurrence of an exact Windows Codex sandbox helper-resolution failure, its grounded correspondence to Validation 127, the single managed Codexless restart and the independently verified command-execution recovery despite a failed supervisor startup receipt.
**Basis:** Validation 127 (2026-09-07), Research 430 (2026-10-01), Research 580 (2026-10-16), owner-relayed current Windows Codex process/helper inventory, and ChatGPT/chatgpt-39 read-only direct Runtime Bridge postflight.
**Authority:** Operational incident and response evidence only. Does not change R0-P03 scientific roles/gates, Checkpoint 898, Specification 028, repository access policy, active routing, runtime release source or model-provider privileges.

## Initial failure and diagnosis

On 2026-10-17, an ordinary read-only `codex.command_exec` request failed before launching Git with:

```text
windows sandbox: orchestrator_helper_launch_failed
setup refresh failed to launch helper
helper=codex-windows-sandbox-setup.exe
error=program not found
```

The same failure occurred with `access=readOnly` and `access=inherit`; merely increasing `timeoutMs` to 30000 did not repair it. `codex.read_many` continued returning source bytes, so this was not evidence of complete MCP/tunnel unavailability. This is distinct from Research 580's slow round-trip with too-short command budgets.

The owner executed a read-only Windows process/filesystem inventory. It found an active desktop Codex executable in generation `2e5e00daee91c61d` with neither the Windows sandbox helper nor the command runner alongside it, whereas generation `e78bad9887fa50cf` had both adjacent executables. An npm-managed Codex executable was also active; its package contained both helpers under `codex-resources`, rather than next to the main binary. The incomplete `2e5e...` generation is the directly relevant candidate for the failure, but exact process-to-failed-request correlation was not instrumented.

Validation 127 previously reproduced this **exact error text** when a live Codex installation generation lacked the helper/runner and a second complete generation existed. That investigation recovered read-only command execution after a bounded managed Codexless restart. The current evidence justified that same limited intervention; it did not justify copying executables between generations, relaxing sandbox isolation, changing PATH or updating/downgrading Codex.

## Managed restart and truthful result

One `codex.runtime_maintenance(action=restart_codexless)` operation was submitted with stable request ID:

```text
requestId   r580.sandbox-helper-generation-recovery.20261017.01
operationId rm_826e855394f33ae6d3b50bc8ae097cc8
initial    armed
```

The MCP connection was briefly unavailable, then the same tool surface resumed responding to `codex.read_many`. A later `codex.runtime_maintenance(action=status)` call returned a **failed operation record** (the tool wrapper surfaced it as an error):

```text
status            failed
errorCode         RUNTIME_STARTUP_TIMEOUT
recoveryAttempted false
recoverySucceeded null
```

This is **not a successful managed-restart receipt**. The restart was not submitted again and no runtime release or configuration mutation was attempted. The record does not establish why the maintenance startup check timed out or whether an internal retry/independent startup event occurred before reconnection.

## Post-reconnection functional verification

After the failed maintenance record, the same registered `ads-public` workspace and model-free `codex.command_exec` surface succeeded with `access=readOnly, timeoutMs=30000` in four distinct calls:

1. `git rev-parse HEAD`: exit 0, exact `de7065f9922920b58419564a700a5d6a64e85086`.
2. `cmd.exe /c echo CODEX_WINDOWS_HELPER_POST_RESTART_OK`: exit 0, expected marker.
3. `git status --short --branch`: exit 0, synchronized `v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume`, no changed paths.
4. Read-only `Get-Process -Name codex` via PowerShell: exit 0, active `e78bad9887fa50cf\codex.exe` plus npm Codex executable; the formerly reported incomplete `2e5e...` generation was not present in that process listing.

This matches the **functional outcome** observed in Validation 127: new command execution works after live Codex switches away from the incomplete generation. The postflight process inventory does not independently certify all future helper-resolution conditions, all runtime maintenance health checks or permanent immunity to generation changes.

## Operational disposition and recurrence trigger

- **Current observed command-execution state:** FUNCTIONALLY_RECOVERED with four successful independent read-only postflight calls.
- **Managed restart state:** FAILED_STARTUP_TIMEOUT according to durable receipt. Do not relabel this PASS. Investigate a startup-supervisor deadline/lifecycle issue only if it recurs or prevents ordinary use; correlate actual local runtime logs and subsequent service state before further repair.
- **Action taken:** exactly one bounded Codexless-only restart. Managed tunnel left running by contract. No helper copying, Codex installation changes, release publication, permission/trust broadening, Git mutation for diagnosis or runtime configuration edits.
- **Future same symptom:** recheck actual active Codex process generation and helper/runner co-location, consult Validation 127, distinguish working read tools from failing command execution, and use bounded maintenance only when justified. Never infer a successful maintenance operation merely from successful postflight calls or blindly repeat a failed restart.
- **Project:** R0-P03 fresh task-author preparation may resume under existing scientific admission controls; no task author, gold, arm, holdout or scoring was launched in this recovery, and Checkpoint 898/routing remain unchanged.

```text
PRE_RESTART_COMMAND_EXEC=WINDOWS_HELPER_NOT_FOUND
PRE_RESTART_ACTIVE_INCOMPLETE_GENERATION=2e5e00daee91c61d
PRE_RESTART_COMPLETE_GENERATION=e78bad9887fa50cf
RUNTIME_MAINTENANCE_REQUESTS=1
RUNTIME_MAINTENANCE_STATUS=FAILED_STARTUP_TIMEOUT
BRIDGE_READ_MANY_POST_RESTART=PASS
COMMAND_EXEC_POST_RESTART=4_OF_4_READ_ONLY_PASS
POST_RESTART_ACTIVE_COMPLETE_GENERATION=e78bad9887fa50cf
ADS_GIT_POST_RESTART_HEAD=de7065f9922920b58419564a700a5d6a64e85086
ADS_GIT_POST_RESTART_TRACKED_TREE=CLEAN_SYNCHRONIZED
R0_P03_SCORE=NOT_RUN
CHECKPOINT=898_UNCHANGED
```
