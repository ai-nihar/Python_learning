"""
======================================================
Python Learning - Week 02 Day 03 (Day 10 Overall)
TOPIC: POLYMORPHISM
======================================================

DESCRIPTION:
This file explores polymorphism in Python, one of the four pillars of
Object-Oriented Programming. Polymorphism allows objects of different classes
to be treated as objects of a common superclass, enabling more flexible and
reusable code.

TOPICS COVERED:
1. Polymorphism with inheritance
2. Duck typing
3. Method overriding for polymorphic behavior
4. Polymorphism in practice

LEARNING OUTCOMES:
- Understand how polymorphism works in Python
- Apply polymorphism for more flexible code design
- Leverage duck typing for increased flexibility
- Implement polymorphic interfaces in your classes

======================================================
"""

# =====================================================
# 1. POLYMORPHISM WITH INHERITANCE
# =====================================================
print("=" * 50)
print("1. POLYMORPHISM WITH INHERITANCE")
print("=" * 50)

"""
Polymorphism allows objects of different classes to be treated as objects
of a common superclass. The most common use is when a parent class reference
is used to refer to a child class object.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

    def introduce(self):
        return f"I am {self.name}, and I can {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "bark"

    def fetch(self):
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def speak(self):
        return "meow"

    def scratch(self):
        return f"{self.name} is scratching the furniture"

class Duck(Animal):
    def speak(self):
        return "quack"

    def swim(self):
        return f"{self.name} is swimming in the pond"

# Create animal instances
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Donald")

# Polymorphism in action
animals = [dog, cat, duck]

print("Different animals speaking:")
for animal in animals:
    # The same method call behaves differently depending on the actual object type
    print(f"{animal.name} says {animal.speak()}")
    print(f"Introduction: {animal.introduce()}")

# We can also use the specific methods when we know the actual type
print("\nType-specific behaviors:")
print(dog.fetch())
print(cat.scratch())
print(duck.swim())

# =====================================================
# 2. DUCK TYPING
# =====================================================
print("\n" + "=" * 50)
print("2. DUCK TYPING")
print("=" * 50)

"""
Duck typing is a concept where the type or class of an object is less important
than the methods it defines or the operations you can perform on it.

"If it walks like a duck and quacks like a duck, then it probably is a duck."

In Python, this means if an object implements certain methods, it can be 
used in contexts where those methods are expected, regardless of its actual type.
"""

# Duck typing example
def make_animal_speak(animal):
    # This function works with any object that has a speak() method
    # It doesn't care about the class hierarchy
    return animal.speak()

# This works even with a completely unrelated class
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "hello"

person = Person("John")
print(f"Person says: {make_animal_speak(person)}")  # This works!

# Another example of duck typing with a collection of different types
class Robot:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "beep boop"

# Add the robot to our collection of speakers
robot = Robot("R2D2")
speakers = [dog, cat, duck, person, robot]

print("\nAll speakers:")
for speaker in speakers:
    print(f"{speaker.name} says: {speaker.speak()}")

# This flexibility is powerful but can also lead to errors if not careful
try:
    class BrokenSpeaker:
        def __init__(self, name):
            self.name = name

        # Note: No speak() method!

    broken = BrokenSpeaker("Broken")
    print(make_animal_speak(broken))
except AttributeError as e:
    print(f"\nError with broken speaker: {e}")
    print("This demonstrates the risk of duck typing: no compile-time checks")

# =====================================================
# 3. POLYMORPHISM FOR EXTENSIBILITY
# =====================================================
print("\n" + "=" * 50)
print("3. POLYMORPHISM FOR EXTENSIBILITY")
print("=" * 50)

"""
Polymorphism allows for code to be extended without modifying existing code.
This is a key component of the Open/Closed Principle (open for extension,
closed for modification).
"""

class Shape:
    def area(self):
        pass  # Abstract method to be implemented by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function that works with any Shape object
def calculate_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Create a collection of different shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8),
    Circle(2)
]

# Calculate the total area
total_area = calculate_total_area(shapes)
print(f"Total area of all shapes: {total_area:.2f}")

# We can add a new shape without modifying the calculate_total_area function
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Add a square to our collection
shapes.append(Square(4))
total_area = calculate_total_area(shapes)
print(f"New total area with square added: {total_area:.2f}")

# =====================================================
# 4. REAL-WORLD POLYMORPHISM EXAMPLE
# =====================================================
print("\n" + "=" * 50)
print("4. REAL-WORLD POLYMORPHISM EXAMPLE")
print("=" * 50)

"""
Let's implement a more realistic example of polymorphism using a
payment processing system.
"""

class PaymentMethod:
    def process_payment(self, amount):
        """Process a payment of the given amount."""
        raise NotImplementedError("Subclasses must implement this method")

    def payment_details(self):
        """Return payment method details."""
        raise NotImplementedError("Subclasses must implement this method")

class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiry_date, cvv):
        # In a real system, we would validate these values
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self, amount):
        # In a real system, this would connect to a payment gateway
        last_4 = self.card_number[-4:]
        return f"Processing ${amount:.2f} payment with credit card ending in {last_4}"

    def payment_details(self):
        return f"Credit Card ending in {self.card_number[-4:]}"

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} payment with PayPal account {self.email}"

    def payment_details(self):
        return f"PayPal ({self.email})"

class BankTransfer(PaymentMethod):
    def __init__(self, account_number, routing_number):
        self.account_number = account_number
        self.routing_number = routing_number

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} payment with bank transfer to account {self.account_number[-4:]}"

    def payment_details(self):
        return f"Bank Transfer to account ending in {self.account_number[-4:]}"

# A shopping cart that uses polymorphism for payment processing
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append((name, price, quantity))

    def total(self):
        return sum(price * quantity for _, price, quantity in self.items)

    def checkout(self, payment_method):
        total_amount = self.total()
        if total_amount <= 0:
            return "Cart is empty, nothing to pay"

        # Polymorphic call to process_payment
        payment_result = payment_method.process_payment(total_amount)

        # Clear the cart after successful payment
        self.items.clear()

        return f"Checkout successful! {payment_result}"

# Create a shopping cart and add items
cart = ShoppingCart()
cart.add_item("Laptop", 1299.99)
cart.add_item("Mouse", 25.99, 2)
cart.add_item("Keyboard", 59.99)

# Display cart total
print(f"Cart total: ${cart.total():.2f}")

# Create different payment methods
credit_card = CreditCard("4111111111111111", "12/25", "123")
paypal = PayPal("customer@example.com")
bank_transfer = BankTransfer("9876543210", "021000021")

# Process checkout with different payment methods
payment_methods = [credit_card, paypal, bank_transfer]
print("\nAvailable payment methods:")
for i, method in enumerate(payment_methods, 1):
    print(f"{i}. {method.payment_details()}")

print("\nCheckout using different payment methods:")
# This demonstrates polymorphism - same method call, different behavior
print(cart.checkout(credit_card))
# Refill the cart for next payment method
cart.add_item("Laptop", 1299.99)
cart.add_item("Mouse", 25.99, 2)
cart.add_item("Keyboard", 59.99)
print(cart.checkout(paypal))

print("\nPolymorphism makes our code more flexible and extensible!")
