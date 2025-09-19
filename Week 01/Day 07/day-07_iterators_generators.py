"""
Day 7: Iteration Made Simple (Iterables, Iterators, Generators)
Date: 2025-09-19

Goal: Understand how Python loops work under the hood in simple words.
We keep it light and practical with short examples you can run.
"""

from itertools import islice  # small helper to take a few items from a long sequence

# ======================================================
# 1) What is an Iterable? What is an Iterator?
# ======================================================
# Iterable: something you can loop over (list, tuple, string, range, dict, set).
# Iterator: a helper that gives items one by one when asked.
# You can get an iterator from an iterable by using iter(...). You get the next
# value by using next(...).

nums = [10, 20, 30]           # list is an iterable
it = iter(nums)               # turn iterable into an iterator
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# If you call next() again, there is nothing left, so Python raises StopIteration.
try:
    print(next(it))
except StopIteration:
    print("No more items (the iterator is finished).")
print()

# TIP: for-loops do iter(...) and next(...) for you automatically.
# That's why `for x in nums:` works out of the box.

# ======================================================
# 2) Generators (the easy way to make your own iterator)
# ======================================================
# A generator is just a function that uses `yield` to give values one by one.
# Think of yield as "pause here and give this value, then resume next time".


def countdown(n):
    """Yield n, n-1, ..., 1."""
    while n > 0:
        yield n
        n -= 1

print("countdown from 5:", list(countdown(5)))  # we collect all values into a list

# Another simple generator: all even numbers from 0 up to limit (not included)

def even_upto(limit):
    for x in range(limit):
        if x % 2 == 0:
            yield x

print("even numbers < 10:", list(even_upto(10)))
print()

# IMPORTANT: Some generators can be endless (infinite). Use islice to take only a few.


def naturals():
    i = 1
    while True:   # this never ends on its own
        yield i
        i += 1

print("first 5 natural numbers:", list(islice(naturals(), 5)))  # take 5 only
print()

# ======================================================
# 3) Generator Expressions (short form)
# ======================================================
# Like list comprehensions, but they produce items one by one (no big list in memory).
# Use () instead of [].

even_squares_sum = sum(x * x for x in range(10) if x % 2 == 0)
print("sum of even squares below 10:", even_squares_sum)

# If you do need a list, just wrap with list(...)
triples = list(3 * x for x in range(5))
print("triples as a list:", triples)
print()

# ======================================================
# 4) When to use these?
# ======================================================
# - Use a normal list/for-loop for small data.
# - Use generators when you want to stream values or save memory.
# - Use iter()/next() only if you need step-by-step control (rare in daily code).

# ======================================================
# 5) Practice (try yourself)
# ======================================================
# 1) Make a generator that yields the first N Fibonacci numbers.
# 2) Make a generator expression that gives cubes of odd numbers < 20.
# 3) Use islice with naturals() to get the first 10 multiples of 3.
# 4) Explain in your own words: iterable vs iterator (1–2 lines).

# ======================================================
# End of Day 7 - Iteration (Beginner)
# ======================================================
