# R0-P01 V01 Implementation and Trial Contract

**Status:** PROSPECTIVELY FROZEN BEFORE HARNESS IMPLEMENTATION OR OWNER TRIALS
**Protocol:** R0-P01-V01
**Candidate:** GOVERNED_LEDGER_KERNEL_V02 owner-authenticity / acceptance path
**Purpose:** Freeze the exact probe implementation choices, sign-what-you-see behavior, credential handling, trial timing, result interface and implementation blindness before any owner signing result is observed.

## 1. Non-production boundary

This probe does not select production canonicalization, renderer text, SSH as a permanent production credential, WebAuthn as a permanent production credential, ChatGPT as an authority surface, exact key-storage topology, or final trust-root UX.

The probe asks whether the architecture can realize a practical owner-exclusive proof over the exact SignedAcceptanceStatement.

The following identifiers are probe-only:

    PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY
    R0_P01_ASCII_OWNER_VIEW_V01
    ADS-R0-P01-SYNTHETIC

No private key, key passphrase, authenticator secret, recovery secret or account credential may be printed, committed, transmitted to a model, placed in Runtime Bridge logs, or included in a result artifact.

## 2. Frozen SignedAcceptanceStatement

Every cryptographic arm signs the same logical fields:

    context
    project_id
    acceptance_id
    envelope_digest
    shown_digest
    decision
    semantic_base_digest
    signer_set_version
    issued_at

Canonical probe bytes are compact, sorted-key, UTF-8 JSON with no NaN/Infinity.

The statement bytes themselves are what Arm A signs.

Arm B sets the WebAuthn challenge to:

    SHA256(canonical_statement_bytes)

and verification independently recomputes that digest before accepting the assertion.

Arm C attests the lowercase hexadecimal SHA-256 of the same canonical statement bytes.

## 3. Sign-what-you-see client rule

The harness, not chat/model prose, owns the signed display.

For every owner trial it must:

1. load the exact envelope from fixture.json;
2. recompute and validate the fixture semantic-base digest;
3. construct the exact owner-view string using R0_P01_ASCII_OWNER_VIEW_V01;
4. display that exact string from the same in-memory byte sequence whose SHA-256 becomes shown_digest;
5. start semantic-review timing only after the complete view is displayed;
6. collect ACCEPT / AMEND / REJECT from the owner;
7. stop semantic-review timing at the owner's decision;
8. construct and display the final canonical SignedAcceptanceStatement preview;
9. start mechanical timing immediately after the decision is captured and before credential invocation;
10. invoke the selected owner credential without receiving any credential secret from the caller/model;
11. verify the proof locally;
12. stop mechanical timing only after local verification has a deterministic result;
13. collect the non-secret friction rating/note.

The rendered owner view must contain, in this exact order:

    R0-P01 OWNER VIEW V01
    Project: <project_id>
    Trial: <trial_id>
    Acceptance: <acceptance_id>
    Title: <title>
    Summary: <summary>
    Semantic base: <semantic_base_digest>
    Effects: <count>
    <for each effect in fixture order>
      [<1-based index>] <grammar> <effect_id>
      Subject: <subject>
      Text: <text>
    END R0-P01 OWNER VIEW V01

Line ending for digested shown bytes is LF. The final byte is LF.

The harness may adapt terminal/browser presentation around that string, but shown_digest must be computed from exactly those UTF-8 bytes.

## 4. Acceptance identifiers

Acceptance IDs are deterministic and arm-specific:

    R0-P01-<ARM>-<TRIAL>

where ARM is A, B or C and TRIAL is S01, S02, S03 or L01.

Security-control acceptance IDs use:

    R0-P01-<ARM>-SEC-<CONTROL>

with CONTROL equal to the exact security-control key.

These IDs are synthetic and never become production authority.

## 5. Arm A: OPENSSH_ED25519_PASSPHRASE_V01

### 5.1 Exact mechanism

Use Windows OpenSSH SSHSIG:

    key type          Ed25519
    signature format  ssh-keygen -Y
    namespace         ads-r0-p01-acceptance

Current environment reconnaissance before freeze observed:

    OpenSSH_for_Windows_9.5p2
    ssh-keygen -Y sign / verify available

### 5.2 Key material

Use a dedicated probe-only local directory outside the repository:

    %LOCALAPPDATA%\ADS-R0-P01\arm-a\

Required owner credentials:

    owner_primary_ed25519
    owner_recovery_ed25519

Each key is generated interactively by the owner with:

    ssh-keygen -t ed25519 -a 100 -f <path> -C <probe-label>

The owner chooses a non-empty passphrase at the native prompt.

Forbidden:

    -N <passphrase>
    command-line passphrase arguments
    storing the passphrase in an environment variable
    ssh-agent caching of either probe key
    copying a private key into the repository
    exposing a private-key path in a public result

The harness records only public key material/fingerprint and proof artifacts needed for independent verification.

### 5.3 Signing

The harness writes canonical statement bytes to the local probe directory and invokes:

    ssh-keygen -Y sign -f <primary-key-path> -n ads-r0-p01-acceptance <statement-file>

with console/TTY inherited so the owner, not the harness, enters the passphrase.

Verification uses ssh-keygen -Y verify against an allowed-signers file constructed from the corresponding public key.

The harness never supplies the passphrase.

### 5.4 Recovery

The separately passphrase-protected recovery key is preregistered by public fingerprint before security-control execution.

It is not loaded into ssh-agent.

Its dry-run use is a separate security control and is not counted as one of the 3+1 burden trials.

## 6. Arm B: LOCALHOST_WEBAUTHN_ES256_UV_V01

### 6.1 Exact mechanism

Use a local WebAuthn relying party implemented only with the installed Node runtime and browser platform APIs.

Current pre-freeze environment reconnaissance observed:

    Node v24.19.0
    connected Chrome Browser runtime available

The exact RP is:

    URL       http://localhost:8765
    rpId      localhost
    origin    http://localhost:8765
    alg       ES256 / COSE -7 only
    UV        required
    attestation none
    residentKey preferred
    authenticatorAttachment omitted

Omitting authenticatorAttachment permits the owner's actual Chrome/WebAuthn environment to offer a platform authenticator or a cross-device/mobile-capable authenticator.

A real credential operation is not performed before this freeze.

### 6.2 Exact statement binding

For every assertion:

    challenge = SHA256(canonical SignedAcceptanceStatement bytes)

The verifier must independently check:

    clientDataJSON.type == webauthn.get
    clientDataJSON.challenge == exact base64url statement digest
    clientDataJSON.origin == http://localhost:8765
    authenticatorData.rpIdHash == SHA256("localhost")
    UP flag is set
    UV flag is set
    credential ID equals the registered probe credential
    ES256 signature verifies over:
        authenticatorData || SHA256(clientDataJSON)

The registration path uses attestation=none and accepts only ES256.

To avoid project-specific cryptographic/CBOR machinery, the browser client must use the platform WebAuthn response methods:

    AuthenticatorAttestationResponse.getPublicKey()
    AuthenticatorAttestationResponse.getPublicKeyAlgorithm()
    AuthenticatorAttestationResponse.getAuthenticatorData()

The public key is transported to the local verifier as SPKI DER and imported with Node's built-in crypto APIs.

The registration verifier independently checks the registration clientDataJSON challenge/origin/type and the returned authenticatorData rpIdHash plus UP/UV flags before storing the probe credential ID/public key.

If the current browser cannot expose these standard response methods for the exact registration result, Arm B is NOT_REALIZABLE for this probe rather than adding a hidden library or hand-written COSE/CBOR parser.

No accepted algorithm may be silently broadened beyond ES256.

### 6.3 Realizability

Before an owner trial, the browser client checks WebAuthn API availability and attempts one explicit owner-authorized probe registration.

If the environment cannot create an ES256 credential with user verification or cannot return an assertion bound to the exact challenge, Arm B is:

    NOT_REALIZABLE

The harness must not replace this with ordinary passkey login, OAuth login, browser account approval or another non-equivalent identity signal.

### 6.4 Recovery

Arm B uses the separately preregistered Arm-A recovery Ed25519 public key as the offline recovery credential for the recovery dry-run.

This is an intentional heterogeneous signer-set test.

The B primary credential must sign the ordinary trust-root rotation statement. The recovery credential signs the synthetic recovery rotation statement.

No WebAuthn private credential material is exported.

## 7. Arm C: CHATGPT_OWNER_USER_ROLE_DIGEST_ATTESTATION_V01

Arm C is a weaker comparator only.

It tests the friction of the owner's existing platform-separated user role compared with agent execution identity.

For one small and one large comparator event, the harness/task owner presents:

    R0-P01 PLATFORM ATTEST <acceptance_id> <statement_sha256>

The owner must send that exact line as a user-authored ChatGPT message.

The result records:

    exact expected line
    exact observed owner line
    match / mismatch
    owner-visible platform separation
    measured interaction count where available
    subjective friction note

Arm C is not cryptographic proof of the SignedAcceptanceStatement, depends on platform/chat provenance and is not independently verifiable from repository evidence alone.

Therefore:

    selection_eligible = false

under all outcomes.

It can never by itself produce PASS_WITH_SELECTION.

## 8. Security controls

The 13 exact controls and their required semantics are frozen in security_control_contract.md.

All 13 must PASS for an owner-exclusive cryptographic arm to be eligible.

No result label is hidden from the implementer.

## 9. Owner burden trials

For each REALIZABLE owner-exclusive cryptographic arm A/B:

    S01  1 effect
    S02  2 effects
    S03  4 effects
    L01 30 effects

All fixture effects are synthetic and low consequence.

The owner must not reveal any secret while performing a trial.

Measurements:

    semantic_review_seconds
        complete owner view displayed
        -> owner decision captured

    mechanical_seconds
        owner decision captured
        -> credential proof locally verified

    interaction_count
        user-visible decision/authentication interactions after display

    device_switches
        number of physical-device changes needed to complete the proof

    manual_metadata_edits
        owner hand-edits to JSON/TOML/Git/signature metadata; must be zero

    friction_rating_1_to_5
        1 very low friction
        5 very high friction

    friction_note
        short non-secret owner note

Infrastructure interruptions are recorded separately. A small-trial >120 seconds caused only by a recorded infrastructure interruption is excluded from that single-trial upper-bound gate but remains visible in evidence.

No other timing exclusion is permitted.

## 10. Mechanical gates

A/B eligibility requires:

    3/3 small trials successful
    median small mechanical_seconds <= 60
    max small mechanical_seconds <= 120 absent recorded infrastructure interruption
    L01 mechanical_seconds <= 120
    manual_metadata_edits == 0
    secret_exposure == false
    all 13 security controls PASS

Semantic-review time is reported but is not subjected to the mechanical thresholds.

## 11. Selection between A and B

If exactly one cryptographic arm is eligible, select it.

If both are eligible:

1. if their median-small mechanical times differ by at least 10 seconds, select the lower median;
2. otherwise, if their L01 mechanical times differ by at least 15 seconds, select the lower L01 time;
3. otherwise select Arm B because it achieves exact statement binding with user verification while the relying party never receives/exportably stores the authenticator private key and it preserves a mobile/cross-device-capable path.

The thresholds and tie-break are frozen before results.

## 12. Legacy-volume estimate

legacy_volume_inventory_rule.json is the only P01 desk-estimate source.

Its source artifact is hash-bound.

Baseline:

    projected acceptances  97
    projected effects      157
    effect-count distribution
        1 -> 62
        2 -> 17
        3 -> 11
        4 -> 7

Projected mechanical burden:

    97 * selected median small mechanical seconds / 60

If the source digest no longer matches, the inventory must be refrozen before classification.

If projected acceptance count >100 or projected mechanical burden >90 minutes:

    P01 cannot classify PASS_WITH_SELECTION
    bounded batch/class acceptance design is required
    disposition is AMEND

unless a stronger preregistered reason requires REOPEN/INVALID.

Cryptographic proof viability is intentionally weaker than full selection eligibility.

An arm is proof-viable when:

    REALIZABLE
    controls 1-10 in security_control_contract.md all PASS
    at least one owner-authenticated small proof succeeds
    secret_exposure == false

Classification then follows result_contract.json:

    no proof-viable A/B arm
        -> REOPEN

    at least one proof-viable arm, but none fully selection-eligible
        -> AMEND

    fully eligible selected arm, but volume gate triggers
        -> AMEND

    fully eligible selected arm and volume gate stays within bounds
        -> PASS_WITH_SELECTION

This preserves Research 513's distinction between an unusable exact-proof architecture and a viable proof path that still needs bounded UX/trust-root/batching work.

## 13. Result integrity

The implementation must produce a machine-readable result conforming to result_contract.json.

No credential secret is ever part of that result.

Proof artifacts/public keys necessary for independent cryptographic verification may be preserved.

Raw owner-trial results are frozen before architectural interpretation.

No post-result threshold, fixture, selection-rule or security-control change is permitted within the same attempt.

## 14. Implementation boundary

The bounded implementation phase may add only:

    experiments/r0_p01_owner_acceptance_v01/harness.py
    experiments/r0_p01_owner_acceptance_v01/webauthn_server.mjs
    experiments/r0_p01_owner_acceptance_v01/score.py

The WebAuthn HTML/JavaScript client must be embedded in webauthn_server.mjs so the bounded implementation remains three files.

No project dependency file may change.

Only Python standard library and Node built-ins may be used.

The implementation may read:

    Research 512
    Research 513
    the eventual P01 freeze research record
    fixture.json
    implementation_contract.md
    security_control_contract.md
    result_contract.json
    legacy_volume_inventory_rule.json

It must not read any later owner-trial result.

It must not execute a real owner credential operation.

Allowed pretrial checks:

    syntax
    deterministic fixture/render vectors
    security-control mutation logic using synthetic in-memory test doubles
    WebAuthn registration/assertion structural unit vectors not involving a real owner credential
    result-schema / classification tests
    local HTTP server syntax/startup without registration/assertion
    secret-redaction checks

Actual SSH signing, WebAuthn registration/assertion and ChatGPT owner attestation begin only after implementation review and freeze.

## 15. Attempt boundary

The first owner-visible credential invocation freezes P01 Trial Attempt 001.

After that point:

    no result-guided harness repair is allowed inside Attempt 001
    any harness defect requires result preservation, explicit classification and prospective refreeze

No retry-to-green.
