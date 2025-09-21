"""
======================================================
Python Learning - Week 02 Day 02 (Day 9 Overall)
TOPIC: CLASSES AND OBJECTS BASICS
======================================================

DESCRIPTION:
This file introduces the fundamental building blocks of Object-Oriented
Programming (OOP) in Python: classes and objects. We'll learn how to
define classes and create objects from them.

TOPICS COVERED:
1. Defining a class
2. Creating objects (instances)
3. Class vs instance attributes
4. Instance methods

LEARNING OUTCOMES:
- Understand the concept of classes as blueprints
- Create and use objects (instances) of classes
- Distinguish between class and instance attributes
- Implement and use instance methods

======================================================
"""

# =====================================================
# 1. DEFINING A CLASS AND CREATING OBJECTS
# =====================================================
print("=" * 50)
print("1. DEFINING A CLASS AND CREATING OBJECTS")
print("=" * 50)

# A class is a blueprint for creating objects
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializes object attributes)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # Another instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Creating objects (instances) of the Dog class
buddy = Dog("Buddy", 5)
rex = Dog("Rex", 3)

# Accessing attributes and methods
print(f"Dog 1: {buddy.name}, age {buddy.age}")
print(f"Dog 2: {rex.name}, age {rex.age}")
print(f"Both dogs are: {buddy.species}")  # Accessing class attribute
print(buddy.bark())
print(rex.description())

# We can modify attributes after creation
buddy.age = 6
print(f"{buddy.name} is now {buddy.age} years old")

# =====================================================
# 2. CLASS VS INSTANCE ATTRIBUTES
# =====================================================
print("\n" + "=" * 50)
print("2. CLASS VS INSTANCE ATTRIBUTES")
print("=" * 50)

class Circle:
    # Class attribute - shared by all instances
    pi = 3.14159

    def __init__(self, radius):
        # Instance attribute - unique to each instance
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

# Creating Circle objects
small_circle = Circle(5)
large_circle = Circle(10)

print(f"Small circle area: {small_circle.area():.2f}")
print(f"Large circle area: {large_circle.area():.2f}")

# Changing the class attribute affects all instances
print("\nChanging class attribute:")
Circle.pi = 3.14  # Less precise value
print(f"Small circle area now: {small_circle.area():.2f}")
print(f"Large circle area now: {large_circle.area():.2f}")

# But if we set the attribute on an instance, it creates an instance attribute
small_circle.pi = 3.14159265359  # More precise value, but only for this instance
print(f"\nSmall circle pi: {small_circle.pi}")
print(f"Large circle pi: {large_circle.pi}")
print(f"Class pi: {Circle.pi}")

# =====================================================
# 3. PRACTICAL EXAMPLE: STUDENT CLASS
# =====================================================
print("\n" + "=" * 50)
print("3. PRACTICAL EXAMPLE: STUDENT CLASS")
print("=" * 50)

class Student:
    # Class attribute
    school = "Python High School"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # List to store courses

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"{self.name} enrolled in {course}"
        return f"{self.name} is already enrolled in {course}"

    def list_courses(self):
        if not self.courses:
            return f"{self.name} is not enrolled in any courses"
        courses_list = ", ".join(self.courses)
        return f"{self.name} is enrolled in: {courses_list}"

    def student_info(self):
        return f"Student: {self.name}, ID: {self.student_id}, School: {self.school}"

# Creating student objects
alice = Student("Alice Smith", "A12345")
bob = Student("Bob Johnson", "B67890")

# Using student methods
print(alice.student_info())
print(bob.student_info())

print(alice.enroll("Python 101"))
print(alice.enroll("Data Structures"))
print(alice.enroll("Python 101"))  # Already enrolled

print(bob.enroll("Machine Learning"))
print(bob.enroll("Web Development"))

print(alice.list_courses())
print(bob.list_courses())

# Changing the school for all students
Student.school = "Python Advanced Academy"
print(f"\nAfter changing school name:")
print(alice.student_info())
print(bob.student_info())
