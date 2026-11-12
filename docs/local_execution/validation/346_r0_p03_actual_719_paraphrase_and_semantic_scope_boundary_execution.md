# Validation 346: Actual 719-query paraphrase and evidence-scope execution

**Date:** 2026-11-12
**Status:** ACTUAL_719_QUERY_EXECUTION / PARTIAL_LINGUISTIC_COVERAGE / UNSUPPORTED_SCOPE_ABSTENTION_CHECK
**Scope:** Record exact full result identity and observed scope/negative outcomes, distinctly from independent authority or scored architecture evaluation.
**Authority:** Executed real-source runner, fixed V01 contract, Research 647, Checkpoint 910.

## Actual source and result receipt

    SCRIPT=experiments/r0_p03_navigation_probe/exploratory_paraphrase_scope_and_abstention_v01.py
    RESULT=experiments/r0_p03_navigation_probe/exploratory_paraphrase_scope_and_abstention_result_v01.json
    RESULT_BYTES=1276498
    RESULT_SHA256=b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e
    PRIOR_CHECKPOINT_909_RESULT_SHA256=99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399
    SOURCE_REVISION=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    SOURCE_FINGERPRINT=01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09
    ORIGINAL_SOURCE_FILES=65
    DIRECTED_LITERAL_EDGES=110
    NEW_QUERIES=719
    EXPLICIT_PATH_REFERENCE_QUERIES=520
    UNSUPPORTED_REAL_WORLD_SCOPE_QUERIES=195
    UNKNOWN_OR_AMBIGUOUS_TITLE_CONTROLS=4
    STRUCTURAL_REFERENCE_OPPORTUNITIES=880
    TOP10_HIT_CEILING=832

Actual execution `python -B -m experiments.r0_p03_navigation_probe.exploratory_paraphrase_scope_and_abstention_v01 --output` produced one new exclusive-create JSON trace with all 719 exact request strings, parser statuses, source/identity states, top-ten lexical candidate paths, asserted relation paths and source-derived structural audit references.

Source-scoped S1, S2, H1: **130/130** accepted each; **208/220** required path instances found each; **60/60** valid source-relative no-edge states each. H2: **0/130** accepted; **0/220** required found; **130** `unparsed_in_scope`, **0/60** true valid no-edge states. S1/S2 were known morphology to the parser; H1/H2 predeclared held-out forms. The old Checkpoint 909 exact grammar independently recognized **0/719** newly worded cases.

Unsupported dependent/governing/hyperlink claims: **195/195** safe `unsupported_scope` abstentions, with no authoritative relation assertions. Unknown and ambiguous titles: **4/4** separate safe identity rejection. The simple lexical search returned **7,190 candidate slots** in 719 questions; these are not relation answers or proofs of hallucination.

## Scientific boundary and post-run checks

The graph answer oracle and accepted index treatment share the same exact literal path extractor, and the query families were hand-authored by the coordinator; structural max-hit performance is expected and not a blind measure. `unparsed_in_scope` cannot be counted as correct evidence absence. There is no claim about real operational dependencies, governed source relations, working hyperlink targets or production authority.

The focused new and preceding 130-query source-relation regressions passed **13/13** (7.52 seconds), including independent rerun, exact complete JSON digest and H2/negative-control outcomes. ## Actual full precommit engineering checks

- Exact 719-query test and predecessor 130-query relation implementation: **13/13 PASS** (7.53 seconds).
- Previous hybrid, 65-title, nine-topic and B2 citation experiments and C02 independent evidence-boundary tests: **34/34 PASS** (12.74 seconds). Combined current/previous source-based regression coverage **47/47 PASS** in two isolated no-pytest-cache runs.
- `scripts/check_current_routing.py`: **PASS**, Checkpoint **910**, boundary `p-three-paraphrase-scope-guard-tested`, latest formal outcome **INCOMPLETE**.
- `scripts/check_knowledge_map.py`: **PASS**, 19 topics, Research **647**, **911** numbered checkpoints (000-910).
- `scripts/check_checkpoint_metadata.py`: **PASS**, **911/911** canonical checkpoint records compliant, no errors/warnings.
- `git check-attr text` on immutable actual 1,276,498-byte result JSON: **unset**, preserving raw bytes across Git checkout.
- `git diff --check`: exit **0**, routine Windows tracked-text LF-to-CRLF warnings only.
- Full `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including family-aware contracts, project knowledge, canonical checkpoints, Knowledge Map, collaboration and current routing.
- Independently rechecked exact output length and SHA-256: **PASS**.

These were observed before commit and publication, which require distinct after-push evidence. No independent source-authority gold, official Research 513 scoring, or actual governed link semantics is claimed.
