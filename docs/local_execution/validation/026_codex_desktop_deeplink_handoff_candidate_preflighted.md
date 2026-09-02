# Codex Desktop deeplink handoff candidate preflighted

**Date:** 2026-09-02  
**Status:** `H6_CANDIDATE_PREPARED / PREFLIGHT_PASS / NOT YET ACTIVATED`  
**Scope:** Preserve the H6 candidate that exposes the canonical Codex Desktop thread deeplink on completed ADS formal Codex tasks while retaining the verified H4 release behavior.  
**Authority:** Pre-activation candidate evidence only. This record must not be read as proof that H6 is live.

## Candidate behavior

The private ignored candidate changes the public formal-agent projection so a real Codex thread identity is exposed as:

```text
threadId

desktopThreadUrl = codex://threads/<threadId>
```

The same values are preserved in terminal task snapshots so they survive task-card persistence/recovery.

Terminal portable/text receipts print the exact Desktop URI. The Rich Task Card includes an `Open in Codex Desktop` link and only renders it for a canonical `codex://threads/` URI.

The candidate also removes the earlier experimental `threadSource = "user"` override because Validation 023 falsified its visibility hypothesis.

## H4 preservation

The candidate retains:

```text
terminal result freeze
resource receipt before release
thread/unsubscribe
formal-agent App Server recycle after all known tasks are safely terminal/released
no App Server restart for read-only terminal status
explicit later ADS follow-up may resume
```

## Validation

```text
DESKTOP_DEEPLINK_REGRESSION=PASS
PROCESS_RELEASE_REGRESSION=PASS
node --check codex-agent-executor.mjs PASS
node --check agent-tools.mjs PASS
node --check agent-card-ui.mjs PASS
DESKTOP_DEEPLINK_ACTIVATION_PREFLIGHT=PASS
NO_FILES_MODIFIED=true
```

The prepared host activation is fail-closed:

```text
verify frozen live hashes
verify frozen candidate hashes
syntax-check all candidate files
create timestamped backup for every touched live file
replace exactly the three intended installed files
verify resulting hashes
syntax-check live files
restore every touched file if any step fails
```

## Current boundary

At preservation time:

```text
H4 live writer/process release       VERIFIED / ACTIVE
H6 candidate                         PREPARED / PREFLIGHTED
H6 live activation                   NOT PERFORMED
fresh post-H6 real Codex test        NOT PERFORMED
```

The next legitimate test is activation followed by one fresh minimal formal Codex turn through the normal visible consent path and direct verification that the returned terminal state exposes the exact thread deeplink.

Detailed synthesis: `docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md`.
