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

Do not reconstruct those commands from prior chat memory when the runbook is available.

Exact secrets and private operational identifiers are intentionally excluded from the public repository and remain `RESOLVED_PRIVATE` in the accepted private/local continuity layer.

## Validation evidence

`docs/local_execution/validation/` contains chronological evidence for the Codexless/Secure MCP Tunnel/ChatGPT local-execution investigation.

Validation records preserve what was tested and observed. They do not replace the evergreen startup/recovery procedure in `OPERATIONS.md`, and historical validation commands should not automatically be treated as the current operational method.

Current live interpretation and the next legitimate mutation remain owned by:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
```

The public ADS repository remains the sole project-development authority.
