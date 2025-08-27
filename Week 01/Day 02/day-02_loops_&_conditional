"""
Day 2: Python Control Flow - Master Guide
Date: 2025-08-26

This file covers Python control flow concepts in detail,
with explanations, examples, and practice exercises.
"""

# ======================================================
# 1. Conditional Statements (if, elif, else)
# ======================================================
# Used to make decisions in code based on conditions.

# Basic if statement
num = 7
if num > 5:
    print("num is greater than 5")

# if-else statement
if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")

# if-elif-else chain
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# Nested if statements
age = 20
if age >= 18:
    print("Adult")
    if age >= 65:
        print("Senior citizen")
    else:
        print("Not a senior citizen")
else:
    print("Minor")

# Short-hand if (ternary operator)
x = 10
y = 20
min_value = x if x < y else y
# format: variable = value_if_true if condition else value_if_false
print(f"Minimum is {min_value}")

# Logical operators in conditions
n = 15
if n > 10 and n < 20: # can be simplified to 10 < n < 20
    print("n is between 10 and 20")

# Best practices:
# - Use indentation (4 spaces per level, no tabs)
# - Keep conditions simple and readable
# - Use elif for multiple branches
# - Avoid deeply nested ifs when possible

# Common mistakes:
# - Don't forget the colon ':' at the end of if/elif/else lines
# - Indentation errors are common for beginners

# Practice Exercise:
# Write a program to check if a number is positive, negative, or zero.
num = -3
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# ======================================================
# 2. Loops (while, for)
# ======================================================
# Used to repeat actions multiple times.

# 2.1 while loop
count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1

# Using break to exit a loop early
n = 1
while True:
    print(n)
    if n == 3:
        break  # Exit loop when n is 3
    n += 1

# for loop syntax
for i in range(1, 6):  # 1 to 5
    print(i)

# if only 1 value is passed, it starts from 0
for i in range(5):  # 0 to 4
    print(i)

# Using continue to skip to the next iteration
for i in range(1, 6):
    if i == 3:
        continue  # Skip printing 3
    print(i)

# pass is a placeholder (does nothing)
for i in range(3):
    pass  # Useful when you need a block syntactically but don't want to do anything yet

# 2.2 for loop
# Using range()
for i in range(1, 6):
    print(f"i = {i}")

# Iterating over a string
s = "Python"
for char in s:
    print(char)

# Iterating over a list
lst = [10, 20, 30]
for item in lst:
    print(item)

# Looping with index (using enumerate) (basically, it is used to get index and value both)
for idx, val in enumerate(lst):
    print(f"Index {idx}: Value {val}")

# Looping over a dictionary
my_dict = {"a": 1, "b": 2}
for key, value in my_dict.items():
    print(f"{key} => {value}")

# Best practices:
# - Use for loop for known number of iterations, while for unknown
# - Avoid infinite loops unless intentional
# - Use descriptive variable names
# - Use break/continue judiciously

# Common pitfalls:
# - Off-by-one errors in range() [start, end) inclusive-exclusive
# - Forgetting to update loop variables in while loops
# - Accidentally creating infinite loops

# ======================================================
# 3. Loop Control Statements (break, continue, pass)
# ======================================================
# break: Exit the nearest enclosing loop
# continue: Skip the rest of the current loop iteration
# pass: Do nothing (placeholder)

# Example: break
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print()

# Example: continue
for i in range(1, 6):
    if i == 2:
        continue
    print(i, end=" ")
print()

# Example: pass
for i in range(3):
    pass  # No operation

# ======================================================
# 4. Practice Patterns and Exercises
# ======================================================
# 1. Print numbers 1–10
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Sum of first N numbers
N = 5
sum_n = 0
for i in range(1, N+1):
    sum_n += i
print(f"Sum of first {N} numbers is {sum_n}")

# 3. Simple star pattern
rows = 4
for i in range(1, rows+1):
    print("*" * i) # here * multiplied by i means print * i times

# 4. Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 5. Print the reverse of a string
s = "Python"
print(s[1:3])
print(s[::-1])  # Slicing to reverse the string
# format: string[start:end:step] (if step is negative, it reverses the string)

# 6. Nested loop: Multiplication table (1 to 3)
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

# ======================================================
# 5. Challenge Exercises (Try These!)
# ======================================================
# 1. Write a program to find the factorial of a number using a loop.
# 2. Print all prime numbers between 1 and 50.
# 3. Print a pyramid star pattern for a given number of rows.
# 4. Write a program to count vowels in a string.
# 5. Print the Fibonacci sequence up to N terms.
# 6. Write a program to check if a string is a palindrome.

# End of Day 2 Master Guide
