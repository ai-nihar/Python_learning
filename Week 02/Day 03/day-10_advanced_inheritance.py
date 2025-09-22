"""
======================================================
Python Learning - Week 02 Day 03 (Day 10 Overall)
TOPIC: ADVANCED INHERITANCE
======================================================

DESCRIPTION:
This file explores advanced inheritance concepts in Python, building on
the inheritance basics covered previously. We'll learn how to create more
complex inheritance hierarchies and properly use inheritance for code reuse.

TOPICS COVERED:
1. Multi-level inheritance
2. Method overriding in depth
3. Using super() effectively
4. Inheritance hierarchies

LEARNING OUTCOMES:
- Design and implement complex inheritance hierarchies
- Use super() to call parent class methods
- Override methods while preserving parent functionality
- Understand when to use inheritance vs. other techniques

======================================================
"""

# =====================================================
# 1. ADVANCED INHERITANCE HIERARCHIES
# =====================================================
print("=" * 50)
print("1. ADVANCED INHERITANCE HIERARCHIES")
print("=" * 50)

"""
Inheritance creates an "is-a" relationship between classes.
We can build complex hierarchies to model real-world relationships.
"""

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"{self.make} {self.model} started"

    def stop(self):
        self.is_running = False
        return f"{self.make} {self.model} stopped"

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Derived class with additional features
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        # Call the parent class's __init__
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.doors = 4

    def drive(self):
        self.is_moving = True
        return f"{self.make} {self.model} is now driving"

# Another derived class
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar=False):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
        self.doors = 0  # Motorcycles don't have doors

    def wheelie(self):
        return "Doing a wheelie!" if not self.has_sidecar else "Cannot do a wheelie with a sidecar!"

# Further specialization - a derived class of Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        # Electric cars use electricity, not traditional fuel
        super().__init__(make, model, year, fuel_type="electric")
        self.battery_capacity = battery_capacity

    # Override the start method
    def start(self):
        return f"{super().start()} silently"

    def charge(self):
        return f"Charging {self.make} {self.model}'s {self.battery_capacity}kWh battery"

# Create instances of our vehicles
regular_car = Car("Toyota", "Camry", 2020, "gasoline")
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019)
electric_car = ElectricCar("Tesla", "Model 3", 2021, 75)

# Using the vehicles
print(f"Regular car: {regular_car}")
print(f"Starting: {regular_car.start()}")
print(f"Honking: {regular_car.drive()}")

print(f"\nMotorcycle: {motorcycle}")
print(f"Starting: {motorcycle.start()}")
print(f"Doing trick: {motorcycle.wheelie()}")

print(f"\nElectric car: {electric_car}")
print(f"Starting: {electric_car.start()}")  # Overridden method
print(f"Charging: {electric_car.charge()}")  # Specialized method
print(f"Fuel type: {electric_car.fuel_type}")  # Inherited and set by super().__init__

# Checking inheritance relationships
print("\nInheritance relationships:")
print(f"Is ElectricCar a Car? {isinstance(electric_car, Car)}")
print(f"Is ElectricCar a Vehicle? {isinstance(electric_car, Vehicle)}")
print(f"Is Car an ElectricCar? {isinstance(regular_car, ElectricCar)}")

# =====================================================
# 2. METHOD OVERRIDING WITH SUPER()
# =====================================================
print("\n" + "=" * 50)
print("2. METHOD OVERRIDING WITH SUPER()")
print("=" * 50)

"""
Method overriding allows a subclass to provide a specific implementation
of a method that is already defined in its superclass. The super() function
allows us to call methods from the parent class.
"""

class Shape:
    def __init__(self, color="red"):
        self.color = color

    def area(self):
        # Base implementation
        return 0

    def describe(self):
        return f"A {self.color} shape with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, width, height, color="blue"):
        # Call parent constructor with super()
        super().__init__(color)
        self.width = width
        self.height = height

    # Override area method
    def area(self):
        return self.width * self.height

    # Override describe method but also use the parent's implementation
    def describe(self):
        base_description = super().describe()
        return f"{base_description} (a rectangle with width={self.width}, height={self.height})"

class Circle(Shape):
    def __init__(self, radius, color="green"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Create shapes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Using the overridden methods
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle description: {rectangle.describe()}")

print(f"\nCircle area: {circle.area()}")
print(f"Circle description: {circle.describe()}")

# =====================================================
# 3. MULTI-LEVEL INHERITANCE
# =====================================================
print("\n" + "=" * 50)
print("3. MULTI-LEVEL INHERITANCE")
print("=" * 50)

"""
Multi-level inheritance creates a hierarchy where a derived class becomes
the base class for another class.
"""

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

# Intermediate class
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying with a wingspan of {self.wingspan} inches"

    def sing(self):
        return f"{self.name} is singing"

# Derived class from Bird
class Parrot(Bird):
    def __init__(self, name, wingspan, color):
        super().__init__(name, wingspan)
        self.color = color

    def speak(self, words):
        return f"{self.name}, the {self.color} parrot, says: '{words}'"

    # Override the sing method
    def sing(self):
        return f"{super().sing()} a beautiful melody"

# Create instances at different levels
generic_animal = Animal("Generic")
canary = Bird("Tweety", 7)
parrot = Parrot("Polly", 12, "green")

# Use methods from different levels
print("Testing multi-level inheritance:")
print(generic_animal.eat())  # From Animal

print(canary.eat())     # Inherited from Animal
print(canary.fly())     # From Bird

print(parrot.eat())     # Inherited from Animal
print(parrot.fly())     # Inherited from Bird
print(parrot.sing())    # Overridden in Parrot
print(parrot.speak("Hello, world!"))  # From Parrot

# =====================================================
# 4. INHERITANCE BEST PRACTICES
# =====================================================
print("\n" + "=" * 50)
print("4. INHERITANCE BEST PRACTICES")
print("=" * 50)

print("When to use inheritance:")
print("1. For 'is-a' relationships (Dog is an Animal)")
print("2. When you want to reuse code from existing classes")
print("3. When you want polymorphic behavior")
print("\nInheritance pitfalls to avoid:")
print("1. Excessive depth (deep hierarchies are hard to understand)")
print("2. Multiple inheritance can lead to complexity")
print("3. Inheritance for code reuse when there's no 'is-a' relationship")
print("4. Overriding methods without understanding parent behavior")

print("\nAlternatives to inheritance:")
print("1. Composition (has-a relationship)")
print("2. Delegation (forwarding calls to a contained object)")
print("3. Mixins/Traits (for reusing code without is-a relationship)")

print("\nRemember: 'Favor composition over inheritance' is a good guideline!")
