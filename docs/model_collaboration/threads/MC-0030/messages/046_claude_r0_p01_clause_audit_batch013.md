# MC-0030 Message 046: Claude independent clause audit, batch Q0-AUDIT-013 (REV04 outcome policy, leaves successor_proposal (rest) … webauthn_assertion_failure_table)

```text
Thread                  MC-0030
Message                 046
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             32d43287f1195d2e3c3259b61e479c4b44a92105 (Message 045)
Batch                   Q0-AUDIT-013 / REV04_POLICY / 42 units / REV04_POLICY:successor_proposal.owner_approval .. REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.requires
Batch unit-list SHA-256 2a393606eb0fdd337425a3c61f96a974f22b914a4014398e6aa86732417c015b (recomputed: match)
Source                  docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json
Source SHA-256          9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c (Git blob, matches inventory)
Cross-checked against   REV04 contract (sha 9160a30c...), B01/B02 owner acceptance records, inventory policy_root_classification,
                        Q0 REV02 trace R01-R40/C01-C13, REV03 test catalogue, Messages 033 and 035-052
Disposition             AMEND_AUDIT_BATCH013
Authority               Message 034 (resumed per Research 535 / Checkpoint 871). Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `32d43287…`, my Message 045 (parent `f4a861e5…`, one added file). The receipt checker returned `PASS batches=12/18 units=667/1022 accepted=615 pending=52`.
- All 7 source SHA-256 values still equal the inventory; the approved REV04 contract/policy hashes (`9160a30c…`, `9b5bbc4d…`) are unchanged; the inventory hash equals the plan; all 18 unit-list hashes recompute. My nine committed records (033, 035–042) and Message 052 are byte-identical at the new HEAD and were not re-audited.
- Every one of the 42 units was resolved from the committed policy JSON by the inventory's own leaf-walk rule (sorted keys, `.key` / `[i]` paths, keys may themselves contain dots) and its canonical-JSON `text_sha256` recomputed: 42/42 match.
- Source is the B01/B02-approved REV04 outcome policy. As in Messages 040–042 (convention B07-S1), `INH*` = INHERITED_UNCHANGED meaning **approved successor text carried into F1 unchanged**. `N/A` (NOT_APPLICABLE_TO_SUCCESSOR, IDs `-`) is used only for leaves under roots the inventory itself classifies NON_NORMATIVE **and** whose content imposes no successor obligation; each states its reason.
- Each leaf was read as a machine rule: is the value unambiguous, consistent with the contract sentence it encodes, mapped to C/R rule text, and testable? `R4:` = REV04_CONTRACT line; `P:` = another REV04_POLICY leaf. This batch completes REV04_POLICY: 237/237 leaves reviewed across batches 010–013.

## 1. Verdict

**`AMEND_AUDIT_BATCH013`**: 42/42 reviewed; **39 ACCEPTED, 3 PENDING** (2 of the accepted rows are NOT_APPLICABLE_TO_SUCCESSOR).

This batch contains the unchanged eligibility thresholds, the canonical blocker list and the WebAuthn assertion-failure table.

- **Thresholds.** All 15 `unchanged_eligibility` values equal R4:L0014 and V02:L0288/L0333: 100 / 90 / 60 / 120 / 120 / 0 / false / 13 / L01 / S01–S03 / 10 / 15 / B.
- **Blocker list.** I compared `unresolved_blockers` mechanically with the ten §11 bullet IDs (R4:L0289–L0298). The match is exact, in the same order, 10/10, which satisfies the byte-equality requirement of R4:L0276/L0287.
- **WebAuthn table.** The NotAllowedError/cancel/timeout row and the "other client error" row match R4:L0199–L0201.

**B13-F1. B05-A1 is sharper here: a NotSupportedError *at assertion* maps to NOT_REALIZABLE.**

- The table is `webauthn_assertion_failure_table`. Its NotSupportedError row assigns `outcome = CAPABILITY_NOT_REALIZABLE` and `proof_viability_receipt = NOT_REALIZABLE`, on condition of a "frozen_signed_or_local_independent_capability_receipt".
- An assertion happens only *after* a registration that already proved ES256 + UV capability (V02:L0258). A NotSupportedError at that stage is therefore more plausibly a client or RP fault than a platform incapacity.
- Under G1, a NOT_REALIZABLE label for Arm B can turn an INVALID_INCOMPLETE run into REOPEN.
- The receipt is also undefined: "signed" by whom, and "local independent" relative to what.
- The closed predicate required by B05-A1 must state explicitly whether assertion-time NotSupportedError after a verified registration can ever qualify. These three leaves stay PENDING under B05-A1. I do not propose which answer governs.

Non-blocking:

- **B13-R1.** `unchanged_eligibility` is a partial restatement. It lacks "3/3 small successful", "L01 success", the friction-rating domain and field completeness (V02:L0288). It also lacks the narrow infrastructure-receipt exemption that qualifies `small_individual_seconds_lte`. The scorer must take the full predicate from V02:L0288 and V02:L0292–L0304, not from this list alone.
- **B13-R2.** The other-client-error row allows `node_rp_failure` **or** `harness_exception_with_intact_chain`. The class (INVALID_INSTRUMENT) is the same, but `instrument_failure_kind` differs. Freeze the selection rule together with B12-R1.
- **B13-S1 (scope).** The inventory marks `unresolved_blockers` NON_NORMATIVE ("historical design progress"). The contract, however, makes its byte-equality a required check (R4:L0276/L0287), so I keep these ten rows as retained approved text rather than N/A.

## 2. Per-unit audit record (42 units)

Paths are relative to the REV04_POLICY root; receipt IDs carry the full `REV04_POLICY:` prefix.

### `successor_proposal`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `successor_proposal.owner_approval` | `false` | - | N/A | Stale: superseded by the B01/B02 owner acceptance records (R21). Root NON_NORMATIVE. | ACCEPTED |
| `successor_proposal.protocol` | `R0-P01-V01-I1_PROPOSED_UNAPPROVED` | - | N/A | Stale label; the identity R0-P01-V01-I1 is stated normatively at R4:L0020 and accepted in B01. Root NON_NORMATIVE. | ACCEPTED |

### `synthetic_webauthn_test`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `synthetic_webauthn_test` | Chromium CDP/Playwright CTAP2 virtual authenticator is **not** Windows Hello UX | R40, R20 | INH* | R4:L0186. T-WEB-VIRTUAL. | ACCEPTED |

### `unchanged_eligibility`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `unchanged_eligibility.acceptances_projected_max` | `100` | R09 | INH* | R4:L0014, L0100. | ACCEPTED |
| `unchanged_eligibility.final_tiebreak` | `B` | R10 | INH* | R4:L0014; V01_CONTRACT-L0351. | ACCEPTED |
| `unchanged_eligibility.large_seconds_lte` | `120` | R08, R10 | INH* | R4:L0014 (no exception for L01). | ACCEPTED |
| `unchanged_eligibility.large_trial` | `L01` | R08 | INH* | R4:L0012. | ACCEPTED |
| `unchanged_eligibility.manual_metadata_edits_eq` | `0` | R10 | INH* | R4:L0100. | ACCEPTED |
| `unchanged_eligibility.owner_mechanical_minutes_projected_max` | `90` | R09 | INH* | R4:L0014; binds at a median above 5400/97 ≈ 55.670 s (B03-R2). | ACCEPTED |
| `unchanged_eligibility.secret_exposure_eq` | `false` | R10, R19 | INH* | R4:L0100. | ACCEPTED |
| `unchanged_eligibility.security_controls_all_pass` | `13` | R10, C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13 | INH* | All 13 must PASS (R4:L0012). | ACCEPTED |
| `unchanged_eligibility.small_individual_seconds_lte` | `120` | R08 | INH* | Exempt only via the narrow infrastructure receipt (V02:L0292–L0304; B13-R1). | ACCEPTED |
| `unchanged_eligibility.small_median_seconds_lte` | `60` | R08, R10 | INH* | R4:L0014. | ACCEPTED |
| `unchanged_eligibility.small_trials[0]` | `S01` | R08 | INH* | 1 effect. | ACCEPTED |
| `unchanged_eligibility.small_trials[1]` | `S02` | R08 | INH* | 2 effects. | ACCEPTED |
| `unchanged_eligibility.small_trials[2]` | `S03` | R08 | INH* | 4 effects. | ACCEPTED |
| `unchanged_eligibility.tiebreak_large_delta_seconds` | `15` | R10 | INH* | Inclusive ≥ (B05-R2). | ACCEPTED |
| `unchanged_eligibility.tiebreak_small_delta_seconds` | `10` | R10 | INH* | Inclusive ≥ (B05-R2). | ACCEPTED |

### `unresolved_blockers`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `unresolved_blockers[0]` | `B01_FAMILY_G1_G2_INTERPRETATION` | R37, R21 | INH* | Equals the §11 bullet at R4:L0289 (order and bytes). Satisfied by the owner acceptance record; retained for list equality. | ACCEPTED |
| `unresolved_blockers[1]` | `B02_OWNER_POLICY_APPROVAL_BEFORE_FREEZE` | R37, R21 | INH* | Equals the §11 bullet at R4:L0290 (order and bytes). Satisfied by the owner acceptance record; retained for list equality. | ACCEPTED |
| `unresolved_blockers[2]` | `B03_NATIVE_WINDOWS_SSH_AND_ABORT_TESTS` | R37, R21 | INH* | Equals the §11 bullet at R4:L0291 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[3]` | `B04_PRECLAIM_KAT_TRISTATE_VERIFY_AND_FLAGS` | R37, R21 | INH* | Equals the §11 bullet at R4:L0292 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[4]` | `B05_DOMAIN_TEMPLATES_AND_OLD_EVIDENCE_SET` | R37, R21 | INH* | Equals the §11 bullet at R4:L0293 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[5]` | `B06_WEBAUTHN_PREFLIGHT_BROWSER_AND_NODE_INTERRUPT` | R37, R21 | INH* | Equals the §11 bullet at R4:L0294 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[6]` | `B07_CRASH_ATOMIC_SNAPSHOT_AND_OWNER_HEAD_WITNESS` | R37, R21 | INH* | Equals the §11 bullet at R4:L0295 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[7]` | `B08_FULL_SYNTHETIC_COMPOSITION_AND_BRANCHES` | R37, R21 | INH* | Equals the §11 bullet at R4:L0296 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[8]` | `B09_OWNER_CONSENT_AND_R1_REQUIREMENTS` | R37, R21 | INH* | Equals the §11 bullet at R4:L0297 (order and bytes). Open qualification work. | ACCEPTED |
| `unresolved_blockers[9]` | `B10_P03_ORDER_AND_AUTHORITY` | R37, R21 | INH* | Equals the §11 bullet at R4:L0298 (order and bytes). Open qualification work. | ACCEPTED |

### `webauthn_assertion_failure_table`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.event_terminal` | `true` | R07, R11 | INH* | R4:L0199, L0151. | ACCEPTED |
| `webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.outcome` | `WEBAUTHN_ASSERTION_NOT_COMPLETED` | R07 | INH* | R4:L0199. | ACCEPTED |
| `webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.requires` | Durable issued-and-consumed pending assertion receipt bound to the same attempt and acceptance ID | R07, R35 | INH* | R4:L0112, L0154 (a missing receipt is never inferred as cancellation). T-WEB-CANCEL. | ACCEPTED |
| `webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.retry_same_assertion` | `false` | R07, R06 | INH* | R4:L0108 (no failed-assertion retry). | ACCEPTED |
| `webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.run_continues` | `true` | R07, R26 | INH* | R4:L0199 (continue scheduled owner events). | ACCEPTED |
| `webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.valid_proof` | `false` | R07 | INH* | Terminal evidence, not authentication (R4:L0151). | ACCEPTED |
| `webauthn_assertion_failure_table.NotSupportedError.event_terminal` | `false` | R07, R11 | INH* | Correctly not a ceremony terminal outcome; its arm-level consequence is in the leaves below. | ACCEPTED |
| `webauthn_assertion_failure_table.NotSupportedError.outcome` | `CAPABILITY_NOT_REALIZABLE` | R07, R11 | INH* | Assertion-time NotSupportedError after a verified ES256/UV registration (B13-F1); predicate open. | **PENDING** B05-A1 |
| `webauthn_assertion_failure_table.NotSupportedError.proof_viability_receipt` | `NOT_REALIZABLE` | R11 | INH* | Feeds G1 directly (REOPEN versus INVALID_INCOMPLETE). | **PENDING** B05-A1 |
| `webauthn_assertion_failure_table.NotSupportedError.requires` | `frozen_signed_or_local_independent_capability_receipt` | R11, R16 | INH* | Receipt schema, signer and independence basis undefined. | **PENDING** B05-A1 |
| `webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.flag` | `integrity.node_rp_failure_or_integrity.harness_exception_with_intact_chain` | R13, R35 | INH* | R4:L0201. Selection between the two kinds needs freezing (B13-R2). | ACCEPTED |
| `webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.not_owner_cancellation` | `true` | R07 | INH* | R4:L0201 (never simulated cancellation). T-WEB-FAULT. | ACCEPTED |
| `webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.outcome` | `INSTRUMENT` | R13 | INH* | R4:L0201. | ACCEPTED |
| `webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.requires` | Source-labelled client or RP error receipt | R13, R35 | INH* | R4:L0201, L0229. | ACCEPTED |

## 3. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
REV04_POLICY:successor_proposal.owner_approval|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||REV04_POLICY:successor_proposal.owner_approval;reason=predecision_lifecycle_metadata_superseded_by_B01_B02_records
REV04_POLICY:successor_proposal.protocol|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||REV04_POLICY:successor_proposal.protocol;reason=predecision_lifecycle_metadata_identity_at_REV04_CONTRACT-L0020
REV04_POLICY:synthetic_webauthn_test|INHERITED_UNCHANGED|R40,R20|ACCEPTED||REV04_POLICY:synthetic_webauthn_test;REV04_CONTRACT-L0186
REV04_POLICY:unchanged_eligibility.acceptances_projected_max|INHERITED_UNCHANGED|R09|ACCEPTED||REV04_POLICY:unchanged_eligibility.acceptances_projected_max;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.final_tiebreak|INHERITED_UNCHANGED|R10|ACCEPTED||REV04_POLICY:unchanged_eligibility.final_tiebreak;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.large_seconds_lte|INHERITED_UNCHANGED|R08,R10|ACCEPTED||REV04_POLICY:unchanged_eligibility.large_seconds_lte;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.large_trial|INHERITED_UNCHANGED|R08|ACCEPTED||REV04_POLICY:unchanged_eligibility.large_trial;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.manual_metadata_edits_eq|INHERITED_UNCHANGED|R10|ACCEPTED||REV04_POLICY:unchanged_eligibility.manual_metadata_edits_eq;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.owner_mechanical_minutes_projected_max|INHERITED_UNCHANGED|R09|ACCEPTED||REV04_POLICY:unchanged_eligibility.owner_mechanical_minutes_projected_max;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.secret_exposure_eq|INHERITED_UNCHANGED|R10,R19|ACCEPTED||REV04_POLICY:unchanged_eligibility.secret_exposure_eq;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.security_controls_all_pass|INHERITED_UNCHANGED|R10,C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13|ACCEPTED||REV04_POLICY:unchanged_eligibility.security_controls_all_pass;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.small_individual_seconds_lte|INHERITED_UNCHANGED|R08|ACCEPTED||REV04_POLICY:unchanged_eligibility.small_individual_seconds_lte;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.small_median_seconds_lte|INHERITED_UNCHANGED|R08,R10|ACCEPTED||REV04_POLICY:unchanged_eligibility.small_median_seconds_lte;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.small_trials[0]|INHERITED_UNCHANGED|R08|ACCEPTED||REV04_POLICY:unchanged_eligibility.small_trials[0];REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.small_trials[1]|INHERITED_UNCHANGED|R08|ACCEPTED||REV04_POLICY:unchanged_eligibility.small_trials[1];REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.small_trials[2]|INHERITED_UNCHANGED|R08|ACCEPTED||REV04_POLICY:unchanged_eligibility.small_trials[2];REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.tiebreak_large_delta_seconds|INHERITED_UNCHANGED|R10|ACCEPTED||REV04_POLICY:unchanged_eligibility.tiebreak_large_delta_seconds;REV04_CONTRACT-L0014
REV04_POLICY:unchanged_eligibility.tiebreak_small_delta_seconds|INHERITED_UNCHANGED|R10|ACCEPTED||REV04_POLICY:unchanged_eligibility.tiebreak_small_delta_seconds;REV04_CONTRACT-L0014
REV04_POLICY:unresolved_blockers[0]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[0];REV04_CONTRACT-L0289;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[1]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[1];REV04_CONTRACT-L0290;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[2]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[2];REV04_CONTRACT-L0291;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[3]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[3];REV04_CONTRACT-L0292;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[4]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[4];REV04_CONTRACT-L0293;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[5]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[5];REV04_CONTRACT-L0294;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[6]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[6];REV04_CONTRACT-L0295;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[7]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[7];REV04_CONTRACT-L0296;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[8]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[8];REV04_CONTRACT-L0297;REV04_CONTRACT-L0287
REV04_POLICY:unresolved_blockers[9]|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_POLICY:unresolved_blockers[9];REV04_CONTRACT-L0298;REV04_CONTRACT-L0287
REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.event_terminal|INHERITED_UNCHANGED|R07,R11|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.event_terminal;REV04_CONTRACT-L0199
REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.outcome|INHERITED_UNCHANGED|R07|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.outcome;REV04_CONTRACT-L0199
REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.requires|INHERITED_UNCHANGED|R07,R35|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.requires;REV04_CONTRACT-L0154
REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.retry_same_assertion|INHERITED_UNCHANGED|R07,R06|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.retry_same_assertion;REV04_CONTRACT-L0108
REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.run_continues|INHERITED_UNCHANGED|R07,R26|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.run_continues;REV04_CONTRACT-L0199
REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.valid_proof|INHERITED_UNCHANGED|R07|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.valid_proof;REV04_CONTRACT-L0151
REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.event_terminal|INHERITED_UNCHANGED|R07,R11|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.event_terminal;REV04_CONTRACT-L0200
REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.outcome|INHERITED_UNCHANGED|R07,R11|PENDING|B05-A1_ASSERTION_TIME_NOTSUPPORTED_PREDICATE_NOT_ENUMERATED|REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.outcome;REV04_CONTRACT-L0200;REV04_CONTRACT-L0150
REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.proof_viability_receipt|INHERITED_UNCHANGED|R11|PENDING|B05-A1_CAPABILITY_PREDICATE_AND_RECEIPT_NOT_ENUMERATED|REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.proof_viability_receipt;REV04_CONTRACT-L0156
REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.requires|INHERITED_UNCHANGED|R11,R16|PENDING|B05-A1_CAPABILITY_RECEIPT_SCHEMA_SIGNER_UNDEFINED|REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.requires;REV04_CONTRACT-L0108
REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.flag|INHERITED_UNCHANGED|R13,R35|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.flag;REV04_CONTRACT-L0201
REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.not_owner_cancellation|INHERITED_UNCHANGED|R07|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.not_owner_cancellation;REV04_CONTRACT-L0201
REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.outcome|INHERITED_UNCHANGED|R13|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.outcome;REV04_CONTRACT-L0201
REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.requires|INHERITED_UNCHANGED|R13,R35|ACCEPTED||REV04_POLICY:webauthn_assertion_failure_table.other_DOMException_or_client_RP_error.requires;REV04_CONTRACT-L0229
END_AUDIT_RECEIPT
```

Counts: 42 rows; 39 ACCEPTED; 3 PENDING; 0 SUPERSEDED_BY_REV04; 40 INHERITED_UNCHANGED; 2 NOT_APPLICABLE_TO_SUCCESSOR.

## 4. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source value of every unit above (each JSON leaf resolved from the committed blob and its `text_sha256` recomputed). I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited. PENDING items, including the classification-sensitive B05-A1, B07-A3 and B08-A1, remain open for ChatGPT reconciliation and are not resolved here.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE046=CLAUDE_AUDIT_BATCH013
DISPOSITION=AMEND_AUDIT_BATCH013
UNITS_AUDITED=42_OF_42
ACCEPTED=39
PENDING=3
KEY_FINDINGS=B13-F1_ASSERTION_TIME_NotSupportedError_MAPS_TO_NOT_REALIZABLE_(B05-A1);UNRESOLVED_BLOCKERS_EQUAL_SECTION_11_10_OF_10;THRESHOLDS_UNCHANGED
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
