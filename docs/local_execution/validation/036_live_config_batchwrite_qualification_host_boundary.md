# Live config/batchWrite qualification host boundary

**Date:** 2026-09-03
**Status:** `PASS / INSTALLED 0.152.1 CONFIG BATCHWRITE QUALIFIED`
**Scope:** Preserve the attempted live qualification of the Research 116 supported Codex App Server `config/batchWrite` trust path for `C:\Projects_Data\autonomous-data-science-system-local-runtime`.
**Authority:** Local integration evidence. This record proves only the observed host/runtime boundaries in the tested ChatGPT + Codexless surface. It does not classify the Research 116 candidate itself as failed.

## Intended qualification

The approved qualification was intentionally narrow:

```text
read current App Server config
verify existing ADS root remains trusted
verify exact runtime repository real Git root and exact origin URL
write only projects."<runtime root>".trust_level = "trusted" through config/batchWrite
reload user config through the supported App Server request
read config back
verify runtime root trusted
verify ADS root still trusted
verify every unrelated config value unchanged
```

No raw Codex config-file/database mutation was permitted. No live Codexless installation edit, Git configuration mutation, commit, push, Source Vault mutation, or `.tmp` cleanup was permitted.

## Prepared qualification script

Candidate-local script:

```text
.ads-private/codexless/qualify-flexible-workspace-trust.mjs
```

The script imports the candidate App Server client and `writeTrustedProjectViaAppServer(...)`, validates the exact target repository and remote, computes deterministic before/after configuration hashes with only the exact target trust field excluded for the unrelated-config invariant, and prints:

```text
FLEXIBLE_AUTHORITY_TRUST_QUALIFICATION=PASS
```

only after all postconditions succeed.

`node --check` passed.

## Attempt 1: repository preflight blocked by sandbox Git identity

Running the script through current live `codex.command_exec(access=inherit)` reached the target Git preflight but Git rejected the sibling repository because the App Server sandbox identity did not own it:

```text
fatal: detected dubious ownership in repository at
'C:/Projects_Data/autonomous-data-science-system-local-runtime'
```

This occurred before App Server trust mutation.

The script was corrected to use only a per-process Git override:

```text
git -c safe.directory=<exact target root> ...
```

This does not write global/local Git configuration.

## Attempt 2: nested App Server launch blocked

With the repository preflight corrected, the script still could not run from inside `codex.command_exec` because the qualification needs an independent `codex app-server --stdio` client, while the command itself is already executing inside the existing App Server sandbox.

Observed terminal result:

```text
FLEXIBLE_AUTHORITY_TRUST_QUALIFICATION=FAIL
ERROR_CODE=UNCLASSIFIED
codex app-server exited: code=1 signal=null
```

No trust mutation was observed or claimed.

## Attempt 3: narrow formal Codex route blocked by outer safety layer

A minimal formal Codex task was prepared whose only purpose was to inspect and run the already-prepared qualification in normal Codex host context, with explicit prohibitions on raw config mutation, live Codexless edits, Git changes, commits/pushes, Source Vault changes, or any authority mutation other than the exact supported trust write.

The ChatGPT/OpenAI outer safety layer blocked the `agent_start` call before Codex started.

Therefore this route also produced no trust mutation.

## Host-terminal qualification result

The user then ran the prepared qualification from the normal Windows host terminal at the public ADS checkout. The first successful host-terminal run used the shell-resolved Codex `0.151.0` binary and established the exact trust mutation:

```text
FLEXIBLE_AUTHORITY_TRUST_QUALIFICATION=PASS
batchWriteAccepted: true
targetTrustBefore: null
targetTrustAfter: trusted
adsTrustBefore: trusted
adsTrustAfter: trusted
unrelatedConfigUnchanged: true
```

Observed configuration hashes were:

```text
beforeConfigSha256
    a85f1f70bd4ca69960641cfb86df6130c71e034b566358255653beb6b9a31d07

afterConfigSha256
    ca69ba6b2eee423acb8ae79e6146b2827f53052ff84d7228f3d756674fb5b87f

unrelatedConfigSha256
    a85f1f70bd4ca69960641cfb86df6130c71e034b566358255653beb6b9a31d07
```

The only intended semantic difference was therefore the exact target trust field:

```text
projects."C:\\Projects_Data\\autonomous-data-science-system-local-runtime".trust_level = "trusted"
```

No unrelated configuration value changed.

## Exact installed Codex 0.152.1 qualification

Because the live Codexless runtime itself reported Codex CLI `0.152.1`, the script was extended with an optional `CODEX_QUALIFY_BIN` override so the exact runtime binary could be qualified rather than inferring compatibility from `0.151.0`.

The user reran the same qualification against the exact live Codexless runtime binary. The second run returned:

```text
status: PASS
batchWriteAccepted: true
targetTrustBefore: trusted
targetTrustAfter: trusted
adsTrustBefore: trusted
adsTrustAfter: trusted
unrelatedConfigUnchanged: true
initializedVersion: ads_flexible_authority_qualification/0.152.1
FLEXIBLE_AUTHORITY_TRUST_QUALIFICATION=PASS
```

Because the target was already trusted, this second write was idempotent at the effective configuration level:

```text
beforeConfigSha256
    ca69ba6b2eee423acb8ae79e6146b2827f53052ff84d7228f3d756674fb5b87f

afterConfigSha256
    ca69ba6b2eee423acb8ae79e6146b2827f53052ff84d7228f3d756674fb5b87f

unrelatedConfigSha256
    a85f1f70bd4ca69960641cfb86df6130c71e034b566358255653beb6b9a31d07
```

A fresh model-free `codex.project_context` call against the runtime-repository cwd also succeeded through the live Codexless runtime and reported:

```text
cwd
    C:\Projects_Data\autonomous-data-science-system-local-runtime

runtimeWorkspaceRoots
    C:\Projects_Data\autonomous-data-science-system-local-runtime

activePermissionProfile
    ads-direct-git

cliVersion
    0.152.1
```

This independently proves that the live Codexless runtime reads and honors the newly established Codex project trust.

## Accepted conclusion

```text
Research 116 candidate tests                         PASS
candidate-over-live 51-tool staged registration      PASS
prepared qualification script syntax                 PASS
supported config/batchWrite on Codex 0.151.0          PASS
exact installed Codex 0.152.1 config/batchWrite       PASS
exact runtime repository trust read-back              PASS
existing ADS trust preserved                          PASS
unrelated Codex configuration preserved               PASS
raw config/database fallback                          NOT USED
Git config/remotes/branches/credentials               UNCHANGED
live Codexless installation                           UNCHANGED BY QUALIFICATION
Source Vault / .tmp                                   UNCHANGED
```

The Research 116 live trust-write compatibility blocker is closed. The next boundary is guarded activation/publication of the 51-tool flexible-authority Codexless candidate, followed by restart/tunnel/app refresh and fresh-chat discovery before the new workspace-registry surface is used for ordinary repository admission.
