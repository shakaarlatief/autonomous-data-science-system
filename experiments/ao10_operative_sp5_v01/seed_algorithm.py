from __future__ import annotations

import hashlib
import json
from pathlib import Path

PROBE_ID = "OPERATIVE-SP5-V01"
AUTHORIZATION_COMMIT = "b3f06a414697b8ac99fd57fcae04159ab01eb35c"
UNITS = ["U1", "U2", "U3", "U4", "U5", "U6"]
ERRORS = ["E1_WRONG_OWNER", "E2_MISSING_GATE_CONDITION", "E3_BROKEN_PROHIBITION_SCOPE"]

SEED_MATERIAL = (
    PROBE_ID + "|" + AUTHORIZATION_COMMIT + "|" + "|".join(UNITS)
).encode("utf-8")
SEED_DIGEST = hashlib.sha256(SEED_MATERIAL).digest()


def _rank(tag: str, value: str) -> bytes:
    return hashlib.sha256(
        SEED_DIGEST + b"|" + tag.encode("utf-8") + b"|" + value.encode("utf-8")
    ).digest()


def deterministic_permutation(tag: str, values: list[str]) -> list[str]:
    return sorted(values, key=lambda value: _rank(tag, value))


def choose_seed_placement(compatibility: dict[str, list[str]]) -> dict[str, str]:
    unit_order = deterministic_permutation("SEED-UNIT-ORDER", UNITS)
    selected: dict[str, str] = {}
    used: set[str] = set()
    cursor = 0

    for error in ERRORS:
        for offset in range(len(unit_order)):
            idx = (cursor + offset) % len(unit_order)
            unit = unit_order[idx]
            if unit not in used and unit in compatibility[error]:
                selected[error] = unit
                used.add(unit)
                cursor = (idx + 1) % len(unit_order)
                break
        else:
            raise RuntimeError(f"No compatible unused unit for {error}")

    return selected


def build_packet(root: Path) -> tuple[dict, dict]:
    clean_doc = json.loads((root / "clean_units.json").read_text(encoding="utf-8"))
    template_doc = json.loads((root / "corruption_templates.json").read_text(encoding="utf-8"))

    clean = {row["unit_id"]: row for row in clean_doc["units"]}
    placement = choose_seed_placement(template_doc["compatibility"])
    error_by_unit = {unit: error for error, unit in placement.items()}

    packet_order = deterministic_permutation("OWNER-PACKET-ORDER", UNITS)
    packet_items = []
    key_items = []

    for index, unit in enumerate(packet_order, 1):
        review_item_id = f"R{index:02d}"
        row = clean[unit]
        error = error_by_unit.get(unit)

        if error is None:
            shown = row["clean_view"]
            criterion = None
            seeded = False
        else:
            template = template_doc["templates"][error][unit]
            shown = template["seeded_view"]
            criterion = template["detection_criterion"]
            seeded = True

        packet_items.append({
            "review_item_id": review_item_id,
            "context": row["context"],
            "proposed_consequence_view": shown,
        })
        key_items.append({
            "review_item_id": review_item_id,
            "unit_id": unit,
            "origin": row["origin"],
            "seeded": seeded,
            "error_class": error,
            "clean_view": row["clean_view"],
            "shown_view": shown,
            "detection_criterion": criterion,
        })

    packet = {
        "schema_version": 1,
        "probe_id": PROBE_ID,
        "owner_instruction": (
            "Exactly three of the six cards contain deliberate material semantic errors. "
            "For each card answer ACCEPT, AMEND, REJECT, or CANNOT_JUDGE. "
            "If you choose AMEND or REJECT, state what is semantically wrong or missing."
        ),
        "non_consequence_notice": (
            "This is experimental review material only. "
            "Your responses do not change real project authority."
        ),
        "items": packet_items,
    }

    key = {
        "schema_version": 1,
        "probe_id": PROBE_ID,
        "authorization_commit": AUTHORIZATION_COMMIT,
        "seed_material_sha256": hashlib.sha256(SEED_MATERIAL).hexdigest(),
        "unit_permutation": deterministic_permutation("SEED-UNIT-ORDER", UNITS),
        "placement": placement,
        "packet_order": packet_order,
        "items": key_items,
    }
    return packet, key


def main() -> None:
    root = Path(__file__).resolve().parent
    packet, key = build_packet(root)
    (root / "owner_review_packet.json").write_text(
        json.dumps(packet, indent=2) + "\n", encoding="utf-8"
    )
    (root / "evaluator_key.json").write_text(
        json.dumps(key, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
