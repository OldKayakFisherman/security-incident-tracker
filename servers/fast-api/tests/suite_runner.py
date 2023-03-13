import unittest


if __name__ == '__main__':
    from config_tests import SettingsTestCase
    from security_tests import *
    from db_tests import *
    from resource_tests import *

    suite1 = unittest.TestLoader().loadTestsFromTestCase(SettingsTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(PasswordUtilityTestCase)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TokenUtilityTestCase)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(UserRepositoryTestCase)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(DatabaseUtilitiesTestCase)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(SchemaReaderTestCases)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(QueryReaderTestCases)

    master_suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6, suite7])

    unittest.TextTestRunner(verbosity=2).run(master_suite)
