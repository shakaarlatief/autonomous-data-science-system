# Research 554: independent WebAuthn ES256 assertion verification component

**Date:** 2026-10-12
**Status:** BOUNDED_PUBLIC_ES256_VERIFIER_PASS / SOURCE_ORIGIN_UNQUALIFIED / F1_UNFROZEN
**Parent:** Research 530, 540, 550–553; Checkpoint 889; the accepted B01/B02 and prospective F1/F2 independence requirements.
**Scope:** A verification-only, non-owner ES256 assertion candidate independent of the historical RP's verification function.
**Authority:** F1 research implementation and synthetic qualification only, not full scorer, real platform WebAuthn, F1/F2 freeze, Attempt 002 authorization or Project System physical architecture selection.

## Motivation and selection

The F1/F2 independence amendment explicitly requires the future independent scorer to recompute WebAuthn ES256 signature and `clientDataJSON` challenge, RP origin, UP/UV and credential-ID bindings independently from the Node relying-party verifier. Checkpoint 889 qualified a separate SSHSIG Ed25519 component but did not address this parallel, essential B-arm requirement. This increment was selected rather than constructing another abstract receipt wrapper or reopening the old exhaustive-review cycle.

## Implementation and bounded trust contract

New `experiments/r0_p01_successor_synthetic/independent_webauthn_es256_verify.mjs` is a standalone Node ESM `--verify-only` public JSON CLI. The input supplies a complete expected run-bound statement, *separately enrolled* WebAuthn public credential and an untrusted assertion proof. It does not infer the expected statement, signer, or decision from the proof and has no key creation, signing, browser, server, file-writing or owner ceremony entrypoint. It imports no historical RP or synthetic signing worker.

The verification path independently checks:

- exact successor statement fields, domain, nonce, decision and digests and a separately implemented sorted JSON serializer;
- canonical base64url and public credential ID, DER SubjectPublicKeyInfo, expected P-256 curve and SHA-256 public identity;
- credential-ID equality; authenticator's SHA-256(`localhost`) RP ID hash; `UP` and `UV` flags; no unqualified attested-credential/extension flags in this synthetic data profile; and four-byte sign counter (observed, not a replay or eligibility gate);
- strict UTF-8 `clientDataJSON` with duplicate-key detection, `webauthn.get`, exact `http://localhost:8765` origin, no cross-origin use, and challenge equal to base64url(SHA-256(expected canonical signed statement));
- a constrained, canonical, positive-scalar P-256 ECDSA DER signature, followed by `node:crypto.verify('sha256', authenticatorData || SHA-256(clientDataJSON), enrolled public key, signature)`.

The resulting `VALID` or `INVALID` is derived by the verifier and not copied from a proof flag. Operational exceptions are not silently converted to valid cryptography; the CLI returns `ERROR` for unexpected exceptions. The verifier requires the `synthetic_non_owner=true` marker from its current **synthetic-only data profile**. This is **not** the final schema for real browser/authenticator assertions; F1 and F2 must explicitly qualify that later transition instead of presenting synthetic markers as evidence of a real user.

## Tests and evidence

`tests/unit/test_r0_p01_independent_webauthn_es256_verifier.py` adds **47 executable non-owner tests** against actual ephemeral P-256 signatures issued by the existing separate synthetic worker. The positive signer and an independent foreign synthetic signer both verify against their own public roots; a foreign signature fails under the enrolled key. Signed statement mutations, challenge/origin/type, crossOrigin, duplicate client JSON keys, bad UTF-8, RP ID hash, missing UP/UV, invalid authenticator flags, malformed/noncanonical DER, wrong signer IDs and missing/noncanonical proof fields all fail closed. The worker's own verifier is used as a test comparator on positive vectors, but no shared worker verification result is consumed in the candidate's decision path. Three additional hardening tests reject ambiguous duplicate keys at the outer request, expected statement and enrolled public-credential levels before JSON parsing. These supplement the original 44 cases, bringing the new test count to **47**.

This verification component uses Node built-in cryptography just as the separate synthetic signing worker and historical RP do. Its **parsing, input-validation and message reconstruction implementation is independent of the RP**, but its underlying cryptographic library is not an independent vendor/library implementation. The implementation and tests were authored in this same ChatGPT interaction session, and no separate blind expected-output reviewer or full scorer freeze has occurred.

The complete focused tests after addition passed **509/509**: 243 new-plus-prior candidate/reference cases, 63 cryptographic/admission security cases, 70 claim/governed cases, 46 measurement/finalization cases and 84 structural/provenance guards. See Validation 242 for exact grouped evidence. These are not a complete integrated V3 or a genuine owner experiment.

## Unresolved readiness and scope

Still open: a real WebAuthn browser/RP source, real platform capability/NotSupportedError vs NotAllowedError attribution, independently authored terminal P0/S01/S02/S03 receipts, authentic issuer admission and currentness, real owner-only SSH/WebAuthn input, full independent arm scoring and 13-control verification, Windows process/console/atomic-snapshot qualification, F1 frozen expected fixtures, F2 runtime qualification, A/B/C full synthetic rehearsal and independent reviewer acceptance.

**Next meaningful work:** connect independent SSH and WebAuthn cryptographic verification to actual claim-bound RP/browser event production with durable source evidence and clear interruption/failure attribution, and then to the complete F1 scorer. Avoid more standalone proof parsers unless a demonstrated requirement justifies them. The current architecture and infrastructure remain freely redesignable.

```text
RESEARCH_554=INDEPENDENT_ES256_VERIFIER_COMPONENT_PASS_BOUNDED
NEW_EXECUTABLE_TESTS=47
FOCUSED_TOTAL=509
REAL_WEBAUTHN=NOT_RUN
FULL_SCORER=UNQUALIFIED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
