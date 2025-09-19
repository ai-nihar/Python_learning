"""
Day 7: Functions in Plain English (Beginner)
Date: 2025-09-19

Goal: Learn how to make and use functions with simple words and examples.
We focus on the basics you will use every day.
"""

# ======================================================
# 1) What is a function?
# ======================================================
# A function is a small block of code you can reuse.
# You call it with inputs, it can give back an output (return value).


def greet(name):
    """Make a hello message for the given name."""
    return f"Hello, {name}!"

print(greet("Nihar"))

# A function can return more than one thing by using a tuple (just commas)

def min_max(values):
    return min(values), max(values)

low, high = min_max([3, 8, 1, 5])
print("min:", low, "max:", high)
print()

# ======================================================
# 2) Parameters (inputs): positional, keyword, defaults
# ======================================================
# - Positional: order matters
# - Keyword: name=value, order doesn’t matter
# - Default: value used when you don’t pass that argument


def power(base, exp=2):
    """Raise base to exp. If exp is not given, use 2 (square)."""
    return base ** exp

print(power(3))              # uses the default exp=2 -> 9
print(power(2, 5))           # positional -> 32
print(power(base=4, exp=3))  # keywords -> 64
print(power(exp=4, base=2))  # keyword order can change -> 16
print()

# ======================================================
# 3) Extra arguments: *args and **kwargs (easy idea)
# ======================================================
# *args = extra positional numbers (packed into a tuple)
# **kwargs = extra named options (packed into a dict)


def summarize(title, *numbers, **options):
    total = sum(numbers)
    count = len(numbers)
    sep = options.get("sep", " - ")
    end = options.get("end", "\n")
    print(title, f"count={count}", f"sum={total}", sep=sep, end=end)

summarize("Stats", 1, 2, 3, 4, sep=" | ")
print()

# ======================================================
# 4) Unpacking with * and ** when calling
# ======================================================
# You can spread a tuple/list into arguments with *
# You can spread a dict into named arguments with **

params = (2, 10)
print("power(*params):", power(*params))   # same as power(2, 10)

kwargs = {"base": 3, "exp": 3}
print("power(**kwargs):", power(**kwargs))  # same as power(base=3, exp=3)

# Star in assignment (grab the middle as a list)
head, *mid, tail = [10, 20, 30, 40, 50]
print("head:", head, "mid:", mid, "tail:", tail)
print()

# ======================================================
# 5) Docstrings and Type Hints (nice to have)
# ======================================================
# - A docstring explains what your function does (triple quotes under def)
# - Type hints show the expected types (they don’t enforce at runtime)


def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b

print("add(2, 5):", add(2, 5))
print("annotations:", add.__annotations__)
print()

# ======================================================
# 6) Tiny lambda (optional)
# ======================================================
# A lambda is a very small one-line function.
# Use normal def for anything more than a quick one-liner.

square = lambda x: x * x
print("square(6):", square(6))
print()

# ======================================================
# 7) Prefer simple tools first
# ======================================================
# - Write clear functions with def
# - Use default values to make calls easy
# - Use *args/**kwargs when you really need “extra inputs”
# - Use list comprehensions over map/filter for readability (for now)

# ======================================================
# 8) Practice
# ======================================================
# 1) Write mean(a, b, c) that returns the average of three numbers.
# 2) Write describe(name, age=18) that prints a short message.
# 3) Write total(*nums) that returns the sum of any count of numbers.
# 4) Write greet_many(*names, sep=", ") that prints names joined by sep.
# 5) Try a tiny lambda: last_char = lambda s: s[-1]

# ======================================================
# End of Day 7 - Functions (Beginner)
# ======================================================
