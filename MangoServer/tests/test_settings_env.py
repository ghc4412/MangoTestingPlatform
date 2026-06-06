import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.settings.env import env_bool, env_int, load_env_file


class SettingsEnvTestCase(unittest.TestCase):
    def test_load_env_file_does_not_override_existing_environment(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            env_file = Path(tmpdir) / ".env.local"
            env_file.write_text(
                "MYSQL_IP=file-db\n"
                "MYSQL_PASSWORD=file-password\n"
                "QUOTED_VALUE='quoted value'\n"
                "COMMENTED=value # comment\n",
                encoding="utf-8",
            )

            with patch.dict(os.environ, {"MYSQL_IP": "system-db"}, clear=False):
                loaded = load_env_file(env_file)

                self.assertTrue(loaded)
                self.assertEqual(os.environ["MYSQL_IP"], "system-db")
                self.assertEqual(os.environ["MYSQL_PASSWORD"], "file-password")
                self.assertEqual(os.environ["QUOTED_VALUE"], "quoted value")
                self.assertEqual(os.environ["COMMENTED"], "value")

    def test_env_bool_and_env_int_convert_strings_safely(self):
        with patch.dict(os.environ, {"IS_MINIO": "true", "MYSQL_PORT": "3307"}, clear=False):
            self.assertTrue(env_bool("IS_MINIO", False))
            self.assertEqual(env_int("MYSQL_PORT", 3306), 3307)

        with patch.dict(os.environ, {"IS_MINIO": "0", "MYSQL_PORT": "invalid"}, clear=False):
            self.assertFalse(env_bool("IS_MINIO", True))
            self.assertEqual(env_int("MYSQL_PORT", 3306), 3306)


if __name__ == "__main__":
    unittest.main()
