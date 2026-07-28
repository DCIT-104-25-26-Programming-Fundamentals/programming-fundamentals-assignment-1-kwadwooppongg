# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Returns the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    return calculate_sum(numbers) / len(numbers)


def calculate_max(numbers):
    """Returns the maximum value in a list of numbers."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calculate_min(numbers):
    """Returns the minimum value in a list of numbers."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def main():
    n_input = input("How many numbers? ")

    try:
        n = int(n_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        value_input = input(f"Enter number {i}: ")
        try:
            value = float(value_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)

    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:.1f}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()
