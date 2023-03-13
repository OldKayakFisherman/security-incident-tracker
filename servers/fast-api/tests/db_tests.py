import os
import unittest
from pydapper import connect
from resources import SchemaReader
from security import PasswordUtility
from db import UserRepository, UserEntity, DatabaseUtilities


SQLITE_DSN = 'sqlite://unit-test:?cache=shared'

"""
def create_unit_test_database():

    statements = SchemaReader().get_schema_statements()

    with connect(SQLITE_DSN) as cn:
        for statement in statements:
            cn.execute(statement)

"""


class UserRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        DatabaseUtilities(SQLITE_DSN).ensure_created()

    def tearDown(self):
        DatabaseUtilities(SQLITE_DSN).ensure_destroyed('unit-test')

    def test_add_user(self):

        repo = UserRepository(SQLITE_DSN)

        email = 'somefakeemail@fake.com'
        password = PasswordUtility().get_password_hash('abcZxy456&#!')

        user = UserEntity(None, email, password, 1, 1)

        repo.add_user(user)

        eval_user = repo.getUser('somefakeemail@fake.com')
        print(eval_user)
        self.assertIsNotNone(eval_user)


class DatabaseUtilitiesTestCase(unittest.TestCase):

    def test_does_table_exist(self):
        du = DatabaseUtilities(SQLITE_DSN)

        self.assertFalse(du.does_table_exist("users"))
        self.assertFalse(du.does_table_exist("incidents"))

        du.ensure_created()

        self.assertTrue(du.does_table_exist("users"))
        self.assertTrue(du.does_table_exist("incidents"))

    def tearDown(self):
        DatabaseUtilities(SQLITE_DSN).ensure_destroyed('unit-test')


if __name__ == '__main__':
    unittest.main()
