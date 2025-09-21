"""
======================================================
Python Learning - Week 02 Day 02 (Day 9 Overall)
TOPIC: CONSTRUCTORS AND SPECIAL METHODS
======================================================

DESCRIPTION:
This file explores constructors and special methods in Python classes,
which provide essential functionality and customization for your objects.

TOPICS COVERED:
1. Constructor (__init__) in detail
2. String representation methods (__str__, __repr__)
3. Destructor (__del__)
4. Other common special methods

LEARNING OUTCOMES:
- Implement constructors with validation
- Create informative string representations
- Understand the lifecycle of objects
- Use special methods to customize object behavior

======================================================
"""

# =====================================================
# 1. CONSTRUCTOR IN DETAIL
# =====================================================
print("=" * 50)
print("1. CONSTRUCTOR IN DETAIL")
print("=" * 50)

class Person:
    # Constructor - called when an object is created
    def __init__(self, name, age):
        print(f"Constructor called for {name}")
        self.name = name
        self.age = age
        # We can do validation here
        if age < 0:
            raise ValueError("Age cannot be negative")

# Creating Person objects with valid age
print("Creating person with valid age:")
alice = Person("Alice", 30)

# Creating with invalid age
try:
    print("\nTrying to create a person with negative age:")
    invalid_person = Person("Invalid", -5)
except ValueError as e:
    print(f"Error: {e}")

# Constructor with default parameters
class Product:
    def __init__(self, name, price=0.0, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

        # Validate parameters
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

    def total_value(self):
        return self.price * self.quantity

# Creating products with default and explicit values
print("\nProducts with default and explicit values:")
default_product = Product("Generic Item")
custom_product = Product("Premium Item", 19.99, 3)

print(f"Default product: {default_product.name}, Price: ${default_product.price}, Quantity: {default_product.quantity}")
print(f"Custom product: {custom_product.name}, Price: ${custom_product.price}, Quantity: {custom_product.quantity}")
print(f"Custom product total value: ${custom_product.total_value()}")

# =====================================================
# 2. STRING REPRESENTATION METHODS
# =====================================================
print("\n" + "=" * 50)
print("2. STRING REPRESENTATION METHODS")
print("=" * 50)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Informal string representation (for users)
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    # Official string representation (for developers)
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

# Create a book
book = Book("Python Crash Course", "Eric Matthes", 544)

# String representations in action
print(f"str(book): {str(book)}")  # User-friendly representation
print(f"repr(book): {repr(book)}")  # Developer representation

print("\nAutomatically used representations:")
print(f"Print statement uses __str__: {book}")  # Uses __str__
book_list = [book]
print(f"List display uses __repr__: {book_list}")  # Uses __repr__

# =====================================================
# 3. DESTRUCTOR AND OBJECT LIFECYCLE
# =====================================================
print("\n" + "=" * 50)
print("3. DESTRUCTOR AND OBJECT LIFECYCLE")
print("=" * 50)

class ResourceUser:
    def __init__(self, name, resource_id):
        self.name = name
        self.resource_id = resource_id
        print(f"{self.name} is using resource {self.resource_id}")

    # Destructor - called when an object is garbage collected
    def __del__(self):
        print(f"{self.name} is releasing resource {self.resource_id}")

# Create and destroy objects
print("Creating resource users:")
user1 = ResourceUser("Process 1", "R-001")
user2 = ResourceUser("Process 2", "R-002")

print("\nDeleting first user explicitly:")
del user1

print("\nSecond user will be deleted when it goes out of scope")
print("(typically at the end of the program)")

# =====================================================
# 4. OTHER COMMON SPECIAL METHODS
# =====================================================
print("\n" + "=" * 50)
print("4. OTHER COMMON SPECIAL METHODS")
print("=" * 50)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add two points
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Subtract two points
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Check equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Convert to string
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Length (magnitude) of the point from origin
    def __len__(self):
        import math
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # Make the object callable
    def __call__(self, factor):
        return Point(self.x * factor, self.y * factor)

# Create points
p1 = Point(3, 4)
p2 = Point(1, 2)

# Using special methods
print(f"p1: {p1}")
print(f"p2: {p2}")

# Addition
p3 = p1 + p2
print(f"p1 + p2 = {p3}")

# Subtraction
p4 = p1 - p2
print(f"p1 - p2 = {p4}")

# Equality check
print(f"Is p1 == p2? {p1 == p2}")
print(f"Is p1 == Point(3, 4)? {p1 == Point(3, 4)}")

# Length
print(f"Length of p1: {len(p1)}")  # 5 (3-4-5 triangle)

# Calling the object
p5 = p1(2)  # Multiply coordinates by 2
print(f"p1(2) = {p5}")
