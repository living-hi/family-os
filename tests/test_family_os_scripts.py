import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INIT = ROOT / "skill" / "scripts" / "family_os_init.py"
CHECK = ROOT / "skill" / "scripts" / "family_os_check.py"
STATUS = ROOT / "skill" / "scripts" / "family_os_status.py"


class FamilyOsScriptTests(unittest.TestCase):
    def run_cmd(self, *args, env=None):
        merged_env = os.environ.copy()
        if env:
            merged_env.update(env)
        return subprocess.run(args, text=True, capture_output=True, check=True, env=merged_env)

    def test_initializes_chinese_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "workspace"
            config = Path(tmp) / "config.yaml"
            result = self.run_cmd(str(INIT), "--workspace", str(workspace), "--config", str(config), "--language", "zh-CN")

            self.assertIn("language: zh", result.stdout)
            self.assertIn("language: zh", config.read_text(encoding="utf-8"))
            self.assertIn("家庭工作区", (workspace / "README.md").read_text(encoding="utf-8"))
            self.assertTrue((workspace / "01-dashboard" / "household-overview.md").exists())

            check = self.run_cmd(str(CHECK), "--workspace", str(workspace))
            self.assertIn("missing: 0", check.stdout)

    def test_auto_language_uses_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "workspace"
            config = Path(tmp) / "config.yaml"
            config.write_text("workspace: /tmp/old\nlanguage: es-MX\n", encoding="utf-8")

            self.run_cmd(str(INIT), "--workspace", str(workspace), "--config", str(config), "--language", "auto")

            self.assertIn("language: es", config.read_text(encoding="utf-8"))
            self.assertIn("Espacio de Family OS", (workspace / "README.md").read_text(encoding="utf-8"))

    def test_status_reports_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "workspace"
            config = Path(tmp) / "config.yaml"
            self.run_cmd(str(INIT), "--workspace", str(workspace), "--config", str(config), "--language", "en")

            project = workspace / "03-projects" / "demo-project"
            project.mkdir()
            (project / "README.md").write_text("# Demo Project\n", encoding="utf-8")

            status = self.run_cmd(str(STATUS), "--workspace", str(workspace), "--lines", "3")
            self.assertIn("projects: 1", status.stdout)
            self.assertIn("Family OS Status", status.stdout)


if __name__ == "__main__":
    unittest.main()
