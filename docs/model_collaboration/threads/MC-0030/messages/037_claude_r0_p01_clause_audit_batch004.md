# MC-0030 Message 037: Claude independent clause audit, batch Q0-AUDIT-004 (V01 implementation contract §1–§6.1)

```text
Thread                  MC-0030
Message                 037
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             99519011faaa6c9c0aeef18ecedb9330b1b34401 (Message 036)
Batch                   Q0-AUDIT-004 / V01_CONTRACT / 65 units / V01_CONTRACT-L0010 .. V01_CONTRACT-L0178
Batch unit-list SHA-256 recomputed from the plan's ordered IDs: match
Source                  experiments/r0_p01_owner_acceptance_v01/implementation_contract.md
Source SHA-256          b3b90d851e25a4b906f6e094e6366ca42baca7fceb7c38c253f8220bc70b1202 (Git blob, matches inventory)
Cross-checked against   V02 addendum (precedence: V02 line 14), REV04 contract, Q0 REV02 trace, REV03 test catalogue
Disposition             AMEND_AUDIT_BATCH004
Authority               Message 034. Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `99519011…` (my Message 036, parent `852db397…`, one added file). The receipt checker returned `PASS batches=3/18 units=151/1022`.
- Source hash matches the inventory. The 65 IDs hash to the plan value; every `text_sha256` matches. Units plus the four recorded exclusions (lines 3–6) cover every non-blank, non-heading line of the file.
- **Precedence applied.** V02 line 14 (Message 035 §3): V02 supersedes V0.1 only where it explicitly defines a detail. REV04 then supersedes either.
- **Disposition-vocabulary gap (scope finding B04-S1).** The inventory offers only INHERITED_UNCHANGED, SUPERSEDED_BY_REV04 and NOT_APPLICABLE_TO_SUCCESSOR. It has no value for "refined by the equally inherited V02 addendum". Where V02 refines a V01 rule without contradicting it, I record INHERITED_UNCHANGED and cite the V02 line in the basis. No V01 unit in this batch is *contradicted* by V02; the refinements are listed per unit.
- Notation: `INH`, `SUP:Lnnnn` (REV04_CONTRACT), `N/A`, `V01:`, `V02:`, `R4:`.

## 1. Verdict

**`AMEND_AUDIT_BATCH004`**: 65/65 reviewed; **62 ACCEPTED** (including 4 NOT_APPLICABLE_TO_SUCCESSOR), **3 PENDING**.

This half of the V01 contract is the base layer that V02 and REV04 refine. It is coherent. The successor replaces:

- the acceptance-ID grammar (REV04 L0025): two units pending on B02-A3;
- key identities and directories (REV04 L0023);
- the freedom to "adapt presentation around" the view, now constrained to a frozen T3 byte table (REV04 L0033).

Four units are pre-freeze environment observations (OpenSSH 9.5p2, Node v24.19.0 and their framing lines). They are historical, not successor requirements. The successor pins the executables actually used (R4:L0066, R39) and records browser UA (R4:L0104).

Findings:

- **B04-F1 (non-production boundary has no testable rule text).** V01:L0010 (no selection of production canonicalization, renderer, credential kinds, ChatGPT authority, key topology or trust-root UX) is the broad form of Message 033 A6(a). No R row states it. REV04 L0132 and L0247 say the same in passing ("not a recommended change to production governance"; "selection not physical target"). Pending under A6.
- **B04-F2 (step order in the sign-what-you-see list).** Read literally, V01:L0061 (display preview) precedes V01:L0062 (start mechanical timing). L0062 itself says mechanical timing starts "immediately after the decision is captured", and V02:L0274 and R4:L0035 put the preview inside the mechanical interval. There is no conflict, but T-TIMER-BOUNDARY should assert `preview_emitted ≥ decision_captured` on the same monotonic clock, so that an implementation that follows the list order literally fails.
- **B04-F3 (SSHSIG namespace retained).** The SSH namespace `ads-r0-p01-acceptance` (V01:L0110/L0151) is not changed by REV04 (R4:L0067: "same namespace"). Cross-attempt separation therefore rests on statement context and prefix plus fresh keys, which R4:L0026 and L0132 already state. No action needed; recorded so that F1 does not silently change the namespace.

## 2. Per-unit audit record (65 units)

### §1 Non-production boundary

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0010 | The probe selects no production canonicalization, renderer, credential kind, ChatGPT authority, key topology or trust-root UX | R12 | INH | R4:L0132, L0247 restate it informally. No testable rule text (A6 / B04-F1). | **PENDING** A6 |
| V01_CONTRACT-L0012 | Research question: can the architecture realize a practical owner-exclusive proof over the exact statement | R04, R10 | INH | Defines what PASS_WITH_SELECTION means. Unchanged (R4:L0012). | ACCEPTED |
| V01_CONTRACT-L0014 | The following identifiers are probe-only | R01, R02 | INH | Framing for L0016. | ACCEPTED |
| V01_CONTRACT-L0016 | Probe-only: canonical JSON scheme, ASCII owner-view scheme, synthetic project ID | R01, R02 | INH | The successor context is likewise a synthetic probe-instance separator (R4:L0132). | ACCEPTED |
| V01_CONTRACT-L0020 | No private key, passphrase, authenticator/recovery secret or account credential may be printed, committed, sent to a model, logged or put in a result | R19, R39 | INH | R4:L0134; synthetic transcript secret scan (R39). | ACCEPTED |

### §2 Frozen SignedAcceptanceStatement

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0024 | Every cryptographic arm signs the same logical fields | R01, R04 | INH | — | ACCEPTED |
| V01_CONTRACT-L0026 | The nine field names | R01 | INH | R4:L0025 keeps the nine names. | ACCEPTED |
| V01_CONTRACT-L0036 | Canonical bytes: compact, sorted keys, UTF-8, no NaN/Infinity | R01, R36 | INH | V02:L0066 refines (no BOM, code-point order, escaping). | ACCEPTED |
| V01_CONTRACT-L0038 | Arm A signs the statement bytes themselves | R01, R04 | INH | — | ACCEPTED |
| V01_CONTRACT-L0040 | Arm B's challenge is set as follows | R06 | INH | Framing for L0042. | ACCEPTED |
| V01_CONTRACT-L0042 | Challenge = SHA256(canonical statement bytes) | R06 | INH | V02:L0068 makes it the raw 32 bytes, unpadded base64url. | ACCEPTED |
| V01_CONTRACT-L0044 | Verification independently recomputes that digest before accepting | R06, R36 | INH | V02:L0262. | ACCEPTED |
| V01_CONTRACT-L0046 | Arm C attests the lowercase hex SHA-256 of the same bytes | R30 | INH | V02:L0068, L0268. | ACCEPTED |

### §3 Sign-what-you-see client rule

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0050 | The harness, not chat or model prose, owns the signed display | R02 | INH | V02:L0260 ("local client owns the view"). | ACCEPTED |
| V01_CONTRACT-L0052 | For every owner trial the following steps are mandatory | R02, R03, R08 | INH | Framing for steps 1–13. | ACCEPTED |
| V01_CONTRACT-L0054 | 1. load the exact envelope from fixture.json | R01, R34 | INH | V02:L0072–L0091 construct it from fixture fields; the successor fixture is an F1 artifact (R34). | ACCEPTED |
| V01_CONTRACT-L0055 | 2. recompute and validate the semantic-base digest | C08, R36 | INH | V02:L0125. | ACCEPTED |
| V01_CONTRACT-L0056 | 3. build the exact owner view with the ASCII view scheme | R02 | INH | V02:L0107. | ACCEPTED |
| V01_CONTRACT-L0057 | 4. display the same in-memory bytes whose SHA-256 is shown_digest | R02, C04 | INH | — | ACCEPTED |
| V01_CONTRACT-L0058 | 5. start semantic-review timing only after the complete view is displayed | R08, R28 | INH | R4:L0094. | ACCEPTED |
| V01_CONTRACT-L0059 | 6. collect ACCEPT / AMEND / REJECT | R03 | INH | R4:L0194 (uncaptured input re-prompts). | ACCEPTED |
| V01_CONTRACT-L0060 | 7. stop semantic-review timing at the decision | R08, R28 | INH | — | ACCEPTED |
| V01_CONTRACT-L0061 | 8. construct and display the final canonical statement preview | R03, R01 | INH | Inside mechanical time (V02:L0274, R4:L0035). See B04-F2. | ACCEPTED |
| V01_CONTRACT-L0062 | 9. start mechanical timing immediately after decision capture, before credential invocation | R08, R27 | INH | R4:L0094, L0096 (`decision_captured` landmark). B04-F2. | ACCEPTED |
| V01_CONTRACT-L0063 | 10. invoke the owner credential without receiving any secret from caller or model | R19, R05 | INH | R4:L0066–L0067. | ACCEPTED |
| V01_CONTRACT-L0064 | 11. verify the proof locally | R14 | INH | Now tri-state with structural pre-checks (R4:L0126, L0132), a refinement of the same step. | ACCEPTED |
| V01_CONTRACT-L0065 | 12. stop mechanical timing only at a deterministic local verification result | R08, R14 | INH | R4:L0094. A VERIFIER_ERROR is not a deterministic result and ends the run INVALID_INSTRUMENT (R4:L0128). | ACCEPTED |
| V01_CONTRACT-L0066 | 13. collect the non-secret friction rating and note | R27, R08 | INH | R4:L0098 (1..5 rating, note). | ACCEPTED |
| V01_CONTRACT-L0068 | The rendered view contains the following lines in exact order | R02 | INH | Framing for L0070. | ACCEPTED |
| V01_CONTRACT-L0070 | View template: header, Project, Trial, Acceptance, Title, Summary, Semantic base, Effects count, per-effect three lines, END footer | R02, R36 | INH | V02:L0107 fixes indentation and LF. The successor renderer bytes are frozen independently (R4:L0035; T-RENDER-GOLDEN). The Acceptance line changes with B02-A3. | ACCEPTED |
| V01_CONTRACT-L0084 | LF line endings; final byte LF | R02 | INH | — | ACCEPTED |
| V01_CONTRACT-L0086 | The harness may adapt terminal/browser presentation around the string; shown_digest is over exactly those bytes | R02 | SUP:L0033 | Surrounding presentation is now a frozen static T3 byte table outside the view delimiters, with no dynamic coaching (R4:L0033, L0035). | ACCEPTED |

### §4 Acceptance identifiers

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0090 | Acceptance IDs are deterministic and arm-specific | R01 | INH | REV04 keeps "arm/item-specific" (R4:L0025). | ACCEPTED |
| V01_CONTRACT-L0092 | Grammar `R0-P01-<ARM>-<TRIAL>` | R01 | SUP:L0025 | Prefix becomes `R0-P01-002-`; exact successor strings not enumerated. | **PENDING** B02-A3 |
| V01_CONTRACT-L0094 | ARM ∈ {A, B, C}; TRIAL ∈ {S01, S02, S03, L01} | R01, R04, R08 | INH | Domains unchanged. | ACCEPTED |
| V01_CONTRACT-L0096 | Security-control IDs use the following grammar | R01 | INH | Framing for L0098. | ACCEPTED |
| V01_CONTRACT-L0098 | Grammar `R0-P01-<ARM>-SEC-<CONTROL>` | R01, R37 | SUP:L0025 | Same as L0092. | **PENDING** B02-A3 |
| V01_CONTRACT-L0100 | CONTROL is the exact security-control key | R01, R37 | INH | T-CONTROL-KEY-BINDING. Only P0, P5, P6 (and the C07 class-A replacement) actually use such IDs (V02:L0181). | ACCEPTED |
| V01_CONTRACT-L0102 | These IDs are synthetic and never become production authority | R01 | INH | Enforced structurally by context/prefix (R4:L0132). | ACCEPTED |

### §5.1 Arm A mechanism

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0108 | Arm A uses Windows OpenSSH SSHSIG | R04, R05 | INH | — | ACCEPTED |
| V01_CONTRACT-L0110 | Ed25519; `ssh-keygen -Y`; namespace `ads-r0-p01-acceptance` | R04, R05 | INH | R4:L0067 keeps the namespace (B04-F3). | ACCEPTED |
| V01_CONTRACT-L0114 | Framing: pre-freeze reconnaissance observed the following | - | N/A | Historical observation framing, not a successor rule. | ACCEPTED |
| V01_CONTRACT-L0116 | Observed OpenSSH_for_Windows_9.5p2 with `-Y sign/verify` | - | N/A | Historical 2026-10 environment observation. The successor pins the executable path and version actually present (R4:L0066, R39) and runs the preclaim KAT (R4:L0120). | ACCEPTED |

### §5.2 Key material

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0121 | Keys live in a dedicated probe-only local directory outside the repository | R19, R16 | INH | R4:L0023, L0027 (new attempt-local directory, separate from Attempt 001 directories). | ACCEPTED |
| V01_CONTRACT-L0123 | Path `%LOCALAPPDATA%\ADS-R0-P01\arm-a\` | R19 | SUP:L0023 | Attempt 001 path; the successor uses a new attempt-local directory. | ACCEPTED |
| V01_CONTRACT-L0125 | Required owner credentials | R04 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0127 | owner_primary_ed25519, owner_recovery_ed25519 | R04, R23 | SUP:L0023 | Fresh PRIMARY and RECOVERY keys after claim, distinct from each other and from all Attempt 001 public IDs (R23). | ACCEPTED |
| V01_CONTRACT-L0130 | Each key is generated interactively by the owner with the following command | R04, R19 | INH | R4:L0023 ("native interactive OpenSSH"). | ACCEPTED |
| V01_CONTRACT-L0132 | `ssh-keygen -t ed25519 -a 100 -f <path> -C <probe-label>` | R04, R19 | INH | The comment is ignored for identity (V02:L0155); it must not be personally linking (R4:L0023). | ACCEPTED |
| V01_CONTRACT-L0134 | The owner chooses a non-empty passphrase at the native prompt | R04, R19, R05 | INH | R4:L0066 checks an encrypted native-key header before every invocation. | ACCEPTED |
| V01_CONTRACT-L0136 | Forbidden practices follow | R19 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0138 | Forbidden: `-N`, command-line passphrase, passphrase env var, agent caching, private key in repo, private-key path in a public result | R19, R05 | INH | R4:L0066 (no agent caching, rechecked each invocation). | ACCEPTED |
| V01_CONTRACT-L0145 | Record only public key material/fingerprint and proof artifacts needed for independent verification | R19, R16, R23 | INH | REV04 narrows publication: no personally linkable fingerprints in the public repository (R4:L0023, L0138). | ACCEPTED |

### §5.3 Signing and §5.4 Recovery

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0149 | Write canonical statement bytes to the local probe directory and invoke signing | R05 | INH | R4:L0066 (on-disk bytes equal the frozen digest before every invocation; no existing `.sig`). | ACCEPTED |
| V01_CONTRACT-L0151 | `ssh-keygen -Y sign -f <key> -n ads-r0-p01-acceptance <file>` | R05, R04 | INH | R4:L0067 (same invocation shape). | ACCEPTED |
| V01_CONTRACT-L0153 | Console/TTY inherited so the owner enters the passphrase | R05, R19, R38 | INH | R4:L0067; Windows ConPTY qualification (R38, T-WIN-CONPTY-SSH). | ACCEPTED |
| V01_CONTRACT-L0155 | Verify with `ssh-keygen -Y verify` against an allowed-signers file from the public key | R14, R36 | INH | In-trial verifier. The independent scorer additionally re-verifies in-process (R36); the preclaim KAT covers this path (R4:L0120). | ACCEPTED |
| V01_CONTRACT-L0157 | The harness never supplies the passphrase | R19 | INH | — | ACCEPTED |
| V01_CONTRACT-L0161 | The recovery key is preregistered by public fingerprint before security-control execution | C12, R04 | INH | In the successor it is created after claim and registered before P0 (R4:L0023). | ACCEPTED |
| V01_CONTRACT-L0163 | The recovery key is not loaded into ssh-agent | R05, R19 | INH | — | ACCEPTED |
| V01_CONTRACT-L0165 | Recovery dry-run is a separate security control, not a burden trial | C12, R08 | INH | V02:L0250. | ACCEPTED |

### §6.1 Arm B mechanism (first part)

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0171 | A local WebAuthn RP implemented only with the installed Node runtime and browser platform APIs | R06, R39 | INH | Same as V02 line 18 for the Node side; B02-A4 concerns only the Python side. The test-only Playwright virtual authenticator (R40) is not part of the RP. | ACCEPTED |
| V01_CONTRACT-L0173 | Framing: pre-freeze reconnaissance observed the following | - | N/A | Historical observation framing. | ACCEPTED |
| V01_CONTRACT-L0175 | Observed Node v24.19.0 and a connected Chrome runtime | - | N/A | Historical observation. The successor records the actual browser, UA and launch method (R4:L0104) and pins Node (R39). | ACCEPTED |
| V01_CONTRACT-L0178 | The exact RP is as follows | R06 | INH | Framing; RP parameters are in batch 005. | ACCEPTED |

## 3. V01_CONTRACT lines outside numbered sections

| Line | Content | Normative? | Finding |
|---|---|---|---|
| 3 | Status: prospectively frozen | No | METADATA |
| 4 | Protocol R0-P01-V01 | No | METADATA; successor identity R4:L0020 |
| 5 | Candidate GOVERNED_LEDGER_KERNEL_V02 | No | METADATA; still unselected (R4:L0016) |
| 6 | Purpose: freeze implementation choices, sign-what-you-see, credential handling, timing, result interface and implementation blindness before results | Restates later sections | Covered by §3, §5–§6, §9–§10, §13 and the §14 implementation boundary (batches 005–006). No new unit needed. |

## 4. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
V01_CONTRACT-L0010|INHERITED_UNCHANGED|R12|PENDING|A6_NONPRODUCTION_BOUNDARY_RULE_TEXT_MISSING|V01_CONTRACT-L0010;REV04_CONTRACT-L0132;REV04_CONTRACT-L0247
V01_CONTRACT-L0012|INHERITED_UNCHANGED|R04,R10|ACCEPTED||V01_CONTRACT-L0012;REV04_CONTRACT-L0012
V01_CONTRACT-L0014|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_CONTRACT-L0014
V01_CONTRACT-L0016|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V01_CONTRACT-L0016;REV04_CONTRACT-L0132
V01_CONTRACT-L0020|INHERITED_UNCHANGED|R19,R39|ACCEPTED||V01_CONTRACT-L0020;REV04_CONTRACT-L0134
V01_CONTRACT-L0024|INHERITED_UNCHANGED|R01,R04|ACCEPTED||V01_CONTRACT-L0024
V01_CONTRACT-L0026|INHERITED_UNCHANGED|R01|ACCEPTED||V01_CONTRACT-L0026;REV04_CONTRACT-L0025
V01_CONTRACT-L0036|INHERITED_UNCHANGED|R01,R36|ACCEPTED||V01_CONTRACT-L0036;V02_ADDENDUM-L0066
V01_CONTRACT-L0038|INHERITED_UNCHANGED|R01,R04|ACCEPTED||V01_CONTRACT-L0038
V01_CONTRACT-L0040|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0040
V01_CONTRACT-L0042|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0042;V02_ADDENDUM-L0068
V01_CONTRACT-L0044|INHERITED_UNCHANGED|R06,R36|ACCEPTED||V01_CONTRACT-L0044;V02_ADDENDUM-L0262
V01_CONTRACT-L0046|INHERITED_UNCHANGED|R30|ACCEPTED||V01_CONTRACT-L0046;V02_ADDENDUM-L0068
V01_CONTRACT-L0050|INHERITED_UNCHANGED|R02|ACCEPTED||V01_CONTRACT-L0050;V02_ADDENDUM-L0260
V01_CONTRACT-L0052|INHERITED_UNCHANGED|R02,R03,R08|ACCEPTED||V01_CONTRACT-L0052
V01_CONTRACT-L0054|INHERITED_UNCHANGED|R01,R34|ACCEPTED||V01_CONTRACT-L0054;V02_ADDENDUM-L0072
V01_CONTRACT-L0055|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V01_CONTRACT-L0055;V02_ADDENDUM-L0125
V01_CONTRACT-L0056|INHERITED_UNCHANGED|R02|ACCEPTED||V01_CONTRACT-L0056;V02_ADDENDUM-L0107
V01_CONTRACT-L0057|INHERITED_UNCHANGED|R02,C04|ACCEPTED||V01_CONTRACT-L0057
V01_CONTRACT-L0058|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_CONTRACT-L0058;REV04_CONTRACT-L0094
V01_CONTRACT-L0059|INHERITED_UNCHANGED|R03|ACCEPTED||V01_CONTRACT-L0059;REV04_CONTRACT-L0194
V01_CONTRACT-L0060|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_CONTRACT-L0060
V01_CONTRACT-L0061|INHERITED_UNCHANGED|R03,R01|ACCEPTED||V01_CONTRACT-L0061;V02_ADDENDUM-L0274;REV04_CONTRACT-L0035
V01_CONTRACT-L0062|INHERITED_UNCHANGED|R08,R27|ACCEPTED||V01_CONTRACT-L0062;REV04_CONTRACT-L0094;REV04_CONTRACT-L0096
V01_CONTRACT-L0063|INHERITED_UNCHANGED|R19,R05|ACCEPTED||V01_CONTRACT-L0063;REV04_CONTRACT-L0067
V01_CONTRACT-L0064|INHERITED_UNCHANGED|R14|ACCEPTED||V01_CONTRACT-L0064;REV04_CONTRACT-L0126
V01_CONTRACT-L0065|INHERITED_UNCHANGED|R08,R14|ACCEPTED||V01_CONTRACT-L0065;REV04_CONTRACT-L0094;REV04_CONTRACT-L0128
V01_CONTRACT-L0066|INHERITED_UNCHANGED|R27,R08|ACCEPTED||V01_CONTRACT-L0066;REV04_CONTRACT-L0098
V01_CONTRACT-L0068|INHERITED_UNCHANGED|R02|ACCEPTED||V01_CONTRACT-L0068
V01_CONTRACT-L0070|INHERITED_UNCHANGED|R02,R36|ACCEPTED||V01_CONTRACT-L0070;V02_ADDENDUM-L0107;REV04_CONTRACT-L0035
V01_CONTRACT-L0084|INHERITED_UNCHANGED|R02|ACCEPTED||V01_CONTRACT-L0084
V01_CONTRACT-L0086|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0033|R02|ACCEPTED||REV04_CONTRACT-L0033;REV04_CONTRACT-L0035
V01_CONTRACT-L0090|INHERITED_UNCHANGED|R01|ACCEPTED||V01_CONTRACT-L0090;REV04_CONTRACT-L0025
V01_CONTRACT-L0092|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|R01|PENDING|B02-A3_SUCCESSOR_ACCEPTANCE_ID_STRINGS_NOT_ENUMERATED|REV04_CONTRACT-L0025;REV04_CONTRACT-L0132
V01_CONTRACT-L0094|INHERITED_UNCHANGED|R01,R04,R08|ACCEPTED||V01_CONTRACT-L0094
V01_CONTRACT-L0096|INHERITED_UNCHANGED|R01|ACCEPTED||V01_CONTRACT-L0096
V01_CONTRACT-L0098|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|R01,R37|PENDING|B02-A3_SUCCESSOR_ACCEPTANCE_ID_STRINGS_NOT_ENUMERATED|REV04_CONTRACT-L0025;REV04_CONTRACT-L0132
V01_CONTRACT-L0100|INHERITED_UNCHANGED|R01,R37|ACCEPTED||V01_CONTRACT-L0100;V02_ADDENDUM-L0181
V01_CONTRACT-L0102|INHERITED_UNCHANGED|R01|ACCEPTED||V01_CONTRACT-L0102;REV04_CONTRACT-L0132
V01_CONTRACT-L0108|INHERITED_UNCHANGED|R04,R05|ACCEPTED||V01_CONTRACT-L0108
V01_CONTRACT-L0110|INHERITED_UNCHANGED|R04,R05|ACCEPTED||V01_CONTRACT-L0110;REV04_CONTRACT-L0067
V01_CONTRACT-L0114|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||V01_CONTRACT_SECTION_5.1;reason=historical_reconnaissance_framing
V01_CONTRACT-L0116|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||V01_CONTRACT_SECTION_5.1;reason=historical_environment_observation;successor_pin=REV04_CONTRACT-L0066
V01_CONTRACT-L0121|INHERITED_UNCHANGED|R19,R16|ACCEPTED||V01_CONTRACT-L0121;REV04_CONTRACT-L0023;REV04_CONTRACT-L0027
V01_CONTRACT-L0123|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0023|R19|ACCEPTED||REV04_CONTRACT-L0023;REV04_CONTRACT-L0027
V01_CONTRACT-L0125|INHERITED_UNCHANGED|R04|ACCEPTED||V01_CONTRACT-L0125
V01_CONTRACT-L0127|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0023|R04,R23|ACCEPTED||REV04_CONTRACT-L0023
V01_CONTRACT-L0130|INHERITED_UNCHANGED|R04,R19|ACCEPTED||V01_CONTRACT-L0130;REV04_CONTRACT-L0023
V01_CONTRACT-L0132|INHERITED_UNCHANGED|R04,R19|ACCEPTED||V01_CONTRACT-L0132;V02_ADDENDUM-L0155
V01_CONTRACT-L0134|INHERITED_UNCHANGED|R04,R19,R05|ACCEPTED||V01_CONTRACT-L0134;REV04_CONTRACT-L0066
V01_CONTRACT-L0136|INHERITED_UNCHANGED|R19|ACCEPTED||V01_CONTRACT-L0136
V01_CONTRACT-L0138|INHERITED_UNCHANGED|R19,R05|ACCEPTED||V01_CONTRACT-L0138;REV04_CONTRACT-L0066
V01_CONTRACT-L0145|INHERITED_UNCHANGED|R19,R16,R23|ACCEPTED||V01_CONTRACT-L0145;REV04_CONTRACT-L0023;REV04_CONTRACT-L0138
V01_CONTRACT-L0149|INHERITED_UNCHANGED|R05|ACCEPTED||V01_CONTRACT-L0149;REV04_CONTRACT-L0066
V01_CONTRACT-L0151|INHERITED_UNCHANGED|R05,R04|ACCEPTED||V01_CONTRACT-L0151;REV04_CONTRACT-L0067
V01_CONTRACT-L0153|INHERITED_UNCHANGED|R05,R19,R38|ACCEPTED||V01_CONTRACT-L0153;REV04_CONTRACT-L0067
V01_CONTRACT-L0155|INHERITED_UNCHANGED|R14,R36|ACCEPTED||V01_CONTRACT-L0155;REV04_CONTRACT-L0120
V01_CONTRACT-L0157|INHERITED_UNCHANGED|R19|ACCEPTED||V01_CONTRACT-L0157
V01_CONTRACT-L0161|INHERITED_UNCHANGED|C12,R04|ACCEPTED||V01_CONTRACT-L0161;REV04_CONTRACT-L0023
V01_CONTRACT-L0163|INHERITED_UNCHANGED|R05,R19|ACCEPTED||V01_CONTRACT-L0163
V01_CONTRACT-L0165|INHERITED_UNCHANGED|C12,R08|ACCEPTED||V01_CONTRACT-L0165;V02_ADDENDUM-L0250
V01_CONTRACT-L0171|INHERITED_UNCHANGED|R06,R39|ACCEPTED||V01_CONTRACT-L0171
V01_CONTRACT-L0173|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||V01_CONTRACT_SECTION_6.1;reason=historical_reconnaissance_framing
V01_CONTRACT-L0175|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||V01_CONTRACT_SECTION_6.1;reason=historical_environment_observation;successor_record=REV04_CONTRACT-L0104
V01_CONTRACT-L0178|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0178
END_AUDIT_RECEIPT
```

Counts: 65 rows; 62 ACCEPTED; 3 PENDING; 5 SUPERSEDED_BY_REV04; 56 INHERITED_UNCHANGED; 4 NOT_APPLICABLE_TO_SUCCESSOR.

## 5. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source for every unit above. I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited; PENDING items remain open.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE037=CLAUDE_AUDIT_BATCH004
DISPOSITION=AMEND_AUDIT_BATCH004
UNITS_AUDITED=65_OF_65
ACCEPTED=62
PENDING=3
FINDINGS=B04-S1_NO_V02_REFINEMENT_DISPOSITION;B04-F1_NONPRODUCTION_RULE_TEXT;B04-F2_PREVIEW_TIMER_ORDER;B04-F3_SSHSIG_NAMESPACE_RETAINED
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
