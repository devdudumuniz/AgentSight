from __future__ import annotations

import argparse
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .annotate import Annotation, annotate_image
from .capture import CaptureConfig, capture
from .cleanup import cleanup_runs
from .policy import CapturePolicy
from .redact import Region, redact_regions
from .report import generate_markdown_report


def _parse_region(value: str) -> Region:
    parts = value.split(",")
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("Use x,y,width,height.")
    try:
        x, y, width, height = (int(part.strip()) for part in parts)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Region values must be integers.") from exc
    if min(x, y, width, height) < 0 or width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("Invalid region.")
    return x, y, width, height


def _parse_regions(value: str | None) -> tuple[Region, ...]:
    if not value:
        return ()
    return tuple(_parse_region(part.strip()) for part in value.split(";") if part.strip())


def _write_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def _default_run_dir(label: str) -> Path:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in label)
    slug = "-".join(part for part in cleaned.split("-") if part)[:80] or "capture"
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return Path(".vision-runs") / f"{timestamp}-{slug}"


def _annotations_from_args(args: argparse.Namespace) -> list[Annotation]:
    if args.annotations_json:
        payload = json.loads(Path(args.annotations_json).read_text(encoding="utf-8"))
        return [Annotation(**item) for item in payload]
    regions = _parse_regions(args.regions)
    return [
        Annotation(label=f"region-{index}", kind="region", x=x, y=y, width=width, height=height)
        for index, (x, y, width, height) in enumerate(regions, start=1)
    ]


def _doctor() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def add(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "ok": ok, "detail": detail})

    add("python", sys.version_info >= (3, 10), platform.python_version())

    try:
        import PIL  # noqa: F401

        add("pillow", True, "import ok")
    except Exception as exc:
        add("pillow", False, str(exc))

    try:
        import mss  # noqa: F401

        add("mss", True, "import ok")
    except Exception as exc:
        add("mss", True, f"optional capture backend unavailable: {exc}")

    root = Path(".vision-runs")
    try:
        root.mkdir(parents=True, exist_ok=True)
        probe = root / ".doctor-write-test"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink(missing_ok=True)
        add("vision_runs_writable", True, str(root))
    except Exception as exc:
        add("vision_runs_writable", False, str(exc))

    has_display = bool(os.environ.get("DISPLAY") or os.name == "nt")
    add("display_hint", True, "display likely available" if has_display else "no DISPLAY detected")
    return {"schema_version": "agentsight.doctor.v1", "platform": platform.platform(), "checks": checks}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agentsight")
    sub = parser.add_subparsers(dest="command", required=True)

    capture_parser = sub.add_parser("capture")
    capture_parser.add_argument("--label", required=True)
    capture_parser.add_argument("--output", type=Path)
    capture_parser.add_argument("--scope", choices=["region", "fullscreen", "browser_page"], default="region")
    capture_parser.add_argument("--region", type=_parse_region)
    capture_parser.add_argument("--consent", action="store_true")
    capture_parser.add_argument("--allow-fullscreen", action="store_true")
    capture_parser.add_argument("--mock", action="store_true")
    capture_parser.add_argument("--redact-regions")
    capture_parser.add_argument("--redact-region", dest="redact_regions")
    capture_parser.add_argument("--no-redact", action="store_false", dest="redact")
    capture_parser.add_argument("--json", action="store_true")

    annotate_parser = sub.add_parser("annotate")
    annotate_parser.add_argument("--image", required=True, type=Path)
    annotate_parser.add_argument("--regions")
    annotate_parser.add_argument("--annotations-json", type=Path)
    annotate_parser.add_argument("--output", type=Path)
    annotate_parser.add_argument("--json", action="store_true")

    redact_parser = sub.add_parser("redact")
    redact_parser.add_argument("--image", required=True, type=Path)
    redact_parser.add_argument("--regions", required=True)
    redact_parser.add_argument("--output", type=Path)
    redact_parser.add_argument("--json", action="store_true")

    report_parser = sub.add_parser("report")
    report_parser.add_argument("--run", required=True, type=Path)
    report_parser.add_argument("--output", type=Path)

    cleanup_parser = sub.add_parser("cleanup")
    cleanup_parser.add_argument("--root", default=".vision-runs", type=Path)
    cleanup_parser.add_argument("--retention-hours", default=24, type=int)
    cleanup_parser.add_argument("--keep-manifest", action="store_true")

    sub.add_parser("doctor")
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "capture":
        output_dir = args.output or _default_run_dir(args.label)
        result = capture(
            CaptureConfig(
                label=args.label,
                output_dir=output_dir,
                scope=args.scope,
                region=args.region,
                redaction_regions=_parse_regions(args.redact_regions),
                consent=args.consent,
                allow_fullscreen=args.allow_fullscreen,
                mock=args.mock,
                redact=args.redact,
            ),
            CapturePolicy(allow_fullscreen=args.allow_fullscreen),
        )
        if args.json:
            _write_json(result)
        else:
            print(f"AgentSight capture saved: {result['image_path']}")
        return

    if args.command == "annotate":
        result = annotate_image(args.image, _annotations_from_args(args), args.output)
        if args.json:
            _write_json(result)
        else:
            print(result["annotated_image_path"])
        return

    if args.command == "redact":
        report = redact_regions(args.image, _parse_regions(args.regions), args.output)
        if args.json:
            _write_json(report.to_dict())
        else:
            print(report.output_path)
        return

    if args.command == "report":
        markdown = generate_markdown_report(args.run)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(markdown, encoding="utf-8")
        else:
            print(markdown, end="")
        return

    if args.command == "cleanup":
        _write_json(
            cleanup_runs(
                args.root,
                retention_hours=args.retention_hours,
                keep_manifest=args.keep_manifest,
            )
        )
        return

    if args.command == "doctor":
        _write_json(_doctor())
        return


if __name__ == "__main__":
    main()
