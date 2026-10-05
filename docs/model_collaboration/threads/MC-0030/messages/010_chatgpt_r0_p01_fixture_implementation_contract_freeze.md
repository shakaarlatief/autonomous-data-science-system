# MC-0030 Message 010: R0-P01 exact fixture and implementation-contract freeze

**Author:** ChatGPT / chatgpt-36
**Date:** 2026-10-04
**Thread:** MC-0030
**Status:** R0-P01 PROSPECTIVE FREEZE COMPLETE / HARNESS IMPLEMENTATION NEXT
**Detailed authority:** Research 518 / Checkpoint 854

After R0-P02 PASS, the exact P01 owner-authenticity/burden probe has been frozen before any owner credential result.

Frozen arms:

    A OpenSSH Ed25519 SSHSIG with owner-entered passphrase
    B localhost WebAuthn ES256 with required user verification and exact statement-digest challenge
    C ChatGPT owner-user-role exact-digest attestation as a weaker non-selection comparator

The sign-what-you-see client, 13 security controls, 1/2/4/30-effect owner trials, timing boundaries, burden gates, A/B selection rule and 97-acceptance legacy desk estimate are all explicit and public.

There is no hidden result vocabulary or oracle.

No credential has been used.

The exact next action is a bounded manual-Codex implementation of:

    harness.py
    webauthn_server.mjs
    score.py

with no real SSH signing, WebAuthn registration/assertion or owner-attestation execution during implementation.
