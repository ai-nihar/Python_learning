"""
===============================================================================
PYTHON PACKAGE STRUCTURE
===============================================================================

A package in Python is a way of organizing related modules into a directory hierarchy.
It's essentially a directory that contains multiple Python modules and a special
__init__.py file that tells Python the directory should be treated as a package.

IN THIS LESSON:
  1. What are packages and why use them
  2. Creating a package structure
  3. The role of __init__.py files
  4. Importing from packages
  5. Absolute vs relative imports
  6. Namespace packages (Python 3.3+)

===============================================================================
"""

#==============================================================================
# 1. WHAT ARE PACKAGES AND WHY USE THEM
#==============================================================================
"""
Packages are a way to structure Python's module namespace by using "dotted module names".

BENEFITS OF USING PACKAGES:
  • Hierarchical organization of modules
  • Better code organization for large projects
  • Avoiding name collisions
  • Logical grouping of related functionality
"""

print("=" * 50)
print("UNDERSTANDING PACKAGES")
print("=" * 50)

# Example of how packages are used
print("Example of importing from a package:")
print("from mypackage.subpackage import mymodule")
print("mymodule.my_function()")

print("\n" + "=" * 50)
print("CREATING A PACKAGE STRUCTURE")
print("=" * 50)

#==============================================================================
# 2. CREATING A PACKAGE STRUCTURE
#==============================================================================
"""
To create a package, you need to:
  1. Create a directory with the package name
  2. Add an __init__.py file (can be empty in modern Python)
  3. Add module files (.py) inside the package

Example package structure:
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
        module4.py
"""

print("A typical package structure:")
print("""
myproject/
   |-- __init__.py
   |-- main.py
   |-- utils/
   |    |-- __init__.py
   |    |-- helpers.py
   |    `-- formatters.py
   `-- data/
        |-- __init__.py
        |-- readers.py
        `-- writers.py
""")

print("\n" + "=" * 50)
print("THE ROLE OF __init__.py FILES")
print("=" * 50)

#==============================================================================
# 3. THE ROLE OF __init__.py FILES
#==============================================================================
"""
The __init__.py file serves multiple purposes:
  1. Marks a directory as a Python package
  2. Can initialize package-level variables
  3. Can import selected modules automatically when the package is imported
  4. Can define what is exported when using "from package import *"
"""

print("Example of a simple __init__.py file:")
print("""
# __init__.py for a 'math_utils' package

# Import commonly used functions to make them available at package level
from .basic import add, subtract
from .advanced import factorial

# Define __all__ to control what's imported with "from package import *"
__all__ = ['add', 'subtract', 'factorial', 'calculate_average']

# Package-level variable
VERSION = '1.0.0'

# Package-level function
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
""")

print("\n" + "=" * 50)
print("IMPORTING FROM PACKAGES")
print("=" * 50)

#==============================================================================
# 4. IMPORTING FROM PACKAGES
#==============================================================================
"""
There are several ways to import from packages:
"""

# Method 1: Import a specific module from a package
print("# Method 1: Import a specific module")
print("import mypackage.module1")
print("mypackage.module1.function1()")

# Method 2: Import a specific item from a module in a package
print("\n# Method 2: Import specific items")
print("from mypackage.module1 import function1, Class1")
print("function1()")
print("obj = Class1()")

# Method 3: Import a subpackage
print("\n# Method 3: Import a subpackage")
print("import mypackage.subpackage")
print("mypackage.subpackage.module3.function3()")

# Method 4: Import with an alias
print("\n# Method 4: Import with an alias")
print("import mypackage.long_module_name as lmn")
print("lmn.some_function()")

print("\n" + "=" * 50)
print("ABSOLUTE VS RELATIVE IMPORTS")
print("=" * 50)

#==============================================================================
# 5. ABSOLUTE VS RELATIVE IMPORTS
#==============================================================================
"""
Python supports two types of imports within packages:
  • Absolute imports: use the full path from the project's root
  • Relative imports: use the current package as a reference point
"""

print("Example of absolute imports:")
print("""
# In mypackage/subpackage/module3.py
import mypackage.module1
from mypackage.module2 import SomeClass
""")

print("\nExample of relative imports:")
print("""
# In mypackage/subpackage/module3.py
from .. import module1           # Import from parent package
from ..module2 import SomeClass  # Import from a specific module in parent package
from . import module4            # Import from the same package
""")

print("""
Relative import symbols:
  • . refers to the current package
  • .. refers to the parent package
  • ... refers to the grandparent package, and so on
""")

print("\n" + "=" * 50)
print("NAMESPACE PACKAGES")
print("=" * 50)

#==============================================================================
# 6. NAMESPACE PACKAGES
#==============================================================================
"""
Introduced in Python 3.3, namespace packages allow package portions to be spread across
multiple directories. They don't require an __init__.py file.
"""

print("Namespace packages allow:")
print("1. Splitting a package across multiple directories")
print("2. Multiple contributors to add to the same namespace")
print("3. Distribution of parts of a package separately")

print("\nExample of a namespace package spread across locations:")
print("""
/path1/mypackage/module1.py
/path2/mypackage/module2.py

# Python will treat both directories as part of the same 'mypackage'
# when both paths are in sys.path
""")

print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)

"""
KEY TAKEAWAYS:

1. Packages help organize related modules into a directory hierarchy
2. The __init__.py file marks a directory as a package and can initialize it
3. There are multiple ways to import from packages
4. Absolute imports use the full path, while relative imports use the current location as reference
5. Namespace packages (Python 3.3+) allow splitting packages across multiple directories
6. Well-structured packages make large Python projects more maintainable

Next, we'll explore some of the most useful modules in Python's standard library.
"""
