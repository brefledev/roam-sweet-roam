import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PackageVerificationTest(unittest.TestCase):
    def test_missing_native_guide_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="portable-agent-package-") as temp:
            target = Path(temp)
            for name in ("README.md", "SPEC.md", "SETUP.md", "VERIFICATION.md", "LICENSE"):
                shutil.copyfile(ROOT / name, target / name)
            for name in ("surfaces", "templates", "examples", "assets"):
                shutil.copytree(ROOT / name, target / name)
            (target / "surfaces/codex.md").unlink()
            result = subprocess.run([sys.executable, "-B", str(ROOT / "tests/verify_package.py"), str(target)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing or empty package file: surfaces/codex.md", result.stderr)

if __name__ == "__main__":
    unittest.main()
