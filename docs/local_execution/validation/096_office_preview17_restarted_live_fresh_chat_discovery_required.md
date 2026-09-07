# Validation 096: Office Preview.17 Restarted Live / Fresh Chat Discovery Required

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.17 LIVE / TUNNEL READY / SAME-CHAT PROJECTION STALE
**Research:** Research 121
**Scope:** Preserve the controlled restart result for the Office file-link surface, independently verify the live process/tunnel and installed core hashes, and distinguish live runtime activation from this persistent ChatGPT conversation's stale callable projection.

## Restart result

After the repository-governed controlled restart, the user reported and an independent read-only ADS probe confirmed:

```text
version        0.1.1-preview.17-office-file-link
toolCount      61
surface        codexless-public-preview-v2
tunnel health  HTTP 200
tunnel ready   HTTP 200
```

The same independent probe re-read the live AB-020 semantic-Git source and the two new Office source modules:

```text
semantic-git.mjs
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02

file-link-reader.mjs
6394a83bf9f59b072e311e528d8f83e5e2d1b1df7c4b200aa99ab289b9d1c95d

file-resource-store.mjs
dea01debc69a3fe4a2d4dd785a71015c4d03f3d02f0c733d879cb9c97ea441e1
```

All match the qualified/published sources.

## Same-chat projection result

After live preview.17 activation, dynamic tool discovery in this existing persistent conversation was queried specifically for `file_link`. The projection still did not expose the new `codex.file_link` action, while older file-link-related tools remained visible.

Therefore the correct classification is:

```text
LOCAL_RUNTIME_PREVIEW17=LIVE
LOCAL_TOOL_COUNT=61
TUNNEL_READY=PASS
CURRENT_PERSISTENT_CHAT_CODEX_FILE_LINK=NOT_EXPOSED
CLASSIFICATION=SAME_CHAT_STALE_PROJECTION
```

This is consistent with the already-preserved AB-008 behavior: a refreshed/restarted local surface can be valid while an existing conversation retains an older callable action projection. It is not evidence that preview.17 registration failed.

## Next action

Because the public tool surface changed, `docs/local_execution/OPERATIONS.md` requires refreshing/rescanning the existing ChatGPT developer MCP app only after local health and tunnel readiness are healthy. Both gates are now satisfied.

The next sequence is:

```text
refresh ADS Codexless Local Bridge in ChatGPT Settings -> Plug-ins
-> open a fresh disposable conversation
-> perform read-only discovery for codex.file_link
-> if exposed, run exactly one native file-link qualification per deterministic DOCX/PPTX/XLSX fixture
-> distinguish host materialization, text/data/structure access, visual/layout fidelity, and fallback need
```

No `codex.file_link` invocation should be substituted in this stale persistent conversation.

```text
OFFICE_PREVIEW17_LIVE_ACTIVATION=PASS
SAME_CHAT_NEW_TOOL_PROJECTION=STALE
NEXT=PLUGIN_REFRESH_AND_FRESH_CHAT_DISCOVERY
```
