import unittest
from calculator import square_root
class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertIsNone(square_root(-1))