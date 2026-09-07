# Validation 095: Office Preview.17 Live Source Published / Restart Pending

**Date:** 2026-09-07
**Status:** PASS / LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Research:** Research 121
**Scope:** Preserve successful ordinary-host publication of the qualified 61-tool Office file-link package, independent verification of all installed hashes, preservation of the AB-020 semantic-Git correction, and the explicit pre-restart process boundary.

## Publication result

The third guarded ordinary-host `-Publish` attempt completed successfully after the atomic replacement harness corrections:

```text
OFFICE_FILE_LINK_PUBLICATION_RESULT=PASS
LIVE_DISK_REGRESSIONS=PASS scripts=8
AB020_SEMANTIC_GIT_PRESERVED=true
RESTART_PERFORMED=false
```

The helper also reran the 10/10 file-link suite, all seven 61-tool staged/public regressions, the 8/8 AB-020 suite, and the exact Windows replacement primitive before mutation.

## Independent installed-byte verification

A separate read-only ADS probe re-read all nine preview.17 publication targets plus the AB-020 semantic-Git source. Every hash matched the exact qualified candidate:

```text
src/mcp-server-factory.mjs
9f6c002c4545ddde7963761c342f91657a0136eaa1954e1358ad49c57288cbdb

src/codexless-runtime.mjs
3a030c22d974f0fea504dc5f5b024054e4609738489c9920923c39817f78a552

src/surface-contracts.mjs
41a4188fa7edf10d3ec1bc79bbd02d2f7f68fdadd5373eba33896ca7f8cfa15c

test/public-surface-registration.mjs
ff6eba85ad20b99420de706aaa36b86ff7f875a99fd5929fcaeab6a08128bab5

test/bounded-git-fetch-origin.mjs
ccfb937ba4b723b629336410074f9ecd4fe7ba9764bfa07feb94e8a59cdf9f40

test/bounded-git-pull-ff-only.mjs
3949803c97f85bd075b93358964bf0816ca8aeeb18e83b8c254dad9acee64cda

src/file-link-reader.mjs
6394a83bf9f59b072e311e528d8f83e5e2d1b1df7c4b200aa99ab289b9d1c95d

src/file-resource-store.mjs
dea01debc69a3fe4a2d4dd785a71015c4d03f3d02f0c733d879cb9c97ea441e1

test/file-link-regression.mjs
d378c7109ffaef4be58c68d26abef863e5cb4a59bc245a33aa1febc8250d5db6

src/semantic-git.mjs
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

`AllHashesMatch=true`. The private durable candidate remains at `386813d1a31afd6748ad829c2f1dab3ea1bb89f4`.

## Running process before restart

The independently probed process and tunnel remain healthy but are still the pre-publication process image:

```text
running version  0.1.1-preview.16-hybrid-pdf-access
running tools    60
surface          codexless-public-preview-v2
tunnel health    HTTP 200
tunnel ready     HTTP 200
```

This is expected and is not evidence that preview.17 is active. The tool-surface change becomes process-live only after the controlled restart.

## Next action

`docs/local_execution/OPERATIONS.md` was re-read at this boundary. The next action is the full controlled restart: stop tunnel first while keeping its Git Bash shell open, stop/restart Codexless, require local health to report preview.17 with 61 tools, restart the tunnel and require HTTP 200/200, then refresh the existing ChatGPT developer MCP app because the public surface changed. A fresh disposable chat must perform read-only discovery before first `codex.file_link` use.

```text
OFFICE_PREVIEW17_LIVE_SOURCE_PUBLICATION=PASS
INSTALLED_HASH_VERIFICATION=PASS
RESTART_PERFORMED=false
NEXT=CONTROLLED_RESTART
```
