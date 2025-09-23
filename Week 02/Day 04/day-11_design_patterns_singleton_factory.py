"""
======================================================
Python Learning - Week 02 Day 04 (Day 11 Overall)
TOPIC: DESIGN PATTERNS - SINGLETON & FACTORY
======================================================

DESCRIPTION:
This file explores two important design patterns: Singleton and Factory.
Design patterns are typical solutions to common problems in software design.
They represent best practices evolved over time by experienced developers.

TOPICS COVERED:
1. Singleton Pattern
2. Implementing Singleton in Python
3. Factory Pattern
4. Factory Method vs Abstract Factory
5. When to use these patterns

LEARNING OUTCOMES:
- Understand the purpose and implementation of the Singleton pattern
- Create various implementations of Singleton in Python
- Implement the Factory pattern for object creation
- Recognize situations where these patterns are appropriate
- Apply these patterns to solve design problems

======================================================
"""

# =====================================================
# 1. SINGLETON PATTERN
# =====================================================
print("=" * 50)
print("1. SINGLETON PATTERN")
print("=" * 50)

"""
The Singleton pattern ensures a class has only one instance and
provides a global point to access it.

Uses:
- Configuration managers
- Database connections
- Logging services
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new Singleton instance")
            cls._instance = super().__new__(cls)
            # Initialize here if needed
            cls._instance.value = 0
        return cls._instance

# Testing the Singleton
print("Creating first instance:")
s1 = Singleton()
s1.value = 42

print("Creating second instance:")
s2 = Singleton()
print(f"s1.value: {s1.value}, s2.value: {s2.value}")  # Both should be 42
print(f"Are s1 and s2 the same object? {s1 is s2}")   # Should be True

# Modifying through one reference affects the other
s2.value = 100
print(f"After s2.value = 100: s1.value = {s1.value}")  # Should be 100

# =====================================================
# 2. SINGLETON IMPLEMENTATIONS IN PYTHON
# =====================================================
print("\n" + "=" * 50)
print("2. SINGLETON IMPLEMENTATIONS IN PYTHON")
print("=" * 50)

"""
There are multiple ways to implement Singletons in Python, each with
their own advantages and disadvantages.
"""

# Method 1: Decorator-based singleton
print("\nDecorator-based Singleton:")

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class ConfigManager:
    def __init__(self):
        print("Initializing Config Manager")
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)

# Testing our decorated singleton
print("Creating first config:")
config1 = ConfigManager()
config1.set("theme", "dark")

print("Creating second config:")
config2 = ConfigManager()  # Should not print "Initializing" again
print(f"config2.get('theme'): {config2.get('theme')}")  # Should be "dark"
print(f"Are config1 and config2 the same? {config1 is config2}")  # Should be True

# Method 2: Metaclass-based singleton
print("\nMetaclass-based Singleton:")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Creating new {cls.__name__} instance")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.log_count = 0

    def log(self, message):
        self.log_count += 1
        print(f"[LOG {self.log_count}] {message}")

# Testing metaclass singleton
print("Creating first logger:")
logger1 = Logger()
logger1.log("System starting")

print("Creating second logger:")
logger2 = Logger()  # Should not print "Creating new" again
logger2.log("User logged in")  # Log count should continue from previous instance

# Method 3: Module-level singleton
print("\nModule-level Singleton:")
print("(In Python, modules are singletons by default)")
print("This is why you often see singletons implemented simply as module-level variables/functions")

# =====================================================
# 3. FACTORY PATTERN
# =====================================================
print("\n" + "=" * 50)
print("3. FACTORY PATTERN")
print("=" * 50)

"""
The Factory Pattern provides an interface for creating objects without
specifying their concrete classes. This allows for more flexible and 
decoupled code.
"""

# Simple Factory Pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        elif animal_type.lower() == "cow":
            return Cow()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Using the factory
animal_types = ["dog", "cat", "cow"]
for animal_type in animal_types:
    animal = AnimalFactory.create_animal(animal_type)
    print(f"{animal_type.capitalize()} says: {animal.speak()}")

# Let's try with an invalid type
try:
    AnimalFactory.create_animal("elephant")
except ValueError as e:
    print(f"Error: {e}")

# =====================================================
# 4. FACTORY METHOD PATTERN
# =====================================================
print("\n" + "=" * 50)
print("4. FACTORY METHOD PATTERN")
print("=" * 50)

"""
The Factory Method Pattern is a creational pattern that uses factory methods
to deal with the problem of creating objects without specifying the exact
class of object that will be created.
"""

from abc import ABC, abstractmethod

# Product classes
class Vehicle(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, num_doors=4):
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.vehicle_type = "Car"

    def get_description(self):
        return f"{self.make} {self.model}, {self.num_doors}-door {self.vehicle_type}"

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar=False):
        self.make = make
        self.model = model
        self.has_sidecar = has_sidecar
        self.vehicle_type = "Motorcycle"

    def get_description(self):
        sidecar = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{self.make} {self.model}, {self.vehicle_type} {sidecar}"

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        self.make = make
        self.model = model
        self.payload_capacity = payload_capacity
        self.vehicle_type = "Truck"

    def get_description(self):
        return f"{self.make} {self.model}, {self.vehicle_type} with {self.payload_capacity}kg capacity"

# Creator classes
class VehicleManufacturer(ABC):
    @abstractmethod
    def create_vehicle(self):
        """Factory method"""
        pass

    def deliver_vehicle(self):
        # Call the factory method to create a vehicle
        vehicle = self.create_vehicle()
        return f"Delivering a new vehicle: {vehicle.get_description()}"

class CarManufacturer(VehicleManufacturer):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def create_vehicle(self):
        return Car(self.make, self.model)

class MotorcycleManufacturer(VehicleManufacturer):
    def __init__(self, make, model, has_sidecar):
        self.make = make
        self.model = model
        self.has_sidecar = has_sidecar

    def create_vehicle(self):
        return Motorcycle(self.make, self.model, self.has_sidecar)

class TruckManufacturer(VehicleManufacturer):
    def __init__(self, make, model, payload_capacity):
        self.make = make
        self.model = model
        self.payload_capacity = payload_capacity

    def create_vehicle(self):
        return Truck(self.make, self.model, self.payload_capacity)

# Using the factory method
manufacturers = [
    CarManufacturer("Toyota", "Camry"),
    MotorcycleManufacturer("Harley-Davidson", "Sportster", False),
    TruckManufacturer("Ford", "F-150", 1500)
]

print("Factory Method Pattern - Creating and delivering vehicles:")
for manufacturer in manufacturers:
    print(manufacturer.deliver_vehicle())

# =====================================================
# 5. ABSTRACT FACTORY PATTERN
# =====================================================
print("\n" + "=" * 50)
print("5. ABSTRACT FACTORY PATTERN")
print("=" * 50)

"""
The Abstract Factory Pattern provides an interface for creating families of
related or dependent objects without specifying their concrete classes.
"""

# Product interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete products for Windows
class WindowsButton(Button):
    def render(self):
        return "[Windows Button]"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "[Windows Checkbox]"

# Concrete products for macOS
class MacOSButton(Button):
    def render(self):
        return "[MacOS Button]"

class MacOSCheckbox(Checkbox):
    def render(self):
        return "[MacOS Checkbox]"

# Abstract Factory interface
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete factories
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacOSFactory(UIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Client code that uses the factory
class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def render_ui(self):
        button_output = self.button.render()
        checkbox_output = self.checkbox.render()
        return f"UI elements: {button_output} and {checkbox_output}"

# Configure the application based on the operating system
import platform

def create_os_factory():
    os_name = platform.system()
    if os_name == "Windows":
        return WindowsFactory()
    elif os_name == "Darwin":  # macOS
        return MacOSFactory()
    else:
        # For this example, default to Windows if not recognized
        print(f"OS {os_name} not recognized, using Windows factory as default")
        return WindowsFactory()

# For demonstration purposes, let's manually create both factories
print("Creating applications with different UI factories:")

windows_app = Application(WindowsFactory())
windows_app.create_ui()
print(f"Windows app: {windows_app.render_ui()}")

mac_app = Application(MacOSFactory())
mac_app.create_ui()
print(f"MacOS app: {mac_app.render_ui()}")

# In a real application, we would determine the factory based on the OS
current_os_factory = create_os_factory()
app = Application(current_os_factory)
app.create_ui()
print(f"\nAutomatically selected UI: {app.render_ui()}")

# =====================================================
# 6. WHEN TO USE THESE PATTERNS
# =====================================================
print("\n" + "=" * 50)
print("6. WHEN TO USE THESE PATTERNS")
print("=" * 50)

print("When to use the Singleton Pattern:")
print("1. When exactly one instance of a class is needed")
print("2. When the instance should be accessible globally")
print("3. Examples: configuration managers, connection pools, loggers")

print("\nWhen to use Factory Patterns:")
print("1. When a system should be independent from how its products are created")
print("2. When you need to work with multiple families of related products")
print("3. When you want to provide a library of products and reveal only their interfaces")
print("4. Examples: UI libraries, document generators, cross-platform applications")

print("\nAdvantages of Factory Patterns:")
print("1. You avoid tight coupling between creator and concrete products")
print("2. Single Responsibility Principle: you can move product creation code into one place")
print("3. Open/Closed Principle: you can introduce new types of products without breaking existing code")

print("\nDesign patterns solve common problems, but shouldn't be applied blindly.")
print("Always consider the specific needs and constraints of your application.")
