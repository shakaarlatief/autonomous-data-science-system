# Exploratory T2 V02: evidence-to-referent binding, ambiguity, and unsupported operative authority

**Date:** 2026-11-13
**Classification:** EXECUTION_FIRST_EXPOSED_REGRESSION_WITH_FIXED_NEW_CHALLENGES / NOT_INDEPENDENT_GOLD
**Prior immutable result:** Checkpoint 913 T2 V01 result `exploratory_t2_owner_status_guarded_retrieval_result_v01.json`, exactly 224009 bytes, SHA-256 `b56b2f173cb69f34e5d6a009421ce738fab5640c47b615796a51a3005b77e843`.
**Historical source pin:** `e8ae867392f818f43dc8b76984f164e277d5cc87`.
**Question:** Can an answer channel refuse source-backed facts about the wrong document, while preserving useful lexical candidate retrieval, when identity is known, partial, contradicted, or unsupported as a current governing claim?

## Input and subject-binding contract, frozen before V02 output

Reuse the exact full 120-source bytes, sample and 24 queries from T2 V01 without modifying that output or any source. The original 65 W5 historical paths must remain excluded. Source paths/contents/hashes and the old rank@10 results must match original V01. Rebuild the *same* SQLite FTS5 unicode61/BM25 index over 120 original document bodies, no learned model, no additional source data, no global repository search. New policies see exactly the same top ten candidate paths as old V01 for its 24 source-status queries.

The question body contains a `topic` field as generated from source headings by V01. An executable user-question parser is **not** being claimed: these are structured test-request messages whose topic and intent are known, and all origin is coordinator-generated. For each candidate from top ten, attempt to derive its first H1 from actual archived source bytes. Some source distractors have no first H1; for those, mark the candidate as **not identity-bound** rather than infer a substitute title or crash. For H1-bearing candidates, run the original V01 `topic_from_heading` transformation, normalize punctuation/whitespace/case to a nonempty token sequence, and compare that to the normalized topic supplied by the query. Accept a candidate as **bound to the question** only if its complete normalized topic exactly matches and exactly **one** candidate in the top ten matches. If two match, abstain `AMBIGUOUS_SOURCE_IDENTITY`. If none match, abstain `IDENTITY_NOT_VERIFIED`. A source-header status on a different relevant document is **never** the requested source's status. This strict identity rule may lose recall on genuine paraphrases, aliases, renamed sources and unseen titles; this is intentional for a fail-closed mechanistic stress rather than a proposed universal answer engine.

For `RECORDED_SOURCE_STATUS` requests, on exactly one bound source use only its native first-100-line `Status` already parsed by T2 V01 and the exact original Status line witness, and return only `ASSERTED_SOURCE_STATUS_ONLY`, or `NOT_FOUND_IN_COVERED_SCOPE` if this header does not classify into the three source-status labels. For an `OPERATIVE_GOVERNANCE` request, **always** return `UNSUPPORTED_OPERATIVE_GOVERNANCE` regardless of archived header; no signed/lifecycle authority or currentness gold exists in this fixture. In all cases keep the same independent top-ten lexical source candidate list marked **NOT_AUTHORITY**, and never promote a candidate solely because the score is high.

## Complete fixed challenge matrix

Use exactly the original V01 24 frozen title-derived topic requests and add the following *source-derived, nonblind* controls, with all challenge requests generated before any index query:

- **BASE_RECORDED_STATUS**: 24 original V01 topics; compare original rank-one header interpretation to subject-bound top-ten interpretation, especially original T2-08 and T2-24.
- **CONTRADICTORY_RECORD_NUMBER**: for every original topic starting with a numbered `Research N:`, `Checkpoint N:`, or `Specification N:`, replace only its numeral with the numeral of the next topic in the *same* numbered family among the 24 tasks (sorted numeric sequence, cycling), preserving the rest of the title. This constructs an intentionally conflicting identifier/title. The engine must not assert either candidate's status.
- **UNKNOWN_RECORD_NUMBER**: for the same numbered subset replace the numeral by `999999`, keeping the remaining title. The engine must not assert existence or a status.
- **PARTIAL_TOPIC**: for each of 24 topics, remove its full numbered prefix if present; take only its first two alphanumeric remaining words, then append literal `overview`. This is deliberately insufficient to bind the complete subject; no status assertion is allowed.
- **OPERATIVE_GOVERNANCE**: for all original 24 topics, change request intent to `OPERATIVE_GOVERNANCE` asking `Does this currently govern?`. The same lexical candidates are still available, but a historical source-header class cannot authorize a current governing assertion.

All challenge counts and any missing numerically identifiable topics must be recorded explicitly. The control source topic is synthesized from the same old 24 titles, not from independent novel human questions. Neither a request's hidden original expected path nor its class may be provided to retrieval, matching or assertion engines. Those are used **only after** generation for evaluation. Refuse to emit any apparent score for operational governance correctness, since this fixture has no trusted governing-currentness answer gold.

## Fixed measures and negatives

Report total requests, counts per matrix family, exact original 24 candidate ranking parity, original rank-one wrong-source recorded-status assertions, subject-bound correct source-status answers, new subject-bound wrong-source assertions, number of ordinary status abstentions for each challenge type, number of unsupported-operative abstentions and presence of candidate suggestions in all cases.

Preserve per-case: query/intent/topic, exact top-ten paths, any matched source H1 and path, witness line+SHA-256, subject-binding disposition, source-status-only claim, separate nonauthoritative candidates, expected original path/class only as evaluation metadata, correctness of claim relative to same original V01 bounded source-header task. No `closed world` or unsupported operational currentness conclusions.

Do not change V01 failure traces, its 120 source sample, original Checkpoint 913 or formal Research 513/559/576. The 65 historical W5 set and this 120-member V01 set are now regression fixtures for any repeated measurements. Future independently worded real lifecycle tasks remain separate. Source-title equality will predictably favor this method on title-derived requests, and is not scientific evidence of natural-language identity resolution.

    SOURCE_INPUT_PIN=e8ae867392f818f43dc8b76984f164e277d5cc87
    PRIOR_T2_V01_BYTES=224009
    PRIOR_T2_V01_SHA256=b56b2f173cb69f34e5d6a009421ce738fab5640c47b615796a51a3005b77e843
    ORIGINAL_TARGETS=24
    CORPUS_SIZE=120
    CONTROL_CLASSES=BASE_RECORDED_STATUS_CONTRADICTORY_RECORD_NUMBER_UNKNOWN_RECORD_NUMBER_PARTIAL_TOPIC_OPERATIVE_GOVERNANCE
    CANDIDATES_K=10
    ORACLE_INDEPENDENT=false
    OPERATIVE_AUTHORITY_ADMISSION=NONE
    PHYSICAL_ARCHITECTURE_SELECTION=NONE
    FORMAL_R0_P03_SCORE=NONE
    FIRST_ATTEMPT=NO_OUTPUT_ABORTED_ON_MISSING_DISTRACTOR_H1
    CORRECTION=PRE_FIRST_RESULT_UNHEADED_DISTRACTOR_FAILS_IDENTITY_BINDING
    OUTPUT=EXCLUSIVE_CREATE_NEW_V02_JSON
