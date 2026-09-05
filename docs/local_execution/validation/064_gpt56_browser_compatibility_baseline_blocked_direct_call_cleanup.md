# Validation 064: GPT-5.6 Sol Browser Compatibility Baseline Qualified, Direct-Call Cleanup Blocked

**Date:** 2026-09-05
**Status:** PARTIAL PASS / DISCOVERY FIX QUALIFIED / DIRECT-CALL CLAIM CLEANUP UNSUPPORTED / NO PUBLICATION
**Research:** Research 117 with Research 113 cross-cutting Codexless integration implications

## Purpose

Preserve the completed GPT-5.6 Sol Browser compatibility investigation as an evidence-backed baseline before the independent Astra architecture challenge. The result is deliberately not classified as a successful Browser publication. The discovery problem was localized and a compatibility candidate was qualified, but the current Codexless direct-call execution primitive lacks a proven supported lifecycle for releasing a claimed existing user tab.

## Starting symptom and root cause

The live Codexless Browser status before this investigation reported:

```text
status      unavailable
reason      chrome_skill_unavailable
chromeSkill missing
nodeRepl    unknown
```

The investigation found that this symptom was primarily Codexless adapter drift. The existing adapter required the retired `chrome:control-chrome` Skill projection, while current Codex `0.153.0` exposes the maintained Browser/Chrome bundles through installed plugin discovery and the supported `node_repl` Browser runtime.

The qualified candidate discovers one enabled, available, same-build `openai-bundled` Browser/Chrome pair, validates the selected manifests/files/cache containment, binds the current Browser client hash, and retains the legacy Skill route as a compatibility fallback. Explicit current-plugin disablement fails closed and cannot silently fall back to a stale legacy Skill.

## Independent qualification

ChatGPT independently reran the focused Browser compatibility suite from the preserved local-runtime candidate. Because the read-only sandbox could not create the test fixtures in the ordinary Windows user temp directory, the rerun used a temporary directory inside the authorized local-runtime workspace. The result was:

```text
tests  7
pass   7
fail   0
```

Syntax checks passed for the ten relevant JavaScript modules/scripts, and `git diff --check` passed with only the expected Windows line-ending warnings.

The preserved current-runtime probe uses supported App Server / maintained Browser mechanisms only. It starts no model turn, claims no real user tab, performs no page mutation, does not invoke `turn_ended`, reports selected Browser/Chrome provenance, and closes both short-lived contexts. The Codex Desktop host-state run reported the maintained Browser/Chrome build and extension backend reachable with healthy `node_repl`. ChatGPT's ordinary model-free command sandbox could not reproduce that exact host-state probe because it is intentionally isolated from the user's normal Codex state directory; this difference is preserved as an execution-context distinction rather than treated as contradictory evidence.

## Supported tab lifecycle found

Maintained Browser documentation and the installed Browser service establish the supported lifecycle for a genuine Codex turn:

```text
browser.user.claimTab(existing user tab)
    -> current Browser session controls the tab
    -> genuine Codex turn completes
    -> unmarked claimed user tab is released and left open
```

`markDeliverable()` and `markHandoff()` classify tabs that should survive the turn. They are not explicit release APIs.

The installed maintained API exposes claim/mark operations but no public `releaseTab`, `unclaimTab`, or equivalent explicit release method. The maintained Browser service records claimed tabs, listens to real turn completion, and detaches turn-owned tabs during that lifecycle.

## Why Codexless direct Browser calls remain blocked

The current Codexless Browser adapter uses a direct model-free `mcpServer/tool/call` path. It may create an ephemeral App Server thread, but it does not start a genuine Codex `turn/start -> turn/completed` lifecycle. Supplying synthetic session/turn metadata does not prove that the maintained Browser service will apply the same claim-release contract.

Therefore the following would be unsupported and were explicitly rejected:

```text
inventing turn-completion metadata and invoking turn_ended
treating markDeliverable/markHandoff as release
closing the user's tab merely to guarantee cleanup
assuming process/context teardown equals maintained Browser turn cleanup
calling undocumented/private Browser cleanup internals
```

The candidate correctly retains a fail-visible `turn-cleanup-unproven` classification for current-runtime existing-tab operations rather than claiming a safe release path that has not been proven.

Accepted classification:

```text
RESEARCH_117_BROWSER_COMPATIBILITY =
BLOCKED_NO_SUPPORTED_CODEXLESS_DIRECT_CALL_CLEANUP
```

## No live Browser mutation or publication

This investigation intentionally did not:

```text
publish the Browser candidate into the live Codexless installation
restart Codexless for this candidate
claim or mutate a real user tab
upload a PDF
change Chrome extension state
change native-host registry state
modify plugin caches/installations
broaden Machine Learning authority
commit or push the Browser candidate before independent review
```

The separate missing native-host registry binding remains an installation-integrity observation, but current maintained Browser/Chrome runtime reachability means reinstalling Browser is not required to explain or fix `chrome_skill_unavailable`.

## Local-runtime preservation

After independent review, the complete GPT-5.6 Sol baseline and its reproducible discovery probe were committed to the private local-runtime repository together with the narrow recurring Git-ACL repair helper and standing exact-recurrence authorization metadata.

```text
local-runtime commit
e45a5de7ddae7f8158445b4b71d9c5f70cab8a2c

message
Preserve GPT-5.6 Sol Browser baseline and ACL repair contract

runtime integrity
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS

push postflight
local HEAD == origin/main
postflightOk=true
retried=false
```

The Browser baseline remains implementation/research evidence, not accepted live runtime code.

## Recurring Git ACL repair and standing authorization

Before the local-runtime preservation commit, the known lifecycle-sensitive Windows `.git` ACL defect recurred. Read-only diagnosis showed exactly two explicit DENY ACEs for the currently active workspace-capability SID on the registered local-runtime `.git`, while the dedicated `.git` writable capability retained `Modify` on `.git` and `FETCH_HEAD`.

The project owner explicitly approved the narrow repair and additionally granted standing authorization for future recurrences of this exact guarded defect so repeated approval is not required. The authorization does not cover arbitrary ACL mutation.

The host-run guarded helper required the exact diagnosed recurrence, created an SDDL backup outside the repository, removed exactly the two matching explicit DENY ACEs, and verified the dedicated writable capability remained intact. Accepted host output:

```text
RECURRING_GIT_ACL_REPAIR=PASS
REMOVED_EXPLICIT_DENY=2
POST_GIT_DENY=0
POST_FETCH_DENY=0
DEDICATED_GIT_MODIFY=1
DEDICATED_FETCH_MODIFY=1
```

Future use remains conditioned on a fresh read-only diagnosis matching the same registered-repository / exact-recurrence guard contract. Any path, identity, rule-count, authority, or postcondition drift remains a stop condition and requires a new decision.

## Baseline disposition and next architecture step

GPT-5.6 Sol is now considered complete as a bounded Browser architecture baseline, not because Browser upload succeeded, but because it localized the obsolete discovery assumption, qualified the maintained discovery path, established the genuine-turn cleanup semantics, identified the unsupported direct-call lifecycle boundary, and stopped before an unsafe workaround.

The next step is the already-preserved AB-028 independent Astra review. Astra should actively search for supported solutions, including whether Browser work should use a genuine App Server turn/lifecycle, another supported Browser execution primitive, a public release contract, a new-tab/deliverable architecture that avoids claiming existing user tabs, or a different whole-PDF fallback entirely. The GPT-5.6 Sol design is evidence to challenge, not an answer Astra must inherit.
