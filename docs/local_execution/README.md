# Local Execution

**Status:** Current local-execution navigation  
**Last reviewed:** 2026-09-02

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

## Cross-cutting investigation lessons

The broader methodological and diagnostic lessons extracted from the completed direct Git investigation are preserved in:

```text
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
```

That record is intentionally broader than Codexless operation. It preserves why ADS must distinguish a failed route from an impossible capability, localize failures by system layer, use targeted research before freezing stronger conclusions when evidence is ambiguous, design the smallest safe discriminating experiment, preserve negative evidence by layer, treat runtime bootstrap/lifecycle state as part of reproducibility, and keep successful capability claims bounded to the exact contract that was actually verified.

Use the detailed validation chronology when exact technical evidence is needed. Use the lessons synthesis when the question is what ADS should learn from the investigation and how those lessons should inform future cross-layer debugging and architecture work.

## Formal Codex thread handoff and Desktop integration

The post-Checkpoint-271 formal Codex thread investigation is preserved in:

```text
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/local_execution/validation/022_formal_codex_thread_persistence_and_desktop_visibility_baseline.md
docs/local_execution/validation/023_thread_source_user_visibility_hypothesis_falsified.md
docs/local_execution/validation/024_completed_codex_thread_writer_handoff_verified.md
docs/local_execution/validation/025_codex_desktop_catalog_reconciliation_trigger_isolated.md
docs/local_execution/validation/026_codex_desktop_deeplink_handoff_candidate_preflighted.md
```

The key accepted distinction is:

```text
Codex thread persistence
    !=
writer/process ownership
    !=
Codex Desktop sidebar catalog reconciliation
```

H4 post-completion writer/process release is live and empirically verified. The H6 canonical `codex://threads/<thread-id>` handoff candidate is prepared and preflighted but is not yet live at the current checkpoint.

Do not manipulate Codex Desktop private catalog/session databases to improve visibility. The deterministic supported handoff direction is the exact thread deeplink plus the verified release lifecycle.

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
