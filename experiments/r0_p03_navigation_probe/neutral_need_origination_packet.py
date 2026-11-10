"""Build an exact, source-free, prospective independent information-need input.

Only a neutral context and neutral author instructions are ever delivered to
the future independent author. The separately generated coordinator receipt
binds real source-history provenance without giving source paths, old tasks,
answers or comparator design to that author.

This packet is for originating candidate information needs. It is NOT an
approved author-visible original corpus, a frozen task fixture, reference
gold, scored run, source admission, or proof of independent exposure safety.
"""
from __future__ import annotations

from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

PIN = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
IDENTIFIER = "R0_P03_FRESH_NEED_ORIGINATION_INPUT_V01"
LOCAL_FOLDER = Path(".venv") / ".r0_p03_fresh_need_origination_v01"
ARCHIVE_NAME = "R0_P03_FRESH_NEED_ORIGINATION_INPUT_V01.zip"
RECEIPT_NAME = "R0_P03_FRESH_NEED_ORIGINATION.safe-receipt.json"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
SOURCE_PROVENANCE = {
    "README.md": {
        "bytes": 2493,
        "sha256": "e79e8cf431d6f208dd7f670090c62012152228c67d4cc17a391867d5b3ab2b68",
        "git_blob": "0fa0fa8d6e168bf4c790051ce793f38583cfdcfe",
        "anchors": ("The Autonomous Data Science System (ADS)", "strong LLM",
                    "frontend/", "Historical material is provenance"),
        "claim_keys": ("system_purpose", "project_artifact_roles"),
    },
    "docs/README.md": {
        "bytes": 15338,
        "sha256": "9e50ff1ae3577f53023ca74aba908d7895d6ceb1da788176ac08673bd346f808",
        "git_blob": "3d8c2fdd01788d78105b1c344fd363f5e26879c0",
        "anchors": ("Repository and Documentation Guide", "current truth",
                    "historical evidence"),
        "claim_keys": ("documentation_roles", "historical_current_distinction"),
    },
    "docs/VISION.md": {
        "bytes": 18340,
        "sha256": "716e58ecac8c95b99acb2576ce68b9a4c66ff1005b9272813bd483ec086d4b76",
        "git_blob": "8cbec9bae6d8edd5c89528dc5a9a1bb18c9e0217",
        "anchors": ("The Autonomous Data Science System aims", "LLM is a component"),
        "claim_keys": ("system_purpose", "methodological_evidence"),
    },
    "docs/DEVELOPMENT_METHOD.md": {
        "bytes": 36337,
        "sha256": "e7e2f5a879773e77a4d6ae4415735fd1b24ab8280bcdeada17918e62ed209d1b",
        "git_blob": "89940bde33d933c3117c5a71aaffe5620e965155",
        "anchors": ("ADS evolves at two levels", "target ADS product/system",
                    "method used to build"),
        "claim_keys": ("project_product_separation", "review_and_history"),
    },
    "frontend/README.md": {
        "bytes": 7028,
        "sha256": "3d8003689bce1a62098843bd3db7f7c9d2d6fc5de53fc93f115af78acc35c7ae",
        "git_blob": "db0d0b2922793ebfdca8094d1b3fd744dde31abd",
        "anchors": ("ADS V1 Frontend Spike",
                    "evaluation and product-validation track",
                    "Overview", "Data", "EDA", "human approval"),
        "claim_keys": ("product_frontend_prototype", "interaction_areas"),
    },
}
PROHIBITED_AUTHOR_PATTERNS = (
    # No original source file paths, specific version IDs, authors' old answers
    # or names of experimental treatment arms in author-visible text.
    re.compile(r"\b(?:R0[-_ ]?P0?3|Research\s+[0-9]{3}|B[0-4])\b", re.I),
    re.compile(r"\b[0-9a-f]{40}\b", re.I),
    re.compile(r"\b[0-9a-f]{64}\b", re.I),
    re.compile(r"\b(?:docs|frontend|src|experiments|tests|schemas|tools)/[A-Za-z0-9_.\-/]+", re.I),
    re.compile(r"https?://", re.I),
    re.compile(r"\b(?:must.retrieve|must.not.retrieve|gold.answer|subject.catalog|winning.arm)\b", re.I),
)
AUTHOR_FILES = {
    "NEUTRAL_CONTEXT.md": "NEED_ORIGINATION_NEUTRAL_CONTEXT_V01.md",
    "AUTHOR_BRIEF.md": "NEED_ORIGINATION_INDEPENDENT_AUTHOR_BRIEF_V01.md",
}


def stable_json(value: object) -> bytes:
    return (json.dumps(
        value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ) + "\n").encode("ascii")


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, check=True
    ).stdout


def verify_originals(repo: Path) -> dict:
    """Verify supporting external historical originals, never ship them.

    These explicit snippets support high-level descriptive statements.
    A successful check cannot prove the safety of a paraphrase by itself.
    """
    actual_commit = git(repo, "rev-parse", "--verify", PIN + "^{commit}").strip().decode("ascii")
    if actual_commit != PIN:
        raise ValueError("Historical source commit mismatch")
    observed = {}
    for path, expected in SOURCE_PROVENANCE.items():
        raw = git(repo, "show", PIN + ":" + path)
        git_id = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if (len(raw) != expected["bytes"]
                or sha256(raw).hexdigest() != expected["sha256"]
                or git_id != expected["git_blob"]):
            raise ValueError("Source provenance drift")
        contents = raw.decode("utf-8")
        if not all(anchor in contents for anchor in expected["anchors"]):
            raise ValueError("Historical source witness anchor unavailable")
        observed[path] = {
            "bytes": expected["bytes"],
            "sha256": expected["sha256"],
            "git_blob": expected["git_blob"],
            "source_claim_keys": expected["claim_keys"],
            "anchor_count_verified": len(expected["anchors"]),
            "source_witness_type": "DECLARATION_ONLY_NOT_IMPLEMENTATION_PROOF",
        }
    return observed


def check_author_texts(texts: dict[str, bytes]) -> None:
    if set(texts) != set(AUTHOR_FILES):
        raise ValueError("Exactly two author-visible files required")
    for name, raw in texts.items():
        if len(raw) > 12000 or b"\0" in raw or b"\r\n" in raw or not raw.endswith(b"\n"):
            raise ValueError("Nonneutral or unsupported input encoding")
        text = raw.decode("utf-8")
        if any(pattern.search(text) for pattern in PROHIBITED_AUTHOR_PATTERNS):
            raise ValueError("Recognized prior-design, source-path or answer leakage")
        if name == "AUTHOR_BRIEF.md":
            for required in (
                "independent contributor", "twelve distinct", "NOT_YET_ADJUDICATED",
                "Do not", "owner-private", "four areas",
                "NEED_PROPOSALS_RESTRICTED.md",
            ):
                if required not in text:
                    raise ValueError("Incomplete author instruction")
        else:
            for required in (
                "historical project-repository snapshot", "Project development",
                "ADS Product", "frontend evaluation/prototype track",
                "not by itself prove", "separate later determination",
            ):
                if required not in text:
                    raise ValueError("Incomplete or inappropriately absolute orientation")


def zip_data(texts: dict[str, bytes]) -> bytes:
    output = BytesIO()
    with ZipFile(output, "w") as archive:
        for name, raw in sorted(texts.items()):
            item = ZipInfo(name, date_time=FIXED_TIME)
            item.compress_type = ZIP_DEFLATED
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            archive.writestr(item, raw)
    return output.getvalue()


def build(repo: Path, *, verify_only: bool = False) -> dict:
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("Real ADS Git repository required")
    provenance = verify_originals(repo)
    local = Path(__file__).resolve().parent
    texts = {name: (local / file).read_bytes() for name, file in AUTHOR_FILES.items()}
    check_author_texts(texts)
    archive = zip_data(texts)
    manifest = {
        "identifier": IDENTIFIER,
        "historical_source_pin": PIN,
        "evidence": provenance,
        "source_claim_boundary": "NEUTRAL_DERIVATIVE_DECLARATIONS_NOT_OWNER_VALIDATED",
        "author_visible_original_source_files": 0,
        "author_visible_restricted_prior_evidence": 0,
        "author_visible_file_count": 2,
        "author_visible_sha256": {name: sha256(raw).hexdigest()
                                  for name, raw in sorted(texts.items())},
        "author_visible_bytes": {name: len(raw) for name, raw in sorted(texts.items())},
        "review_type": "ACTUAL_FRESH_INDEPENDENT_NEED_ORIGINATION_NOT_ANSWER_KEY",
        "semantic_disclosure_clearance": "CANDIDATE_PENDING_ACTUAL_AUTHOR_ROLE_EXPOSURE",
        "owner_transfer_authorization": "NOT_YET_AUTHORIZED",
        "source_admissions": 0,
        "task_proposals_created": 0,
        "scored_tasks": 0,
        "answer_key": "NONE",
        "b0_b4_results": "NONE",
    }
    receipt = {
        "identifier": IDENTIFIER,
        "archive_filename": ARCHIVE_NAME,
        "archive_bytes": len(archive),
        "archive_sha256": sha256(archive).hexdigest(),
        "neutral_source_count": len(provenance),
        "delivered_original_source_count": 0,
        "delivered_author_visible_files": 2,
        "source_provenance_commit": PIN,
        "author_source_exposure": "TWO_NEUTRAL_DERIVATIVES_ONLY",
        "author_role_admission": "PENDING_ACTUAL_INDEPENDENT_INTAKE",
        "owner_transfer_authorization": "NOT_YET_AUTHORIZED",
        "task_proposals": "NONE",
        "source_admissions": 0,
        "scored_tasks": "NONE",
        "b0_b4_results": "NONE",
    }
    folder = repo / LOCAL_FOLDER
    packet = folder / ARCHIVE_NAME
    pmanifest = folder / "R0_P03_FRESH_NEED_ORIGINATION.coordinator_provenance.json"
    preceipt = folder / RECEIPT_NAME
    if verify_only:
        if (not packet.is_file() or packet.read_bytes() != archive
                or not pmanifest.is_file() or pmanifest.read_bytes() != stable_json(manifest)
                or not preceipt.is_file() or preceipt.read_bytes() != stable_json(receipt)):
            raise ValueError("The exact neutral author input is not reproducible")
        print("NEUTRAL_NEED_ORIGINATION_REPRODUCIBILITY=PASS")
    else:
        if any(p.exists() for p in (packet, pmanifest, preceipt)):
            raise FileExistsError("No overwriting an existing independent-author input")
        folder.mkdir(parents=True, exist_ok=True)
        with packet.open("xb") as f:
            f.write(archive)
        with pmanifest.open("xb") as f:
            f.write(stable_json(manifest))
        with preceipt.open("xb") as f:
            f.write(stable_json(receipt))
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit(
            "usage: python -m experiments.r0_p03_navigation_probe."
            "neutral_need_origination_packet REPOSITORY [--verify-only]"
        )
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
