# Research 623: Owner-authorized finite Wave0 semantic decisions and experiment-facing source closure

**Date:** 2026-11-09
**Status:** OWNER_AUTHORIZED_NEW_NON_ARM_ADJUDICATOR / PROTECTED_DECISION_TRANSPORT_PREPARED / NO_REAL_ADJUDICATION_YET
**Scope:** Convert three authenticated real Wave0 source-status evidence layers into a narrowly bounded source-specific decision register with ten grounded proposed decisions or justified HOLDs. Preserve the separate role and protected evidence context while keeping R0-P03 B0–B4 execution as the actual scientific goal.
**Basis:** Research 513, 559, 576, 590–591, 620–622; Validation 293–304.
**Authority:** Explicit owner authorization in conversation, "Yes, I authorize.", in direct answer to the question granting **one separate non-arm semantic adjudicator** access to the same ten original sources, the two original complete first-pass assessments and the recently authenticated adversarial challenge. It is not permission to release source data to primary authors or scorers, and is not permission to expand beyond the ten original files.
**Specification:** 028 unchanged. **Checkpoint:** 898 unchanged.

## 1. Why this is distinct from earlier reviews

The first source-status reviewer and independently blind second first-pass challenger proposed source status for ten pinned original historical source files, then a separate non-arm adversarial challenger reviewed all ten and their two complete rationales. The owner independently authenticated all existing protected reports, including the adversarial challenge CMS (Validation 304). The repository coordinator knows only source-free status receipts, fixed ciphertext digests, and schema/protocol details, not any source-specific dispositions or reasoning.

The unresolved scientific question is not whether a model can repeatedly authenticate CMS files. It is whether a qualified, separately role-isolated source-status decision maker can ground an actual source eligibility/disclosure determination in each original source and the strongest substantive objections, or justify a **source-bound HOLD**. The new owner decision authorizes exactly that restricted evidence transfer.

A complete reviewer/counterargument report does not automatically imply that any source qualifies for a future blind author. In particular, a historical file can have limited reference authority, missing governing linked context, unverified media, or old architecture/gold leakage despite apparent agreement between earlier reviewers.

## 2. Exact restricted evidence and recipient

Only one newly assigned **NON-ARM_SOURCE_STATUS_SEMANTIC_ADJUDICATOR** may receive:
- the exact ten original source files from the pinned historical source ZIP SHA-256 `c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387`;
- both complete earlier private first-pass reasoning and paired evidence, derived from original reviewer CMS SHA-256 `9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366`, independent first-pass CMS SHA-256 `50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64`, and owner-paired comparison CMS SHA-256 `f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3`;
- the new owner-authenticated adversarial report, received as AES-256-GCM CMS SHA-256 `e2d2c31d0486b9314b1d5902776da866397cb092963ac75c95e7b5c6f313ac03`, reported size 49,653 bytes;
- a public certificate for encrypting the new result, a source-bound manifest, submission code, and focused decision instructions.

The first two reviews, comparison and adversarial challenge remain immutable source evidence. This is not a new first pass and the adjudicator is not blind to prior conclusions. The separate adjudicator must not be the former challenger, future author, scorer, reference writer, arm engineer or exposed public coordinator. A fresh Temporary Chat without connected apps is the practicable Level B role boundary, not a formal proof of model/provider isolation. The provider will receive the plaintext evidence voluntarily uploaded by the owner.

## 3. Finite semantic decision contract

Each of exactly ten original source records requires a grounded source and version identity; actual original file and previous-reasoning inspection; historical authority; supported/disputed/unproven prior evidence; strongest counterinterpretation; **claim materiality** and **author-disclosure materiality** independently; missing representations/evidence; a specific decision; supporting rationale; falsification/closure trigger; and an explicit necessary next action.

The only proposed outcomes:
- `PROSPECTIVE_WHOLE_FILE_CANDIDATE`: potentially acceptable **after further independent source-world and co-exposure qualification**; does **not** admit or release it.
- `AUXILIARY_ONLY_EXCLUDED_FROM_AUTHOR`: useful for owner/non-scored evidence, excluded from author-facing source world.
- `PROHIBIT_AUTHOR_EXPOSURE`: grounded design/gold/leakage or other confirmed reason to prohibit author consumption.
- `HOLD_FOR_MATERIAL_EVIDENCE`: essential evidence/context unavailable, not silently resolved. The report must name a concrete next step or justified unavailability.

The schema permanently sets `author_release=NONE`, `source_world=WORLD_UNFROZEN`, `record_status=PROPOSED_DECISIONS_REQUIRE_OWNER_QUALIFICATION`, even for a whole-file candidate. No final author admission or scored gold can be inferred from an encrypted or owner-verified candidate decision.

**Stop criterion for Wave0 adjudication:** a real, owner-recovered, source-bound proposed decision/HOLD register for all ten with explicit status and materiality arguments, plus owner qualification and documented unresolved next actions; no additional generic reviewer loop unless a specific material gap warrants it. Finite success does not require every HOLD to become acceptance.

## 4. Purpose-specific protected implementation

- `experiments/r0_p03_navigation_probe/s1_wave0_semantic_adjudication_packet.py` reauthenticates all four fixed owner CMS objects and their exact source versions under the owner's existing encrypted key, reconstructs the prior challenger input and paired evidence in memory, validates the new challenge report's ten source identities and schema, and creates one deterministic, no-overwrite **restricted plaintext ZIP** in the existing ACL-protected owner directory. Separate `VerifyExport` independently reauthenticates/recomputes exact packet bytes.
- `experiments/r0_p03_navigation_probe/s1_wave0_semantic_decision_report.py` is a fully standalone recipient-side schema/CMSEncrypt and owner-authenticated readback module. It can be used from a third-party Temporary Chat with only the new packet and OpenSSL; its `seal` function needs only the public certificate.
- `scripts/r0_p03_s1_owner_wave0_semantic_adjudication.ps1` wraps `SelfTest`, `Export`, `VerifyExport`, `Receive`, and `Verify`. The current original owner recipient ID and encrypted key are reused, never exported. A new plaintext packet is created only after an additional interactive user confirmation. Both the new owner packet and returned CMS use strict no-overwrite semantics.
- `experiments/r0_p03_navigation_probe/S1_WAVE0_SEMANTIC_ADJUDICATION_HANDOFF_V01.md` defines the exact local commands, the qualified non-arm adjudicator prompt, source-access limits and later encrypted owner intake.

**Public-tool boundary:** Only code, synthetic tests, protocol and source-free status go into Git. The public Runtime Bridge must never be used to decrypt owner inputs, create the actual restricted packet or store external source-specific decisions.

## 5. Evidence and next milestone

The full new route was exercised only on fabricated ten-source manifests, invented three-stage reviews, disposable encrypted RSA key and fabricated decisions. Real OpenSSL AES-256-GCM CMS decrypt/encrypt and structural source bindings are tested, along with negative cases such as tampered prior challenger CMS, packet mutation, wrong passphrase/certificate, missing records, unsupported auto-release and unjustified HOLD. The existing source status and challenge suites remain the regression baseline. **No synthetic source decision is a conclusion about the actual ten historical sources.**

Once the owner generates and independently verifies the restricted packet locally, it is to be supplied personally to **one separate non-arm adjudicator**. That adjudicator must return a genuine owner-encrypted ten-decision report and a safe size/hash receipt. Owner `Receive` and independent `Verify` recover that evidence and keep the source-specific rationale outside the public coordinator.

After source-grounded decision qualification, proceed to a **prospective task-independent risk-based source-family closure** for the broader historical population, honest exclusion/abstention for unresolved material omissions, and then the actual twelve primary tasks, separately neutralized nine legacy cases, private independent reference packet, prospective 60/20 split and fair Level B five-arm comparison under Research 513. Do not impose identical manual three-actor reviews on all 2,133 records without actual demonstrated need, and do not retrospectively change source access based on scoring results.

```text
RESEARCH_623=OWNER_AUTHORIZED_SEPARATE_NON_ARM_SEMANTIC_ADJUDICATION
EXACT_ORIGINAL_SOURCE_COUNT=10
FOUR_OWNER_CMS_OBJECTS=PREVIOUSLY_AUTHENTICATED
REAL_PRIVATE_ADJUDICATION_PACKET=NOT_YET_CREATED
ADJUDICATOR_SOURCE_DECISIONS=NOT_YET_AUTHORED
OWNER_FINAL_ACCEPTANCE=NOT_YET_QUALIFIED
SOURCE_AUTHOR_ADMISSIONS=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
