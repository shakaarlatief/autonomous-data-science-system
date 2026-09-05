# Validation 063: Direct Codex Guard False Positive Corrected and Live-Qualified

**Date:** 2026-09-05
**Status:** PASS / FALSE POSITIVE REMOVED / DIRECT MODEL-CALL GUARD PRESERVED
**Research:** Research 113/117 cross-cutting Codexless execution architecture

This validation preserves a model-free routing defect discovered while creating ordinary project documentation after the native Auto-review qualification.

## Reproduction

A `codex.command_exec` PowerShell command attempted to create new Markdown files with `Set-Content`. The Markdown body contained ordinary prose such as `Codex App Server`, `Call Codex?`, and `native Codex Auto-review`. The command was rejected before execution with:

```text
FORMAL_CODEX_AGENT_REQUIRED
```

The files were confirmed absent afterward. The rejection did not prove that model-free file creation was forbidden. It localized a false positive in the direct-Codex invocation guard.

The guard's purpose is valid: model-free `command_exec` / process lanes must not be used to launch a formal Codex model/control invocation and bypass the visible `Call Codex?` flow. The defect was that PowerShell `-Command` source text was scanned too broadly for a standalone `codex` token, so quoted data and here-string document contents could be mistaken for executable syntax.

The Auto-review patch was not causal. The relevant live `mcp-server-factory.mjs` was byte-identical to the pre-Auto-review candidate at SHA-256:

```text
54FF0A63FA94FF2AC299C871E32763B6AB78D7AE95079C9F32B791C5D68EB1E7
```

## Narrow correction

A clean candidate was created from the exact current live source tree. Only `mcp-server-factory.mjs` differs from live. The PowerShell wrapper classifier now distinguishes executable command positions from quoted strings and PowerShell here-string bodies while retaining the existing direct Codex CLI guard.

Qualified candidate:

```text
candidate mcp-server-factory.mjs SHA-256
B14F0C71E414382190C71C0407581E35ADB4E69919359B44E22B85165AD38F59

focused regression SHA-256
C3545D145A6192AB12447321109744A6D2C97247235A53D070A07686FAC48879

FORMAL_CODEX_GUARD_FALSE_POSITIVE_REGRESSION=PASS
node --check = PASS
candidate source-tree diff count = 1
changed source file = mcp-server-factory.mjs
```

Focused regression cases:

```text
ordinary quoted prose mentioning Codex                    ALLOWED
quoted search patterns mentioning Codex CLI               ALLOWED
single-quoted PowerShell here-string containing Codex     ALLOWED
double-quoted PowerShell here-string containing Codex     ALLOWED
powershell -Command "codex exec ..."                      BLOCKED
CLI invocation after a statement separator                BLOCKED
PowerShell call-operator invocation                       BLOCKED
quoted codex.exe path invoked via call operator            BLOCKED
real CLI invocation after a here-string                   BLOCKED
direct codex exec                                         BLOCKED
direct codex --version                                    existing safe behavior preserved
```

## Guarded publication

The user ran the exact guarded publication helper from ordinary PowerShell. Accepted output:

```text
FORMAL_CODEX_GUARD_FALSE_POSITIVE_REGRESSION=PASS
FORMAL_AGENT_GUARD_FIX_PREFLIGHT=PASS
LIVE_HASH=54FF0A63FA94FF2AC299C871E32763B6AB78D7AE95079C9F32B791C5D68EB1E7
CANDIDATE_HASH=B14F0C71E414382190C71C0407581E35ADB4E69919359B44E22B85165AD38F59
REGRESSION_HASH=C3545D145A6192AB12447321109744A6D2C97247235A53D070A07686FAC48879
FORMAL_AGENT_GUARD_FIX_PUBLICATION=PASS
BACKUP_SHA256=54FF0A63FA94FF2AC299C871E32763B6AB78D7AE95079C9F32B791C5D68EB1E7
LIVE_HASH_AFTER=B14F0C71E414382190C71C0407581E35ADB4E69919359B44E22B85165AD38F59
RESTART_PERFORMED=false
```

Independent post-publication read confirmed the live file hash exactly matched the candidate.

After the controlled Codexless/tunnel restart:

```text
Codexless /healthz  ok=true
version             0.1.1-preview.14
surface             codexless-public-preview-v2
toolCount           56
tunnel /healthz     HTTP 200 live
tunnel /readyz      HTTP 200 ready
```

## Live two-sided qualification

Positive live probe:

```text
PowerShell here-string containing:
    Codex routine in-turn approvals
    Call Codex?
    Codex App Server

FALSE_POSITIVE_LIVE_PROBE=PASS
```

Negative live probe:

```text
powershell -NoProfile -Command "codex exec --help"
    -> FORMAL_CODEX_AGENT_REQUIRED
```

The negative probe used `--help`, so even if the guard had failed it would not intentionally start a model task. The guard rejected it before execution as required.

The original end-to-end use case was then re-tested model-free with an actual temporary new-file write. A PowerShell here-string containing Codex prose was written with `Set-Content`, read back, and removed in the same bounded command:

```text
MODEL_FREE_NEW_FILE_WITH_CODEX_PROSE=PASS
PROBE_RESIDUE=False
```

Accepted result:

```text
DIRECT_CODEX_GUARD_FALSE_POSITIVE_FIXED=PASS
DIRECT_WRAPPED_CODEX_MODEL_CONTROL_GUARD_PRESERVED=PASS
MODEL_FREE_NEW_FILE_WITH_CODEX_PROSE=PASS
```

This is a narrow classifier correction. It does not widen workspace authority, enable direct formal Codex model routing, alter the Call Profile, alter native Auto-review, or change the public MCP schema/tool count.
