from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PACKETS = HERE / "packets"
EVENT_MANIFEST = ROOT / "docs/research/project_knowledge_activation_orchestration/ao10/DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V03.json"


def stable_id(prefix: str, payload: str, length: int = 12) -> str:
    return prefix + "-" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:length]


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def acceptance_diff(commit: str) -> dict[str, Any]:
    parent = subprocess.check_output(["git", "rev-parse", commit + "^"], cwd=ROOT, text=True).strip()
    changed = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-status", "-r", commit],
        cwd=ROOT,
        text=True,
    ).splitlines()

    allowed_paths: list[str] = []
    for row in changed:
        parts = row.split("\t")
        if len(parts) < 2:
            continue
        path = parts[-1]
        if path.startswith("docs/research/"):
            allowed_paths.append(path)
            continue
        if (
            path.startswith("docs/model_collaboration/threads/")
            and "/messages/" in path
            and path.endswith((".md", ".json"))
        ):
            allowed_paths.append(path)

    records = []
    for path in sorted(set(allowed_paths)):
        proc = subprocess.run(
            ["git", "diff", "--no-ext-diff", "--unified=3", parent, commit, "--", path],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        diff_text = proc.stdout.decode("utf-8")
        records.append(
            {
                "path": path,
                "diff_sha256": hashlib.sha256(diff_text.encode("utf-8")).hexdigest(),
                "diff_text": diff_text,
            }
        )
    return {"parent": parent, "commit": commit, "records": records}


def main() -> None:
    manifest = load(EVENT_MANIFEST)
    provenance = load(PACKETS / "birth_provenance.json")
    by_packet = {record["packet_event_id"]: record for record in provenance["records"]}

    event_by_historical = {event["event_id"]: event for event in manifest["events"]}
    development = load(PACKETS / "birth_development.json")
    heldout = load(PACKETS / "birth_heldout.json")

    outputs = {}
    for split_name, packet in (("development", development), ("heldout", heldout)):
        events = []
        for event_packet in packet["events"]:
            prov = by_packet[event_packet["packet_event_id"]]
            record = {
                "packet_event_id": event_packet["packet_event_id"],
                "decision_token": event_packet["decision_token"],
                "proposal_catalog": event_packet["sources"],
            }
            if "historical_event_id" in prov:
                event = event_by_historical[prov["historical_event_id"]]
                record.update(
                    {
                        "historical_event_id": event["event_id"],
                        "event_kind": event["event_kind"],
                        "acceptance_commit": event["acceptance_commit"],
                        "pre_acceptance_snapshot": event["pre_acceptance_snapshot"],
                        "proposal_source_cluster_id": event["proposal_source_cluster_id"],
                        "birth_scoring_eligibility": event["birth_scoring_eligibility"],
                        "acceptance_evidence": acceptance_diff(event["acceptance_commit"]),
                        "key_rules": {
                            "restated": "Neutral when bounded evidence establishes the item was already governing immediately before the event and was not materially changed.",
                            "decision_time_delta": "Neutral when accepted meaning is determinable only from acceptance-time evidence unavailable in the reviewer proposal packet.",
                        },
                    }
                )
            else:
                record.update(
                    {
                        "protocol_defined_control": True,
                        "construct_gate_included": False,
                        "control_note": "Protocol-defined over-declaration control. It is scored on blind reviewer behavior but excluded from independent key-author construct-agreement denominators.",
                    }
                )
            events.append(record)

        outputs[split_name] = {
            "schema_version": 1,
            "protocol_id": "AO10-DRP03-R2-V03",
            "component": "BIRTH_KEY_AUTHOR_PACKET",
            "split": split_name.upper(),
            "instructions": "KEY_AUTHOR_INSTRUCTIONS.md",
            "events": events,
        }

    for split_name, value in outputs.items():
        write(PACKETS / ("key_author_birth_" + split_name + ".json"), value)

    files = []
    for name in ("key_author_birth_development.json", "key_author_birth_heldout.json"):
        path = PACKETS / name
        data = path.read_bytes()
        parsed = json.loads(data.decode("utf-8"))
        files.append(
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "events": len(parsed["events"]),
            }
        )
    write(
        PACKETS / "key_author_packet_manifest.json",
        {
            "schema_version": 1,
            "protocol_id": "AO10-DRP03-R2-V03",
            "birth_key_author_packets": files,
            "legacy_key_author_inputs": [
                "packets/legacy.json",
                "packets/legacy_provenance.json",
                "legacy_corpus_manifest.json",
            ],
            "state_key_author_inputs": [
                "packets/state.json",
                "packets/state_provenance.json",
                "public_fixtures/state_rules.json",
            ],
            "other_key_output_must_remain_unseen": True,
            "hidden_semantic_key_created": False,
        },
    )
    print(json.dumps(load(PACKETS / "key_author_packet_manifest.json"), indent=2))


if __name__ == "__main__":
    main()
