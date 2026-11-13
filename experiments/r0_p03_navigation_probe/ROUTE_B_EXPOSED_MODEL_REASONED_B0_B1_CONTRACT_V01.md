# Route B exposed GPT-6 reasoning over fixed original B0/B1 source evidence

**Date:** 2026-11-13
**Status:** PROSPECTIVE_SOURCE_ONLY_ANSWER_AUTHORING_CONTRACT / NO_GOLD_IN_EXPORTED_PACKET / AUTHOR_PREVIOUSLY_EXPOSED / NO_FORMAL_SCORE
**Owner direction:** Advance actual R0-P03 full answer reconstruction promptly using the already executed Route B twelve primary questions. Avoid another indefinite preparatory evidence-qualification cycle.

## Inputs and scope fixed before authoring

The immutable source world is the same Checkpoint 918 Git revision `47ed6344a9153dcf366769e95722840fbf1a8f8b`, 60 build and 20 heldout original source files, twelve coordinator-authored questions. Use exactly the previously saved Checkpoint 921 original source-cited extractive evidence result `route_b_extractively_cited_answer_evidence_result_v01.json`, size **995317** SHA-256 **`17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8`**. Its arm-source rankings were frozen in Checkpoints 918–920 and its source evidence selectors fixed in Checkpoint 921.

Export an **answerer-visible, gold-free** source packet in the exact original question order for two already executed structurally distinct methods only: `B0_ORIGINAL` and `B1_EXPOSED_SUBJECT_B0`. For each of 12 questions × 2 arms, include the question, each original top-three source path and its exact Git original source SHA, and the selected complete original source line numbers/text/SHA from Checkpoint 921. Do not copy any original reference answer, intended source, required reference excerpt, previous grade or model-evaluation outcome into the packet. Its output and hash must be frozen before manual GPT-6 authoring.

Why two instead of seven: this is the first **actual model-authored prose response** comparison, not a comprehensive formal score. B1 and B0 are a controlled contrast using the same 12 questions and original evidence extraction budget. B2/B3/LSA remain fully preserved in Checkpoints 919–921 and should not be silently treated as evaluated by this prose-author pass. Future other-arm prose reconstruction must be separately prospectively declared and recorded.

## Model and authoring constraints

The answerer is **this same GPT-6 assistant**, not a newly isolated fresh agent. It has prior exposure to this repository, source world, both arm outputs and coordinator-authored draft reference answers. The exported packet is mechanically gold-free, but the model's *context and memory are not*, so no blind evaluation, independent gold, independent semantic entailment or Research 575 Level B admission is inferred. The responses are an exploratory source-constrained model-author study.

For each of the **24** question × arm records:

1. Answer only from the original cited lines supplied to that arm. Distinguish historical statement, candidate/proposal, selected logical design, accepted conceptual foundation, current operative authority and genuine deployment. Never infer an operative switch from the word `Accepted` alone.
2. Every substantive assertion must name its supporting source **rank and original line number(s)** in the exact frozen packet. A source may be cited only if it was among that arm's actual top three and the cited line was present in its 5-or-fewer selected original lines. No citing a source merely because the model already knows it.
3. If the retrieved evidence does not directly establish the asked fact, explicitly abstain on that fact. A later-recorded supersession or amendment must not be imported into a frozen earlier historical question as if it were the prior status. Conflicting source statements must be identified by source and temporal scope.
4. Provide a short natural-language `answer` (not a template quotation renderer), an explicit `coverage` from `SUPPORTED`, `PARTIAL`, `ABSTAIN`, an `authority_boundary` note where material, and `claims` with exact `source_rank` (1-3) and `line` references.
5. A source title may support file identity and general topic, but not hidden full semantic claims absent its lines. In particular, a document named `Decisions` does not alone prove every project-wide governance property. Distinguish that ambiguity.
6. No external web/context, question rewrites, source changes, higher source limit, use of a fourth-ranked carrier or reference-answer lookup during the model-authored response construction. As an exposed model, nonuse of prior knowledge cannot be guaranteed by process design, so report contamination risk clearly.
7. Freeze all 24 original model-authored outputs as a separate exclusive-create JSON, without retuning the texts after reviewing observed comparator metrics. A mechanical post-author audit validates all cited source line identities and allowed references, exact original source bytes, source/arm counts, no future source leakage and result digest. It does **not** validate natural-language entailment, so language correctness remains reviewer-unqualified.

## Comparison dimensions and forbidden claims

Measure per-arm counts of `SUPPORTED/PARTIAL/ABSTAIN` as **author self-classification only**, not independently scored correctness or original Research513 `>=10/12` acceptance. Preserve 24 full model-generated answer texts, not autogenerated quote templates. Analyze actual paired differences (P01 and prospective limitation P02/P03; historical P10 later gate amendment). Highlight what the answerer did not know.

An actual independent reviewer may later examine the frozen packets and answers through an authorized Claude/Codex route, but neither Claude's previous timed-out readiness call nor a Codex call requiring the owner's separate metered authorization counts as review. Do not circumvent those controls or claim fresh reviewer truth.

Formal original Research513/559/576 R0-P03 remains `INCOMPLETE`: reference gold is exposed coordinator-authored, complete V03-native common substrate and source-owned B1 metadata unqualified, only 2/5 arms receive this specific model prose pass, the nine independent historical legacy tasks and heldout F1 are still unscored, no zero-false-authority formal gate or two fresh scored evaluators. No physical architecture, authority switch, repository workflow or migration is selected.

    ORIGINAL_PRIMARY_QUERIES=12
    AUTHOR_OUTPUTS=24
    COMPARED_METHODS=B0_ORIGINAL,B1_EXPOSED_SUBJECT_B0
    SOURCE_CONTEXT=CHECKPOINT_921_TOP3_FIVE_ORIGINAL_LINES_PER_SOURCE
    MODEL=GPT-6_EXPOSED_COORDINATOR
    ANSWERER_PACKET_HAS_GOLD=false
    MODEL_AUTHOR_HAS_HISTORICAL_EXPOSURE=true
    FULL_SEMANTIC_CORRECTNESS_INDEPENDENTLY_VERIFIED=false
    FORMAL_R0_P03_RESULT=INCOMPLETE
