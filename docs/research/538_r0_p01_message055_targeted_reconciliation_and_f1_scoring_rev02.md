# Research 538: R0-P01 Message 055 independent challenge and prospective F1 scoring-boundary REV02

**Date:** 2026-10-11
**Status:** AMEND_REV01_TARGETED RECONCILED INTO UNFROZEN REV02 / INDEPENDENT TARGETED CONFIRMATION NEXT
**Parent:** Research 537 / Validation 226 / Checkpoint 873 / MC-0030 Message 055 (`19ea777ee191cac6c46bc1aac7c0edffb9093d1f`)
**Scope:** Reconcile Claude's independent critique, harden the exact source/peer-review safeguards, repair cross-platform pending-register hashes, and reserve only a *focused* technical continuation before F1 scoring-vector implementation.
**Authority:** Nonsecret public prospective scenario design and review only. No alteration of B01/B02-approved contract/policy, original Attempt 001, cryptographic scorer, F1/F2 freeze, new owner claim or physical architecture target.

## 1. Verified incoming reviewer result

GitHub compare from Checkpoint 873 HEAD `c75c346b17f3f420b4eb58d73dcefda775dfdd63` showed exactly one new file, Message 055; guarded Runtime Bridge pull was initially rejected because the workspace contained old untracked `.tmp` unit-test directories. The directories were **not deleted**. Git rejected an attempt to add a narrow local-only `.git/info/exclude` entry with access denied, leaving that file unchanged. To preserve all old artifacts and avoid bypassing the purpose-specific fast-forward Git control plane, the entire former `.tmp` directory was atomically moved into the already Git-ignored local-only folder `.venv/.ads-preserved-untracked-temp-pre-message055-20261011`, retaining all three top-level child directories. Guarded `codex_git_pull_ff_only` subsequently succeeded, reaching exactly `19ea777ee191cac6c46bc1aac7c0edffb9093d1f`.

Message 055's signed-off reviewer verdict is `AMEND_REV01_TARGETED`: of 17 initial matrix cases, 8 CONFIRMED_AS_STATED, 9 AMEND_PRECONDITION_OR_CONCLUSION, 0 REJECT_UNSUPPORTED and 0 NEEDS_OWNER_INTERPRETATION. Claude identified seven omitted scoring-sensitive cross-family scenarios and seven guard/data-assurance gaps V1–V7. It remains a source-technical critique, not an F1-scoring oracle.

## 2. Reconciliation decisions

The original Research 537 REV01 matrix and source guard remain preserved as historical draft artifacts. A **distinct REV02** candidate is created at `docs/research/r0_p01_successor_design/R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV02_UNFROZEN.json`. No historical Claude batch message or Message 055 was rewritten. The REV02 candidate includes 24 exact source-grounded scenarios: **17 narrow SOURCE_DETERMINED candidate implications**, **7 CANDIDATE_BLOCKED** unresolved interpretations. The designation SOURCE_DETERMINED is not a globally scored, qualified outcome and is subject to independent semantic confirmation.

The 9 amended initial cases are S1-02, S1-04, S2-02, S2-03, S2-04, S3-01, S3-02, S3-04 and S4-01. Claude's 8 original confirmed findings are retained. The 7 new cross-family case IDs retain independent provenance: X1 owner Ctrl+C racing the third native SSH attempt; X2 RP-only timeout without browser credential invocation; X3 Ctrl+C during crash-atomic snapshot publication; X4 false NOT_REALIZABLE suppressing G2 disclosure; X5 independently proven RP fault overriding an already eligible Arm A; X6 recurring no-proof native tool failure exhausting the bounded SSH budget; X7 Arm C attestations must not enter A/B G1 evidence-state denominator.

**S1/B05, capability and event completion:** An RP issue/expiry alone is not shown to be a completed owner ceremony; REV02 requires corroborated client `navigator.credentials.get()` invocation and a correctly bound durable RP consume receipt for S1-02. A postregistration NotSupportedError *without* frozen capability evidence is not sufficient for B NOT_REALIZABLE or event-terminal COMPLETED. The inherited V01_CONTRACT-L0223/L0231 and the two specific NotSupportedError JSON leaves are now explicitly cited. Whether a demonstrated independent assertion-only incapability after successful registration may qualify as NOT_REALIZABLE remains BLOCKED. The exact client receipt standard still requires independent review; a technical strengthening must not silently narrow human B01 acceptance of a genuinely consumed NotAllowedError owner event.

**S2/B07, source site, private-header property and fault origin:** A genuinely verified public-key/member mismatch or encryption property violation after postclaim setup is not an unreadable file or a bytewise private-header difference. A legitimate private-key passphrase change can alter salts without removing encryption or changing the public key; REV02 no longer automatically labels this as public-key identity tampering. Executable process creation failure at an inventoried postclaim launch site is INSTRUMENT only under independently intact evidence; precheck inability and successful process launch with nonzero/no sig are distinct and must not be conflated. Precheck failures without proven source site and immutable receipt remain BLOCKED. The approved `COMPLETED` terminal enumeration must not be expanded by a generic PRECHECK_FAILED token.

**S3/B08, Ctrl+C/RP and late receipts:** An unexpected RP failure classification requires `HARNESS_RECORDED` source authority and verified Windows isolation, not a self-reported RP crash or absolute timestamps across unrelated monotonic domains. Harness-observed ordering and independent causal receipts distinguish cleanup from an unprovoked RP fault. Unorderable abort/fault races may not be upgraded to the B02 favorable instrument-repair exception without a prior frozen evidence burden. Any late recovered **successful** RP assertion without in-run completed VERIFY must remain an unverified/incomplete proof event, preserving bytes for disclosure rather than retrospectively creating viability. Scenario S3-03 retains a blocked classification/tie-break rule, pending independent technical review.

**S4/B11, terminal alias:** Under *fully evidenced* three native calls (all nonzero/no signature, exact owner R after the first two, same statement/timer, no overlapping Ctrl+C), REV04 `PROOF_NOT_CREATED` and the approved policy enum `SSH_UNLOCK_BUDGET_EXHAUSTED` refer to the same B01 terminal no-proof observation. REV02 promotes S4-01 from blocked to source-determined **representation-only**, with a reversible raw-token record and normalization to the approved policy enumeration, subject to independent review. Not permitted: absent calls, owner S or non-R, partial files, exit 0, fourth call, or owner abort during call 3. X1 specifically prevents an interrupted owner run from being silently recorded as completed budget exhaustion.

## 3. Strengthened guard without inventing normative authority

The new, separate `scripts/check_r0_p01_scoring_boundary_rev02.py` pins the **exact 24 scenario IDs and each anticipated reviewer-determined vs blocked status**. It carries forward the independent Message 055 per-case disposition, exact original B01/B02 bytes and acceptance receipts, valid predecessor V01/V02 source IDs, explicit conditional whole-attempt premises (other arm, proof viability, raw flags, isolation, flag origin, receipt producer), and nonempty machine-readable `blocked_reason` for every unresolved scenario. It does **not** rely on the former keyword heuristic. Guard success cannot be achieved by simply deleting S3-03, relabelling it SOURCE_DETERMINED, removing X1, omitting inherited NotSupportedError/V01 source units, or fabricating closed task-owner decisions.

Every one of the 18 source-unit rows in the existing 55-entry pending register associated with these four scoring gates has an explicit REV02 `open_gate_pending_coverage` entry, currently all **18 cited by scenario IDs**. Their `task_owner_resolution` still stays `UNRESOLVED`. The other 37 reviewer-pending source units are unaffected by this four-gate review. Old REV01 historical files are preserved rather than overwritten. No source-level reviewer ACCEPTED or newly `SOURCE_DETERMINED` scenario counts as runtime verifier qualification.

## 4. Corrected committed-Git-blob hash basis

Claude's V7 finding is independently reproduced: on Windows, working-copy Message 033 hashed to `f6f8a87690860d047c50ab8d0a1ad3a3ff5a325144f7218645f9c2cd56429842`, but the **committed Git LF blob** hashes to `d46897a99f0880596d1eef63d6475911e131bb5d95a339da9c10156b65097244`. Previously the machine-generated reviewer pending register indexed the checkout-converted CRLF copy, making CI/Linux reproducibility false despite local PASS.

`scripts/check_r0_p01_pending_review_register.py` now reads exact historical blobs through read-only `git show HEAD:path` for **each reviewer message and the source inventory**, and the same 55-row unfrozen candidate register was regenerated from those blobs. The revision includes an explicit `hash_basis` indicator. This does not alter any historical reviewer message, approved source or per-unit disposition; it only corrects the synthetic index of committed evidence. New tests verify committed-blob identities and a simulated CRLF encoding cannot be mistaken for the committed blob hash. Every pending task-owner resolution remains `UNRESOLVED`.

## 5. Proportional next technical stage

The first independent audit campaign is already finished. This is a focused reconciliation of the scoring-sensitive subset, not a repeat of 18 batches. Before freezing any scorer, one independent Claude challenge should confirm the nine amendments, seven cross-family additions, the S4 alias scope, the no-post-hoc VERIFY distinction and the four still-disputed scoring families, plus check the stronger guard's *actual* negative behavior. Then the task owner can prepare one bounded technical decision/attempt-level counterexample table, including all seven precedence rows under fully fixed input flags, with separate blind oracle work only after reviewed source obligations exist.

No further owner interpretation is currently requested. The OI-1/2/3 alternatives Claude identified would require separate owner decisions **only if** someone proposes modifying B01 NotAllowedError acceptance, treating unsupported RP/abort ambiguity as a favorable instrument exception, or weakening the approved identity/agent integrity rule. The conservative prospective source reading does not request any of those changes.

The human owner does not need to relay 18 batch prompts again. Normal ChatGPT–Claude manual collaboration remains intact. No new owner credential operation or Attempt 002 claim is authorized. P02 PASS, P03 pending, physical target unselected, Specification 028 unchanged.

```text
RESEARCH_538=CLAUDE055_AMEND_REV01_TARGETED_RECONCILED_AS_REV02_CANDIDATE
CLAUDE055=8_CONFIRMED_9_AMEND_0_REJECTED_0_OWNER_INTERPRETATION
REV02_CASES=24
SOURCE_DETERMINED=17
CANDIDATE_BLOCKED=7
SCORING_GATE_PENDING_ROWS=18_OF_18_REFERENCED_NOT_APPROVED
COMMITTED_GIT_BLOB_HASH_BASIS=CORRECTED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
