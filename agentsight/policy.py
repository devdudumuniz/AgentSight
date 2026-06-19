from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

Region = tuple[int, int, int, int]


class CaptureScope(str, Enum):
    REGION = "region"
    WINDOW = "window"
    BROWSER_PAGE = "browser_page"
    FULLSCREEN = "fullscreen"


class PolicyViolation(PermissionError):
    """Raised when a capture request violates the active policy."""


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    scope: str
    reason: str
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class CapturePolicy:
    allow_fullscreen: bool = False
    allow_window_capture: bool = True
    allow_region_capture: bool = True
    require_user_consent: bool = True
    retention_hours: int = 24
    output_root: Path = Path(".vision-runs")
    blocked_window_keywords: tuple[str, ...] = (
        "password",
        "senha",
        "bank",
        "banco",
        "nubank",
        "pix",
        "token",
        "secret",
    )
    allowed_domains: tuple[str, ...] = field(default_factory=tuple)
    allowed_processes: tuple[str, ...] = field(default_factory=tuple)

    def validate_capture_request(
        self,
        *,
        scope: CaptureScope | str,
        consent: bool,
        region: Region | None = None,
        window_title: str | None = None,
    ) -> PolicyDecision:
        capture_scope = CaptureScope(scope)
        warnings: list[str] = []

        if self.require_user_consent and not consent:
            raise PolicyViolation("Capture blocked: explicit consent is required.")

        if capture_scope == CaptureScope.FULLSCREEN and not self.allow_fullscreen:
            raise PolicyViolation("Capture blocked: fullscreen is disabled by policy.")

        if capture_scope == CaptureScope.WINDOW and not self.allow_window_capture:
            raise PolicyViolation("Capture blocked: window capture is disabled by policy.")

        if capture_scope == CaptureScope.REGION:
            if not self.allow_region_capture:
                raise PolicyViolation("Capture blocked: region capture is disabled by policy.")
            if region is None:
                raise PolicyViolation("Capture blocked: region scope requires a region.")

        if region is not None:
            validate_region(region)

        if window_title:
            normalized = window_title.lower()
            for keyword in self.blocked_window_keywords:
                if keyword.lower() in normalized:
                    raise PolicyViolation(
                        f"Capture blocked: window title contains sensitive keyword: {keyword!r}."
                    )

        if capture_scope == CaptureScope.BROWSER_PAGE:
            warnings.append("browser_page scope requires a browser adapter provided by the caller.")

        return PolicyDecision(
            allowed=True,
            scope=capture_scope.value,
            reason="allowed",
            warnings=warnings,
        )


def validate_region(region: Region) -> None:
    x, y, width, height = region
    if min(x, y, width, height) < 0 or width <= 0 or height <= 0:
        raise PolicyViolation("Capture blocked: invalid region.")


def validate_capture_request(
    policy: CapturePolicy,
    *,
    scope: CaptureScope | str,
    consent: bool,
    region: Region | None = None,
    window_title: str | None = None,
) -> PolicyDecision:
    return policy.validate_capture_request(
        scope=scope,
        consent=consent,
        region=region,
        window_title=window_title,
    )
