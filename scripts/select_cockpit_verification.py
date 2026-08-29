from __future__ import annotations

import argparse
import shlex
from dataclasses import dataclass
from pathlib import Path

FULL_SPECS = "e2e/cockpit-reintegration*.spec.ts"

PRESENTATION_SPECS = (
    "e2e/cockpit-reintegration-review-256.spec.ts",
    "e2e/cockpit-reintegration-presentation-integrity.spec.ts",
    "e2e/cockpit-reintegration-conversation-integration-study.spec.ts",
)
CONVERSATION_SPECS = (
    "e2e/cockpit-reintegration-conversation-integration-study.spec.ts",
    "e2e/cockpit-reintegration-conversation-performance.spec.ts",
    "e2e/cockpit-reintegration-presentation-integrity.spec.ts",
    "e2e/cockpit-reintegration-review-256.spec.ts",
)
SPATIAL_RAIL_SPECS = (
    "e2e/cockpit-reintegration-spatial-rail-angle.spec.ts",
    "e2e/cockpit-reintegration-product-surface.spec.ts",
    "e2e/cockpit-reintegration-conversation-integration-study.spec.ts",
)
FOCUS_SPECS = (
    "e2e/cockpit-reintegration-presentation-integrity.spec.ts",
    "e2e/cockpit-reintegration-phasec-completion.spec.ts",
    "e2e/cockpit-reintegration-product-surface.spec.ts",
)

WORKFLOW_PATH = ".github/workflows/cockpit-reintegration-fidelity.yml"
SELECTOR_PATH = "scripts/select_cockpit_verification.py"


@dataclass(frozen=True)
class Selection:
    mode: str
    tier: str
    specs: tuple[str, ...]
    reason: str


def ordered_unique(items: list[str] | tuple[str, ...]) -> tuple[str, ...]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)


def is_docs_only(path: str) -> bool:
    return path.startswith("docs/") or path in {"README.md"}


def is_cockpit_test(path: str) -> bool:
    return path.startswith("frontend/e2e/cockpit-reintegration") and path.endswith(".spec.ts")


def classify(event: str, message: str, changed_files: list[str]) -> Selection:
    files = ordered_unique(tuple(path.strip() for path in changed_files if path.strip()))

    if event in {"pull_request", "workflow_dispatch"}:
        return Selection("full", "V3", (FULL_SPECS,), f"{event} requires complete integrated verification")

    if "[full-cockpit]" in message.lower():
        return Selection("full", "V3", (FULL_SPECS,), "head commit explicitly requested the complete Cockpit gate")

    if not files:
        return Selection("full", "V3", (FULL_SPECS,), "changed-file set unavailable; conservative fallback")

    if WORKFLOW_PATH in files or SELECTOR_PATH in files:
        return Selection("full", "V3", (FULL_SPECS,), "verification architecture changed")

    if all(is_docs_only(path) for path in files):
        return Selection("skip", "V0", (), "documentation/provenance-only change")

    test_files = [path for path in files if is_cockpit_test(path)]
    implementation_files = [
        path for path in files if not is_cockpit_test(path) and not is_docs_only(path)
    ]
    if test_files and not implementation_files:
        specs = tuple(path.removeprefix("frontend/") for path in test_files)
        return Selection("targeted", "V1", ordered_unique(specs), "only Cockpit regression specifications changed")

    presentation_paths = {
        "frontend/design-lab/cockpit-reintegration-presentation-integrity.css",
        "frontend/design-lab/cockpit-reintegration-review-256.css",
    }
    if implementation_files and all(path in presentation_paths for path in implementation_files):
        extras = [path.removeprefix("frontend/") for path in test_files]
        return Selection(
            "subsystem",
            "V2",
            ordered_unique((*PRESENTATION_SPECS, *extras)),
            "localized Conversation presentation-integrity change",
        )

    if implementation_files and all(
        path.startswith("frontend/design-lab/cockpit-conversation-")
        or path.startswith("frontend/design-lab/cockpit-reintegration-conversation-")
        for path in implementation_files
    ):
        extras = [path.removeprefix("frontend/") for path in test_files]
        return Selection(
            "subsystem",
            "V2",
            ordered_unique((*CONVERSATION_SPECS, *extras)),
            "localized Conversation subsystem change",
        )

    if implementation_files and all(
        "process-focus" in path or "focus" in Path(path).name
        for path in implementation_files
    ):
        extras = [path.removeprefix("frontend/") for path in test_files]
        return Selection(
            "subsystem",
            "V2",
            ordered_unique((*FOCUS_SPECS, *extras)),
            "localized current-process Focus subsystem change",
        )

    if implementation_files and all(
        path.startswith("frontend/design-lab/cockpit-spatial-rail-")
        for path in implementation_files
    ):
        extras = [path.removeprefix("frontend/") for path in test_files]
        return Selection(
            "subsystem",
            "V2",
            ordered_unique((*SPATIAL_RAIL_SPECS, *extras)),
            "localized spatial-rail subsystem change",
        )

    return Selection(
        "full",
        "V3",
        (FULL_SPECS,),
        "shared, mixed, or unknown Cockpit blast radius; conservative fallback",
    )


def write_github_output(path: Path, selection: Selection) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"mode={selection.mode}\n")
        handle.write(f"tier={selection.tier}\n")
        handle.write("specs=" + " ".join(shlex.quote(spec) for spec in selection.specs) + "\n")
        handle.write("reason=" + selection.reason.replace("\n", " ") + "\n")


def self_test() -> int:
    cases = [
        ("docs only", classify("push", "docs", ["docs/checkpoints/265_example.md"]), ("skip", "V0")),
        ("targeted spec", classify("push", "test", ["frontend/e2e/cockpit-reintegration-review-256.spec.ts"]), ("targeted", "V1")),
        ("presentation subsystem", classify("push", "small css", ["frontend/design-lab/cockpit-reintegration-presentation-integrity.css"]), ("subsystem", "V2")),
        (
            "presentation plus checkpoint note",
            classify(
                "push",
                "small css",
                [
                    "frontend/design-lab/cockpit-reintegration-presentation-integrity.css",
                    "docs/checkpoints/264_example.md",
                ],
            ),
            ("subsystem", "V2"),
        ),
        ("unknown shared", classify("push", "core", ["frontend/design-lab/cockpit-reintegration.html"]), ("full", "V3")),
        ("explicit full", classify("push", "[full-cockpit] close boundary", ["docs/checkpoints/265_example.md"]), ("full", "V3")),
        ("pr full", classify("pull_request", "", ["frontend/design-lab/cockpit-reintegration-presentation-integrity.css"]), ("full", "V3")),
    ]
    failures: list[str] = []
    for name, selection, expected in cases:
        observed = (selection.mode, selection.tier)
        if observed != expected:
            failures.append(f"{name}: expected {expected}, observed {observed}")
    if failures:
        print("Cockpit verification selector self-test FAILED")
        for failure in failures:
            print("  " + failure)
        return 1
    print(f"Cockpit verification selector self-test: PASS ({len(cases)} cases)")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select the minimum justified Cockpit verification tier.")
    parser.add_argument("--event", default="push")
    parser.add_argument("--message", default="")
    parser.add_argument("--changed-file", action="append", default=[])
    parser.add_argument("--github-output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        return self_test()

    selection = classify(args.event, args.message, args.changed_file)
    print(f"mode={selection.mode}")
    print(f"tier={selection.tier}")
    print("specs=" + " ".join(selection.specs))
    print(f"reason={selection.reason}")
    if args.github_output:
        write_github_output(args.github_output, selection)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
