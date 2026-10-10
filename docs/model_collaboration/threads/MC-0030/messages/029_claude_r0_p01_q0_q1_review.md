# MC-0030 Message 029: Claude review of R0-P01 successor Q0 trace and Q1 implementation boundary

```text
Thread                  MC-0030
Message                 029
Author / collaborator   Claude / claude-04
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Reviewed HEAD           58cef4c634eb66655fcbac1820c51e76797c96d3
Reviewed artifacts      R0_P01_Q0_REQUIREMENTS_TRACE_UNFROZEN.json
                        R0_P01_Q1_IMPLEMENTATION_BOUNDARY_CANDIDATE.md
                        scripts/check_r0_p01_successor_trace.py
                        tests/unit/test_r0_p01_successor_trace_guard.py
                        Research 531, Validation 220, Checkpoint 867, MC-0030 Message 028
Consulted (read-only)   Research 513 §5; approved REV04 contract and policy; B01/B02 receipt;
                        frozen V02 fixture, result contract, addendum, harness.py, webauthn_server.mjs
Disposition             AMEND_Q0_Q1_BEFORE_FREEZE
Authority               Review only. No fixture freeze, implementation, credential, WebAuthn ceremony or Attempt 002.
```

## 0. Verification and boundary

- `git ls-remote` returned `58cef4c634eb66655fcbac1820c51e76797c96d3`, the expected HEAD. Three commits follow my Message 025 (`1a331cf2`): `8361907` (REV04 and governed decisions), `323acf5` (human B01/B02 acceptance receipts) and `58cef4c` (Q0 trace and Q1 candidate).
- `current_routing.json`: checkpoint 867, boundary `p-one-qone-architecture-review`, Specification 028 unchanged. MC-0030 `STATE.json`: `OPEN`, `R0_P01_Q0_QUALIFIED_Q1_DESIGN_REVIEW_PENDING`, `next_expected_actor = claude`, Claude write surface `messages/**`. No contradiction found.
- **Independent hash recomputation.** All seven `historical_artifacts` SHA-256 values and both approved hashes (contract `9160a30c…`, policy `9b5bbc4d…`) match the **Git-blob (LF)** bytes at this HEAD. None of those files contains CRLF.
- **Trace counts.** The trace has 34 requirements (C01–C13, R01–R21), 68 test-ID references and 64 unique IDs, consistent with Research 531.
- I wrote only this message. I do not reopen B01/B02. Where I found a gap in the approved REV04 itself (Q-3 below), I classify it as a fixture-level clarification that is consistent with the approved rules, not as an owner-policy amendment.

## 1. Verdict

**`AMEND_Q0_Q1_BEFORE_FREEZE`.**

The approach is right and should not be reopened:

- a requirements trace before any fixture work;
- an explicit split between static traceability and behavioural qualification;
- the Q0→Q6 staging, with a third human approval gating any real claim;
- candidate B's separation of pure semantics, platform adapters, evidence and an independent scorer.

The guard is careful: exact bytes, duplicate-key rejection, no imports of owner code, and status fields that cannot claim qualification.

Three things must change before the exact fixture design is frozen:

1. **Q0 is not complete against REV04, and nothing in it could notice that.** The 34 rows are hand-authored, and several REV04 obligations are absent (Q-1). The guard verifies the rows that exist but cannot detect a missing one. A clause-level completeness index is needed.
2. **"Independent scorer" and "independent oracle" are stated as goals, not designed** (Q-2). Q1 must specify *what* is independent of *what*, and how that is enforced. Otherwise the expected values will be produced by running the implementation, and the qualification becomes circular.
3. **The freeze sequencing conflates two different freezes** (Q-4). Some required evidence, notably the exception-site map (R15), depends on the implementation and cannot be frozen with the pre-implementation fixture.

The other findings are concrete design and test corrections.

## 2. Findings

### Q-1. Q0 omits REV04 obligations, and the guard cannot detect omissions (blocking)

A keyword and row-by-row check of the trace against the approved REV04 contract found these normative obligations with **no** requirement row:

| REV04 obligation (approved bytes `9160a30c…`) | Status in Q0 |
|---|---|
| Pre-claim reachability-only browser mode, forbidden-API scan scoped to the pre-claim page, UA and launch-method receipt, non-gating `ua_matches_preflight` (§7, B06) | Absent. R06/R07 cover only the post-claim RP |
| Old canonical-statement digest set (full Attempt 001 coverage including mutated and non-owner copies; count and sorted-set hash frozen; runtime refusal) and local old-public-ID inequality (§2.4, §2.7, §8.5) | Absent. R01 covers only structural context/prefix rejection |
| Start-claim binding contents (protocol ID, contract/fixture/harness/scorer hashes, T3 hashes, prior claim hash, prior snapshot hash, authorization reference) (§2.2, §8.3) | Absent. R16 says only "exclusive claim" |
| P0/P5/P6 require owner ACCEPT; a different decision is a failed positive control and is not retried (§5) | Absent |
| Event continuation after a terminal no-proof event, and dependent controls `FAIL / UNEXECUTED_DEPENDENCY_ABSENT` (§4.4, §8.4) | Absent. R17 says only that S does not stop the process |
| `mechanical_interaction_floor`, per-invocation monotonic landmarks, browser-monotonic assertion landmarks, no clock stitching (§6, §8.3) | Absent. R08 covers only gate timing |
| Optional `consulted_before_decision`; semantic review ungated (§6) | Absent |
| No pooling with Attempt 001; side-by-side reporting with the Attempt 001 AMEND; repeated-participant (practice) disclosure (§1, §9, policy `reporting`) | Absent |
| Arm C exactly S01 and L01, user-authored line, task-owner receipt, no timing gate, controls NOT_APPLICABLE (§5) | Partial (R04) |
| Same-process between-arm pause only, outside scored events (§7) | Absent. R17 covers only "no resume" |
| Scorer re-run on unchanged bytes gives an identical derived result (pending-state semantics, §8.1) | Absent |

A missing row is exactly the failure that a hand-authored trace plus a row-shape guard cannot catch. **Correction:**

1. Add a **normative clause index** to Q0. It lists every normative unit of the approved REV04 contract and policy:
   - each numbered item, table row and named rule in §1–§11;
   - each JSON key under `claim_cap`, `guards`, `evidence_state`, `raw_flag_schema`, `attempt_terminal_vs_event_terminal`, `snapshot_evidence`, `browser_node_interrupt` and `reporting`.

   Each clause is mapped to ≥1 requirement ID or to an explicit `NON_NORMATIVE` / `GOVERNANCE_ONLY` disposition with a reason.
2. Extend the guard to fail on any unmapped clause, and on any requirement row that cites no clause. The clause index can be generated semi-mechanically from headings, numbered lists and table rows, then reviewed. It must be bound to the approved source hashes, so a later edit to the approved text cannot leave the index silently stale.
3. Bind each C row to its control key explicitly (`"control_key": "CROSS_PROJECT_REPLAY_REJECTS"`) and make the guard check C01..C13 ↔ `fixture.security_controls[0..12]` positionally. Today the C rows are linked to controls only by count and prose.
4. Add a **test catalogue**: one record per test ID with the following fields, and make the guard enforce bidirectional coverage between catalogue and requirements.
   - layer: `PURE`, `SCORER_ORACLE`, `WINDOWS_NATIVE`, `BROWSER_VIRTUAL`, `INTEGRATED_SYNTHETIC` or `OWNER_MACHINE_MANUAL`;
   - oracle source: frozen vector, decision table, or second implementation;
   - which component it must *not* share code with.

   Today the 64 IDs are free strings, so a typo creates a phantom obligation that nothing ever has to satisfy.

### Q-2. Make oracle and scorer independence concrete and enforceable (blocking)

Q1 §3 correctly states that "a shared production crypto primitive cannot itself serve as independent evidence". It does not yet say how independence is achieved. There are three distinct circularity risks.

**(a) Expected bytes produced by the implementation under test.** Golden statement and view bytes, P5/P6 instantiations and envelope digests cannot be "independently authored" by hand at scale, and running the harness to produce them makes the tests circular.

- **Correction:** generate golden vectors with **two independently written implementations** of the pure layer, in different languages or by different authors. Natural candidates are a Python core and a Node implementation built only on Node built-ins.
- Freeze the vectors only where both agree byte-for-byte. Record any disagreement as a spec ambiguity to resolve in the fixture, never by picking a winner.
- This mirrors the blind dual-evaluator pattern the project already used in MC-0029 D-1/D-2, applied to canonicalization, rendering and classification, which are exactly the functions whose bugs would be shared.

**(b) Scorer reusing harness code or tools.**

- **Correction:** the scorer is a separate package that **must not import** harness or core modules. Enforce this with an import-graph test that fails on any edge from the scorer to the harness.
- The scorer reconstructs canonical statements, rendering, signer-set history and admission from public evidence plus the frozen fixture data alone.
- **Cryptographic independence.** The harness verifies SSHSIG with `ssh-keygen -Y verify`. The scorer should verify **in-process** with an independent implementation:
  - parse the SSHSIG armour and blob;
  - rebuild the signed data (`"SSHSIG"`, namespace, reserved, hash algorithm, H(message));
  - verify Ed25519 using either Node's built-in `crypto.verify` or a hash-pinned Python library.

  This gives genuine verifier diversity and also removes the temporary-file dependency that caused the Attempt 001 readOnly false `INVALID`. ES256 assertions: Node `crypto` or the same pinned library, with no code shared with the RP module.

**(c) Classification expectations derived from the scorer.**

- **Correction:** freeze the B01/B02 **decision table as data** before any scorer exists. Rows are scenario predicates (evidence states, flags, viability, eligibility, volume); outputs are the expected class, the reason and the G2 flag.
- Check the scorer against that table, which is the oracle. Validation 217/218's nine-plus scenarios are a seed, but the table should be exhaustive over the predicate lattice: three evidence states per arm, viable/eligible combinations, integrity and instrument flag sets, and volume pass/fail.

### Q-3. P5/P6 templates: anti-substitution check, and a missing B→A rotation dependency

1. **Template mechanics are sound in principle.**
   - Templates with explicit member slots plus a pure instantiation function `(template, sorted_members) → envelope`.
   - Synthetic-key instantiations frozen as vectors.
   - **Add:** at scoring time, the scorer re-instantiates the template from the *public setup-receipt members* and requires byte equality with the signed statement's envelope. This is the check that stops a rotation statement from naming members other than the ones the owner registered.
   - **Negative tests:**
     - swap PRIMARY and RECOVERY in the effect text;
     - substitute a non-member public ID;
     - reorder members;
     - instantiate the arm-A template for arm B.
2. **Missing dependency (REV04 gap; fixture clarification).** REV04 makes the B→A **recovery** dependency explicit (P6 uses the Attempt 002 Arm-A RECOVERY key, else `FAIL / UNEXECUTED_RECOVERY_MEMBER_ABSENT`). It inherits the V02 C05 rotation rule, under which B's ordinary rotation target **V2 is PRIMARY = Arm-A primary, RECOVERY = Arm-A recovery** (V02 addendum §9, P01-C07).
   - B's P5 envelope therefore also cannot be constructed if Arm A setup did not produce its keys. REV04 and Q0 are silent on this.
   - **Correction:** add a fixture rule mirroring P6: `FAIL / UNEXECUTED_ROTATION_TARGET_ABSENT`. B's P5 envelope is built only from same-attempt A public members and never substituted.
   - Record it as a fixture-level clarification consistent with the approved P6 rule. It does not change any B01/B02 classification semantics, so I do not think it needs a new owner decision. ChatGPT should confirm that reading.
3. **Cross-arm replay.** Acceptance IDs are arm-qualified (`R0-P01-002-<ARM>-<ITEM>`). Add a test that an A-arm P5 statement presented in B's ledger fails structurally even when signed by a member that is valid in both. Under V02 member sets, the Arm-A keys are members of both arms' signer histories.

### Q-4. Split the freeze into F1 (fixture and oracle) and F2 (implementation and evidence map) (blocking)

Q1 §4–§5 places "exact fixture freeze" before implementation, which is correct. It also lists, inside the fixture freeze, items that only exist after implementation: "every source raise/subprocess/Node/browser error is exactly mapped" (R15), tool versions, and Windows lifecycle behaviour.

**Correction.** Define two prospectively reviewed freezes.

- **F1, pre-implementation fixture and oracle freeze:**
  - spec data: context, project, prefix grammar; nine-field canonical rules; renderer profile; T3 byte table;
  - templates and golden vectors from Q-2a;
  - the decision table from Q-2c;
  - the 13 control mutations and expected outcomes;
  - flag schema with origins;
  - terminal-outcome enumeration;
  - the error-*category* vocabulary;
  - B02 policy binding;
  - the clause index and test catalogue from Q-1.
- **F2, post-qualification implementation freeze (before Q6):**
  - implementation and scorer source hashes;
  - the **exhaustive error-site map** (R15) generated from the frozen source, for example by AST enumeration of `raise` statements, subprocess exits and Node `throw`/`reject` sites, each mapped to an F1 category, with zero unmapped sites;
  - pinned tool versions (Python, Node, OpenSSH, Chromium/Playwright);
  - Windows and browser qualification receipts;
  - the full synthetic A/B/C run outputs;
  - the F1 hash.

The Attempt 002 start claim binds the **F2 manifest hash**, which transitively binds F1, the approvals and the policy. Any change after F2 requires a new F2 and a new review before Q6.

### Q-5. Evidence architecture: two writers, two streams

REV04 requires durable RP ceremony receipts written by the Node process, and atomic snapshots written by the harness. Two processes writing into one numbered `raw-NNNN` sequence would introduce shared mutable state and race conditions.

**Correction:**

- The RP writes its **own** append-only, hash-chained receipt stream (for example `rp-NNNN.json`) with the same atomic temp-file-and-rename discipline.
- Each harness snapshot records the RP stream's head hash and count at that moment.
- The scorer cross-validates the two chains.
- The owner's final-head witness covers both heads.

This keeps one writer per stream and makes the post-Ctrl+C rule ("use last durable RP receipts") mechanically checkable. Neither stream is authority: both are evidence, and the scorer's ledger replay is derived. No database, daemon or third process is needed. I see no other unnecessary service in candidate B.

### Q-6. Windows qualification: separate what CI can prove from what needs the target machine

1. **Atomic no-overwrite promotion.**
   - Use `MoveFileExW` *without* `MOVEFILE_REPLACE_EXISTING`, with `MOVEFILE_WRITE_THROUGH`, via ctypes. Python's `os.rename` gives no-overwrite on Windows but not write-through.
   - Directory fsync is not available on Windows, so specify write-through as the "parent-directory durability strategy" REV04 asks for.
   - Test: target exists → refusal; temp file orphaned after a forced kill → never treated as final.
2. **SSH R/S and passphrase flows.** These cannot be automated through an inherited console without a pseudo-console.
   - Drive the harness under **ConPTY** (for example `pywinpty`) in tests, with synthetic passphrase-protected keys. The test driver owns the PTY; the harness code still inherits it and captures nothing.
   - This automates first-try success, wrong→correct, three wrong, S, Ctrl+C at the prompt (sending `\x03` through the PTY) and the precondition mutations between invocations.
   - Native-prompt *visibility* on the owner's real console remains a manual receipt.
3. **Node process group.**
   - Test `CREATE_NEW_PROCESS_GROUP` plus `GenerateConsoleCtrlEvent` to the harness's group.
   - Assert that the RP survives long enough for the harness's bounded final read, *and* that receipts written before the interrupt are complete when the RP is killed outright.
4. **Two Windows tiers.** GitHub Actions `windows-latest` (or an equivalent CI Windows runner) can run tiers 1–3, but its OpenSSH and Node versions will not match the owner's frozen versions.
   - Make CI necessary but not sufficient.
   - Add a **target-machine synthetic run**: the owner's actual Windows build with synthetic keys only, no owner credentials, no claim marker, separate directories. Record it as F2 evidence.
   - It is not owner-sensitive, but it is the only place where version-specific prompt and process behaviour is observed.
5. **Guard portability (non-blocking).**
   - The guard hashes working-tree bytes, while the recorded hashes are Git-blob (LF) bytes.
   - The repository has no `.gitattributes`. A checkout with `core.autocrlf=true` (common on Windows) would fail the guard with a misleading "historical baseline byte mismatch", which is the CRLF/blob defect this project has hit twice before.
   - Either hash `git cat-file blob` output, or add `.gitattributes` `-text` entries for every hashed path. Label the byte basis in the trace.

### Q-7. WebAuthn virtual-authenticator realism

- Use Playwright with Chromium CDP `WebAuthn.addVirtualAuthenticator` (`protocol: ctap2`, `transport: internal`, `hasResidentKey: true`, `hasUserVerification: true`, `isUserVerified: true`).
- **Negative cases to add:**
  - `isUserVerified: false` → UV flag absent → rejection;
  - a credential from a second virtual authenticator → not the registered ID → rejection;
  - `automaticPresenceSimulation: false` with no presence → `NotAllowedError` at timeout.
- The last case needs the frozen 120-second timeout. Either run it at full length (acceptable once per qualification), or make the timeout a test-only parameter and add a separate assertion that the frozen production value is 120 s and is the one bound into F2.
- Cancellation receipts must show the pending assertion consumed with the right acceptance ID, per R07/T1.
- I agree with the Q1 statement that none of this qualifies Windows Hello UX.

### Q-8. Arm C synthetic provenance

Marking synthetic role receipts as test doubles is correct. Add a scorer test that a C record without the task-owner receipt field, or with a mismatched line, is a C mismatch and never affects A/B classification. Keep C's evidence schema physically separate from A/B proof records, so that no code path can treat a C attestation as a proof object.

### Q-9. Smaller corrections

1. **Determinism.** The scorer's derived output must be canonical JSON. Specify float formatting, for example `repr` of the unrounded monotonic seconds. Test byte-identical output across two runs and across Windows and Linux, since pending-state re-runs may happen on a different host.
2. **Dependency pinning.** Any non-stdlib dependency (Playwright, a crypto library, pywinpty) must be installed with hash pinning (`--require-hashes` / lockfile integrity). Owner-run tooling must need no network at run time.
3. **Secret scanning.** Run the REV04 last-chance scanner as an F2 test over all synthetic-run outputs *and* over the ConPTY transcripts, to prove no passphrase reaches harness-captured streams.
4. **Validation 220 tempfile episode.** It is honestly reported. Add a guard-level known-answer check (hash of a fixed byte string) to the guard's own self-test, so an environment problem cannot masquerade as a source mismatch. This is the same lesson as F10 for the scorer.

## 3. Recommended decomposition

Adopt candidate B, trimmed to five units plus one test-only oracle, with enforced dependency directions:

```text
p01_spec      DATA ONLY: fixture, T3 table, templates, golden vectors, decision table,
              flag schema, clause index, test catalogue            (F1)
p01_core      pure Python: canonical, render, statement, ledger/admission, controls
p01_owner     owner-run coordinator + SSH adapter + snapshot writer (imports core, spec)
p01_rp        Node RP: registration/assertion, own receipt stream    (reads spec only)
p01_score     independent scorer: own canonical/render/verify/classify (reads spec + evidence;
              MUST NOT import core/owner/rp)
p01_oracle    second implementation of the pure layer, used only to generate and cross-check
              F1 vectors; never shipped to the owner run
```

There are no services and no shared mutable store beyond the two append-only evidence streams. CI enforces the import-graph constraints. Candidate A (a single coordinator) would make Q-2(b) and the error-site audit materially harder, and I would not adopt it.

## 4. Tests required before F1 and F2 (additions to the Q0 catalogue)

| ID | Layer | Purpose |
|---|---|---|
| T-CLAUSE-COVERAGE | static | Every REV04/policy clause mapped; no orphan rows; bound to approved hashes |
| T-CONTROL-KEY-BINDING | static | C01..C13 ↔ fixture control keys, positionally |
| T-CATALOGUE-BIDIRECTIONAL | static | Every test ID catalogued with layer, oracle and forbidden-shared-code fields, and every catalogued ID used |
| T-VECTOR-NVERSION | oracle | Two implementations agree byte-for-byte on all F1 vectors |
| T-DECISION-TABLE-EXHAUSTIVE | oracle | Scorer matches the frozen decision table over the full predicate lattice |
| T-SCORER-IMPORT-ISOLATION | static | No scorer→core/owner/rp import edge |
| T-SSHSIG-INPROCESS-VERIFY | scorer | In-process SSHSIG verification agrees with `ssh-keygen -Y verify` on synthetic vectors, including negatives |
| T-TEMPLATE-REINSTANTIATE | scorer | Signed P5/P6 envelope equals re-instantiation from public setup members; swap and substitute negatives |
| T-B-P5-TARGET-DEPENDENCY | integrated | Missing A members gives B P5 `FAIL / UNEXECUTED_ROTATION_TARGET_ABSENT` |
| T-CROSS-ARM-REPLAY | pure | An A-arm statement in B's ledger rejects structurally |
| T-ERROR-SITE-AST | F2 static | Generated raise/exit/throw site inventory has zero unmapped sites |
| T-RP-STREAM-CROSSCHAIN | integrated | Harness snapshots bind the RP head; a deleted or edited RP receipt is detected |
| T-WIN-MOVEFILE-WRITETHROUGH | Windows CI | No-overwrite and write-through promotion; orphan temp files never final |
| T-WIN-CONPTY-SSH | Windows CI | R/S, wrong→correct, three wrong, Ctrl+C, precondition mutations under ConPTY |
| T-WIN-NODE-GROUP | Windows CI | RP survives the harness Ctrl+C; outright kill preserves earlier receipts |
| T-TARGET-MACHINE-SYNTHETIC | owner machine, synthetic | Version-specific prompt and process behaviour; no owner keys, no marker |
| T-WEB-UV-FALSE, T-WEB-FOREIGN-CRED, T-WEB-PRESENCE-TIMEOUT | browser virtual | UV, credential-ID and timeout negatives |
| T-SCORER-DETERMINISM-XOS | scorer | Byte-identical derived output across runs and operating systems |
| T-GUARD-BLOB-BASIS | static | Guard result independent of the checkout line-ending configuration |

## 5. Unchanged boundaries

- B01/B02 accepted and not reopened.
- Attempt 001 immutable AMEND.
- All 13 controls with zero misses, 1/2/4/30 effects, 60/120/120-second gates, volume gates, A/B selection with the B tie-break, C ineligible, no pooling, secret boundary.
- The third human approval (Q6) is required before any owner key, marker or ceremony. Attempt 002 is not authorized.
- GOVERNED_LEDGER_KERNEL_V02 unselected; R0-P02 PASS; R0-P03 pending; Specification 028 unchanged. No architecture question is raised.

```text
MC0030_MESSAGE029=CLAUDE_Q0_Q1_REVIEW
DISPOSITION=AMEND_Q0_Q1_BEFORE_FREEZE
BLOCKING=Q1_CLAUSE_COMPLETENESS_INDEX;Q2_ENFORCED_ORACLE_SCORER_INDEPENDENCE;Q4_SPLIT_F1_F2_FREEZES
ALSO=Q3_TEMPLATE_REINSTANTIATION_AND_B_P5_TARGET_DEPENDENCY;Q5_TWO_EVIDENCE_STREAMS;Q6_WINDOWS_CI_VS_TARGET_MACHINE;Q7_WEBAUTHN_NEGATIVES
HASHES_RECOMPUTED=MATCH_GIT_BLOB_LF
B01_B02=NOT_REOPENED
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CHATGPT_RECONCILIATION
```
