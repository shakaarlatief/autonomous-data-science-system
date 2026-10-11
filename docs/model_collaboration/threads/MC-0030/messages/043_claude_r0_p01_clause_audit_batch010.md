# MC-0030 Message 043: Claude independent clause audit, batch Q0-AUDIT-010 (REV04 outcome policy, leaves attempt_terminal … evidence_disclosures)

```text
Thread                  MC-0030
Message                 043
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             dbd333335e545a563f0311597fcf85b9413e793f (Checkpoint 871 / Research 535 / Validation 224; JSON-path receipt parser repaired)
Batch                   Q0-AUDIT-010 / REV04_POLICY / 65 units / REV04_POLICY:attempt_terminal_vs_event_terminal.ctrl_c_or_crash .. REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.origin
Batch unit-list SHA-256 098436950b701b3a1029ffb6e8385c10477438a49ce0fa998408a775d0dd7ac7 (recomputed: match)
Source                  docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json
Source SHA-256          9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c (Git blob, matches inventory)
Cross-checked against   REV04 contract (sha 9160a30c...), B01/B02 owner acceptance records, inventory policy_root_classification,
                        Q0 REV02 trace R01-R40/C01-C13, REV03 test catalogue, Messages 033 and 035-052
Disposition             AMEND_AUDIT_BATCH010
Authority               Message 034 (resumed per Research 535 / Checkpoint 871). Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `dbd33333…`, one commit after my Message 052. It changes only the receipt checker, its tests, and ChatGPT governance records (Research 535, Validation 224, Checkpoint 871, routing/state). The repaired checker returned `PASS batches=9/18 units=472/1022 accepted=428 pending=44`; `check_r0_p01_f1_audit_rev03.py` passed; the 25 receipt/inventory unit tests passed locally. The repaired parser now **rejects** any non-row text inside the receipt block, so this receipt contains rows only.
- All 7 source SHA-256 values still equal the inventory; the approved REV04 contract/policy hashes (`9160a30c…`, `9b5bbc4d…`) are unchanged; the inventory hash equals the plan; all 18 unit-list hashes recompute. My nine committed records (033, 035–042) and Message 052 are byte-identical at the new HEAD and were not re-audited.
- Every one of the 65 units was resolved from the committed policy JSON by the inventory's own leaf-walk rule (sorted keys, `.key` / `[i]` paths, keys may themselves contain dots) and its canonical-JSON `text_sha256` recomputed: 65/65 match.
- Source is the B01/B02-approved REV04 outcome policy. As in Messages 040–042 (convention B07-S1), `INH*` = INHERITED_UNCHANGED meaning **approved successor text carried into F1 unchanged**. `N/A` (NOT_APPLICABLE_TO_SUCCESSOR, IDs `-`) is used only for leaves under roots the inventory itself classifies NON_NORMATIVE **and** whose content imposes no successor obligation; each states its reason.
- Each leaf was read as a machine rule: is the value unambiguous, consistent with the contract sentence it encodes, mapped to C/R rule text, and testable? `R4:` = REV04_CONTRACT line; `P:` = another REV04_POLICY leaf.

## 1. Verdict

**`AMEND_AUDIT_BATCH010`**: 65/65 reviewed; **63 ACCEPTED, 2 PENDING** (3 of the accepted rows are NOT_APPLICABLE_TO_SUCCESSOR).

This batch covers the attempt-versus-event termination rules, the WebAuthn/Node interrupt rules, the seven scored-policy `cases`, the full `claim_cap` stopping policy and the final-head-witness disclosure leaves. Checked against REV04 §4, §7, §8.4 and §9:

- The seven `cases` have distinct `(claim, class, reason)` triples. They are exactly NOT_RUN plus the six scored outcomes (R4:L0239–L0252, L0276).
- `claim_cap` has exactly five ALL_REQUIRED exception conditions, matching the five common requirements in R4:L0241. The cap is 2, with 1 historical claim. No exception follows INVALID_INTEGRITY or PASS (including PASS with G2).
- The witness-absent leaves are disclosure-only (R4:L0138, L0231).

**Finding B10-F1 (confirms B08-A1 in the approved policy, with a second facet).** The `node_rp_failure` flag is defined two ways:

- `browser_node_interrupt.unexpected_node_failure` sets it if the cause is an **"unprovoked RP process fault"**, a *causal* predicate.
- `raw_flag_schema.node_rp_failure` (batch 012) sets it for an exit **"observed before any owner KeyboardInterrupt/abort was recorded"**, a *temporal* predicate.
- `browser_node_interrupt.owner_ctrl_c` says owner Ctrl+C is attempt abort, not node failure, **"by default"**. That wording implies a rebuttable default, but it names neither who may rebut it nor with what evidence.

The two predicates disagree in exactly the cases B08-A1 is about:

- an OS-killed Node process after an owner abort;
- an unprovoked Node fault whose receipt precedes, or cannot be ordered against, a Ctrl+C.

The "by default" wording is consistent with my earlier candidate (ambiguous order → attempt abort / INCOMPLETE), but it is not a frozen tie-break. **B08-A1 stays open.** I record it at the two policy leaves where the rule lives, without proposing which interpretation governs.

## 2. Per-unit audit record (65 units)

Paths are relative to the REV04_POLICY root; receipt IDs carry the full `REV04_POLICY:` prefix.

### `attempt_terminal_vs_event_terminal`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `attempt_terminal_vs_event_terminal.ctrl_c_or_crash` | `whole_claimed_attempt_ends; event_in_flight_INCOMPLETE; event_not_reissued` | R17, R31, R11 | INH* | R4:L0069, L0114, L0198. T-CTRL-C-SSH, T-NO-RESUME. | ACCEPTED |
| `attempt_terminal_vs_event_terminal.dependent_controls` | `FAIL_UNEXECUTED_DEPENDENCY_ABSENT_if_parent_proof_missing` | R26, C02, C13 | INH* | R4:L0069. Same code as the contract; the P5/P6 member-absent codes differ (B07-R1). | ACCEPTED |
| `attempt_terminal_vs_event_terminal.no_process_resume` | `true`: no cross-process resumption | R31, R17 | INH* | R4:L0114. | ACCEPTED |
| `attempt_terminal_vs_event_terminal.owner_input_R` | R allows only the next native sign invocation, same statement, same monotonic clock | R05 | INH* | R4:L0069, L0197. | ACCEPTED |
| `attempt_terminal_vs_event_terminal.owner_input_S_or_non_R` | S/any non-R → event-terminal without proof; continue with the next scheduled event where possible | R05, R26 | INH* | R4:L0060, L0197. B07-R2 (empty input also stops the event). | ACCEPTED |

### `authority`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `authority` | `CANDIDATE_ONLY_NOT_OWNER_AUTHORIZED` | - | N/A | Stale drafting attribution; B02 later accepted the policy. Root classified NON_NORMATIVE by the inventory; R21 keeps the approved proposal immutable despite stale flags. | ACCEPTED |

### `browser_node_interrupt`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `browser_node_interrupt.candidate_process_isolation` | CREATE_NEW_PROCESS_GROUP only if verified on the target Windows build | R38, R17 | INH* | R4:L0112. T-WIN-NODE-GROUP. | ACCEPTED |
| `browser_node_interrupt.durable_event_receipt` | Owner-local non-secret RP ceremony receipt written before acknowledgement | R35, R16 | INH* | R4:L0112. T-RP-STREAM-CROSSCHAIN. | ACCEPTED |
| `browser_node_interrupt.missing_rp_receipt` | Missing receipt → unattempted event INCOMPLETE; never fabricated success | R11, R35 | INH* | R4:L0112, L0154. | ACCEPTED |
| `browser_node_interrupt.no_postinterrupt_rpc_dependency` | `true`: classification never depends on a post-interrupt RPC | R17, R35 | INH* | R4:L0112. T-RP-TAIL-AFTER-CRASH. | ACCEPTED |
| `browser_node_interrupt.owner_ctrl_c` | Owner Ctrl+C = attempt abort, not node_rp_failure **by default** | R17, R13 | INH* | Rebuttable default with no named rebuttal evidence; ordering ambiguity unresolved (B10-F1). | **PENDING** B08-A1 |
| `browser_node_interrupt.unexpected_node_failure` | `node_rp_failure=true` if the cause is an **unprovoked** RP process fault | R13, R35 | INH* | Causal predicate; it conflicts in edge cases with the temporal definition at `raw_flag_schema.node_rp_failure` (B10-F1). | **PENDING** B08-A1 |

### `cases`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `cases[0].next` | Owner declined/deferred: no new claim; Attempt 001 stays AMEND; no physical target | R12, R18 | INH* | R4:L0239. | ACCEPTED |
| `cases[0].when.claim` | `NOT_RUN_PRECLAIM` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[0].when.class` | `null`: no class before a claim | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[1].next` | Qualify successor only; disclose 001 and G2; permanently end the family after PASS; no claim to change arm; P03 and owner target decision required | R18, R12, R29 | INH* | R4:L0247, L0158. T-B02-POST-PASS-DENIED. | ACCEPTED |
| `cases[1].when.claim` | `CLAIMED` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[1].when.class` | `PASS_WITH_SELECTION` | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[2].next` | Stop; no automatic 003; owner may defer or govern a specific new hypothesis within cap | R18 | INH* | R4:L0248. | ACCEPTED |
| `cases[2].when.claim` | `CLAIMED` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[2].when.class` | `AMEND` | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[3].next` | Stop; reopen owner-authenticity assumptions; no automatic new claim | R18 | INH* | R4:L0249. | ACCEPTED |
| `cases[3].when.claim` | `CLAIMED` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[3].when.class` | `REOPEN` | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[4].next` | Preserve; only a substantiated tested instrument repair with ALL_REQUIRED conditions may permit one exceptional claim within cap | R18, R13 | INH* | R4:L0250, L0241. | ACCEPTED |
| `cases[4].when.claim` | `CLAIMED` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[4].when.class` | `INVALID` | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[4].when.reason` | `INVALID_INSTRUMENT` | R13, R12 | INH* | R4:L0162–L0166 mechanical reason. | ACCEPTED |
| `cases[5].next` | Preserve after abort/external crash; no default retry; no instrument-repair exception; exception needs a new falsifiable hypothesis | R18, R11 | INH* | R4:L0251, L0242. | ACCEPTED |
| `cases[5].when.claim` | `CLAIMED` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[5].when.class` | `INVALID` | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[5].when.reason` | `INVALID_INCOMPLETE` | R13, R12 | INH* | R4:L0162–L0166 mechanical reason. | ACCEPTED |
| `cases[6].next` | Preserve; stop; no exception; new Research 513 preregistration required | R18, R13 | INH* | R4:L0252, L0241. | ACCEPTED |
| `cases[6].when.claim` | `CLAIMED` | R12, R18 | INH* | Distinct predicate triple (7/7 unique). | ACCEPTED |
| `cases[6].when.class` | `INVALID` | R12 | INH* | R4:L0144 (four classes; NOT_RUN is unscored). | ACCEPTED |
| `cases[6].when.reason` | `INVALID_INTEGRITY` | R13, R12 | INH* | R4:L0162–L0166 mechanical reason. | ACCEPTED |

### `claim_cap`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `claim_cap.absolute_new_claim_cap` | `2` new claims (002 and at most 003) | R18 | INH* | R4:L0240. T-B02-CAP-DENIED. | ACCEPTED |
| `claim_cap.attempt_claim_consumed_on_ctrl_c_or_power_loss` | `true` | R18, R17 | INH* | R4:L0242; must be in the owner disclosure (L0254). | ACCEPTED |
| `claim_cap.beyond_cap` | Separate Research 513 family preregistration amendment and owner decision | R18 | INH* | R4:L0240. | ACCEPTED |
| `claim_cap.exception_conditions[0]` | Bounded documented specific cause and explicit testable remedy | R18 | INH* | One of the five R4:L0241 common requirements; T-B02-4-OF-5-DENIED. | ACCEPTED |
| `claim_cap.exception_conditions[1]` | New owner authorization for the exact exception | R18 | INH* | One of the five R4:L0241 common requirements; T-B02-4-OF-5-DENIED. | ACCEPTED |
| `claim_cap.exception_conditions[2]` | Independent prospective review and new frozen artifacts | R18 | INH* | One of the five R4:L0241 common requirements; T-B02-4-OF-5-DENIED. | ACCEPTED |
| `claim_cap.exception_conditions[3]` | New exclusive claim, unique keys/namespace and complete evidence | R18 | INH* | One of the five R4:L0241 common requirements; T-B02-4-OF-5-DENIED. | ACCEPTED |
| `claim_cap.exception_conditions[4]` | Within the absolute new-claim cap | R18 | INH* | One of the five R4:L0241 common requirements; T-B02-4-OF-5-DENIED. | ACCEPTED |
| `claim_cap.exception_conditions_operator` | `ALL_REQUIRED` | R18 | INH* | R4:L0241 (never OR). | ACCEPTED |
| `claim_cap.first_new_claim` | Attempt 002 only after owner approves the stop policy **and** execution | R18, R21 | INH* | B02 supplied the policy approval; execution approval is still absent (R4:L0254, L0290). | ACCEPTED |
| `claim_cap.historical_claims_prior_to_successor_family` | `1` (Attempt 001) | R18, R29 | INH* | Distinct from the cap of two new claims (R4:L0240). | ACCEPTED |
| `claim_cap.instrument_exception` | May keep the original hypothesis only if a substantiated verifier/harness defect is fixed and prespecified | R18, R13 | INH* | R4:L0241, L0250. | ACCEPTED |
| `claim_cap.instrument_exception_only_if_source_flags_and_tested_remedy` | `ALL_REQUIRED`: source flags and a tested remedy | R18, R13 | INH* | R4:L0174 (later governance cannot change the subtype). | ACCEPTED |
| `claim_cap.integrity_breach_exception` | `FORBIDDEN_IN_THIS_FOLLOWUP_POLICY` | R18 | INH* | R4:L0241, L0252. Which conditions are INTEGRITY is partly open (B07-A3, recorded at R4:L0066/L0206). | ACCEPTED |
| `claim_cap.no_automatic_attempt_003` | `true` | R18 | INH* | R4:L0240. | ACCEPTED |
| `claim_cap.no_exception_after_invalid_integrity` | `true` | R18 | INH* | Duplicate of integrity_breach_exception; consistent. | ACCEPTED |
| `claim_cap.no_new_claim_after_pass_with_selection` | `true` | R18 | INH* | R4:L0247, L0279. | ACCEPTED |
| `claim_cap.other_exception` | AMEND/REOPEN/INCOMPLETE exceptions need a genuinely new falsifiable mechanism hypothesis | R18 | INH* | R4:L0241. | ACCEPTED |
| `claim_cap.owner_may_decline_preclaim_no_score` | `true` | R18, R12 | INH* | R4:L0239. | ACCEPTED |
| `claim_cap.pass_with_selection_G2_is_terminal` | `true` | R18, R12 | INH* | R4:L0158. | ACCEPTED |
| `claim_cap.prospective_family_start` | `ATTEMPT_002` | R18, R24 | INH* | R4:L0020. | ACCEPTED |
| `claim_cap.second_and_final_possible_new_claim` | `ATTEMPT_003_EXCEPTION_ONLY` | R18 | INH* | R4:L0240. | ACCEPTED |

### `draft_date`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `draft_date` | `2026-10-10` | - | N/A | Document drafting metadata (inventory: NON_NORMATIVE). | ACCEPTED |

### `draft_revision`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `draft_revision` | `DRAFT_REV_04_POST_MESSAGE_025` | - | N/A | Revision identity; exact content is bound by the approved SHA `9b5bbc4d…`, not by this label. | ACCEPTED |

### `evidence_disclosures`

| Unit | Value / normative meaning | IDs | Disp. | Basis, concerns and tests | Status |
|---|---|---|---|---|---|
| `evidence_disclosures.evidence.final_head_witness_absent.affects_primary_class` | `false` | R13, R16 | INH* | R4:L0138, L0231. T-WITNESS-DISCLOSURE. | ACCEPTED |
| `evidence_disclosures.evidence.final_head_witness_absent.can_authorize_new_attempt` | `false` | R13, R18 | INH* | R4:L0233. | ACCEPTED |
| `evidence_disclosures.evidence.final_head_witness_absent.meaning` | Independent final SHA-256/count/marker receipt unavailable before scoring; weaker tamper assurance | R16 | INH* | R4:L0138. | ACCEPTED |
| `evidence_disclosures.evidence.final_head_witness_absent.must_report` | `true` | R13 | INH* | R4:L0231 (in every report). | ACCEPTED |
| `evidence_disclosures.evidence.final_head_witness_absent.origin` | `SCORER_DERIVED` | R13 | INH* | R4:L0231. | ACCEPTED |

## 3. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
REV04_POLICY:attempt_terminal_vs_event_terminal.ctrl_c_or_crash|INHERITED_UNCHANGED|R17,R31,R11|ACCEPTED||REV04_POLICY:attempt_terminal_vs_event_terminal.ctrl_c_or_crash;REV04_CONTRACT-L0069;REV04_CONTRACT-L0114
REV04_POLICY:attempt_terminal_vs_event_terminal.dependent_controls|INHERITED_UNCHANGED|R26,C02,C13|ACCEPTED||REV04_POLICY:attempt_terminal_vs_event_terminal.dependent_controls;REV04_CONTRACT-L0069
REV04_POLICY:attempt_terminal_vs_event_terminal.no_process_resume|INHERITED_UNCHANGED|R31,R17|ACCEPTED||REV04_POLICY:attempt_terminal_vs_event_terminal.no_process_resume;REV04_CONTRACT-L0114
REV04_POLICY:attempt_terminal_vs_event_terminal.owner_input_R|INHERITED_UNCHANGED|R05|ACCEPTED||REV04_POLICY:attempt_terminal_vs_event_terminal.owner_input_R;REV04_CONTRACT-L0069
REV04_POLICY:attempt_terminal_vs_event_terminal.owner_input_S_or_non_R|INHERITED_UNCHANGED|R05,R26|ACCEPTED||REV04_POLICY:attempt_terminal_vs_event_terminal.owner_input_S_or_non_R;REV04_CONTRACT-L0060
REV04_POLICY:authority|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||REV04_POLICY:authority;reason=historical_drafting_attribution_superseded_by_B02_record
REV04_POLICY:browser_node_interrupt.candidate_process_isolation|INHERITED_UNCHANGED|R38,R17|ACCEPTED||REV04_POLICY:browser_node_interrupt.candidate_process_isolation;REV04_CONTRACT-L0112
REV04_POLICY:browser_node_interrupt.durable_event_receipt|INHERITED_UNCHANGED|R35,R16|ACCEPTED||REV04_POLICY:browser_node_interrupt.durable_event_receipt;REV04_CONTRACT-L0112
REV04_POLICY:browser_node_interrupt.missing_rp_receipt|INHERITED_UNCHANGED|R11,R35|ACCEPTED||REV04_POLICY:browser_node_interrupt.missing_rp_receipt;REV04_CONTRACT-L0112
REV04_POLICY:browser_node_interrupt.no_postinterrupt_rpc_dependency|INHERITED_UNCHANGED|R17,R35|ACCEPTED||REV04_POLICY:browser_node_interrupt.no_postinterrupt_rpc_dependency;REV04_CONTRACT-L0112
REV04_POLICY:browser_node_interrupt.owner_ctrl_c|INHERITED_UNCHANGED|R17,R13|PENDING|B08-A1_ABORT_VS_NODE_EXIT_TIEBREAK_NOT_FROZEN_DEFAULT_REBUTTAL_UNDEFINED|REV04_POLICY:browser_node_interrupt.owner_ctrl_c;REV04_CONTRACT-L0215
REV04_POLICY:browser_node_interrupt.unexpected_node_failure|INHERITED_UNCHANGED|R13,R35|PENDING|B08-A1_NODE_RP_FAILURE_CAUSAL_VS_TEMPORAL_PREDICATE|REV04_POLICY:browser_node_interrupt.unexpected_node_failure;REV04_POLICY:raw_flag_schema.node_rp_failure;REV04_CONTRACT-L0215
REV04_POLICY:cases[0].next|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[0].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[0].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[0].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[0].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[0].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[1].next|INHERITED_UNCHANGED|R18,R12,R29|ACCEPTED||REV04_POLICY:cases[1].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[1].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[1].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[1].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[1].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[2].next|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:cases[2].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[2].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[2].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[2].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[2].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[3].next|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:cases[3].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[3].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[3].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[3].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[3].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[4].next|INHERITED_UNCHANGED|R18,R13|ACCEPTED||REV04_POLICY:cases[4].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[4].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[4].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[4].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[4].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[4].when.reason|INHERITED_UNCHANGED|R13,R12|ACCEPTED||REV04_POLICY:cases[4].when.reason;REV04_CONTRACT-L0162
REV04_POLICY:cases[5].next|INHERITED_UNCHANGED|R18,R11|ACCEPTED||REV04_POLICY:cases[5].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[5].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[5].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[5].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[5].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[5].when.reason|INHERITED_UNCHANGED|R13,R12|ACCEPTED||REV04_POLICY:cases[5].when.reason;REV04_CONTRACT-L0162
REV04_POLICY:cases[6].next|INHERITED_UNCHANGED|R18,R13|ACCEPTED||REV04_POLICY:cases[6].next;REV04_CONTRACT-L0245
REV04_POLICY:cases[6].when.claim|INHERITED_UNCHANGED|R12,R18|ACCEPTED||REV04_POLICY:cases[6].when.claim;REV04_CONTRACT-L0276
REV04_POLICY:cases[6].when.class|INHERITED_UNCHANGED|R12|ACCEPTED||REV04_POLICY:cases[6].when.class;REV04_CONTRACT-L0144
REV04_POLICY:cases[6].when.reason|INHERITED_UNCHANGED|R13,R12|ACCEPTED||REV04_POLICY:cases[6].when.reason;REV04_CONTRACT-L0162
REV04_POLICY:claim_cap.absolute_new_claim_cap|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.absolute_new_claim_cap;REV04_CONTRACT-L0240
REV04_POLICY:claim_cap.attempt_claim_consumed_on_ctrl_c_or_power_loss|INHERITED_UNCHANGED|R18,R17|ACCEPTED||REV04_POLICY:claim_cap.attempt_claim_consumed_on_ctrl_c_or_power_loss;REV04_CONTRACT-L0242
REV04_POLICY:claim_cap.beyond_cap|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.beyond_cap;REV04_CONTRACT-L0240
REV04_POLICY:claim_cap.exception_conditions[0]|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.exception_conditions[0];REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.exception_conditions[1]|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.exception_conditions[1];REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.exception_conditions[2]|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.exception_conditions[2];REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.exception_conditions[3]|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.exception_conditions[3];REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.exception_conditions[4]|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.exception_conditions[4];REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.exception_conditions_operator|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.exception_conditions_operator;REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.first_new_claim|INHERITED_UNCHANGED|R18,R21|ACCEPTED||REV04_POLICY:claim_cap.first_new_claim;REV04_CONTRACT-L0290
REV04_POLICY:claim_cap.historical_claims_prior_to_successor_family|INHERITED_UNCHANGED|R18,R29|ACCEPTED||REV04_POLICY:claim_cap.historical_claims_prior_to_successor_family;REV04_CONTRACT-L0240
REV04_POLICY:claim_cap.instrument_exception|INHERITED_UNCHANGED|R18,R13|ACCEPTED||REV04_POLICY:claim_cap.instrument_exception;REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.instrument_exception_only_if_source_flags_and_tested_remedy|INHERITED_UNCHANGED|R18,R13|ACCEPTED||REV04_POLICY:claim_cap.instrument_exception_only_if_source_flags_and_tested_remedy;REV04_CONTRACT-L0174
REV04_POLICY:claim_cap.integrity_breach_exception|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.integrity_breach_exception;REV04_CONTRACT-L0252
REV04_POLICY:claim_cap.no_automatic_attempt_003|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.no_automatic_attempt_003;REV04_CONTRACT-L0240
REV04_POLICY:claim_cap.no_exception_after_invalid_integrity|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.no_exception_after_invalid_integrity;REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.no_new_claim_after_pass_with_selection|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.no_new_claim_after_pass_with_selection;REV04_CONTRACT-L0279
REV04_POLICY:claim_cap.other_exception|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.other_exception;REV04_CONTRACT-L0241
REV04_POLICY:claim_cap.owner_may_decline_preclaim_no_score|INHERITED_UNCHANGED|R18,R12|ACCEPTED||REV04_POLICY:claim_cap.owner_may_decline_preclaim_no_score;REV04_CONTRACT-L0239
REV04_POLICY:claim_cap.pass_with_selection_G2_is_terminal|INHERITED_UNCHANGED|R18,R12|ACCEPTED||REV04_POLICY:claim_cap.pass_with_selection_G2_is_terminal;REV04_CONTRACT-L0158
REV04_POLICY:claim_cap.prospective_family_start|INHERITED_UNCHANGED|R18,R24|ACCEPTED||REV04_POLICY:claim_cap.prospective_family_start;REV04_CONTRACT-L0020
REV04_POLICY:claim_cap.second_and_final_possible_new_claim|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_POLICY:claim_cap.second_and_final_possible_new_claim;REV04_CONTRACT-L0240
REV04_POLICY:draft_date|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||REV04_POLICY:draft_date;reason=drafting_metadata
REV04_POLICY:draft_revision|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||REV04_POLICY:draft_revision;reason=revision_label_content_bound_by_approved_sha256
REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.affects_primary_class|INHERITED_UNCHANGED|R13,R16|ACCEPTED||REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.affects_primary_class;REV04_CONTRACT-L0231
REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.can_authorize_new_attempt|INHERITED_UNCHANGED|R13,R18|ACCEPTED||REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.can_authorize_new_attempt;REV04_CONTRACT-L0233
REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.meaning|INHERITED_UNCHANGED|R16|ACCEPTED||REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.meaning;REV04_CONTRACT-L0138
REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.must_report|INHERITED_UNCHANGED|R13|ACCEPTED||REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.must_report;REV04_CONTRACT-L0231
REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.origin|INHERITED_UNCHANGED|R13|ACCEPTED||REV04_POLICY:evidence_disclosures.evidence.final_head_witness_absent.origin;REV04_CONTRACT-L0231
END_AUDIT_RECEIPT
```

Counts: 65 rows; 63 ACCEPTED; 2 PENDING; 0 SUPERSEDED_BY_REV04; 62 INHERITED_UNCHANGED; 3 NOT_APPLICABLE_TO_SUCCESSOR.

## 4. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source value of every unit above (each JSON leaf resolved from the committed blob and its `text_sha256` recomputed). I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited. PENDING items, including the classification-sensitive B05-A1, B07-A3 and B08-A1, remain open for ChatGPT reconciliation and are not resolved here.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE043=CLAUDE_AUDIT_BATCH010
DISPOSITION=AMEND_AUDIT_BATCH010
UNITS_AUDITED=65_OF_65
ACCEPTED=63
PENDING=2
KEY_FINDINGS=B10-F1_NODE_RP_FAILURE_CAUSAL_VS_TEMPORAL_PREDICATE_(B08-A1);CASES_7_DISTINCT;CLAIM_CAP_5_ALL_REQUIRED_CONSISTENT
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
