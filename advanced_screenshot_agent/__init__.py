"""Advanced Screenshot Agent.

Camada local-first para captura visual segura em agentes de IA.
"""

from .evidence import EvidenceEvent, EvidenceRun
from .policy import CapturePolicy


def capture_screen(*args, **kwargs):
    from .capture import capture_screen as _capture_screen

    return _capture_screen(*args, **kwargs)


def __getattr__(name: str):
    if name == "CaptureConfig":
        from .capture import CaptureConfig

        return CaptureConfig
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "CapturePolicy",
    "EvidenceEvent",
    "EvidenceRun",
    "CaptureConfig",
    "capture_screen",
]
