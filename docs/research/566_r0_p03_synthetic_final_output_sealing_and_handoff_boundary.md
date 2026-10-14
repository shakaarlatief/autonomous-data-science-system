# Research 566: R0-P03 synthetic final-output sealing and handoff boundary

**Date:** 2026-10-14
**Status:** SYNTHETIC_CAPTURE_MECHANICS_POSITIVE / REAL_REVIEWER_GOLD_CUSTODY_UNQUALIFIED
**Scope:** Test whether simulated reviewer final output can be validated and encrypted directly from memory through a pipe, without writing an intermediate plaintext file, while maintaining strict separation from real benchmark tasks, answers and credentials.
**Parent:** Research 513, 559, 561–565; Validation 254; MC-0030; starting HEAD `6294ef031e85911ca67e63bc27748e9c592a2cb6`.
**Authority:** Bounded fake-only mechanical evidence, not reviewer independence, reference authoring, accepted ciphertext custody, a real scorer, an experiment freeze or new physical architecture.

## 1. Narrow problem and motivation

Research 565 found an installed 7-Zip GUI and CLI with working fake-data AES archive round-trip. Its first proof used a fabricated plaintext staging file. The remaining practical question is whether a bounded collector can accept a simulated provider stream and seal only its final structured result **without that intermediate plaintext file**.

This does **not** prove that the actual provider, model process or terminal leaves no transcripts, history, debug logs, process memory or pagefile content. Nor does sealing fake output qualify an independent gold author or authorized storage principal. The earlier owner-terminal Read/Glob/Grep denials remain valid for the exercised paths only.

## 2. Synthetic-only implementation

Added `experiments/r0_p03_navigation_probe/synthetic_output_collector_candidate.py` and `tests/unit/test_r0_p03_synthetic_output_collector.py`.

The prototype uses standard-library Python and an existing local `7z.exe`. It constructs exactly nine **fabricated** legacy cases and twelve **fabricated** primary cases in the Research 513 four-by-three category arrangement. Every case ID, claim and source is a fixed unmistakable synthetic sentinel, not a question or source from the real R0-P03 task pool.

The simulated Claude-style JSONL stream includes nonfinal events and one terminal `result`. The parser selects only the single successful terminal event, bounds input size, validates strict UTF-8, rejects malformed and duplicate terminal results, and checks an exact fixed fake-only packet schema. Nonfinal assistant text is not promoted to an answer. Real-looking claims or unknown fields fail closed.

For a valid fake packet, Python passes its canonical JSON bytes directly to 7-Zip `-si` over a subprocess stdin pipe. A `.7z` archive is created using `-t7z -mhe=on` inside a newly created, purpose-named disposable `.venv` scratch directory. The collector does not create a plaintext packet file, overwrite an existing archive, print packet contents or print a test password. The public-facing synthetic receipt contains only case counts, lengths, digests and booleans, including `real_output_custody_qualified=false`. A separate extraction subprocess verifies byte-exact recovery; an incorrect password is rejected. The demo deletes its temporary archive and key.

**Critical restriction:** This is **not a production collector**. It accepts only an exact fixed fabricated packet and a disposable `SYNTHETIC_ONLY_` password. The test passes this dummy password via subprocess arguments, which is **forbidden for real secret handling**. The interface cannot be used for real historical answers, genuine owner data or secrets without explicit redesign and fresh qualification.

## 3. Evidence and negative tests

A direct subprocess experiment first verified 7-Zip `-si` with an imaginary payload: archive creation succeeded, a separate extraction recovered exactly the original bytes, and no plaintext member file was present. The completed synthetic collector demo then returned: nine + twelve fake slots, exact post-subprocess recovery true, wrong-password rejection true, plaintext-file-written-by-collector false and real-output-custody-qualified false.

The final new unit suite passed **17/17** after repairing a caught scratch-destination weakness. Tests covered:

- Final-only extraction, correct counts and ignored nonfinal material.
- Missing, failed, duplicated, malformed, oversized and invalid UTF-8 stream events.
- Partial 12-case packet, altered fake reference, forbidden real-looking claims and modified synthetic marker.
- Reject real-looking passwords, outside/general temporary destinations and existing encrypted file overwrite.
- Actual AES method listing, wrong-password filename concealment, exact hash recovery, and a receipt with no fake answer text or password.

Initially an unrestricted directory under `.venv` was erroneously allowed, because pytest itself creates scratch directories there. The rule was tightened to disposable `.r0p03-`-prefixed directories under `.venv`, and the negative test passed. Do not count the initial overly broad check as security proof.

This remains evidence from an ordinary agent-executable **synthetic** test, not a separate custodian identity. The parent Python process knows the disposable password and constructs simulated final output. No additional Claude inference or real ADS reference-input exposure occurred.

## 4. Remaining qualification gates

The following have **not** been shown:

| Boundary | Missing evidence |
|---|---|
| Real reviewer output transport | Full actual Claude stdout/provider logs must not expose answer plaintext to later arm authors; no real model inference was run |
| Fresh reference author | Unresumed genuinely unexposed neutralizer with bounded source world and declared previous exposure |
| Owner-only production secret | Trusted owner entry, key storage/recovery and real denial for every arm-author process/tool; test dummy password in argv does not qualify |
| Archive authenticity | Ordinary 7zAES is not AEAD. Exact plaintext digest must be checked against an independently trusted pre-arm commitment, or use a qualified authenticated-encryption mechanism |
| Complete durable packet | Fake demo archive is removed. No full gold bytes were independently versioned, retained and successfully recovered after an authorized custody transfer |
| Arm-author access exclusion | No actual future B0–B4 principal or plugin was tested against real plaintext, source logs or decryption authority |
| Scorer handoff | At least two fresh evaluators, release rules and independent answer access remain prospective |

An archive encrypted with a password accessible to the same coding agents is not a valid secret boundary. Even a perfectly encrypted stored packet is insufficient if its raw generation transcript remains readable. Conversely, requiring new permanent infrastructure before testing available owner-controlled storage/identity options would be premature.

## 5. Recommended next step

Keep the fake-only pipe test as a qualified **mechanical building block**. Next investigate who is allowed to receive the real model's final output, who can securely enter a production secret without CLI arguments/model exposure, and which later arm-author identities are actually excluded from both. Prefer one small **owner-designated synthetic-only end-to-end** custody/denial/recovery test once the principal and output locations are identified. Do not generate actual historical neutralization or select twelve primary questions until that boundary is genuinely qualified.

Preserve the original Research 513 B0–B4 definitions, 9 and 12 case totals, the `>=8/9` historical and `>=10/12` primary gates, exact provenance/currentness requirements, zero false-authority tolerance, legacy Option A, two fresh evaluation roles and parity/heldout/freeze integrity. No physical architecture, migration or current operational authority change is authorized. Checkpoint 898 and `p-three-reviewer-execution-authority-qualification` remain unchanged.

```text
SYNTHETIC_FINAL_PIPE=MECHANICS_POSITIVE
SYNTHETIC_SCHEMA_ONLY=TRUE
REAL_REFERENCE_AUTHOR=NOT_QUALIFIED
REAL_SECRET_HANDLING=NOT_QUALIFIED
INDEPENDENT_REVIEWER_OUTPUT_CUSTODY=NOT_QUALIFIED
R0_P03_SCORE=NOT_OBSERVED
CHECKPOINT=898_UNCHANGED
```
