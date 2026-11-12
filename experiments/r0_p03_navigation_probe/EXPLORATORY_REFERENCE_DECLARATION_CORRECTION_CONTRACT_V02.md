# V02 additive correction: source-owned declared-reference evidence, no semantic elevation

**Date:** 2026-11-12
**Status:** V01 audit immutably preserved / V02 fixed method before V02 run / exploratory source evidence only
**Immutable V01:** `exploratory_reference_provenance_audit_result_v01.json`, 177638 bytes, SHA-256 `e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299`.
**Source:** Same exact pinned historical 65 Git sources at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`. Original Checkpoint 910 output remains hash `b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e`.

## Discovered V01 classification error

V01's `PATH_SELECTOR` indicator looked for the full string `path:docs/` only in a prefix ending at the **first character** of the `docs/...` token. This systematically **missed** a selector adjacent to the current token while incidentally labeling some later tokens on the same line if an earlier `path:docs/` occurred. Actual V01 flagged 7 occurrences; this is **not the actual number** of adjacent `path:` selectors. The line/byte provenance, syntax context and 110 legacy pairs remain unchanged. This is a legitimate observed mechanical defect; never silently rewrite the V01 output.

An independent exact adjacent-selector preflight found **18** unique occurrences/edges with immediate `path:` before the current source-path token, of which **11** are authored under explicit Markdown `**Declared references:**` metadata lines. These numbers informed this correction but are not independent semantic gold; disclose preflight exposure.

## V02 fixed correction and scope

1. Re-run the V01 full source audit (and verify the original V01 result SHA-256) against exact Git object bytes. Require all previous occurrence identities, source SHA-256 and Git blob SHA-1 values, line numbers, original lines, context classes, and flags **other than PATH_SELECTOR** to remain byte-identical in meaning.
2. Remove the erroneous `PATH_SELECTOR` flag for each occurrence and recompute it **only** when the five characters immediately preceding this occurrence's actual token equal `path:` case-insensitively. This is a string-syntax diagnostic, not validated source schema.
3. Add an independent `DECLARED_REFERENCES_FIELD` diagnostic only when the token has that immediate `path:` prefix and the same exact original line contains the authored heading `**Declared references:**` (case-insensitive). This identifies *source-owned declared-reference metadata*, not normative relationship, operational dependency, currentness, true target authority or authentic Research 513 B2/J2 link.
4. Compare V02's original 146 occurrences and 110 pairs against an **independent eligible-path enumeration**: enumerate each of the exact 65 eligible target paths via escaped exact-string matching on each historical original text line with bounded token boundaries. Accept a trailing punctuation mark after a valid `.md`/`.json` path, but reject trailing alphanumeric or ineligible path continuation and obvious `.md.bak` extension continuations. This challenger is a parity/defect check; not new independent natural-language gold. Report any differences without modifying V01. (Preflight showed no extra pairs or occurrences in this pinned corpus; the legacy regex has a known synthetic terminal-period blind spot.)
5. Preserve the syntactic graph projections RAW_PATH_MENTIONS 110, OUTSIDE_FENCE 40, OTHER_TEXT_ONLY 7 and MARKDOWN_LINKS_ONLY 0. Add two explicit **candidate metadata** projections: adjacent PATH_SELECTOR and DECLARED_REFERENCES_FIELD. Their edges may not be projected as accepted J2/B2 authority. Record each original source and exact line witness in the output.
6. Recompute all counts and statistics deterministically. No original experiment scoring, primary source admission, B0–B4 arm changes, gold or private C01/C02 access. No code changes to V01 or prior checkpoints.

## Negative controls and limits

Unit tests must demonstrate: selector recognized at exact token adjacency; a prior selector in the same source line does not qualify another token; a source-author declaration indicator is correctly limited to the authored field; an arbitrary literal path does not become a declared relation; direct original Git bytes and V01 result hashes match; alternate exact-string scan matches the actual pinned corpus while exposing synthetic terminal punctuation behavior difference.

A source-owned `Declared references` line is a real authored relationship to other *cited sources*, but it says only that a reference is declared. It does **not** mean the cited file governs the citing file or implements the same evidence standard. Potential governance in inline prose remains a separate case-level semantic question.

    FROZEN_V01_EXACT_BYTES=177638
    FROZEN_V01_EXACT_SHA256=e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299
    ORIGINAL_SOURCE_COUNT=65
    ORIGINAL_MENTION_EDGES=110
    ADJACENT_PATH_SELECTOR_PREFLIGHT=18
    DECLARED_REFERENCES_FIELD_PREFLIGHT=11
    V02_OUTPUT=EXCLUSIVE_CREATE_SEPARATE_FILE
    AUTHORITY_ADMISSIONS=NONE
    FORMAL_R0_P03_SCORE=NONE
