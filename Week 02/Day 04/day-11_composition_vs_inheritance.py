"""
======================================================
Python Learning - Week 02 Day 04 (Day 11 Overall)
TOPIC: COMPOSITION VS INHERITANCE
======================================================

DESCRIPTION:
This file explores the key differences between composition and inheritance
in Object-Oriented Programming. Both are strategies for code reuse, but they
follow different design philosophies. We'll see when to use each approach
and why many programmers follow the principle "favor composition over inheritance".

TOPICS COVERED:
1. Inheritance review ("is-a" relationship)
2. Composition basics ("has-a" relationship)
3. Comparing the approaches
4. Complex composition example
5. When to use each approach

LEARNING OUTCOMES:
- Understand the difference between inheritance and composition
- Identify when to use each approach for different design problems
- Apply composition for flexible, modular designs
- Recognize common composition patterns

======================================================
"""

# =====================================================
# 1. INHERITANCE REVIEW
# =====================================================
print("=" * 50)
print("1. INHERITANCE REVIEW")
print("=" * 50)

"""
Inheritance creates an "is-a" relationship:
- A Car is a Vehicle
- A Dog is an Animal
"""

# Inheritance approach (is-a relationship)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return f"{self.make} {self.model} engine starting..."

    def stop(self):
        return f"{self.make} {self.model} engine stopping..."

class Car(Vehicle):
    def __init__(self, make, model, car_type):
        super().__init__(make, model)
        self.car_type = car_type
        self.is_moving = False

    def drive(self):
        self.is_moving = True
        return f"{self.make} {self.model} is now driving"

# Using inheritance
my_car = Car("Toyota", "Corolla", "Sedan")
print(my_car.start())  # Inherited method
print(my_car.drive())  # Car-specific method

# =====================================================
# 2. COMPOSITION BASICS
# =====================================================
print("\n" + "=" * 50)
print("2. COMPOSITION BASICS")
print("=" * 50)

"""
Composition creates a "has-a" relationship:
- A Car has an Engine
- A Dog has a Collar
"""

class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return f"{self.power}hp engine starting..."

    def stop(self):
        return f"{self.power}hp engine stopping..."

class CarComposition:
    def __init__(self, make, model, engine_power):
        self.make = make
        self.model = model
        # Composition: Car has an Engine
        self.engine = Engine(engine_power)
        self.is_moving = False

    def start_engine(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

    def stop_engine(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"

    def drive(self):
        self.is_moving = True
        return f"{self.make} {self.model} is now driving"

# Using composition
composed_car = CarComposition("Honda", "Civic", 180)
print(composed_car.start_engine())
print(composed_car.drive())

# =====================================================
# 3. COMPARING THE APPROACHES
# =====================================================
print("\n" + "=" * 50)
print("3. COMPARING THE APPROACHES")
print("=" * 50)

print("Advantages of Inheritance:")
print("1. Direct access to parent methods and attributes")
print("2. Clear 'is-a' relationship when that's what you need")
print("3. Polymorphism through inheritance hierarchies")
print("4. Support for method overriding")

print("\nAdvantages of Composition:")
print("1. More flexible - can change behavior at runtime")
print("2. Avoids deep inheritance hierarchies (easier to understand)")
print("3. Less coupling between classes")
print("4. Better for code reuse when there's no clear 'is-a' relationship")
print("5. Follows 'favor composition over inheritance' principle")

print("\nWhen to use each:")
print("- Inheritance: When subclass IS-A superclass (true subtype relationship)")
print("- Composition: When class HAS-A component (aggregation relationship)")

# =====================================================
# 4. COMPLEX COMPOSITION EXAMPLE
# =====================================================
print("\n" + "=" * 50)
print("4. COMPLEX COMPOSITION EXAMPLE")
print("=" * 50)

"""
A complex example showing the power of composition with
a smartphone built from multiple components.
"""

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge_level = 100  # Percent

    def use_power(self, amount):
        if self.charge_level >= amount:
            self.charge_level -= amount
            return True
        return False

    def recharge(self, amount):
        self.charge_level = min(100, self.charge_level + amount)
        return f"Battery recharged to {self.charge_level}%"

    def status(self):
        return f"{self.capacity}mAh battery at {self.charge_level}%"

class Display:
    def __init__(self, size, resolution):
        self.size = size
        self.resolution = resolution
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return f"{self.size}\" display turned on at {self.resolution}"

    def turn_off(self):
        self.is_on = False
        return "Display turned off"

    def show_content(self, content):
        if self.is_on:
            return f"Displaying: {content}"
        return "Cannot display content - screen is off"

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        return f"Taking a {self.megapixels}MP photo"

    def record_video(self, seconds):
        return f"Recording {seconds} seconds of video at {self.megapixels}MP"

class Smartphone:
    def __init__(self, brand, model, screen_size, resolution, battery_capacity, camera_mp):
        self.brand = brand
        self.model = model
        # Composition: smartphone has various components
        self.display = Display(screen_size, resolution)
        self.battery = Battery(battery_capacity)
        self.camera = Camera(camera_mp)
        self.is_powered_on = False

    def power_on(self):
        if self.battery.charge_level > 5:
            self.is_powered_on = True
            self.battery.use_power(5)  # Power on uses battery
            self.display.turn_on()
            return f"{self.brand} {self.model} powered on"
        return f"Cannot power on: battery too low ({self.battery.charge_level}%)"

    def power_off(self):
        self.is_powered_on = False
        self.display.turn_off()
        return f"{self.brand} {self.model} powered off"

    def use_app(self, app_name):
        if not self.is_powered_on:
            return "Phone is off"

        if self.battery.use_power(10):  # Using app consumes battery
            return self.display.show_content(f"Running {app_name} app")
        else:
            self.power_off()
            return "Phone turned off due to low battery"

    def take_picture(self):
        if not self.is_powered_on:
            return "Phone is off"

        if self.battery.use_power(5):  # Taking pictures uses battery
            return self.camera.take_photo()
        else:
            self.power_off()
            return "Phone turned off due to low battery"

    def charge(self, amount):
        return f"{self.brand} {self.model}: {self.battery.recharge(amount)}"

    def status(self):
        power = "ON" if self.is_powered_on else "OFF"
        return f"{self.brand} {self.model} - Power: {power}, {self.battery.status()}"

# Using our composed smartphone
iphone = Smartphone("Apple", "iPhone 14", 6.1, "2532x1170", 3279, 48)
print(iphone.status())
print(iphone.power_on())
print(iphone.use_app("Maps"))
print(iphone.take_picture())
print(iphone.use_app("Games"))  # Uses more battery
print(iphone.status())
print(iphone.charge(30))
print(iphone.status())
print(iphone.power_off())

# =====================================================
# 5. REAL-WORLD COMPOSITION PATTERNS
# =====================================================
print("\n" + "=" * 50)
print("5. REAL-WORLD COMPOSITION PATTERNS")
print("=" * 50)

print("Common composition patterns:")
print("1. Strategy Pattern - inject behavior")
print("2. Decorator Pattern - add functionality dynamically")
print("3. Composite Pattern - tree-like object structures")
print("4. Bridge Pattern - separate abstraction from implementation")

# Example of Strategy Pattern with Composition
print("\nStrategy Pattern Example:")

class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date):
        self.card_number = card_number
        self.expiry_date = expiry_date

    def pay(self, amount):
        return f"Paid ${amount} with credit card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid ${amount} with PayPal account {self.email}"

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, name, price):
        self.items.append((name, price))

    def calculate_total(self):
        return sum(price for _, price in self.items)

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self):
        if not self.payment_strategy:
            return "No payment strategy set"

        amount = self.calculate_total()
        if amount == 0:
            return "Cart is empty"

        result = self.payment_strategy.pay(amount)
        self.items = []  # Clear cart after checkout
        return result

# Use the strategy pattern
cart = ShoppingCart()
cart.add_item("Laptop", 1299.99)
cart.add_item("Mouse", 25.99)

# Set payment strategy and checkout
cart.set_payment_strategy(CreditCardPayment("4111111111111111", "12/25"))
print(cart.checkout())

# Change payment strategy dynamically
cart.add_item("Headphones", 149.99)
cart.set_payment_strategy(PayPalPayment("customer@example.com"))
print(cart.checkout())

print("\nComposition allows us to change behavior at runtime and create more flexible designs!")
