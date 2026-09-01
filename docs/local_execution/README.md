# Local Execution

**Status:** Current local-execution navigation  
**Last reviewed:** 2026-09-01

This directory contains durable ADS evidence, accepted bounded capability records, and operational guidance for the local-execution bridge.

## Operational procedure

Use:

```text
docs/local_execution/OPERATIONS.md
```

for the current public-safe procedure to:

```text
start / stop / restart Codexless HTTP
verify local Codexless health
start / stop / restart the OpenAI Secure MCP Tunnel
verify tunnel liveness/readiness
refresh the ChatGPT developer MCP app after a surface change
recover safely when the foreground terminal is lost
```

Before starting Codexless for ADS, also use:

```text
docs/local_execution/AUTHORITY_BOOTSTRAP.md
```

This is the canonical ADS-specific parent-shell/bootstrap procedure for restoring:

```text
CODEXLESS_PROFILE
CODEXLESS_CONFIG_OVERRIDES_FILE
CODEXLESS_DEFAULT_CWD
```

and verifying that `inherit` resolves to the accepted `ads-direct-git` authority with network enabled while `readOnly` still downscopes to `:read-only`.

For direct-lane Git mutation after relevant Codex/Codexless/sandbox lifecycle changes, also use:

```text
docs/local_execution/ACL_INTEGRITY_GATE.md
```

This is the canonical read-only Windows Git-metadata ACL gate for `.git` and `.git\FETCH_HEAD`. It exists because the workspace-capability DENY condition was observed to recur after later lifecycle activity even while `ads-direct-git` still reported `.git` as writable.

A healthy HTTP process and ready tunnel are not sufficient evidence that the accepted ADS Git authority path is mutation-ready. The authority bootstrap and, when applicable, ACL integrity gate must pass first.

Do not reconstruct these commands or authority inputs from prior chat memory when repository procedures are available.

Exact secrets, current capability identities, temporary ACL backup locations, and private operational identifiers are intentionally excluded from the public repository and remain `RESOLVED_PRIVATE` in the accepted private/local continuity layer.

## Accepted bounded Git synchronization

The current stable acceptance boundary for semantic strict-fast-forward synchronization is:

```text
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
```

It records the exact verified `codex.git_pull_ff_only` contract and explicitly excludes stronger Git authority such as commit, push, reset, rebase, checkout, merge commits, force behavior, or arbitrary Git execution.

## Validation evidence

`docs/local_execution/validation/` contains chronological evidence for the Codexless/Secure MCP Tunnel/ChatGPT local-execution investigation.

Validation records preserve what was tested and observed. They do not replace the evergreen operational procedures, and historical validation commands should not automatically be treated as the current operational method.

The latest successful strict-fast-forward evidence is:

```text
docs/local_execution/validation/021_semantic_git_pull_ff_only_verified_after_acl_repair.md
```

Current live interpretation and the next legitimate project action remain owned by:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
```

The public ADS repository remains the sole project-development authority.
