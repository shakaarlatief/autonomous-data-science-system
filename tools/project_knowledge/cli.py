"""L4 deterministic command-line interface for project-knowledge W0 operations."""

import argparse
import json
from pathlib import Path

from .model import SnapshotMode, SubstrateError
from .services.cli_ops import (
    check_freshness_operation,
    rebuild_operation,
    refresh_operation,
    validate_operation,
)


def _parser():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    validate = commands.add_parser("validate", help="Validate governed project-knowledge sources.")
    validate.add_argument("--root", type=Path, default=Path.cwd())
    validate.add_argument("--snapshot-mode", required=True, choices=[mode.value for mode in SnapshotMode])
    validate.add_argument("--ref", help="Required for COMMIT_SNAPSHOT; forbidden for WORKTREE_SNAPSHOT.")
    validate.add_argument("--durable-evidence", action="store_true")

    rebuild = commands.add_parser("rebuild", help="Stage/diff a full deterministic derived-view rebuild.")
    rebuild.add_argument("--root", type=Path, default=Path.cwd())
    rebuild.add_argument("--ref", default="HEAD")
    rebuild.add_argument(
        "--write", action="store_true",
        help="Explicitly materialize generated non-authoritative outputs after successful staging.",
    )

    refresh = commands.add_parser("refresh", help="Stage/diff affected views since an earlier commit.")
    refresh.add_argument("--root", type=Path, default=Path.cwd())
    refresh.add_argument("--changed-since", required=True)
    refresh.add_argument("--ref", default="HEAD")
    refresh.add_argument(
        "--write", action="store_true",
        help="Explicitly materialize affected generated outputs after successful staging.",
    )

    freshness = commands.add_parser(
        "check-freshness", help="Compare materialized generated artifacts with a complete rebuild."
    )
    freshness.add_argument("--root", type=Path, default=Path.cwd())
    freshness.add_argument("--ref", default="HEAD")
    return parser


def _diagnostic_data(diagnostic):
    return {
        "code": diagnostic.code,
        "severity": diagnostic.severity.value,
        "carrier_path": diagnostic.carrier_path,
        "message": diagnostic.message,
        **({"semantic_id": diagnostic.semantic_id.value} if diagnostic.semantic_id else {}),
        **({"related_sources": list(diagnostic.related_sources)} if diagnostic.related_sources else {}),
        **({"remediation": diagnostic.remediation} if diagnostic.remediation else {}),
    }


def _error_payload(command, error):
    diagnostics = tuple(getattr(error, "diagnostics", ()))
    payload = {
        "command": command,
        "ok": False,
        "error": {
            "code": getattr(error, "code", "COMMAND_FAILED"),
            "message": str(error),
        },
    }
    if diagnostics:
        payload["diagnostics"] = [_diagnostic_data(d) for d in diagnostics]
    return payload


def _render(payload):
    print(json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)

    if args.command == "validate":
        mode = SnapshotMode(args.snapshot_mode)
        if (mode == SnapshotMode.COMMIT_SNAPSHOT) != (args.ref is not None):
            parser.error("--ref is required exactly when --snapshot-mode is COMMIT_SNAPSHOT")

    try:
        if args.command == "validate":
            payload = validate_operation(
                args.root, mode, args.ref, durable_evidence=args.durable_evidence
            )
        elif args.command == "rebuild":
            payload = rebuild_operation(args.root, args.ref, materialize=args.write)
        elif args.command == "refresh":
            payload = refresh_operation(
                args.root, args.changed_since, args.ref, materialize=args.write
            )
        else:
            payload = check_freshness_operation(args.root, args.ref)
    except SubstrateError as error:
        payload = _error_payload(args.command, error)
    except OSError:
        payload = {
            "command": args.command,
            "ok": False,
            "error": {"code": "IO_OPERATION_FAILED", "message": "Filesystem operation failed."},
        }
    except ValueError as error:
        payload = {
            "command": args.command,
            "ok": False,
            "error": {"code": "INVALID_OPERATION", "message": str(error)},
        }

    _render(payload)
    return 0 if payload["ok"] else 1
