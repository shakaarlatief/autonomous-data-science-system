from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANIFEST = HERE / "public_freeze_manifest.json"
COMMITMENT = HERE / "public_freeze_commitment.json"

EXCLUDE = {
    "public_freeze_manifest.json",
    "public_freeze_commitment.json",
}

EXTERNAL_BINDINGS = [
    "docs/research/330_mc0029_message009_reconciliation_v07_and_drp03_r2_protocol_v03_freeze_candidate.md",
    "docs/research/331_owner_acceptance_m1_governed_deferral_and_r2_public_freeze_unblock.md",
    "docs/research/project_knowledge_activation_orchestration/ao10/DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V03.json",
    "docs/research/project_knowledge_activation_orchestration/ao10/M1_OWNER_REVIEW_EFFICACY_DEFERRAL_V01.json",
]


def digest(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


def main() -> None:
    assets = []
    for path in sorted(HERE.rglob("*")):
        if not path.is_file():
            continue
        if path.name in EXCLUDE:
            continue
        if "__pycache__" in path.parts:
            continue
        assets.append(digest(path))

    external = [digest(ROOT / relative) for relative in EXTERNAL_BINDINGS]

    manifest = {
        "schema_version": 1,
        "protocol_id": "AO10-DRP03-R2-V03",
        "freeze_kind": "PUBLIC_PROTOCOL_ASSET_FREEZE",
        "canonical_serialization": "UTF-8 JSON, indent=2, ensure_ascii=true, LF newline",
        "assets": assets,
        "external_bindings": external,
        "hidden_key_created": False,
        "hidden_labels_created": False,
        "scoring_harness_created": False,
    }
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    manifest_bytes = MANIFEST.read_bytes()
    manifest_sha = hashlib.sha256(manifest_bytes).hexdigest()
    commitment = {
        "schema_version": 1,
        "protocol_id": "AO10-DRP03-R2-V03",
        "hash_basis": "EXACT_PUBLIC_FREEZE_MANIFEST_BYTES",
        "manifest_path": MANIFEST.relative_to(ROOT).as_posix(),
        "manifest_sha256": manifest_sha,
        "manifest_bytes": len(manifest_bytes),
        "bootstrap_seed_source": manifest_sha,
        "hidden_key_created": False,
        "hidden_labels_created": False,
        "scoring_harness_created": False,
    }
    COMMITMENT.write_text(
        json.dumps(commitment, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(commitment, indent=2))


if __name__ == "__main__":
    main()
