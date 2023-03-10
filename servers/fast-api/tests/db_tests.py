import os
import unittest
from pydapper import connect
from resources import SchemaReader
from security import PasswordUtility
from db import UserRepository
from db import UserEntity

SQLITE_DSN = 'sqlite://unit-test:?cache=shared'


def create_unit_test_database():

    statements = SchemaReader().get_schema_statements()

    with connect(SQLITE_DSN) as cn:
        for statement in statements:
            cn.execute(statement)



class UserRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        create_unit_test_database()

    def tearDown(self):
        os.remove("unit-test")

    def test_add_user(self):

        repo = UserRepository(SQLITE_DSN)

        email = 'somefakeemail@fake.com'
        password = PasswordUtility().get_password_hash('abcZxy456&#!')

        user = UserEntity(None, email, password, 1, 1)

        repo.add_user(user)

        eval_user = repo.getUser('somefakeemail@fake.com')
        print(eval_user)
        self.assertIsNotNone(eval_user)


if __name__ == '__main__':
    unittest.main()
