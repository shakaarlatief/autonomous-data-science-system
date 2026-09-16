# Checkpoint 531: Current Browser Plugin Compatibility Live Qualified, G009 Route Preserved

**Date:** 2026-09-16
**Status:** BROWSER COMPATIBILITY LIVE QUALIFIED / EXISTING-TAB CLAIMS FAIL-CLOSED / G009 REMAINS NEXT
**Checkpoint class:** LOCAL_EXECUTION / RUNTIME_SUPPORT / VALIDATION
**Project stage:** Candidate 01 W0 implementation with bounded runtime-support side repair
**Scope:** Preserve the guarded live repair of current Codex Browser/Chrome plugin discovery and exact runtime binding without changing the project-knowledge implementation route or operational authority.
**Authority:** Validation 207 is the detailed execution evidence. Research 117 and Research 118 remain the governing Browser/document architecture evidence. Specification 028 and Research 179 remain governing for the project-knowledge W0 program.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-25
**Conversation title:** 25 - Identity Transition Semantics and G006 Repair
**Primary collaborator:** ChatGPT

The Browser side investigation was reconstructed from current public/private repository evidence rather than blindly copying a historical candidate. Live `chrome_skill_unavailable` was confirmed as Codexless adapter drift against the maintained bundled Chrome/Browser pair. The repair now uses current installed-plugin discovery, exact same-build validation, trusted-cache realpath containment, manifest checks, independent Browser client/service byte hashes and explicit restart-on-drift semantics while retaining the historical Skill route only as a compatibility fallback.

Later Research 118 safety findings were carried forward. Current model-free existing-tab operations are not considered safe merely because discovery works: every existing-tab claim path is guarded before `claimTab()`, and direct new-tab creation is also guarded when the upstream lifecycle cannot provide a provable explicit finalization/release path.

The guarded release progression itself exposed and safely contained two integration defects before final acceptance:

```text
v1  browser-current-plugin-compat-v1
    source aa1897b3cabf62a2e5f3ab21baddd5bfb33b2fb5
    activation FAILED: RUNTIME_REPLACEMENT_CONTRACT_MISMATCH
    automatic recovery PASS

v2  browser-current-plugin-compat-v2
    source c28b12ade8a4aa93c0a85966c2bd87849e841ba5
    preview.46 activation PASS
    live status exposed public-mode compatibility-binding gap

v3  browser-current-plugin-compat-v3
    source d49ebfd024438d4ddf0eb7a86a07d7ab11800137
    preview.47 activation PASS
    postactivation verification PASS / mismatchCount=0
```

The final active runtime contract is:

```text
version        0.1.1-preview.47-browser-current-plugin-compat-public
surfaceVersion codexless-public-preview-v2
toolCount      172
manifest       4c8c5823b23b7112cedffa8623284ff9dce6201969d741e174b427cf32bc537c
focused Browser tests 13 / 13 PASS
```

Live qualification then established:

```text
codex.browser_status      PASS / Chrome + node_repl healthy
codex.browser_tabs        PASS / 5 existing tabs enumerated
codex.browser_screenshot  FAIL-CLOSED before claim
                          BROWSER_EXISTING_TAB_RELEASE_UNAVAILABLE
post-failure tabs         PASS / same 5 tabs remain visible
```

No PDF upload, existing-tab claim, screenshot capture, page mutation, Browser-plugin mutation, Chrome-extension mutation, trust/permission widening or private cleanup workaround occurred.

The preserved Browser upload mechanism remains potentially useful once a supported claim/release lifecycle exists, but Validation 207 does not promote it to a live-qualified PDF transport. The already-qualified direct PDF/resource/text/render/hybrid architecture remains the preferred document-access route.

This checkpoint is a bounded runtime-support checkpoint only. It does not advance or reinterpret Candidate 01's W0 semantic gates. The project-development route remains exactly:

```text
PKA-G001..PKA-G008   PASS
PKA-G009..PKA-G017   PENDING
next W0 task          PKA-G009 derived-view framework
W1                    NOT STARTED
operational authority current continuity architecture
authority switch      NOT ALLOWED
```

```text
CHECKPOINT531=BROWSER_CURRENT_PLUGIN_COMPATIBILITY_LIVE_QUALIFIED
VALIDATION207=PASS
RUNTIME_VERSION=0.1.1-preview.47-browser-current-plugin-compat-public
BROWSER_STATUS=PASS
BROWSER_TABS=PASS
EXISTING_TAB_CLAIM_ACTIONS=FAIL_CLOSED_UNTIL_SUPPORTED_RELEASE_LIFECYCLE
PDF_BROWSER_UPLOAD=NOT_PERFORMED
NEXT=PKA_G009_DERIVED_VIEW_FRAMEWORK
AUTHORITY_SWITCH_ALLOWED=false
```
