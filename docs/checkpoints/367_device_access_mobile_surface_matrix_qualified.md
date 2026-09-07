# Checkpoint 367: Device Access Mobile Surface Matrix Qualified

**Date:** 2026-09-07
**Status:** PASS / AB-001 CONNECTOR REACHABILITY RESOLVED VIA MOBILE WEB / NATIVE APP AUTHORIZATION-CONTEXT FAIL PRESERVED
**Checkpoint class:** DEVICE-SURFACE REACHABILITY QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance, lifecycle supervision, and device-independent access
**Scope:** Preserves the native ChatGPT mobile-app versus normal mobile-browser reachability matrix against the same running ADS tunnel/Codexless instance and decides the accepted phone access path.
**Authority:** Research 122 governs the architecture; Validation 125 owns detailed evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The project owner performed both phone tests in fresh disposable ChatGPT conversations while the laptop-hosted ADS runtime and tunnel remained available. Results were then reported back in the persistent laptop conversation for reconciliation.

## Native ChatGPT mobile app

The native app exposed both the `ADS Codexless Local Bridge` connector and `codex.account_preflight`, proving discovery/tool projection reached the mobile conversation. The single permitted tool invocation did not succeed. It returned HTTP 401 with:

```text
code     tunnel_active_organization_required
message  Access denied: this tunnel requires an active organization context.
         Configure the organization ID or send the OpenAI-Organization header.
```

Therefore the native result is not classified as a generic network/tunnel outage or inability to discover the connector. It is preserved specifically as an organization-context authorization failure at invocation time.

```text
native app connector discovery  PASS
native app tool discovery       PASS
native app invocation           FAIL
classification                  AUTHORIZATION-CONTEXT FAIL
```

This result is consistent with Research 122's previously preserved current product evidence that Developer Mode/MCP apps are web-only and not supported on native mobile clients. ADS must not weaken tunnel principal/organization validation to work around the client behavior.

## Normal ChatGPT mobile browser

The project owner then opened `chatgpt.com` in the phone's ordinary mobile browser view, not the native app and not desktop-site mode, and used a fresh conversation. The same connector and `codex.account_preflight` were exposed. The single call succeeded completely:

```text
overall status   ok
account status   ok
account present  true
auth mode        chatgpt
plan             plus
quota status     ok
usage status     ok
rate limits      ok
cleanup status   ok
```

No connector, MCP, transport, authorization, organization-context or client-surface error occurred.

Local tunnel evidence visible during that test independently showed a dispatcher event forwarding a command to the MCP server at approximately 18:18:47 local time, matching the successful browser invocation. The same laptop conversation subsequently continued to reach ADS successfully. This establishes the intended laptop -> phone browser -> laptop continuity on one running connector/tunnel path.

```text
mobile browser connector discovery   PASS
mobile browser tool discovery        PASS
mobile browser invocation            PASS
authorization                        PASS
transport                            PASS
local dispatcher forwarding          OBSERVED
laptop -> phone -> laptop continuity PASS
```

## Runtime/tunnel clarification

The visible PowerShell terminal had returned to a prompt because runtime-maintenance had stopped an older foreground Codexless process during prior semantic restart/rollback qualification. Independent machine health proved the current Codexless replacement was already running detached and healthy, so no manual `$CodexlessLauncher` invocation was missing or required for this test. The tunnel was also `live/ready`.

Desktop-site mobile-browser mode is skipped under the preregistered Research 122 matrix because the normal mobile web route already passed.

## AB-001 decision

AB-001 asks whether the authorized local ADS connector can be reached from another device. That objective is now satisfied on the phone through the normal ChatGPT web client while preserving the existing tunnel security model. The native mobile app remains a current product/client limitation with a specific organization-context authorization failure, not an ADS backend defect.

Accepted phone path:

```text
phone -> normal mobile browser -> chatgpt.com -> ADS developer MCP -> OpenAI tunnel -> local Codexless
```

AB-001 is resolved for the accepted connector-reachability scope. Cross-device persistence of already-started Codex tasks, cards, approvals and handoff state remains separate AB-006 work and becomes the next Research 122 discriminator.

```text
CHECKPOINT_367=DEVICE_ACCESS_MOBILE_SURFACE_MATRIX_QUALIFIED
AB001=RESOLVED_VIA_MOBILE_WEB
NATIVE_MOBILE_APP=AUTHORIZATION_CONTEXT_FAIL
MOBILE_BROWSER=PASS
DESKTOP_SITE_MODE=SKIPPED_NOT_NEEDED
NEXT=AB006_CROSS_DEVICE_TASK_RECOVERY
```