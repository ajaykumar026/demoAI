# test_multiply.py
# Tests for multiply() - covers the requirements in issue #2.

import unittest

from a import multiply


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(5, 4), 20)

    def test_negative_by_positive(self):
        self.assertEqual(multiply(-3, 7), -21)

    def test_negative_by_negative(self):
        self.assertEqual(multiply(-3, -7), 21)

    def test_with_zero(self):
        self.assertEqual(multiply(0, 10), 0)

    def test_is_commutative(self):
        self.assertEqual(multiply(6, 9), multiply(9, 6))

    def test_floats(self):
        self.assertAlmostEqual(multiply(1.5, 2), 3.0)


if __name__ == "__main__":
    unittest.main()
