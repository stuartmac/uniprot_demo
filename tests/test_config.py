import unittest
import os
from uniprot_demo.config import read_config

class TestConfig(unittest.TestCase):

    def test_read_config(self):
        config = read_config()
        self.assertIsNotNone(config)
        self.assertIn("cache_expiration_seconds", config)

    def test_custom_config(self):
        custom_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "custom_config.json")
        os.environ["MY_UNIPROT_MODULE_CONFIG"] = custom_config_path
        config = read_config()
        self.assertIsNotNone(config)
        self.assertIn("cache_expiration_seconds", config)
        self.assertEqual(config["cache_expiration_seconds"], 7200)

if __name__ == "__main__":
    unittest.main()
