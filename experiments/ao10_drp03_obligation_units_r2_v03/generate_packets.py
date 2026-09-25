from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from splitter import segment_markdown, sentence_split


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROTOCOL_ID = "AO10-DRP03-R2-V03"

EVENT_MANIFEST = ROOT / "docs/research/project_knowledge_activation_orchestration/ao10/DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V03.json"
LEGACY_MANIFEST = HERE / "legacy_corpus_manifest.json"
STATE_FIXTURES = HERE / "public_fixtures/state_fixtures.json"
STATE_REAL_MANIFEST = HERE / "public_fixtures/state_real_fact_manifest.json"
SPLITTER_VECTORS = HERE / "public_fixtures/sentence_splitter_test_vectors.json"
CONTROL_PRINCIPLE = HERE / "public_fixtures/control_principle.md"
CONTROL_DISPOSITION = HERE / "public_fixtures/control_disposition.md"
PACKETS = HERE / "packets"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def stable_id(prefix: str, payload: str, length: int = 16) -> str:
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:length]
    return f"{prefix}-{digest}"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def git_show(revision: str, path: str) -> str:
    proc = subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout.decode("utf-8")


def run_splitter_vectors() -> None:
    vectors = load_json(SPLITTER_VECTORS)
    failures = []
    for case in vectors["cases"]:
        actual = sentence_split(case["input"])
        if actual != case["expected"]:
            failures.append(
                {
                    "id": case["id"],
                    "expected": case["expected"],
                    "actual": actual,
                }
            )
    if failures:
        raise RuntimeError(f"sentence splitter vector failures: {failures}")


def segment_document(
    *,
    packet_owner_id: str,
    source_id: str,
    text: str,
) -> list[dict[str, Any]]:
    segments = segment_markdown(text)
    items: list[dict[str, Any]] = []
    for ordinal, segment in enumerate(segments, start=1):
        text_digest = sha256_bytes(segment.text.encode("utf-8"))
        item_id = stable_id(
            "ITM",
            f"{packet_owner_id}|{source_id}|{ordinal}|{text_digest}",
        )
        items.append(
            {
                "item_id": item_id,
                "ordinal": ordinal,
                "kind": segment.kind,
                "heading_context": segment.heading,
                "table_header_context": segment.context,
                "text": segment.text,
                "text_sha256": text_digest,
            }
        )
    return items


def birth_packets() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    manifest = load_json(EVENT_MANIFEST)
    development: list[dict[str, Any]] = []
    heldout: list[dict[str, Any]] = []
    provenance: list[dict[str, Any]] = []

    for event in manifest["events"]:
        packet_event_id = stable_id("EVP", f"birth|{event['event_id']}", 12)
        packet_sources = []
        provenance_sources = []
        for source_index, source_path in enumerate(event["proposal_sources"], start=1):
            source_id = stable_id(
                "SRC",
                f"{event['event_id']}|{source_index}|{source_path}",
                12,
            )
            text = git_show(event["pre_acceptance_snapshot"], source_path)
            items = segment_document(
                packet_owner_id=packet_event_id,
                source_id=source_id,
                text=text,
            )
            packet_sources.append(
                {
                    "source_id": source_id,
                    "items": items,
                }
            )
            provenance_sources.append(
                {
                    "source_id": source_id,
                    "source_path": source_path,
                    "revision": event["pre_acceptance_snapshot"],
                    "blob_sha256": sha256_bytes(text.encode("utf-8")),
                    "item_count": len(items),
                }
            )

        packet_event = {
            "packet_event_id": packet_event_id,
            "decision_token": event["decision_input"],
            "sources": packet_sources,
        }
        target = development if event["split"] == "DEVELOPMENT" else heldout
        target.append(packet_event)
        provenance.append(
            {
                "packet_event_id": packet_event_id,
                "historical_event_id": event["event_id"],
                "acceptance_commit": event["acceptance_commit"],
                "pre_acceptance_snapshot": event["pre_acceptance_snapshot"],
                "proposal_source_cluster_id": event["proposal_source_cluster_id"],
                "birth_scoring_eligibility": event["birth_scoring_eligibility"],
                "split": event["split"],
                "decision_input_provenance": event["decision_input_provenance"],
                "sources": provenance_sources,
            }
        )

    controls = [
        ("NC-PRINCIPLE-01", CONTROL_PRINCIPLE, "ACCEPT"),
        ("NC-DISPOSITION-01", CONTROL_DISPOSITION, "ACCEPT"),
    ]
    for control_id, path, decision_token in controls:
        packet_event_id = stable_id("EVP", f"birth-control|{control_id}", 12)
        source_id = stable_id("SRC", f"birth-control|{control_id}|source", 12)
        text = path.read_text(encoding="utf-8")
        items = segment_document(
            packet_owner_id=packet_event_id,
            source_id=source_id,
            text=text,
        )
        heldout.append(
            {
                "packet_event_id": packet_event_id,
                "decision_token": decision_token,
                "sources": [{"source_id": source_id, "items": items}],
            }
        )
        provenance.append(
            {
                "packet_event_id": packet_event_id,
                "controlled_negative_id": control_id,
                "split": "HELD_OUT",
                "birth_scoring_eligibility": "NEGATIVE_BIRTH_CONTROL_ONLY",
                "sources": [
                    {
                        "source_id": source_id,
                        "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                        "revision": "PUBLIC_FREEZE_WORKTREE",
                        "blob_sha256": sha256_bytes(text.encode("utf-8")),
                        "item_count": len(items),
                    }
                ],
            }
        )

    development.sort(
        key=lambda x: hashlib.sha256(
            f"birth-order|{x['packet_event_id']}".encode("utf-8")
        ).hexdigest()
    )
    heldout.sort(
        key=lambda x: hashlib.sha256(
            f"birth-order|{x['packet_event_id']}".encode("utf-8")
        ).hexdigest()
    )

    common = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "component": "BIRTH",
        "reviewer_instructions": "REVIEWER_INSTRUCTIONS.md",
        "contains_hidden_labels": False,
    }
    return (
        {**common, "split": "DEVELOPMENT", "events": development},
        {**common, "split": "HELD_OUT", "events": heldout},
        {
            "schema_version": 1,
            "protocol_id": PROTOCOL_ID,
            "component": "BIRTH",
            "records": provenance,
        },
    )


def legacy_packet() -> tuple[dict[str, Any], dict[str, Any]]:
    manifest = load_json(LEGACY_MANIFEST)
    sources = []
    provenance = []
    for source in manifest["sources"]:
        packet_source_id = stable_id("LSP", f"legacy|{source['id']}|{source['path']}", 12)
        text = git_show(manifest["source_base"], source["path"])
        items = segment_document(
            packet_owner_id=packet_source_id,
            source_id=packet_source_id,
            text=text,
        )
        sources.append(
            {
                "packet_source_id": packet_source_id,
                "items": items,
            }
        )
        provenance.append(
            {
                "packet_source_id": packet_source_id,
                "manifest_id": source["id"],
                "path": source["path"],
                "revision": manifest["source_base"],
                "manifest_role": source["role"],
                "blob_sha256": sha256_bytes(text.encode("utf-8")),
                "item_count": len(items),
            }
        )

    sources.sort(
        key=lambda x: hashlib.sha256(
            f"legacy-order|{x['packet_source_id']}".encode("utf-8")
        ).hexdigest()
    )
    packet = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "component": "LEGACY",
        "authority": "CANDIDATE_ONLY",
        "reviewer_instructions": "REVIEWER_INSTRUCTIONS.md",
        "contains_hidden_labels": False,
        "sources": sources,
    }
    prov = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "component": "LEGACY",
        "records": provenance,
    }
    return packet, prov


def extract_real_state_cases() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    manifest = load_json(STATE_REAL_MANIFEST)
    packet_cases = []
    provenance = []

    for case in manifest["cases"]:
        text = git_show(case["revision"], case["path"])
        evidence: list[dict[str, Any]] = []
        if case.get("include_whole_file"):
            evidence.append(
                {
                    "fact_id": stable_id("RF", f"{case['case_id']}|whole", 12),
                    "candidate_fact_type": case["candidate_fact_type"],
                    "source_excerpt": text,
                }
            )
        else:
            lines = text.splitlines()
            for pattern in case.get("match_substrings", []):
                matches = [
                    (index + 1, line)
                    for index, line in enumerate(lines)
                    if pattern in line
                ]
                if not matches:
                    raise RuntimeError(
                        f"state real case {case['case_id']} missing pattern: {pattern}"
                    )
                for line_number, line in matches:
                    evidence.append(
                        {
                            "fact_id": stable_id(
                                "RF",
                                f"{case['case_id']}|{line_number}|{line}",
                                12,
                            ),
                            "candidate_fact_type": case["candidate_fact_type"],
                            "source_excerpt": line.strip(),
                        }
                    )

        packet_cases.append(
            {
                "fixture_id": case["case_id"],
                "obligation_id": case["obligation_id"],
                "facts": evidence,
                "source_class": "REAL_REPOSITORY_FACT_CANDIDATE",
            }
        )
        provenance.append(
            {
                "fixture_id": case["case_id"],
                "path": case["path"],
                "revision": case["revision"],
                "candidate_fact_type": case["candidate_fact_type"],
                "source_blob_sha256": sha256_bytes(text.encode("utf-8")),
            }
        )
    return packet_cases, provenance


def state_packet() -> tuple[dict[str, Any], dict[str, Any]]:
    synthetic = load_json(STATE_FIXTURES)
    real_cases, real_provenance = extract_real_state_cases()
    packet = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "component": "STATE",
        "reviewer_instructions": "REVIEWER_INSTRUCTIONS.md",
        "state_rules": "public_fixtures/state_rules.json",
        "contains_expected_outputs": False,
        "fixtures": synthetic["fixtures"] + real_cases,
    }
    provenance = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "component": "STATE",
        "real_repository_cases": real_provenance,
    }
    return packet, provenance


def assert_no_forbidden_reviewer_fields(value: Any) -> None:
    forbidden = {
        "acceptance_commit",
        "pre_acceptance_snapshot",
        "source_path",
        "path",
        "manifest_role",
        "controlled_negative_id",
        "birth_scoring_eligibility",
        "expected_state",
        "expected_output",
    }

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            overlap = forbidden.intersection(node.keys())
            if overlap:
                raise RuntimeError(f"reviewer packet exposes forbidden fields: {sorted(overlap)}")
            for child in node.values():
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(value)


def packet_summary(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    parsed = json.loads(data.decode("utf-8"))
    result = {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "sha256": sha256_bytes(data),
        "bytes": len(data),
    }
    if "events" in parsed:
        result["events"] = len(parsed["events"])
        result["items"] = sum(
            len(source["items"])
            for event in parsed["events"]
            for source in event["sources"]
        )
    if "sources" in parsed:
        result["sources"] = len(parsed["sources"])
        result["items"] = sum(len(source["items"]) for source in parsed["sources"])
    if "fixtures" in parsed:
        result["fixtures"] = len(parsed["fixtures"])
    return result



def _attention_count(primary_count: int) -> int:
    if primary_count <= 0:
        return 0
    proposed = max(5, (primary_count * 3 + 99) // 100)
    return min(primary_count, 20, proposed)


def _presentation(
    *,
    batch_id: str,
    semantic_item: dict[str, Any],
    owner_id: str,
    source_id: str,
    duplicate: bool,
) -> tuple[dict[str, Any], dict[str, Any]]:
    semantic_item_id = semantic_item["item_id"]
    role = "duplicate" if duplicate else "primary"
    presentation_id = stable_id(
        "PRS",
        f"{batch_id}|{role}|{semantic_item_id}",
        16,
    )
    public = {
        "presentation_id": presentation_id,
        "owner_id": owner_id,
        "source_id": source_id,
        "kind": semantic_item["kind"],
        "heading_context": semantic_item["heading_context"],
        "table_header_context": semantic_item["table_header_context"],
        "text": semantic_item["text"],
        "text_sha256": semantic_item["text_sha256"],
    }
    provenance = {
        "presentation_id": presentation_id,
        "semantic_item_id": semantic_item_id,
        "attention_duplicate": duplicate,
    }
    return public, provenance


def _chunk_items(items: list[dict[str, Any]], size: int = 380) -> list[list[dict[str, Any]]]:
    return [items[index:index + size] for index in range(0, len(items), size)]


def birth_classification_sessions(
    packet: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    batches: list[dict[str, Any]] = []
    provenance_records: list[dict[str, Any]] = []

    for event in packet["events"]:
        flattened: list[tuple[str, dict[str, Any]]] = []
        for source in event["sources"]:
            for item in source["items"]:
                flattened.append((source["source_id"], item))

        for part_index, chunk in enumerate(_chunk_items(flattened), start=1):
            batch_id = stable_id(
                "BAT",
                f"{packet['split']}|{event['packet_event_id']}|{part_index}",
                12,
            )
            primary_presentations: list[dict[str, Any]] = []
            primary_provenance: list[dict[str, Any]] = []
            for source_id, item in chunk:
                public, prov = _presentation(
                    batch_id=batch_id,
                    semantic_item=item,
                    owner_id=event["packet_event_id"],
                    source_id=source_id,
                    duplicate=False,
                )
                primary_presentations.append(public)
                primary_provenance.append(prov)

            ranked = sorted(
                zip(chunk, primary_provenance),
                key=lambda pair: hashlib.sha256(
                    f"attention|{batch_id}|{pair[1]['semantic_item_id']}".encode("utf-8")
                ).hexdigest(),
            )
            duplicate_count = _attention_count(len(chunk))
            duplicates: list[dict[str, Any]] = []
            duplicate_provenance: list[dict[str, Any]] = []
            for (source_id, item), _ in ranked[:duplicate_count]:
                public, prov = _presentation(
                    batch_id=batch_id,
                    semantic_item=item,
                    owner_id=event["packet_event_id"],
                    source_id=source_id,
                    duplicate=True,
                )
                duplicates.append(public)
                duplicate_provenance.append(prov)

            presentations = primary_presentations + duplicates
            presentations.sort(
                key=lambda item: hashlib.sha256(
                    f"presentation-order|{batch_id}|{item['presentation_id']}".encode("utf-8")
                ).hexdigest()
            )
            if len(presentations) > 400:
                raise RuntimeError(f"batch {batch_id} exceeds 400 presentations")

            batches.append(
                {
                    "batch_id": batch_id,
                    "packet_event_id": event["packet_event_id"],
                    "decision_token": event["decision_token"],
                    "part_index": part_index,
                    "presentations": presentations,
                }
            )
            provenance_records.append(
                {
                    "batch_id": batch_id,
                    "packet_event_id": event["packet_event_id"],
                    "part_index": part_index,
                    "primary_count": len(primary_presentations),
                    "attention_duplicate_count": len(duplicates),
                    "presentation_map": primary_provenance + duplicate_provenance,
                }
            )

    return (
        {
            "schema_version": 1,
            "protocol_id": PROTOCOL_ID,
            "component": "BIRTH_CLASSIFICATION_SESSIONS",
            "split": packet["split"],
            "delivery_rule": "Freeze each batch annotation before exposing the next batch. Expose the unique grouping catalog only after all classification batches are frozen.",
            "max_presentations_per_batch": 400,
            "batches": batches,
        },
        {
            "schema_version": 1,
            "protocol_id": PROTOCOL_ID,
            "component": "BIRTH_CLASSIFICATION_ATTENTION_PROVENANCE",
            "split": packet["split"],
            "records": provenance_records,
        },
    )


def legacy_classification_sessions(
    packet: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    batches: list[dict[str, Any]] = []
    provenance_records: list[dict[str, Any]] = []

    for source in packet["sources"]:
        for part_index, chunk in enumerate(_chunk_items(source["items"]), start=1):
            batch_id = stable_id(
                "LBAT",
                f"{source['packet_source_id']}|{part_index}",
                12,
            )
            primary: list[dict[str, Any]] = []
            primary_prov: list[dict[str, Any]] = []
            for item in chunk:
                public, prov = _presentation(
                    batch_id=batch_id,
                    semantic_item=item,
                    owner_id=source["packet_source_id"],
                    source_id=source["packet_source_id"],
                    duplicate=False,
                )
                primary.append(public)
                primary_prov.append(prov)

            ranked = sorted(
                zip(chunk, primary_prov),
                key=lambda pair: hashlib.sha256(
                    f"attention|{batch_id}|{pair[1]['semantic_item_id']}".encode("utf-8")
                ).hexdigest(),
            )
            duplicate_count = _attention_count(len(chunk))
            duplicates: list[dict[str, Any]] = []
            duplicate_prov: list[dict[str, Any]] = []
            for item, _ in ranked[:duplicate_count]:
                public, prov = _presentation(
                    batch_id=batch_id,
                    semantic_item=item,
                    owner_id=source["packet_source_id"],
                    source_id=source["packet_source_id"],
                    duplicate=True,
                )
                duplicates.append(public)
                duplicate_prov.append(prov)

            presentations = primary + duplicates
            presentations.sort(
                key=lambda item: hashlib.sha256(
                    f"presentation-order|{batch_id}|{item['presentation_id']}".encode("utf-8")
                ).hexdigest()
            )
            if len(presentations) > 400:
                raise RuntimeError(f"batch {batch_id} exceeds 400 presentations")

            batches.append(
                {
                    "batch_id": batch_id,
                    "packet_source_id": source["packet_source_id"],
                    "part_index": part_index,
                    "presentations": presentations,
                }
            )
            provenance_records.append(
                {
                    "batch_id": batch_id,
                    "packet_source_id": source["packet_source_id"],
                    "part_index": part_index,
                    "primary_count": len(primary),
                    "attention_duplicate_count": len(duplicates),
                    "presentation_map": primary_prov + duplicate_prov,
                }
            )

    return (
        {
            "schema_version": 1,
            "protocol_id": PROTOCOL_ID,
            "component": "LEGACY_CLASSIFICATION_SESSIONS",
            "delivery_rule": "Freeze each batch annotation before exposing the next batch. Expose the unique grouping catalog only after all classification batches are frozen.",
            "max_presentations_per_batch": 400,
            "batches": batches,
        },
        {
            "schema_version": 1,
            "protocol_id": PROTOCOL_ID,
            "component": "LEGACY_CLASSIFICATION_ATTENTION_PROVENANCE",
            "records": provenance_records,
        },
    )


def main() -> None:
    run_splitter_vectors()
    PACKETS.mkdir(parents=True, exist_ok=True)

    birth_dev, birth_held, birth_prov = birth_packets()
    legacy, legacy_prov = legacy_packet()
    state, state_prov = state_packet()
    birth_dev_sessions, birth_dev_attention = birth_classification_sessions(birth_dev)
    birth_held_sessions, birth_held_attention = birth_classification_sessions(birth_held)
    legacy_sessions, legacy_attention = legacy_classification_sessions(legacy)

    for reviewer_packet in (
        birth_dev,
        birth_held,
        legacy,
        state,
        birth_dev_sessions,
        birth_held_sessions,
        legacy_sessions,
    ):
        assert_no_forbidden_reviewer_fields(reviewer_packet)

    outputs = {
        "birth_development.json": birth_dev,
        "birth_heldout.json": birth_held,
        "legacy.json": legacy,
        "state.json": state,
        "birth_development_classification_sessions.json": birth_dev_sessions,
        "birth_heldout_classification_sessions.json": birth_held_sessions,
        "legacy_classification_sessions.json": legacy_sessions,
        "birth_development_attention_provenance.json": birth_dev_attention,
        "birth_heldout_attention_provenance.json": birth_held_attention,
        "legacy_attention_provenance.json": legacy_attention,
        "birth_provenance.json": birth_prov,
        "legacy_provenance.json": legacy_prov,
        "state_provenance.json": state_prov,
    }
    for name, value in outputs.items():
        write_json(PACKETS / name, value)

    reviewer_paths = [
        PACKETS / "birth_development_classification_sessions.json",
        PACKETS / "birth_heldout_classification_sessions.json",
        PACKETS / "birth_development.json",
        PACKETS / "birth_heldout.json",
        PACKETS / "legacy_classification_sessions.json",
        PACKETS / "legacy.json",
        PACKETS / "state.json",
    ]
    manifest = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "reviewer_packets": [packet_summary(path) for path in reviewer_paths],
        "provenance_packets": [
            packet_summary(PACKETS / "birth_provenance.json"),
            packet_summary(PACKETS / "legacy_provenance.json"),
            packet_summary(PACKETS / "state_provenance.json"),
            packet_summary(PACKETS / "birth_development_attention_provenance.json"),
            packet_summary(PACKETS / "birth_heldout_attention_provenance.json"),
            packet_summary(PACKETS / "legacy_attention_provenance.json"),
        ],
        "splitter_vectors_pass": True,
        "hidden_key_created": False,
        "scoring_harness_created": False,
    }
    write_json(PACKETS / "packet_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
