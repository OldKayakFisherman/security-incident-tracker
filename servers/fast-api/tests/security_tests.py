import unittest
from security import PasswordUtility, TokenUtility


class PasswordUtilityTestCase(unittest.TestCase):
    def testVerifyPassword(self):
        passutil = PasswordUtility()
        original_password = "MySuperSecretPasspassword123!"
        encrypted_password = passutil.get_password_hash(original_password)
        self.assertNotEqual(original_password, encrypted_password)
        self.assertTrue(passutil.verify_password(original_password, encrypted_password))

    def testGetPasswordHash(self):
        passutil = PasswordUtility()
        original_password = "MySuperSecretPasspassword123!"
        encrypted_password = passutil.get_password_hash(original_password)
        self.assertNotEqual(original_password, encrypted_password)


class TokenUtilityTestCase(unittest.TestCase):

    def testCreateAccessToken(self):

        token = TokenUtility().create_access_token({})
        self.assertTrue(token is not None)


if __name__ == '__main__':
    unittest.main()
