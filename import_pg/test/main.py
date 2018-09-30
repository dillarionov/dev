import unittest

from import_pg.custom_class import CustomClass


class CustomClassTest(unittest.TestCase):
    def setUp(self):
        self.custom_object = CustomClass()

    def test_custom_object(self):
        self.assertEqual(self.custom_object.sum(2, 3), 5)


if __name__ == '__main__':
    unittest.main()