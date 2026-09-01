# Local Execution

**Status:** Current local-execution navigation  
**Last reviewed:** 2026-09-01

This directory contains durable ADS evidence and operational guidance for the bounded local-execution bridge.

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

A healthy HTTP process alone is not sufficient evidence that the accepted ADS authority configuration was loaded. Authority must be verified after restart before any mutation experiment.

Do not reconstruct these commands or authority inputs from prior chat memory when the repository procedures are available.

Exact secrets and private operational identifiers are intentionally excluded from the public repository and remain `RESOLVED_PRIVATE` in the accepted private/local continuity layer.

## Validation evidence

`docs/local_execution/validation/` contains chronological evidence for the Codexless/Secure MCP Tunnel/ChatGPT local-execution investigation.

Validation records preserve what was tested and observed. They do not replace the evergreen startup/recovery procedures, and historical validation commands should not automatically be treated as the current operational method.

Current live interpretation and the next legitimate mutation remain owned by:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
```

The public ADS repository remains the sole project-development authority.
