"""
======================================================
Python Learning - Week 02 Day 02 (Day 9 Overall)
TOPIC: INHERITANCE BASICS
======================================================

DESCRIPTION:
This file introduces inheritance, one of the core principles of
Object-Oriented Programming. Inheritance allows a class to inherit
attributes and methods from another class, enabling code reuse
and establishing relationships between classes.

TOPICS COVERED:
1. Basic inheritance
2. The super() function
3. Method overriding
4. Checking instance relationships

LEARNING OUTCOMES:
- Create parent-child class relationships
- Use the super() function to call parent methods
- Override methods in subclasses
- Test object relationships with isinstance()

======================================================
"""

# =====================================================
# 1. BASIC INHERITANCE
# =====================================================
print("=" * 50)
print("1. BASIC INHERITANCE")
print("=" * 50)

# Parent class (base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"{self.name} is a {self.species}"

# Child class (derived class)
class Dog(Animal):
    def __init__(self, name, breed):
        # Initialize the parent class
        super().__init__(name, species="Dog")
        # Add Dog-specific attributes
        self.breed = breed

    # Override the parent method
    def make_sound(self):
        return "Woof!"

# Another child class
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow!"

# Creating objects
generic_animal = Animal("Generic", "Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

# Using the objects
print(f"Generic animal: {generic_animal.info()}")
print(f"Sound: {generic_animal.make_sound()}")

print(f"\nDog: {dog.info()}")
print(f"Breed: {dog.breed}")
print(f"Sound: {dog.make_sound()}")

print(f"\nCat: {cat.info()}")
print(f"Breed: {cat.breed}")
print(f"Sound: {cat.make_sound()}")

# =====================================================
# 2. THE SUPER() FUNCTION
# =====================================================
print("\n" + "=" * 50)
print("2. THE SUPER() FUNCTION")
print("=" * 50)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"{self.year} {self.make} {self.model} started"

    def stop(self):
        self.is_running = False
        return f"{self.year} {self.make} {self.model} stopped"

    def info(self):
        status = "running" if self.is_running else "not running"
        return f"{self.year} {self.make} {self.model} ({status})"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type="gasoline"):
        # Call the parent class's __init__ method
        super().__init__(make, model, year)
        # Add Car-specific attributes
        self.fuel_type = fuel_type
        self.doors = 4

    # Override with enhancement
    def info(self):
        # Call the parent method first
        basic_info = super().info()
        # Add more information
        return f"{basic_info}, {self.doors} doors, runs on {self.fuel_type}"

# Create a car
car = Car("Toyota", "Camry", 2022, "hybrid")
print(car.info())  # Not running yet

# Start the car
print(car.start())
print(car.info())  # Now running

# =====================================================
# 3. METHOD OVERRIDING
# =====================================================
print("\n" + "=" * 50)
print("3. METHOD OVERRIDING")
print("=" * 50)

class Shape:
    def __init__(self, color="red"):
        self.color = color

    def area(self):
        # Base implementation
        return 0

    def describe(self):
        return f"A {self.color} shape with area {self.area()}"

class Circle(Shape):
    def __init__(self, radius, color="blue"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height, color="green"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        # Completely override the parent method
        return f"{self.color.capitalize()} rectangle with width={self.width}, height={self.height}, area={self.area()}"

# Create shapes
shape = Shape()
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Test the methods
print("Using overridden methods:")
print(f"Generic shape: {shape.describe()}")
print(f"Circle: {circle.describe()}")  # Uses Shape's describe but Circle's area
print(f"Rectangle: {rectangle.describe()}")  # Completely overridden describe method

# =====================================================
# 4. CHECKING INSTANCE RELATIONSHIPS
# =====================================================
print("\n" + "=" * 50)
print("4. CHECKING INSTANCE RELATIONSHIPS")
print("=" * 50)

# Create a hierarchy of classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} My student ID is {self.student_id}."

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, research_area):
        super().__init__(name, age, student_id)
        self.research_area = research_area

    def introduce(self):
        return f"{super().introduce()} I'm researching {self.research_area}."

# Create objects
person = Person("John", 30)
student = Student("Alice", 20, "A12345")
grad_student = GraduateStudent("Bob", 25, "G67890", "Machine Learning")

# Test the class relationships
print("Class relationships:")
print(f"Is person a Person? {isinstance(person, Person)}")
print(f"Is person a Student? {isinstance(person, Student)}")

print(f"\nIs student a Person? {isinstance(student, Person)}")
print(f"Is student a Student? {isinstance(student, Student)}")
print(f"Is student a GraduateStudent? {isinstance(student, GraduateStudent)}")

print(f"\nIs grad_student a Person? {isinstance(grad_student, Person)}")
print(f"Is grad_student a Student? {isinstance(grad_student, Student)}")
print(f"Is grad_student a GraduateStudent? {isinstance(grad_student, GraduateStudent)}")

# Test their methods
print("\nIntroductions:")
print(f"Person: {person.introduce()}")
print(f"Student: {student.introduce()}")
print(f"Graduate Student: {grad_student.introduce()}")

# =====================================================
# 5. PRACTICAL EXAMPLE: MEDIA LIBRARY
# =====================================================
print("\n" + "=" * 50)
print("5. PRACTICAL EXAMPLE: MEDIA LIBRARY")
print("=" * 50)

class MediaItem:
    def __init__(self, title, year, creator):
        self.title = title
        self.year = year
        self.creator = creator
        self._checked_out = False

    def check_out(self):
        if self._checked_out:
            return f"{self.title} is already checked out."
        self._checked_out = True
        return f"{self.title} has been checked out."

    def return_item(self):
        if not self._checked_out:
            return f"{self.title} is not checked out."
        self._checked_out = False
        return f"{self.title} has been returned."

    def display_info(self):
        status = "checked out" if self._checked_out else "available"
        return f"{self.title} ({self.year}) by {self.creator} - {status}"

class Book(MediaItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, year, author)
        self.pages = pages

    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}, {self.pages} pages"

class Movie(MediaItem):
    def __init__(self, title, director, year, runtime):
        super().__init__(title, year, director)
        self.runtime = runtime  # in minutes

    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}, {self.runtime} minutes"

class MusicAlbum(MediaItem):
    def __init__(self, title, artist, year, tracks):
        super().__init__(title, year, artist)
        self.tracks = tracks

    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}, {self.tracks} tracks"

# Create a library of items
library = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180),
    Movie("The Shawshank Redemption", "Frank Darabont", 1994, 142),
    MusicAlbum("Thriller", "Michael Jackson", 1982, 9)
]

# Display and interact with items
print("Library catalog:")
for i, item in enumerate(library, 1):
    print(f"{i}. {item.display_info()}")

print("\nChecking out items:")
print(library[0].check_out())
print(library[1].check_out())
print(library[0].check_out())  # Already checked out

print("\nUpdated catalog:")
for i, item in enumerate(library, 1):
    print(f"{i}. {item.display_info()}")

print("\nReturning items:")
print(library[0].return_item())

print("\nFinal catalog:")
for i, item in enumerate(library, 1):
    print(f"{i}. {item.display_info()}")

print("\nInheritance allows us to create specialized classes while reusing code!")
