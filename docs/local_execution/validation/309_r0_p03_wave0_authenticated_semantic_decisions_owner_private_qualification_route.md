# Validation 309: Owner-authenticated Wave0 decisions and protected scientific review route

**Date:** 2026-11-09
**Status:** REAL_SEMANTIC_CMS_OWNER_VERIFY_PASS / SOURCE_FREE_OWNER_PRIVATE_REVIEW_CODE_QUALIFIED / REAL_REVIEW_PENDING_OWNER
**Research:** 624, 623, 622; **Prior validation:** 304–308.
**Scope:** Preserve the actual owner-side semantic CMS verification and qualify a targeted, offline owner-private review of all ten proposals against all earlier source evidence. No public source-specific findings or automatic source admissions.
**Specification:** 028 unchanged. **Checkpoint:** 898 unchanged.

## 1. Owner's real authenticated readback

The owner supplied:

```text
S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_READBACK=PASS
S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_RECHECK=PASS
PS C:\Projects_Data\autonomous-data-science-system>
```

This is one owner `-Action Verify` call with two nested fixed PASS markers, not multiple scientific reviews. The authenticated ten-record report is now recoverable and exactly source-bound to the earlier historical source ZIP, complete paired original first-pass reasoning and substantive adversarial challenge (Validation 308). The owner did **not** supply the earlier standalone `Receive` marker or independently pasted downloaded-file hash. However, successful `Verify` implies a saved encrypted report and receipt have survived exact digest and CMS authenticated readback.

The separate adjudicator had reported `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms` as 51,235 bytes with SHA-256 `8868f308c2e4273eb06726705985bfb12a06a9ddff94a9b25e1f31018bc3fa78`. No source-path-to-status decisions, reasoned claims or category counts were disclosed to the coordinating chat.

## 2. Implemented owner-local review

New `experiments/r0_p03_navigation_probe/s1_wave0_owner_private_decision_review.py` generates one human-readable, source-complete Markdown review in the existing owner ACL-protected location, using `-Action Review` added to `scripts/r0_p03_s1_owner_wave0_semantic_adjudication.ps1`.

The script:
- Checks the existing owner-protected folder, actual historical source archive and prior CMS identities using the existing bounded PowerShell control plane.
- Validates existing owner receipt and exact packet/CMS hashes before the review path.
- Prompts the actual owner for an explicit **`GENERATE PRIVATE WAVE0 REVIEW`** confirmation and the existing key passphrase via local interactive console.
- Reauthenticates CMS with the pre-existing private key, revalidates the canonical ten-record decisions against the exact source packet and never emits private findings to the terminal.
- Writes one no-overwrite `R0_P03_S1_WAVE0_OWNER_PRIVATE_DECISION_REVIEW.md` file, with all ten original source texts where UTF-8-renderable, both prior full first-pass records, complete adversarial challenge, proposed adjudicator decision and owner review prompts.
- Does not silently pretend that unsupported source representations were read. Original bytes remain present in the owner-protected source ZIP for separate inspection where needed. Markdown content is enclosed inside dynamically sized literal code fences to avoid interpreting source-provided Markdown as executable markup. Its exact source-specific proposal counts are intentionally **inside the private file**, not in public status.
- Returns fixed-safe counts, Markdown file size/digest and `owner_scientific_acceptance=PENDING`, `author_release=NONE`, without printing any path-to-decision mapping.

Creating this review document is a new restricted plaintext local file. It is intentionally opt-in and distinct from opening the prior ciphertext. Do not attach this file to this coordinating conversation, public GitHub, connected apps or future blind experimental roles.

The existing action semantics `SelfTest/Export/VerifyExport/Receive/Verify` are preserved; only the new `Review` action and harmless `SelfTest` module import are added. No real protected owner reports were opened or exported via the Runtime Bridge.

## 3. Measured source-free qualification

Using ten **invented** historical source blobs, fabricated original first passes, fictional adversarial claims and semantic proposals, and a disposable encrypted RSA key:

- Synthetic full review generation reproduced each source's original bytes and all three earlier/private evidence layers plus ten proposed outcomes.
- Output stayed in a no-overwrite path in the same test-owner directory, and source-specific findings were not printed as tool receipts.
- Wrong CMS SHA-256 and wrong owner passphrase produced fixed-safe holds, without creating the review.
- Embedded Markdown fence delimiters were treated as inert literal source text, not an interpreted Markdown boundary.
- The owner PowerShell wrapper required explicit local confirmation, made a separate module help import available in `SelfTest`, and exposed only a fixed output marker for private review creation.

**Observed outcomes:** Focused original-plus-review suite **24/24 PASS**, integrated original, independent, adversarial, semantic and owner-review suites **39/39 PASS**. PowerShell AST: PASS on the expanded owner wrapper. These synthetic tests show implementation integrity, not scientific truth or an accepted status for any real Wave0 source.

## 4. Bounded continuation

Next owner-local action: from an ordinary interactive PowerShell, use the **same recipient ID** with:

```powershell
& .\scripts\r0_p03_s1_owner_wave0_semantic_adjudication.ps1 -Action Review -RecipientId $recipientId
```

This requests explicit local plaintext creation confirmation and the owner encrypted-key passphrase, then generates one private review file. Its contents should be inspected in a local editor, and source-specific qualifications/contests/HOLDs kept in owner-private custody. The file alone is **not** owner acceptance or a source release. Actual scientific decisions must be grounded in exact evidence and separately recorded. Source/world decisions should be followed by a risk-based historical source-family coverage study and the prospective primary 12/legacy 9 task/reference/arm experiment rather than another blanket Wave0 reviewer cycle.

```text
VALIDATION_309=OWNER_SEMANTIC_CMS_AUTHENTICATED_AND_PRIVATE_REVIEW_ROUTE_QUALIFIED
OWNER_REAL_SEMANTIC_VERIFY=PASS
OWNER_PRIVATE_SOURCE_DECISIONS=NOT_EXPOSED
OWNER_PRIVATE_REVIEW_REAL_GENERATION=NOT_YET_EXECUTED
SOURCE_FREE_FOCUSED_SYNTHETIC_TESTS=24_OF_24_PASS
SOURCE_FREE_INTEGRATED_SYNTHETIC_TESTS=39_OF_39_PASS
OWNER_POWERSHELL_AST=PASS
OWNER_SCIENTIFIC_ACCEPTANCE=PENDING
AUTHOR_RELEASE=NONE
SOURCE_AUTHOR_ADMISSIONS=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
