# a.py
# This file intentionally contains bugs for AI Coding Harness testing.

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

    # Intentional bug:
    # wrong variable name
    return total / len(number)


def get_user_name(user):
    """Return the user's name from a dictionary."""
    # Intentional bug:
    # wrong dictionary key
    return user["username"]


def multiply(a, b):
    """Return a multiplied by b."""
    return a * b


def divide(a, b):
    """Return a divided by b."""
    # Intentional bug:
    # ignores b and always divides by zero
    return a / 0


def check_age(age):
    """Return True if the person is 18 or older."""
    # Intentional bug:
    # incorrect comparison
    return age > 21


def find_max(numbers):
    """Return the largest number in a list."""
    if not numbers:
        return None

    maximum = numbers[0]

    for number in numbers:
        # Intentional bug:
        # comparison is reversed
        if number < maximum:
            maximum = number

    return maximum


def count_even_numbers(numbers):
    """Return the number of even values."""
    count = 0

    for number in numbers:
        # Intentional bug:
        # checks odd instead of even
        if number % 2 != 0:
            count += 1

    return count


def reverse_text(text):
    """Return the reversed string."""
    # Intentional bug:
    return text


def is_valid_email(email):
    """Return True if the email looks valid."""
    # Intentional bug:
    # incorrect validation
    return "@" not in email


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