# Validation 209: Windows Sandbox Managed-Runtime Recovery Qualified

**Date:** 2026-09-17
**Status:** QUALIFIED RECOVERY / CODEXLESS RESTORED / NO REPOSITORY OR ACL WIDENING
**Scope:** Preserve the exact failure localization and recovery sequence for a Codexless startup failure caused by Windows sandbox setup validation of a defective Desktop-managed `cua_node` runtime subtree.
**Authority:** Historical validation evidence and recovery qualification. The evergreen operational procedure is `docs/local_execution/OPERATIONS.md`.

## 1. Incident summary

Codexless stopped starting successfully and the Codex App Server reported:

```text
windows sandbox: helper_unknown_error: setup refresh had errors
```

The failure occurred during App Server command execution before normal Runtime Bridge work could resume. The public ADS repository itself was not implicated by the failure.

The recovery ultimately required moving one defective Desktop-managed runtime subtree entirely outside the directory scanned by sandbox setup. Once that subtree was no longer under `cua_node`, Codexless started normally and a fresh Runtime Bridge `codex.command_exec` succeeded.

```text
RECOVERY_RESULT=PASS
CODEXLESS_STARTUP=RESTORED
RUNTIME_BRIDGE_COMMAND_EXEC=VERIFIED
REPOSITORY_PERMISSION_WIDENING=NONE
ACL_REPAIR=NONE
REPOSITORY_MUTATION_CAUSED_BY_RECOVERY=NONE
```

## 2. Initial evidence

The sandbox log showed two materially different historical states.

Earlier healthy setup runs successfully invoked the Windows sandbox setup helper, processed the configured writable roots, and completed setup with no setup errors. A recurring warning about hiding `C:\Users\Default` returned Windows access denied, but command execution continued afterward. That warning therefore was not treated as the blocking cause.

Later failing setup runs localized the blocker to read/execute validation of a deep path inside a Desktop-managed runtime below the public-safe root:

```text
%LOCALAPPDATA%\OpenAI\Codex\runtimes\cua_node\<runtime-id>\...
```

The relevant failure class was:

```text
runtime read/execute validation failed
CreateFileW failed for <path>
setup refresh had errors
```

A separate short-lived `program not found` helper-launch symptom also appeared during the investigation, but later runs again found the absolute helper executable and returned to the runtime-validation failure. It was therefore not accepted as the current root cause.

## 3. Hypotheses ruled out before repair

The investigation deliberately avoided broad changes and tested several simpler explanations first.

Observed host evidence established:

```text
Windows long paths enabled
normal path existence = true
extended \\?\ path existence = true
parent runtime directory exists
DNS later resolves normally
Codex installation otherwise reports normal repository/runtime state
```

The npm Codex CLI was updated successfully from the older installed version to:

```text
codex-cli 0.154.0
```

The direct Windows sandbox was then tested with Codex Desktop closed.

```powershell
$cmd = Join-Path $env:WINDIR 'System32\cmd.exe'

codex -c 'windows.sandbox="unelevated"' sandbox -- `
    $cmd /d /c echo CODEX_UNELEVATED_OK

codex -c 'windows.sandbox="elevated"' sandbox -- `
    $cmd /d /c echo CODEX_ELEVATED_OK
```

Both tests passed:

```text
CODEX_UNELEVATED_OK
CODEX_ELEVATED_OK
```

This was decisive negative evidence against a general failure of either Windows sandbox backend in the updated ordinary CLI.

## 4. CLI versus Codexless runtime distinction

Despite both direct sandbox modes passing, launching Codexless still returned:

```text
windows sandbox: helper_unknown_error: setup refresh had errors
```

The important interpretation was that the direct npm CLI path and the Codexless/Codex App Server path were not necessarily executing against the same managed runtime generation.

At the time, diagnostic evidence showed an npm-managed Codex CLI and a separately installed Codex Desktop/App Server environment. The failure path continued to reference a Desktop-managed `cua_node` runtime even after the ordinary CLI update had made both direct sandbox probes healthy.

Therefore the investigation stopped treating a successful direct CLI probe as proof that every Desktop-managed runtime subtree was healthy.

## 5. First quarantine attempt and why it failed

The exact runtime subtree named by the failing sandbox log was preserved by renaming it in place from its original runtime ID to a `.bad-20260917` name.

That operation was reversible and confirmed:

```text
original path exists = false
renamed backup exists = true
```

However, Codexless still failed with the same sandbox setup error. Fresh log evidence then showed sandbox setup validating the renamed `.bad-20260917` subtree itself.

This established a key recovery fact:

```text
RENAMING_INSIDE_CUA_NODE_IS_NOT_QUARANTINE
```

The sandbox setup process scans runtime trees under `cua_node`; changing only the leaf directory name does not necessarily remove a defective subtree from validation.

## 6. Successful bounded recovery

With Codex Desktop and Codexless stopped, the preserved defective runtime was moved entirely outside the scanned `cua_node` directory into a separate quarantine area under the Codex local-data root.

The recovery used the public-safe directory relationship:

```text
from:
%LOCALAPPDATA%\OpenAI\Codex\runtimes\cua_node\<defective-runtime>.bad-20260917

to:
%LOCALAPPDATA%\OpenAI\Codex\runtime-quarantine\<defective-runtime>.bad-20260917
```

The subtree was moved, not deleted.

Post-move verification established:

```text
defective backup still inside cua_node = false
preserved quarantine copy exists        = true
other cua_node runtimes remain intact   = true
```

Codexless was then launched again without first opening Codex Desktop. It started successfully:

```text
Codexless public HTTP listening on http://127.0.0.1:7690/mcp; surface=codexless-public-preview-v2
```

After the managed tunnel was restarted, Runtime Bridge executed a fresh model-free command successfully:

```text
CODEXLESS_COMMAND_EXEC_OK
exitCode = 0
```

A later independent bridge health probe also returned:

```text
BRIDGE_STILL_HEALTHY
exitCode = 0
```

This closes the recovery qualification.

## 7. Non-blocking log lines observed after recovery

Several red/error-looking lines appeared after the blocking incident was repaired. They were classified separately instead of being conflated with the prior startup failure.

### Ordinary `/mcp` request with wrong media type

Observed:

```text
Unsupported Media Type: Content-Type must be application/json
```

Interpretation: an ordinary HTTP request reached the MCP endpoint without a valid MCP `application/json` request. The Codexless process remained healthy.

### One command-specific executable lookup failure

An attempted repository search used `rg.exe`, and App Server returned Windows error 2 / file not found for that executable. The same bridge immediately executed other commands successfully after switching to built-in Windows tooling.

Interpretation: one requested executable was not resolvable in that sandbox environment. This was not a recurrence of `helper_unknown_error` and did not imply general command execution failure.

### Background `AGENTS.md` discovery failures

Repeated App Server background lines reported failure while trying to find `AGENTS.md` documentation for the local environment. The ADS repository had no root `AGENTS.md`, while ordinary `command/exec` remained healthy.

Interpretation: background documentation-discovery noise, not evidence that Runtime Bridge execution had failed.

## 8. Recovery rules frozen from the incident

For a future recurrence of `helper_unknown_error` or `setup refresh had errors`:

```text
1. separate Codexless/tunnel health from direct Codex CLI health;
2. update/verify the ordinary Codex CLI when appropriate;
3. test both direct Windows sandbox modes with a trivial command;
4. inspect the fresh sandbox log for the exact current validation path;
5. do not infer that long paths, ACLs, Defender, networking, or the repository are at fault without matching evidence;
6. if the direct sandbox is healthy but Codexless still fails on one `cua_node` subtree, preserve that exact subtree and move it entirely outside the scanned `cua_node` directory;
7. do not merely rename the subtree inside `cua_node`;
8. retry Codexless before modifying any additional runtime;
9. prove recovery with a fresh Runtime Bridge `codex.command_exec`;
10. keep the quarantined subtree until the recovery is stable and later cleanup is separately justified.
```

The recovery does not authorize broad ACL mutation, generic `FullControl`, disabling sandboxing, Defender exclusions, deleting all Codex runtimes, or rewriting ADS repository state.

## 9. Relationship to evergreen operations

The reusable procedure and log interpretation have been incorporated into:

```text
docs/local_execution/OPERATIONS.md
```

The local-execution navigation surface also points to that recovery capability:

```text
docs/local_execution/README.md
```

This validation preserves the incident-specific evidence so a future collaborator can distinguish the proven recovery from generic Windows troubleshooting advice.

```text
VALIDATION_209=PASS
WINDOWS_SANDBOX_MANAGED_RUNTIME_RECOVERY=QUALIFIED
CODEXLESS_RUNTIME=RESTORED
RUNTIME_BRIDGE=VERIFIED
```
