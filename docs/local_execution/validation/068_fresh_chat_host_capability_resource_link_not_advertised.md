# Validation 068: Fresh Chat Host Capability Snapshot Does Not Advertise ResourceLink Model Context

**Date:** 2026-09-06
**Status:** PASS / FRESH TOOL PROJECTION / MCP APP HANDSHAKE PASS / `updateModelContext` ADVERTISED / `resourceLink` NOT ADVERTISED / RESULT-STORE BUG LOCALIZED
**Research:** Research 117 / Research 119
**Scope:** Preserve the fresh disposable ChatGPT qualification of the temporary Checkpoint 309 MCP Apps host-capability probe, classify the actual ChatGPT host advertisement for `updateModelContext.resourceLink`, separate the raw host result from the diagnostic result-store lifetime bug, and select the next direct-file experiment.

## Governing objective

Research 119 remains authoritative. The target is direct bounded ChatGPT access to authorized local-machine files through Codexless. A source or faithful model-free source representation must reach ChatGPT directly; another reasoning model interpreting the source is a separate delegated-analysis capability.

## Fresh-chat qualification

A separate fresh disposable ChatGPT conversation was opened after the live Codexless `0.1.1-preview.15-host-capability-probe` / 59-tool publication and Plugin refresh. It was deliberately not treated as the next persistent ADS session.

Fresh projection evidence:

```text
codex.host_capability_probe          EXPOSED
codex.host_capability_probe_result   EXPOSED
probe tool call                      PASS
MCP App mount                        PASS
```

This closes the Checkpoint 309 uncertainty about whether a fresh conversation would acquire the newly published tool projection. It did.

## Raw host capability evidence

The mounted MCP App visibly completed the `ui/initialize` handshake. The user returned a screenshot of the rendered diagnostic to the persistent project conversation. The widget displayed the status:

```text
Host capabilities recorded. Use the result tool to read the server-side receipt.
```

The visible raw host snapshot was:

```json
{
  "protocolVersion": "2026-01-26",
  "host": {
    "name": "chatgpt",
    "version": "0.0.1"
  },
  "capabilities": {
    "updateModelContext": {},
    "message": {},
    "downloadFile": null,
    "serverResources": {
      "available": true,
      "listChanged": false
    },
    "serverTools": {
      "available": true,
      "listChanged": false
    },
    "logging": {},
    "openLinks": {}
  },
  "chatgptExtensions": {
    "windowOpenAI": true,
    "callTool": true,
    "uploadFile": true,
    "selectFiles": true,
    "getFileDownloadUrl": true
  }
}
```

The screenshot is direct fresh-host evidence. It is stronger for the requested capability classification than the later empty model-visible receipt because it shows the actual initialization result rendered by the MCP App.

## Capability classification

The MCP Apps `McpUiHostCapabilities` contract defines `updateModelContext` as a `McpUiSupportedContentBlockModalities` object. Each supported content modality is represented by its own optional property. In particular:

```text
resourceLink?: {}
    Host supports resource link content blocks.
```

The observed host advertises:

```text
updateModelContext = {}
```

but that object contains no `resourceLink` property and no other content-modality property.

Therefore the correct bounded classification is:

```text
UPDATE_MODEL_CONTEXT = ADVERTISED
UPDATE_MODEL_CONTEXT_RESOURCE_LINK = NOT_ADVERTISED
```

This does not prove that `ui/update-model-context` is unusable for every content type forever. It establishes only that the current ChatGPT host did not advertise the `resourceLink` modality in this fresh qualification.

It also establishes nothing new about the existing whole-PDF host-materialization size boundary. Capability advertisement and large-file materialization are separate questions.

## Why `codex.host_capability_probe_result` returned `not_recorded`

The fresh conversation called the result tool twice after the mounted widget had visibly reported successful recording. Both calls returned:

```json
{"status":"not_recorded"}
```

The disposable chat therefore conservatively declined to classify `resourceLink`. Subsequent source review in the persistent project conversation localized a diagnostic-state lifetime bug rather than a failed host handshake.

The current HTTP MCP runtime constructs a fresh `McpServer` per request. `registerHostCapabilityProbe()` currently defaults:

```text
store = createHostCapabilityProbeStore()
```

inside each server registration. Consequently:

```text
widget app-only report request
    -> server registration A
    -> store A records snapshot

later model-visible result request
    -> server registration B
    -> fresh empty store B
    -> {"status":"not_recorded"}
```

A new focused private regression reproduces the same behavior without the host: two separately registered probe instances receive isolated default stores; reporting into the first does not populate the second result reader.

```text
host-capability-probe tests
    tests 6
    pass 6
    fail 0

new regression
    default stores are isolated across separate server registrations = PASS
```

The result-store bug therefore does not invalidate the raw host capability snapshot. If the diagnostic is reused later, its store should be moved to Codexless runtime lifetime rather than request/server-registration lifetime. No live repair is needed to resolve the current discriminator.

## Other observed ChatGPT helpers

The host snapshot also feature-detected:

```text
window.openai                present
callTool                     present
uploadFile                   present
selectFiles                  present
getFileDownloadUrl           present
```

These are useful host-integration evidence but are not silently promoted into a solution. Current OpenAI Plugin documentation describes file selection/upload/download-URL helpers, but this qualification did not establish a supported arbitrary custom-MCP mechanism for Codexless to mint a ChatGPT-managed file ID directly from local bytes without user selection/upload.

## Decision and next experiment

Checkpoint 309 explicitly defined the branch:

```text
resourceLink advertised
    -> tiny PDF resourceLink -> ui/update-model-context qualification

resourceLink not advertised
    -> stop that route for the current host
    -> deterministic multi-native-PDF document_file_link experiment
```

The second branch now applies.

The next direct-access experiment should take the already-used approximately 11.8 MiB large-PDF fixture and produce deterministic valid PDF parts whose individual byte sizes remain below the known clean whole-PDF host-materialization PASS envelope. Each part should preserve source/page provenance and then be handed to the same ordinary ChatGPT conversation with `codex.document_file_link`.

A PASS may establish only:

```text
large source can be directly represented to ChatGPT as several native PDF parts
```

It must not be restated as:

```text
unchanged 11.8 MiB source materializes as one native ChatGPT file
```

No semantic reasoning model belongs in the split/handoff path.

## Result

```text
FRESH_CHAT_TOOL_PROJECTION = PASS
MCP_APP_UI_INITIALIZE = PASS
UPDATE_MODEL_CONTEXT = ADVERTISED
UPDATE_MODEL_CONTEXT_RESOURCE_LINK = NOT_ADVERTISED
PROBE_RESULT_STORE_LIFETIME = REQUEST_LOCAL_BUG
TINY_RESOURCE_LINK_MODEL_CONTEXT_TEST = SKIP
NEXT = DETERMINISTIC_MULTI_NATIVE_PDF_DOCUMENT_FILE_LINK
```
