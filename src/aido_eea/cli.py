from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .decision import adjudicate_claim
from .io import load_claim


def cmd_audit(args: argparse.Namespace) -> int:
    claim = load_claim(args.input)
    decision = adjudicate_claim(claim)
    payload = decision.to_dict()

    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aido-eea",
        description="AIDO-EEA reference implementation CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_audit = sub.add_parser("audit", help="Adjudicate a governed claim JSON object.")
    p_audit.add_argument("input", help="Path to claim JSON.")
    p_audit.add_argument("-o", "--output", help="Optional output JSON path.")
    p_audit.set_defaults(func=cmd_audit)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
