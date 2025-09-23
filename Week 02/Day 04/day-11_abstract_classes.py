"""
======================================================
Python Learning - Week 02 Day 04 (Day 11 Overall)
TOPIC: ABSTRACT CLASSES AND INTERFACES
======================================================

DESCRIPTION:
This file explores abstract classes and interfaces in Python, which allow
you to define common APIs that derived classes must implement. While Python
doesn't have formal interfaces like Java, we can use abstract base classes
to achieve similar functionality.

TOPICS COVERED:
1. Abstract Base Classes (ABC)
2. Abstract methods
3. Creating interfaces with ABCs
4. Concrete implementations
5. Duck typing vs formal interfaces

LEARNING OUTCOMES:
- Create abstract base classes that define interfaces
- Implement abstract methods in concrete classes
- Understand when and why to use abstract classes
- Apply abstract classes to design better APIs

======================================================
"""

# =====================================================
# 1. ABSTRACT BASE CLASSES
# =====================================================
print("=" * 50)
print("1. ABSTRACT BASE CLASSES")
print("=" * 50)

"""
Abstract Base Classes (ABCs) are classes that cannot be instantiated and
are designed to be subclassed. They often include abstract methods that
derived classes must implement.
"""

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass

    # Concrete method in abstract class
    def describe(self):
        return f"This is a {self.color} shape with area {self.area()} and perimeter {self.perimeter()}"

# Try to instantiate an abstract class
try:
    shape = Shape("purple")  # This will raise an error
except TypeError as e:
    print(f"Cannot instantiate abstract class: {e}")

# =====================================================
# 2. IMPLEMENTING ABSTRACT CLASSES
# =====================================================
print("\n" + "=" * 50)
print("2. IMPLEMENTING ABSTRACT CLASSES")
print("=" * 50)

# Concrete implementation of Shape
class Rectangle(Shape):
    def __init__(self, width, height, color="blue"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius, color="red"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Create concrete shapes
rectangle = Rectangle(5, 4)
circle = Circle(3)

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle description: {rectangle.describe()}")

print(f"\nCircle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")
print(f"Circle description: {circle.describe()}")

# =====================================================
# 3. ABSTRACT CLASS AS INTERFACE
# =====================================================
print("\n" + "=" * 50)
print("3. ABSTRACT CLASS AS INTERFACE")
print("=" * 50)

"""
Python doesn't have explicit interfaces like Java, but abstract classes
can serve as interfaces by defining a set of methods that implementing
classes must provide.
"""

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process a payment"""
        pass

    @abstractmethod
    def refund(self, amount):
        """Process a refund"""
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        # In a real system, this would connect to a payment gateway
        masked_card = "xxxx-xxxx-xxxx-" + self.card_number[-4:]
        return f"Paid ${amount} with credit card {masked_card}"

    def refund(self, amount):
        masked_card = "xxxx-xxxx-xxxx-" + self.card_number[-4:]
        return f"Refunded ${amount} to credit card {masked_card}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid ${amount} with PayPal account {self.email}"

    def refund(self, amount):
        return f"Refunded ${amount} to PayPal account {self.email}"

# Using the processors polymorphically
cc_processor = CreditCardProcessor("1234-5678-9012-3456", "12/25", "123")
paypal_processor = PayPalProcessor("user@example.com")

# Process payments with either processor
def process_payment(processor, amount):
    return processor.pay(amount)

print(process_payment(cc_processor, 100))
print(process_payment(paypal_processor, 50))

# Try with incomplete implementation
try:
    class IncompleteProcessor(PaymentProcessor):
        def pay(self, amount):
            return f"Paid ${amount}"
        # Missing refund method

    incomplete = IncompleteProcessor()
except TypeError as e:
    print(f"\nError with incomplete implementation: {e}")

# =====================================================
# 4. ABSTRACT PROPERTIES
# =====================================================
print("\n" + "=" * 50)
print("4. ABSTRACT PROPERTIES")
print("=" * 50)

"""
Abstract base classes can also define abstract properties that
subclasses must implement.
"""

class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self):
        """Number of wheels"""
        pass

    @abstractmethod
    def drive(self):
        """Drive the vehicle"""
        pass

    def describe(self):
        return f"This vehicle has {self.wheels} wheels"

class Bicycle(Vehicle):
    @property
    def wheels(self):
        return 2

    def drive(self):
        return "Pedaling the bicycle"

class Car(Vehicle):
    @property
    def wheels(self):
        return 4

    def drive(self):
        return "Driving the car"

# Create vehicles
bicycle = Bicycle()
car = Car()

print(f"Bicycle: {bicycle.describe()}")
print(f"Bicycle action: {bicycle.drive()}")

print(f"Car: {car.describe()}")
print(f"Car action: {car.drive()}")

# =====================================================
# 5. DUCK TYPING VS FORMAL INTERFACES
# =====================================================
print("\n" + "=" * 50)
print("5. DUCK TYPING VS FORMAL INTERFACES")
print("=" * 50)

"""
Python supports both duck typing ("if it walks like a duck and quacks like a duck...")
and more formal interfaces through ABCs. Let's compare them.
"""

print("Duck typing example:")

# Function using duck typing
def process_shape(shape):
    """Just needs objects with area() and perimeter() methods"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# This class doesn't inherit from Shape but provides the same methods
class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# This works with duck typing
triangle = Triangle(5, 4, 3, 4, 5)
print("\nUsing triangle with process_shape():")
process_shape(triangle)

print("\nAdvantages of duck typing:")
print("1. More flexible - any object with required methods works")
print("2. Simpler code - no inheritance required")
print("3. Follows Python's 'we're all consenting adults' philosophy")

print("\nAdvantages of abstract base classes:")
print("1. Clear documentation of required methods")
print("2. Enforcement of method implementation")
print("3. Runtime type checking with isinstance()")
print("4. More explicit about design intentions")

# Check if our classes adhere to interfaces
print("\nType checking:")
print(f"Is rectangle a Shape? {isinstance(rectangle, Shape)}")
print(f"Is triangle a Shape? {isinstance(triangle, Shape)}")

# We can register a class with an ABC even after defining it
print("\nRegistering a class with an ABC after definition:")
Shape.register(Triangle)
print(f"Is triangle a Shape now? {isinstance(triangle, Shape)}")  # Still False because registration doesn't check methods

print("\nPython allows both approaches - choose based on your needs!")
print("- Use ABCs for library APIs and frameworks")
print("- Use duck typing for simpler code within your application")
