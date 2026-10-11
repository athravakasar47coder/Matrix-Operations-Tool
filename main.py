import numpy as np


# Function to input a matrix
def input_matrix(rows, cols):
    matrix = []

    print("Enter matrix elements:")

    for i in range(rows):
        row = list(map(float, input().split()))

        while len(row) != cols:
            print("Please enter", cols, "values.")
            row = list(map(float, input().split()))

        matrix.append(row)

    return np.array(matrix)


# Input first matrix
print("===== MATRIX OPERATIONS TOOL =====")

rows1 = int(input("Enter rows of Matrix A: "))
cols1 = int(input("Enter columns of Matrix A: "))

print("\nMatrix A")
A = input_matrix(rows1, cols1)


# Input second matrix
rows2 = int(input("\nEnter rows of Matrix B: "))
cols2 = int(input("Enter columns of Matrix B: "))

print("\nMatrix B")
B = input_matrix(rows2, cols2)


# Display matrices
print("\n===== MATRIX A =====")
print(A)

print("\n===== MATRIX B =====")
print(B)


# Addition
if A.shape == B.shape:
    print("\n===== ADDITION =====")
    print(A + B)
else:
    print("\nAddition not possible.")
    print("Both matrices must have the same dimensions.")


# Subtraction
if A.shape == B.shape:
    print("\n===== SUBTRACTION =====")
    print(A - B)
else:
    print("\nSubtraction not possible.")
    print("Both matrices must have the same dimensions.")


# Multiplication
if cols1 == rows2:
    print("\n===== MULTIPLICATION =====")
    print(A @ B)
else:
    print("\nMultiplication not possible.")
    print("Columns of Matrix A must equal rows of Matrix B.")


# Transpose
print("\n===== TRANSPOSE OF MATRIX A =====")
print(A.T)

print("\n===== TRANSPOSE OF MATRIX B =====")
print(B.T)


# Determinant
if rows1 == cols1:
    print("\n===== DETERMINANT OF MATRIX A =====")
    print(round(np.linalg.det(A), 2))
else:
    print("\nDeterminant of Matrix A not possible.")
    print("Matrix A must be square.")


if rows2 == cols2:
    print("\n===== DETERMINANT OF MATRIX B =====")
    print(round(np.linalg.det(B), 2))
else:
    print("\nDeterminant of Matrix B not possible.")
    print("Matrix B must be square.")


print("\n===== OPERATION COMPLETED =====")