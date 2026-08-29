from __future__ import annotations

import argparse
import re
from pathlib import Path

MAP_PATH = Path("docs/KNOWLEDGE_MAP.md")
TOPIC_RE = re.compile(r"<!--\s*KM-TOPIC:\s*([a-z0-9][a-z0-9-]*)\s*-->")
EXPECTED_TOPICS = {
    "system-vision",
    "project-state",
    "reusable-knowledge",
    "evaluation-falsification",
    "v1-runtime-persistence",
    "retrieval-horizon",
    "recommendation-calibration",
    "methodological-knowledge-universe",
    "source-universe",
    "development-continuity",
    "cockpit-architecture",
    "cockpit-visual-grammar",
    "cockpit-interaction-states",
    "conversation-workspace",
    "cockpit-provenance-fidelity",
    "cockpit-shell-rail",
    "canonical-history",
}
PATH_PREFIXES = (
    "README.md",
    "docs/",
    "frontend/",
    "scripts/",
    ".github/",
    "experiments/",
    "prototype_v0/",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the evergreen ADS knowledge-routing map.")
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
    candidate = candidate.split()[0]
    return candidate.rstrip(",;:")


def path_exists(root: Path, candidate: str) -> bool:
    if any(char in candidate for char in "*?["):
        return any(root.glob(candidate))
    return (root / candidate).exists()


def validate(root: Path) -> list[str]:
    map_path = root / MAP_PATH
    try:
        text = map_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"missing {MAP_PATH}"]

    errors: list[str] = []
    if "## Current continuation route" not in text:
        errors.append("missing '## Current continuation route' section")
    if "## Evergreen topic library" not in text:
        errors.append("missing '## Evergreen topic library' section")

    topic_ids = TOPIC_RE.findall(text)
    duplicates = sorted({topic for topic in topic_ids if topic_ids.count(topic) > 1})
    if duplicates:
        errors.append("duplicate KM-TOPIC ids: " + ", ".join(duplicates))

    missing = sorted(EXPECTED_TOPICS - set(topic_ids))
    if missing:
        errors.append("missing required KM-TOPIC ids: " + ", ".join(missing))

    library_marker = text.find("## Evergreen topic library")
    if library_marker < 0:
        return errors
    library = text[library_marker:]

    current_topic: str | None = None
    topic_path_counts: dict[str, int] = {topic: 0 for topic in topic_ids}
    unresolved: list[str] = []
    for line in library.splitlines():
        marker = TOPIC_RE.search(line)
        if marker:
            current_topic = marker.group(1)
            continue
        candidate = normalize_candidate(line)
        if candidate is None:
            continue
        if current_topic is not None:
            topic_path_counts[current_topic] = topic_path_counts.get(current_topic, 0) + 1
        if not path_exists(root, candidate):
            unresolved.append(candidate)

    empty_topics = sorted(topic for topic in EXPECTED_TOPICS if topic_path_counts.get(topic, 0) == 0)
    if empty_topics:
        errors.append("topics with no routed repository paths: " + ", ".join(empty_topics))
    if unresolved:
        errors.append("unresolved routed paths: " + ", ".join(sorted(set(unresolved))))

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
    print(
        "Knowledge map integrity: PASS "
        f"topics={len(topics)} required={len(EXPECTED_TOPICS)} map={MAP_PATH}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
