# Validation 154: GitHub App Registered, Private-Key Installation Gate Discovered

**Date:** 2026-09-09
**Status:** PASS / APP REGISTERED / INSTALLATION BLOCKED BY CURRENT GITHUB PRIVATE-KEY GATE
**Research:** Research 123

The owner successfully created the public GitHub App after Checkpoint 396.

Live non-secret identifiers visible in GitHub:

```text
App name   Codexless Runtime Bridge
Owner      shakaarlatief
App ID     4881901
Client ID  Iv23ligrmw82wVOSGTWn
Slug       codexless-runtime-bridge
Public URL https://github.com/apps/codexless-runtime-bridge
```

No Client secret, private key, access token, refresh token or device code was generated in the supplied evidence.

GitHub's live post-registration UI now displays an installation gate:

```text
Registration successful. You must generate a private key in order to install your GitHub App.
```

This is new empirical host evidence and supersedes the earlier assumption that no private-key bootstrap step would be required before installation.

The underlying Runtime Bridge authorization architecture does **not** change: GitHub's official device-flow contract uses the App Client ID plus device code and does not require a client secret, and refresh requests for user tokens originally generated through device flow likewise do not require a client secret. The App private key is required for authenticating as the App itself / installation-token flows, which Runtime Bridge is not currently using.

Therefore the corrected bounded bootstrap is:

```text
1. generate exactly one GitHub App private key only because current GitHub UI requires it before installation;
2. never paste, print, commit, upload or expose the PEM through ChatGPT/Runtime Bridge;
3. do not generate a Client secret;
4. install the App on shakaarlatief with All repositories;
5. after installation is confirmed, securely destroy the downloaded local PEM;
6. leave the corresponding GitHub-side public key registered so the App continues to satisfy GitHub's key-existence requirement;
7. continue Runtime Bridge with device-flow user access tokens using Client ID only.
```

Destroying the local private half does not affect the GitHub installation or device-flow user-token architecture because GitHub stores only the public half of the App key and the selected Runtime Bridge flow does not use App JWT authentication.

```text
VALIDATION154=PASS
GITHUB_APP_REGISTERED=true
APP_ID=4881901
CLIENT_ID=Iv23ligrmw82wVOSGTWn
APP_SLUG=codexless-runtime-bridge
GITHUB_APP_INSTALLED=false
PRIVATE_KEY_GENERATED=false
CLIENT_SECRET_GENERATED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_GENERATE_ONE_PRIVATE_KEY_INSTALL_ALL_REPOSITORIES_THEN_DESTROY_LOCAL_PEM
```
