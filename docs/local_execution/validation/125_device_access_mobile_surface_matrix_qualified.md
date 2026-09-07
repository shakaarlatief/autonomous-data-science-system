# Validation 125: Device Access Mobile Surface Matrix Qualified

**Date:** 2026-09-07
**Status:** PASS / NORMAL MOBILE WEB REACHES ADS / NATIVE APP FAILS AT ORGANIZATION-CONTEXT AUTHORIZATION
**Research:** Research 122
**Backlog item:** AB-001
**Scope:** Qualify phone access to the same laptop-hosted ADS connector/tunnel across native ChatGPT mobile and ordinary mobile-browser ChatGPT surfaces.

## 1. Test discipline

Both phone tests used fresh disposable ChatGPT conversations. The user performed the device interaction on the phone, then returned to the laptop conversation to report the exact result. Neither test performed a mutation. Each test was limited to one `codex.account_preflight` call.

The laptop-hosted tunnel/Codexless environment remained the same ADS topology under test.

## 2. Native mobile app

Fresh native ChatGPT app result:

```text
ADS connector exposed            yes
codex.account_preflight exposed  yes
single invocation succeeded      no
HTTP status                      401
error code                       tunnel_active_organization_required
```

Returned message:

```text
Access denied: this tunnel requires an active organization context.
Configure the organization ID or send the OpenAI-Organization header.
```

The failure is therefore after connector/tool discovery and is classified as organization-context authorization failure. It does not establish a dead tunnel or generic inability of the phone to contact ADS. No second call was made.

Research 122 already preserves current official product evidence that MCP apps are web-only and not available in native mobile ChatGPT. The observed native-app result is consistent with that constraint. No tunnel-authentication weakening is permitted as a workaround.

## 3. Ordinary mobile web

Fresh normal mobile-browser `chatgpt.com` result:

```text
ADS connector exposed            yes
codex.account_preflight exposed  yes
single invocation succeeded      yes
connector error                  none
MCP error                        none
transport error                  none
authorization error              none
organization-context error       none
client-surface error             none
```

Returned account/preflight state:

```text
overall status   ok
account status   ok
account present  true
auth mode        chatgpt
plan             plus
quota status     ok
usage status     ok
rate-limits      ok
cleanup status   ok
```

This proves the normal ChatGPT mobile web client can invoke the same ADS connector successfully from the phone.

## 4. Local tunnel evidence

The tunnel terminal displayed an approximately contemporaneous event:

```text
2026/09/07 18:18:47 INFO dispatcher forwarded command to MCP server ...
```

Earlier temporary DNS/control-plane poll failures had already recovered at 18:09:54 with `poller recovered; polling operational`. They are therefore not used to explain the successful 18:18 mobile-browser invocation or the separate structured native-app 401.

The Codexless foreground terminal displayed historical `Unsupported Media Type` and `Codexless public HTTP stopped (runtime-maintenance)` lines. Those are not evidence that current Codexless was down. Runtime-maintenance had moved the active replacement process into detached operation. Independent health from the laptop confirmed current Codexless remained healthy and the tunnel remained `live/ready`.

## 5. Continuity result

The evidence sequence is:

```text
laptop persistent conversation reaches ADS
-> fresh native mobile app discovers ADS but invocation receives 401 org-context failure
-> fresh ordinary mobile browser discovers ADS and account_preflight succeeds
-> local tunnel observes MCP command forwarding
-> laptop persistent conversation continues reaching ADS
```

Therefore device-independent connector reachability is proven through mobile web without changing the local runtime/tunnel architecture.

## 6. Acceptance decision

The preregistered Research 122 rule said desktop-site mode should be tested only if ordinary mobile web failed or materially lacked the relevant surface. It passed, so desktop-site mode is not needed.

AB-001 is resolved for connector reachability with this accepted path:

```text
normal phone browser -> chatgpt.com -> existing ADS connector
```

The native app remains a current client/product limitation and may be monitored for future product changes. It is not a reason to build a weaker authentication path.

Cross-device task/card/approval recovery is not inferred from connector reachability. It remains AB-006 and is the next test branch.

```text
ADS_NATIVE_MOBILE_REACHABILITY=AUTHORIZATION_CONTEXT_FAIL
ADS_MOBILE_BROWSER_REACHABILITY=PASS
AB001_CONNECTOR_REACHABILITY=RESOLVED
NEXT=AB006_CROSS_DEVICE_TASK_RECOVERY
```