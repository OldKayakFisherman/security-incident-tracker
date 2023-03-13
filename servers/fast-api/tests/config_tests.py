import unittest
from config import Settings


class SettingsTestCase(unittest.TestCase):
    def test_settings(self):
        settings = Settings()

        self.assertIsNotNone(settings.get_algorithm())  # add assertion here
        self.assertIsNotNone(settings.get_secret_key())
        self.assertIsNotNone(settings.get_token_expires())


if __name__ == '__main__':
    unittest.main()