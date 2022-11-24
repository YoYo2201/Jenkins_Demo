import unittest

from DemoFile import mul


class TestAdd(unittest.TestCase):
    def test_fail_simple(self):
        a = 20
        b = 30
        c = mul(a, b)
        self.assertEqual(c, -50)

    def test_fail_medium(self):
        a = 3489871
        b = 6216789
        c = mul(a, b)
        self.assertEqual(c, 100)


if __name__ == "__main__":
    unittest.main()