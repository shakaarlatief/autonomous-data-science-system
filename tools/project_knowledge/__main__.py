"""L4: validation-only CLI for the first W0 substrate slice."""

import argparse
import json
from pathlib import Path

from .model import SnapshotMode, SubstrateError
from .services.validation import validate_repository
from .services.discovery import open_snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--snapshot-mode", required=True, choices=list(SnapshotMode))
    parser.add_argument("--ref", help="Required for COMMIT_SNAPSHOT; forbidden for WORKTREE_SNAPSHOT")
    parser.add_argument("--durable-evidence", action="store_true")
    args = parser.parse_args(argv)
    mode = SnapshotMode(args.snapshot_mode)
    if (mode == SnapshotMode.COMMIT_SNAPSHOT) != (args.ref is not None):
        parser.error("--ref is required exactly when --snapshot-mode is COMMIT_SNAPSHOT")
    try:
        snapshot = open_snapshot(args.root, mode, args.ref)
        result = validate_repository(snapshot, durable_evidence=args.durable_evidence)
    except (SubstrateError, OSError, ValueError) as error:
        print(json.dumps({"ok": False, "code": getattr(error, "code", "SNAPSHOT_INVALID"), "message": str(error)}, sort_keys=True))
        return 1
    print(json.dumps({
        "ok": result.ok, "snapshot_mode": mode, "snapshot_status": snapshot.status,
        "source_commit": snapshot.source_commit,
        "candidate_count": result.candidate_count, "governed_declaration_count": len(result.sources),
        "excluded_count": result.excluded_count,
        "excluded_but_declared_count": result.excluded_but_declared_count,
        "path_role_counts": dict(result.path_role_counts),
        "noncanonical_declaration_count": result.noncanonical_declaration_count,
        "undeclared_by_root": dict(result.undeclared_by_root),
        "diagnostics": [{
            "code": d.code, "severity": d.severity, "carrier_path": d.carrier_path,
            "message": d.message,
            **({"semantic_id": d.semantic_id.value} if d.semantic_id else {}),
            **({"related_sources": d.related_sources} if d.related_sources else {}),
            **({"remediation": d.remediation} if d.remediation else {}),
        } for d in result.diagnostics],
    }, indent=2, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
