"""
======================================================
Python Learning - Week 02 Day 01 (Day 8 Overall)
TOPIC: Exception Handling
======================================================
This file covers exception handling in Python:
- What errors and exceptions are
- How to handle exceptions with try/except
- How to use finally, else, and raise
- How to create custom exceptions
======================================================
"""

print("=" * 50)
print("DAY 8: EXCEPTION HANDLING")
print("=" * 50)
print()

# ======================================================
# 1) Understanding Errors & Exceptions
# ======================================================
print("1. UNDERSTANDING ERRORS & EXCEPTIONS")
print("-" * 40)

# 1.1 Common built-in exceptions
print("1.1. Common exception types:")

# TypeError: when an operation is performed on an inappropriate type
print("\nTypeError example:")
try:
    result = "5" + 5
    print(result)
except TypeError as e:
    print(f"Error caught: {e}")
    print("Can't add string and integer directly")
    # Correct solution:
    result = int("5") + 5
    print(f"Corrected: {result}")

# ValueError: when a function receives an argument of correct type but inappropriate value
print("\nValueError example:")
try:
    number = int("hello")
except ValueError as e:
    print(f"Error caught: {e}")
    print("Can't convert 'hello' to an integer")

# IndexError: when trying to access an index that doesn't exist
print("\nIndexError example:")
fruits = ["apple", "banana", "cherry"]
try:
    print(fruits[10])
except IndexError as e:
    print(f"Error caught: {e}")
    print(f"The list only has {len(fruits)} items")

# KeyError: when a dictionary key doesn't exist
print("\nKeyError example:")
person = {"name": "John", "age": 30}
try:
    print(person["height"])
except KeyError as e:
    print(f"Error caught: {e}")
    print(f"Dictionary doesn't have a 'height' key")
    print(f"Available keys: {person.keys()}")

# ZeroDivisionError: when dividing by zero
print("\nZeroDivisionError example:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")
    print("Division by zero is not allowed in math")

print()

# ======================================================
# 2) Basic Exception Handling with try/except
# ======================================================
print("2. BASIC EXCEPTION HANDLING")
print("-" * 40)

# The basic structure
print("2.1. Simple try/except:")
try:
    # Code that might raise an exception
    age = int(input("Enter your age: "))
    print(f"Next year you'll be {age + 1}")
except:
    # This catches ANY exception (not recommended)
    print("That's not a valid age")

# Catching specific exceptions (recommended)
print("\n2.2. Catching specific exceptions:")
try:
    user_input = input("Enter a number to divide 100 by: ")
    number = float(user_input)
    result = 100 / number
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
    result = 10 / data[key]
    print(f"10 / data['{key}'] = {result}")
except (KeyError, ZeroDivisionError) as e:
    print(f"Operation failed: {type(e).__name__}: {e}")

print()

# ======================================================
# 3) Advanced Exception Handling
# ======================================================
print("3. ADVANCED EXCEPTION HANDLING")
print("-" * 40)

# 3.1 try/except/else/finally structure
print("3.1. Complete try/except/else/finally structure:")
try:
    # Code that might raise an exception
    number = int(input("Enter a positive number: "))

    # This will only run if no exception occurs
    if number <= 0:
        raise ValueError("The number must be positive")

except ValueError as e:
    print(f"Invalid input: {e}")
else:
    # This block runs if no exception occurred in the try block
    print(f"You entered the valid number: {number}")
    print(f"Square root: {number ** 0.5:.2f}")
finally:
    # This always runs, regardless of whether an exception occurred
    print("Exception handling complete")

# 3.2 Raising exceptions manually
print("\n3.2. Raising exceptions manually:")
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    return f"Age set to {age}"

try:
    print(set_age(25))      # Works fine
    print(set_age("30"))    # TypeError
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

try:
    print(set_age(130))     # ValueError
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

print()

# ======================================================
# 4) Creating Custom Exceptions
# ======================================================
print("4. CREATING CUSTOM EXCEPTIONS")
print("-" * 40)

# Define a custom exception
class InvalidEmailError(Exception):
    """Raised when an email doesn't have the correct format"""
    pass

def send_email(email, message):
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
    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age
        message = f"Age {age} is outside allowed range ({min_age}-{max_age})"
        super().__init__(message)

def verify_age(age):
    min_age, max_age = 18, 65
    if age < min_age or age > max_age:
        raise AgeError(age, min_age, max_age)
    return f"Age {age} is valid"

try:
    print(verify_age(30))   # Valid
    print(verify_age(15))   # Too young
except AgeError as e:
    print(f"Error: {e}")

print()

# ======================================================
# 5) Best Practices & Tips
# ======================================================
print("5. BEST PRACTICES & TIPS")
print("-" * 40)

# 5.1 Don't catch all exceptions silently
print("5.1. Avoid bare except clauses:")
def bad_practice():
    try:
        # This will raise a ZeroDivisionError
        return 10 / 0
    except:
        # Silently catching and ignoring the error - BAD!
        return 0  # User has no idea what went wrong

def better_practice():
    try:
        # This will raise a ZeroDivisionError
        return 10 / 0
    except ZeroDivisionError:
        # Specific error handling - GOOD!
        print("Warning: Division by zero detected, returning 0")
        return 0

print(f"Bad practice result: {bad_practice()}")
print(f"Better practice result: {better_practice()}")

# 5.2 Only catch exceptions you can handle
print("\n5.2. Only catch exceptions you can handle:")
def process_data(data):
    # More specific exception handling pattern
    try:
        result = data['value'] / data['divisor']
        return result
    except KeyError as e:
        # We know exactly what's missing
        print(f"Missing key in data: {e}")
        return None
    except ZeroDivisionError:
        # We can handle division by zero
        print("Cannot divide by zero")
        return None
    except Exception as e:
        # For unexpected errors, re-raise to avoid hiding bugs
        print(f"Unexpected error: {e}")
        raise

# 5.3 Context managers: using 'with' for cleanup
print("\n5.3. Using context managers:")
print("Example with file handling:")
print("with open('file.txt', 'w') as f:")
print("    f.write('Hello world')")
print("# File is automatically closed when the 'with' block ends")

print("\n" + "=" * 50)
print("End of Exception Handling Examples")
print("=" * 50)
