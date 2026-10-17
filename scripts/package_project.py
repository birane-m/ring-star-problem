"""Build a flat ZIP with source, tests and results, excluding local state."""
from __future__ import annotations

import argparse
from pathlib import Path
import time
import zipfile

EXCLUDED = {".git", ".venv", "venv", "env", "__pycache__", ".matplotlib-cache",
            ".pytest_cache", ".mypy_cache", ".ruff_cache", "build", "dist",
            ".aws", ".agents", ".codex", "_legacy", "archives"}


def package(root: Path, output: Path) -> Path:
    root, output = root.resolve(), output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(root.rglob("*")):
            relative = path.relative_to(root)
            if not path.is_file() or path.is_symlink() or path.resolve() == output:
                continue
            if any(part in EXCLUDED or part.endswith(".egg-info") for part in relative.parts):
                continue
            if path.suffix in {".pyc", ".pyo"}:
                continue
            # A conservative UTC date avoids Make warnings on extraction.
            stamp = time.gmtime(min(path.stat().st_mtime, time.time() - 86400))[:6]
            info = zipfile.ZipInfo(relative.as_posix(), date_time=stamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"Invalid archive member: {bad}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("dist/ring-star.zip"))
    args = parser.parse_args()
    print(package(Path(__file__).resolve().parents[1], args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
