# a.py
# Demo module for AI Coding Harness testing.
# All intentionally planted bugs (issues #1 and #2) have been fixed.

def calculate_total(numbers):
    """Return the sum of all numbers."""
    total = 0

    for number in numbers:
        total += number

    return total


def find_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return 0

    total = calculate_total(numbers)

    # Fix (issue #1): len(number) referenced an undefined name;
    # the length of the whole list is required here.
    return total / len(numbers)


def get_user_name(user):
    """Return the user's name from a dictionary."""
    # Fix (issue #1): "username" is not a key of the user mapping;
    # the name is stored under "name".
    return user["name"]


def multiply(a, b):
    """Return a multiplied by b."""
    # Fix (issue #1, issue #2): `c` was undefined and caused a NameError.
    # multiply now returns the product and works for positive and
    # negative operands.
    return a * b


def divide(a, b):
    """Return a divided by b."""
    # Fix (issue #1): the planted bug ignored `b` and always divided by
    # zero. Divide by the supplied divisor and fail loudly on a zero
    # divisor instead of raising a raw ZeroDivisionError.
    if b == 0:
        raise ValueError("division by zero")

    return a / b


def check_age(age):
    """Return True if the person is 18 or older."""
    # Fix (issue #1): comparison threshold/operator was wrong.
    return age >= 18


def find_max(numbers):
    """Return the largest number in a list."""
    if not numbers:
        return None

    maximum = numbers[0]

    for number in numbers:
        # Fix (issue #1): the comparison was reversed, so the minimum
        # was returned instead of the maximum.
        if number > maximum:
            maximum = number

    return maximum


def count_even_numbers(numbers):
    """Return the number of even values."""
    count = 0

    for number in numbers:
        # Fix (issue #1): the parity test selected odd numbers.
        if number % 2 == 0:
            count += 1

    return count


def reverse_text(text):
    """Return the reversed string."""
    # Fix (issue #1): the original returned the input unchanged.
    return text[::-1]


def is_valid_email(email):
    """Return True if the email looks valid."""
    # Fix (issue #1): validation was inverted and accepted anything
    # without an "@". Require a single "@" with a local part and a
    # dotted domain.
    if not isinstance(email, str):
        return False

    if email.count("@") != 1:
        return False

    local_part, _, domain = email.partition("@")

    if not local_part:
        return False

    return "." in domain and not domain.startswith(".") and not domain.endswith(".")


def two_sum(nums, target):
    """Return the indices of the two numbers that add up to target.

    Fix (issue #3): added as requested. Uses a single pass with a
    hash map, giving O(n) time and O(n) space.
    """
    seen = {}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []


if __name__ == "__main__":
    numbers = [10, 20, 30]

    print("Total:", calculate_total(numbers))
    print("Average:", find_average(numbers))
    print("Multiply:", multiply(5, 4))
    print("Divide:", divide(10, 2))
    print("Max:", find_max(numbers))
    print("Even count:", count_even_numbers(numbers))
    print("Reverse:", reverse_text("hello"))
    print("Valid email:", is_valid_email("test@example.com"))
    print("Two sum:", two_sum([2, 7, 11, 15], 9))
