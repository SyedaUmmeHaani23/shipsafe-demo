import unittest
from calculator import add, get_user


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_public_get_user_api(self):
        user = get_user("u1")
        self.assertEqual(user["id"], "u1")
        self.assertEqual(user["timeout"], 30)


if __name__ == "__main__":
    unittest.main()
