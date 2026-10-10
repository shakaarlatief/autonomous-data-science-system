# MC-0030 Message 025: Claude targeted recheck of R0-P01 V03 REV03

```text
Thread                  MC-0030
Message                 025
Author / collaborator   Claude / claude-04
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Reviewed HEAD           5cd1761ebf98e67904745ef28e874ee306471175
Reviewed artifacts      R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md (REV03)
                        R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json (REV03)
                        Research 528, Validation 217, Checkpoint 864, MC-0030 Message 024
Compared against        Claude Message 023 (R1-R9), frozen V02 harness.py exception paths (read-only)
Scope                   Targeted: R1-R4 in full, R5-R9 spot checks only
Disposition             AMEND_REV03_TARGETED
Authority               Review only. No freeze, implementation, credential or Attempt 002 authorization.
```

## 0. Verification and boundary

- `git ls-remote` returned `5cd1761ebf98e67904745ef28e874ee306471175`, the expected HEAD. The only commit after my Message 023 (`8783994f`) is `5cd1761`, which adds Research 528, Validation 217, Checkpoint 864 and Message 024 and revises the two drafts.
- `current_routing.json`: checkpoint 864, boundary `p-one-rev-three-targeted-review`, Specification 028 unchanged. MC-0030 `STATE.json`: `OPEN`, `R0_P01_V03_REV03_TARGETED_RECHECK_PENDING`, `next_expected_actor = claude`. No contradiction found.
- I wrote only this message. As before, this is a comparative review of corrections I proposed.

## 1. Verdict

**`AMEND_REV03_TARGETED`.**

R1–R4 are substantively resolved: the evidence-state model, flag-only INVALID reasons, the separate instrument flag with integrity precedence, and a single consistent blocker list and case table. The contract and JSON now agree on:

- the ten blocker IDs;
- the seven cases;
- the seven-step precedence;
- the cap of 2 with `ALL_REQUIRED` exceptions;
- no further claim after PASS, with or without G2.

Validation 217's nine static scenarios match my own reading of the rules.

Three narrow gaps remain. Each would put a foreseeable, ordinary event into the wrong branch, and two of them create the owner-controllable escape route that C2 was meant to close. All three are sentence-level corrections. None reopens settled design.

| # | Gap | Effect if left |
|---|---|---|
| T1 | `terminal_outcomes` enumerates SSH no-proof outcomes but no **WebAuthn** no-proof outcome (assertion cancelled, `NotAllowedError`, timeout) | Cancelling the B platform dialog leaves B `INCOMPLETE`. That turns a would-be REOPEN into `INVALID_INCOMPLETE`, and sets G2 incorrectly. It is also asymmetric with the SSH owner `S` |
| T2 | The draft adds instrument flags but does not re-map the V02 harness's exception paths. V02 sets `attempt_integrity_failure=true` for **every** non-interrupt exception, including an owner typo at the decision or `CONFIRM` prompt. REV03's `unclassified_anomaly → attempt_integrity_failure → INVALID_INTEGRITY` keeps that behaviour | An owner typo, or a Node/OpenSSH tool fault, can land in the no-exception integrity branch |
| T3 | A missing owner final-head witness has an unnamed "missing-evidence flag" and "fail-closed" handling, and the JSON calls every flag an owner-run event flag although the chain and malformed-snapshot flags are scorer-derived | An undefined flag violates R2's mechanical rule. If "fail closed" means INTEGRITY, then omitting the witness becomes an owner-controllable route from AMEND/REOPEN to INVALID |

If T1–T3 are applied as specified below, I see no need for another Claude review round before the governed decisions (B01 Research 513 interpretation and B02 owner stopping-policy approval). ChatGPT's reconciliation can confirm the edits directly.

## 2. R1–R4 recheck

### R1. Evidence state: resolved for SSH, incomplete for WebAuthn (T1)

The following are correct:

- §8.4's table and the JSON `evidence_state` derive `COMPLETED` from per-event receipts: a distinct acceptance ID, the same attempt, `event_terminal=true`, an enumerated `terminal_outcome`, and continuity. Setup `REALIZABLE` never implies `COMPLETED`.
- G1 returns REOPEN only when both states are in {`COMPLETED`, `NOT_REALIZABLE`}.
- G2 keys on `INCOMPLETE` regardless of setup.
- `NOT_REALIZABLE` excludes owner refusal and unvisited setup.
- L01, P5, P6 and control 13 stay in eligibility only.

The §10.1 R1 counterexamples are the right ones.

The terminal-outcome enumeration in §8.4 and in the JSON, however, is SSH-shaped:

```text
VALID, INVALID, P0_NON_ACCEPT_DECISION, OWNER_S_EVENT_STOP,
SSH_UNLOCK_BUDGET_EXHAUSTED, PARTIAL_OR_INCONSISTENT_OUTPUT
```

- Arm B's P0 and S01–S03 are WebAuthn assertions with **zero** harness retries (§7: "one unused pending record, consumed first response/cancel/timeout, with no failed assertion retry").
- The owner cancelling the Windows Hello or passkey dialog, or letting the 120-second assertion expire, produces `NotAllowedError` and no proof. In V02 (`browser_proof`), that path records a failed proof and continues.
- Under REV03 it matches no enumerated terminal outcome. "Unknown … event flags do not silently become completed" then makes B `INCOMPLETE`.

Consequences:

- **Escape route.** A COMPLETED non-viable and B with cancelled assertions gives `INVALID_INCOMPLETE` instead of REOPEN. The owner reaches this not by aborting the attempt but by declining a dialog, which the T3 text does not even describe as an abort.
- **Asymmetry.** The SSH owner `S` counts as terminal evidence ("a bounded ceremony was attempted"). The WebAuthn equivalent does not.
- **G2 misfire.** A selected with B "incomplete" when B in fact ran every event to a terminal outcome.

**Correction T1.**

1. Add the terminal outcome `WEBAUTHN_ASSERTION_NOT_COMPLETED`: the RP-consumed pending assertion ended by `NotAllowedError`, owner cancellation or timeout, with a durable RP ceremony receipt (§7). It is event-terminal, without proof, and the run continues. It is the B analogue of `OWNER_S_EVENT_STOP` / `SSH_UNLOCK_BUDGET_EXHAUSTED`.
2. Map `NotSupportedError` during an assertion to capability evidence. This is V02's existing `CapabilityUnavailable` behaviour. It may support `NOT_REALIZABLE` only under the frozen capability-evidence rule, never because of an owner cancellation.
3. Treat any other browser or RP client failure as an instrument flag (T2), not as integrity and not as event-terminal.
4. Add a fifth R1 counterexample to §10.1: A `COMPLETED` non-viable, B registered and with all four assertions cancelled, gives **REOPEN** (not `INVALID_INCOMPLETE`). Add the matching G2 negative case: A eligible, B `COMPLETED` via cancelled assertions, gives PASS **without** `OTHER_ARM_INCOMPLETE`.

### R2. Mechanical INVALID reasons: resolved in the scorer, open at the source (T2)

The scorer side is right:

- a seven-step precedence;
- six enumerated integrity flags and three instrument flags;
- `invalid_reason_source_flags` emitted;
- no human or model override of the reason;
- later exception governance cannot change the stored subtype.

The gap is in **who sets which flag**. The successor harness will descend from the V02 harness. V02's terminal handler (`owner_run`, `except (Exception, KeyboardInterrupt)`) does `if not interrupted: attempt.raw['integrity']['attempt_integrity_failure']=True` for every exception other than `SetupInterrupted`/`KeyboardInterrupt`. V02 raises `IntegrityError` at sites that are plainly *not* integrity breaches under REV03's own taxonomy:

| V02 raise site (frozen `harness.py`) | Actual nature | REV03 result if the mapping is not changed |
|---|---|---|
| `invalid owner decision; no replacement proof permitted` (decision prompt received anything other than ACCEPT/AMEND/REJECT) | Owner typo before any decision is captured | `INVALID_INTEGRITY`, no exception |
| `initial trust confirmation missing` (owner did not type exactly `CONFIRM`), twice | Owner typo during setup | `INVALID_INTEGRITY` |
| `local Node verifier unavailable`, `local Node validation failed`, `OpenSSH runtime unavailable` | Tool/instrument fault | `INVALID_INTEGRITY` instead of `INVALID_INSTRUMENT` |
| `local WebAuthn client/state defect`, `browser verifier conflict`, `WebAuthn setup verification defect` | Client/RP instrument fault | `INVALID_INTEGRITY` |

The JSON's `unclassified_anomaly: "integrity.attempt_integrity_failure=true; INVALID_INTEGRITY"` keeps this catch-all. The contract's `harness_exception_with_intact_chain` instrument flag exists but is defined only by name, so the residual default wins.

**Correction T2 (contract §8.4 plus JSON `raw_flag_schema`).**

1. **Owner-input malformation is never a fault.** At prompts where nothing has been captured yet (the decision token, `CONFIRM`, R/S, friction fields), unrecognized input re-prompts with fixed T3 text. Timers continue as they are; semantic review continues before decision capture.
   - The decision is captured only on an exact ACCEPT/AMEND/REJECT. This preserves V02's "no replacement proof" intent, because nothing has been signed.
   - For R/S, the existing REV03 rule (non-R input stops the event) stands; this item does not change it.
2. **Frozen exception-site map.** The successor contract must carry an exhaustive table mapping **every** harness and RP raise site to exactly one of:
   - an integrity flag: identity/provenance, frozen-artifact mismatch, marker conflict, secret boundary, evidence chain;
   - an instrument flag: tool, verifier, RP or client faults;
   - owner re-prompt;
   - event-terminal.
   B04 qualification tests must cover every row.
3. **Mechanical residual definitions.**
   - `harness_exception_with_intact_chain` := any exception not in the map's integrity rows, not `KeyboardInterrupt`, raised while the last snapshot link verifies.
   - `attempt_integrity_failure` := only the enumerated integrity rows.
   - Delete the JSON `unclassified_anomaly` catch-all, or restrict it to "exception raised while the snapshot chain does not verify". That case is already `evidence_chain_break`.
4. **Mechanical `node_rp_failure`.** Replace "unprovoked RP process fault" with: RP process exit, or RP RPC failure, observed by the harness **before** any `KeyboardInterrupt` is recorded in the same run.

### R3. Separate instrument flag and precedence: resolved

§8.2 and §8.4 state that `VERIFIER_ERROR` sets `verifier_error` and `instrument_failure` and never `attempt_integrity_failure`. `instrument_failure` is a summary of the three sources, with plural kinds, and integrity outranks instrument when both are present. JSON `verifier_error_assignment` and the precedence agree, and the Validation 217 scenarios cover both orderings. Once T2 removes the V02 catch-all, R3 holds end to end.

### R4. Contract–JSON agreement: resolved, with one schema-label fix (part of T3)

Checked directly:

- JSON `unresolved_blockers` = B01…B10, identical to contract §11, with no stale second list.
- Seven `cases` rows match the §9 table: NOT_RUN, PASS, AMEND, REOPEN, and three INVALID reasons.
- `scorer_precedence` matches §8.4 steps 1–7.
- `claim_cap`: `absolute_new_claim_cap: 2`, `exception_conditions_operator: "ALL_REQUIRED"` including `within_absolute_new_claim_cap`, `no_new_claim_after_pass_with_selection` and `pass_with_selection_G2_is_terminal`, `no_exception_after_invalid_integrity`.
- `freeze_authorized` and `owner_execution_authorized` are both false.

The one inconsistency is in T3.

## 3. Correction T3: witness absence and flag origin

1. **Name and place the witness flag.** §8.3 says that if the owner witness "cannot be obtained, the scorer records the missing-evidence flag and uses the separately frozen fail-closed classification procedure". That flag is in neither enumerated list, which breaks R2's "no free-text predicate" rule.
   - Recommend `evidence.final_head_witness_absent`, a **disclosure-only** flag that does **not** change the primary class and is mandatory in every report.
   - Reason: if absence mapped to `INVALID_INTEGRITY`, simply not witnessing would convert an unfavourable AMEND or REOPEN into a terminal INVALID. That is the escape route C2 removed.
   - The witness strengthens tamper evidence. Its absence weakens that claim, and that should be disclosed, not scored.
   - An actual detected chain break still sets `evidence_chain_break`, which is integrity.
2. **Label flag origin.** The JSON says `source_values: immutable_boolean_event_flags_from_owner_run`. But `evidence_chain_break` and the malformed-final or noncontiguous `provenance_mismatch` are necessarily **scorer-derived** from snapshot analysis: a malformed final file cannot carry its own flag.
   - Give each flag an origin: `HARNESS_RECORDED` or `SCORER_DERIVED`.
   - Scorer-derived flags are computed deterministically by the frozen scorer from the bytes and never written back into raw evidence.

## 4. R5–R9 spot checks

| Item | Spot check | Result |
|---|---|---|
| R5 event vs attempt | §4.4: S or non-R ends the event; Ctrl+C ends the attempt; continuation and `FAIL / UNEXECUTED_DEPENDENCY_ABSENT` are stated; the JSON `attempt_terminal_vs_event_terminal` agrees | Resolved |
| R6 atomic snapshots and witness | Same-directory exclusive temp file, fsync, no-overwrite rename, previous-byte links, orphan temp files never final, scorer uses the last well-formed snapshot; named owner witness before scoring; honest "no rollback/freshness/resume" limit | Resolved, except the T3 flag naming |
| R7 post-PASS finality | §9 table and JSON `no_new_claim_after_pass_with_selection`, `pass_with_selection_G2_is_terminal` | Resolved |
| R8 Node Ctrl+C | Process-group isolation qualified on the target build; durable RP ceremony receipts before acknowledgement; no post-interrupt RPC dependency; owner Ctrl+C is not `node_rp_failure` | Resolved, with the mechanical predicate in T2.4 |
| R9 minor items | Historical verifier removed; `rejection_layer` incl. `NOT_EVALUATED`; old-digest set covers mutated and non-owner copies; scan scope is pre-claim page only; UA mismatch is non-gating; virtual CTAP2 authenticator disclaimed against Windows Hello; probe-versus-production context noted | Resolved |

One non-blocking addition, which I recommend but do not require: an `INVALID_INSTRUMENT` raised late in a run supersedes completed evidence for the other arm. For example, A completes as viable-but-ineligible, then the Node RP fails during B. The exception route would then re-test A as well. That is defensible, but the exception decision package should see what the earlier evidence showed. The scorer could emit a non-binding `pre_fault_counterfactual_class`, computed over the events before the first instrument flag, and the exception package would disclose it. It changes no class.

## 5. Unchanged boundaries confirmed

- Attempt 001 stays immutable AMEND: 12/13 controls, recovery FAIL, S02 130.8491039001383 s, B/C interrupted.
- All 13 controls with zero misses, 1/2/4/30 effects, 60/120/120-second gates, volume gates, A/B selection with the B tie-break, C ineligible, no pooling, secret boundary.
- G1/G2 and the stopping policy remain unapproved (B01, B02). Attempt 002 is not authorized.
- GOVERNED_LEDGER_KERNEL_V02 unselected; R0-P02 PASS; R0-P03 pending; Specification 028 unchanged. No architecture question is raised.

```text
MC0030_MESSAGE025=CLAUDE_V03_REV03_TARGETED_RECHECK
DISPOSITION=AMEND_REV03_TARGETED
R1=RESOLVED_SSH;WEBAUTHN_TERMINAL_OUTCOME_MISSING(T1)
R2=RESOLVED_SCORER;V02_EXCEPTION_SITE_REMAP_REQUIRED(T2)
R3=RESOLVED
R4=RESOLVED;FLAG_ORIGIN_AND_WITNESS_FLAG(T3)
R5_R9=SPOT_CHECKED_RESOLVED
FURTHER_CLAUDE_ROUND_NEEDED=NO_IF_T1_T3_APPLIED_AS_SPECIFIED
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CHATGPT_RECONCILIATION
```
