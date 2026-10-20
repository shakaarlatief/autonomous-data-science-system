# R0-P03 S1 fictional security-boundary trial candidate

**Candidate version:** 0.1 (2026-10-20)
**Status:** OWNER_DECISION_READY / NOT_EXECUTED / ALL_SECURITY_CHANGES_UNAUTHORIZED
**Purpose:** Obtain genuinely observable authentication, resource access, confidential-readback, independent journal-anchor, session continuity and revocation evidence before considering real source-status reviewer data.
**Basis:** Research 598/599, Validations 264–267 and the existing fictional-only tests in `experiments/r0_p03_navigation_probe/`.
**Inputs:** **Invented fictional test content only.** No old W5/Research 217 relevance, R0-P03 source records, private runtime credentials, project conversation memory or actual hidden gold.
**Current authority:** Read-only capability inspection and public-safe trial design. Nothing in this file creates users, modifies ACLs, registers workspaces, provisions secrets or authorizes a real reviewer.

## 1. Question to answer, without assuming the final architecture

Can a reviewer, challenger and separate authorizer use the *actual intended provider/tool route* to obtain a restricted fictional batch and append preserved evidence while a future blind author and exposed coordinator are **observably unable** to read, rewrite, infer or release it?

The test must discriminate at least three independent boundaries:

- Real, enforceable identity and role binding, not a string role or session title.
- Confidential resource access and durable/anti-rollback evidence, not a hash-chain that an unrestricted writer can replace.
- Distinct author-facing release surface and safe provenance, not the absence of obvious gold keywords in text.

A Windows ACL only tests the second boundary for identities running on the local machine. It does **not** independently bind ChatGPT Temporary Chats or remote model sessions to those Windows identities. A service may help supply cross-session authentication but adds secret, network and logging obligations. A hybrid may be necessary; no option is yet selected.

## 2. Trial-option comparison and entry gate

| Trial option | Smallest candidate exercise | Not proven by itself | Status |
| --- | --- | --- | --- |
| Owner-local Windows principals and fictional ACL-protected resource | Owner-approved disposable test location; two independently verified security tokens; positive allowed read/write and negative denied access; restart/revocation and cleanup | Remote-model identity, provider memory isolation, logs or true cryptographic journal anchor | Candidate, no principal/resource approved |
| Authenticated purpose-built reviewer service | Test-only identities/credentials; scoped fake API; refusal for wrong audience/role; durable readback, secret-safe logs and revocation | Native OS isolation, provider retention, model-access parity, signed journal custody unless separately tested | Candidate, no service/provider/key approved |
| Split/hybrid | Exact fake source transport to test reviewer; independently authenticated review log and separate digest anchor; separate packet gateway | End-to-end actor identity and cross-system consistency until tested | Candidate, not automatically mandatory |
| Alternative independently discovered route | Demonstrably equivalent test of all relevant controls | Same proof gates and threat review apply | Explicitly open |

**No permission to execute a state-changing trial is implied by a candidate ranking.** If the owner chooses a route, first qualify actual access from the reviewer’s eventual app or tool. Do not assume the current public Runtime Bridge command profile should be used for the future private reviewer.

## 3. Minimum authorization decisions before the first state-changing test

Obtain affirmative owner review of a concrete proposal containing:

1. Selected *fictional-only* architecture option, threat model and why this route is relevant to the actual non-arm reviewer/challenger.
2. Exact existing accounts/services and whether distinct temporary principals must be created; authority to create/remove them, and proof no unintended privilege elevation or shared actor impersonation.
3. Explicit disposable storage root **outside public Git and outside real private evidence**; project trust/registered-root changes must be separately requested, not inferred from the storage selection.
4. Credential/key handling, read/write/delete scope, allowed provider or local tooling, logging/telemetry and how secret text is prevented from appearing in a public receipt or conversation.
5. Named independent journal-head owner/anchor, expected readback/restore and defense against primary-log rollback, with actual compromised-writer assumptions stated.
6. Bounded duration, reset/cleanup plan, expected artifacts/hashes, and who reviews permission changes, process effects and complete removal.
7. Explicit confirmation that **only fabricated fictional bytes** are supplied and that no real reviewer admission, author release or source-status scoring may be inferred.

If any decision is absent, remain at `S1_SECURITY_TRIAL_UNAUTHORIZED`. No default Windows account name, guessed filesystem path, cloud service or permission change should be introduced to bypass the hold.

## 4. Owner-authorized execution sequence, still prospective

**Stage A: Baseline and positive control.** Record immutable fake manifest and trial receipt ID, actual principal+session and relevant authentication claims without exposing secrets in public logs. Establish owner-approved test resource under expected allow/deny ACL or service policy. Test an authorized reviewer access through the **actual proposed reviewer route**; record source hash and permitted operation. A direct owner test is not a reviewer-route test unless that is the proposed route.

**Stage B: Genuine negative control.** Under an actually distinct blind-author or public-coordinator principal, attempt only a harmless read of a fictional marker and, separately, a bounded attempted write. Record whether denial occurred in the OS, service, registered-workspace guard, or missing path. Do not report `ACL_DENIED` for a bridge-root refusal. Also test denied challenger write to reviewer-only action and denied self-authorization.

**Stage C: Identity continuity and aliases.** Create a new session for the same reviewer and verify real exposure binding and revocation. Attempt a known alternate identifier/credential only when the owner authorizes that fake identity; if the system cannot attribute it, explicitly hold the blind-author isolation gate. Never infer a shared natural-person relationship from matching text names alone.

**Stage D: Confidential evidence, restart and audit.** Write fictional reviewer events, preserve exact bytes and hashes, close/reopen the authorized client, restart only explicitly approved test processes, and verify audit event order. Test a torn tail and an internally valid short prefix. Anchor the expected head/sequence in **separately authorized custody**, not just another file under the same writer’s control. The test must not overwrite actual reviewer output.

**Stage E: Revocation and hostile access.** Revoke one test principal or service grant via the approved route; verify previously valid sessions/credentials can no longer read or mutate fictional evidence. Confirm audit/log/backup boundaries and time-of-check/time-of-use behavior. An access failure from a crashed client, deleted file or missing provider is NOT an authorization PASS.

**Stage F: Author-view leakage challenge.** Attempt to disclose a fake protected cue through filename, citation, search snippet, download name, loaded linked asset and two benign-looking aggregate receipts that become revealing when joined. Deny or hold the assembled exposure without concluding that all useful historical observations must be excluded. Record actual renderer/tool observations, not simulated booleans.

**Stage G: Reconciliation and cleanup.** Independently verify exact journal and anchor readback, expected event count, role audit, denial/success evidence and residual files. Remove only owner-approved disposable resources through a separately allowed cleanup plan; restore original permission configuration with readback. Report failed cleanup as a real blocker, not success. Preserve **only non-secret qualification receipts** in public ADS.

## 5. Explicit evidence classification contract

Every claim of qualification must include:

```text
test_case_id
synthetic_data_fingerprint
chosen_actual_actor_binding_or_UNKNOWN
trusted_executor_and_tool
resource_and_access_method
expected_allowed_or_denied_operation
actual_return_and_observed_content_exposure
denial_layer=OS|SERVICE|BRIDGE_REGISTRY|MISSING_PATH|OTHER|NONE|UNKNOWN
readback_or_recovery_witness
protected_logs_and_backup_assessment
owner_authorization_reference
remaining_unknowns
qualification=OBSERVED|FAILED|NOT_TESTED|NOT_OBSERVABLE|HOLD
```

Never log credential values, unredacted protected paths, real source-to-gold mappings or private-reviewer notes in a public receipt. A test “PASS” is admissible only for the exact control/layer actually witnessed. In particular:

- `ENOENT` is not security enforcement.
- A Codexless workspace refusal is not OS or service access denial.
- A Python mock principal name or caller-supplied boolean is not authentication.
- A digest with no separately held trusted anchor does not prove complete journal history.
- One Windows token reading an ACL does not prove a second actor was denied.
- A safe source-file blob does not prove a safe rendering or author-world packet.
- A new chat does not prove independent prior exposure or complete retention/recovery.

## 6. Stop/advance conditions

**Advance from read-only reconnaissance to a real-principal fictional test** only after explicit approval of the identities, trust substrate, resource, permitted changes, credential/custody rules and cleanup plan. That approval must identify the actual actor/tool route.

**Advance toward real reviewer S1 content** only when all actual reviewer/challenger role, exact batch, representation, durable confidential output/anchor, recovery, author-view and challenge mechanisms have been independently evidenced and accepted, and V0.4 or a successor is method-qualified. A successful two-token ACL test is insufficient.

**No scored work:** this plan cannot choose B0–B4 arms, mutate Research 217 gold, write a fresh task source roster, freeze an author packet or alter Checkpoint 898/Specification 028.

```text
PROSPECTIVE_S1_TRIAL=DESIGNED_NOT_EXECUTED
OWNER_APPROVAL_FOR_SECURITY_MUTATION=NOT_REQUESTED_BY_THIS_FILE
ACTUAL_SEPARATE_REVIEWER_IDENTITY=NOT_PROVEN
OS_ACL_DENIAL=NOT_TESTED
SECURE_PRIVATE_REVIEWER_CUSTODY=NOT_SELECTED
EXTERNAL_JOURNAL_ANCHOR=NOT_SELECTED
MODEL_FACING_SOURCE_REVIEW=HOLD
AUTHOR_WORLD_AND_SCORING=HOLD
```
