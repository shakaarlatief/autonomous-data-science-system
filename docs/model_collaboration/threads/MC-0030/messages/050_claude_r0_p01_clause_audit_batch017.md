# MC-0030 Message 050: Claude independent clause audit, batch Q0-AUDIT-017 (V01 fixture, end of L01 and fixture root fields)

```text
Thread                  MC-0030
Message                 050
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             6bdaf746a3ea0edb3d7d7993ea7182768157d4f7 (Message 049)
Batch                   Q0-AUDIT-017 / V01_FIXTURE / 59 units / V01_FIXTURE:owner_trials[3].effects[27].grammar .. V01_FIXTURE:wrong_project_id
Batch unit-list SHA-256 869cb8ba73dd79a780a41ef16e5eb3e944a39744bb9d65bd1609dc88fa34fd20 (recomputed: match)
Source                  experiments/r0_p01_owner_acceptance_v01/fixture.json
Source SHA-256          177dc3d7d071dd4ed2d34bc87f92e33d448e05a475af5c23c97014b928649f68 (Git blob, matches inventory)
Cross-checked against   V02 addendum (C02-C05 field sources, C03 base, C13), V01 implementation/security contracts, REV04 contract,
                        clarification_vectors_v02.json, Q0 REV02 trace, REV03 test catalogue, Messages 033 and 035-049
Disposition             ACCEPT_AUDIT_BATCH017
Authority               Message 034 (resumed per Research 535 / Checkpoint 871). Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `6bdaf746…`, my Message 049 (parent `8510b04e…`, one added file). The receipt checker returned `PASS batches=16/18 units=904/1022 accepted=849 pending=55`.
- Source hashes, inventory hash and all 18 unit-list hashes unchanged since Message 043. Every one of the 59 units was resolved from the committed fixture blob by the inventory's leaf-walk rule and its canonical-JSON `text_sha256` recomputed: 59/59 match.
- V01_FIXTURE is inherited source. `INH` = INHERITED_UNCHANGED (retained for the successor fixture, subject to the F1 re-pinning already recorded); `SUP` = superseded by the named REV04 line; `N/A` only with a stated reason. Precedence as before: V02 refines V01 where explicit, and REV04 supersedes both.
- Batch-specific checks, all read-only on the committed fixture:
  - **B17-P1:** the ordinary semantic base built from `grammar_version`, `predicate_semantics_version` and BASE-A/BASE-B (sorted, four fields each) recomputes to `76a7391fafd9683566f011be522dd4c3bfbe6bcfb0f1963500d1776b77b4d7a6`, equal to V02:L0125 and to the value in clarification_vectors_v02.json. The C08 mutation gives `164ca4c0…`. Adding `source_revision` would give `3543688e…`.
  - **B17-P2:** `security_controls[0..12]` equal the trace `security_control_key_bindings` C01–C13 and the V01_CONTROLS headings 1–13 in order (13/13).
  - **B17-P3:** `webauthn.port` 8765 agrees with `webauthn.origin`. All nine RP parameters are consistent with R4:L0108 and V02:L0256 (port via the origin).

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

**`ACCEPT_AUDIT_BATCH017`**: 59/59 reviewed; **59 ACCEPTED, 0 PENDING** (0 of the accepted rows are NOT_APPLICABLE_TO_SUCCESSOR).

This batch closes L01 and audits the fixture's root fields:

- the end of L01, effects 28–30;
- L01 metadata;
- `project_id` and `wrong_project_id`;
- `protocol` and `statement_context`;
- `renderer_profile`, `schema_version`, `signer_set_version` and `ssh_namespace`;
- the 13 security-control keys;
- the semantic base;
- the WebAuthn RP parameters.

Two fields are superseded by REV04:

- **`protocol`** is superseded by R0-P01-V01-I1 (R4:L0020).
- **`statement_context`** is superseded by `ADS-R0-P01-002-OWNER-ACCEPTANCE-V01` (R4:L0025). The old context survives only as negative replay material (R4:L0132, L0263).

Everything else is retained. The semantic base and control ordering were independently recomputed (B17-P1, B17-P2), not taken from the stored vectors.

No PENDING items. Two observations:

- **B17-R1 (name collision, non-blocking).** The fixture value `semantic_base.grammar_version = "G1"` is unrelated to REV04's Research-513 "G1/G2" incomplete-evidence interpretation (R4:L0020) and to policy G1. F1 text and tests should always qualify which "G1" they mean. This is not a semantic conflict, because the fields never meet.
- **B17-R2 (golden-vector consequence, already governed).** Successor re-pinning changes the fixture bytes (`protocol`, `statement_context`), so `fixture_sha256` and every V02 golden envelope/statement vector that embeds `ADS-GOVERNING-ACCEPTANCE/v1` cannot be reused as positive successor vectors. R4:L0035 already requires independent re-freezing. Those V02 vectors become old-context negatives.

The open campaign items B05-A1, B07-A3 and B08-A1 are unaffected by fixture data and remain open for reconciliation.

## 2. Per-unit audit record (59 units)

Paths are relative to the fixture root; receipt IDs carry the full `V01_FIXTURE:` prefix. `FX-Pn` cites the shared data properties in §0.

### `owner_trials`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `owner_trials[3].effects[27].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[28] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[3].effects[27].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[3].effects[27].subject` | `"SYNTHETIC-LARGE-028"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. Unique within L01 (`SYNTHETIC-LARGE-<nnn>`); effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[3].effects[27].text` | Templated effect text 028 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[3].effects[28].effect_id` | `"E-L01-029"` | R01, R08 | INH | L01 effect 29; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[3].effects[28].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[29] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[3].effects[28].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[3].effects[28].subject` | `"SYNTHETIC-LARGE-029"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. Unique within L01 (`SYNTHETIC-LARGE-<nnn>`); effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[3].effects[28].text` | Templated effect text 029 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[3].effects[29].effect_id` | `"E-L01-030"` | R01, R08 | INH | L01 effect 30; envelope field in fixture order (V02:L0091); FX-P1/FX-P2. | ACCEPTED |
| `owner_trials[3].effects[29].grammar` | `"REQUIRE"` | R01, R02 | INH | Rendered as `[30] REQUIRE <id>` (V01_CONTRACT-L0070); FX-P3. Only one grammar is exercised; acceptable for a burden probe (V01_CONTRACT-L0295). | ACCEPTED |
| `owner_trials[3].effects[29].independently_acceptable` | `true` | R01 | INH | Carried as envelope bytes only; no P01 rule evaluates partial acceptance; FX-P6. | ACCEPTED |
| `owner_trials[3].effects[29].subject` | `"SYNTHETIC-LARGE-030"` | R01, R02 | INH | `Subject:` line of the view; FX-P4. Unique within L01 (`SYNTHETIC-LARGE-<nnn>`); effect_id and acceptance_id keep envelopes distinct. | ACCEPTED |
| `owner_trials[3].effects[29].text` | Templated effect text 030 | R01, R02, R08, R29 | INH | `Text:` line; FX-P5. Identical templated text in Attempt 001 means owner familiarity must be disclosed (R4:L0094, L0247). | ACCEPTED |
| `owner_trials[3].issued_at` | `"2026-10-04T00:04:00Z"` | R01 | INH | Statement `issued_at` source (V02:L0105); provenance only, never order (V02:L0052). | ACCEPTED |
| `owner_trials[3].summary` | Thirty-effect synthetic governing acceptance used only to measure rendering and mechanical owner-authentication burden. | R01, R02 | INH | Envelope and `Summary:` view line (V02:L0074, L0107). | ACCEPTED |
| `owner_trials[3].title` | `"Large owner trial"` | R01, R02 | INH | Envelope and `Title:` view line. | ACCEPTED |
| `owner_trials[3].trial_id` | `"L01"` | R01, R08 | INH | Envelope `item_id` and view `Trial:` label (V02:L0107); trial domain (V01_CONTRACT-L0094). | ACCEPTED |

### `project_id`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `project_id` | `"ADS-R0-P01-SYNTHETIC"` | R01, C06 | INH | Synthetic project ID; a structural VERIFY gate in the successor (R4:L0025). | ACCEPTED |

### `protocol`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `protocol` | `"R0-P01-V01"` | R24, R21 | SUP:0020 | Successor protocol identity R0-P01-V01-I1 (R4:L0020, accepted in B01). | ACCEPTED |

### `renderer_profile`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `renderer_profile` | `"R0_P01_ASCII_OWNER_VIEW_V01"` | R02 | INH | Probe-only renderer (V01_CONTRACT-L0016); successor bytes frozen independently (R4:L0035). | ACCEPTED |

### `schema_version`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `schema_version` | `1` | R37 | INH | Fixture-file schema label. Retained while the successor fixture keeps this key set; any structural change needs a new value under F1 re-pinning. | ACCEPTED |

### `security_controls`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `security_controls[0]` | `"VALID_ACCEPTANCE"` | C01, R37 | INH | Control 1 key at position 0, equal to trace binding C01 and V01_CONTROLS heading 1. P0 VERIFY=VALID and first ADMIT succeeds; exactly one owner-authenticated P0 per cryptographic arm (V02:L0161). | ACCEPTED |
| `security_controls[1]` | `"FORGED_OR_AGENT_PREPARED_PROOF_REJECTS"` | C02, R37 | INH | Control 2 key at position 1, equal to trace binding C02 and V01_CONTROLS heading 2. First raw proof byte XOR 0x01, never a substituted valid forgery (V02:L0186). | ACCEPTED |
| `security_controls[2]` | `"CHANGED_ENVELOPE_REJECTS"` | C03, R37 | INH | Control 3 key at position 2, equal to trace binding C03 and V01_CONTROLS heading 3. Append ` [MUTATED]` to SEC-BASE-001.text and reuse P0. | ACCEPTED |
| `security_controls[3]` | `"CHANGED_SHOWN_VIEW_REJECTS"` | C04, R37 | INH | Control 4 key at position 3, equal to trace binding C04 and V01_CONTROLS heading 4. First displayed byte R to X; recompute shown_digest and reuse P0. | ACCEPTED |
| `security_controls[4]` | `"DECISION_SUBSTITUTION_REJECTS"` | C05, R37 | INH | Control 5 key at position 4, equal to trace binding C05 and V01_CONTROLS heading 5. ACCEPT to REJECT with reused P0. Open item C05_AMEND (AMEND substitution) concerns the mutation set, not this key. | ACCEPTED |
| `security_controls[5]` | `"CROSS_PROJECT_REPLAY_REJECTS"` | C06, R37 | INH | Control 6 key at position 5, equal to trace binding C06 and V01_CONTROLS heading 6. project_id to `wrong_project_id`; under REV04 the rejection layer is recorded and may be STRUCTURAL (R4:L0180). | ACCEPTED |
| `security_controls[6]` | `"ACCEPTANCE_ID_REPLAY_REJECTS"` | C07, R37 | INH | Control 7 key at position 6, equal to trace binding C07 and V01_CONTROLS heading 7. Changed ID rejects (A) and a second ADMIT of the consumed ID rejects (B); both must pass. | ACCEPTED |
| `security_controls[7]` | `"SEMANTIC_BASE_MISMATCH_REJECTS"` | C08, R37 | INH | Control 8 key at position 7, equal to trace binding C08 and V01_CONTROLS heading 8. BASE-A.lineage_head to BASE-A-1; I recomputed that this changes the base digest (`164ca4c0…`), so the control is not vacuous. | ACCEPTED |
| `security_controls[8]` | `"UNRELATED_REPOSITORY_LANDING_DOES_NOT_INVALIDATE"` | C09, R37 | INH | Control 9 key at position 8, equal to trace binding C09 and V01_CONTROLS heading 9. Out-of-band repository metadata only; exact P0 stays VALID. Pairs with the `source_revision` exclusion (V02:L0038). | ACCEPTED |
| `security_controls[9]` | `"SIGNER_SET_MISMATCH_REJECTS"` | C10, R37 | INH | Control 10 key at position 9, equal to trace binding C10 and V01_CONTROLS heading 10. signer_set_version to `SIGNERS-P01-V999-SYNTHETIC`; VERIFY rejects (V02:L0194). | ACCEPTED |
| `security_controls[10]` | `"TRUST_ROOT_ROTATION_DRY_RUN"` | C11, R37 | INH | Control 11 key at position 10, equal to trace binding C11 and V01_CONTROLS heading 11. Current PRIMARY signs the rotation; the candidate alone cannot promote itself. For Arm B, REV04 requires same-attempt Arm A public IDs as the P5 target, else FAIL (trace `B_arm_P5_rotation_dependency`). | ACCEPTED |
| `security_controls[11]` | `"RECOVERY_CREDENTIAL_DRY_RUN"` | C12, R37 | INH | Control 12 key at position 11, equal to trace binding C12 and V01_CONTROLS heading 12. Dedicated Arm-A RECOVERY key; under REV04 it must be the *new same-attempt* key, missing key is FAIL/unexecuted, never the old key (R4:L0024). | ACCEPTED |
| `security_controls[12]` | `"COMPROMISE_BOUNDARY_DRY_RUN"` | C13, R37 | INH | Control 13 key at position 12, equal to trace binding C13 and V01_CONTROLS heading 13. Deterministic classification REVIEW_REQUIRED / GOVERNING_OWNER from DECLARATION_TRUSTED_SYNTHETIC_INPUT (V02:L0056); authority matrix stays R1 work. | ACCEPTED |

### `semantic_base`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `semantic_base.effects[0].contract_revision` | `"C-A@1"` | C08, R36 | INH | Pinned contract revision of BASE-A; must match before signing or admission (V02:L0123). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[0].effect_id` | `"BASE-A"` | C08, R36 | INH | Selector member BASE-A; selector holds exactly BASE-A and BASE-B sorted by effect_id (V02:L0091, L0123). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[0].lineage_head` | `"BASE-A-0"` | C08, R36 | INH | BASE-A identity/version evidence against ABA staleness (V02:L0040). C08 mutates exactly this value to `BASE-A-1` (V02:L0192). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[0].status` | `"CURRENT"` | C08, R36 | INH | BASE-A dependency status; part of the ordinary base projection (V02:L0040); mismatch fails closed (V02:L0123). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[1].contract_revision` | `"C-B@1"` | C08, R36 | INH | Pinned contract revision of BASE-B; must match before signing or admission (V02:L0123). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[1].effect_id` | `"BASE-B"` | C08, R36 | INH | Selector member BASE-B; selector holds exactly BASE-A and BASE-B sorted by effect_id (V02:L0091, L0123). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[1].lineage_head` | `"BASE-B-0"` | C08, R36 | INH | BASE-B identity/version evidence against ABA staleness (V02:L0040). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.effects[1].status` | `"CURRENT"` | C08, R36 | INH | BASE-B dependency status; part of the ordinary base projection (V02:L0040); mismatch fails closed (V02:L0123). Base recomputes to `76a7391f…` (B17-P1). | ACCEPTED |
| `semantic_base.grammar_version` | `"G1"` | C08, R36 | INH | Base projection input (V02:L0113); recomputes to `76a7391f…` (V02:L0125; B17-P1). Not the REV04 Research-513 "G1" interpretation (B17-R1). | ACCEPTED |
| `semantic_base.predicate_semantics_version` | `"P1"` | C08, R36 | INH | Base projection input (V02:L0113); recomputes to `76a7391f…` (V02:L0125; B17-P1). Must match before signing or admission (V02:L0123). | ACCEPTED |
| `semantic_base.source_revision` | `"R0-P01-SYNTHETIC-BASE-V1"` | C09, C08 | INH | Historical metadata **excluded** from base and selector (V02:L0038). The exclusion is load-bearing: including it would change the digest (`3543688e…`). Golden vectors omit it. | ACCEPTED |

### `signer_set_version`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `signer_set_version` | `"SIGNERS-P01-V1"` | C10, C11, R01 | INH | Initial V1 version (V02:L0157); C10 mutates it to `SIGNERS-P01-V999-SYNTHETIC`. | ACCEPTED |

### `ssh_namespace`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `ssh_namespace` | `"ads-r0-p01-acceptance"` | R05, R04 | INH | Retained namespace (R4:L0067; B04-F3). | ACCEPTED |

### `statement_context`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `statement_context` | `"ADS-GOVERNING-ACCEPTANCE/v1"` | R01, C06 | SUP:0025 | V01/V02 context; replaced by `ADS-R0-P01-002-OWNER-ACCEPTANCE-V01` with prefix `R0-P01-002-` (R4:L0025). Old-context statements become negative replay fixtures (R4:L0132, L0263). | ACCEPTED |

### `webauthn`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `webauthn.algorithm_name` | `"ES256"` | R06 | INH | RP parameter preserved by R4:L0108. | ACCEPTED |
| `webauthn.attestation` | `"none"` | R06 | INH | RP parameter preserved by R4:L0108. | ACCEPTED |
| `webauthn.authenticator_attachment` | `null` | R06 | INH | `null` = omitted (V01_CONTRACT-L0180, L0189). | ACCEPTED |
| `webauthn.origin` | `"http://localhost:8765"` | R06 | INH | RP parameter preserved by R4:L0108. | ACCEPTED |
| `webauthn.port` | `8765` | R06, R22 | INH | Consistent with origin `http://localhost:8765`; same origin for preclaim readiness (R4:L0104). | ACCEPTED |
| `webauthn.public_key_algorithm` | `-7` | R06 | INH | COSE -7 = ES256 only (V01_CONTRACT-L0225). | ACCEPTED |
| `webauthn.resident_key` | `"preferred"` | R06 | INH | RP parameter preserved by R4:L0108. | ACCEPTED |
| `webauthn.rp_id` | `"localhost"` | R06 | INH | RP parameter preserved by R4:L0108. | ACCEPTED |
| `webauthn.user_verification` | `"required"` | R06 | INH | RP parameter preserved by R4:L0108. | ACCEPTED |

### `wrong_project_id`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `wrong_project_id` | `"OTHER-PROJECT-SYNTHETIC"` | C06 | INH | C06 mutation target (V02:L0190). It differs from `project_id`, so REV04 structural project checks reject it before crypto (R4:L0025, L0180). | ACCEPTED |

## 3. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
V01_FIXTURE:owner_trials[3].effects[27].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[27].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[27].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[27].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[27].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[27].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[27].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[27].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[3].effects[28].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[28].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[28].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[28].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[28].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[28].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[28].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[28].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[28].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[28].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[3].effects[29].effect_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[29].effect_id;FX-P2;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[29].grammar|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[29].grammar;FX-P3;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[29].independently_acceptable|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[29].independently_acceptable;FX-P6;V02_ADDENDUM-L0091
V01_FIXTURE:owner_trials[3].effects[29].subject|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[29].subject;FX-P4;V01_CONTRACT-L0070
V01_FIXTURE:owner_trials[3].effects[29].text|INHERITED_UNCHANGED|R01,R02,R08,R29|ACCEPTED||V01_FIXTURE:owner_trials[3].effects[29].text;FX-P5;REV04_CONTRACT-L0094
V01_FIXTURE:owner_trials[3].issued_at|INHERITED_UNCHANGED|R01|ACCEPTED||V01_FIXTURE:owner_trials[3].issued_at;V02_ADDENDUM-L0105
V01_FIXTURE:owner_trials[3].summary|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].summary;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[3].title|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_FIXTURE:owner_trials[3].title;V02_ADDENDUM-L0074
V01_FIXTURE:owner_trials[3].trial_id|INHERITED_UNCHANGED|R01,R08|ACCEPTED||V01_FIXTURE:owner_trials[3].trial_id;V02_ADDENDUM-L0107;V01_CONTRACT-L0094
V01_FIXTURE:project_id|INHERITED_UNCHANGED|R01,C06|ACCEPTED||V01_FIXTURE:project_id;REV04_CONTRACT-L0025
V01_FIXTURE:protocol|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0020|R24,R21|ACCEPTED||V01_FIXTURE:protocol;REV04_CONTRACT-L0020
V01_FIXTURE:renderer_profile|INHERITED_UNCHANGED|R02|ACCEPTED||V01_FIXTURE:renderer_profile;REV04_CONTRACT-L0035
V01_FIXTURE:schema_version|INHERITED_UNCHANGED|R37|ACCEPTED||V01_FIXTURE:schema_version;REV04_CONTRACT-L0035
V01_FIXTURE:security_controls[0]|INHERITED_UNCHANGED|C01,R37|ACCEPTED||V01_FIXTURE:security_controls[0];V01_CONTROLS-L0011;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[1]|INHERITED_UNCHANGED|C02,R37|ACCEPTED||V01_FIXTURE:security_controls[1];V01_CONTROLS-L0017;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[2]|INHERITED_UNCHANGED|C03,R37|ACCEPTED||V01_FIXTURE:security_controls[2];V01_CONTROLS-L0025;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[3]|INHERITED_UNCHANGED|C04,R37|ACCEPTED||V01_FIXTURE:security_controls[3];V01_CONTROLS-L0033;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[4]|INHERITED_UNCHANGED|C05,R37|ACCEPTED||V01_FIXTURE:security_controls[4];V01_CONTROLS-L0039;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[5]|INHERITED_UNCHANGED|C06,R37|ACCEPTED||V01_FIXTURE:security_controls[5];V01_CONTROLS-L0047;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[6]|INHERITED_UNCHANGED|C07,R37|ACCEPTED||V01_FIXTURE:security_controls[6];V01_CONTROLS-L0053;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[7]|INHERITED_UNCHANGED|C08,R37|ACCEPTED||V01_FIXTURE:security_controls[7];V01_CONTROLS-L0065;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[8]|INHERITED_UNCHANGED|C09,R37|ACCEPTED||V01_FIXTURE:security_controls[8];V01_CONTROLS-L0071;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[9]|INHERITED_UNCHANGED|C10,R37|ACCEPTED||V01_FIXTURE:security_controls[9];V01_CONTROLS-L0079;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[10]|INHERITED_UNCHANGED|C11,R37|ACCEPTED||V01_FIXTURE:security_controls[10];V01_CONTROLS-L0085;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[11]|INHERITED_UNCHANGED|C12,R37|ACCEPTED||V01_FIXTURE:security_controls[11];V01_CONTROLS-L0104;V02_ADDENDUM-L0181
V01_FIXTURE:security_controls[12]|INHERITED_UNCHANGED|C13,R37|ACCEPTED||V01_FIXTURE:security_controls[12];V01_CONTROLS-L0122;V02_ADDENDUM-L0181
V01_FIXTURE:semantic_base.effects[0].contract_revision|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[0].contract_revision;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[0].effect_id|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[0].effect_id;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[0].lineage_head|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[0].lineage_head;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[0].status|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[0].status;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[1].contract_revision|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[1].contract_revision;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[1].effect_id|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[1].effect_id;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[1].lineage_head|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[1].lineage_head;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.effects[1].status|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.effects[1].status;V02_ADDENDUM-L0040;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.grammar_version|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.grammar_version;V02_ADDENDUM-L0113;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.predicate_semantics_version|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_FIXTURE:semantic_base.predicate_semantics_version;V02_ADDENDUM-L0113;V02_ADDENDUM-L0125
V01_FIXTURE:semantic_base.source_revision|INHERITED_UNCHANGED|C09,C08|ACCEPTED||V01_FIXTURE:semantic_base.source_revision;V02_ADDENDUM-L0038
V01_FIXTURE:signer_set_version|INHERITED_UNCHANGED|C10,C11,R01|ACCEPTED||V01_FIXTURE:signer_set_version;V02_ADDENDUM-L0157;V02_ADDENDUM-L0194
V01_FIXTURE:ssh_namespace|INHERITED_UNCHANGED|R05,R04|ACCEPTED||V01_FIXTURE:ssh_namespace;REV04_CONTRACT-L0067
V01_FIXTURE:statement_context|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|R01,C06|ACCEPTED||V01_FIXTURE:statement_context;REV04_CONTRACT-L0025;REV04_CONTRACT-L0132
V01_FIXTURE:webauthn.algorithm_name|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.algorithm_name;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.attestation|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.attestation;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.authenticator_attachment|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.authenticator_attachment;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.origin|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.origin;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.port|INHERITED_UNCHANGED|R06,R22|ACCEPTED||V01_FIXTURE:webauthn.port;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.public_key_algorithm|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.public_key_algorithm;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.resident_key|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.resident_key;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.rp_id|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.rp_id;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:webauthn.user_verification|INHERITED_UNCHANGED|R06|ACCEPTED||V01_FIXTURE:webauthn.user_verification;REV04_CONTRACT-L0108;V02_ADDENDUM-L0256
V01_FIXTURE:wrong_project_id|INHERITED_UNCHANGED|C06|ACCEPTED||V01_FIXTURE:wrong_project_id;V02_ADDENDUM-L0190;REV04_CONTRACT-L0180
END_AUDIT_RECEIPT
```

Counts: 59 rows; 59 ACCEPTED; 0 PENDING; 2 SUPERSEDED_BY_REV04; 57 INHERITED_UNCHANGED; 0 NOT_APPLICABLE_TO_SUCCESSOR.

## 4. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source value of every unit above (each JSON leaf resolved from the committed blob and its `text_sha256` recomputed). I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited. PENDING items, including the classification-sensitive B05-A1, B07-A3 and B08-A1, remain open for ChatGPT reconciliation and are not resolved here.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE050=CLAUDE_AUDIT_BATCH017
DISPOSITION=ACCEPT_AUDIT_BATCH017
UNITS_AUDITED=59_OF_59
ACCEPTED=59
PENDING=0
KEY_FINDINGS=B17-P1_SEMANTIC_BASE_76A7391F_RECOMPUTED;B17-P2_CONTROL_KEYS_13_OF_13;B17-P3_RP_PARAMETERS;PROTOCOL_AND_CONTEXT_SUPERSEDED;B17-R1_G1_NAME_COLLISION;B17-R2_GOLDEN_VECTORS_REFREEZE;NO_PENDING
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
