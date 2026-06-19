from __future__ import annotations

import argparse
import json
from pathlib import Path

from .capture import CaptureConfig, capture_screen
from .policy import CapturePolicy


def _parse_region(value: str) -> tuple[int, int, int, int]:
    parts = value.split(",")
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("Use o formato x,y,width,height.")
    try:
        x, y, width, height = (int(part.strip()) for part in parts)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Regiao deve conter apenas numeros inteiros.") from exc
    if min(x, y, width, height) < 0 or width == 0 or height == 0:
        raise argparse.ArgumentTypeError("Regiao invalida.")
    return x, y, width, height


def main() -> None:
    parser = argparse.ArgumentParser(prog="screenshot-agent")
    sub = parser.add_subparsers(dest="command", required=True)

    capture = sub.add_parser("capture")
    capture.add_argument("--label", required=True)
    capture.add_argument("--output", required=True)
    capture.add_argument("--region", type=_parse_region)
    capture.add_argument("--redact-region", action="append", type=_parse_region, default=[])
    capture.add_argument("--no-redact", action="store_false", dest="redact")
    capture.add_argument("--fullscreen", action="store_true")
    capture.add_argument("--consent", action="store_true")
    capture.add_argument("--allow-fullscreen", action="store_true")

    report = sub.add_parser("report")
    report.add_argument("--run", required=True)

    args = parser.parse_args()

    if args.command == "capture":
        result = capture_screen(
            CaptureConfig(
                label=args.label,
                output_dir=Path(args.output),
                region=args.region,
                redaction_regions=tuple(args.redact_region),
                fullscreen=args.fullscreen,
                consent=args.consent,
                redact=args.redact,
            ),
            CapturePolicy(allow_fullscreen=args.allow_fullscreen),
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if args.command == "report":
        run_dir = Path(args.run)
        items = sorted(run_dir.glob("*.json"))
        print(f"# Visual Evidence Report\n\nRun: `{run_dir}`\n")
        for item in items:
            data = json.loads(item.read_text(encoding="utf-8"))
            if "path" in data:
                print(f"## {data.get('label', item.stem)}\n")
                print(f"- SHA-256: `{data['sha256']}`")
                print(f"- Timestamp UTC: `{data['timestamp_utc']}`")
                print(f"- Redaction aplicada: `{data.get('redact_applied', False)}`")
                print(f"\n![{data.get('label', item.stem)}]({Path(data['path']).name})\n")
        return


if __name__ == "__main__":
    main()
