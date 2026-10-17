"""Remove only the explicitly obsolete project paths, preserving local state."""
from __future__ import annotations

from pathlib import Path
import shutil

OBSOLETE_DIRECTORIES = ("_legacy", "archives")
OBSOLETE_FILES = ("requirements-py312-lock.txt", "figure_001.jpg", "scripts/run_report_benchmarks.py")


def cleanup(root: Path) -> list[str]:
    root = root.resolve()
    if not (root / "pyproject.toml").is_file() or not (root / "Makefile").is_file():
        raise ValueError("Expected the root of the Ring-Star project.")
    # Preserve the source statement when the script is used before extraction.
    old_statement = root / "_legacy/SAE_Optim_2025.pdf"
    statement = root / "docs/enonce_sae.pdf"
    if old_statement.is_file() and not statement.exists():
        statement.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(old_statement, statement)
    removed = []
    for name in OBSOLETE_FILES:
        path = root / name
        if path.is_file() or path.is_symlink():
            path.unlink()
            removed.append(name)
    for name in OBSOLETE_DIRECTORIES:
        path = root / name
        if path.is_symlink():
            path.unlink()
            removed.append(name)
        elif path.is_dir():
            shutil.rmtree(path)
            removed.append(name + "/")
    report = root / "report"
    if report.is_dir() and not report.is_symlink() and not any(report.iterdir()):
        report.rmdir()
        removed.append("report/ (vide)")
    return removed


def main() -> int:
    removed = cleanup(Path(__file__).resolve().parents[1])
    print("Supprimé : " + ", ".join(removed) if removed else "Aucun fichier obsolète présent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
