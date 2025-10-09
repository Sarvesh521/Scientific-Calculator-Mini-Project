import unittest
from calculator import square_root, factorial

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertIsNone(square_root(-1))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertIsNone(factorial(-1))
        self.assertIsNone(factorial(1.5))

    def test_natural_log(self):
        self.assertEqual(natural_log(1), 0)
        self.assertAlmostEqual(natural_log(math.e), 1)
        self.assertIsNone(natural_log(0))
        self.assertIsNone(natural_log(-5))