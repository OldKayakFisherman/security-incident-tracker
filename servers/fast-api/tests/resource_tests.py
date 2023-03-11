import unittest
from resources import SchemaReader, QueryReader


class SchemaReaderTestCases(unittest.TestCase):
    def test_read_schema(self):
        rdr = SchemaReader()
        self.assertTrue(len(rdr.get_schema_statements()) > 0)  # add assertion here

    def test_get_user_table_statement(self):
        rdr = SchemaReader()
        self.assertTrue(len(rdr.get_user_table_statement()) > 0)  # add assertion here

    def test_incident_table_statement(self):
        rdr = SchemaReader()
        self.assertTrue(len(rdr.get_incident_table_statement()) > 0)  # add assertion here


class QueryReaderTestCases(unittest.TestCase):

    def test_get_user_insert_statement(self):
        rdr = QueryReader()
        self.assertIsNotNone(rdr.get_user_insert_statement())

    def test_get_user_by_email_statement(self):
        rdr = QueryReader()
        self.assertIsNotNone(rdr.get_user_by_email_statement())

    def test_get_table_check_statement(self):
        rdr = QueryReader()
        self.assertIsNotNone(rdr.get_table_check_statement())



if __name__ == '__main__':
    unittest.main()
