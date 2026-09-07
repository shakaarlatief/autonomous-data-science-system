# Validation 126: Native Codex Remote and Accepted Phone Split Qualified

**Date:** 2026-09-07
**Status:** PASS / OFFICIAL PRODUCT REUSE + LIVE WINDOWS/IPHONE REMOTE CONTINUITY QUALIFIED
**Research:** Research 122
**Scope:** Verify that native OpenAI Codex Remote satisfies the user-facing cross-device Codex requirement, while mobile web remains the accepted ADS connector surface, so custom direct ChatGPT-to-Codex mobile orchestration can be demoted from the core architecture.

## 1. Official product refresh

Current official OpenAI documentation establishes:

```text
Codex Remote GA
    all ChatGPT plans
    mobile app can start or continue work on a connected Mac or Windows host
    mobile can review progress and approve actions
    authenticated one-to-one QR host/device pairing

ChatGPT Work/Codex mobile boundary
    Codex is not selectable as an ordinary web/mobile mode
    supported desktop Codex chats are available from the Remote tab in the native mobile app
    those chats remain separate from ordinary ChatGPT web/mobile history

Developer MCP apps
    MCP apps are web-only
    native mobile is not a supported MCP-app surface
```

Official references checked on 2026-09-07:

```text
OpenAI Help: ChatGPT Release Notes, June 25 2026 Codex Remote GA
https://help.openai.com/en/articles/6825453

OpenAI Help: ChatGPT Work and Codex
https://help.openai.com/en/articles/20001275

OpenAI Help: Developer mode and MCP apps in ChatGPT
https://help.openai.com/en/articles/12584461

OpenAI: Work with Codex from anywhere
https://openai.com/index/work-with-codex-from-anywhere/
```

The June 25 release evidence is important because the earlier May announcement still said Windows phone-to-Codex support was coming soon. Research 122's reuse decision must follow the newer generally available Windows Remote state.

## 2. Pairing evidence

The Windows ChatGPT desktop settings showed:

```text
Remote / Connections enabled
paired iPhone present
connection allowed
```

The project owner paired the iPhone through the native ChatGPT Remote setup before the execution test.

## 3. Manual Codex task from Windows

A read-only task was started manually in the Windows Codex experience. It read only `docs/current_routing.json` and returned:

```text
current_checkpoint: 367
current_boundary: device-access-mobile-web-resolved-task-recovery-next
CODEX_REMOTE_WINDOWS_IPHONE_TEST_COMPLETE
```

No Git mutation, package installation, network work or file modification was requested.

## 4. Phone Remote continuity

The same supported desktop Codex thread appeared in the native ChatGPT app on iPhone.

Phone evidence showed:

```text
same repository/thread visible
original Windows-started prompt visible
original result visible
follow-up composer available
```

The user sent `Do it again` from the phone. A second Codex turn ran for approximately eight seconds and returned the same marker/result. The phone therefore did not merely mirror a completed thread; it successfully continued active work on the connected Windows host.

## 5. Visible desktop app/window closure

Immediately after the initial Windows prompt, the project owner closed the visible desktop app/window to test whether the phone remained usable. The phone continued to display the thread and successfully launched the second turn.

This supports the precise claim:

```text
visible Windows desktop UI need not remain open
```

It does not support the stronger claim that the paired Windows host or every ChatGPT/Codex background process may be terminated. Remote still depends on a connected host for local repository/shell execution.

## 6. Return-to-desktop continuity

After reopening the Windows desktop app, the same Codex thread displayed both turns:

```text
turn 1  started from Windows
turn 2  started from iPhone Remote
```

Both returned the same routing values and completion marker. No custom ADS rebind/archive/resume mechanism was involved.

## 7. Relation to ADS mobile-web qualification

Validation 125 already established:

```text
native ChatGPT app + ADS MCP invocation
    connector/tool discovery succeeds
    invocation receives 401 tunnel_active_organization_required

normal phone browser + ADS MCP invocation
    connector/tool discovery succeeds
    codex.account_preflight succeeds
    local tunnel forwards the MCP request
```

Combined with this validation, the accepted phone architecture is now:

```text
native app  -> Codex Remote
mobile web  -> ADS connector/tunnel
```

This split preserves current OpenAI product boundaries instead of trying to force unsupported native-mobile MCP behavior.

## 8. User workflow decision

The project owner explicitly stated that direct ChatGPT-to-Codex invocation is not necessary if ChatGPT can provide a precise prompt for manual paste into Codex. The orchestration benefit is convenience, not a correctness requirement.

Accepted development workflow:

```text
ChatGPT/ADS prepares prompt
-> user pastes into Codex
-> Codex executes locally
-> native Remote can supervise from phone
-> result is pasted back into ChatGPT/ADS when needed
```

Therefore direct Codexless agent dispatch, custom cross-device approval cards and custom Ready-in-Chat handoff are optional convenience layers. They no longer block core ADS progress.

## 9. Research disposition

Research 122 is complete for its accepted practical goals:

```text
runtime self-maintenance          PASS
secure phone ADS access          PASS via mobile web
phone Codex supervision          PASS via native Remote
manual prompt/result bridge      ACCEPTED
native-app ADS MCP               current product limitation, monitor only
```

AB-006/AB-007 are not falsely claimed technically complete in their original custom-orchestration formulations. They are explicitly deferred because their user-facing need is now satisfied by supported Remote plus manual prompt transfer.

The correct next stage is to resume Research 113's broader upstream survey and continue reuse-first comparison before additional Codexless architecture work.

```text
NATIVE_CODEX_REMOTE_WINDOWS_IPHONE=PASS
PHONE_ADS_MOBILE_WEB=PASS
CUSTOM_CODEX_MOBILE_ORCHESTRATION_CORE_REQUIREMENT=false
RESEARCH122=CLOSED
NEXT=RESEARCH113_RESUME
```