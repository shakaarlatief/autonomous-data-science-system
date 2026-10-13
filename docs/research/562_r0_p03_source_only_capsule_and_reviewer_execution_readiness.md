# Research 562: R0-P03 source-only legacy capsule and reviewer execution readiness

**Date:** 2026-10-13
**Status:** SOURCE_CONTENT_PREPARATION_VERIFIED / REVIEWER_EXECUTION_AND_GOLD_CUSTODY_UNQUALIFIED / EXACT_FIXTURE_UNFROZEN
**Scope:** Inspect and narrowly repair the existing historical source exporter, verify source bytes, and establish the remaining independent-reference execution and authority boundaries without authoring or scoring tasks.
**Parent:** Research 513, 559, 560, 561; Checkpoint 897; Validation 250; owner-relayed bounded Codex request.
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `159de980266e183cf24ee08d0ab2e9f7d4f1e1ba`.
**Interaction:** Codex desktop / codex-01 / 01 - R0-P03 Source Capsule Verification; ChatGPT/chatgpt-38 retains task ownership and subsequent acceptance.
**Authority:** Engineering evidence and prospective readiness assessment only. This is not independent reference adjudication, an evaluator attestation, experiment freeze, a new repository charter, or physical architecture acceptance.

## Historical source capsule and verified evidence

The starting branch and HEAD exactly matched the handoff. Its only changes were the two untracked files `source_only_capsule_candidate.py` and `test_r0_p03_source_only_capsule.py`. Both were inspected before editing. The unchanged initial four-module P03 suite passed **36/36**.

The exporter calls the existing intake generator at immutable coordination ref `54b603c5fe550af963aac808b1fe7cacb516c6d4`. That generator consults the original scenario/annotation Git objects only to obtain historical source paths, source boundary and theme IDs. It resolves the **65 original regular-file Git blobs** at historical ref `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`. The exporter reads each source through `git show`, compares `git hash-object --stdin` with the expected blob ID, writes exclusively, and now reads the saved bytes back for exact equality.

The capsule has exactly three top-level entries:

- `sources/`: historical source bytes under their original relative paths.
- `reviewer_intake.json`: nine `legacy-01` through `legacy-09` aliases, historical topic hints and prospective reviewer instructions.
- `capsule_integrity.json`: counts, source manifest/content commitments and explicit limitations.

No original W5 answer-fixture file, B1 membership/relevance array, required/rejected source set, preferred-subject mapping or Git history is transferred. The historical source text is preserved rather than semantically redacted; source preparation does not erase its historical design context. The topic words still descend from B1 subject names, and the 65-source population remains historically selected for B1. Neither becomes an independently sampled benchmark or an authored natural-language question.

The saved corpus is **1,725,920 bytes**. Its source-content digest is:

```text
baf2b893435c1951b52814a3de897f7684890b1449bb437b46948cc868d304d3
```

This digest is SHA-256 of the UTF-8 concatenation, in case-sensitive lexicographic Git-path order, of `path + NUL + SHA256(source bytes) + LF`. It is not a hash of a platform-dependent directory enumeration or a concatenation of file contents alone. Validation 250 records the saved-byte recomputation, immutable-Git comparison and complete repeat-export equality, including both JSON files. No timestamps or destination paths enter output bytes.

## Demonstrated defects and bounded corrections

Two implementation defects were demonstrated with targeted regressions:

1. The path validator inspected `Path.parts` after normalization. It accepted duplicate separators, embedded `.` segments, a Windows drive-relative path, a Windows rooted path and case variants of `.git`; a lone `.` raised `IndexError`. It now checks raw slash-separated segments, rejects backslashes/colons and checks `.git` case-insensitively before constructing a filesystem path. All actual historical paths continue to pass.
2. The exporter hashed the Git input but only checked saved-file existence before returning success. An injected writer that appended a byte still received an integrity receipt describing the uncorrupted input. It now reads each closed saved file and rejects any byte mismatch before writing the receipt. A failed export may leave a new partial directory, which is not usable for review; existing destinations are never overwritten.

The original seven capsule tests remain, with deterministic-output coverage strengthened and ten additional cases covering saved-byte commitment, eight invalid path forms and corrupted saved output. The other 29 P03 tests and executable candidates are unchanged. No unrelated refactoring or production mechanism was added.

Materialization remains confined by the prototype's resolved-parent containment check to the repository's existing ignored `.venv` scratch root. Existing destinations and an immediate symlink parent are rejected; exclusive creation prevents overwriting an existing capsule. These are local staging safeguards, not hostile concurrent-filesystem confinement, a Windows ACL qualification, or proof that a reviewer cannot read the surrounding repository. A qualified handoff destination remains future work.

## Source integrity is distinct from reviewer execution isolation

This Codex session works inside the complete public checkout. It can read immutable Git history, original W5 annotations and answers, and R0-P03 design material. It has inspected exposed design and intake code. It therefore serves as an engineering verifier, **not a fresh neutralizer, reference adjudicator or scored evaluator**. The exposed ChatGPT/chatgpt-38 and Claude/claude-04 limitations remain unchanged.

A mechanically clean capsule can be delivered to a future independent actor, but copying files does not remove ambient filesystem, Git, browser, other-tool or conversation access. No isolated reviewer was launched, no denied-access tests for such an environment ran, and no exposure attestation or independent reference answer was obtained here. Available coding/reviewer capabilities are possible execution opportunities, not qualified independent-reference availability. An instruction to read only `sources/` is insufficient evidence of access restriction.

The next practical action is to qualify an actually available fresh, non-arm actor and its execution surface using the prepared input: identify the exact allowed sources/tools, demonstrate exclusion of original gold and arm-design context, record prior exposure and permitted output flow, and settle prospective disagreement handling before reference authorship. Reuse a suitable existing capability if it can meet these conditions. This work does not create or assign that reviewer. Separate fresh scored-evaluator requirements under Research 513 still apply later.

## Private repository authority and complete-gold custody

The owner-supplied handoff records an already verified private ADS companion repository and Codexless workspace, including GitHub's private visibility finding. The accepted `docs/private_companion/README.md` independently identifies that companion and its role: **knowledge-preservation complement only**, with the public repository the **sole ADS project-development repository**. The companion is **not a private development fork**. Its read/write/Git capabilities do not authorize a new experimental answer-store responsibility. The separate local-runtime contract likewise preserves runtime/materialization evidence rather than creating an alternate project-development authority.

No private repository was modified, no charter was changed, and no gold was stored. Prior private visibility is not re-certified by this local engineering check. A qualified restricted mechanism must preserve the **complete** independently authored answer packet in an immutable durable version, bind it publicly by digest before arm construction, and demonstrate that arm authors cannot retrieve it prematurely. A public plaintext packet leaks answers; a digest without the preserved complete packet is insufficient. The existing private companion's technical writability alone satisfies neither authority nor experimental separation. Any future custody arrangement requires its own explicit qualification rather than an inferred charter extension.

## Primary-task population and remaining execution blockers

A read-only exact-source scan verifies **36 numbered D-xxx decision headings** in `docs/DECISIONS.md`; their statuses and temporal authority vary. A decision heading is not automatically a genuine owner query, an independently meaningful task, or evidence that its answer closure fits the future build world. Counts alone cannot establish three tasks in each of Research 513's four categories: cold-start/current orientation; cross-plane discovery; impact/architecture evolution; exact-source/authority/recovery.

A fresh non-arm task author remains a reasonable prospective route. A prospectively mechanical historical owner-query/event rule remains permitted, and Research 513 prefers that route when fresh-author independence cannot be demonstrated. Either route still needs real provenance, category coverage, handling of superseded events, answerable source closure and prospective selection rules. Neither route is selected or executed here; no twelve scored tasks were authored.

The remaining blockers and proportionate next actions are:

| Unresolved obligation | Next bounded action |
|---|---|
| Fresh legacy neutralizer/adjudicator and actual execution isolation | Qualify a concrete available actor, exposure declaration and allowed/denied source/tool boundary before reference work. |
| Authorized restricted complete-gold preservation | Qualify responsibility, durable full-packet versioning, public commitment and exclusion of arm-author access; do not repurpose the companion by assumption. |
| Twelve independent primary tasks with source closure | Qualify one permitted authorship/selection route against all four categories before task choice or build conditioning. |
| Exact fair experiment world and evaluation contract | After the reference prerequisites, prospectively freeze corpus, task wording, references, common substrate, distinct arms, disclosure, fresh evaluator/run and adjudication rules. |

Owner-approved Research 559 Option A remains **approved but unexecuted**. Preserve original Research 217/W5 fixtures and results, original Research 513 text, nine legacy cases and >=8/9 gate, twelve primary tasks and >=10/12 gate, and zero false-authority tolerance. No task/answer packet, held-out cohort, scored experiment, physical target, implementation/migration cutover or new Claude review is authorized or claimed. R0-P01 remains AMEND/deferred, R0-P02 remains bounded PASS, and Specification 028 remains operational authority.

```text
SOURCE_CAPSULE=PREPARED_AND_BYTE_VERIFIED
REVIEWER_EXECUTION=NOT_QUALIFIED
INDEPENDENT_REFERENCE_ANSWERS=NOT_AUTHORED
RESTRICTED_COMPLETE_GOLD_CUSTODY=NOT_QUALIFIED
PRIMARY_TASK_ROUTE=UNSELECTED
EXACT_EXPERIMENT_FIXTURE=UNFROZEN
P03_SCORE=NOT_OBSERVED
NEXT_ACTOR=chatgpt
NEXT_BOUNDARY=p-three-reviewer-execution-authority-qualification
```
