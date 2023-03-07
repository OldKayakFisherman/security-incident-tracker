import unittest
from resources import read_schema_resource


class ResourceTestCases(unittest.TestCase):
    def test_read_schema(self):
        self.assertIsNotNone(read_schema_resource())  # add assertion here


if __name__ == '__main__':
    unittest.main()
