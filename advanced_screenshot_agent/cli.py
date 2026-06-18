from __future__ import annotations

import argparse
import json
from pathlib import Path

from .capture import CaptureConfig, capture_screen
from .policy import CapturePolicy


def main() -> None:
    parser = argparse.ArgumentParser(prog="screenshot-agent")
    sub = parser.add_subparsers(dest="command", required=True)

    capture = sub.add_parser("capture")
    capture.add_argument("--label", required=True)
    capture.add_argument("--output", required=True)
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
                fullscreen=args.fullscreen,
                consent=args.consent,
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
                print(f"\n![{data.get('label', item.stem)}]({Path(data['path']).name})\n")
        return


if __name__ == "__main__":
    main()
