"""Packaging and cleanup must preserve the user's repository and local state."""
import importlib.util
import tempfile
import time
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectToolTests(unittest.TestCase):
    def test_packaging_is_flat_and_excludes_local_state(self):
        package = load_script("package_project").package
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = {"Makefile": "make", "src/main.py": "print(1)", ".github/workflows/tests.yml": "ci",
                     ".git/config": "history", ".venv/bin/python": "local", ".aws/credentials": "local",
                     "src/__pycache__/main.pyc": "cache", "archives/old.txt": "old", "_legacy/main.py": "old"}
            for relative, text in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
            target = package(root, root / "dist/project.zip")
            with zipfile.ZipFile(target) as archive:
                self.assertEqual(set(archive.namelist()), {"Makefile", "src/main.py", ".github/workflows/tests.yml"})
                self.assertIsNone(archive.testzip())
                self.assertLessEqual(archive.getinfo("Makefile").date_time[:3], time.gmtime(time.time()-86400)[:3])

    def test_cleanup_keeps_git_environment_and_current_outputs(self):
        cleanup = load_script("cleanup_legacy").cleanup
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = {"Makefile": "make", "pyproject.toml": "project", ".git/config": "git-history",
                     ".venv/bin/python": "environment", ".codex/config": "settings", "outputs/runs/current.json": "new",
                     "src/main.py": "new", "_legacy/old.py": "old", "_legacy/SAE_Optim_2025.pdf": "statement",
                     "archives/old.csv": "old", "requirements-py312-lock.txt": "old-lock",
                     "figure_001.jpg": "old-image", "scripts/run_report_benchmarks.py": "old-script"}
            for relative, text in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
            (root / "report").mkdir()
            removed = cleanup(root)
            self.assertIn("_legacy/", removed)
            self.assertIn("archives/", removed)
            for name in ("_legacy", "archives", "requirements-py312-lock.txt", "figure_001.jpg", "report"):
                self.assertFalse((root / name).exists())
            for name in (".git/config", ".venv/bin/python", ".codex/config", "outputs/runs/current.json", "src/main.py"):
                self.assertEqual((root / name).read_text(), files[name])
            self.assertEqual((root / "docs/enonce_sae.pdf").read_text(), "statement")
            self.assertEqual(cleanup(root), [])

    def test_cleanup_preserves_an_existing_nonempty_report(self):
        cleanup = load_script("cleanup_legacy").cleanup
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Makefile").touch()
            (root / "pyproject.toml").touch()
            (root / "report").mkdir()
            (root / "report/new.tex").write_text("new report")
            cleanup(root)
            self.assertEqual((root / "report/new.tex").read_text(), "new report")

    def test_cleanup_rejects_a_non_project_directory(self):
        cleanup = load_script("cleanup_legacy").cleanup
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                cleanup(Path(tmp))


if __name__ == "__main__":
    unittest.main()
