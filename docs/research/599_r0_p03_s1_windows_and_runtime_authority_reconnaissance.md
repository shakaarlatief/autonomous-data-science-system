# Research 599: R0-P03 S1 Windows and Runtime Bridge security-boundary reconnaissance

**Date:** 2026-10-20
**Status:** READ_ONLY_CAPABILITY_RECONCILIATION_COMPLETE / ACTUAL_WORKSPACE_ADMISSION_REFUSAL_OBSERVED / SEPARATE_REVIEWER_IDENTITY_AND_CUSTODY_UNQUALIFIED
**Scope:** Evaluate the current Windows and Codexless Runtime Bridge environment without changing accounts, ACLs, secrets, trusted workspaces, background processes or storage. Identify the smallest falsifiable next source-free access and custody exercise while leaving the final security architecture and workflow unconstrained.
**Basis:** Research 513/559/576/590–598, Validations 264–266, S1 prospectively authored V0.4 method, public branch `v1-source-vault-bootstrap-resume` at input commit `a9a44d6d2c922b0d389c1b16573eb7e3f20542f9`.
**Evidence:** Validation 267, containing only non-identifying, read-only operational observations. The separate `S1_FICTIONAL_SECURITY_BOUNDARY_TRIAL_CANDIDATE.md` is a not-yet-executed prospective test plan.
**Authority:** Infrastructure reconnaissance and method-design evidence only. No reviewer or challenger admitted; no credential, ACL, identity, protected store or production route changed. No real R0-P03 source, legacy gold, task author, B0–B4 score, Checkpoint 898 transition or Specification 028 modification.

## 1. Why the current trial cannot by itself qualify S1

Research 597/598 established the conceptual trust planes and validated a fictional transport, event journal and role decision system. Validation 266's negative control showed that a mock reviewer can obtain a new, unlinked identity and appear to be a blind author. This is an essential distinction: an internally consistent policy engine cannot authenticate who invokes it.

S1 needs observed **separation between acting principals and resources**, not simply labels such as `SIMULATED_REVIEWER` or `SIMULATED_AUTHORIZER`. The controls must survive actual model-facing access routes, possible cross-session/context exposure, account/session revocation, credential leakage, audit readback and failure/recovery. In particular, a workspace trust root limits where an ADS tool may execute; it does not prove private reviewer output confidentiality against a process with another existing admission or against the same Windows user.

The owner-accepted Level B relaxation in Research 576 applies to subsequent **arm authors**, not as a blanket exception to real source-reviewer independence or secret gold/custody separation. More elaborate security mechanisms may still be justified for *actual protected evidence custody*, but unnecessary infrastructure should not be imposed without a testable threat-based benefit.

## 2. Actual read-only evidence and correct attribution

The authorized read-only Codex command was executed through `mcp__Codexless_Runtime_Bridge__codex_command_exec` with the registered ADS public root as its working directory. The observations were intentionally reduced to non-identifying booleans and counts. No Windows username, user SID, group list, private directory path, credential value, registered workspace root path or ACL principal name was recorded in the public finding.

| Read-only observation | Actual result | What this does and does not demonstrate |
| --- | --- | --- |
| Git public HEAD and synchronization before changes | `a9a44d6d2c922b0d389c1b16573eb7e3f20542f9`; branch clean; tracking divergence 0/0 | Reliable engineering starting state; no private review qualification |
| Windows process token | Present; Windows principal reports non-administrator membership; authentication type reported `NTLM` | Current process identity exists; does not establish a *second independently controlled reviewer identity* or authorization to disclose protected data |
| Local-account enumeration | `Get-LocalUser` is available and returns seven local account entries | Enumeration capability and count only; no proof that a suitable reviewer/challenger principal exists or can be used for independent model access |
| Public ADS root ACL | Eight access rules; inherited rules present; inheritance is not protected; no deny ACE observed in this read | Describes the **existing public development root**, not a proposed restricted reviewer store and not a proven access-denial |
| Local platform commands | `icacls`, `cipher`, `New-LocalUser`, `Set-Acl` are discoverable | Existence of executables/cmdlets, not permission to change accounts/ACLs or proof that they enforce a chosen architecture |
| DPAPI managed type | Resolvable after explicitly loading `System.Security` | Type availability only; no encryption, decryption, key scope, encrypted at-rest ledger or restore tested. An earlier generic assembly-resolution probe returning false was **not** a valid DPAPI absence finding |
| Runtime workspace admission registry | Read-only registry inspection reports 11 registered workspace entries | Registry is a real tool access mechanism; not a proof that the same caller cannot reach multiple admitted workspaces or that role-specific private reviewer data is isolated |
| Nonexistent fictional external working directory | Command request fails with `ENOENT` on directory stat | A *missing path* check, not an ACL denial nor actual registry-enforcement test |
| Existing out-of-registry working directory `C:\Windows` | Command rejected with Codexless “no admitted root covering path” before expected harmless `echo` execution | **Observed workspace-registry admission refusal**, NOT a Windows filesystem ACL denial or attempted access to secret data |

One registered trust root may support public software development, while another separately admitted root may be accessible under other tool capabilities. An 11-workspace registry inventory does not define reviewer roles or authorize using any of those roots for protected source-status material.

**No actual OS access-denial trial was executed.** A genuine positive/negative Windows ACL result would require at least two independently identified Windows security tokens and a deliberately controlled *fictional* test resource with known ACLs. This exercise had neither. Existing public-root inherited ACEs cannot substitute for such a test.

## 3. Explicit layer taxonomy to prevent false assurance

For any future denial or success, record **which authority layer** rejected or permitted it, and whether content might have been read before failure:

1. **Missing input/environment:** `ENOENT`, broken command, crashed helper or missing provider. None demonstrates authorization enforcement.
2. **Runtime workspace admission:** registered root, trust, workspace capability and purpose-specific operation. A denial here is genuine enforcement by that tool, but does not establish independent OS access control or separation across other tools.
3. **Windows/OS process and file security:** actual authenticated access token, file DACL/privilege, access check at OS boundary, tested with distinct principals and negative plus positive controls.
4. **Service or application-level authorization:** externally issued, audience-scoped and revocable identity/role binding, enforced independently of untrusted caller strings.
5. **Protected evidence custody:** encrypted/appropriately access-controlled data, independent journal anchor, verified readback/recovery, log/backups/telemetry exclusions and deliberate release gateway.
6. **Scientific role and exposure qualification:** independent authors/reviewers, safe author-world source closure and hidden reference separation. OS/service permissions alone do not create unbiased reviewers or source validity.

Every observation also needs **scope, actual executor, read/write operation, expected behavior, observed behavior and uncertainty**. Recording “PASS” with no layer or observed action must be prohibited in future qualification receipts.

## 4. Candidate routes compared against observed infrastructure

The owner is not constrained by present folders, branches, Git strategy, Codexless processes or the original Windows deployment. The criteria below permit redesign at **any** level, including full changes to work procedures.

| Approach | Plausible next evidence | Remaining failure risk | Current recommendation |
| --- | --- | --- | --- |
| Single Windows user plus a Temporary Chat, with manual uploads | Exact fake batch bytes and human-attested session-scoped access could be measured | Same user can access files, unlinked identity aliases, external chat retention and missing restricted readback; no actual private boundary proven | Do **not** infer real confidential reviewer custody merely from the convenience of this route |
| Distinct owner-controlled Windows principals with a disposable fictional ACL-protected resource | Genuine different-token access-allow and OS-level access-deny tests plus revocation/readback | Local administrative authority, extra account lifecycle, backup/telemetry, cloud/model session identity and sensitive process environment remain unresolved | **Candidate for the smallest real OS-boundary trial**, contingent on owner-approved identities, temporary resource, cleanup and no actual protected content |
| Purpose-specific authenticated review service and restricted evidence journal | Server-side principal binding, narrow methods, simulated audit and readback, explicit denial under distinct credentials | Service trust, credential provisioning/rotation, network, provider retention, logs, revocation and backup surface | **Candidate for later side-by-side comparison**, not automatically more secure |
| Hybrid content-addressed transport, separate reviewer storage, independently held anchor and author packet gateway | Separately replaceable components and cross-boundary provenance; may reduce accidental shared context | Multiple authentication/recovery boundaries and more complex failure consistency | Strong logical decomposition, **not a mandated physical topology** |
| A new approach discovered during qualification | Possible better assurance at lower cost or operational burden | Same falsifiable boundary requirements apply | Explicitly permitted and should trigger architecture reconsideration |

**Assessment:** The read-only observations make a Windows two-principal fictional denial trial practically investigable, but **do not establish permission or feasibility to perform it** under the current process. A service or hybrid trial may be preferable if owner-mediated model access cannot actually be bound to Windows principals. The architecture should be chosen after actual route-to-model access and custody threat analysis, not by assuming local accounts solve cloud/session exposure.

## 5. Progress without selecting final custody

The next engineering phase can be split into two nonblocking workstreams:

- **S1A (owner-authorized security-boundary trial):** Test two *actual* independent principals or authenticated service identities against an explicitly disposable fictional resource, with positive/negative access tests, audit, revocation, session changes, restart, backup and cleanup. Obtain owner approval **before** accounts, ACLs, keys, services, workspaces or provider connections change.
- **S1B (source-free architecture engineering):** Specify a signed or independently committed journal head, explicit missing/truncated event handling, actual reviewer audit readback, separate release metadata screening and presentation-gateway isolation; validate mechanics with fake data while acknowledging that the final private store and access channel remain unselected.

V0.4's bounded independent method challenge may proceed separately, but a synthetic method PASS does not supply missing S1 security evidence. Real source-status review remains on HOLD even when source-free engineering checks pass.

## 6. Architecture-change triggers to monitor at every gate

Reevaluate the entire architecture and workflow when actual evidence shows: a reviewer can read an unapproved file through another admitted workspace; actor aliases cannot be bound across the chosen model/provider route; Windows ACL denies the desktop process but not a connected service; logs or transcript retention expose restricted source text; external anchor custody can roll back with the primary ledger; dynamic content or metadata evades author-packet controls; the security approach makes source-neutral reviewer access infeasible; or a genuinely better process/technology is available.

Do not solve a blocked gate by secretly widening Codexless trust, turning off ACL protection, placing a future private ledger in public Git, granting additional credentials, or relaxing Research 513/559/576/Specification 028. Owner authority, science controls and negative-test evidence remain prerequisites even if the storage and working procedure are fully redesigned.

## 7. Decision to carry forward

**Completed:** A real, read-only platform/tool boundary reconnaissance, including a demonstrable rejection at Codexless workspace admission and a correctly classified nonexistent-path error. **Not completed:** actual Windows ACL denial, separate reviewer identity, OS-level custody, independent journal anchor or author-view security.

The companion Validation 267 is the observed operational receipt; the trial candidate is an *owner-decision-ready design*, not approval to perform account/ACL mutations. The strongest next step is an explicit choice of a synthetic-only two-principal/identity test architecture and its bounded resource lifecycle, followed by approval and measured execution.

```text
RESEARCH_599=READ_ONLY_BOUNDARY_RECONCILIATION_COMPLETE
OBSERVED_CODEXLESS_WORKSPACE_ADMISSION_REFUSAL=YES
OBSERVED_WINDOWS_ACL_DENIAL=NO
WINDOWS_TOKEN_METADATA_READ=YES
SECOND_ACTUAL_INDEPENDENT_REVIEWER_TOKEN=NOT_TESTED
DPAPI_TYPE_AVAILABLE=YES_NO_ENCRYPTION_TEST
PRIVATE_REVIEWER_STORAGE=NOT_SELECTED
SOURCE_REVIEW_ACTOR_AND_CHALLENGER=NOT_QUALIFIED
REAL_SOURCE_DELIVERY=NOT_AUTHORIZED
SCORED_R0_P03=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
