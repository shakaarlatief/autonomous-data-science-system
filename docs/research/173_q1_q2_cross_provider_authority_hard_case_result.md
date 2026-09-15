# Research 173: Q1 + Q2 Cross-Provider Authority Hard-Case Result

**Date:** 2026-09-15
**Status:** CROSS-PROVIDER Q1+Q2 SUPPORT PASSED / ALL NON-Q10 ITEMS NOW HAVE REAL EVIDENCE / Q10 FINAL MULTIDIMENSIONAL QUALIFICATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification clusters:** Q1 provider/tool portability + Q2 authority hard cases
**Fixture freeze commit:** `3652996296021c34ecbefffe6723b059bac76801`
**Exact real base:** `a685ef48c4c4853babff9295f03f198c7b3dcd1d`
**External provider:** Anthropic
**External model:** Claude Opus 5
**External effort:** High
**Scope:** Preserve the untouched fresh external-provider result, evaluate it against the separately frozen oracle, record portable authority behavior across provider boundaries, and close the final three non-Q10 real-evidence gaps without granting final qualification or target selection.
**Authority:** Cross-provider qualification evidence only. Current continuity remains operational authority.
**Declared references:** `research:172`, `research:171`, `research:168`, `research:144`, `checkpoint:517`

## 1. External-provider run provenance

The project owner ran the frozen request in a completely fresh standard Claude chat outside the ADS Claude Project. The run used:

```text
provider          Anthropic
model             Claude Opus 5
effort            High
fresh session     true
prior ADS context false
web browsing      not used by experiment instruction
attached evidence PORTABLE_PROVIDER_PACKET_V01.md only
```

The result was copied verbatim into the repository and preserved before oracle evaluation:

```text
EXTERNAL_PROVIDER_RESULT_V01.json
FIRST_RUN_EXTERNAL_PROVIDER_RESULT_V01.json
SHA-256  d118cc88c6576ef35470fed95e48c7ee13fc295a7ce64dab919c871f15ec8ef8
byte-identical  yes
```

No result repair occurred before evaluation.

## 2. Task A: explicit scoped replacement beats retrieval rank

The retrieval layer deliberately ranked `D-011` first, but Claude resolved:

```text
governing decision  D-028
resolution          RESOLVED
retrieval authority false
```

The reason correctly follows the Candidate 01 relation:

```text
D-011 --REPLACE(scope=v1_persistence_retrieval_architecture)--> D-028
```

This is direct cross-provider evidence that a probabilistic nomination can remain useful for discovery without becoming the governing authority decision.

## 3. Task B: under-specified authority scope remains unresolved

For the intentionally vague question “Which implementation architecture decision governs?”, Claude did not choose the highest-ranked retrieved source and did not invent a subsystem.

```text
resolution          UNRESOLVED_INSUFFICIENT_SCOPE
governing IDs       []
retrieval authority false
```

The result explicitly identifies the missing subsystem/scope and explains that D-011 has different scoped successors plus residual applicability. It also surfaces a further evidence limitation: the packet contains canonical excerpts for D-011/D-015/D-028/D-033 but not the full source-local lifecycle declarations of D-029/D-030/D-031/D-032.

That extra caution is desirable. The collaborator refuses to claim more authority resolution than the bounded evidence supports.

## 4. Task C: partial supersession preserves retained outcome

For external learning-source architecture, Claude reconstructs:

```text
current governing architecture  D-033
retained D-015 outcome           public_git_source_binary_exclusion
source binaries allowed merely because ADS consumes them  false
retrieval authority              false
```

This matches the intended Candidate 01 semantics: D-033 replaces D-015 for the architecture-uncertainty scope, while D-015 retains the durable public-Git exclusion outcome.

## 5. Authority receipt

The external provider binds its receipt to exact real base:

```text
a685ef48c4c4853babff9295f03f198c7b3dcd1d
```

and records:

```text
retrieval_is_non_authoritative = true
```

It also preserves unresolved items rather than hiding them, including the under-specified Task B scope and bounded-packet evidence limitations.

## 6. Oracle comparison

`EVALUATION_V01.json` records:

```text
semantic checks  20 / 20 PASS
failed checks     0
cross-provider support true
```

Two literal status-label variances are preserved rather than rewritten:

```text
Task B
oracle    UNRESOLVED_SCOPE_REQUIRED
observed  UNRESOLVED_INSUFFICIENT_SCOPE
semantic match true

Task C
oracle    RESOLVED_WITH_RETAINED_OUTCOME
observed  RESOLVED
retained outcome explicitly present
semantic match true
```

These are non-semantic label differences. The untouched external result already contains the required unresolved-scope behavior and retained-outcome semantics.

## 7. Portable packet materialization provenance

The packet attached to Claude was the Windows working-tree materialization frozen by Research 172:

```text
working-tree packet SHA-256
    dc24924a828da7ea4d2421e70c35d7d65a0b42decf83cb3d03c888a461a351b8

canonical Git blob SHA-256 at freeze commit
    669715d607f3ac4fd71f7e9d653b9721ca1d8bc173cb01197b28ed44176c4799
```

The two byte streams differ only by checkout line-ending materialization; LF-normalizing the working-tree packet reproduces the canonical Git blob exactly. This does not affect the semantic cross-provider result, but it exposes a provenance-format weakness in the Research 172 freeze metadata: the published attachment digest did not label its byte basis explicitly.

The Research 168 revision-binding rule is therefore extended to external attachments:

```text
repository identity
    source_commit
    source_path
    hash_algorithm
    hash_basis = GIT_BLOB_BYTES_AT_COMMIT
    content_digest

attachment identity
    materialization_basis
    raw_attachment_digest
```

Future external-provider fixtures must record both when attachment bytes may differ from canonical repository bytes.

## 8. Verification

```text
focused cross-provider tests          9 / 9 PASS
exhaustive partitioned unit suite   300 / 300 PASS
```

The external result itself required zero repair. Evaluation is deterministic from the frozen oracle and preserved result.

## 9. Evidence disposition

This result adds real evidence for the final three non-Q10 gaps:

```text
KA-R36  provider and tool portability
KA-R14  supersession / supplementation / conflict visibility
KA-R24  probabilistic retrieval is not sole governing authority
```

The Candidate 01 evidence field therefore becomes:

```text
real-evidence items             64 / 67
synthetic-or-better items       64 / 67
full-real subsystem clusters    Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9
remaining non-real items        KA-R30 KA-R40 KA-R41
remaining cluster               Q10 only
final qualified passes           0 / 67
```

All non-Q10 items now have some real Candidate 01 evidence. This is the point at which the Q10 final governing program can begin without wrapping known untested architecture mechanisms.

## 10. Next step

The next step is Q10 final multidimensional qualification. It must establish:

```text
KA-R30  bounded task-specific qualification budgets
KA-R40  both structural and behavioral qualification
KA-R41  multidimensional reconstruction quality without one aggregate winner score
```

Q10 must consume the entire frozen acceptance boundary and the accumulated evidence field. It must not convert descriptive subsystem evidence into automatic final passes. Final requirement/invariant dispositions, architecture selection, owner acceptance and any authority switch remain separate later decisions.

```text
RESEARCH173=CROSS_PROVIDER_Q1_Q2_SUPPORT_PASS
PROVIDER=ANTHROPIC
MODEL=CLAUDE_OPUS_5
SEMANTIC_CHECKS=20_OF_20
RESULT_REPAIRS=0
REAL_EVIDENCE_ITEMS=64_OF_67
ALL_NON_Q10_ITEMS_HAVE_REAL_EVIDENCE=true
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=Q10_FINAL_MULTIDIMENSIONAL_QUALIFICATION
```
