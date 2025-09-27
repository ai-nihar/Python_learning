"""
===============================================================================
PYTHON STANDARD LIBRARY EXPLORATION
===============================================================================

The Python Standard Library is a collection of modules and packages that come with Python.
These provide ready-to-use functionality for many common programming tasks,
from file I/O to web services, without requiring additional installation.

IN THIS LESSON:
  1. Overview of the standard library
  2. Essential standard library modules
  3. Deep dive into selected modules
  4. Finding and using documentation

===============================================================================
"""

#==============================================================================
# 1. OVERVIEW OF THE STANDARD LIBRARY
#==============================================================================
"""
The Python Standard Library contains modules for:
  • File and directory access
  • Mathematical functions
  • Internet protocols
  • Data manipulation
  • Operating system interfaces
  • Concurrent execution
  • And much more!
"""

print("=" * 50)
print("THE PYTHON STANDARD LIBRARY")
print("=" * 50)

print("Python comes with 'batteries included' - a rich and versatile standard library")
print("Some categories of modules in the standard library:")
print("- Text Processing: string, re, difflib")
print("- Data Types: datetime, collections, array")
print("- Mathematics: math, random, statistics")
print("- File Handling: os, io, pathlib")
print("- Concurrent Execution: threading, multiprocessing, asyncio")
print("- Internet Data Handling: json, html, xml")
print("- Internet Protocols: http, email, urllib")
print("- Development Tools: unittest, doctest, pdb")

print("\n" + "=" * 50)
print("ESSENTIAL STANDARD LIBRARY MODULES")
print("=" * 50)

#==============================================================================
# 2. ESSENTIAL STANDARD LIBRARY MODULES
#==============================================================================
"""
Let's explore some of the most commonly used standard library modules:
"""

# datetime: Date and time manipulation
import datetime

print("\n--- datetime module ---")
now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d')}")
print(f"In 10 days it will be: {now + datetime.timedelta(days=10)}")

# os: Operating system interface
import os

print("\n--- os module ---")
print(f"Current working directory: {os.getcwd()}")
print(f"Contents of the current directory: {os.listdir('.')[:5]} ...")  # First 5 items

# random: Generate pseudo-random numbers
import random

print("\n--- random module ---")
print(f"Random integer between 1 and 100: {random.randint(1, 100)}")
print(f"Random choice from a list: {random.choice(['red', 'green', 'blue'])}")
print(f"Random sample of 3 from a range: {random.sample(range(1, 30), 3)}")
print(f"Random float between 0 and 1: {random.random()}")

# math: Mathematical functions
import math

print("\n--- math module ---")
print(f"Pi value: {math.pi}")
print(f"Square root of 25: {math.sqrt(25)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Factorial of 5: {math.factorial(5)}")

# collections: Container datatypes
import collections

print("\n--- collections module ---")
# Counter: count occurrences of elements
counter = collections.Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
print(f"Counting fruits: {counter}")
print(f"Most common fruit: {counter.most_common(1)}")

# defaultdict: dict with default values for missing keys
fruit_colors = collections.defaultdict(lambda: "unknown")
fruit_colors["apple"] = "red"
fruit_colors["banana"] = "yellow"
print(f"Color of apple: {fruit_colors['apple']}")
print(f"Color of grape: {fruit_colors['grape']}")  # Returns 'unknown' instead of KeyError

# deque: efficient list-like container with fast appends/pops on both ends
deque = collections.deque([1, 2, 3])
deque.appendleft(0)
deque.append(4)
print(f"Deque after modifications: {deque}")

print("\n" + "=" * 50)
print("DEEP DIVE: STRING MODULE")
print("=" * 50)

#==============================================================================
# 3. DEEP DIVE INTO SELECTED MODULES
#==============================================================================

# Let's do a deeper exploration of the string module
import string

print("\n--- string module in depth ---")
print(f"ASCII lowercase letters: {string.ascii_lowercase}")
print(f"ASCII uppercase letters: {string.ascii_uppercase}")
print(f"Digits: {string.digits}")
print(f"Hexadecimal digits: {string.hexdigits}")
print(f"Punctuation characters: {string.punctuation}")
print(f"Printable characters: {string.printable[:30]}...")  # First 30 chars

# String constants are useful for validation and filtering
password = "MyP@ssw0rd"
has_lowercase = any(c in string.ascii_lowercase for c in password)
has_uppercase = any(c in string.ascii_uppercase for c in password)
has_digit = any(c in string.digits for c in password)
has_special = any(c in string.punctuation for c in password)

print("\nPassword validation:")
print(f"- Has lowercase: {has_lowercase}")
print(f"- Has uppercase: {has_uppercase}")
print(f"- Has digit: {has_digit}")
print(f"- Has special character: {has_special}")
print(f"- Valid password: {has_lowercase and has_uppercase and has_digit and has_special}")

# String translation using maketrans and translate
print("\nString translation example:")
translation_table = str.maketrans(
    {"a": "4", "e": "3", "i": "1", "o": "0", "s": "$"}
)
text = "hello this is a secret message"
leet_text = text.translate(translation_table)
print(f"Original: {text}")
print(f"Translated to 'leet speak': {leet_text}")

print("\n" + "=" * 50)
print("DEEP DIVE: PATHLIB MODULE")
print("=" * 50)

# Another deep dive: pathlib for file path manipulation
import pathlib

print("\n--- pathlib module in depth ---")
# Creating path objects
current_file = pathlib.Path(__file__)
print(f"Current file: {current_file}")
print(f"Parent directory: {current_file.parent}")
print(f"Absolute path: {current_file.absolute()}")

# Path manipulation
new_file = current_file.parent / "example.txt"
print(f"Constructed path: {new_file}")
print(f"File name: {new_file.name}")
print(f"File stem (name without extension): {new_file.stem}")
print(f"File suffix (extension): {new_file.suffix}")

# Path information
print(f"Does the file exist? {new_file.exists()}")
print(f"Is it a file? {new_file.is_file()}")
print(f"Is it a directory? {new_file.is_dir()}")

# Path iteration
print("\nContents of parent directory:")
# List first 5 items in the parent directory
for i, item in enumerate(current_file.parent.iterdir()):
    if i >= 5:
        print("...")
        break
    print(f"- {item.name}")

print("\n" + "=" * 50)
print("FINDING AND USING DOCUMENTATION")
print("=" * 50)

#==============================================================================
# 4. FINDING AND USING DOCUMENTATION
#==============================================================================
"""
There are several ways to access Python documentation:
"""

print("\nAccessing Python documentation:")
print("1. Built-in help system:")
print("   help(math)")
print("   help(str.split)")

print("\n2. Python Official Documentation:")
print("   https://docs.python.org/3/library/")

print("\n3. Using the dir() function to see available attributes/methods:")
print("   dir(math)")

print("\n4. Docstrings in interactive mode:")
print("   print(math.sqrt.__doc__)")

# Demonstrating docstrings access
print("\nDocstring for math.sqrt:")
print(math.sqrt.__doc__)

print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)

"""
KEY TAKEAWAYS:

1. Python's standard library provides ready-to-use modules for many common tasks
2. Essential modules include datetime, os, random, math, and collections
3. Each module has specialized functions and classes for specific domains
4. The help() function and official documentation are valuable resources
5. Using standard library modules can save significant development time
6. Exploring the standard library helps discover built-in solutions before seeking external packages

Next, we'll learn about working with third-party packages using pip and virtual environments.
"""
