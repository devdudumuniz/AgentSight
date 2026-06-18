from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class CapturePolicy:
    """Política de segurança para captura visual.

    Ideia central: o agente não decide sozinho o que pode capturar.
    A política é o firewall da visão. Sem isso, vira Recall caseiro, e aí a LGPD
    chega com um café amargo.
    """

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

    def validate_capture_request(
        self,
        *,
        fullscreen: bool,
        window_title: str | None,
        region: tuple[int, int, int, int] | None,
        consent: bool,
    ) -> None:
        if self.require_user_consent and not consent:
            raise PermissionError("Captura bloqueada: consentimento explícito ausente.")

        if fullscreen and not self.allow_fullscreen:
            raise PermissionError("Captura fullscreen bloqueada pela política.")

        if window_title and not self.allow_window_capture:
            raise PermissionError("Captura de janela bloqueada pela política.")

        if region is not None and not self.allow_region_capture:
            raise PermissionError("Captura por região bloqueada pela política.")

        if window_title:
            normalized = window_title.lower()
            for keyword in self.blocked_window_keywords:
                if keyword.lower() in normalized:
                    raise PermissionError(
                        f"Captura bloqueada: janela contém palavra sensível: {keyword!r}"
                    )

        if region is not None:
            x, y, width, height = region
            if min(x, y, width, height) < 0 or width == 0 or height == 0:
                raise ValueError("Região inválida para captura.")
