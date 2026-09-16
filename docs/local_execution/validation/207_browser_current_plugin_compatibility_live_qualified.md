# Validation 207: Current Browser Plugin Compatibility Live Qualified

**Date:** 2026-09-16
**Status:** PASS / PREVIEW.47 ACTIVE / CURRENT PLUGIN DISCOVERY RESTORED / EXISTING-TAB CLAIMS FAIL-CLOSED
**Research:** Research 117 / Research 118 with Research 124 operational support

## 1. Trigger

The live Runtime Bridge Browser surface regressed to:

```text
status      unavailable
reason      chrome_skill_unavailable
chromeSkill missing
nodeRepl    unknown
```

User-side Chrome integration was already enabled. Independent model-free inspection confirmed that current Codex no longer requires the retired `chrome:control-chrome` projection as the primary Browser discovery mechanism. The maintained bundled pair was present as:

```text
chrome   26.908.40834
browser  26.908.40834
```

The current Chrome `browser-client.mjs` SHA-256 was:

```text
3fde147aa3779bfc112aa91cbab60fde99dc494f7de76c3766ffeb9b1dc7ccae
```

and the Browser service SHA-256 was:

```text
3b173421bc39677842ac1005be84c9c60c15e4c574598fc5b1324eac05b03ecd
```

The live Browser failure was therefore adapter drift, not an ordinary missing-extension condition.

## 2. Repair design

The repaired Runtime Bridge now prefers maintained installed-plugin discovery:

```text
plugin/installed
    -> exactly one enabled/available chrome@openai-bundled
    -> exactly one enabled/available browser@openai-bundled
    -> matching build required
    -> resolved version roots must remain inside bundled cache
    -> manifests validated
    -> browser client and browser service both hash-bound
    -> exact compatibility binding injected into isolated node_repl Browser context
```

The historical `chrome:control-chrome` route remains only as an older-runtime fallback. Explicit current-plugin disablement cannot silently fall back to a stale legacy Skill.

Research 118's later Browser findings were incorporated rather than blindly reviving the earlier seven-test candidate. The repair additionally rejects resolved plugin-version roots that escape the trusted bundled cache, independently binds Browser service bytes, and treats same-path client/service drift as a restart-required compatibility change.

## 3. Existing-tab lifecycle remains intentionally blocked

Current upstream Browser exposes claim and turn-lifecycle semantics but no public explicit release/finalize primitive for the Runtime Bridge's model-free direct-call path. Therefore restoring discovery must not silently reactivate existing-tab operations that claim a user tab without a provable release lifecycle.

Every current existing-tab `claimTab()` path is now preguarded before claim dispatch. The direct new-tab creation path is also preguarded. On the current finalize-absent Browser shape, claim-requiring operations fail visibly rather than forging turn completion, using private cleanup internals, treating markDeliverable/markHandoff as release, or closing a user tab as a cleanup substitute.

This keeps the Browser capability surface available for future lifecycle qualification while making current safety explicit.

## 4. Qualification sequence and two caught integration defects

### Candidate v1

Private source commit:

```text
aa1897b3cabf62a2e5f3ab21baddd5bfb33b2fb5
```

Release:

```text
browser-current-plugin-compat-v1
```

The Browser compatibility candidate itself passed focused and staged regressions and published successfully. Activation then failed with:

```text
RUNTIME_REPLACEMENT_CONTRACT_MISMATCH
```

The release declared preview.46 but did not replace `src/surface-contracts.mjs`, so the restarted runtime still advertised preview.45. The restart supervisor automatically recovered the previous preview.45 source/runtime state:

```text
recoveryAttempted true
recoverySucceeded true
```

No partial failed runtime remained active.

### Candidate v2

Private source commit:

```text
c28b12ade8a4aa93c0a85966c2bd87849e841ba5
```

Release:

```text
browser-current-plugin-compat-v2
```

V2 added the exact surface-contract transition. Prepare, publish, preactivation verify, restart activation and postactivation verify all succeeded, with zero file mismatches. The resulting preview.46 process exposed a second integration defect through the live status call:

```text
status      unavailable
reason      BROWSER_RUNTIME_COMPATIBILITY_UNAVAILABLE
chromeSkill ok
nodeRepl    ok
```

The maintained plugin pair was now visible, but the monolithic public runtime still bound Browser compatibility only when `mode === household`. Public preview mode therefore detected the pair after startup without having bound the compatibility descriptor during runtime construction.

### Candidate v3

Private source commit:

```text
d49ebfd024438d4ddf0eb7a86a07d7ab11800137
```

Release:

```text
browser-current-plugin-compat-v3
```

V3 binds the same maintained Browser compatibility path in both household and public-preview runtime modes, including both existing-runtime lanes, without changing the public tool count or widening Browser authority. The target contract is:

```text
version        0.1.1-preview.47-browser-current-plugin-compat-public
surfaceVersion codexless-public-preview-v2
toolCount      172
manifest       4c8c5823b23b7112cedffa8623284ff9dce6201969d741e174b427cf32bc537c
```

The focused Browser suite is now:

```text
13 / 13 PASS
```

It covers maintained pair selection, exact bundle/manifests/files, path escape rejection, independent client/service hashing, service-drift restart detection, lifecycle preguards, legacy fallback, public status, explicit-disable fail-closed behavior, maintained node_repl inventory, and public runtime compatibility binding.

Staged/public regressions preserved the 172-tool public surface. Guarded preparation, publication and preactivation verification passed. Controlled restart activation succeeded without recovery. Postactivation verification passed with zero mismatches.

## 5. Live Browser qualification

After preview.47 activation:

```text
codex.browser_status
    status      ok
    chromeSkill ok
    nodeRepl    ok
    connected   Chrome extension backend
```

`codex.browser_tabs` then successfully enumerated five existing user-visible Chrome tabs using opaque `tabRef` values. This is the first live proof in this repair sequence that the Runtime Bridge recognizes and reaches the current maintained Browser/Chrome integration rather than stopping on the retired Skill projection.

The next interaction deliberately tested the fail-closed claim boundary against the already-open ChatGPT ADS tab:

```text
codex.browser_screenshot
    -> BROWSER_EXISTING_TAB_RELEASE_UNAVAILABLE
```

The operation was rejected before claim dispatch because the current upstream lifecycle does not expose a release mechanism that this model-free path can prove safe. A second `codex.browser_tabs` call still returned the same five open tabs. No screenshot was captured and no existing user tab was claimed or mutated by that qualification.

## 6. File-upload consequence

The existing authority-bounded Browser upload architecture remains preserved:

```text
prepare_upload
    -> canonical trusted-workspace path
    -> byte length + SHA-256 binding
    -> exact semantic upload target

upload
    -> revalidate source and target
    -> official Chrome filechooser/setFiles
    -> no arbitrary execution-time path
```

This repair restores the compatibility substrate needed to reach that architecture, but it does not falsely claim an end-to-end PDF-to-ChatGPT Browser upload. Uploading through an existing user tab still depends on solving the same supported claim/release lifecycle. No PDF upload was performed in Validation 207.

## 7. Safety and preservation

This work did not modify `.codex/plugins`, bundled OpenAI Browser/Chrome bytes, Chrome extension files, native-host registry state, trust roots, permissions, Browser private cleanup internals or public tool authority. The compatibility layer verifies upstream bytes rather than patching them.

The private runtime repository remained clean/synchronized after each guarded preservation commit. All private pushes passed `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`.

The ADS project-development route is unchanged by this bounded runtime repair. PKA-G001 through PKA-G008 remain PASS, PKA-G009 through PKA-G017 remain pending, W1 remains not started, current continuity remains operational authority and `authority_switch_allowed=false`.

## 8. Disposition

```text
VALIDATION207=PASS
RUNTIME_VERSION=0.1.1-preview.47-browser-current-plugin-compat-public
BROWSER_CURRENT_PLUGIN_DISCOVERY=LIVE_QUALIFIED
BROWSER_STATUS=PASS
BROWSER_TABS=PASS
EXISTING_TAB_SCREENSHOT=FAIL_CLOSED_BEFORE_CLAIM
EXISTING_TAB_RELEASE_LIFECYCLE=UNRESOLVED
BROWSER_UPLOAD_IMPLEMENTATION=PRESERVED_NOT_LIVE_QUALIFIED
PDF_BROWSER_UPLOAD=NOT_PERFORMED
PUBLIC_TOOL_COUNT=172
UPSTREAM_PLUGIN_MUTATION=NONE
AUTHORITY_WIDENING=NONE
NEXT_PROJECT_KNOWLEDGE_TASK=PKA_G009
```
