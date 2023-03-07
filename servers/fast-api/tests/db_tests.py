import unittest
from pydapper import connect
from resources import read_schema_resource
def create_in_memory_database(self):

    cn = connect("file::memory:?cache=shared")
    cn.execute(read_schema_resource())
    return cn
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
