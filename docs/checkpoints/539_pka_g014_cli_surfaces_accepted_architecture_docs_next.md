# Checkpoint 539: PKA-G014 CLI Surfaces Accepted, Architecture Documentation Next

**Date:** 2026-09-18
**Status:** PKA-G014 ACCEPTED / PKA-G001..PKA-G014 PASS / W0 CONTINUES / W1 BLOCKED
**Checkpoint class:** IMPLEMENTATION / VALIDATION / PROJECT_KNOWLEDGE
**Project stage:** Selected project-development knowledge architecture W0 implementation
**Scope:** Accept deterministic CLI validation/rebuild/refresh/freshness surfaces after adversarial write-boundary hardening, completion of the full eight-view persistent W0 contract, and complete regression qualification; advance W0 to PKA-G015 architecture documentation.
**Authority:** Specification 028 remains governing. Research 179 remains the accepted W0 implementation design, with Research 185 retaining its G010 field-level refinement. Research 190 records G014 implementation/result evidence. Current continuity remains operational authority.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-26
**Conversation title:** 26 - Full Rebuild and Incremental Refresh Equivalence
**Primary collaborator:** ChatGPT

```text
selected architecture                   PKA-CANDIDATE-01
implementation contract                 Specification 028
implementation design                   Research 179 (+ Research 185 for G010)
G014 result                              Research 190
initial G014 commit                      05dca1d6d3f71dfa19c0c166be83dc08ae6e9237
accepted implementation base            eae343ac1f5c242b19d69f5c5c888cfe9b7bf0bd
PKA-G001..PKA-G014                      PASS
PKA-G015..PKA-G017                      PENDING
G014 CLI                                 26 / 26 PASS
persistent W0 views                       5 / 5 PASS
architecture guards                      23 / 23 PASS
G009 + G013 regression                  169 / 169 PASS
complete unit inventory               1,130 / 1,130 PASS
compileall                               PASS
pre-documentation WORKTREE validation   PASS / 1418 candidates / zero diagnostics
acceptance-document WORKTREE validation PASS / 1420 candidates / zero diagnostics
implementation COMMIT validation        PASS / 1418 candidates / zero diagnostics
public repository integrity             PASS
git diff --check                        PASS
W0 overall                               IN PROGRESS
W1 migration                             NOT STARTED
successor authority publication          NONE
compatibility overwrite                  NONE
current operational authority           current continuity architecture
authority switch allowed                false
```

G014 exposes deterministic JSON command surfaces for query-independent validation, full rebuild, G013-backed incremental refresh and generated-artifact freshness. Hard defects fail non-zero. Rebuild and refresh are stage/diff-only by default; repository materialization requires explicit `--write`.

Acceptance review found that the first committed CLI implementation wired only the G009 demonstration `source_inventory` plus G010 `current_state_core`, while Specification 028 requires eight persistent W0 structural artifacts. The accepted repair implements and registers the complete persistent set: source catalog, identity index, authority index, workstream graph, subject index, risk/obligation index, machine current-state core and Markdown current-state core.

The repair also introduces explicit authority-class input selection so `identity_index` can include accepted historical sources without broadening every other view. That selector contract is bound into G009 manifests and covered by G013 impact analysis. Identity and workstream projections were cross-checked against the already accepted G006 and G008 semantics.

Generated artifact materialization is confined to `docs/project_knowledge/generated/`. Adversarial review additionally exposed hard-link alias risk at an existing generated path; the accepted adapter writes a same-directory temporary file, flushes/fsyncs it, and replaces the generated path atomically so a hard-linked external/canonical inode is not modified in place. Explicit writes reject local drift in every governed input class that can influence the production views, including accepted historical identity inputs.

Final qualification passes 54/54 focused G014/persistent/architecture tests, 169/169 G009/G013 regressions and the complete 1,130-test unit inventory. Exact committed project-knowledge validation passes at `eae343ac1f5c242b19d69f5c5c888cfe9b7bf0bd`.

No W1 migration, private-companion mutation, successor-view authority publication, compatibility overwrite or authority switch occurred. The new CLI and generated views remain derived tooling under the current continuity architecture.

```text
CHECKPOINT539=PKA_G014_ACCEPTED
RESEARCH190=ACCEPTED
NEXT=PKA_G015_ARCHITECTURE_DOCUMENTATION
W1_MIGRATION=BLOCKED
CURRENT_ARCHITECTURE=STILL_AUTHORITY
AUTHORITY_SWITCH_ALLOWED=false
```
