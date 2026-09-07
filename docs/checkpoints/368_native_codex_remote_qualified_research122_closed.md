# Checkpoint 368: Native Codex Remote Qualified and Research 122 Simplified

**Date:** 2026-09-07
**Status:** PASS / NATIVE CODEX REMOTE QUALIFIED / ADS PHONE ACCESS SPLIT ACCEPTED / RESEARCH 122 CLOSED
**Checkpoint class:** PRODUCT-REUSE AND RESEARCH-CLOSURE BOUNDARY
**Project stage:** Research 122 runtime self-maintenance, lifecycle supervision, and device-independent access
**Scope:** Qualifies the supported native Codex Remote workflow on Windows/iPhone, records the accepted split between Codex Remote and ADS mobile-web access, demotes custom ChatGPT-to-Codex cross-device orchestration from a core requirement, and closes Research 122.
**Authority:** Research 122 governs the accepted architecture; Validation 126 owns detailed product/live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

## 1. Current official product evidence refreshed

Official OpenAI evidence was rechecked before changing the ADS boundary.

Current product state:

```text
Codex Remote
    generally available on all ChatGPT plans
    supported connected Mac or Windows host
    ChatGPT mobile app can start/continue work, inspect progress and approve actions
    authenticated one-to-one QR pairing between mobile device and host

Codex on mobile/web
    Codex is not a selectable ordinary web/mobile experience
    supported desktop Codex chats are accessed from the Remote tab in the ChatGPT mobile app
    Remote Codex chats remain separate from ordinary ChatGPT mobile/web chat history

Developer MCP apps
    current OpenAI documentation says MCP apps are web-only and not available on mobile native clients
```

Primary official references:

```text
https://help.openai.com/en/articles/6825453
https://help.openai.com/en/articles/20001275
https://help.openai.com/en/articles/12584461
https://openai.com/index/work-with-codex-from-anywhere/
```

This refresh materially changes the reuse decision. ADS should not build a custom phone supervision layer for Codex when the supported product already provides that function.

## 2. Native Windows/iPhone Remote live qualification

The project owner paired the Windows ChatGPT/Codex desktop host with an iPhone through the native ChatGPT Remote setup.

A manual read-only Codex task was started from Windows with the explicit marker:

```text
CODEX_REMOTE_WINDOWS_IPHONE_TEST_COMPLETE
```

The same Codex thread appeared on the iPhone native ChatGPT Remote surface. The task returned:

```text
current_checkpoint: 367
current_boundary: device-access-mobile-web-resolved-task-recovery-next
CODEX_REMOTE_WINDOWS_IPHONE_TEST_COMPLETE
```

The project owner then sent a second message, `Do it again`, from the iPhone Remote thread. Codex executed the second turn on the Windows-hosted workspace and returned the same read-only result on the phone.

The visible desktop application/window had been closed after the initial desktop message. Remote execution still continued from the phone, which proves the visible desktop UI does not need to remain open. This is not evidence that every background host/service process can be terminated; the connected Windows host remained available and the Remote backend continued running.

When the desktop app was reopened, the same Codex thread contained both the original desktop-started turn and the phone-started follow-up turn. This establishes supported cross-device thread continuity without ADS owning a custom task/card/handoff protocol.

```text
Windows manual Codex task -> phone Remote visibility       PASS
phone follow-up -> Windows-hosted Codex execution          PASS
phone receives second result                               PASS
visible desktop UI may be closed                           PASS
reopened Windows app shows same thread and both turns      PASS
custom ADS orchestration required for this workflow        NO
```

## 3. Accepted phone architecture

Research 122 now adopts a deliberate two-surface phone workflow:

```text
A. ADS / local-machine tools

phone normal browser
    -> chatgpt.com
    -> ADS developer MCP connector
    -> OpenAI secure tunnel
    -> local Codexless / ADS tools

B. Codex coding work

phone native ChatGPT app
    -> Remote tab
    -> paired Windows Codex host
    -> local repository / shell / Codex execution
```

The project owner accepts manual prompt transfer between those surfaces when needed:

```text
ChatGPT mobile web + ADS
    -> ChatGPT prepares exact Codex prompt
    -> user copies prompt
    -> native ChatGPT app / Codex Remote
    -> Codex executes on Windows
    -> user copies relevant result
    -> mobile web ChatGPT + ADS continues
```

This is functionally complete for phone work today. The native app's ADS developer-MCP invocation remains a product/client limitation observed as HTTP 401 `tunnel_active_organization_required`, while normal mobile web is already live-qualified. ADS must not weaken organization/principal validation merely to collapse the two phone surfaces into one.

## 4. Direct ChatGPT-to-Codex orchestration is no longer core

The project owner explicitly accepts manual Codex prompt copy/paste. Therefore the following features are no longer required to progress the ADS core architecture:

```text
ChatGPT directly starting every Codex turn
custom cross-device Call Codex approval cards
custom Proceed-in-Chat / Desktop archive-rebind phone handoff
custom phone Codex progress viewer solely for remote supervision
```

Those mechanisms may remain as optional convenience/research work, but they must not block Source Vault, data-science execution, ADS connector evolution, or broader Research 113 architecture decisions.

The earlier custom Rich Card experiment still produced useful evidence that a laptop-created card could appear in the same ChatGPT conversation on mobile web and that a deliberate phone approval could start and complete the exact prepared task. That result is retained as implementation evidence, but native Codex Remote supersedes the need to make that custom path a core mobile architecture.

## 5. Backlog disposition

```text
AB-001  RESOLVED
    accepted ADS phone path = normal mobile browser + secure ADS tunnel
    native-app MCP support remains a product-monitoring item, not a blocker

AB-002  CLOSED
    semantic runtime publication/restart/rollback already production-qualified

AB-006  DEFERRED / OPTIONAL CONVENIENCE
    its original Codexless-task recovery guarantees are useful only if direct ADS-to-Codex
    orchestration is re-prioritized; supported Codex Remote now satisfies the user-facing
    cross-device Codex supervision requirement

AB-007  DEFERRED / OPTIONAL CONVENIENCE
    custom Rich Card supervision no longer blocks the accepted workflow

AB-017  REMAINS OPEN
    broader non-workspace host-authority taxonomy is larger than Research 122
```

## 6. Research 122 closure

Research 122 opened to remove two practical blockers:

```text
1. repeated manual installed-runtime publication/restart work
2. inability to work effectively from a phone
```

Both are now resolved for the accepted architecture:

```text
runtime maintenance
    semantic release + restart + rollback
    no ordinary-host install helper for normal future updates
    no manual Codexless/tunnel restart for normal Codexless maintenance

phone operation
    ADS tools via normal mobile web
    Codex supervision via native OpenAI Remote
    manual prompt/result transfer accepted where the two surfaces must cooperate
```

Research 122 is therefore closed. The broader Research 113 upstream ecosystem survey resumes as the active Level-2 research program. The product-reuse finding strengthens its original rule: prefer current upstream/native mechanisms over custom ADS infrastructure unless a concrete unmet requirement remains.

```text
CHECKPOINT_368=NATIVE_CODEX_REMOTE_QUALIFIED_RESEARCH122_CLOSED
RESEARCH122=CLOSED
AB001=RESOLVED
AB002=CLOSED
AB006=DEFERRED_OPTIONAL
AB007=DEFERRED_OPTIONAL
CODEX_REMOTE_WINDOWS_IPHONE=PASS
ADS_PHONE_WEB=PASS
NATIVE_APP_ADS_MCP=PRODUCT_LIMITATION_MONITOR
NEXT=RESUME_RESEARCH113_UPSTREAM_SURVEY
```