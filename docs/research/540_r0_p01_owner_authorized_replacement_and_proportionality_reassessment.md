# Research 540: R0-P01 owner-authorized replacement and proportionate experiment qualification

**Date:** 2026-10-11
**Status:** OWNER PROCEDURAL APPROVAL RECEIVED / PRIOR REVIEW CYCLE PAUSED / PROSPECTIVE QUALIFICATION TRIAGE NEXT
**Scope:** Reassess the root cause of excessive R0-P01 review work, identify the essential scientific and security requirements, and apply the owner's approved simplified replacement procedure without changing the production ADS architecture.
**Parent:** Research 513 / 529 / 539, Checkpoint 875, MC-0030 Messages 055/057/059, owner B01/B02 decisions, and the new separate owner procedure decision.
**Authority:** Task-owner reconciliation of explicit human research-procedure approval. Does not approve a trial, scorer, physical architecture, production trust root or replacement credential.

## Why this changed

The preceding campaign built an 18-batch / 1,022-unit independent normative audit (967 reviewer ACCEPTED; 55 PENDING), 17- then 24-scenario source-bound scoring matrices, 15 source-site decision candidates and repeated independent reviews (Messages 055, 057, 059). These identified real security and attribution issues but also created a reflexive **design -> review -> new qualification -> review** loop before implementing and testing the successor experiment.

The project owner objected specifically to **unnecessary effort spent engineering around an owner-governance choice without first asking the owner**. The objection was **not** that ADS architecture quality should be compromised, that extensive genuinely useful engineering is unwanted, or that scientific evidence may be fabricated. The owner approved an explicit, simpler owner-authorized replacement procedure. The precise decision and supersession boundary are recorded in:

`docs/research/r0_p01_successor_design/R0_P01_OWNER_AUTHORIZED_INTERRUPTION_REPLACEMENT_DECISION_20261011.md`.

## Actual research objective and necessary controls

R0-P01 asks whether independently verifiable owner-exclusive cryptographic governing acceptance is **usable at realistic volume** and compares SSH signatures, WebAuthn/Windows Hello and a weaker identity comparator. Essential evidence includes proper sign-what-you-see semantic binding, anti-forgery/alteration/replay/trust-root/recovery controls, correct owner-proof verification, comparable small and large trial burden measures, no secret disclosure, representative failures, honest reporting, and preregistered scientific comparisons. None inherently requires a two-attempt numerical cap for accidental interruption.

An owner declaration is sufficient **to authorize procedural replacement** but is not equivalent to valid cryptographic proof. Preservation of raw interrupted evidence and explicit cause/authorization/disposition is sufficient research traceability for a replacement, without constructing an exhaustive adjudication oracle for every hypothetical Ctrl+C/Node timing race **just to determine retry eligibility**. A genuinely required technical observability or safety test remains essential when needed to protect evidence or execution.

## Immediate impact on Message 059 and F1/F2

Claude Message 059 remains preserved as the independent review of the former 15-row candidate table. Its critique about assertion-time NotSupportedError remains technically important because incorrect capability assessment could misrepresent **WebAuthn viability**, not just retries. Its false-positive security test findings, independent proof verification, Windows crash-safe evidence requirements and true integrity/failure classification also merit bounded testing.

But it is **not automatically the next work order** to amend D01-D15, hash-pin them again, request Message 061, and repeat. Decide first what must be demonstrated for a fair, safe R0-P01 comparison.

| Work | Provisional necessity assessment |
|---|---|
| Cryptographic forgery, changed-view/statement, replay, recovery and negative-test sensitivity | ESSENTIAL; must actually be tested |
| Correctly bind owner approval/credential proof to shown bytes, distinguish unavailable WebAuthn capability | ESSENTIAL; directly affects mechanism conclusion |
| Safe interrupted-process cleanup and no falsely valid proof, crash-safe evidence capture | ESSENTIAL at appropriate implementation level; use targeted Windows synthetic tests |
| Reliable timing/usability measurement, owner error/abort counts, full result provenance | ESSENTIAL; disclose accidents/replacements |
| Precise distinction between INVALID subtypes solely to award a B02 exceptional re-claim | NO LONGER A REPLACEMENT GATE; only retain where scientifically/security relevant |
| Requiring all 55 pending source-unit findings to receive independent detailed review before any code | NOT AUTOMATIC; risk-classify against essential requirements first |
| Additional hash pinning, broad static documentation guards and recurring cross-model review | OPTIONAL unless they materially mitigate a demonstrated risk |
| Immediate new live owner-credential experiment | NOT AUTHORIZED; synthetic and readiness work still required |

## Proportional implementation path

1. **Explicitly supersede historical B02 replacement restrictions prospectively**, not by altering its old byte-bound artifact. Keep B01 scientific class/evidence semantics and Attempt 001 history intact.
2. **Triage open findings by actual risk**, not old exceptional claim rights, and create a short implementation-facing checklist of essential controls and behavioral outcomes. Preserve the audit as background trace rather than requiring completion of every documentation subtask.
3. **Implement and synthetically qualify the smallest suitable successor**, with independent real cryptographic positive/negative tests and targeted native Windows checks only where the results matter to safe operation or valid proof evidence.
4. **Measure, preserve and disclose all interruptions and declared replacements** as part of the experiment's friction/reliability observations. Fresh run identity and fresh explicit owner consent are required for each real execution, not a separate complex proof of accident.
5. Use independent Claude critique when it finds a material security issue, helps test a design choice, or verifies the implementation. Avoid automatic cycles of speculative scored-vector design and artifact-hash approval.
6. Present the actual readiness and practical burden of the next run to the owner, then ask independently for the required explicit real Attempt 002 authorization. No changes to production ADS identity or physical target follow automatically.

**Avoid a second overcorrection:** Do not turn simplification into uncritical green-runs-only testing. Preserve negative outcomes and preregister substantial protocol revisions. The owner can choose to continue *research* after an accident without making missing/invalid cryptographic proof valid.

```text
RESEARCH_540=OWNER_PROCEDURE_APPROVED
REVIEW_CYCLE=PAUSED_FOR_PROPORTIONALITY_TRIAGE
F1_F2=UNFROZEN
OWNER_TRIAL=NOT_AUTHORIZED
```
