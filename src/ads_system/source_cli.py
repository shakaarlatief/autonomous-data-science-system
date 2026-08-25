"""Provider-free command line operations for the ADS Source Universe substrate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ads_system.application.source_manifest import (
    compare_intake_manifest,
    load_intake_manifest,
    manifest_ingest_requests,
)
from ads_system.application.source_universe import SourceUniverseService
from ads_system.infrastructure.persistence.engine import (
    create_operational_engine,
    sqlite_database_url,
)
from ads_system.infrastructure.source_store import LocalSourceArtifactStore


def _service(database: Path, vault: Path) -> SourceUniverseService:
    return SourceUniverseService(
        create_operational_engine(sqlite_database_url(database)),
        LocalSourceArtifactStore(vault),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m ads_system.source_cli")
    sub = parser.add_subparsers(dest="command", required=True)

    compare = sub.add_parser(
        "compare", help="Compare a local course folder with an intake manifest"
    )
    compare.add_argument("--manifest", type=Path, required=True)
    compare.add_argument("--root", type=Path, required=True)
    compare.add_argument("--output", type=Path)

    ingest = sub.add_parser(
        "ingest", help="Ingest locally present files from a reviewed intake manifest"
    )
    ingest.add_argument("--manifest", type=Path, required=True)
    ingest.add_argument("--root", type=Path, required=True)
    ingest.add_argument("--database", type=Path, required=True)
    ingest.add_argument("--vault", type=Path, required=True)

    audit = sub.add_parser(
        "audit", help="Audit registry and source-artifact store integrity"
    )
    audit.add_argument("--database", type=Path, required=True)
    audit.add_argument("--vault", type=Path, required=True)

    backup = sub.add_parser(
        "backup", help="Create and verify a provider-neutral source backup"
    )
    backup.add_argument("--database", type=Path, required=True)
    backup.add_argument("--vault", type=Path, required=True)
    backup.add_argument("--target", type=Path, required=True)

    restore = sub.add_parser(
        "restore", help="Restore a verified source backup into a clean migrated target"
    )
    restore.add_argument("--backup", type=Path, required=True)
    restore.add_argument("--database", type=Path, required=True)
    restore.add_argument("--vault", type=Path, required=True)

    args = parser.parse_args(argv)
    if args.command == "compare":
        manifest = load_intake_manifest(args.manifest)
        report = [
            {
                "observed_name": item.observed_name,
                "status": item.status,
                "local_name": item.local_name,
                "expected_sha256": item.expected_sha256,
                "observed_sha256": item.observed_sha256,
                "expected_size": item.expected_size,
                "observed_size": item.observed_size,
            }
            for item in compare_intake_manifest(manifest, args.root)
        ]
        text = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.write_text(text, encoding="utf-8", newline="\n")
        else:
            print(text, end="")
        return 0

    service = _service(args.database, args.vault)
    if args.command == "ingest":
        manifest = load_intake_manifest(args.manifest)
        outcomes = [
            service.ingest_file(request)
            for request in manifest_ingest_requests(manifest, args.root)
        ]
        print(
            json.dumps(
                [
                    {
                        "stable_key": outcome.source.stable_key,
                        "sha256": outcome.artifact.sha256,
                        "result": outcome.result,
                    }
                    for outcome in outcomes
                ],
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    if args.command == "audit":
        results = service.audit(update_verified_at=True)
        print(
            json.dumps(
                [
                    {
                        "sha256": result.sha256,
                        "status": result.status,
                        "expected_size": result.expected_size,
                        "observed_size": result.observed_size,
                        "detail": result.detail,
                    }
                    for result in results
                ],
                indent=2,
                sort_keys=True,
            )
        )
        return 0 if all(result.status == "OK" for result in results) else 1
    if args.command == "backup":
        path = service.create_backup(args.target)
        print(path)
        return 0
    if args.command == "restore":
        SourceUniverseService.restore_backup(
            args.backup,
            target_engine=service.engine,
            target_store=service.store,
        )
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
