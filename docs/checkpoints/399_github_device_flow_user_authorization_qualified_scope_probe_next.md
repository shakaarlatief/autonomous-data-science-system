# Checkpoint 399: GitHub Device Flow User Authorization Qualified, Scope Probe Next

**Date:** 2026-09-09
**Status:** PASS / LIVE USER AUTHORIZATION / PROTECTED TOKEN STORAGE / SCOPE PROBE NEXT
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve recovery from the interrupted device-flow bootstrap, correction of the GitHub App Client ID, successful live user authorization and protected token storage.
**Authority:** Validation 156 owns the detailed live evidence; Research 123 owns the active GitHub architecture and continuation boundary.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

The owner-supplied GitHub settings screenshot confirms `Enable Device Flow` is ON. The 404 blocker was instead localized to a transcription error in the non-secret Client ID previously preserved from manual UI evidence. GitHub's public App record for `codexless-runtime-bridge` supplied the corrected identifier, and direct device-code discrimination changed from HTTP 404 with the old value to HTTP 200 with the live value.

Runtime release `github-client-config-v4` activated `0.1.1-preview.27-github-client-id-correction` with 64 tools, one exact runtime dependency and zero postactivation mismatches. The preceding v3 activation attempt failed safely because its version contract was incomplete; Runtime Bridge recovered automatically before the corrected immutable v4 release was published.

Exactly one live corrected device authorization was then completed. The poll returned `authorized`, and follow-up metadata proves the protected store now contains a current non-expired authorization while no token value is exposed through the public tool surface.

```text
CHECKPOINT399=GITHUB_USER_AUTHORIZATION_QUALIFIED
DEVICE_FLOW_ENABLED=true
GITHUB_APP_ID=4881901
GITHUB_APP_CLIENT_ID=Iv23lirgmw82wV0SGTWn
GITHUB_APP_SLUG=codexless-runtime-bridge
GITHUB_APP_INSTALLED=true
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
LOCAL_PRIVATE_KEY_DELETION=CONFIRMED_BY_OWNER
CLIENT_SECRET_GENERATED=false
AUTHORIZED=true
STORED_AUTHORIZATION=true
PUBLIC_GITHUB_ACTIONS=0
NEXT=AUTHENTICATED_IDENTITY_INSTALLATION_SCOPE_AND_FIRST_READ_ONLY_GITHUB_ACTION_QUALIFICATION
```
