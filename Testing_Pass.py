import unittest

from DemoFile import mul


class TestAdd(unittest.TestCase):
    def test_simple(self):
        a = 20
        b = 30
        c = mul(a, b)
        self.assertEqual(c, a*b)

    def test_medium(self):
        a = 12325
        b = 985278
        c = mul(a, b)
        self.assertEqual(c, a*b)

    def test_hard(self):
        a = 3457778.896745
        b = 5756632.214379
        c = mul(a, b)
        self.assertEqual(c, a*b)


if __name__ == "__main__":
    unittest.main()