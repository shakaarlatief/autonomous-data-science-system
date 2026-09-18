# Checkpoint 538: PKA-G013 Rebuild Equivalence Accepted, CLI Surfaces Next

**Date:** 2026-09-18
**Status:** PKA-G013 ACCEPTED / PKA-G001..PKA-G013 PASS / W0 CONTINUES / W1 BLOCKED
**Checkpoint class:** IMPLEMENTATION / VALIDATION / PROJECT_KNOWLEDGE
**Project stage:** Selected project-development knowledge architecture W0 implementation
**Scope:** Accept full/incremental derived-view semantic equivalence after independent adversarial review and repair, and advance W0 to PKA-G014 deterministic CLI surfaces.
**Authority:** Specification 028 remains governing. Research 179 remains the accepted W0 implementation design, with Research 185 retaining its G010 field-level refinement. Research 189 records G013 implementation/result evidence. Current continuity remains operational authority.
**Interaction environment:** ChatGPT + Codex Desktop
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-26
**Conversation title:** 26 - Full Rebuild and Incremental Refresh Equivalence
**Primary collaborator:** ChatGPT + Codex in Codex Desktop

```text
selected architecture                  PKA-CANDIDATE-01
implementation contract                Specification 028
implementation design                  Research 179 (+ Research 185 for G010)
G013 result                             Research 189
accepted implementation base           192dc161203577c11e7a7fce869634a5fccc29d8
PKA-G001..PKA-G013                     PASS
PKA-G014..PKA-G017                     PENDING
G013 full/incremental                   38 / 38 PASS
G012 public/private                     34 / 34 PASS
G011 capture/promotion                  27 / 27 PASS
G010 current-state core                 76 / 76 PASS
G009 view framework                     53 / 53 PASS
G009 execution/adversarial              76 / 76 PASS
authority suite                        103 / 103 PASS
identity suite                          63 / 63 PASS
workstream suite                        89 / 89 PASS
substrate suite                        228 / 228 PASS
inherited unit inventory               309 / 309 PASS
complete unit inventory              1,096 / 1,096 PASS
compileall                              PASS
pre-documentation WORKTREE validation  PASS / 1416 candidates / zero diagnostics
acceptance-document WORKTREE validation PASS / 1418 candidates / zero diagnostics
implementation COMMIT validation       PASS / 1416 candidates / zero diagnostics
public repository integrity            PASS
git diff --check                       PASS
W0 overall                              IN PROGRESS
W1 migration                            NOT STARTED
successor view publication              NONE
compatibility overwrite                 NONE
current operational authority          current continuity architecture
authority switch allowed               false
```

G013 now provides a read-only deterministic refresh plan over exact committed previous/current snapshots. It compares exact implementation closures and, where those closures are comparable, complete G009-derived dependency/output envelopes. Affected views are rebuilt only through the existing `generate_views(...)` path from the complete current canonical corpus. No persisted view state is patched and no changed-file delta enters compute.

The first Codex implementation passed its focused qualification but was not accepted immediately. Independent ChatGPT review reproduced a specification-only `manifest_path` relocation that the initial impact comparison incorrectly classified as no impact because the accepted G009 manifest does not contain its own carrier path. The repair adds `manifest_path` only to the internal G013 impact envelope, preserves the G009 schema, and adds both a relocation regression and a complete `ViewSpecification` field-coverage guard.

The repaired implementation then passed 38/38 focused G013 tests and the complete 1,096-test unit inventory. ChatGPT independently reran the exact repair regressions, committed the reviewed implementation at `192dc161203577c11e7a7fce869634a5fccc29d8`, and verified the committed repository state.

The bounded Codex work occurred in the persistent Codex Desktop thread `Implement W0 knowledge substrate`, with the owner manually relaying prompts/results to `chatgpt-26`. This checkpoint records that collaboration fact without attempting to solve the broader collaboration-lineage modeling gap.

No W1 migration, private-companion mutation, successor-view publication, compatibility overwrite or authority switch occurred. The accepted G013 machinery remains derived/read-only substrate under the current continuity architecture.

```text
CHECKPOINT538=PKA_G013_ACCEPTED
RESEARCH189=ACCEPTED
NEXT=PKA_G014_DETERMINISTIC_CLI_SURFACES
W1_MIGRATION=BLOCKED
CURRENT_ARCHITECTURE=STILL_AUTHORITY
AUTHORITY_SWITCH_ALLOWED=false
```
