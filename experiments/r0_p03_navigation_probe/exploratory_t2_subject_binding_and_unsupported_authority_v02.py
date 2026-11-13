"""Execute a fixed subject-binding and unsupported-authority T2 regression.

Only full subject-title identity within the same top-ten lexical candidate
set may license an archived document's OWN recorded Status. This does not
authenticate operative currentness or establish a general NL identity solver.
All challenge language is coordinator-produced from the exposed V01 fixture.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_t2_owner_status_guarded_retrieval_v01 import (
    PIN, RESULT as ORIGINAL_RESULT, ROOT, K,
    classified_status, first_h1, query_from_heading, rank_query,
    source_archive, status_witness, topic_from_heading,
)

IDENTIFIER = "R0_P03_EXPLORATORY_T2_SUBJECT_IDENTITY_AND_AUTHORITY_ABSTENTION_V02"
CONTRACT = "EXPLORATORY_T2_SUBJECT_BINDING_AND_UNSUPPORTED_AUTHORITY_CONTRACT_V02.md"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_t2_subject_binding_and_unsupported_authority_result_v02.json"
ORIGINAL_RESULT_SHA256 = "b56b2f173cb69f34e5d6a009421ce738fab5640c47b615796a51a3005b77e843"
NUMBERED = re.compile(r"^(Research|Checkpoint|Specification)\s+(\d+)\s*:", re.I)
NONALNUM = re.compile(r"[^a-z0-9]+")
REQUEST_KINDS = (
    "BASE_RECORDED_STATUS",
    "CONTRADICTORY_RECORD_NUMBER",
    "UNKNOWN_RECORD_NUMBER",
    "PARTIAL_TOPIC",
    "OPERATIVE_GOVERNANCE",
)
STATUS_INTENT = "RECORDED_SOURCE_STATUS"
OPERATIVE_INTENT = "OPERATIVE_GOVERNANCE"


def normalize_subject(value: str) -> str:
    """Normalize only case, punctuation and whitespace; never fuzzy-match."""
    return " ".join(w for w in NONALNUM.split(value.casefold()) if w)


def challenge_matrix(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Freeze all new topic/intent controls before retrieval execution."""
    by_family: dict[str, list[int]] = defaultdict(list)
    for item in cases:
        match = NUMBERED.match(item["topic"])
        if match is not None:
            by_family[match.group(1).casefold()].append(int(match.group(2)))
    by_family = {k: sorted(set(v)) for k, v in by_family.items()}
    if not all(len(v) > 1 for v in by_family.values()):
        raise ValueError("No same-family alternative for numbered identifier conflicts")
    tasks = []
    for kind in REQUEST_KINDS:
        for item in cases:
            topic = item["topic"]
            numbered = NUMBERED.match(topic)
            if kind in ("CONTRADICTORY_RECORD_NUMBER", "UNKNOWN_RECORD_NUMBER") and not numbered:
                continue
            if kind == "CONTRADICTORY_RECORD_NUMBER":
                ids = by_family[numbered.group(1).casefold()]
                original = int(numbered.group(2))
                next_id = ids[(ids.index(original) + 1) % len(ids)]
                topic = topic[:numbered.start(2)] + str(next_id) + topic[numbered.end(2):]
            elif kind == "UNKNOWN_RECORD_NUMBER":
                topic = topic[:numbered.start(2)] + "999999" + topic[numbered.end(2):]
            elif kind == "PARTIAL_TOPIC":
                remainder = NUMBERED.sub("", topic).strip()
                words = re.findall(r"[a-z0-9]+", remainder.casefold())
                if len(words) < 2:
                    raise ValueError("Partial topic lacks two content words")
                topic = " ".join(words[:2]) + " overview"
            intent = OPERATIVE_INTENT if kind == "OPERATIVE_GOVERNANCE" else STATUS_INTENT
            question = (
                "Does the decision about " + topic + " currently govern this project? "
                "Cite authoritative effect evidence or abstain, and keep suggested documents separate."
                if intent == OPERATIVE_INTENT else
                "What source-recorded owner-decision Status does " + topic +
                " have? Cite that exact document or abstain; keep candidate documents separate."
            )
            tasks.append({
                "challenge_id": "T2-V02-" + str(len(tasks) + 1).zfill(3),
                "family": kind,
                "source_v01_case_id": item["id"],
                "intent": intent,
                "topic": topic,
                "question": question,
                "expected_source_for_evaluation_only": item["expected_source"],
                "expected_status_class_for_evaluation_only": item["expected_source_header_class"],
                "original_h1_for_evaluation_only": item["original_first_h1"],
            })
    if len(tasks) < 90 or len(tasks) > 150:
        raise ValueError("Unexpected fixed challenge matrix size")
    return tasks


def assess_subject(
    topic: str,
    intent: str,
    candidates: list[str],
    headings: dict[str, str | None],
    parsed_statuses: dict[str, str | None],
    original_text: dict[str, str],
) -> dict[str, Any]:
    """Never receive the expected source, label, or challenge family.

    A source whose status is correctly cited but whose title is not the
    exact requested subject must not be described as the answer.
    """
    normalized = normalize_subject(topic)
    matches = [
        p for p in candidates
        if headings[p] is not None and normalize_subject(topic_from_heading(headings[p])) == normalized
    ]
    if intent == OPERATIVE_INTENT:
        state = "UNSUPPORTED_OPERATIVE_GOVERNANCE"
        selected = None
        evidence = None
        status_class = None
    elif intent != STATUS_INTENT:
        raise ValueError("Unrecognized typed request intent")
    elif len(matches) > 1:
        state = "AMBIGUOUS_SOURCE_IDENTITY"
        selected = None
        evidence = None
        status_class = None
    elif not matches:
        state = "IDENTITY_NOT_VERIFIED"
        selected = None
        evidence = None
        status_class = None
    else:
        selected = matches[0]
        header = parsed_statuses[selected]
        status_class = classified_status(header) if header else None
        if status_class is None:
            state = "NOT_FOUND_IN_COVERED_SCOPE"
            evidence = None
        else:
            state = "ASSERTED_SOURCE_STATUS_ONLY"
            evidence = status_witness(original_text[selected], header)
            evidence = {
                **evidence,
                "source_path": selected,
                "source_body_sha256": sha256(original_text[selected].encode("utf-8")).hexdigest(),
                "recorded_status": header,
                "not_operative_governing_authority": True,
            }
    return {
        "state": state,
        "matched_candidates": matches,
        "bound_source": selected,
        "asserted_status_class": status_class,
        "evidence": evidence,
        "identity_rule": "UNIQUE_COMPLETE_NORMALIZED_FIRST_H1_TOPIC_MATCH_WITHIN_TOP_TEN",
        "operative_authority_asserted": False,
        "candidate_documents_not_authority": list(candidates),
    }


def run() -> dict[str, Any]:
    original_bytes = ORIGINAL_RESULT.read_bytes()
    if sha256(original_bytes).hexdigest() != ORIGINAL_RESULT_SHA256 or len(original_bytes) != 224009:
        raise ValueError("Frozen Checkpoint 913 original T2 result identity drift")
    prior = json.loads(original_bytes)
    if prior["source_commit"] != PIN or len(prior["sources"]) != 120:
        raise ValueError("Source frame drift")
    corpus_bytes = source_archive()
    roster = prior["sources"]
    if len({item["path"] for item in roster}) != len(roster):
        raise ValueError("Duplicate source paths in original roster")
    for source in roster:
        if sha256(corpus_bytes[source["path"]]).hexdigest() != source["body_sha256"]:
            raise ValueError("Original Git archive source bytes changed")
    paths = sorted(source["path"] for source in roster)
    texts = {p: corpus_bytes[p].decode("utf-8") for p in paths}
    headings = {}
    for p in paths:
        try:
            headings[p] = first_h1(texts[p])
        except ValueError:
            headings[p] = None  # Unheaded distractor is not a verified subject identity.
    statuses = {row["path"]: row["native_header_status"] for row in roster}

    # This list of tasks is fully generated BEFORE any index/ranking call.
    challenges = challenge_matrix(prior["test_cases_and_results"])
    if len(challenges) != len({r["challenge_id"] for r in challenges}):
        raise ValueError("Duplicate challenge identifiers")

    connection = sqlite3.connect(":memory:")
    results = []
    try:
        connection.execute("CREATE VIRTUAL TABLE docs_fts USING fts5(path UNINDEXED, body, tokenize='unicode61')")
        for path in paths:
            connection.execute("INSERT INTO docs_fts(path,body) VALUES (?,?)", (path, texts[path]))
        connection.commit()
        connection.execute("PRAGMA query_only=ON")
        prior_cases = {x["id"]: x for x in prior["test_cases_and_results"]}
        for ch in challenges:
            ranked = rank_query(connection, ch["topic"])
            previous = prior_cases[ch["source_v01_case_id"]]
            if ch["family"] in ("BASE_RECORDED_STATUS", "OPERATIVE_GOVERNANCE"):
                if ranked != previous["candidate_ranking"]:
                    raise ValueError("Old baseline lexical rankings drifted")
            assessment = assess_subject(ch["topic"], ch["intent"], ranked, headings, statuses, texts)
            claim_source = assessment["bound_source"]
            # Only evaluation code, never the resolver, uses these expected
            # labels from the exposed original source-derived tasks.
            expected_source = ch["expected_source_for_evaluation_only"]
            expected_class = ch["expected_status_class_for_evaluation_only"]
            results.append({
                **ch,
                "lexical_top_ten": ranked,
                "lexical_top_one": ranked[0] if ranked else None,
                "target_rank_for_evaluation_only": ranked.index(expected_source) + 1 if expected_source in ranked else None,
                "subject_binding_and_answer": assessment,
                "correct_target_source_status_assertion_for_evaluation_only": (
                    assessment["state"] == "ASSERTED_SOURCE_STATUS_ONLY"
                    and claim_source == expected_source
                    and assessment["asserted_status_class"] == expected_class
                ),
                "wrong_target_source_status_assertion_for_evaluation_only": (
                    assessment["state"] == "ASSERTED_SOURCE_STATUS_ONLY"
                    and claim_source != expected_source
                ),
            })
    finally:
        connection.close()

    base = [r for r in results if r["family"] == "BASE_RECORDED_STATUS"]
    counts = Counter(r["family"] for r in results)
    by_family_state = {
        family: dict(sorted(Counter(
            r["subject_binding_and_answer"]["state"] for r in results if r["family"] == family
        ).items()))
        for family in REQUEST_KINDS
    }
    old_wrong_source = sum(
        x["governed_header_assertion"]["state"] == "ASSERTED_SOURCE_STATUS_ONLY"
        and x["top_candidate"] != x["expected_source"]
        for x in prior["test_cases_and_results"]
    )
    metrics = {
        "requests": len(results),
        "request_families": dict(sorted(counts.items())),
        "states_by_family": by_family_state,
        "old_base_correct_rank1_source_and_status": prior["metrics"]["source_header_exact_status_correct_at_rank_1"],
        "old_base_wrong_source_assertions": old_wrong_source,
        "v02_base_exact_source_and_status_answers": sum(x["correct_target_source_status_assertion_for_evaluation_only"] for x in base),
        "v02_base_wrong_source_assertions": sum(x["wrong_target_source_status_assertion_for_evaluation_only"] for x in base),
        "v02_all_challenges_wrong_source_assertions": sum(x["wrong_target_source_status_assertion_for_evaluation_only"] for x in results),
        "challenge_nonbase_status_assertions": sum(
            x["subject_binding_and_answer"]["state"] == "ASSERTED_SOURCE_STATUS_ONLY"
            for x in results if x["family"] != "BASE_RECORDED_STATUS"
        ),
        "retained_nonassertive_candidates_every_request": all(
            x["subject_binding_and_answer"]["candidate_documents_not_authority"] == x["lexical_top_ten"]
            for x in results
        ),
        "operative_governance_assertions": sum(
            x["subject_binding_and_answer"]["operative_authority_asserted"] for x in results
        ),
        "independent_currentness_gold": False,
        "genuine_language_paraphrase_robustness_evaluated": False,
    }
    return {
        "identifier": IDENTIFIER,
        "contract": CONTRACT,
        "original_t2_result_sha256": ORIGINAL_RESULT_SHA256,
        "original_source_git_pin": PIN,
        "original_120_source_manifest_sha256": prior["source_cohort"]["sampled_source_sha256"],
        "baseline_exact_result_unchanged": True,
        "source_roster": roster,
        "challenges_and_outputs": results,
        "metrics": metrics,
        "scientific_limits": [
            "This is a fully exposed title-derived regression and synthetic contradiction/ambiguity stress, not independent natural user questions.",
            "Exact normalized full H1 matching is structurally advantaged on title-derived tasks and can incorrectly abstain for valid aliases, paraphrases or renamed sources.",
            "The resolver receives structured topic and intent supplied by the challenge generator; parsing arbitrary natural language has not been tested.",
            "Status header self-description is not authenticated current operative governance, signed owner acceptance, semantic lifecycle reconstruction or source-authority gold.",
            "A zero operative governing assertion is a deliberate output policy, not proof of zero real-world false-authority rate.",
            "All policies share the same lexical candidate ranking; this is a referent-binding answer-safety comparison, not B0-B4 architecture selection.",
            "The 120-source and older 65-source sets are regression fixtures after exposure and repeated testing.",
        ],
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", action="store_true")
    args = p.parse_args()
    result = run()
    raw = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as writer:
            writer.write(raw)
    print(json.dumps({
        "id": result["identifier"],
        "metrics": result["metrics"],
        "output_saved": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
