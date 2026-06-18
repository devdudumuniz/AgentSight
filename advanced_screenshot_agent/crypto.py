from __future__ import annotations

from pathlib import Path

from cryptography.fernet import Fernet


def generate_key() -> bytes:
    return Fernet.generate_key()


def encrypt_file(path: Path, key: bytes, output_path: Path | None = None) -> Path:
    output_path = output_path or path.with_suffix(path.suffix + ".enc")
    data = path.read_bytes()
    output_path.write_bytes(Fernet(key).encrypt(data))
    return output_path


def decrypt_file(path: Path, key: bytes, output_path: Path) -> Path:
    data = path.read_bytes()
    output_path.write_bytes(Fernet(key).decrypt(data))
    return output_path
