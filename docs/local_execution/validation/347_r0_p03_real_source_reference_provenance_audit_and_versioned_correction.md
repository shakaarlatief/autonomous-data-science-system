# Validation 347: Real source-level evidence audit and independently challenged V02 correction

**Date:** 2026-11-12
**Status:** ACTUAL_V01_V02_EXECUTION / EXACT_SOURCE_ORIGINALS / AUDIT_BUG_VERSIONED / FORMAL_R0_P03_UNSCORED
**Authority:** V01/V02 executable audit against Git-pinned originals, source-specific line and SHA-256 receipts, Research 648, Checkpoint 911.
**Scope:** Exact-source path occurrence provenance, versioned selector-field correction, independent alternate-path scanner and scientific interpretation limits.
**Research:** Research 648.

## Executed source-bound evidence

| Property | Observed |
| --- | --- |
| Exact historical source revision | `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` |
| Original document count | 65 |
| Original aggregate fingerprint | `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09` |
| V01 original audited occurrences / directed pairs | 146 / 110 |
| V01 source code / inline code / other text occurrences | 93 / 46 / 7 |
| Raw / outside-fence / outside-code / Markdown-link edge counts | 110 / 40 / 7 / 0 |
| V01 result original exact bytes / SHA-256 | 177638 / `e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299` |
| V01 PATH_SELECTOR diagnostic (known undercount) | 7 |
| V02 corrected adjacent path selectors | 18 |
| V02 authored Declared references entries | 11 |
| V02 source owners with authored Declared references | 6 |
| V02 unchanged original occurrence identity and source bytes | Verified |
| V02 independent exact eligible-path scan parity | 146/146 occurrences; 110/110 pairs, zero additions |
| V02 exact result bytes / SHA-256 | 175032 / `25b26e66e3bb03232d4ee7931e66aceb6bd6eaf28d2f5ae0ff207713c333831d` |

Both audit modules completed actual exclusive-create output runs. Original Checkpoint 910 experimental JSON identity was reverified. V02 used the fixed V01 output hash and reproduced the complete V01 data before changing only indicator flags; nothing was reclassified as authoritative.

The initial regression exposed two **test-only** defects (miscounted synthetic sample involving terminal punctuation, and mistaken dictionary-order assumption after sorted JSON serialization). Those test assertions were corrected with no changes to original result or method. A follow-on test caught the **real V01 PATH_SELECTOR flag defect**; it is retained as a V01 limitation and corrected in a separate V02 contract, module, output and tests. V01's exact bytes remain immutable. The legacy path-token regex has a synthetic trailing-period blind spot; an independent original-corpus scanner found no missing occurrences within the exact 65-source frame.

The same 110 source pairs were retained in V01 and V02. The resulting Declared references subset remains *source-owned reference declarations*, not an independently qualified governing, semantic J2, editorial B2, or operational dependency truth set.

## Engineering checks

## Observed full precommit engineering validation

- V01 source evidence audit + V02 independent extraction/correction, 719 paraphrase experiment and 130 relation experiment: **26/26 tests PASS** (20.75 seconds, no pytest cache, isolated temp).
- Previous hybrid/subject/link/heading source experiments plus C02 source-free private-evidence boundary tests: **34/34 PASS** (12.07 seconds). Total **60/60 actual focused checks PASS**.
- `scripts/check_current_routing.py`: **PASS**, Checkpoint **911**, branch `v1-source-vault-bootstrap-resume`, boundary `p-three-source-reference-provenance-and-declarations-audited`, formal outcome **INCOMPLETE**.
- `scripts/check_knowledge_map.py`: **PASS**, Research **648**, **912** numbered canonical checkpoints and 19 topic families.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **912/912** canonical checkpoint records compliant.
- `git check-attr text` for V01 and V02 source evidence results: **unset** for both, preserving raw Git bytes on Windows.
- `git diff --check`: exit **0** with ordinary Windows working-copy LF-to-CRLF warnings only.
- Full `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including model collaboration, family-aware contracts, Project Knowledge, checkpoints, Knowledge Map and routing. Its **first** invocation exposed a missing `Scope`/`Research` header in this new Validation 347 artifact and correctly failed; only the validation document header was amended, and the full gate then actually passed.
- Both exact saved source-result byte counts and SHA-256 values rechecked **PASS** after all changes.
- MC-0030 Message 063 is an exposed **prepared but not dispatched** Claude critique request; no reviewer response or independent gold is claimed.

No postcommit or GitHub publication result is inferred until separate actual commit/push/remote verification.
