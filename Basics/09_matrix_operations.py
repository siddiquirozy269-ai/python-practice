"""
==========================================================
              MATRIX OPERATIONS IN PYTHON
==========================================================

This program performs the following matrix operations:

1. Matrix Addition
2. Matrix Subtraction
3. Matrix Transpose
4. Matrix Multiplication

Concepts Used:
- Nested Lists
- Nested Loops
- Functions
- Matrix Indexing

Author : Rozy
Language : Python
==========================================================
"""

# ========================================================
#                 MATRIX INPUT
# ========================================================

rows = int(input("Enter Number of Rows    : "))
columns = int(input("Enter Number of Columns : "))

print("\nEnter Elements of Matrix 1")

matrix1 = []

for r in range(rows):
    row = []

    for col in range(columns):
        num = int(input(f"Element [{r}][{col}] : "))
        row.append(num)

    matrix1.append(row)

print("\nEnter Elements of Matrix 2")

matrix2 = []

for r in range(rows):
    row = []

    for col in range(columns):
        num = int(input(f"Element [{r}][{col}] : "))
        row.append(num)

    matrix2.append(row)


# ========================================================
#               MATRIX ADDITION
# ========================================================

def add_matrix():
    add_result_matrix = []

    for r in range(rows):
        result_row = []

        for col in range(columns):
            result = matrix1[r][col] + matrix2[r][col]
            result_row.append(result)

        add_result_matrix.append(result_row)

    return add_result_matrix


# ========================================================
#              MATRIX SUBTRACTION
# ========================================================

def subtract_matrix():
    subtract_result_matrix = []

    for r in range(rows):
        result_row = []

        for col in range(columns):
            result = matrix1[r][col] - matrix2[r][col]
            result_row.append(result)

        subtract_result_matrix.append(result_row)

    return subtract_result_matrix


# ========================================================
#               MATRIX TRANSPOSE
# ========================================================

def transpose(matrix):
    transpose_result = []

    for col in range(columns):
        row = []

        for r in range(rows):
            row.append(matrix[r][col])

        transpose_result.append(row)

    return transpose_result


# ========================================================
#            MATRIX MULTIPLICATION
# ========================================================

def multiply_matrix():
    multiply_result_matrix = []

    for r in range(rows):
        result_row = []

        for col in range(columns):

            total = 0

            for k in range(columns):
                total += matrix1[r][k] * matrix2[k][col]

            result_row.append(total)

        multiply_result_matrix.append(result_row)

    return multiply_result_matrix


# ========================================================
#                 OUTPUT SECTION
# ========================================================

print("\n" + "=" * 50)
print("              MATRIX OPERATIONS")
print("=" * 50)

print("\nMatrix 1")
for row in matrix1:
    print(row)

print("\nMatrix 2")
for row in matrix2:
    print(row)

print("\nMatrix Addition")
for row in add_matrix():
    print(row)

print("\nMatrix Subtraction")
for row in subtract_matrix():
    print(row)

print("\nTranspose of Matrix 1")
for row in transpose(matrix1):
    print(row)

print("\nTranspose of Matrix 2")
for row in transpose(matrix2):
    print(row)

print("\nMatrix Multiplication")
for row in multiply_matrix():
    print(row)

print("=" * 50)