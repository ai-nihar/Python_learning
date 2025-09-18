"""
Day 6: Mastering Python Sets - Complete Guide
Date: 2025-09-18

This file covers Python sets: creation, properties, core operations,
methods, set algebra, comprehensions, frozenset, and common patterns.
Includes concise explanations, pitfalls, and mini exercises.
"""

# ======================================================
# 1) Introduction to Sets
# ======================================================
# A set is an unordered collection of unique, hashable elements.
# Key facts:
# - Unordered: no index-based access (can't do s[0])
# - Unique: duplicates are removed automatically
# - Elements must be hashable (immutable types like int, str, tuple OK; list/dict NOT OK)

# Ways to create a set
empty_set = set()                 # Correct way to create an empty set ({} is an empty dict)
nums = {1, 2, 3, 3, 2, 1}         # Duplicates collapse
print("Set from literal:", nums)  # Order may differ across runs
print("Empty set type:", type(empty_set))

# From iterables (e.g., list/tuple/string)
from_list = set([1, 2, 2, 3])
from_str = set("banana")          # Unique letters
print("From list:", from_list)
print("From string (unique chars):", from_str)
print()

# ======================================================
# 2) Core Set Operations (Algebra)
# ======================================================
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A:", A)
print("B:", B)

# Union (elements in A or B)
print("A | B (union):", A | B)
print("A.union(B):", A.union(B))

# Intersection (elements in both)
print("A & B (intersection):", A & B)
print("A.intersection(B):", A.intersection(B))

# Difference (elements in A, but not in B)
print("A - B (difference):", A - B)
print("B - A (difference):", B - A)

# Symmetric Difference (in A or B but not both)
print("A ^ B (symmetric diff):", A ^ B)
print()

# Relationship checks
print("A <= B (subset?):", A <= B)          # True if A is subset of B
print("A.issubset(B):", A.issubset(B))
print("A >= B (superset?):", A >= B)
print("A.isdisjoint(B):", A.isdisjoint(B))  # True if no common elements
print()

# ======================================================
# 3) Mutating Methods (in-place)
# ======================================================
s = {1, 2}
print("Start:", s)

s.add(3)                      # Add single element
print("after add(3):", s)

s.update([3, 4, 5])           # Add multiple items from iterable
print("after update([3,4,5]):", s)

s.remove(5)                   # Remove 5; KeyError if not present
print("after remove(5):", s)

s.discard(99)                 # Remove if present; NO error if missing
print("after discard(99):", s)

popped = s.pop()              # Remove and return an arbitrary element
print("popped:", popped, "remaining:", s)

s.clear()                     # Remove all elements
print("after clear():", s)
print()

# In-place algebra variants
X = {1, 2, 3, 4}
Y = {3, 4, 5}
X_copy = X.copy()

X_copy |= Y                   # In-place union
print("|= result:", X_copy)

X_copy = X.copy(); X_copy &= Y
print("&= result:", X_copy)

X_copy = X.copy(); X_copy -= Y
print("-= result:", X_copy)

X_copy = X.copy(); X_copy ^= Y
print("^= result:", X_copy)
print()

# ======================================================
# 4) Set Comprehensions
# ======================================================
# Build sets concisely with conditions.
squares = {n * n for n in range(10)}
print("Squares set:", squares)

even_cubes = {n ** 3 for n in range(20) if n % 2 == 0}
print("Even cubes:", even_cubes)
print()

# ======================================================
# 5) Common Use-Cases & Patterns
# ======================================================
# 5.1) Deduplicate a list fast (order not guaranteed)
raw = [3, 1, 2, 3, 2, 1, 4]
unique_fast = set(raw)
print("Dedup (unordered):", unique_fast)

# 5.2) Deduplicate while preserving first occurrence order
# Use dict.fromkeys (dict preserves insertion order in Python 3.7+)
unique_ordered = list(dict.fromkeys(raw))
print("Dedup (preserve order):", unique_ordered)

# 5.3) Membership tests are O(1) average (fast containment checks)
allowed = {"read", "write"}
print("has 'read'?:", "read" in allowed)
print("has 'delete'?:", "delete" in allowed)

# 5.4) Find common/unique tags between two users
user1_tags = {"python", "ds", "algorithms"}
user2_tags = {"python", "ml", "statistics"}
print("Shared tags:", user1_tags & user2_tags)
print("Unique to user1:", user1_tags - user2_tags)
print()

# ======================================================
# 6) Frozenset (Immutable Set)
# ======================================================
# frozenset is hashable (can be a key in dict or element of a set)
fs = frozenset({1, 2, 3})
print("frozenset:", fs)

# Using frozenset to build a set of sets
set_of_sets = {frozenset({1, 2}), frozenset({2, 3})}
print("Set of frozensets:", set_of_sets)

# fs.add(4)  # ❌ AttributeError: frozenset has no add (it's immutable)
print()

# ======================================================
# 7) Pitfalls & Gotchas
# ======================================================
# - Using mutable/unhashable elements -> TypeError
try:
    bad = {1, 2, [3, 4]}  # list is unhashable
except TypeError as e:
    print("Unhashable element error:", e)

# - Pop removes an arbitrary item (not predictable)
r = {10, 20, 30}
print("Before pop():", r)
print("pop():", r.pop())
print("After pop():", r)
print()

# ======================================================
# 8) Built-ins that work with sets
# ======================================================
S = {5, 1, 9, 2}
print("len(S):", len(S))
print("min(S):", min(S))
print("max(S):", max(S))
print("sum(S):", sum(S))
print("sorted(S):", sorted(S))  # returns a list (sorted copy)
print()

# ======================================================
# 9) Practice Exercises (Try These!)
# ======================================================
# 1) Given two lists, print their common elements (unique only).
# 2) Remove duplicates from a list while preserving order.
# 3) Check if a set A is a subset of set B; print a friendly message.
# 4) Build a set of squares from 1..N that are even.
# 5) Use frozenset to store unique, unordered pairs as dict keys.

# ======================================================
# End of Day 6 - Sets
# ======================================================

