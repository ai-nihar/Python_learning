"""
======================================================
Python Learning - Week 02 Day 01 (Day 8 Overall)
TOPIC: EXCEPTION HANDLING
======================================================

DESCRIPTION:
This file covers exception handling in Python, which is essential for writing
robust and error-resistant code. Exception handling allows programs to
gracefully respond to unexpected conditions without crashing.

TOPICS COVERED:
1. Understanding Errors & Exceptions
2. Basic Exception Handling with try/except
3. Advanced Exception Handling (else, finally, raise)
4. Creating Custom Exceptions

LEARNING OUTCOMES:
- Recognize common Python exceptions
- Handle errors appropriately using try/except blocks
- Implement advanced exception handling techniques
- Create custom exceptions for specific use cases

======================================================
"""

# ======================================================
# 1) Understanding Errors & Exceptions
# ======================================================
"""
Python has two types of errors:
- Syntax errors: Code that Python cannot parse
- Exceptions: Runtime errors that occur during execution

Exceptions occur when something unexpected happens while 
your program is running. Instead of letting the program crash,
we can "catch" these exceptions and handle them.
"""

# 1.1 Common built-in exceptions with examples
print("\n1. UNDERSTANDING ERRORS & EXCEPTIONS")
print("-" * 40)
print("1.1. Common exception types:")

# TypeError: when an operation is performed on an inappropriate type
print("\nTypeError example:")
try:
    result = "5" + 5  # Attempting to add string and integer
    print(result)
except TypeError as e:
    print(f"Error caught: {e}")
    print("Can't add string and integer directly")
    # Correct solution:
    result = int("5") + 5  # Convert string to int first
    print(f"Corrected result: {result}")  # Output: 10

# ValueError: when a function receives an argument of correct type but inappropriate value
print("\nValueError example:")
try:
    number = int("hello")  # Trying to convert non-numeric string to int
except ValueError as e:
    print(f"Error caught: {e}")
    print("Can't convert 'hello' to an integer")

# IndexError: when trying to access an index that doesn't exist
print("\nIndexError example:")
fruits = ["apple", "banana", "cherry"]
try:
    print(fruits[10])  # Trying to access 11th element in a 3-item list
except IndexError as e:
    print(f"Error caught: {e}")
    print(f"The list only has {len(fruits)} items")

# KeyError: when a dictionary key doesn't exist
print("\nKeyError example:")
person = {"name": "John", "age": 30}
try:
    print(person["height"])  # Trying to access a key that doesn't exist
except KeyError as e:
    print(f"Error caught: {e}")
    print(f"Dictionary doesn't have a 'height' key")
    print(f"Available keys: {list(person.keys())}")

# ZeroDivisionError: when dividing by zero
print("\nZeroDivisionError example:")
try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"Error caught: {e}")
    print("Division by zero is not allowed in math")


# ======================================================
# 2) Basic Exception Handling with try/except
# ======================================================
"""
The try/except block is used to handle exceptions in Python:
- try: Contains code that might raise an exception
- except: Executes when an exception occurs in the try block

This prevents your program from crashing when errors occur.
"""

print("\n2. BASIC EXCEPTION HANDLING")
print("-" * 40)

# The basic structure
print("2.1. Simple try/except:")
try:
    # Code that might raise an exception
    age = int(input("Enter your age: "))
    print(f"Next year you'll be {age + 1}")
except:
    # This catches ANY exception (not recommended in production code)
    print("That's not a valid age")

# Catching specific exceptions (recommended)
print("\n2.2. Catching specific exceptions (recommended practice):")
try:
    user_input = input("Enter a number to divide 100 by: ")
    number = float(user_input)  # Might cause ValueError
    result = 100 / number       # Might cause ZeroDivisionError
    print(f"100 / {number} = {result}")
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Multiple exception types in one handler
print("\n2.3. Handling multiple exceptions together:")
try:
    data = {"a": 100, "b": 0}
    key = input("Enter a key (a or b): ")
    result = 10 / data[key]  # Potential KeyError or ZeroDivisionError
    print(f"10 / data['{key}'] = {result}")
except (KeyError, ZeroDivisionError) as e:
    # The 'as e' syntax captures the exception object
    print(f"Operation failed: {type(e).__name__}: {e}")


# ======================================================
# 3) Advanced Exception Handling
# ======================================================
"""
Python provides additional components for more sophisticated
exception handling:
- else: Runs if no exception occurred
- finally: Always runs, regardless of exceptions
- raise: Manually triggers an exception
"""

print("\n3. ADVANCED EXCEPTION HANDLING")
print("-" * 40)

# 3.1 try/except/else/finally structure
print("3.1. Complete try/except/else/finally structure:")
try:
    # Code that might raise an exception
    number = int(input("Enter a positive number: "))

    # This will only run if no exception occurs in the above code
    if number <= 0:
        raise ValueError("The number must be positive")

except ValueError as e:
    # Runs if a ValueError occurs in the try block
    print(f"Invalid input: {e}")
else:
    # This block runs ONLY if no exception occurred in the try block
    print(f"You entered the valid number: {number}")
    print(f"Square root: {number ** 0.5:.2f}")
finally:
    # This ALWAYS runs, regardless of whether an exception occurred
    print("Exception handling complete")

# 3.2 Raising exceptions manually
print("\n3.2. Raising exceptions manually:")
def set_age(age):
    """
    Set a person's age, with validation.

    Args:
        age: The age to set

    Raises:
        TypeError: If age is not an integer
        ValueError: If age is not between 0 and 120

    Returns:
        str: Confirmation message
    """
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    return f"Age set to {age}"

try:
    print(set_age(25))      # Works fine
    print(set_age("30"))    # Raises TypeError
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

try:
    print(set_age(130))     # Raises ValueError
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")


# ======================================================
# 4) Creating Custom Exceptions
# ======================================================
"""
You can create your own exception classes by inheriting from Exception.
This allows you to define domain-specific errors for your applications.

Custom exceptions make your code more readable and can carry
additional information relevant to the specific error.
"""

print("\n4. CREATING CUSTOM EXCEPTIONS")
print("-" * 40)

# Define a custom exception
class InvalidEmailError(Exception):
    """Raised when an email doesn't have the correct format"""
    pass

def send_email(email, message):
    """
    Send an email (simulated)

    Args:
        email: Email address to send to
        message: Email content

    Raises:
        InvalidEmailError: If email format is invalid
    """
    # Basic check if email contains @ and .
    if '@' not in email or '.' not in email:
        raise InvalidEmailError("Invalid email format")

    # Simulate sending email
    print(f"Email sent to {email}: {message}")

# Using the custom exception
print("4.1. Using a custom exception:")
try:
    send_email("user@example.com", "Hello!")    # Valid
    send_email("invalid-email", "Hello!")       # Invalid
except InvalidEmailError as e:
    print(f"Failed to send email: {e}")

# More advanced custom exception
print("\n4.2. More detailed custom exception:")
class AgeError(Exception):
    """Custom exception with additional information about the error"""

    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age
        message = f"Age {age} is outside allowed range ({min_age}-{max_age})"
        super().__init__(message)

try:
    age = 150
    min_age, max_age = 0, 120

    if age < min_age or age > max_age:
        raise AgeError(age, min_age, max_age)

    print(f"Age {age} is valid")
except AgeError as e:
    print(f"Error: {e}")
    print(f"Provided age: {e.age}")
    print(f"Allowed range: {e.min_age} to {e.max_age}")

"""
SUMMARY:
- Exception handling makes your code more robust by preventing crashes
- Always use specific exception types rather than catching all exceptions
- The try/except/else/finally structure provides comprehensive error handling
- Custom exceptions help create clear, domain-specific error messages
- Good exception handling improves user experience and helps with debugging
"""
