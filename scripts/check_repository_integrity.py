from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from repository_integrity import validate_repository_contracts


@dataclass(frozen=True)
class ValidatorResult:
    name: str
    returncode: int
    output: str


FOCUSED_VALIDATORS: tuple[tuple[str, str], ...] = (
    ("checkpoint metadata", "check_checkpoint_metadata.py"),
    ("Knowledge Map", "check_knowledge_map.py"),
    ("model collaboration state", "check_model_collaboration_state.py"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the aggregate PUBLIC repository-integrity gate while preserving the "
            "existing focused validators as authoritative subcontracts."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of scripts/.",
    )
    parser.add_argument(
        "--checked-branch",
        help="Optional explicit branch identity forwarded to current-routing validation.",
    )
    return parser.parse_args()


def run_validator(
    root: Path, name: str, script_name: str, extra_args: tuple[str, ...] = ()
) -> ValidatorResult:
    command = [sys.executable, str(root / "scripts" / script_name), "--root", str(root)]
    command.extend(extra_args)
    completed = subprocess.run(
        command,
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    output = "\n".join(
        part.strip() for part in (completed.stdout, completed.stderr) if part.strip()
    )
    return ValidatorResult(name, completed.returncode, output)


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    failures: list[str] = []

    contract_errors = validate_repository_contracts(root)
    if contract_errors:
        failures.append("family-aware repository contracts")
        print("Family-aware repository-integrity violations:")
        for error in contract_errors:
            print(f"  ERROR {error}")
    else:
        print("Family-aware repository contracts: PASS")

    results: list[ValidatorResult] = []
    for name, script_name in FOCUSED_VALIDATORS:
        results.append(run_validator(root, name, script_name))

    routing_args: tuple[str, ...] = ()
    if args.checked_branch:
        routing_args = ("--checked-branch", args.checked_branch)
    results.append(
        run_validator(
            root,
            "current routing",
            "check_current_routing.py",
            routing_args,
        )
    )

    for result in results:
        if result.returncode == 0:
            print(f"Focused validator {result.name}: PASS")
        else:
            failures.append(result.name)
            print(
                f"Focused validator {result.name}: FAIL "
                f"(exit={result.returncode})"
            )
            if result.output:
                for line in result.output.splitlines():
                    print(f"    {line}")

    status = "FAIL" if failures else "PASS"
    print(f"PUBLIC_REPOSITORY_INTEGRITY={status}")
    if failures:
        print("Failed components: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
