# W1_RULE: Prospective R0-P03-V2 build-world sampling and source-reported common substrate

**Date:** 2026-11-16
**Status:** PROSPECTIVELY_FROZEN_BEFORE_FIRST_W1_EXECUTION / NO_BUILD_DRAW_YET / HELDOUT_NOT_DRAWN / NO_TASKS
**Scope:** The single bounded W1 source-world exercise requested by MC-0030 Message 113 §5. This rule is committed and published **before** any W1 source selection/generator execution. It is not a modification of Research 513, 559, 576 or 673.
**Authority:** Owner-accepted Research 673 M1–M6 and Research 559 source-assertion extraction with explicit uncertainty. Exposed coordinator may author this pre-task experiment-only rule; source paths and extracted records gain no production or governing authority.

## 1. Fixed source horizon and immutable eligibility

- Original historical Git source revision: `17ea403ef64092f275e3c7d6492d99929804f8e5` (the Checkpoint 954 original ADS source horizon).
- Candidate frame: exact paths/blob IDs obtained from `role_frame_candidate.committed_paths` at that revision, under its fixed `SOURCE_ROOTS`, limited to `REVIEWABLE_SUFFIXES`, bucket `REVIEW*` in `proposed_family`, excluding `leakage_reason(path)` and all explicitly named exclusions below. The recorded 2,897 is a historical feasibility count, **not** a source admission count.
- Every eligible file must be a nonempty UTF-8 original Git blob. Verify raw Git blob hash, content SHA-256, byte size and original commit. Never use mutable worktree bytes as the source. Reject suspicious absolute, traversal or duplicate path. Preserve all source bytes for equal read/lexical access, not only extracted spans.
- Exclude `docs/CURRENT_STATE.md`, `docs/KNOWLEDGE_MAP.md`, and `docs/ARCHITECTURE_PROGRAM_OVERVIEW.md` because these accumulated P03 design/results expose comparison content; also exclude all model-collaboration `/messages/` files, `experiments/r0_p03_navigation_probe/`, any `tests/unit/test_r0_p03_*`, and `role_frame_candidate.leakage_reason` paths.
- Exclude any carrier whose **first H1** (first line beginning `# `, if present) or any `**Scope:**` line among the first 48 original lines contains the case-insensitive whole marker `R0-P03`, `R0_P03`, `P03`, `navigation probe`, `W5` or `B0` through `B4`. Ordinary body mentions of those markers are not independently a disqualification unless the known path exclusions above apply. Log every exclusion reason and count. Never claim this necessary prefilter proves cumulative blindness or correctness.

## 2. Fixed source seed, role strata and graph

The following **ten task-independent seed anchors** represent existing real ADS orientation, Specification 028 and the existing experimental S1 implementation/verification evidence. They do **not** imply accepted J1/J2 for these carriers:

1. `docs/DECISIONS.md`
2. `docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md`
3. `docs/CONTINUITY.md`
4. `tools/project_knowledge/identity.py`
5. `tools/project_knowledge/services/refresh.py`
6. `tools/project_knowledge/services/generation.py`
7. `tests/unit/test_project_knowledge_identity.py`
8. `tests/unit/test_project_knowledge_refresh.py`
9. `schemas/project_knowledge/semantic_source.v1.schema.json`
10. `docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`

If any mandatory seed is missing or excluded, fail closed `W1_RULE_INFEASIBLE`; never replace it with a convenient source after observing the result.

Classify each candidate into exactly one **source-location sampling stratum**, *not* a semantic authority class, in this precedence order:

| Stratum | Exact path rule | Build | Future heldout |
|---|---|---:|---:|
| `governing` | `docs/DECISIONS.md`, `docs/specifications/**` | 9 | 3 |
| `orientation_foundation` | `docs/foundations/**`, root-level `docs/*.md`, `docs/project_knowledge/**` | 7 | 2 |
| `project_realization` | `tools/**`, `scripts/**`, `schemas/**`, `migrations/**` | 12 | 4 |
| `product_realization` | `src/**`, `frontend/**` | 10 | 3 |
| `verification` | `tests/**` | 8 | 3 |
| `historical_evidence` | `docs/research/**`, `docs/checkpoints/**`, `docs/local_execution/**` | 10 | 3 |
| `domain_collaboration` | remaining permitted `docs/**` (including `docs/cockpit/**`, `docs/source_universe/**`, `docs/model_collaboration/**`) | 4 | 2 |
| **Total** | | **60** | **20** |

No class confers provenance, accepted effect, currentness, implementation conformity or an independent relevance judgment.

**Literal-document path citation rule:** from a UTF-8 source body, recognize only exact case-sensitive candidate repository paths that occur as bounded path tokens (the whole path, not arbitrary basename or substring), preceded/followed by a non-path character. Allowed path characters are ASCII letters, digits, underscore, dot, hyphen, slash. A citation graph edge is source path → exact target path, when different and the target is in the eligible frame. The edge has evidence class `LITERAL_DOCUMENTARY_MENTION`, not `REALIZES`, `SUPERSEDES`, `ACCEPTED` or required dependency. Do not infer edges from filenames, Python imports, folder membership, numbered Research IDs, or semantic similarity.

Perform breadth-first expansion from the ten sorted seed paths through exact literal path citations, up to **four edges**. Within each BFS layer, traverse target paths in ascending `SHA-256("W1-EXPAND-v1" || NUL || path || NUL || git_blob_oid)`, then path. Record minimum distance and first deterministic predecessor witness. Reaching a source does **not** prove its documentary context has been fully closed.

## 3. Build selection, deterministic fallbacks, and nonpromotion

- Mandatory seeds are included in the 60 build paths and count against their stratum quota.
- In every stratum, order eligible non-seed carriers by `(BFS_distance_or_99, SHA-256("W1-BUILD-v1" || NUL || source_path || NUL || git_blob_oid), path)`. Take the first available candidates until that stratum's exact build quota is met; union with mandatory seeds. A carrier disconnected from the four-hop citation frontier has `distance=99` and must be recorded as `DETERMINISTIC_DISCONNECTED_STRATUM_BACKFILL` with **no invented graph relationship**.
- If a stratum cannot fill its quota from the eligible frame, fail `W1_RULE_INFEASIBLE` with missing counts. A single **prospective** rule amendment is allowed with its reason committed before any retry; do not silently reroll. The 60/20 target is preferred; Research 513's 3:1 fallback can only be considered with a separately evidenced true fewer-than-80 eligible universe and cannot be invented to disguise a bad stratum rule.
- Output a create-only `w1_manifest.json` with original source commit, Git OID, content SHA, bytes, path role **hint**, stratum, BFS distance, predecessor (when available), selected BUILD marker, and the fixed heldout **rule**, but no heldout path, salt, task, answer or rank score. Preserve `w1_exclusion_log.json` as counts and exact excluded path/reason **only**; it is task-free prefreeze metadata and cannot be exposed to a fresh author as navigational hints.
- Any attempt to use path/source-family labels as semantic authority, an external ranking feature, or hidden answer material is invalid.

## 4. Common substrate mechanical extraction and scope

- On all **60 exact build** original texts, extract bounded literal source claims with path, original Git blob OID, source revision, original 1-based line number, exact UTF-8 line content and line-content SHA-256. Revalidate every extracted line against the original bytes.
- `docs/DECISIONS.md`: extract each `## D-XXX.` declaration, its raw first status line within the entry, and explicit literal `Supersedes:` lines. These are **SOURCE_REPORTED** facts, not current accepted effects. Existing decision/implementation status and dates remain raw text.
- Markdown documents: extract the literal `**Status:**`, `**Authority:**`, `**Scope:**`, `**Parent:**` and `**Supersedes:**` header lines from the first 48 original lines as `SOURCE_REPORTED`. No `Status: PASS` becomes a verified test outcome or current status merely because the source reports it.
- Every selected text: extract the first 24 distinct exact *literal source-path citation line witnesses* in original line/target order, class `SOURCE_REPORTED`, relation `LITERAL_DOCUMENTARY_MENTION`. Label the presence of additional matches as a **bounded-extraction remainder UNKNOWN**, rather than treating omitted links as absent.
- `.py`, `.ts`, `.tsx`, `.js`, `.mjs`, `.sql`, `.yml`, `.yaml`: extract the first 24 lines starting a direct `def`, `class`, `function`, `export`, `CREATE`, `name:`, `on:`, `jobs:`, or `test_` definition, class `DEFINITION_ONLY_NOT_EXECUTION`. Observing a test or workflow definition **does not** establish execution success, deployment or natural-owner J2.
- Every selected original blob itself has one `OBSERVABLE_GIT_BLOB` record containing the verifiable Git blob OID, raw-byte SHA-256, length and pinned revision; it is not an accepted effect. Git revision cannot make assertions in old content currently true.
- Separately include **one** accepted experimental-core envelope from the exact previously source-verified S1 J1/J2/J3 receipt `1b31365160e29b902d578222a8dc39e15c55b49e0e592448baeada13284b4341`, read from `17ea403ef64092f275e3c7d6492d99929804f8e5:experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_j3_lifecycle_result_v01.json`. Class `ACCEPTED_EXPERIMENT_ONLY_WEAK_ASSURANCE`; exact four accepted J1 IDs, one source-relative experimental J2 and the separate J3 result, with the recorded actor weakness. **This is the only accepted-effect entry.** The S1 Git evidence may reside outside the sampled build paths as fixed shared experimental-core evidence, available identically to every arm; it must not become one of the sampling carriers or a private answer.
- The common derived orientation is non-governing and lists the observed source roster plus the S1 currentness/evidence envelope. Missing semantic relations and unverified authority remain `SOURCE_BOUNDED_UNKNOWN`.
- The extractor is a **bounded source-reported mechanical view**, not semantic adjudication, no per-carrier natural-owner acceptance, no exhaustive source-citation closure, no automatically accepted source role or task answerability gold.

## 5. Precommitted heldout procedure; no premature draw

- **Do not draw or compute the actual 20 heldout paths before the real `C_arm` has been committed** with B0-B3 implementation and metadata frozen. A future procedure must revalidate the exact candidate frame, exclude the 60 build carriers, use the same seven stratum eligibility rules and draw the seven heldout quotas above.
- For each stratum, order remaining eligible carriers by `SHA-256("W1-HELDOUT-v1" || NUL || C_arm_full_40_hex || NUL || path || NUL || git_blob_oid)` then path. Select the first required count *after* `C_arm` and before scoring. The actor who draws may not change the seed, frame, strata or rules after seeing scores. The actual heldout identities must be withheld from arm authors until the planned evaluation boundary.
- A path sampled in BUILD is never allowed in HELDOUT. If any stratum cannot provide both its build and future heldout quota at the fixed source horizon, this W1 rule fails **now** as `W1_RULE_INFEASIBLE`, before arm freeze. No hidden rule reroll after scores.
- A preliminary count of remaining candidates per stratum is allowed now; listing or selecting prospective heldout identities is not.

## 6. Mandatory verification and finite stop

- **T1:** two W1 generator runs produce byte-identical manifest, substrate and exclusion log under the pinned commit and this preregistered rule.
- **T2:** exact Git source blob/SHA-256/size for all build carriers and every extracted cited line.
- **T3:** zero selected files match any exclusion rule.
- **T4:** all cited `SOURCE_REPORTED` and `DEFINITION_ONLY_NOT_EXECUTION` values exactly equal the source's cited line; zero source-reported entries carry accepted tags; **only one** experiment S1 envelope has `ACCEPTED_EXPERIMENT_ONLY_WEAK_ASSURANCE`, with exactly four accepted J1 and one J2.
- **T5:** exactly 60 build carriers under the frozen seven stratum quotas and enough additional eligible candidates for future 20 heldout without choosing their identities. Otherwise `W1_RULE_INFEASIBLE` and the bounded pre-scoring amendment-or-HOLD path.
- **T6:** all five arm labels `B0`–`B4` receive identical source/semantic/lexical/derived-orientation bytes and can exercise identical read/list/search methods on the W1 build, with full source content; no B1/B2/B3/B4 specific metadata is added to common fields. The earlier 695/956 24-source runtime tests remain independently preserved, not falsely represented as W1 parity.
- Run once under this frozen rule; only fix code defects without changing the rule and rerun for reproduction. One explicit prospective rule revision only if infeasible, committed before retry; otherwise record `W1_RULE_INFEASIBLE` and stop.
- No hidden gold, no selected primary tasks, no legacy packet change, no score, no B4 omission decision, no owner budget approval, no M6 formal attempt, no architecture selection or production J1/J2/J3 switch occurs in W1.

    W1_RULE_VERSION=1
    SOURCE_REF=17ea403ef64092f275e3c7d6492d99929804f8e5
    BUILD_TARGET=60
    HELDOUT_TARGET=20
    BFS_MAX_DEPTH=4
    STRATA=7
    WORLD_SOURCE_ASSERTION_CLASS=SOURCE_REPORTED
    ONLY_ACCEPTED_CORE=EXPERIMENT_S1_WEAK_ASSURANCE
    FIRST_W1_EXECUTION=NOT_YET_RUN
    HELDOUT_DRAW=PROHIBITED_BEFORE_C_ARM
    PRIMARY_TASKS=NONE
    FORMAL_P03=INCOMPLETE
