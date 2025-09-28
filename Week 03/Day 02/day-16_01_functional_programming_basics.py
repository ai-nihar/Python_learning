"""
====================================================
PYTHON FUNCTIONAL PROGRAMMING BASICS - DAY 16
====================================================

Functional programming is a programming paradigm where programs are constructed by
applying and composing functions. Python supports a functional programming style
while remaining multi-paradigm.

This file covers:
- First-class functions
- Pure functions
- Lambda expressions
- Higher-order functions
- Built-in functional tools (map, filter, reduce)
"""

print("PYTHON FUNCTIONAL PROGRAMMING BASICS")
print("=" * 50)

# =====================================================
# First-Class Functions
# =====================================================
# In Python, functions are first-class citizens, which means they can be:
# - Assigned to variables
# - Passed as arguments to other functions
# - Returned from other functions
# - Stored in data structures

print("\nFIRST-CLASS FUNCTIONS:")
print("-" * 30)

def greet(name):
    """A simple greeting function."""
    return f"Hello, {name}!"

# Assigning function to a variable
greeting_func = greet
print(f"Function assigned to variable: {greeting_func('Alice')}")  # Output: Hello, Alice!

# Storing functions in data structures
function_list = [greet, str.upper, len]
print("Calling functions from a list:")
for func in function_list:
    # Using the function stored in the list
    if func == greet:
        print(f"  {func.__name__}: {func('Bob')}")
    elif func == str.upper:
        print(f"  {func.__name__}: {func('hello')}")
    else:
        print(f"  {func.__name__}: {func('hello')}")

# Passing function as an argument
def execute_function(func, value):
    """Execute the given function with the value."""
    return func(value)

print(f"Passing function as argument: {execute_function(len, 'hello')}")  # 5

# =====================================================
# Pure Functions
# =====================================================
# A pure function:
# - Always returns the same output for the same input
# - Has no side effects (doesn't modify external state)
# - Doesn't depend on external state

print("\nPURE FUNCTIONS:")
print("-" * 30)

# Example of a pure function
def add(x, y):
    """Pure function that adds two numbers."""
    return x + y

print(f"Pure function add(5, 3): {add(5, 3)}")

# Example of an impure function with side effects
counter = 0
def increment_counter(amount):
    """Impure function that modifies external state."""
    global counter
    counter += amount
    return counter

print(f"Before calling impure function, counter = {counter}")
increment_counter(5)
print(f"After calling impure function, counter = {counter}")

# Benefits of pure functions:
# - Easier to test and debug
# - Can be cached (memoized) for performance
# - Thread-safe (no shared state)
# - Often more readable and maintainable

# =====================================================
# Lambda Expressions
# =====================================================
# Lambda expressions are small anonymous functions defined with the lambda keyword

print("\nLAMBDA EXPRESSIONS:")
print("-" * 30)

# Simple lambda function
square = lambda x: x**2
print(f"Lambda function square(4): {square(4)}")

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(f"Lambda function multiply(3, 4): {multiply(3, 4)}")

# Lambda with conditional expression
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"Lambda function is_even(7): {is_even(7)}")
print(f"Lambda function is_even(8): {is_even(8)}")

# Immediate invocation of lambda
print(f"Immediate lambda invocation: {(lambda x, y: x + y)(10, 20)}")

# When to use lambdas:
# - Simple operations where defining a full function is overkill
# - Functions that are used only once (especially as arguments)
# - Short transformations in functional programming operations

# =====================================================
# Higher-Order Functions
# =====================================================
# Functions that accept other functions as arguments or return functions

print("\nHIGHER-ORDER FUNCTIONS:")
print("-" * 30)

# Function that takes a function as an argument
def apply_twice(func, value):
    """Apply the given function twice to the value."""
    return func(func(value))

# Using with a regular function
def double(x):
    return x * 2

print(f"apply_twice(double, 3): {apply_twice(double, 3)}")  # 3 -> 6 -> 12

# Using with a lambda
print(f"apply_twice(lambda x: x + 1, 5): {apply_twice(lambda x: x + 1, 5)}")  # 5 -> 6 -> 7

# Function that returns a function (closure)
def make_multiplier(factor):
    """Return a function that multiplies by the given factor."""
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"double(7): {double(7)}")  # 14
print(f"triple(7): {triple(7)}")  # 21

# =====================================================
# Built-in Functional Tools: map()
# =====================================================
# map() applies a function to all items in an input list

print("\nMAP FUNCTION:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]

# Using map with a regular function
squares = list(map(double, numbers))
print(f"map(double, {numbers}): {squares}")

# Using map with lambda
cubes = list(map(lambda x: x**3, numbers))
print(f"map(lambda x: x**3, {numbers}): {cubes}")

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"map(lambda x, y: x + y, {list1}, {list2}): {sums}")

# =====================================================
# Built-in Functional Tools: filter()
# =====================================================
# filter() constructs an iterator from elements that satisfy a condition

print("\nFILTER FUNCTION:")
print("-" * 30)

# Using filter with a regular function
def is_even_func(x):
    return x % 2 == 0

even_numbers = list(filter(is_even_func, numbers))
print(f"filter(is_even_func, {numbers}): {even_numbers}")

# Using filter with lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"filter(lambda x: x % 2 != 0, {numbers}): {odd_numbers}")

# Using filter with None (removes falsy values)
mixed_values = [0, 1, False, True, "", "hello", None, [], [1, 2]]
truthy_values = list(filter(None, mixed_values))
print(f"filter(None, {mixed_values}): {truthy_values}")

# =====================================================
# Built-in Functional Tools: reduce()
# =====================================================
# reduce() applies a function cumulatively to the items of an iterable
# It's part of the functools module in Python 3

print("\nREDUCE FUNCTION:")
print("-" * 30)

from functools import reduce

# Sum of all numbers
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"reduce(lambda x, y: x + y, {numbers}): {sum_result}")

# Product of all numbers
product_result = reduce(lambda x, y: x * y, numbers)
print(f"reduce(lambda x, y: x * y, {numbers}): {product_result}")

# Finding maximum value
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"reduce(lambda x, y: x if x > y else y, {numbers}): {max_value}")

# =====================================================
# Simple Practical Example
# =====================================================
print("\nSIMPLE PRACTICAL EXAMPLE:")
print("-" * 30)

# Sample data: Student records (name, grade)
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 72},
    {'name': 'Charlie', 'grade': 90},
    {'name': 'David', 'grade': 65},
    {'name': 'Eva', 'grade': 88},
]

# Get names of students who passed (grade >= 70)
passed_students = list(map(
    lambda student: student['name'],
    filter(lambda student: student['grade'] >= 70, students)
))
print(f"Students who passed: {passed_students}")

# Calculate average grade using functional approach
total_grade = reduce(lambda total, student: total + student['grade'], students, 0)
average_grade = total_grade / len(students)
print(f"Average grade: {average_grade:.2f}")

# List comprehension alternative (for comparison)
passed_students_comp = [student['name'] for student in students if student['grade'] >= 70]
print(f"Students who passed (using comprehension): {passed_students_comp}")

print("\n" + "=" * 50)
