# Codexless prerequisite preflight

**Date:** 2026-08-31  
**Research:** `docs/research/098_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `PREREQUISITES_READY_CONNECTION_PATH_NEXT`

## Observed local prerequisite state

The bounded real-machine preflight completed before any Codexless installation or Source Vault ingestion.

```text
Windows architecture        x64
Node.js                     24.19.0
npm                         11.17.0
Codex CLI                   0.151.0
Codex authentication        ChatGPT
Codex doctor                21 ok / 1 idle / 2 notes / 2 warnings / 0 failures
Git repository detected     yes
active ADS branch           v1-source-vault-bootstrap-resume
working tree                clean at preflight
Codex sandbox               restricted filesystem + restricted network
Codex approval policy       OnRequest
Codex connectivity          healthy
Codex desktop application   installed; not required for bridge evaluation
```

The Codex runtime resolved to the native Windows executable behind the npm installation, satisfying the Codexless requirement for a directly launchable Codex runtime rather than relying only on an npm shell shim.

## Doctor warnings

The two doctor warnings were:

```text
Microsoft Defender Codex exclusions not verified
worktree is not located on a Windows Dev Drive
```

Neither warning is classified as a functional blocker for the Codexless evaluation. No Defender exclusion or Dev Drive migration is authorized merely to silence these warnings. If a later bridge or Codex operation is actually blocked or materially degraded, the specific cause should be investigated before changing system security or storage configuration.

## Boundaries preserved

```text
Codexless installed         no
secure tunnel configured    no
ChatGPT custom app linked   no
browser integration         deferred
Source Vault ingestion      not started
```

The next bounded action is to determine whether the active ChatGPT account/product surface can expose the required custom-app / MCP connection path and, if so, choose the secure tunnel route before installing Codexless.
