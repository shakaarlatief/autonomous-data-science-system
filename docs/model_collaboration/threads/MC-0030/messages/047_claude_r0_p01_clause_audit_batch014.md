# MC-0030 Message 047: Claude independent clause audit, batch Q0-AUDIT-014 (V01 fixture, leaves arm_ids … owner_trials[3].effects[1] (part))

```text
Thread                  MC-0030
Message                 047
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             c19adcbc9beee81bc8b9f641cb3793c3fd4d931d (Message 046)
Batch                   Q0-AUDIT-014 / V01_FIXTURE / 65 units / V01_FIXTURE:arm_ids.A .. V01_FIXTURE:owner_trials[3].effects[1].effect_id
Batch unit-list SHA-256 de8274848332544b540bb39cb7aa16b7c1420c66a36411957a5c15c692397be7 (recomputed: match)
Source                  experiments/r0_p01_owner_acceptance_v01/fixture.json
Source SHA-256          177dc3d7d071dd4ed2d34bc87f92e33d448e05a475af5c23c97014b928649f68 (Git blob, matches inventory)
Cross-checked against   V02 addendum (C02-C05 field sources, C03 base, C13), V01 implementation/security contracts, REV04 contract,
                        clarification_vectors_v02.json, Q0 REV02 trace, REV03 test catalogue, Messages 033 and 035-046
Disposition             ACCEPT_AUDIT_BATCH014
Authority               Message 034 (resumed per Research 535 / Checkpoint 871). Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `c19adcbc…`, my Message 046 (parent `32d43287…`, one added file). The receipt checker returned `PASS batches=13/18 units=709/1022 accepted=654 pending=55`.
- Source hashes, inventory hash and all 18 unit-list hashes unchanged since Message 043. Every one of the 65 units was resolved from the committed fixture blob by the inventory's leaf-walk rule and its canonical-JSON `text_sha256` recomputed: 65/65 match.
- V01_FIXTURE is inherited source. `INH` = INHERITED_UNCHANGED (retained for the successor fixture, subject to the F1 re-pinning already recorded); `SUP` = superseded by the named REV04 line; `N/A` only with a stated reason. Precedence as before: V02 refines V01 where explicit, and REV04 supersedes both.

**Shared data properties (FX-P1..FX-P8).** I checked these once over the whole committed fixture with a scratch read-only script. Effect-field rows cite them, but each leaf keeps its own receipt row and its own reasoned status.

| ID | Property | Result |
|---|---|---|
| FX-P1 | Trial order and effect counts S01/S02/S03/L01 = 1/2/4/30 (37 effects); each effect has exactly the keys {effect_id, grammar, independently_acceptable, subject, text} | holds 37/37 |
| FX-P2 | `effect_id` = `E-<trial>-<nnn>` with 1-based index; unique | 37/37 unique |
| FX-P3 | `grammar` = `REQUIRE` | 37/37 |
| FX-P4 | `subject` = `SYNTHETIC-SMALL-<nnn>` for S trials, `SYNTHETIC-LARGE-<nnn>` for L01 | 37/37 |
| FX-P5 | `text` = "Synthetic low-consequence governing effect <nnn> for R0-P01 usability and exact-binding qualification." | 37/37 |
| FX-P6 | `independently_acceptable` = `true` | 37/37 |
| FX-P7 | All values printable ASCII; no `|`; canonical JSON reproduces the golden V02 envelope for A/S01 (`b4a274d8…` in clarification_vectors_v02.json uses exactly these S01 fields) | holds |
| FX-P8 | Fixture blob SHA-256 `177dc3d7…` equals the inventory and the `fixture_sha256` bound inside clarification_vectors_v02.json | match |

## 1. Verdict

**`ACCEPT_AUDIT_BATCH014`**: 65/65 reviewed; **65 ACCEPTED, 0 PENDING** (0 of the accepted rows are NOT_APPLICABLE_TO_SUCCESSOR).

This batch covers the arm identities, the canonicalization profile, the three small trials S01/S02/S03 in full, and the start of L01. The fixture is pure data, so the audit question per leaf is narrower: does the value match the role the inherited contracts give it, and does any successor rule change it?

- **Small-trial effects.** All small-trial effect leaves satisfy FX-P1–P6. Their envelope roles are fixed by V02:L0074/L0091 and their view roles by V01_CONTRACT-L0070.
- **Trial metadata.** `class` and `consequence` are correctly *outside* the envelope (V02:L0091). They only steer gate membership and disclosure.
- **No successor conflict.** REV04 changes nothing in this slice of the fixture. Its context and protocol supersessions fall in batch 017.

No PENDING items. Two observations carry forward:

- **B14-R1 (familiarity).** The trial texts are templated and identical to those Attempt 001's owner already saw. If the successor fixture reuses them, practice-effect disclosure is mandatory (R4:L0094, L0247; policy `reporting[9]`). This is not a defect, and it is already governed.
- **B14-R2 (monotone grammar).** Only `REQUIRE` occurs, and `independently_acceptable` is always true. The probe therefore exercises no partial-acceptance or mixed-grammar rendering. That is acceptable for a burden and binding probe, which makes no comprehension claim (R4:L0032), but it must not be cited as evidence about richer future acceptance UX (an R1 concern).

## 2. Per-unit audit record (65 units)

Paths are relative to the fixture root; receipt IDs carry the full `V01_FIXTURE:` prefix. `FX-Pn` cites the shared data properties in §0.

### `arm_ids`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `arm_ids.A` | `"OPENSSH_ED25519_PASSPHRASE_V01"` | R04 | INH | Arm identity retained (V02:L0333; R4:L0089). T-ARM-IDENTITY. | ACCEPTED |
| `arm_ids.B` | `"LOCALHOST_WEBAUTHN_ES256_UV_V01"` | R04 | INH | Arm identity retained (V02:L0333; R4:L0089). T-ARM-IDENTITY. | ACCEPTED |
| `arm_ids.C` | `"CHATGPT_OWNER_USER_ROLE_DIGEST_ATTESTATION_V01"` | R04 | INH | Arm identity retained (V02:L0333; R4:L0089). T-ARM-IDENTITY. | ACCEPTED |

### `canonicalization_profile`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `canonicalization_profile` | `"PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY"` | R01, R36 | INH | Probe-only canonicalization (V01_CONTRACT-L0016; V02:L0066). B02-R2 domain guard. | ACCEPTED |

### `owner_trials`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `owner_trials[0].class` | `"SMALL"` | R08 | INH | Gate membership (small median/max); excluded from the envelope (V02:L0091). | ACCEPTED |
| `owner_trials[0].consequence` | `"LOW"` | R08, R28 | INH | Synthetic low consequence (V01_CONTRACT-L0295); excluded from the envelope; no comprehension claim (R4:L0032). | ACCEPTED |
| `owner_trials[0].effects[0].effect_id` | `"E-S01-001"` | R01, R08 | INH | S01 effect 1; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[0].effects[0].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[1] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[0].effects[0].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[0].effects[0].subject` | `"SYNTHETIC-SMALL-001"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[0].effects[0].text` | Templated effect text 001 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[0].issued_at` | `"2026-10-04T00:01:00Z"` | R01 | INH | Statement `issued_at` source (V02:L0105); provenance only, never order (V02:L0052). | ACCEPTED |
| `owner_trials[0].summary` | `"One-effect synthetic governing acceptance."` | R01, R02 | INH | Envelope and `Summary:` view line (V02:L0074, L0107). | ACCEPTED |
| `owner_trials[0].title` | `"Small owner trial 1"` | R01, R02 | INH | Envelope and `Title:` view line. | ACCEPTED |
| `owner_trials[0].trial_id` | `"S01"` | R01, R08 | INH | Envelope `item_id` and view `Trial:` label (V02:L0107); trial domain (V01_CONTRACT-L0094). | ACCEPTED |
| `owner_trials[1].class` | `"SMALL"` | R08 | INH | Gate membership (small median/max); excluded from the envelope (V02:L0091). | ACCEPTED |
| `owner_trials[1].consequence` | `"LOW"` | R08, R28 | INH | Synthetic low consequence (V01_CONTRACT-L0295); excluded from the envelope; no comprehension claim (R4:L0032). | ACCEPTED |
| `owner_trials[1].effects[0].effect_id` | `"E-S02-001"` | R01, R08 | INH | S02 effect 1; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[1].effects[0].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[1] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[1].effects[0].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[1].effects[0].subject` | `"SYNTHETIC-SMALL-001"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[1].effects[0].text` | Templated effect text 001 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[1].effects[1].effect_id` | `"E-S02-002"` | R01, R08 | INH | S02 effect 2; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[1].effects[1].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[2] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[1].effects[1].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[1].effects[1].subject` | `"SYNTHETIC-SMALL-002"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[1].effects[1].text` | Templated effect text 002 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[1].issued_at` | `"2026-10-04T00:02:00Z"` | R01 | INH | Statement `issued_at` source (V02:L0105); provenance only, never order (V02:L0052). | ACCEPTED |
| `owner_trials[1].summary` | `"Two-effect synthetic governing acceptance."` | R01, R02 | INH | Envelope and `Summary:` view line (V02:L0074, L0107). | ACCEPTED |
| `owner_trials[1].title` | `"Small owner trial 2"` | R01, R02 | INH | Envelope and `Title:` view line. | ACCEPTED |
| `owner_trials[1].trial_id` | `"S02"` | R01, R08 | INH | Envelope `item_id` and view `Trial:` label (V02:L0107); trial domain (V01_CONTRACT-L0094). | ACCEPTED |
| `owner_trials[2].class` | `"SMALL"` | R08 | INH | Gate membership (small median/max); excluded from the envelope (V02:L0091). | ACCEPTED |
| `owner_trials[2].consequence` | `"LOW"` | R08, R28 | INH | Synthetic low consequence (V01_CONTRACT-L0295); excluded from the envelope; no comprehension claim (R4:L0032). | ACCEPTED |
| `owner_trials[2].effects[0].effect_id` | `"E-S03-001"` | R01, R08 | INH | S03 effect 1; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[2].effects[0].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[1] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[2].effects[0].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[2].effects[0].subject` | `"SYNTHETIC-SMALL-001"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[2].effects[0].text` | Templated effect text 001 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[2].effects[1].effect_id` | `"E-S03-002"` | R01, R08 | INH | S03 effect 2; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[2].effects[1].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[2] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[2].effects[1].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[2].effects[1].subject` | `"SYNTHETIC-SMALL-002"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[2].effects[1].text` | Templated effect text 002 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[2].effects[2].effect_id` | `"E-S03-003"` | R01, R08 | INH | S03 effect 3; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[2].effects[2].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[3] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[2].effects[2].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[2].effects[2].subject` | `"SYNTHETIC-SMALL-003"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[2].effects[2].text` | Templated effect text 003 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[2].effects[3].effect_id` | `"E-S03-004"` | R01, R08 | INH | S03 effect 4; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[2].effects[3].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[4] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[2].effects[3].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[2].effects[3].subject` | `"SYNTHETIC-SMALL-004"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. The same subject string recurs across S01/S02/S03, but effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[2].effects[3].text` | Templated effect text 004 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[2].issued_at` | `"2026-10-04T00:03:00Z"` | R01 | INH | Statement `issued_at` source (V02:L0105); provenance only, never order (V02:L0052). | ACCEPTED |
| `owner_trials[2].summary` | `"Four-effect synthetic governing acceptance."` | R01, R02 | INH | Envelope and `Summary:` view line (V02:L0074, L0107). | ACCEPTED |
| `owner_trials[2].title` | `"Small owner trial 3"` | R01, R02 | INH | Envelope and `Title:` view line. | ACCEPTED |
| `owner_trials[2].trial_id` | `"S03"` | R01, R08 | INH | Envelope `item_id` and view `Trial:` label (V02:L0107); trial domain (V01_CONTRACT-L0094). | ACCEPTED |
| `owner_trials[3].class` | `"LARGE"` | R08 | INH | Gate membership (L01 ≤120 s); excluded from the envelope (V02:L0091). | ACCEPTED |
| `owner_trials[3].consequence` | `"LOW"` | R08, R28 | INH | Synthetic low consequence (V01_CONTRACT-L0295); excluded from the envelope; no comprehension claim (R4:L0032). | ACCEPTED |
| `owner_trials[3].effects[0].effect_id` | `"E-L01-001"` | R01, R08 | INH | L01 effect 1; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[3].effects[0].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[1] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[3].effects[0].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[3].effects[0].subject` | `"SYNTHETIC-LARGE-001"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. Unique within L01 (`SYNTHETIC-LARGE-<nnn>`); effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[3].effects[0].text` | Templated effect text 001 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[3].effects[1].effect_id` | `"E-L01-002"` | R01, R08 | INH | L01 effect 2; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |

## 3. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
V01_FIXTURE:arm_ids.A|INHERITED_UNCHANGED|R04|ACCEPTED||V01_FIXTURE:arm_ids.A;V02_ADDENDUM-L0333
V01_FIXTURE:arm_ids.B|INHERITED_UNCHANGED|R04|ACCEPTED||V01_FIXTURE:arm_ids.B;V02_ADDENDUM-L0333
V01_FIXTURE:arm_ids.C|INHERITED_UNCHANGED|R04|ACCEPTED||V01_FIXTURE:arm_ids.C;V02_ADDENDUM-L0333
V01_FIXTURE:canonicalization_profile|INHERITED_UNCHANGED|R01,R36|ACCEPTED||V01_FIXTURE:canonicalization_profile;V02_ADDENDUM-L0066
V01_FIXTURE:owner_trials[0].class|INHERITED_UNCHANGED|R08|ACCEPTED||V01_FIXTURE:owner_trials[0].class;V02_ADDENDUM-L0091;V01_CONTRACT-L0290
V01_FIXTURE:owner_trials[0].consequence|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_FIXTURE:owner_trials[0].consequence;V01_CONTRACT-L0295;REV04_CONTRACT-L0032
V01_FIXTURE:owner_trials[0].effects[0].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[0].effects[0].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[0].effects[0].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[0].effects[0].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[0].effects[0].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[0].effects[0].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[0].effects[0].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[0].effects[0].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[0].effects[0].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[0].effects[0].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[0].issued_at|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[0].issued_at;V02_ADDENDUM-L0105
V01_FIXTURE:owner_trials[0].summary|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[0].summary;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[0].title|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[0].title;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[0].trial_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[0].trial_id;V02_ADDENDUM-L0107;V01_CONTRACT-L0094
V01_FIXTURE:owner_trials[1].class|INHERITED_UNCHANGED|R08|ACCEPTED||V01_FIXTURE:owner_trials[1].class;V02_ADDENDUM-L0091;V01_CONTRACT-L0290
V01_FIXTURE:owner_trials[1].consequence|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_FIXTURE:owner_trials[1].consequence;V01_CONTRACT-L0295;REV04_CONTRACT-L0032
V01_FIXTURE:owner_trials[1].effects[0].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[0].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[1].effects[0].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[0].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[1].effects[0].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[0].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[1].effects[0].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[0].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[1].effects[0].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[0].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[1].effects[1].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[1].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[1].effects[1].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[1].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[1].effects[1].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[1].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[1].effects[1].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[1].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[1].effects[1].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[1].effects[1].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[1].issued_at|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[1].issued_at;V02_ADDENDUM-L0105
V01_FIXTURE:owner_trials[1].summary|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[1].summary;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[1].title|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[1].title;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[1].trial_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[1].trial_id;V02_ADDENDUM-L0107;V01_CONTRACT-L0094
V01_FIXTURE:owner_trials[2].class|INHERITED_UNCHANGED|R08|ACCEPTED||V01_FIXTURE:owner_trials[2].class;V02_ADDENDUM-L0091;V01_CONTRACT-L0290
V01_FIXTURE:owner_trials[2].consequence|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_FIXTURE:owner_trials[2].consequence;V01_CONTRACT-L0295;REV04_CONTRACT-L0032
V01_FIXTURE:owner_trials[2].effects[0].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[0].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[0].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[0].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[0].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[0].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[0].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[0].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[0].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[0].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[2].effects[1].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[1].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[1].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[1].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[1].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[1].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[1].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[1].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[1].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[1].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[2].effects[2].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[2].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[2].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[2].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[2].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[2].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[2].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[2].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[2].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[2].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[2].effects[3].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[3].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[3].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[3].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[3].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[3].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[2].effects[3].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[3].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[2].effects[3].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[2].effects[3].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[2].issued_at|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[2].issued_at;V02_ADDENDUM-L0105
V01_FIXTURE:owner_trials[2].summary|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].summary;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[2].title|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[2].title;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[2].trial_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[2].trial_id;V02_ADDENDUM-L0107;V01_CONTRACT-L0094
V01_FIXTURE:owner_trials[3].class|INHERITED_UNCHANGED|R08|ACCEPTED||V01_FIXTURE:owner_trials[3].class;V02_ADDENDUM-L0091;V01_CONTRACT-L0290
V01_FIXTURE:owner_trials[3].consequence|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_FIXTURE:owner_trials[3].consequence;V01_CONTRACT-L0295;REV04_CONTRACT-L0032
V01_FIXTURE:owner_trials[3].effects[0].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[0].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[0].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[0].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[0].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[0].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[0].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[0].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[0].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[0].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[3].effects[1].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[1].effect_id;FX-P2;V02_ADDENDUM-L0091
END_AUDIT_RECEIPT
```

Counts: 65 rows; 65 ACCEPTED; 0 PENDING; 0 SUPERSEDED_BY_REV04; 65 INHERITED_UNCHANGED; 0 NOT_APPLICABLE_TO_SUCCESSOR.

## 4. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source value of every unit above (each JSON leaf resolved from the committed blob and its `text_sha256` recomputed). I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited. PENDING items, including the classification-sensitive B05-A1, B07-A3 and B08-A1, remain open for ChatGPT reconciliation and are not resolved here.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE047=CLAUDE_AUDIT_BATCH014
DISPOSITION=ACCEPT_AUDIT_BATCH014
UNITS_AUDITED=65_OF_65
ACCEPTED=65
PENDING=0
KEY_FINDINGS=FIXTURE_DATA_PROPERTIES_FX-P1_TO_FX-P8_HOLD;NO_PENDING;B14-R1_FAMILIARITY_DISCLOSURE;B14-R2_MONOTONE_GRAMMAR
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
