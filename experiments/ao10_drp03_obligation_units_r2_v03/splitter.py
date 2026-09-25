from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

_SENTINEL = "\u241f"
_ABBREVIATIONS = (
    "e.g.",
    "i.e.",
    "etc.",
    "vs.",
    "Fig.",
    "Eq.",
    "Dr.",
    "Mr.",
    "Ms.",
    "No.",
)


@dataclass(frozen=True)
class Segment:
    kind: str
    heading: str | None
    text: str
    context: str | None = None


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _protect_periods(text: str) -> str:
    protected = text
    urls: list[str] = []

    def protect_url(match: re.Match[str]) -> str:
        token = f"__URL_{len(urls)}__"
        raw = match.group(0)
        trailing = ""
        while raw and raw[-1] in ".,!?":
            trailing = raw[-1] + trailing
            raw = raw[:-1]
        urls.append(raw)
        return token + trailing

    protected = re.sub(r"https?://[^\s)\]>]+", protect_url, protected)

    for abbreviation in _ABBREVIATIONS:
        protected = protected.replace(abbreviation, abbreviation.replace(".", _SENTINEL))

    protected = re.sub(
        r"\b([Vv]\d+)\.(\d+(?:\.\d+)*)\b",
        lambda m: m.group(0).replace(".", _SENTINEL),
        protected,
    )
    protected = re.sub(r"(?<=\d)\.(?=\d)", _SENTINEL, protected)
    protected = re.sub(r"(?<=\w)\.(?=\w)", _SENTINEL, protected)

    for index, url in enumerate(urls):
        protected = protected.replace(
            f"__URL_{index}__",
            url.replace(".", _SENTINEL),
        )
    return protected


def sentence_split(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text.strip())
    if not compact:
        return []

    protected = _protect_periods(compact)
    parts = re.split(
        r"(?<=[.!?])\s+(?=(?:[A-Z0-9*_(\[\u00a7]|\*\*))",
        protected,
    )
    result = []
    for part in parts:
        restored = part.replace(_SENTINEL, ".").strip()
        if restored:
            result.append(restored)
    return result


def _indent_width(line: str) -> int:
    expanded = line.replace("\t", "    ")
    return len(expanded) - len(expanded.lstrip(" "))


def split_structured_lines(lines: Iterable[str]) -> list[str]:
    normalized = [line.rstrip() for line in lines]
    groups: list[list[str]] = []
    current: list[str] = []
    for line in normalized:
        if not line.strip():
            if current:
                groups.append(current)
                current = []
            continue
        current.append(line)
    if current:
        groups.append(current)

    items: list[str] = []
    for group in groups:
        min_indent = min(_indent_width(line) for line in group if line.strip())
        current_item: list[str] = []
        for line in group:
            indent = _indent_width(line)
            if indent == min_indent:
                if current_item:
                    items.append("\n".join(current_item).strip())
                current_item = [line.strip()]
            else:
                if not current_item:
                    current_item = [line.strip()]
                else:
                    current_item.append(line.strip())
        if current_item:
            items.append("\n".join(current_item).strip())
    return [item for item in items if item]


def _is_table_separator(line: str) -> bool:
    stripped = line.strip().strip("|")
    cells = [cell.strip() for cell in stripped.split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def segment_markdown(text: str) -> list[Segment]:
    lines = normalize_newlines(text).split("\n")
    segments: list[Segment] = []
    heading: str | None = None
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if re.match(r"^#{1,6}\s+", stripped):
            heading = stripped
            i += 1
            continue

        fence = re.match(r"^\s*((?:\x60{3})|(?:~{3}))", line)
        if fence:
            marker = fence.group(1)
            i += 1
            block: list[str] = []
            while i < len(lines) and not re.match(rf"^\s*{re.escape(marker)}", lines[i]):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            for item in split_structured_lines(block):
                segments.append(Segment("structured", heading, item))
            continue

        if "|" in line and i + 1 < len(lines) and _is_table_separator(lines[i + 1]):
            header = line.strip()
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                row = lines[i].strip()
                segments.append(Segment("table_row", heading, row, context=header))
                i += 1
            continue

        list_match = re.match(r"^(\s*)(?:[-*+]|\d+[.)])\s+(.*)$", line)
        if list_match:
            base_indent = len(list_match.group(1).replace("\t", "    "))
            content = [list_match.group(2).strip()]
            i += 1
            while i < len(lines):
                next_line = lines[i]
                if not next_line.strip():
                    break
                if re.match(r"^#{1,6}\s+", next_line.strip()):
                    break
                if re.match(r"^(\s*)(?:[-*+]|\d+[.)])\s+", next_line):
                    break
                if _indent_width(next_line) <= base_indent:
                    break
                content.append(next_line.strip())
                i += 1
            joined = " ".join(content)
            for sentence in sentence_split(joined):
                segments.append(Segment("text", heading, sentence))
            continue

        if stripped.startswith(">"):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            for sentence in sentence_split(" ".join(quote_lines)):
                segments.append(Segment("text", heading, sentence))
            continue

        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            nxt_stripped = nxt.strip()
            if not nxt_stripped:
                break
            if re.match(r"^#{1,6}\s+", nxt_stripped):
                break
            if re.match(r"^\s*((?:\x60{3})|(?:~{3}))", nxt):
                break
            if re.match(r"^(\s*)(?:[-*+]|\d+[.)])\s+", nxt):
                break
            if nxt_stripped.startswith(">"):
                break
            if "|" in nxt and i + 1 < len(lines) and _is_table_separator(lines[i + 1]):
                break
            paragraph.append(nxt_stripped)
            i += 1

        for sentence in sentence_split(" ".join(paragraph)):
            segments.append(Segment("text", heading, sentence))

    return segments
