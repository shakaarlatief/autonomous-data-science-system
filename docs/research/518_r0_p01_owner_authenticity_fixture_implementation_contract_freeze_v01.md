# Research 518: R0-P01 exact owner-authenticity fixture and implementation-contract freeze V0.1

**Date:** 2026-10-04
**Status:** R0-P01 EXACT FIXTURE / ARM CHOICES / SECURITY CONTROLS / BURDEN RULE / LEGACY-VOLUME RULE FROZEN / NO OWNER CREDENTIAL RESULT OBSERVED / HARNESS IMPLEMENTATION NEXT
**Parent:** Research 512-513, Research 517
**Candidate under test:** GOVERNED_LEDGER_KERNEL_V02
**Probe:** R0-P01
**Scope:** Freeze the exact owner-authenticity and acceptance-burden probe inputs, credential-arm choices, sign-what-you-see contract, public result vocabulary, security controls, burden thresholds, selection rule and legacy-volume desk estimate before any owner credential operation or trial result is observed.
**Authority:** Probe-fixture and implementation-contract preregistration only. No R0-P01 result, physical target selection, production credential selection, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction, or authority switch is authorized.

## 1. Prior boundary

Research 517 closed R0-P02 as:

    R0_P02=PASS
    GOVERNED_LEDGER_KERNEL_V02=RETAINED

R0-P01 is therefore the next preregistered probe in Research 513 order.

No owner signing/authentication trial has occurred for P01.

No P01 SSH key, recovery key or WebAuthn credential has been created by this work.

No ChatGPT owner attestation has been requested.

## 2. Frozen probe directory

The exact prospective probe surface is:

    experiments/r0_p01_owner_acceptance_v01/

Frozen inputs:

    fixture.json
        SHA-256 177dc3d7d071dd4ed2d34bc87f92e33d448e05a475af5c23c97014b928649f68
        bytes 14028

    legacy_volume_inventory_rule.json
        SHA-256 f58e9a836303019071e68a21e76e25eac90697aa419b9d6c3890925de5a5d72a
        bytes 1422

    result_contract.json
        SHA-256 1f054d12e18499b36c26de79f9c94d5073c1d7978c68e62fc1f2b2b2725bd506
        bytes 3244

    implementation_contract.md
        SHA-256 b3b90d851e25a4b906f6e094e6366ca42baca7fceb7c38c253f8220bc70b1202
        bytes 16037

    security_control_contract.md
        SHA-256 aad6e99387da888662c3a2d66bb573cb4b35db6f0d6a29371417700ce4222705
        bytes 4810

Static validation before freeze confirmed:

    protocol R0-P01-V01
    13 frozen security controls
    owner-trial effect counts 1 / 2 / 4 / 30
    legacy inventory source hash exact
    97 reviewed obligation units
    157 proposition/effect proxies
    distribution 62x1 / 17x2 / 11x3 / 7x4

No credential proof or owner result was used by that validation.

## 3. Probe-only representation

P01 uses the same probe canonicalization family already established for architecture testing:

    PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY

Owner-visible rendering is separately frozen as:

    R0_P01_ASCII_OWNER_VIEW_V01

These are probe mechanisms only.

They do not select production canonicalization or permanent user-interface text.

The logical SignedAcceptanceStatement remains the Research 512 field set:

    context
    project_id
    acceptance_id
    envelope_digest
    shown_digest
    decision
    semantic_base_digest
    signer_set_version
    issued_at

## 4. Exact sign-what-you-see rule

The qualified client must itself:

    load exact fixture envelope
    validate semantic base
    render exact owner view
    display exactly the bytes that become shown_digest
    measure semantic review separately
    collect owner decision
    construct canonical statement
    display final statement preview
    invoke owner credential
    verify proof locally
    measure mechanical authentication separately

Chat/model prose is advisory only.

No model rendering can substitute for the bytes bound by shown_digest.

The exact LF-terminated ASCII-safe rendering grammar and order are frozen in implementation_contract.md.

## 5. Arm A frozen: OPENSSH_ED25519_PASSPHRASE_V01

Arm A is the desktop owner-exclusive cryptographic path.

Exact mechanism:

    Windows OpenSSH SSHSIG
    Ed25519
    ssh-keygen -Y sign / verify
    namespace ads-r0-p01-acceptance

Pre-freeze environment reconnaissance observed:

    OpenSSH_for_Windows_9.5p2
    LibreSSL 3.8.2
    ssh-keygen -Y sign/verify available

Probe key material must live outside the repository:

    %LOCALAPPDATA%\ADS-R0-P01\arm-a\

Two keys are required:

    owner_primary_ed25519
    owner_recovery_ed25519

Both are owner-created interactively with non-empty passphrases.

The passphrases must never be supplied through command arguments, environment variables, repository files, model messages or Runtime Bridge inputs.

The keys must not be loaded into ssh-agent for the probe.

Owner passphrase entry occurs only at the native credential prompt.

Only public key/fingerprint and proof artifacts needed for independent verification may enter sanitized evidence.

## 6. Arm B frozen: LOCALHOST_WEBAUTHN_ES256_UV_V01

Arm B is the passkey/WebAuthn/mobile-capable owner-exclusive path.

Exact RP:

    http://localhost:8765
    rpId localhost
    ES256 / COSE -7 only
    userVerification required
    attestation none
    residentKey preferred
    authenticatorAttachment omitted

The assertion challenge is exactly:

    SHA256(canonical SignedAcceptanceStatement bytes)

The verifier independently checks:

    webauthn.get type
    exact challenge
    exact origin
    rpIdHash
    UP
    UV
    exact registered credential
    ES256 signature

Pre-freeze environment reconnaissance observed:

    Node v24.19.0
    connected Chrome Browser runtime available

No WebAuthn credential operation was executed.

Registration uses the browser platform methods:

    getPublicKey()
    getPublicKeyAlgorithm()
    getAuthenticatorData()

and Node built-in crypto.

If the actual current browser/authenticator cannot provide the exact ES256/UV binding, B is NOT_REALIZABLE.

The probe must not replace failure with ordinary passkey login or OAuth approval.

B uses the dedicated Arm-A recovery key as the synthetic offline recovery credential, demonstrating a heterogeneous signer set without exporting a WebAuthn private key.

## 7. Arm C frozen: CHATGPT_OWNER_USER_ROLE_DIGEST_ATTESTATION_V01

Arm C is intentionally a weaker platform-separated comparator.

For a small and large comparator event the owner sends an exact user-authored line:

    R0-P01 PLATFORM ATTEST <acceptance_id> <statement_sha256>

This tests the friction of the user's platform-authenticated role relative to agent execution.

It is explicitly not treated as cryptographic exact-statement proof and is not independently repository-verifiable without platform/chat provenance.

Therefore:

    ARM_C_SELECTION_ELIGIBLE=false

under every result.

C cannot by itself produce PASS_WITH_SELECTION.

## 8. Frozen owner-trial packet

For every REALIZABLE A/B arm:

    S01 1 synthetic effect
    S02 2 synthetic effects
    S03 4 synthetic effects
    L01 30 synthetic effects

All effects are synthetic and low consequence.

Measured separately:

    semantic review seconds
    mechanical authentication seconds
    interaction count
    device switches
    manual metadata edits
    failures/recovery events
    subjective friction rating 1-5
    short non-secret friction note

Mechanical timing starts only after the owner decision is captured.

It ends only after proof verification returns deterministically.

## 9. Frozen burden gates

An A/B arm is fully selection-eligible only if:

    13/13 security controls PASS
    3/3 small trials succeed
    median small mechanical overhead <= 60 seconds
    no small trial > 120 seconds absent recorded infrastructure interruption
    L01 mechanical overhead <= 120 seconds
    manual JSON/TOML/Git/signature metadata edits = 0
    secret exposure = false

Semantic reading/review time is reported but not thresholded.

## 10. Frozen security-control set

Exactly 13 controls are required:

    VALID_ACCEPTANCE
    FORGED_OR_AGENT_PREPARED_PROOF_REJECTS
    CHANGED_ENVELOPE_REJECTS
    CHANGED_SHOWN_VIEW_REJECTS
    DECISION_SUBSTITUTION_REJECTS
    CROSS_PROJECT_REPLAY_REJECTS
    ACCEPTANCE_ID_REPLAY_REJECTS
    SEMANTIC_BASE_MISMATCH_REJECTS
    UNRELATED_REPOSITORY_LANDING_DOES_NOT_INVALIDATE
    SIGNER_SET_MISMATCH_REJECTS
    TRUST_ROOT_ROTATION_DRY_RUN
    RECOVERY_CREDENTIAL_DRY_RUN
    COMPROMISE_BOUNDARY_DRY_RUN

Their exact semantics are public in security_control_contract.md.

There is no hidden oracle.

This specifically avoids the P02 Attempt-001 hidden-output-vocabulary failure class.

## 11. Proof viability versus full eligibility

Research 513 distinguishes:

    unusable exact owner proof
from
    viable proof needing bounded UX/trust-root amendment

The exact P01 contract therefore defines proof viability before full eligibility.

A/B is proof-viable when:

    REALIZABLE
    controls 1-10 PASS
    at least one owner-authenticated small proof succeeds
    no secret exposure

Full selection eligibility additionally requires:

    controls 11-13
    all 3+1 burden trials
    all mechanical thresholds

This preserves the decision semantics:

    no proof-viable A/B
        REOPEN

    proof-viable A/B exists but none fully eligible
        AMEND

rather than incorrectly treating a repairable trust-root/UX issue as a substrate falsification.

## 12. Frozen A-versus-B selection rule

If only one A/B arm is fully eligible:

    select it

If both are eligible:

    if median-small mechanical times differ by >= 10 seconds
        select lower median

    else if L01 mechanical times differ by >= 15 seconds
        select lower L01 time

    else
        select B

The final tie-break prefers B because it provides exact statement binding with required user verification while the RP does not receive an exportable authenticator private key and it preserves the mobile/cross-device-capable path.

This rule is frozen before any owner timing is observed.

## 13. Frozen legacy-volume estimate

The inventory source is exactly:

    docs/model_collaboration/threads/MC-0029/messages/006_claude_drp03_obligation_units_a.json

Source SHA-256:

    71fd3b691afb245e294e6012d29bc0780fe4d671fe7a4d09ef6a44845d3e0630

The desk-estimate boundary is:

    one reviewed obligation_unit = one projected migration/reconciliation governing acceptance
    no cross-unit batching assumed
    each proposition = one effect proxy

Result:

    projected acceptance count 97
    projected effect count     157

Effects per acceptance:

    1 -> 62
    2 -> 17
    3 -> 11
    4 -> 7

The projected mechanical burden after trials is:

    97 * selected_arm_median_small_seconds / 60

If:

    count > 100
or
    projected mechanical minutes > 90

then a governed batch/class acceptance variant is required and P01 cannot return PASS_WITH_SELECTION without amendment.

The source is hash-bound. Source drift requires prospective inventory refreeze.

## 14. Exact implementation boundary

The bounded implementation may add only:

    experiments/r0_p01_owner_acceptance_v01/harness.py
    experiments/r0_p01_owner_acceptance_v01/webauthn_server.mjs
    experiments/r0_p01_owner_acceptance_v01/score.py

No dependency file may change.

Implementation languages/libraries:

    Python standard library
    Node built-ins
    browser WebAuthn platform APIs

No real owner credential operation is allowed during implementation.

Allowed pretrial checks are limited to syntax, deterministic rendering/canonicalization, synthetic mutation/test-double controls, WebAuthn structural vectors without real credentials, result classification, local server startup without registration/assertion, and secret-redaction behavior.

The implementer must not read any later owner-trial result.

## 15. Owner-secret boundary

The probe must never collect, transmit or preserve:

    SSH passphrase
    private SSH key
    authenticator private key
    WebAuthn platform secret
    recovery passphrase
    account password
    one-time login secret

A public proof/public key is not a credential secret.

If any credential secret reaches a model, Runtime Bridge log, repository file or result artifact:

    P01=INVALID

for that attempt.

## 16. Attempt integrity

Harness implementation is frozen and independently reviewed before owner use.

The first real owner credential invocation starts:

    R0-P01 Trial Attempt 001

After that:

    no result-guided repair inside Attempt 001
    raw result is preserved before interpretation
    harness defect requires explicit INVALID/HARNESS_INVALID-style classification as appropriate and prospective refreeze
    no retry-to-green

## 17. Current boundary

    R0_P01_PROTOCOL=RESEARCH_513
    R0_P01_FIXTURE=FROZEN_V01
    R0_P01_HARNESS=NOT_IMPLEMENTED
    R0_P01_OWNER_TRIAL=NOT_STARTED
    R0_P01_RESULT=NOT_OBSERVED

    ARM_A=OPENSSH_ED25519_PASSPHRASE_V01
    ARM_B=LOCALHOST_WEBAUTHN_ES256_UV_V01
    ARM_C=CHATGPT_OWNER_USER_ROLE_DIGEST_ATTESTATION_V01

    LEGACY_PROJECTED_ACCEPTANCES=97
    LEGACY_PROJECTED_EFFECTS=157

    R0_P02=PASS
    R0_P03=PENDING

    PHYSICAL_ARCHITECTURE_SELECTED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED
    PRODUCTION_IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_AUTHORIZED=false

    NEXT=BOUNDED_MANUAL_CODEX_R0_P01_HARNESS_IMPLEMENTATION
