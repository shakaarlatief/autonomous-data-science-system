from __future__ import annotations

import argparse


PUBLIC_STATUSES = ("PASS", "FAIL")
PRIVATE_STATUSES = ("PASS", "FAIL", "NOT_VERIFIED")


def evaluate_chat_rotation(
    public_integrity: str,
    private_integrity: str,
    *,
    private_required: bool,
    open_transition_obligations: tuple[str, ...] = (),
) -> tuple[str, list[str]]:
    if public_integrity not in PUBLIC_STATUSES:
        raise ValueError(f"invalid public integrity status: {public_integrity!r}")
    if private_integrity not in PRIVATE_STATUSES:
        raise ValueError(f"invalid private integrity status: {private_integrity!r}")

    reasons: list[str] = []
    if public_integrity == "FAIL":
        reasons.append("public repository integrity is not green")
        return "FAIL", reasons

    if private_required and private_integrity == "FAIL":
        reasons.append("required private continuity integrity failed")
        return "FAIL", reasons

    if private_required and private_integrity == "NOT_VERIFIED":
        reasons.append("required private continuity integrity is not verified")

    if open_transition_obligations:
        reasons.extend(
            f"open transition obligation: {obligation}"
            for obligation in open_transition_obligations
        )

    if reasons:
        return "HOLD", reasons
    return "PASS", []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Combine public repository integrity, private continuity integrity, and "
            "open transition obligations into the governed chat-rotation preflight."
        )
    )
    parser.add_argument("--public-integrity", choices=PUBLIC_STATUSES, required=True)
    parser.add_argument("--private-integrity", choices=PRIVATE_STATUSES, required=True)
    parser.add_argument("--private-required", action="store_true")
    parser.add_argument(
        "--open-transition-obligation",
        action="append",
        default=[],
        help="Repeat for each unresolved transition obligation that prevents rotation PASS.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    status, reasons = evaluate_chat_rotation(
        args.public_integrity,
        args.private_integrity,
        private_required=args.private_required,
        open_transition_obligations=tuple(args.open_transition_obligation),
    )
    for reason in reasons:
        print(f"  HOLD {reason}" if status == "HOLD" else f"  ERROR {reason}")
    print(f"CHAT_ROTATION_PREFLIGHT={status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
