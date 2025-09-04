"""
Day 4: Mastering Python Lists - Complete Guide
Date: 2025-09-03

This file covers Python lists, their operations, methods, comprehension, and additional useful tips.
"""

import copy

# ======================================================
# 1. Introduction to Lists
# ======================================================
# Lists are ordered, mutable collections of items.
# Items can be of any type (int, str, float, another list, etc.)

my_list = [10, 20, 30, "Python", [1, 2, 3]]
print("Original list:", my_list)
print("Type of my_list:", type(my_list))
print()

# ======================================================
# 2. Access List Items
# ======================================================
# Indexing and slicing work similar to strings.

print("First item:", my_list[0])
print("Last item:", my_list[-1])
print("Slice [1:4]:", my_list[1:4])
print("Nested list item:", my_list[4][1])
print()

# ======================================================
# 3. Change List Items
# ======================================================
# Lists are mutable, so we can change values.

my_list[1] = 25
print("After changing index 1:", my_list)

# Changing a slice
my_list[2:4] = [35, "Java"]
print("After changing slice [2:4]:", my_list)
print()

# ======================================================
# 4. Add List Items
# ======================================================
# Append, insert, and extend are commonly used.

my_list.append("New Item")  # Add at the end
print("After append:", my_list)

my_list.insert(1, "Inserted")  # Add at a specific index
print("After insert at index 1:", my_list)

my_list.extend([50, 60, 70])  # Add multiple items
print("After extend:", my_list)
print()

# ======================================================
# 5. Remove List Items
# ======================================================
# Remove items by value or index, and clear the entire list.

my_list.remove("Java")  # Remove by value
print("After remove 'Java':", my_list)

popped_item = my_list.pop(2)  # Remove by index and return it
print("Popped item:", popped_item)
print("After pop:", my_list)

del my_list[0]  # Delete by index
print("After del index 0:", my_list)

# Clear all items
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear():", temp_list)
print()

# ======================================================
# 6. Looping Through Lists
# ======================================================
# Using for, while, and list comprehensions.

colors = ["red", "green", "blue"]

# Using for loop
for color in colors:
    print("Color:", color)

# Using while loop
i = 0
while i < len(colors):
    print("While loop:", colors[i])
    i += 1
print()

# ======================================================
# 7. List Comprehension (Powerful Python Feature)
# ======================================================
# Concise way to create lists.

squares = [x ** 2 for x in range(6)]
print("Squares:", squares)

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)
print()

# Inline conditional in comprehension
[print(x, end=",") if x % 2 == 0 else print(f"{x} is odd", end=", ") for x in squares]
print("\n")

# ======================================================
# 8. Sort Lists
# ======================================================
numbers = [5, 2, 9, 1, 7]

# Sort ascending
numbers.sort()
print("Sorted ascending:", numbers)

# Sort descending
numbers.sort(reverse=True)
print("Sorted descending:", numbers)


# Sort by custom key (absolute difference from 5)
def myfunc(n):
    return abs(n - 5)


numbers.sort(key=myfunc)
print("Sorted by distance from 5:", numbers)
print()

# ======================================================
# 9. Copy Lists
# ======================================================
original = [1, 2, 3]
# Using copy()
copy1 = original.copy()
# Using list()
copy2 = list(original)
print("Original:", original)
print("Copy using copy():", copy1)
print("Copy using list():", copy2)
print()

# ======================================================
# 10. Join Lists
# ======================================================
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

# Using + operator
joined1 = list1 + list2
print("Joined with + :", joined1)

# Using extend()
list1.extend(list2)
print("Joined with extend():", list1)
print()

# ======================================================
# 11. Useful List Methods (Extras)
# ======================================================
nums = [5, 3, 8, 6, 3]

print("Count of 3:", nums.count(3))  # Count occurrences
print("Index of 8:", nums.index(8))  # First occurrence
nums.reverse()
print("Reversed list:", nums)
print()

# ======================================================
# 12. Nested Lists & Access
# ======================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("Element [1][2]:", matrix[1][2])  # 6
print()

# ======================================================
# 13. Practice Exercises
# ======================================================
# 1. Find max and min in a list (basic aggregation)
numbers = [4, 7, 1, 9, 0]
print("Max:", max(numbers))  # Largest value in the list
print("Min:", min(numbers))  # Smallest value in the list

# 2. Filter even numbers using list comprehension (conditional filtering)
even_numbers = [n for n in numbers if n % 2 == 0]  # Only even numbers
print("Even numbers:", even_numbers)

# 3. Flatten a nested list (list comprehension with two loops)
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]  # Unpack all sublist into one list
print("Flattened list:", flat)

# 4. Remove duplicates (set conversion, order not preserved)
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(dup_list))
# Fastest way, but order is lost because sets are unordered and doesn't allow duplicates
print("Unique list (unordered):", unique_list)
# Ordered way (preserves first occurrence)
unique_ordered = []
for x in dup_list:
    if x not in unique_ordered:
        unique_ordered.append(x)
print("Unique list (ordered):", unique_ordered)

unique = []
[unique.append(x) for x in dup_list if x not in unique]

# 5. Sum of all elements (aggregation)
print("Sum:", sum(numbers))  # Adds all elements

# 6. List slicing (step, reverse, copy)
# Slicing: [start:stop:step]
print("Slice [1:4]:", numbers[1:4])  # Elements from index 1 to 3
print("Every second element:", numbers[::2])  # Step of 2
print("Reversed:", numbers[::-1])  # Reverse the list

# 7. List unpacking (assigning multiple variables at once)
a, b, *rest = numbers  # a=4, b=7, rest=[1,9,0]
print("a:", a, "b:", b, "rest:", rest)

# 8. Enumerate in loops (get index and value)
for idx, val in enumerate(numbers):
    print(f"Index {idx} has value {val}")

# ======================================================
# 14. More List Tips & Edge Cases
# ======================================================
# Negative indices in slicing (count from end)
print("Last two elements:", numbers[-2:])  # [-2] is second last

# List multiplication (quickly create repeated lists)
zeros = [0] * 5
print("List of five zeros:", zeros)

# Deleting a slice (batch removal)
del numbers[1:3]  # Removes elements at index 1 and 2
print("After deleting slice [1:3]:", numbers)

# Unpacking edge cases
try:
    a, b = [1]  # Not enough values
except ValueError as e:
    print("Unpacking error (too few values):", e)
try:
    a, b = [1, 2, 3]  # Too many values
except ValueError as e:
    print("Unpacking error (too many values):", e)

# zip() for parallel iteration
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
for num, char in zip(list_a, list_b):
    print(f"Pair: {num} and {char}")


# Shallow copy vs deep copy (with nested lists)
nested_list = [[1, 2], [3, 4]]
shallow = nested_list.copy()
deep = copy.deepcopy(nested_list)
nested_list[0][0] = 99  # Change original
print("After modifying nested_list:")
print("Original:", nested_list)
print("Shallow copy:", shallow)
# Also changed (shares inner lists) (if it was just a flat list, it would be independent)
print("Deep copy:", deep)
# Unchanged (fully independent)
