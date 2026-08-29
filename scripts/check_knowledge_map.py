from __future__ import annotations

import argparse
import re
from pathlib import Path

MAP_PATH = Path("docs/KNOWLEDGE_MAP.md")
TOPIC_RE = re.compile(r"<!--\s*KM-TOPIC:\s*([a-z0-9][a-z0-9-]*)\s*-->")
CHECKPOINT_RANGE_RE = re.compile(
    r"<!--\s*KM-CHECKPOINT-RANGE:\s*(\d{3})-(\d{3})\s+([a-z0-9 -]+?)\s*-->"
)
NUMBERED_NAME_RE = re.compile(r"^(\d{3})_.*\.md$")

EXPECTED_TOPICS = {
    "system-identity",
    "project-state",
    "knowledge-representation",
    "evaluation-falsification",
    "runtime-persistence",
    "retrieval-horizon",
    "recommendation-action",
    "methodological-knowledge-universe",
    "source-universe",
    "development-governance",
    "cockpit-core",
    "cockpit-world",
    "work-unit-visual-grammar",
    "connector-visual-grammar",
    "interaction-focus",
    "conversation-workspace",
    "cockpit-provenance",
    "shell-rail",
    "canonical-history",
}

NUMBERED_FAMILIES = (
    Path("docs/foundations"),
    Path("docs/specifications"),
    Path("docs/research"),
)

REQUIRED_SPECIALIZED_ROUTES = {
    "docs/methodological_knowledge/COVERAGE_MAP.md",
    "docs/cockpit/PHASE_C_DECISION_LEDGER.md",
    "docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md",
    "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md",
    "docs/model_collaboration/REVIEW_INBOX.md",
}

FORBIDDEN_LIVE_MARKERS = (
    "## Current continuation route",
    "**Current checkpoint:**",
    "**Active development branch:**",
    "**Active PR:**",
    "**Promoted V1 integration branch:**",
    "**Latest scientific experiment outcome:**",
)

PATH_PREFIXES = (
    "README.md",
    "docs/",
    "frontend/",
    "scripts/",
    ".github/",
    "experiments/",
    "prototype_v0/",
    "src/",
    "tests/",
    "schemas/",
    "migrations/",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the ADS evergreen semantic Knowledge Map, including exhaustive "
            "numbered durable-family routing and checkpoint topic coverage."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of scripts/.",
    )
    return parser.parse_args()


def normalize_candidate(line: str) -> str | None:
    candidate = line.strip().strip("`")
    if not candidate or candidate.startswith("#"):
        return None
    if not candidate.startswith(PATH_PREFIXES):
        return None
    candidate = candidate.split()[0].strip("`")
    return candidate.rstrip(",;:")


def path_exists(root: Path, candidate: str) -> bool:
    if any(char in candidate for char in "*?["):
        return any(root.glob(candidate))
    return (root / candidate).exists()


def numbered_files(root: Path, relative_dir: Path) -> set[str]:
    directory = root / relative_dir
    if not directory.is_dir():
        return set()
    return {
        path.relative_to(root).as_posix()
        for path in directory.iterdir()
        if path.is_file() and NUMBERED_NAME_RE.match(path.name)
    }


def checkpoint_numbers(root: Path) -> set[int]:
    directory = root / "docs" / "checkpoints"
    if not directory.is_dir():
        return set()
    numbers: set[int] = set()
    for path in directory.iterdir():
        if not path.is_file():
            continue
        match = NUMBERED_NAME_RE.match(path.name)
        if match:
            numbers.add(int(match.group(1)))
    return numbers


def validate(root: Path) -> list[str]:
    map_path = root / MAP_PATH
    try:
        text = map_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"missing {MAP_PATH}"]

    errors: list[str] = []

    if "## Subject library" not in text:
        errors.append("missing '## Subject library' section")

    for marker in FORBIDDEN_LIVE_MARKERS:
        if marker in text:
            errors.append(
                f"live-state marker must not be stored in evergreen Knowledge Map: {marker!r}"
            )

    topic_ids = TOPIC_RE.findall(text)
    duplicates = sorted({topic for topic in topic_ids if topic_ids.count(topic) > 1})
    if duplicates:
        errors.append("duplicate KM-TOPIC ids: " + ", ".join(duplicates))

    topic_set = set(topic_ids)
    missing_topics = sorted(EXPECTED_TOPICS - topic_set)
    unexpected_topics = sorted(topic_set - EXPECTED_TOPICS)
    if missing_topics:
        errors.append("missing required KM-TOPIC ids: " + ", ".join(missing_topics))
    if unexpected_topics:
        errors.append("unexpected KM-TOPIC ids: " + ", ".join(unexpected_topics))

    current_topic: str | None = None
    topic_path_counts: dict[str, int] = {topic: 0 for topic in topic_ids}
    routed_paths: set[str] = set()
    unresolved: list[str] = []

    for line in text.splitlines():
        marker = TOPIC_RE.search(line)
        if marker:
            current_topic = marker.group(1)
            continue

        candidate = normalize_candidate(line)
        if candidate is None:
            continue

        routed_paths.add(candidate)
        if current_topic is not None:
            topic_path_counts[current_topic] = topic_path_counts.get(current_topic, 0) + 1
        if not path_exists(root, candidate):
            unresolved.append(candidate)

    empty_topics = sorted(
        topic for topic in EXPECTED_TOPICS if topic_path_counts.get(topic, 0) == 0
    )
    if empty_topics:
        errors.append("topics with no routed repository paths: " + ", ".join(empty_topics))

    if unresolved:
        errors.append("unresolved routed paths: " + ", ".join(sorted(set(unresolved))))

    for relative_dir in NUMBERED_FAMILIES:
        actual = numbered_files(root, relative_dir)
        missing_routes = sorted(actual - routed_paths)
        if missing_routes:
            errors.append(
                f"unrouted numbered files in {relative_dir.as_posix()}: "
                + ", ".join(missing_routes)
            )

    missing_specialized = sorted(REQUIRED_SPECIALIZED_ROUTES - routed_paths)
    if missing_specialized:
        errors.append(
            "required specialized indexes not routed: " + ", ".join(missing_specialized)
        )

    covered_checkpoint_numbers: set[int] = set()
    range_errors: list[str] = []
    for start_text, end_text, topic_text in CHECKPOINT_RANGE_RE.findall(text):
        start = int(start_text)
        end = int(end_text)
        if end < start:
            range_errors.append(f"invalid checkpoint range {start_text}-{end_text}")
            continue

        range_topics = topic_text.split()
        unknown = sorted(set(range_topics) - EXPECTED_TOPICS)
        if unknown:
            range_errors.append(
                f"checkpoint range {start_text}-{end_text} has unknown topics: "
                + ", ".join(unknown)
            )
            continue

        if not range_topics:
            range_errors.append(f"checkpoint range {start_text}-{end_text} has no topics")
            continue

        covered_checkpoint_numbers.update(range(start, end + 1))

    if range_errors:
        errors.extend(range_errors)

    actual_checkpoint_numbers = checkpoint_numbers(root)
    missing_checkpoint_coverage = sorted(
        actual_checkpoint_numbers - covered_checkpoint_numbers
    )
    if missing_checkpoint_coverage:
        errors.append(
            "numbered checkpoints without semantic topic coverage: "
            + ", ".join(f"{number:03d}" for number in missing_checkpoint_coverage)
        )

    if not CHECKPOINT_RANGE_RE.search(text):
        errors.append("no KM-CHECKPOINT-RANGE records found")

    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = validate(root)
    if errors:
        print("Knowledge map integrity violations:")
        for error in errors:
            print("  ERROR " + error)
        return 1

    text = (root / MAP_PATH).read_text(encoding="utf-8")
    topics = TOPIC_RE.findall(text)
    families = {
        relative_dir.as_posix(): len(numbered_files(root, relative_dir))
        for relative_dir in NUMBERED_FAMILIES
    }
    checkpoints = len(checkpoint_numbers(root))
    print(
        "Knowledge map integrity: PASS "
        f"topics={len(topics)} "
        f"foundations={families['docs/foundations']} "
        f"specifications={families['docs/specifications']} "
        f"research={families['docs/research']} "
        f"checkpoint_numbers={checkpoints} "
        f"map={MAP_PATH}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
