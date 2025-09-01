"""
Day 3: Pattern Printing with Loops - Master Guide
Date: 2025-09-01

This file covers classic pattern printing problems using loops in Python.
"""

# ======================================================
# 1. Square Pattern
# ======================================================
n = int(input("Enter number of rows: "))
print("\nSquare Pattern:")
for i in range(n):
    print("*" * n)

# ======================================================
# 2. Right-Angled Triangle (Increasing)
# ======================================================
print("\nRight-Angled Triangle (Increasing):")
for i in range(n):
    print("*" * (i + 1))

# ======================================================
# 3. Right-Angled Triangle (Decreasing)
# ======================================================
print("\nRight-Angled Triangle (Decreasing):")
for i in range(n):
    print("*" * (n - i))

# ======================================================
# 4. Left-Aligned Triangle (Increasing)
# ======================================================
print("\nLeft-Aligned Triangle (Increasing):")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))

# ======================================================
# 5. Left-Aligned Triangle (Decreasing)
# ======================================================
print("\nLeft-Aligned Triangle (Decreasing):")
for i in range(n):
    print(" " * i + "*" * (n - i))

# ======================================================
# 6. Hourglass Pattern
# ======================================================
print("\nHourglass Pattern:")
for i in range(2 * n):
    if i < n:
        print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))
    else:
        print("*" * (i - n + 1) + " " * (2 * (2 * n - i - 1)) + "*" * (i - n + 1))

# ======================================================
# 7. Diamond Pattern
# ======================================================
print("\nDiamond Pattern:")
# Upper part (including center)
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1) + "*" * i)
# Lower part
for i in range(1, n):
    print(" " * i + "*" * (n - i) + "*" * (n - i - 1))

# ======================================================
# 8. Butterfly Pattern (Classic)
# ======================================================
print("\nButterfly Pattern (Classic):")
# Upper half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
# Lower half
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# ======================================================
# Practice Exercises
# ======================================================
# 1. Print a hollow square pattern.
# 2. Print a number pyramid.
# 3. Print a right-angled triangle with numbers instead of stars.
# 4. Print a pattern of your choice!
