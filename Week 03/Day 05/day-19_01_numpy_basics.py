"""
NUMPY BASICS IN PYTHON

NumPy (Numerical Python) is a fundamental library for scientific computing in Python.
It provides support for arrays, matrices, and many mathematical functions to operate on these data structures.
This module introduces basic NumPy concepts and operations for beginners.

Key concepts:
1. Arrays and their creation
2. Basic array operations and attributes
3. Array indexing and slicing
4. Broadcasting and vectorization
5. Basic mathematical operations

NumPy is essential for data analysis, scientific computing, and forms the foundation
for many other data science libraries like pandas, matplotlib, and scikit-learn.
"""

# =====================================================
# 0. INSTALLATION (if needed)
# =====================================================
# To install NumPy, you would typically use pip:
# pip install numpy
#
# For this tutorial, we'll assume NumPy is already installed

# =====================================================
# 1. INTRODUCTION TO NUMPY ARRAYS
# =====================================================
print("=" * 50)
print("1. INTRODUCTION TO NUMPY ARRAYS")
print("=" * 50)

import numpy as np  # Standard convention for importing NumPy

# Creating arrays from Python lists
simple_array = np.array([1, 2, 3, 4, 5])
print(f"Simple array: {simple_array}")
print(f"Type: {type(simple_array)}")

# Multi-dimensional arrays (2D)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array (matrix):\n{matrix}")

# Creating arrays with special values
zeros = np.zeros(5)  # Array of 5 zeros
ones = np.ones((3, 3))  # 3x3 matrix of ones
identity = np.eye(3)  # 3x3 identity matrix

print(f"\nArray of zeros: {zeros}")
print(f"\nMatrix of ones:\n{ones}")
print(f"\nIdentity matrix:\n{identity}")

# Creating sequences
range_array = np.arange(0, 10, 2)  # Start, stop, step
linspace = np.linspace(0, 1, 5)  # Start, stop, num of points

print(f"\nRange array (0 to 10, step 2): {range_array}")
print(f"Linspace (5 evenly spaced points from 0 to 1): {linspace}")

# =====================================================
# 2. ARRAY ATTRIBUTES AND METHODS
# =====================================================
print("\n" + "=" * 50)
print("2. ARRAY ATTRIBUTES AND METHODS")
print("=" * 50)

# Create a sample array
sample = np.array([[1, 2, 3], [4, 5, 6]])

# Basic attributes
print(f"Array dimensions (shape): {sample.shape}")
print(f"Number of dimensions: {sample.ndim}")
print(f"Size (total number of elements): {sample.size}")
print(f"Data type: {sample.dtype}")
print(f"Item size in bytes: {sample.itemsize}")
print(f"Total size in bytes: {sample.nbytes}")

# Basic methods
print(f"\nSum of all elements: {sample.sum()}")
print(f"Min value: {sample.min()}")
print(f"Max value: {sample.max()}")
print(f"Mean value: {sample.mean()}")
print(f"Standard deviation: {sample.std()}")

# Sum by axis
print(f"\nSum of each row (axis=1): {sample.sum(axis=1)}")
print(f"Sum of each column (axis=0): {sample.sum(axis=0)}")

# Reshaping arrays
reshaped = sample.reshape(3, 2)  # Reshape to 3x2 matrix
print(f"\nReshaped array (3x2):\n{reshaped}")

flattened = sample.flatten()  # Convert to 1D array
print(f"\nFlattened array: {flattened}")

# =====================================================
# 3. ARRAY INDEXING AND SLICING
# =====================================================
print("\n" + "=" * 50)
print("3. ARRAY INDEXING AND SLICING")
print("=" * 50)

# Create a sample array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Original array:\n{arr}")

# Single element indexing
print(f"\nElement at row 1, column 2: {arr[1, 2]}")  # Value 7

# Slicing (same as with lists, but works on multiple dimensions)
print(f"\nFirst two rows, all columns:\n{arr[0:2, :]}")
print(f"\nAll rows, last two columns:\n{arr[:, 2:]}")
print(f"\nSubmatrix (rows 1-2, columns 1-3):\n{arr[1:3, 1:4]}")

# Fancy indexing with arrays of indices
row_indices = np.array([0, 2])  # Select rows 0 and 2
col_indices = np.array([1, 3])  # Select columns 1 and 3
print(f"\nSpecific rows {row_indices}:\n{arr[row_indices, :]}")
print(f"\nSpecific columns {col_indices}:\n{arr[:, col_indices]}")
print(f"\nSpecific elements at (row,col) positions (0,1) and (2,3): {arr[row_indices, col_indices]}")

# Boolean masking
mask = arr > 6  # Creates a boolean array of same shape
print(f"\nBoolean mask (arr > 6):\n{mask}")
print(f"\nElements where value > 6:\n{arr[mask]}")

# =====================================================
# 4. ARRAY OPERATIONS
# =====================================================
print("\n" + "=" * 50)
print("4. ARRAY OPERATIONS")
print("=" * 50)

# Basic arithmetic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"\nAddition (a + b): {a + b}")
print(f"Subtraction (b - a): {b - a}")
print(f"Multiplication (a * b): {a * b}")  # Element-wise multiplication
print(f"Division (b / a): {b / a}")
print(f"Power (a ** 2): {a ** 2}")

# With scalars
print(f"\nAdd 5 to all elements in a: {a + 5}")
print(f"Multiply all elements in b by 2: {b * 2}")

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"\nMatrix A:\n{A}")
print(f"Matrix B:\n{B}")

# Matrix multiplication (dot product)
print(f"\nMatrix multiplication (A @ B):\n{A @ B}")
print(f"Matrix multiplication using dot():\n{np.dot(A, B)}")

# Matrix transposition
print(f"\nTranspose of A:\n{A.T}")

# =====================================================
# 5. BROADCASTING
# =====================================================
print("\n" + "=" * 50)
print("5. BROADCASTING")
print("=" * 50)

# Broadcasting allows NumPy to work with arrays of different shapes
# during arithmetic operations

# Example 1: Adding a scalar to an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original array:\n{arr}")
print(f"\nAdd 10 to all elements:\n{arr + 10}")

# Example 2: Operations between arrays of different shapes
row_vector = np.array([1, 2, 3])
print(f"\nRow vector: {row_vector}")
print(f"Adding row vector to each row of the matrix:\n{arr + row_vector}")

# Creating a column vector for demonstration
col_vector = np.array([[10], [20]])
print(f"\nColumn vector:\n{col_vector}")
print(f"Adding column vector to each column of the matrix:\n{arr + col_vector}")

# =====================================================
# 6. PRACTICAL EXAMPLE: TEMPERATURE CONVERSION
# =====================================================
print("\n" + "=" * 50)
print("6. PRACTICAL EXAMPLE: TEMPERATURE CONVERSION")
print("=" * 50)

# Create an array of Celsius temperatures
celsius = np.array([0, 15, 30, 45, 100])
print(f"Celsius temperatures: {celsius}")

# Convert to Fahrenheit: F = C * 9/5 + 32
fahrenheit = celsius * 9/5 + 32
print(f"Fahrenheit temperatures: {fahrenheit}")

# Temperature statistics
print(f"\nAverage Celsius temperature: {celsius.mean():.1f}°C")
print(f"Min temperature: {celsius.min()}°C ({fahrenheit.min():.1f}°F)")
print(f"Max temperature: {celsius.max()}°C ({fahrenheit.max():.1f}°F)")

# =====================================================
# 7. GENERATING RANDOM DATA
# =====================================================
print("\n" + "=" * 50)
print("7. GENERATING RANDOM DATA")
print("=" * 50)

# Set a seed for reproducibility
np.random.seed(42)

# Generate random integers
rand_ints = np.random.randint(1, 100, size=5)  # 5 random integers between 1 and 100
print(f"Random integers: {rand_ints}")

# Generate random floats (uniform distribution)
rand_floats = np.random.random(5)  # 5 random floats between 0 and 1
print(f"Random floats (0-1): {rand_floats}")

# Generate normally distributed random numbers
normal_dist = np.random.normal(loc=0, scale=1, size=5)  # Mean=0, Std=1
print(f"Normal distribution samples: {normal_dist}")

# Generate a random 2D array
rand_matrix = np.random.rand(3, 3)  # 3x3 matrix of random values between 0 and 1
print(f"\nRandom 3x3 matrix:\n{rand_matrix}")

# =====================================================
# 8. SAVING AND LOADING NUMPY ARRAYS
# =====================================================
print("\n" + "=" * 50)
print("8. SAVING AND LOADING NUMPY ARRAYS")
print("=" * 50)

# Creating sample data to save
data_to_save = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Data to save:\n{data_to_save}")

# Save array to .npy file (binary format)
# np.save('my_array.npy', data_to_save)
print("\nArray can be saved to a file with np.save('filename.npy', array)")

# To load the saved array
# loaded_array = np.load('my_array.npy')
print("And loaded with loaded_array = np.load('filename.npy')")

# Save in text format
# np.savetxt('my_array.txt', data_to_save)
print("\nArray can also be saved in text format with np.savetxt('filename.txt', array)")

# To load from text format
# loaded_text_array = np.loadtxt('my_array.txt')
print("And loaded with loaded_array = np.loadtxt('filename.txt')")

# =====================================================
# CONCLUSION
# =====================================================
print("\n" + "=" * 50)
print("CONCLUSION")
print("=" * 50)

print("""
NumPy is a powerful library that forms the foundation of the Python data science ecosystem.
The basics covered in this tutorial include:

1. Creating and manipulating arrays
2. Understanding array attributes and methods
3. Indexing and slicing arrays
4. Performing array operations
5. Understanding broadcasting
6. Working with random data
7. Saving and loading arrays

These fundamentals will help you get started with NumPy and prepare you for 
more advanced topics in data analysis and scientific computing.
""")

# Additional resources
print("\nAdditional Resources:")
print("- NumPy official documentation: https://numpy.org/doc/")
print("- SciPy lectures: https://scipy-lectures.org/")
print("- Python Data Science Handbook by Jake VanderPlas")
