# Codexless local install and doctor validation

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `LOCAL_CORE_READY_TUNNEL_NEXT`

## Evaluated build

The first ADS Codexless evaluation installed the exact previously reviewed source revision:

```text
Codexless version   0.1.1-preview.5
source commit       ae9ee9201431a1241786ca938cb67f2e1b017f2b
runtime mode        existing / existing-only explicit
```

The installer completed successfully and reported that it did not change PATH, service, Browser, or Tunnel settings.

## First doctor result

The first project-scoped doctor run failed closed because the ADS repository had not yet been explicitly trusted by the local Codex authority layer.

Observed blocker:

```text
Codex has no explicitly trusted project/root covering the ADS repository cwd.
```

No Codex model turn was started. This failure was treated as desirable evidence that Codexless did not silently widen local authority.

## Explicit trust boundary

Trust was then granted through Codex's own project trust flow for the ADS Git repository root only. No broader parent filesystem root was selected as the intended authority boundary.

This project trust permits Codex to treat the repository as an authorized project root while the existing Codex sandbox and approval policy remain the permission ceiling.

## Successful doctor result

The subsequent Codexless doctor run completed `OK`.

```text
platform                   PASS / Windows
Node                       PASS / v24.19.0
public surface             PASS / 42 tools
MCP dependencies           PASS
runtime routing policy     PASS / existing-only explicit
Codex executable           PASS / codex-cli 0.151.0
Codex contract gate        PASS
Codex App Server           PASS / initialize succeeded
project authority          PASS
core health                ok
optional dependency health ok
actual project profile     :read-only
local permission ceiling   :workspace
authority source           codex-quiet-profile-resolver
Codex model turn started   no
Tunnel                     not checked yet
```

The distinction between actual project profile and local ceiling is important:

```text
read-only operations are currently downscoped to :read-only
explicit project writes may inherit at most the existing local :workspace ceiling
Codexless cannot silently select stronger authority than the local Codex ceiling
```

## Browser status

Browser Reader remained unavailable during this validation. This is non-blocking because browser integration is deliberately deferred from the first ADS Codexless evaluation.

## Boundary preserved

```text
Codexless local installation      COMPLETE
project authority validation      COMPLETE / PASS
core local doctor                 COMPLETE / OK
secure tunnel                     NOT YET CONFIGURED
ChatGPT custom Codexless app      NOT YET CONNECTED
read-only ChatGPT smoke test      NOT YET RUN
controlled disposable write test NOT YET RUN
Source Vault ingestion            NOT STARTED
```

The next bounded action is to start and verify Codexless's loopback-only HTTP MCP service, then provision and validate the Secure MCP Tunnel transport before connecting the custom app in ChatGPT.
