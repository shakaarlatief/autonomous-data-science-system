# Research 580: Runtime Bridge command-execution timeout retest and bounded recovery

**Date:** 2026-10-16
**Status:** MODEL_FREE_COMMAND_EXEC_RECOVERED_WITH_30_SECOND_CALL_DEADLINE / UNDERLYING_LATENCY_CAUSE_UNRESOLVED / NO_RUNTIME_CHANGE
**Scope:** Record a transient Runtime Bridge command/exec failure, the independently observed read/exec distinction, earlier incident relevance, and the successful bounded no-restart retest.
**Basis:** Research 430 (Codex App Server compatibility probe completed in 13.0–13.6 seconds and needed a longer outer RPC budget), Research 519 (uncertain results and concurrency trigger), Research 520 (exact-duplicate semantic Git coalescing repair), Validation 099 (managed tunnel/backend distinction), Research 579 published commit `1e575ac0509a3fefd4616a864b3f50d71cab1afd`.
**Provenance:** ChatGPT/chatgpt-39 live model-free Runtime Bridge reads and command tests, in direct response to the owner's request to diagnose and fix read-working/command-timeout behavior.
**Authority:** Operational observation and scoped invocation guidance only. Not a new Codexless software release, native App Server repair, tunnel repair, architectural target, scored R0-P03 result, checkpoint advancement, or license to retry uncertain Git mutations.

## Initial symptom and discrimination

Under the ordinary registered `ads-public` workspace, two `codex.command_exec` read-only Git invocations timed out:

| Call | Requested `timeoutMs` | Caller-visible result |
| --- | ---: | --- |
| `git rev-parse HEAD` | 12000 | `command/exec timed out after 17000ms` |
| `git status --short --branch` | 10000 | `command/exec timed out after 15000ms` |

At the same time, `codex.read_many` successfully returned `docs/current_routing.json` and its SHA-256, proving that the Runtime Bridge was connected and read authority remained functional. Thus the data does not support classifying the entire bridge/tunnel as offline. There was no reported `bridge concurrency limit reached (1)` in this incident and no reason to attribute it to the previously repaired long semantic-operation duplicate delivery of Research 520.

## Prior incident relevance, without unjustified root-cause equivalence

Research 430 separately measured native Codex App Server successful `command/exec` round trips at **13.030** and **13.593 seconds**. Its fault involved an independently too-short *outer compatibility probe RPC* timeout of 10 seconds, corrected in a managed release to 45 seconds while retaining the independent command budget of five seconds. The live October 16 failures occurred on **ordinary user-facing command/exec calls with explicit 10- or 12-second requested command timeouts**, so this record does **not** claim that the compatibility probe fix regressed or that the exact underlying 13-second latency mechanism is proven identical.

Historical Research 519/520 explain uncertainty and duplicate-delivery paths for long semantic operations. No corresponding evidence of admission saturation, active duplicate arrival, failed daemon/tunnel service or runtime release regression was collected here.

## Successful minimal recovery without configuration mutation

After reading the saved incident evidence, ChatGPT retried with an explicit **`timeoutMs: 30000`** and `access: readOnly`, keeping the same registered ADS working directory:

1. `cmd.exe /c echo CODEX_BRIDGE_READONLY_ECHO_OK` returned exit code 0 and the expected marker.
2. `git rev-parse HEAD` returned exit code 0 and exact published commit `1e575ac0509a3fefd4616a864b3f50d71cab1afd`.
3. `git status --short --branch` returned exit code 0, branch `v1-source-vault-bootstrap-resume` synchronized with origin and no changed paths. Model-side elapsed time approximately **13,257 ms**.
4. `cmd.exe /c echo SECOND_EXEC_OK` returned exit code 0 with expected marker. Model-side elapsed time approximately **12,853 ms**.

`codex.workspace_authority(action=show)` also succeeded read-only, showing the expected registered `ads-public` workspace. Both direct-command timing observations are compatible with the previous approximately 13-second startup/round-trip duration. They suggest that the immediately observed 10–12-second call budgets were insufficient to accommodate current normal invocation latency. They do **not** independently localize the latency within the Codex process, sandbox initialization, host transport or App Server.

## Bounded operational guidance

- For subsequent **model-free ordinary command/exec** calls experiencing this approximately 13-second behavior, use the supported explicit **`timeoutMs: 30000`**, and attribute success/failure to the returned exit/result rather than assuming timeout means infrastructure outage. This is a per-invocation recovery, **not a changed runtime default or latency fix**.
- Prefer read-only workspace and Git state checks to test availability. Do not use mutations to diagnose read-path problems.
- If read-only calls still time out with the larger supported bound, or fail with a new error, stop and collect the exact call budget, host receipt, command, profile, elapsed time and outcome. Only then consider a bounded native App Server/runtime lifecycle investigation or managed Codexless-only restart.
- Do not treat `Tools vernieuwen` (schema projection refresh) as a command/exec recovery mechanism. Do not restart Codexless or its tunnel unnecessarily, broaden sandbox/trust permissions, downgrade Codex or change managed runtime source.
- For semantic Git or other mutations, an uncertain timeout **must** be reconciled against exact authoritative state before any subsequent attempt; the 30-second read-only observation does not authorize blind mutation replay.
- Use pre-existing Research 430/519/520 records when future symptoms match, but do not collapse distinct timeouts, duplicate delivery, tunnel availability, process liveness and provider/tool behavior into one cause.

## Verified boundary

```text
READ_MANY_WORKS=true
WORKSPACE_AUTHORITY_SHOW_WORKS=true
COMMAND_EXEC_10_TO_12_SECOND_CALLS=TIMED_OUT
COMMAND_EXEC_30_SECOND_CALLS=4_SUCCESSFUL_READ_ONLY
OBSERVED_ELAPSED_MILLISECONDS=13257,12853
PUB_GIT_HEAD=1e575ac0509a3fefd4616a864b3f50d71cab1afd
PUB_GIT_WORKTREE_AT_READ=CLEAN_SYNCHRONIZED
IMMEDIATE_OPERATIONAL_WORKAROUND=TIMEOUTMS_30000
PERMANENT_RUNTIME_LATENCY_FIX=NOT_CLAIMED
RUNTIME_RESTART_OR_RELEASE=NOT_PERFORMED
TUNNEL_CONFIG_OR_SECURITY_CHANGE=NOT_PERFORMED
SCIENTIFIC_R0_P03_WORK=NOT_ADVANCED
CHECKPOINT=898_UNCHANGED
```
