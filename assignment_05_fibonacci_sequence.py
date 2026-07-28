# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="matrix"):
    """Reads a matrix of given size from the user, one row per line."""
    print(f"Enter {name} values:")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"Error: Expected {cols} values, got {len(row_input)}. Try again.")
                continue
            try:
                row = [float(val) for val in row_input]
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue
            matrix.append(row)
            break
    return matrix


def display_matrix(matrix):
    """Displays a matrix in a neat, aligned grid format."""
    if not matrix:
        print("(empty matrix)")
        return
    widths = [max(len(format_num(matrix[r][c])) for r in range(len(matrix)))
              for c in range(len(matrix[0]))]
    for row in matrix:
        formatted_row = [format_num(val).rjust(widths[c]) for c, val in enumerate(row)]
        print(" ".join(formatted_row))


def format_num(val):
    """Formats a number without unnecessary decimal points."""
    if val == int(val):
        return str(int(val))
    return str(val)


def transpose_matrix(matrix):
    """Returns the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b):
    """Returns the element-wise sum of two matrices of the same size."""
    rows = len(a)
    cols = len(a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b):
    """Returns the matrix product of A (MxN) and B (NxP)."""
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


def get_positive_int(prompt):
    """Reads a positive integer from the user."""
    while True:
        value = input(prompt)
        try:
            n = int(value)
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue
        if n <= 0:
            print("Error: Value must be a positive integer.")
            continue
        return n


def part_a():
    print("\n--- Part A: Transpose a Matrix ---")
    rows = get_positive_int("Enter number of rows: ")
    cols = get_positive_int("Enter number of columns: ")
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)


def part_b():
    print("\n--- Part B: Add Two Matrices ---")
    rows = get_positive_int("Enter number of rows: ")
    cols = get_positive_int("Enter number of columns: ")

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols, "matrix A")
    print("\nMatrix B:")
    matrix_b = read_matrix(rows, cols, "matrix B")

    result = add_matrices(matrix_a, matrix_b)
    print("\nSum:")
    display_matrix(result)


def part_c():
    print("\n--- Part C: Multiply Two Matrices ---")
    m = get_positive_int("Enter rows of Matrix A (M): ")
    n = get_positive_int("Enter columns of Matrix A / rows of Matrix B (N): ")
    p = get_positive_int("Enter columns of Matrix B (P): ")

    print("\nMatrix A:")
    matrix_a = read_matrix(m, n, "matrix A")
    print("\nMatrix B:")
    matrix_b = read_matrix(n, p, "matrix B")

    result = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct (A x B):")
    display_matrix(result)


def main():
    part_a()
    part_b()
    part_c()


if __name__ == "__main__":
    main()
