"""
====================================================
PYTHON ADVANCED FUNCTIONAL PROGRAMMING - DAY 17
====================================================

This file explores more advanced functional programming techniques in Python,
building on the basics covered in Day 16.

Topics covered:
- Function composition
- Partial functions
- Currying
- Recursion in functional programming
- Immutability and functional data structures
- Functional error handling
"""

print("PYTHON ADVANCED FUNCTIONAL PROGRAMMING")
print("=" * 50)

# =====================================================
# Function Composition
# =====================================================
# Function composition is the process of combining two or more functions
# to produce a new function

print("\nFUNCTION COMPOSITION:")
print("-" * 30)

# Define some simple functions
def add_one(x):
    """Add 1 to the input value."""
    return x + 1

def double(x):
    """Double the input value."""
    return x * 2

def square(x):
    """Square the input value."""
    return x ** 2

# Manual function composition
def compose_two(f, g):
    """
    Compose two functions: f(g(x))

    Args:
        f: Outer function
        g: Inner function

    Returns:
        A new function that applies g first, then f to the result
    """
    return lambda x: f(g(x))

# Example: compose add_one and double: double(add_one(x))
add_one_then_double = compose_two(double, add_one)
print(f"add_one_then_double(5): {add_one_then_double(5)}")  # (5+1)*2 = 12

# Example: compose double and square: square(double(x))
double_then_square = compose_two(square, double)
print(f"double_then_square(3): {double_then_square(3)}")  # (3*2)^2 = 36

# More general composition function for multiple functions
import functools

def compose(*functions):
    """
    Compose an arbitrary number of functions

    Args:
        *functions: Variable number of functions to compose

    Returns:
        A new function that applies all functions in sequence
    """
    def compose_two_funcs(f, g):
        return lambda x: f(g(x))

    if len(functions) == 0:
        return lambda x: x  # Identity function

    return functools.reduce(compose_two_funcs, functions)

# Example: Compose three functions: square(double(add_one(x)))
composed = compose(square, double, add_one)
print(f"compose(square, double, add_one)(3): {composed(3)}")  # ((3+1)*2)^2 = 64

# =====================================================
# Partial Functions
# =====================================================
# Partial functions let you fix a certain number of arguments of a function
# and generate a new function

print("\nPARTIAL FUNCTIONS:")
print("-" * 30)

from functools import partial

# Original function with multiple parameters
def power(base, exponent):
    """Calculate base raised to the exponent power."""
    return base ** exponent

# Create partial functions with fixed parameters
square_func = partial(power, exponent=2)  # Fix exponent=2
cube_func = partial(power, exponent=3)    # Fix exponent=3

print(f"square_func(4): {square_func(4)}")  # 4^2 = 16
print(f"cube_func(3): {cube_func(3)}")      # 3^3 = 27

# More complex example with multiple parameters
def format_string(template, name, age):
    """Format a string using the provided template and values."""
    return template.format(name=name, age=age)

# Create a greeter with a fixed template
greeting_format = "Hello {name}! You are {age} years old."
greeter = partial(format_string, greeting_format)

print(f"greeter('Alice', 30): {greeter('Alice', 30)}")

# Partial with positional arguments
def create_tag(tag_name, content):
    """Create an HTML tag with the given name and content."""
    return f"<{tag_name}>{content}</{tag_name}>"

# Create specialized tag creators
h1_tag = partial(create_tag, "h1")
p_tag = partial(create_tag, "p")

print(f"h1_tag('Title'): {h1_tag('Title')}")  # <h1>Title</h1>
print(f"p_tag('Paragraph'): {p_tag('Paragraph')}")  # <p>Paragraph</p>

# =====================================================
# Currying
# =====================================================
# Currying transforms a function with multiple arguments into a sequence
# of functions each with a single argument

print("\nCURRYING:")
print("-" * 30)

# Manually curried function
def curry_add(x):
    """
    First step of curried add function.

    Args:
        x: First number

    Returns:
        A function waiting for the second argument
    """
    def add_y(y):
        """Inner function that adds y to the captured x value."""
        return x + y
    return add_y

add_5 = curry_add(5)
print(f"curry_add(5)(3): {add_5(3)}")  # 5 + 3 = 8
print(f"Direct currying: {curry_add(10)(20)}")  # 10 + 20 = 30

# More general currying function
def curry(func, arity=None):
    """
    Curry a function with specified arity.
    If arity is None, it's determined from function's signature.

    Args:
        func: The function to curry
        arity: Optional number of arguments to curry

    Returns:
        A curried version of the function
    """
    import inspect

    if arity is None:
        # Get number of non-default parameters
        params = inspect.signature(func).parameters
        arity = sum(1 for p in params.values()
                   if p.default == inspect.Parameter.empty)

    def curried(*args):
        if len(args) >= arity:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))

    return curried

# Test with a multi-argument function
def add3(x, y, z):
    """Add three numbers together."""
    return x + y + z

curried_add3 = curry(add3)
print(f"curried_add3(1)(2)(3): {curried_add3(1)(2)(3)}")  # 1+2+3 = 6
print(f"curried_add3(1, 2)(3): {curried_add3(1, 2)(3)}")  # Alternative way

# =====================================================
# Recursion in Functional Programming
# =====================================================
# Recursion often replaces iteration in functional programming

print("\nRECURSION IN FUNCTIONAL PROGRAMMING:")
print("-" * 30)

# Factorial using recursion
def factorial(n):
    """
    Calculate factorial using recursion.

    Args:
        n: The number to calculate factorial for

    Returns:
        n! (n factorial)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5): {factorial(5)}")  # 5! = 120

# Fibonacci sequence using recursion
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n: Position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"fibonacci(7): {fibonacci(7)}")  # fib(7) = 13

# Tail-recursive factorial (though Python doesn't optimize tail recursion)
def factorial_tail(n, accumulator=1):
    """
    Tail-recursive factorial implementation.

    Args:
        n: The number to calculate factorial for
        accumulator: Running product (default: 1)

    Returns:
        n! (n factorial)
    """
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

print(f"factorial_tail(5): {factorial_tail(5)}")  # 5! = 120

# =====================================================
# Immutability and Functional Data Structures
# =====================================================
# Functional programming prefers immutable data structures

print("\nIMMUTABILITY AND FUNCTIONAL DATA STRUCTURES:")
print("-" * 30)

# Using built-in immutable types
immutable_tuple = (1, 2, 3)
print(f"Immutable tuple: {immutable_tuple}")

# Try to modify tuple (will raise error)
try:
    immutable_tuple[0] = 99
except TypeError as e:
    print(f"Error when modifying tuple: {e}")

# Functional transformation of data
original = (1, 2, 3, 4, 5)
# Instead of modifying in place, create new data
transformed = tuple(map(lambda x: x * 2, original))
print(f"Original: {original}")
print(f"Transformed: {transformed}")

# Using namedtuple for immutable objects
from collections import namedtuple

# Define an immutable Point class
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
print(f"Namedtuple point: {p1}")
print(f"Access fields: p1.x = {p1.x}, p1.y = {p1.y}")

# Try to modify it (will raise error)
try:
    p1.x = 10
except AttributeError as e:
    print(f"Error when modifying namedtuple: {e}")

# To "update" a field, create a new instance
p2 = p1._replace(x=10)
print(f"Original point: {p1}")
print(f"'Updated' point: {p2}")

# =====================================================
# Functional Error Handling
# =====================================================
# Functional approach to error handling using monads-like structures

print("\nFUNCTIONAL ERROR HANDLING:")
print("-" * 30)

# Basic Maybe monad-like implementation
class Maybe:
    """
    A simple Maybe monad-like class.

    Represents a computation that might return a value or nothing.
    Allows chaining operations safely without explicit None checks.
    """
    def __init__(self, value=None):
        self.value = value
        self.is_nothing = value is None

    def map(self, func):
        """
        Apply function if value exists, otherwise return Nothing.

        Args:
            func: Function to apply to the value

        Returns:
            A new Maybe instance with the result or Nothing
        """
        if self.is_nothing:
            return self  # Nothing
        try:
            return Maybe(func(self.value))
        except Exception:
            return Maybe(None)  # Convert exceptions to Nothing

    def __str__(self):
        if self.is_nothing:
            return "Nothing"
        return f"Just {self.value}"

# Using Maybe for safe operations
def safe_div(x, y):
    """
    Safe division using Maybe.

    Args:
        x: Numerator
        y: Denominator

    Returns:
        Maybe with result or Nothing if division by zero
    """
    return Maybe(x / y if y != 0 else None)

def safe_sqrt(x):
    """
    Safe square root using Maybe.

    Args:
        x: Number to take square root of

    Returns:
        Maybe with result or Nothing if x is negative
    """
    return Maybe(x**0.5 if x >= 0 else None)

# Testing Maybe with chain of operations
result = Maybe(16).map(lambda x: x + 4).map(safe_sqrt).map(str)
print(f"Result of Maybe chain: {result}")  # Just 2.0

# Error case
result = Maybe(16).map(lambda x: x - 16).map(safe_sqrt).map(str)
print(f"Result with error: {result}")  # Nothing

# =====================================================
# Practical Example: Data Pipeline
# =====================================================
print("\nPRACTICAL EXAMPLE - DATA PIPELINE:")
print("-" * 30)

# Define some sample data: temperatures in Celsius
celsius_readings = [0, 12, 23, -10, 41, -5, 30]

# Create a data processing pipeline
def validate_temperature(temp):
    """
    Check if temperature is in valid range (-30 to 45 C)

    Args:
        temp: Temperature value to validate

    Returns:
        True if valid, False otherwise
    """
    return -30 <= temp <= 45

def celsius_to_fahrenheit(temp):
    """
    Convert Celsius to Fahrenheit

    Args:
        temp: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit
    """
    return (temp * 9/5) + 32

def format_temperature(temp):
    """
    Format temperature with symbol

    Args:
        temp: Temperature value

    Returns:
        Formatted temperature string
    """
    return f"{temp:.1f}°F"

# Process data using functional tools
valid_temps = filter(validate_temperature, celsius_readings)
fahrenheit_temps = map(celsius_to_fahrenheit, valid_temps)
formatted_temps = map(format_temperature, fahrenheit_temps)

print("Processed temperatures:")
for temp in formatted_temps:
    print(f"  {temp}")

# Alternative: compose the entire pipeline into a single function
def process_temperature(temp):
    """
    Process a single temperature reading through entire pipeline.

    Args:
        temp: Temperature in Celsius

    Returns:
        Formatted temperature string or None if invalid
    """
    if not validate_temperature(temp):
        return None
    fahrenheit = celsius_to_fahrenheit(temp)
    return format_temperature(fahrenheit)

# Process using the composed function
results = [process_temperature(temp) for temp in celsius_readings]
filtered_results = [r for r in results if r is not None]
print(f"Results using composed function: {filtered_results}")

# Example of using our compose function for this pipeline
def safe_validate(temp):
    """Return temperature if valid, None otherwise."""
    return temp if validate_temperature(temp) else None

# Create a pipeline using compose (need to handle None values)
# This is a simplified example compared to a full Maybe implementation
pipeline = compose(
    format_temperature,
    celsius_to_fahrenheit,
    safe_validate
)

# Apply pipeline (with manual None handling)
pipeline_results = []
for temp in celsius_readings:
    result = pipeline(temp)
    if result is not None:
        pipeline_results.append(result)

print(f"Results using compose pipeline: {pipeline_results}")

print("\n" + "=" * 50)
