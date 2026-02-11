

import numpy as np

# =========================
# Task 1 (10 Marks)
# =========================

print("----- Task 1 -----")

# Create 1D array of 15 random integers (1–50)
array1 = np.random.randint(1, 51, 15)

print("Array:", array1)

# Compute statistics
print("Sum:", np.sum(array1))
print("Mean:", np.mean(array1))
print("Min:", np.min(array1))
print("Max:", np.max(array1))
print("Standard Deviation:", np.std(array1))


# =========================
# Task 2 (10 Marks)
# =========================

print("\n----- Task 2 -----")

# Create 4x4 matrix
matrix = np.random.randint(1, 10, (4, 4))

print("Matrix:\n", matrix)

# Determinant
det = np.linalg.det(matrix)
print("Determinant:", det)

# Transpose
print("Transpose:\n", matrix.T)

# Inverse (check if determinant not zero)
if det != 0:
    print("Inverse:\n", np.linalg.inv(matrix))
else:
    print("Matrix is not invertible (Determinant = 0)")


# =========================
# Task 3 (10 Marks)
# =========================

print("\n----- Task 3 -----")

# Generate 10 random numbers
original = np.random.randint(1, 100, 10)

print("Original Array:", original)

# Shuffle array
shuffled = original.copy()
np.random.shuffle(shuffled)

print("Shuffled Array:", shuffled)
