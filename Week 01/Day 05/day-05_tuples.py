"""
Day 5: Mastering Python Tuples - Complete Guide
Date: 2025-09-04

This file covers Python tuples, their properties, operations, methods,
and real-world usage examples. Includes explanations, code snippets,
and exercises for practice.
"""

# ======================================================
# 1. Introduction to Tuples
# ======================================================
# Tuples are ordered, immutable collections of items.
# They can store different data types (int, str, float, etc.).
# Tuples are defined using parentheses ().

example_tuple = (10, "apple", 3.14, True)
print("Example tuple:", example_tuple)
print("Type of tuple:", type(example_tuple))

# Single element tuple requires a following comma:
single_tuple = ("hello",)
print("Single-element tuple:", single_tuple)

# ======================================================
# 2. Accessing Tuples
# ======================================================
# Tuples allow indexing and slicing like lists.

numbers = (10, 20, 30, 40, 50)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice (index 1 to 3):", numbers[1:4])

# ======================================================
# 3. Updating Tuples (Immutability)
# ======================================================
# Tuples are immutable: you cannot directly change elements.
# Attempting direct modification -> ERROR
# numbers[0] = 99   # ❌ Not allowed

# Workaround: Convert to list, modify, then convert back to tuple
# This is a common way to "update" a tuple
# (Tuples themselves cannot be changed)
temp_list = list(numbers)
temp_list[0] = 99
numbers = tuple(temp_list)
print("Updated tuple:", numbers)

# ======================================================
# 4. Unpacking Tuples
# ======================================================
# Tuples can be unpacked into variables for easy access.
person = ("Nihar", 19, "India")
(name, age, country) = person
print(f"Name: {name}, Age: {age}, Country: {country}")

# Using * operator for extended unpacking (captures middle values)
fruits = ("apple", "banana", "cherry", "mango")
(first, *middle, last) = fruits
print("First:", first)  # First element
print("Middle:", middle)  # All elements except first/last
print("Last:", last)  # Last element

# ======================================================
# 5. Looping Through Tuples
# ======================================================
# You can loop through tuples with for or while loops.
animals = ("dog", "cat", "rabbit")
print("For loop:")
for a in animals:
    print(a)

print("While loop:")
i = 0
while i < len(animals):
    print(animals[i])
    i += 1

# ======================================================
# 6. Joining & Repeating Tuples
# ======================================================
# Tuples can be concatenated (+) or repeated (*)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined = tuple1 + tuple2
print("Joined tuple:", joined)

repeated = tuple1 * 3
print("Repeated tuple:", repeated)

# ======================================================
# 7. Tuple Methods
# ======================================================
# Tuples support two built-in methods: count() and index()
nums = (1, 2, 3, 2, 2, 4, 5)
print("Count of 2:", nums.count(2))  # frequency of value
print("Index of 4:", nums.index(4))  # first occurrence (throws error if not found)

# ======================================================
# 8. Tuple vs List (Key Differences)
# ======================================================
# Tuples are immutable, lists are mutable
# Tuples use (), lists use []
# Tuples can be used as dictionary keys, lists cannot
# Tuples are generally faster and safer for fixed data

# Example: Tuple as dictionary key
locations = {
    (19.07, 72.87): "Mumbai",
    (28.61, 77.20): "Delhi"
}
print("Location at (28.61, 77.20):", locations[(28.61, 77.20)])

# ======================================================
# 9. Nested Tuples
# ======================================================
# Tuples can contain other tuples (useful for matrices, etc.)
nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("First inner tuple:", nested[0])

# ======================================================
# 10. Tuple Conversion & Built-in Functions
# ======================================================
# Convert list to tuple, tuple to list
sample_list = [1, 2, 3]
sample_tuple = tuple(sample_list)
print("List to tuple:", sample_tuple)
print("Tuple to list:", list(sample_tuple))

# Built-in functions: len, min, max, sum
numbers = (10, 20, 30, 40, 50)
print("Length:", len(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))


# ======================================================
# 11. Real-World Examples
# ======================================================
# Example 1: Returning multiple values from a function
def min_max(values):
    return (min(values), max(values))  # returns a tuple


print("Min and Max:", min_max([3, 7, 1, 9, 4]), type(min_max([3, 7, 1, 9, 4])))

# Example 2: Coordinates (immutable data is safer for fixed values)
point = (12.5, 7.8)
print("Point coordinates:", point)

# ======================================================
# 12. Exercises for Practice (With Solutions)
# ======================================================
# Exercise 1: Create a tuple of 5 favorite movies and print the second one.
movies = ("Inception", "Interstellar", "The Matrix", "Shutter Island", "Avengers")
print("Second movie:", movies[1])  # Indexing starts at 0

# Exercise 2: Unpack a tuple of 3 values into variables and print them.
colors = ("red", "green", "blue")
(c1, c2, c3) = colors
print("Colors:", c1, c2, c3)

# Exercise 3: Count how many times 'apple' appears in a tuple.
fruit_basket = ("apple", "banana", "apple", "cherry", "apple")
print("Apple count:", fruit_basket.count("apple"))


# Exercise 4: Write a function that takes a tuple of numbers and returns their sum and average as a tuple.
# functions are yet to be covered, so ignore if this is confusing
def sum_and_avg(nums):
    total = sum(nums)
    avg = total / len(nums)
    return (total, avg)


print("Sum and Average:", sum_and_avg((10, 20, 30, 40)))

# ======================================================
# 13. Advanced Tuple Features
# ======================================================
# Named Tuples: Tuples with named fields for readability (from collections)
from collections import namedtuple

# Define a named tuple type called 'Person'
Person = namedtuple('Person', ['name', 'age', 'country'])
# if you are familiar with java/OOP then this can be treated like a class with attributes but is immutable like a tuple

# Create a named tuple instance
person1 = Person(name='Alice', age=25, country='USA')
print("NamedTuple - Name:", person1.name)  # Access by name
print("NamedTuple - Age:", person1.age)
print("NamedTuple - Country:", person1.country)

print("NamedTuple: ", person1) # Full representation

# Named tuples are still immutable and behave like regular tuples
print("NamedTuple as tuple:", tuple(person1))

# Using zip() to pair elements from two tuples
names = ("John", "Jane", "Jim")
ages = (22, 24, 21)
paired = tuple(zip(names, ages))  # Each pair is a tuple
# used tuple() to convert zip object to tuple (otherwise it would be a zip object which is an iterator)
print("Paired tuples (name, age):", paired)

# Using enumerate() to get index and value from a tuple
for idx, value in enumerate(movies):
    print(f"Movie #{idx + 1}: {value}")

# Nested unpacking: Unpack tuples inside tuples
nested_pair = ((1, 'a'), (2, 'b'), (3, 'c'))
for number, letter in nested_pair:
    print(f"Number: {number}, Letter: {letter}")

# Generator expressions with tuple: Convert to tuple for immutability
squares = tuple(x * x for x in range(5))
print("Tuple of squares:", squares)

# ======================================================
# End of Day 5
# ======================================================
