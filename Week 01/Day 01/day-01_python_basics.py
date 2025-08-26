"""
Day 1: Python Basics - Master Guide
Date: 2025-08-25

This file covers the most fundamental Python concepts in detail,
with explanations, examples, and practice exercises.
"""

# ======================================================
# 1. The print() Function
# ======================================================
# print() is used to display output to the console.
# Common parameters:
# - sep: Separator between values (default is space)
# - end: What to print at the end (default is newline '\n')
# - file: Where to print (default is sys.stdout which is the console)
# - flush: Whether to forcibly flush the stream (default is False)

print("Hello", "World", sep="-", end="!\n")   # Output: Hello-World!
print("Python", "is", "fun", sep=" | ", end="\n\n")

# f-strings (modern and recommended for formatting):
name = "Nihar"
age = 18
print(f"My name is {name} and I am {age} years old.\n")

# ======================================================
# 2. Variables and Data Types
# ======================================================
# Python is dynamically typed. You don’t declare types explicitly.

# Integer
a = 10
print("a:", a, type(a))

# Float
b = 3.14
print("b:", b, type(b))

# String
c = "Hello Python"
print("c:", c, type(c))

# Boolean
is_active = True
print("is_active:", is_active, type(is_active))

# NoneType (represents “nothing” or “no value”)
d = None
print("d:", d, type(d), "\n")

# ======================================================
# 3. Basic Operators
# ======================================================
x = 7
y = 3

# Arithmetic Operators (+, -, *, /, //, %, **)
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)     # float division
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponent:", x ** y, "\n")

# Assignment Operators (=, +=, -=, *=, /=, etc.)
z = 5
z += 2  # z = z + 2
print("z after += 2:", z, "\n")

# Comparison Operators (==, !=, >, <, >=, <=)
print("Is x equal to y?", x == y)
print("Is x not equal to y?", x != y)
print("Is x greater than y?", x > y, "\n")

# Logical Operators (and, or, not)
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True, "\n")

# Bitwise Operators (operate on binary representation)
print("Bitwise AND (5 & 3):", 5 & 3)
print("Bitwise OR (5 | 3):", 5 | 3)
print("Bitwise XOR (5 ^ 3):", 5 ^ 3)
print("Bitwise NOT (~5):", ~5)
print("Left Shift (5 << 1):", 5 << 1)
print("Right Shift (5 >> 1):", 5 >> 1, "\n")

# ======================================================
# 4. Type Casting (Type Conversion)
# ======================================================
num1 = "10"
num2 = "20"
print("String concatenation:", num1 + num2)  # 1020

# Explicit conversion
num1 = int(num1)
num2 = int(num2)
print("Integer addition:", num1 + num2)  # 30

# Converting back to string
num1 = str(num1)
print("num1 is:", num1, type(num1))

# More examples
print(float("3.5"))   # 3.5
print(bool(0))        # False
print(bool(123))      # True
print(bool(""))       # False (empty string)
print(bool("Hi"))     # True (non-empty string), "\n")

# ======================================================
# 5. Order of Operations (PEMDAS)
# ======================================================
# Parentheses > Exponents > Multiplication/Division > Addition/Subtraction
result = 2 + 3 * 4 ** 2 / 8 - 1
print("Order of operations result:", result, "\n")

# ======================================================
# 6. Input from Users
# ======================================================
# Always returns a string
x = input("Enter a number (string): ")
print("x:", x, type(x))

# Convert to integer
y = int(input("Enter a number (int): "))
print("y:", y, type(y))

# f-string with input
user = input("Enter your name: ")
print(f"Welcome, {user}!\n")

# ======================================================
# 7. Useful Built-in Functions
# ======================================================
# id() - memory address of an object
n = 5
print("Memory address of n:", id(n))

# len() - length of a sequence
print("Length of 'Python':", len("Python"))

# type() - type of a variable
print("Type of 3.14:", type(3.14))

# help() - documentation (useful but prints a lot)
# Uncomment to try: help(print)

print("\n")

# ======================================================
# 8. Comments and Docstrings
# ======================================================
# Single-line comment: starts with #
# Multi-line comment: use """ or ''' (actually multi-line strings, not real comments)

"""
This is a multi-line docstring.
It can describe modules, classes, or functions.
"""

# ======================================================
# 9. Practice Exercises (Try These!)
# ======================================================
# 1. Print your name, age, and city using f-strings.
# 2. Take two numbers as input and print their sum, difference, product, and quotient.
# 3. Convert a string "50" into an integer, add 25, and print the result.
# 4. Write a program that asks for a number and prints whether it’s greater than 100.
# 5. Use bitwise operators to show the result of 6 & 2, 6 | 2, and 6 ^ 2.
# 6. Write a program that asks the user for a sentence and prints its length.
# 7. Explore the difference between == and is using small examples.

# End of Day 1 Master Guide
