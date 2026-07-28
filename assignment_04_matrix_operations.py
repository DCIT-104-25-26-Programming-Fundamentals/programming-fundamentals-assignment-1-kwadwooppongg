# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
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
