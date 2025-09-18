"""
Day 6: Mastering Python Dictionaries - Complete Guide
Date: 2025-09-18

This file covers Python dictionaries: creation, accessing, updating,
removal, iteration patterns, methods, comprehensions, merging, nested
structures, and advanced tips. Includes runnable snippets and notes.
"""

# ======================================================
# 1) Introduction to Dictionaries
# ======================================================
# Dict = mapping of key -> value pairs.
# - Keys must be hashable (int, str, tuple). Values can be anything.
# - Insertion order is preserved (Python 3.7+). Useful for predictable output.

person = {"name": "Nihar", "age": 19, "country": "India"}
print("Person:", person)
print("Type:", type(person))
print()

# ======================================================
# 2) Creating Dictionaries (many ways)
# ======================================================
# Literal
user = {"id": 101, "active": True}
print("Literal:", user)

# dict() with keyword args (keys must be valid identifiers)
user2 = dict(id=102, active=False)
print("dict(...) with kwargs:", user2)

# From iterable of pairs (e.g., list of tuples)
pairs = [("x", 1), ("y", 2)]
coords = dict(pairs)
print("From pairs:", coords)

# Using zip
keys = ["a", "b", "c"]
vals = [1, 2, 3]
combined = dict(zip(keys, vals))
print("From zip:", combined)

# fromkeys (same default for all keys)
defaults = dict.fromkeys(["r", "g", "b"], 0)
print("fromkeys:", defaults)
print()

# ======================================================
# 3) Accessing Items
# ======================================================
print("Name via indexing:", person["name"])  # KeyError if missing

# get() is safe: returns None or default if key not found
print("Nickname via get (default='N/A'):", person.get("nickname", "N/A"))

# keys(), values(), items()
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# Membership tests check keys by default
print("Has key 'age'?:", "age" in person)
print("Has value 'India'?:", "India" in person.values())
print()

# ======================================================
# 4) Inserting & Updating
# ======================================================
settings = {"theme": "light"}
settings["theme"] = "dark"     # Update existing
settings["font"] = "Inter"      # Insert new
print("After assignments:", settings)

# update(): merge another mapping or iterable of pairs
settings.update({"font_size": 14, "line_height": 1.6})
print("After update():", settings)

# setdefault(): get value if exists, else set to default and return it
lang = {}
lang.setdefault("primary", "en")
lang.setdefault("secondary", "hi")
print("After setdefault():", lang)
print()

# ======================================================
# 5) Removing Items
# ======================================================
profile = {"u": "john", "role": "admin", "active": True}
val = profile.pop("role")        # Remove by key and return value
print("popped 'role':", val, "remaining:", profile)

missing = profile.pop("email", None)  # Provide default to avoid KeyError
print("popped 'email' (default None):", missing)

last = {"a": 1, "b": 2, "c": 3}
print("Before popitem():", last)
print("popitem():", last.popitem())  # Removes last inserted pair (LIFO)
print("After popitem():", last)

# del removes a key entirely (raises KeyError if missing)
if "u" in profile:
    del profile["u"]
print("After del 'u':", profile)

profile.clear()                   # Remove all items
print("After clear():", profile)
print()

# ======================================================
# 6) Iteration Patterns
# ======================================================
project = {"name": "Alpha", "stars": 5, "lang": "Python"}

# Iterate keys (default)
for k in project:
    print("key:", k)

# Iterate values
for v in project.values():
    print("val:", v)

# Iterate items (key and value)
for k, v in project.items():
    print(f"{k} -> {v}")
print()

# ======================================================
# 7) Dictionary Comprehensions
# ======================================================
nums = [1, 2, 3, 4, 5]
squares = {n: n * n for n in nums}
print("Squares dict:", squares)

# With condition
parity = {n: ("even" if n % 2 == 0 else "odd") for n in range(6)}
print("Parity dict:", parity)

# Reverse a mapping safely (values must be unique)
reversed_map = {v: k for k, v in squares.items()}
print("Reversed squares:", reversed_map)
print()

# ======================================================
# 8) Merging Dictionaries (Python 3.9+)
# ======================================================
base = {"a": 1, "b": 2}
extra = {"b": 20, "c": 3}
merged_copy = base | extra        # New dict; right side wins on conflicts
print("base | extra:", merged_copy)

base |= extra                     # In-place merge into base
print("base after |= extra:", base)
print()

# ======================================================
# 9) Nested Dictionaries
# ======================================================
users = {
    1: {"name": "Alice", "scores": {"math": 92, "eng": 88}},
    2: {"name": "Bob",   "scores": {"math": 77, "eng": 81}},
}
print("Users:", users)
print("Alice math:", users[1]["scores"]["math"])  # Chain keys

# Safe access for deep reads using get()
print(
    "Bob eng (safe):",
    users.get(2, {}).get("scores", {}).get("eng", "N/A")
)
print()

# ======================================================
# 10) Copying: Shallow vs Deep
# ======================================================
import copy
state = {"nums": [1, 2], "flag": True}
shallow = state.copy()            # or dict(state)
deep = copy.deepcopy(state)

state["nums"][0] = 99             # Mutating nested list affects shallow, not deep
print("Original:", state)
print("Shallow copy:", shallow)
print("Deep copy:", deep)
print()

# ======================================================
# 11) Pitfalls & Best Practices
# ======================================================
# - Keys must be hashable; list/dict as key -> TypeError
try:
    bad = { [1, 2]: "oops" }     # list is unhashable
except TypeError as e:
    print("Unhashable key error:", e)

# - KeyError on missing key access with []
try:
    _ = person["unknown"]
except KeyError as e:
    print("KeyError example:", e)

# - Updating an existing key keeps its insertion position in CPython 3.7+
order_demo = {"first": 1, "second": 2}
order_demo["second"] = 22
order_demo["third"] = 3
print("Order preserved on update:", list(order_demo.keys()))
print()

# ======================================================
# 12) Useful Methods (Quick Reference)
# ======================================================
# get(key, default), setdefault(key, default), update(mapping),
# pop(key[, default]), popitem(), clear(), copy(), keys(), values(), items(),
# fromkeys(iterable, value)

print("get('age'):", person.get("age"))
print("setdefault('city','Mumbai'):", person.setdefault("city", "Mumbai"))
print("after setdefault, person:", person)
print()

# ======================================================
# 13) Advanced: collections (defaultdict, Counter)
# ======================================================
from collections import defaultdict, Counter

# defaultdict: auto-creates default values for missing keys
freq = defaultdict(int)
for ch in "mississippi":
    freq[ch] += 1                  # no need to check if key exists
print("defaultdict counts:", dict(freq))

# Counter: specialized dict for counting hashable items
cnt = Counter(["a", "b", "a", "c", "b", "a"])
print("Counter counts:", cnt)
print("Most common 2:", cnt.most_common(2))
print()

# ======================================================
# 14) Practice Exercises (Try These!)
# ======================================================
# 1) Build a frequency table of words in a sentence (hint: Counter or defaultdict).
# 2) Merge two dicts with | and compare with update().
# 3) Create a dict comprehension mapping n -> n^3 for n in 1..10 (only even n).
# 4) Safely read nested dict value with get() chain and a default.
# 5) Convert a list of dicts (users) into a dict keyed by user id.

# ======================================================
# End of Day 6 - Dictionaries
# ======================================================

