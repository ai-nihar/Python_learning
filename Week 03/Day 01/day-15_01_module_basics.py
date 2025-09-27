"""
===============================================================================
PYTHON MODULE BASICS
===============================================================================

A module in Python is simply a file containing Python code that can be imported
and used in other Python files. Modules help organize code into logical units,
making it more maintainable, reusable, and easier to understand.

IN THIS LESSON:
  1. What are modules and why use them
  2. How to import modules
  3. Module search paths
  4. Creating your own modules
  5. Module attributes and functions

===============================================================================
"""

#==============================================================================
# 1. WHAT ARE MODULES AND WHY USE THEM
#==============================================================================
"""
Modules are Python's way to organize code into logical units.

BENEFITS OF USING MODULES:
  • Code organization: Break down complex programs into manageable parts
  • Code reusability: Write once, use anywhere
  • Namespace management: Avoid naming conflicts
  • Sharing functionality: Distribute useful code to others
"""

print("=" * 50)
print("UNDERSTANDING MODULES")
print("=" * 50)

#==============================================================================
# 2. HOW TO IMPORT MODULES
#==============================================================================
"""
Python provides several ways to import modules:
"""

# Method 1: Import the entire module
import math  # Standard library module for mathematical operations

# Now we can use functions from the math module using the dot notation
print(f"Pi value from math module: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Method 2: Import specific items from a module
from random import randint, choice

# Now we can use these functions directly without the module prefix
print(f"Random integer between 1 and 10: {randint(1, 10)}")
print(f"Random choice from a list: {choice(['apple', 'banana', 'cherry'])}")

# Method 3: Import with an alias (useful for modules with long names)
import datetime as dt

# Now we can use the shorter alias
current_time = dt.datetime.now()
print(f"Current time: {current_time}")

# Method 4: Import all names from a module (generally not recommended)
# from math import *  # This would import all functions from math
# print(sqrt(25))     # No need for math.sqrt

print("\n" + "=" * 50)
print("MODULE SEARCH PATH")
print("=" * 50)

#==============================================================================
# 3. MODULE SEARCH PATH
#==============================================================================
"""
When you import a module, Python looks for it in several locations:
  1. The directory containing the script you're running
  2. The directories in the PYTHONPATH environment variable
  3. Standard library directories
  4. Site-packages directories (where third-party packages are installed)
"""

import sys  # System-specific parameters and functions

# Print the module search paths
print("Python searches for modules in these locations:")
for path in sys.path:
    print(f"- {path}")

print("\n" + "=" * 50)
print("CREATING YOUR OWN MODULES")
print("=" * 50)

#==============================================================================
# 4. CREATING YOUR OWN MODULES
#==============================================================================
"""
Creating your own module is as simple as writing a Python file.

Example: Imagine we have a file called 'my_math.py' with these contents:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

Then in another file, we could do:

import my_math
print(my_math.add(5, 3))  # 8
print(my_math.PI)  # 3.14159
"""

# Example of what using a custom module looks like
print("Example of using a custom module (simulated):")
print("import my_math")
print("result = my_math.add(5, 3)")
print("print(result)  # Output: 8")

print("\n" + "=" * 50)
print("MODULE ATTRIBUTES AND FUNCTIONS")
print("=" * 50)

#==============================================================================
# 5. MODULE ATTRIBUTES AND FUNCTIONS
#==============================================================================
"""
Modules have special attributes and functions that can be useful.
"""

# The __name__ attribute
print(f"The __name__ of this module is: {__name__}")
print("This is '__main__' when the file is run directly.")
print("It will be the module's name when imported.")

# Demonstrating the if __name__ == "__main__": pattern
def main():
    print("\nThis function runs only when the module is executed directly")

if __name__ == "__main__":
    main()  # This runs when the file is executed directly
    # But not when it's imported as a module in another file

# The dir() function - list all names defined in a module
print("\nNames defined in the math module:")
math_contents = [name for name in dir(math) if not name.startswith('_')]
print(math_contents[:10])  # Show first 10 items for brevity

# The help() function - get documentation for a module
print("\nTo get help on a module, use:")
print("help(math)  # Prints documentation for the math module")
# Uncommenting the line below would print extensive documentation
# help(math)

print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)

"""
KEY TAKEAWAYS:

1. Modules help organize and reuse code across Python programs
2. There are multiple ways to import modules (import x, from x import y, etc.)
3. Python searches for modules in specific locations (sys.path)
4. Creating custom modules is as simple as writing .py files
5. The __name__ attribute helps determine if a file is being run directly or imported
6. Functions like dir() and help() provide information about modules

Next, we'll learn about packages, which are collections of modules organized in a directory hierarchy.
"""
