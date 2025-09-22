"""
======================================================
Python Learning - Week 02 Day 03 (Day 10 Overall)
TOPIC: MULTIPLE INHERITANCE AND MRO
======================================================

DESCRIPTION:
This file explores multiple inheritance in Python, where a class can inherit
from more than one parent class. We'll also learn about the Method Resolution
Order (MRO), which determines how Python resolves method calls in complex
inheritance hierarchies.

TOPICS COVERED:
1. Multiple inheritance basics
2. Method Resolution Order (MRO)
3. The diamond problem
4. Best practices for multiple inheritance

LEARNING OUTCOMES:
- Implement classes that inherit from multiple parent classes
- Understand how Python resolves method calls with MRO
- Solve common problems associated with multiple inheritance
- Apply multiple inheritance effectively and safely

======================================================
"""

# =====================================================
# 1. MULTIPLE INHERITANCE BASICS
# =====================================================
print("=" * 50)
print("1. MULTIPLE INHERITANCE BASICS")
print("=" * 50)

"""
Multiple inheritance allows a class to inherit from multiple parent classes.
This can be powerful but also complex if not used carefully.
"""

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Device: {self.brand} {self.model}"

class Portable:
    def __init__(self, weight):
        self.weight = weight

    def is_heavy(self):
        return self.weight > 1  # kg

    def info(self):
        heavy_status = "heavy" if self.is_heavy() else "light"
        return f"This is a {heavy_status} portable device weighing {self.weight}kg"

# Multiple inheritance
class Laptop(Device, Portable):
    def __init__(self, brand, model, weight, battery_life):
        # Initialize both parent classes
        Device.__init__(self, brand, model)
        Portable.__init__(self, weight)
        # Add laptop-specific attribute
        self.battery_life = battery_life

    # Override the info method with super()
    def info(self):
        # Method Resolution Order determines which parent's method is called first
        device_info = Device.info(self)
        return f"{device_info}, Battery: {self.battery_life}h, Weight: {self.weight}kg"

# Create a laptop
laptop = Laptop("Dell", "XPS 13", 1.2, 10)

print(f"Brand: {laptop.brand}")
print(f"Model: {laptop.model}")
print(f"Weight: {laptop.weight}kg")
print(f"Battery life: {laptop.battery_life}h")
print(f"Is heavy? {laptop.is_heavy()}")

# Method Resolution Order (MRO) determines which method is called
print(f"Info: {laptop.info()}")
print(f"MRO: {[cls.__name__ for cls in Laptop.__mro__]}")  # Shows method resolution order

# =====================================================
# 2. METHOD RESOLUTION ORDER (MRO)
# =====================================================
print("\n" + "=" * 50)
print("2. METHOD RESOLUTION ORDER (MRO)")
print("=" * 50)

"""
The Method Resolution Order (MRO) is the order in which Python looks for
methods and attributes in a class hierarchy. Python uses the C3 Linearization
algorithm to determine the MRO.
"""

# Simple example of MRO
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

# Let's see the MRO
print("Method Resolution Order (MRO) for class D:")
print(f"D.__mro__: {[cls.__name__ for cls in D.__mro__]}")

# Which method gets called?
d = D()
print(f"d.method() returns: {d.method()}")  # Method from B (first in MRO)

# Explicitly calling methods from the hierarchy
print("\nExplicitly calling methods from the hierarchy:")
print(f"A.method(d) returns: {A.method(d)}")
print(f"B.method(d) returns: {B.method(d)}")
print(f"C.method(d) returns: {C.method(d)}")

# Using super() to call parent methods
class E(B, C):
    def method(self):
        return f"Method from E, then {super().method()}"

e = E()
print(f"\nE's MRO: {[cls.__name__ for cls in E.__mro__]}")
print(f"e.method() returns: {e.method()}")  # Calls E's method, then B's method (next in MRO)

# =====================================================
# 3. THE DIAMOND PROBLEM
# =====================================================
print("\n" + "=" * 50)
print("3. THE DIAMOND PROBLEM")
print("=" * 50)

"""
The Diamond Problem is a classic issue in multiple inheritance where a class
inherits from two classes that both inherit from a common base class.
Python's MRO resolves this using the C3 linearization algorithm.
"""

print("Diamond inheritance diagram:")
print("    A")
print("   / \\")
print("  B   C")
print("   \\ /")
print("    D")

# Implementing the diamond
class Base:
    def __init__(self):
        print("Base init called")

    def method(self):
        return "Method from Base"

class Left(Base):
    def __init__(self):
        print("Left init called")
        super().__init__()

    def method(self):
        return "Method from Left"

class Right(Base):
    def __init__(self):
        print("Right init called")
        super().__init__()

    def method(self):
        return "Method from Right"

class Diamond(Left, Right):
    def __init__(self):
        print("Diamond init called")
        super().__init__()

    def method(self):
        return f"Method from Diamond, then {super().method()}"

# Let's check the MRO
print(f"\nDiamond's MRO: {[cls.__name__ for cls in Diamond.__mro__]}")

# Create a Diamond object
print("\nCreating a Diamond object:")
d = Diamond()  # Notice the order of __init__ calls

print(f"d.method() returns: {d.method()}")

print("\nImportant points about the Diamond problem:")
print("1. Base.__init__() is called only once (not twice)")
print("2. The MRO determines which method implementation is called")
print("3. super() follows the MRO, not the immediate parent")
print("4. Python's C3 linearization guarantees that:")
print("   - A class always appears before its parents")
print("   - Parents are kept in the order they were listed")

# =====================================================
# 4. PRACTICAL MULTIPLE INHERITANCE
# =====================================================
print("\n" + "=" * 50)
print("4. PRACTICAL MULTIPLE INHERITANCE")
print("=" * 50)

"""
Multiple inheritance is often used for mixins - classes designed to add
functionality to other classes without requiring inheritance from a common base.
"""

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"

# Mixins - add behavior without requiring inheritance
class ElectricMixin:
    def __init__(self, battery_capacity, *args, **kwargs):
        self.battery_capacity = battery_capacity
        super().__init__(*args, **kwargs)

    def charge(self):
        return f"Charging the {self.battery_capacity}kWh battery"

class LuxuryMixin:
    def __init__(self, luxury_features=None, *args, **kwargs):
        self.luxury_features = luxury_features or []
        super().__init__(*args, **kwargs)

    def list_features(self):
        if not self.luxury_features:
            return "No luxury features"
        return f"Luxury features: {', '.join(self.luxury_features)}"

class OffRoadMixin:
    def __init__(self, ground_clearance, *args, **kwargs):
        self.ground_clearance = ground_clearance  # in inches
        super().__init__(*args, **kwargs)

    def off_road_capability(self):
        return f"Off-road capability: {self.ground_clearance} inches ground clearance"

# Using mixins to create specialized vehicles
class ElectricCar(ElectricMixin, Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(battery_capacity=battery_capacity, make=make, model=model, year=year)

class LuxurySUV(LuxuryMixin, Vehicle):
    def __init__(self, make, model, year, luxury_features):
        super().__init__(luxury_features=luxury_features, make=make, model=model, year=year)

class OffRoadTruck(OffRoadMixin, Vehicle):
    def __init__(self, make, model, year, ground_clearance):
        super().__init__(ground_clearance=ground_clearance, make=make, model=model, year=year)

# Complex example: Luxury electric off-road vehicle
class LuxuryElectricOffRoader(LuxuryMixin, ElectricMixin, OffRoadMixin, Vehicle):
    def __init__(self, make, model, year, battery_capacity, luxury_features, ground_clearance):
        super().__init__(
            luxury_features=luxury_features,
            battery_capacity=battery_capacity,
            ground_clearance=ground_clearance,
            make=make, model=model, year=year
        )

# Create vehicles
print("Creating different vehicles with mixins:")
tesla = ElectricCar("Tesla", "Model Y", 2023, 75)
print(f"Electric Car: {tesla.info()}")
print(tesla.charge())

lexus = LuxurySUV("Lexus", "RX", 2023, ["Leather seats", "Premium sound", "Advanced safety"])
print(f"\nLuxury SUV: {lexus.info()}")
print(lexus.list_features())

ford = OffRoadTruck("Ford", "F-150 Raptor", 2023, 12.5)
print(f"\nOff-road Truck: {ford.info()}")
print(ford.off_road_capability())

# Complex vehicle with multiple mixins
rivian = LuxuryElectricOffRoader(
    "Rivian", "R1S", 2023, 135,
    ["Leather seats", "Premium sound", "Auto-driving"],
    11.5
)
print(f"\nLuxury Electric Off-roader: {rivian.info()}")
print(rivian.list_features())
print(rivian.charge())
print(rivian.off_road_capability())
print(f"MRO: {[cls.__name__ for cls in LuxuryElectricOffRoader.__mro__]}")

# =====================================================
# 5. BEST PRACTICES FOR MULTIPLE INHERITANCE
# =====================================================
print("\n" + "=" * 50)
print("5. BEST PRACTICES FOR MULTIPLE INHERITANCE")
print("=" * 50)

print("1. Use multiple inheritance sparingly")
print("2. Prefer composition over inheritance when possible")
print("3. Understand the MRO of your classes")
print("4. Always use super() correctly")
print("5. Design mixins to be orthogonal (independent functionality)")
print("6. Avoid inheriting from multiple concrete classes")
print("7. Keep inheritance hierarchies as flat as possible")
print("8. Document the purpose and requirements of each mixin")
print("9. Test classes with multiple inheritance thoroughly")
print("10. Consider alternatives like composition or delegation")

print("\nMultiple inheritance can be powerful when used correctly!")
