import unittest
from tests.test_reg1 import test_reg1
from tests.test_registration2 import test_registration2


class MyTestCase(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(test_reg1(), 'AssertionError: OK')  # add assertion here

    def test_registration2(self):
        self.assertEqual(test_registration2(), False)


if __name__ == '__main__':
    unittest.main()
