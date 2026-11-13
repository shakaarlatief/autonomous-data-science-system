# Validation 348: Native parsed reference evidence and collaboration message identity guard

**Date:** 2026-11-13
**Status:** REAL_V03_NATIVE_GIT_SOURCE_AUDIT_EXECUTED / EXACT_063_COLLISION_GUARD_ADDED / INTEGRITY_CHECK_PENDING_POSTWRITE
**Scope:** Verify native Specification 025/028 parsing on real immutable 65 Git originals, detect historical typed-reference coverage gaps and test exact per-thread message identity collisions without rewriting prior artifacts.
**Research:** Research 649.
**Authority:** MC-0030 Message 064/065, frozen V01/V02 receipts, exact V03 executable original-source trace, source and hash-specific guard regression.

## Real evidence and test basis

    REVIEWER_COMMIT=a4065bcd36e0f023677468aa82105eeeca42e2ef
    REVIEWER_PARENT=6aff3c902803c48b778035580b583bcc9b93f483
    NEW_V03_SOURCE_GRAMMAR_OUTPUT_BYTES=138104
    NEW_V03_SOURCE_GRAMMAR_OUTPUT_SHA256=f6037c05a6d88e27dc22bb838db24d9e066619f19314dddc2a68ff766f4866cb
    OLD_V01_EXACT_SHA256=e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299
    OLD_V02_EXACT_SHA256=25b26e66e3bb03232d4ee7931e66aceb6bd6eaf28d2f5ae0ff207713c333831d
    SOURCES=65
    ORIGINAL_GIT_REVISION=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    NATIVE_SPEC025_TOKENS=59
    NATIVE_SPEC028_REFERENCE_TOKENS=20
    NATIVE_SPEC028_PROVENANCE_TOKENS=34
    IN_CORPUS_TYPED_PAIRS=31
    IN_CORPUS_TYPED_PAIRS_NOT_IN_PREVIOUS_110=12
    FRAGMENT_IDENTITIES_PRESERVED=3
    HISTORICAL_TWO_DUPLICATE_063_FILES=EXACT_HASH_PRESERVED

The new V03 runner called the existing header and PKA declaration parsers, not a new experimental approximation. Both original audit JSON files were hash-checked before V03 execution. The 113 source-typed tokens preserve separate reference/provenance grammar slots and exact original Git source lines with SHA-256. A token absent from the sampled 65 is not declared non-existent in the broader repository. No parsed source status was promoted into governing authority.

The message identity guard now checks every MC thread's actual numbered Markdown message filenames, not only STATE.json coherence. Exactly two historical MC-0030 Message 063 claimants are permitted if and only if their exact names **and** SHA-256 values match. The guard rejects new collisions, third-claimant 063, changed historical bytes and cross-identity contamination; cross-thread matching numbers remain legal.

Focused V03 native-source audit, original collaboration coherence and new collision tests: **41/41 PASS** (7.20 seconds, no pytest cache). A first synthetic source-witness test erroneously used a Spec028 *header* token as though it were in its structured JSON declaration. The test fixture alone was corrected to a real structured `research:176` token and rerun; saved V03 source result and parser unchanged.

## Observed integrated precommit verification

The original large combined historical regression invocation timed out without a verdict twice under the maximum 30-second command ceiling. **Neither timeout was counted as success.** The same selected test files were then run in bounded isolated groups with no cache, and every group returned a recorded successful pytest verdict:

| Actual check group | Result |
| --- | --- |
| V03 native grammar, prospective message collision guard and prior MC state tests | **41/41 PASS** (5.60 s latest) |
| V01/V02 exact historical provenance audit and repair tests | **13/13 PASS** (15.37 s) |
| Previous paraphrase and directed relation query tests | **13/13 PASS** (7.78 s) |
| Earlier hybrid and 65-heading retrieval tests | **11/11 PASS** (6.68 s) |
| Original legacy topical and B2 proxy retrieval tests | **8/8 PASS** (6.42 s) |
| Restricted C02 evidence-boundary/source-free result identity tests | **15/15 PASS** (0.23 s) |
| **All executed focused tests across six disjoint batches** | **101/101 PASS** |

Additional actual validators:
- `scripts/check_model_collaboration_state.py`: **PASS** for 28 guarded model-collaboration states plus the newly integrated source-file numeric message uniqueness check; historic exact-identity MC-0030/063-A/B exception only.
- `scripts/check_current_routing.py`: **PASS**, Checkpoint **912**, branch `v1-source-vault-bootstrap-resume`, current boundary `p-three-native-grammar-and-message-identity-guarded`, formal outcome `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, research index **649**, checkpoint count **913** (000–912), 19 mapped topics.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **913/913** canonical numbered checkpoints compliant.
- `git check-attr text` on the actual V03 JSON output: **unset**, preserving exact source evidence bytes.
- `git diff --check`: exit **0**, routine tracked text LF/CRLF worktree warnings only.
- Family-aware repository contracts: **PASS**, separately executed as well as in the aggregate.
- Project Knowledge worktree snapshot validator: `ok=true`, zero diagnostics/deferred checks, separately executed.
- The first aggregate `scripts/check_repository_integrity.py` attempt timed out without a verdict; the second completed with **PUBLIC_REPOSITORY_INTEGRITY=PASS**, independently confirming family-aware contracts, Project Knowledge, checkpoint metadata, Knowledge Map, model collaboration and routing.

No official P03 source/gold admission, semantic governing relation score, B0–B4 selection, real physical target decision, or private C01/C02 access is implied. Git commit/push/remote publication will be verified separately and must not be inferred from these precommit checks.
