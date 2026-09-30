"""Tests for a.py.

Covers the fixes for issues #1 and #2 and the two_sum function
requested in issue #3.
"""

import unittest

from a import (
    calculate_total,
    check_age,
    count_even_numbers,
    divide,
    find_average,
    find_max,
    get_user_name,
    is_valid_email,
    multiply,
    reverse_text,
    two_sum,
)


class TestTwoSum(unittest.TestCase):
    """Issue #3: two_sum(nums, target)."""

    def test_example_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_duplicate_values(self):
        # Additional case: the two addends are equal.
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), [0, 2])

    def test_no_solution_returns_empty_list(self):
        self.assertEqual(two_sum([1, 2, 3], 100), [])

    def test_empty_input(self):
        self.assertEqual(two_sum([], 5), [])


class TestMultiply(unittest.TestCase):
    """Issue #2: multiply must return a * b."""

    def test_positive_numbers(self):
        self.assertEqual(multiply(5, 4), 20)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-3, 7), -21)

    def test_two_negatives(self):
        self.assertEqual(multiply(-3, -7), 21)

    def test_zero(self):
        self.assertEqual(multiply(0, 9), 0)


class TestIssueOneBugs(unittest.TestCase):
    """Issue #1: the remaining planted bugs."""

    def test_calculate_total(self):
        self.assertEqual(calculate_total([10, 20, 30]), 60)
        self.assertEqual(calculate_total([]), 0)

    def test_find_average_uses_list_length(self):
        # Previously raised NameError: name 'number' is not defined.
        self.assertEqual(find_average([10, 20, 30]), 20)
        self.assertEqual(find_average([1, 2]), 1.5)

    def test_find_average_empty_list(self):
        self.assertEqual(find_average([]), 0)

    def test_get_user_name_uses_valid_key(self):
        # Previously raised KeyError: 'username'.
        self.assertEqual(get_user_name({"name": "Alice", "age": 30}), "Alice")

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_check_age_boundary(self):
        self.assertTrue(check_age(18))
        self.assertTrue(check_age(30))
        self.assertFalse(check_age(17))

    def test_find_max(self):
        self.assertEqual(find_max([10, 20, 30]), 30)
        self.assertEqual(find_max([-5, -1, -9]), -1)
        self.assertIsNone(find_max([]))

    def test_count_even_numbers(self):
        self.assertEqual(count_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(count_even_numbers([1, 3, 5]), 0)

    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")
        self.assertEqual(reverse_text(""), "")

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("test.example.com"))
        self.assertFalse(is_valid_email("test@@example.com"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("test@example"))


if __name__ == "__main__":
    unittest.main()
