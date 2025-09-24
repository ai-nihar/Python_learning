"""
======================================================
Python Learning - Week 02 Day 01 (Day 8 Overall)
TOPIC: EXCEPTION HANDLING
======================================================

DESCRIPTION:
This file covers exception handling in Python, which is essential for writing
robust and error-resistant code. Rather than crashing when unexpected situations
occur, properly handled exceptions allow programs to respond gracefully.

TOPICS COVERED:
1. Understanding Errors & Exceptions
2. Basic Exception Handling with try/except
3. Advanced Exception Handling Techniques
4. Using Built-in Exception Types

LEARNING OUTCOMES:
- Recognize common Python exceptions and their causes
- Handle errors appropriately using try/except blocks
- Implement robust error recovery with else/finally clauses
- Apply exception handling to make programs more reliable

======================================================
"""

# ======================================================
# 1) Understanding Errors & Exceptions
# ======================================================
"""
In Python, things can go wrong in two main ways:

SYNTAX ERRORS: These occur when Python can't parse your code
- Example: print("Hello world"  # Missing closing parenthesis

EXCEPTIONS: These occur during execution when something unexpected happens
- Example: 10/0  # ZeroDivisionError occurs at runtime

Instead of letting exceptions crash our program, we can anticipate and handle them.
"""

print("\n1. UNDERSTANDING ERRORS & EXCEPTIONS")
print("=" * 50)

# Creating a small interactive error explorer
def explore_exception(code_snippet, exception_name, description):
    """Helper function to demonstrate exceptions in a consistent way"""
    print(f"\n{exception_name}:")
    print(f"  What it means: {description}")
    print(f"  Code example: {code_snippet}")
    try:
        # Using eval to execute the code snippet
        eval(code_snippet)
    except Exception as e:
        print(f"  Error message: {e}")
        print(f"  Error type: {type(e).__name__}")
    print("-" * 40)

# Demonstrate common built-in exceptions
print("\n1.1. Common Python exceptions:")

explore_exception(
    '"5" + 5',
    "TypeError",
    "Operation applied to an object of inappropriate type"
)

explore_exception(
    'int("hello")',
    "ValueError",
    "Function receives argument with correct type but inappropriate value"
)

explore_exception(
    '["apple", "banana", "cherry"][10]',
    "IndexError",
    "Trying to access an index that doesn't exist in a sequence"
)

explore_exception(
    '{"name": "John", "age": 30}["height"]',
    "KeyError",
    "Trying to access a dictionary key that doesn't exist"
)

explore_exception(
    '10/0',
    "ZeroDivisionError",
    "Attempting to divide by zero"
)

explore_exception(
    'open("nonexistent_file.txt")',
    "FileNotFoundError",
    "Trying to access a file that doesn't exist"
)

print("\nUnderstanding these common exceptions helps you anticipate what might go wrong in your code.")

# ======================================================
# 2) Basic Exception Handling with try/except
# ======================================================
"""
The try/except block is the foundation of exception handling:

try:
    # Code that might raise exceptions
except SomeException:
    # Code that runs if SomeException occurs

This pattern prevents your program from crashing when errors occur,
allowing you to handle the problem or provide meaningful feedback.
"""

print("\n\n2. BASIC EXCEPTION HANDLING")
print("=" * 50)

# 2.1 A real-world example: Data processing function
print("\n2.1. Building a robust data processing function:")

def calculate_average(data):
    """Calculate the average of numbers in a list."""
    print(f"Processing data: {data}")

    try:
        total = sum(data)
        count = len(data)
        average = total / count
        return average
    except TypeError:
        print("Error: Input must be a list of numbers")
        return None
    except ZeroDivisionError:
        print("Error: Cannot calculate average of empty list")
        return None

# Test with various inputs to show exception handling
test_cases = [
    [10, 20, 30, 40],       # Normal case
    [10, "20", 30, 40],     # Type error
    []                      # Zero division error
]

for data in test_cases:
    result = calculate_average(data)
    if result is not None:
        print(f"Average: {result}")
    print("-" * 30)

# 2.2 Handling multiple exceptions
print("\n2.2. Handling multiple exceptions:")

def get_value_safely(dictionary, key, divisor):
    """Safely get a value from a dictionary and divide it."""
    try:
        # This could raise KeyError if key not in dict
        value = dictionary[key]

        # This could raise ZeroDivisionError if divisor is 0
        result = value / divisor

        # This could raise TypeError if value can't be divided
        return f"Result: {result}"

    except KeyError:
        return f"Error: Key '{key}' not found in dictionary"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero"
    except TypeError:
        return f"Error: Value cannot be divided by {divisor}"

# Test with different scenarios
test_data = {"a": 100, "b": "hello", "c": 0}

print(get_value_safely(test_data, "a", 5))    # Should work fine
print(get_value_safely(test_data, "x", 5))    # Key error
print(get_value_safely(test_data, "a", 0))    # Zero division error
print(get_value_safely(test_data, "b", 5))    # Type error

# 2.3 Catching any exception
print("\n2.3. Catching any exception (use with caution):")

def parse_input(user_input):
    """Try to parse user input as a number"""
    try:
        # Try to convert to float
        value = float(user_input)
        return f"Successfully parsed: {value}"
    except Exception as e:
        # Catch any exception - generally not recommended
        # but useful for simple user input scenarios
        return f"Could not parse input: {e}"

inputs = ["123", "3.14", "hello", ""]
for user_input in inputs:
    print(f"Input: '{user_input}' → {parse_input(user_input)}")

# ======================================================
# 3) Advanced Exception Handling Techniques
# ======================================================
"""
Python provides additional tools for more sophisticated exception handling:

- try/except/else: Add code that runs ONLY if no exceptions occur
- try/except/finally: Add code that ALWAYS runs, with or without exceptions
- raise: Manually trigger exceptions when conditions warrant it

These tools give you fine-grained control over error handling.
"""

print("\n\n3. ADVANCED EXCEPTION HANDLING TECHNIQUES")
print("=" * 50)

# 3.1 Using else and finally
print("\n3.1. Using else and finally clauses:")

def process_file(filename):
    """Process a file with comprehensive exception handling."""
    file = None
    try:
        print(f"Attempting to open {filename}...")
        file = open(filename, "r")
        content = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found")
        return None

    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None

    else:
        # This runs only if no exceptions occurred in the try block
        print(f"Successfully read {len(content)} characters")
        word_count = len(content.split())
        print(f"Word count: {word_count}")
        return word_count

    finally:
        # This always runs, whether there was an exception or not
        print(f"File operation on '{filename}' complete")
        # Close the file if it was successfully opened
        if file is not None and not file.closed:
            file.close()
            print("File closed")

# Create a test file
with open("sample_text.txt", "w") as f:
    f.write("This is a sample text file.\nIt contains multiple lines.\nUsed for testing exception handling.")

# Process the file
process_file("sample_text.txt")
print()
# Try with a nonexistent file
process_file("nonexistent_file.txt")

# 3.2 Raising exceptions manually
print("\n3.2. Raising exceptions manually:")

def divide_positive_numbers(a, b):
    """Divide two numbers, with validation."""
    # Check if inputs are valid
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")

    if a < 0 or b < 0:
        raise ValueError("Both numbers must be positive")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b

# Test the function with different inputs
test_cases = [
    (10, 2),       # Should work
    (10, -2),      # ValueError
    (10, 0),       # ZeroDivisionError
    ("10", 2)      # TypeError
]

for a, b in test_cases:
    try:
        print(f"{a} / {b} = ", end="")
        result = divide_positive_numbers(a, b)
        print(result)
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

# 3.3 Re-raising exceptions
print("\n3.3. Re-raising exceptions:")

def process_age(age_str):
    """Process age string with helpful error messages."""
    try:
        # Convert to integer
        age = int(age_str)

        # Validate range
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120")

        return f"Valid age: {age}"

    except ValueError as e:
        # Check if this is from int() or our validation
        if "invalid literal" in str(e):
            print(f"Error: '{age_str}' is not a valid number")
        else:
            # Re-raise the exception for our custom validation
            print(f"Error: {e}")
        return None

# Test with different inputs
test_ages = ["25", "abc", "150", "-5"]
for age_str in test_ages:
    print(f"\nProcessing age: {age_str}")
    result = process_age(age_str)
    if result:
        print(result)

# ======================================================
# 4) Using Built-in Exception Types
# ======================================================
"""
Python provides many built-in exception types that you can use to signal
specific error conditions in your code.

Using the right exception type makes your code more readable and helps
users of your functions understand what went wrong.
"""

print("\n\n4. USING BUILT-IN EXCEPTION TYPES")
print("=" * 50)

# 4.1 Common built-in exceptions and when to use them
print("\n4.1. When to use specific exception types:")

def demonstrate_exceptions():
    examples = [
        (ValueError, "Used when a function receives an argument with right type but wrong value",
         "process_age('150')  # Age outside allowed range"),

        (TypeError, "Used when an operation is performed on an object of incorrect type",
         "len(5)  # int has no length"),

        (IndexError, "Used when a sequence index is out of range",
         "['a', 'b'][10]  # Accessing index beyond list length"),

        (KeyError, "Used when a dictionary key is not found",
         "{'a': 1}['b']  # Key 'b' doesn't exist"),

        (FileNotFoundError, "Used when a file or directory cannot be found",
         "open('missing.txt')  # File doesn't exist"),

        (ZeroDivisionError, "Used when division or modulo by zero is encountered",
         "10 / 0  # Division by zero"),

        (PermissionError, "Used when trying to run an operation without adequate access rights",
         "open('/etc/passwd', 'w')  # No permission"),

        (ImportError, "Used when an import statement fails to find the module definition",
         "import non_existent_module")
    ]

    for exception_type, description, example in examples:
        print(f"\n{exception_type.__name__}:")
        print(f"  Description: {description}")
        print(f"  Example: {example}")

demonstrate_exceptions()

# 4.2 Choosing the right exception
print("\n4.2. Choosing the right exception type:")

def save_user_data(user_id, data):
    """Save user data to a file."""

    # Check user_id type
    if not isinstance(user_id, int):
        raise TypeError("user_id must be an integer")

    # Check user_id value
    if user_id <= 0:
        raise ValueError("user_id must be positive")

    # Check data type
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    # Check required fields
    required_fields = ["name", "email"]
    for field in required_fields:
        if field not in data:
            raise KeyError(f"Required field '{field}' missing from data")

    # Convert to string representation
    data_str = str(data)

    # Create filename
    filename = f"user_{user_id}.txt"

    # Try to save file
    try:
        with open(filename, "w") as file:
            file.write(data_str)
        return f"Data saved to {filename}"
    except PermissionError:
        return f"Error: No permission to write to {filename}"
    except Exception as e:
        return f"Error saving data: {type(e).__name__}: {e}"

# Test with different scenarios
test_cases = [
    (1, {"name": "Alice", "email": "alice@example.com"}),  # Valid
    ("1", {"name": "Bob", "email": "bob@example.com"}),    # TypeError (user_id)
    (0, {"name": "Charlie", "email": "charlie@example.com"}),  # ValueError (user_id)
    (3, {"name": "Dave"}),  # KeyError (missing email)
    (4, "invalid data")  # TypeError (data)
]

for user_id, data in test_cases:
    try:
        result = save_user_data(user_id, data)
        print(f"Case: user_id={user_id}, data={data}")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Case: user_id={user_id}, data={data}")
        print(f"Error: {type(e).__name__}: {e}")
    print("-" * 30)

# 4.3 Exception handling in functions
print("\n4.3. Exception handling patterns in functions:")

def safe_function(risky_function, *args, default=None):
    """Run a function safely, returning default value on error."""
    try:
        return risky_function(*args)
    except Exception as e:
        print(f"Error in {risky_function.__name__}: {type(e).__name__}: {e}")
        return default

# Some functions that might raise exceptions
def reciprocal(x):
    """Return the reciprocal of x."""
    return 1 / x

def get_first_element(sequence):
    """Return the first element of a sequence."""
    return sequence[0]

# Test the safe function with different scenarios
print(f"Reciprocal of 5: {safe_function(reciprocal, 5)}")
print(f"Reciprocal of 0: {safe_function(reciprocal, 0, default='Cannot compute reciprocal')}")
print(f"First element of [1,2,3]: {safe_function(get_first_element, [1,2,3])}")
print(f"First element of []: {safe_function(get_first_element, [], default='Empty sequence')}")

"""
SUMMARY:

Exception handling is a critical skill that makes your code:
1. More robust - prevents crashes from unexpected inputs or conditions
2. More informative - provides helpful error messages instead of cryptic crashes
3. More maintainable - centralizes error handling logic in clear patterns

Best practices:
- Be specific: Catch only the exceptions you can handle appropriately
- Be informative: Provide clear error messages that guide users
- Be defensive: Anticipate what might go wrong before it does
- Use built-in exceptions: Choose the right exception type for each error condition
- Use else/finally: Control exactly what code runs in different error scenarios
"""
