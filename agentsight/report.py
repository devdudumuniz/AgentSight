from __future__ import annotations

from pathlib import Path

from .evidence import EvidenceStore


def _short_hash(value: str) -> str:
    return value[:12]


def generate_markdown_report(run_dir: Path) -> str:
    store = EvidenceStore(run_dir)
    events = store.list_events()
    lines = [
        "# AgentSight Visual Evidence Report",
        "",
        f"Run: `{run_dir}`",
        "",
        "| Label | Scope | Backend | Redacted | Hash | Timestamp |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for event in events:
        redacted = "yes" if event.get("redacted_image_path") else "no"
        lines.append(
            "| {label} | {scope} | {backend} | {redacted} | `{hash}` | {timestamp} |".format(
                label=event.get("label", ""),
                scope=event.get("scope", ""),
                backend=event.get("backend", ""),
                redacted=redacted,
                hash=_short_hash(str(event.get("sha256", ""))),
                timestamp=event.get("timestamp_utc", ""),
            )
        )

    lines.append("")
    for event in events:
        image_value = event.get("redacted_image_path") or event.get("image_path")
        if not image_value:
            continue
        image_path = Path(str(image_value))
        try:
            relative = image_path.relative_to(run_dir)
        except ValueError:
            relative = Path(image_path.name)
        lines.extend([f"## {event.get('label', image_path.stem)}", "", f"![capture]({relative})", ""])

    return "\n".join(lines).rstrip() + "\n"
