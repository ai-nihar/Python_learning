"""
======================================================
Python Learning - Week 02 Day 02 (Day 9 Overall)
TOPIC: ENCAPSULATION
======================================================

DESCRIPTION:
This file explores encapsulation in Python, one of the four main principles
of Object-Oriented Programming. Encapsulation is about bundling data and
methods that operate on that data, and restricting access to certain components.

TOPICS COVERED:
1. Public, Protected, and Private attributes
2. Getters and Setters
3. Data validation
4. Name mangling

LEARNING OUTCOMES:
- Implement proper encapsulation in Python classes
- Create controlled access to object attributes
- Apply data validation using getters and setters
- Understand Python's approach to access control

======================================================
"""

# =====================================================
# 1. PUBLIC, PROTECTED, AND PRIVATE ATTRIBUTES
# =====================================================
print("=" * 50)
print("1. PUBLIC, PROTECTED, AND PRIVATE ATTRIBUTES")
print("=" * 50)

class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name          # Public attribute - accessible anywhere
        self._salary = salary     # Protected attribute - convention only
        self.__employee_id = employee_id  # Private attribute - name mangling

    def display_info(self):
        return f"Name: {self.name}, Salary: ${self._salary}, ID: {self.__employee_id}"

# Create an employee
employee = Employee("John Doe", 60000, "E12345")
print(employee.display_info())

# Accessing attributes directly
print("\nAccessing attributes directly:")
print(f"Public attribute: {employee.name}")  # Works fine
print(f"Protected attribute: {employee._salary}")  # Works, but not recommended
try:
    print(f"Private attribute: {employee.__employee_id}")  # Will raise an error
except AttributeError as e:
    print(f"Error accessing private attribute: {e}")

# Name mangling - how private attributes actually work
print("\nAccessing private attribute with name mangling:")
print(f"Private attribute via mangling: {employee._Employee__employee_id}")  # Works, but shouldn't be used

print("\nNote: Python doesn't have true access control - it uses conventions:")
print("- Public attributes: normal_name")
print("- Protected attributes: _protected_name (single underscore)")
print("- Private attributes: __private_name (double underscore)")

# =====================================================
# 2. GETTERS AND SETTERS
# =====================================================
print("\n" + "=" * 50)
print("2. GETTERS AND SETTERS")
print("=" * 50)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner      # Public attribute
        self._balance = balance  # Protected attribute

    # Getter method
    def get_balance(self):
        return self._balance

    # Setter method with validation
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            raise ValueError("Balance cannot be negative")

    # Method for depositing money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            raise ValueError("Deposit amount must be positive")

    # Method for withdrawing money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            raise ValueError("Invalid withdrawal amount")

# Creating a bank account
account = BankAccount("John Doe", 1000)
print(f"Account owner: {account.owner}")
print(f"Account balance: ${account.get_balance()}")

# Using methods for controlled access
try:
    print(account.deposit(500))
    print(account.withdraw(200))
    # This will raise an exception:
    print(account.withdraw(2000))
except ValueError as e:
    print(f"Error: {e}")

# Trying to set a negative balance
try:
    print("\nTrying to set a negative balance:")
    account.set_balance(-500)
except ValueError as e:
    print(f"Error: {e}")

# =====================================================
# 3. PROPERTY DECORATORS - MODERN APPROACH
# =====================================================
print("\n" + "=" * 50)
print("3. PROPERTY DECORATORS - MODERN APPROACH")
print("=" * 50)

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # Getter for celsius
    @property
    def celsius(self):
        return self._celsius

    # Setter for celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  # Absolute zero check
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    # Getter for fahrenheit (computed property)
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    # Setter for fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# Using properties
temp = Temperature(25)  # 25°C
print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

# Changing temperature using celsius property
temp.celsius = 30
print(f"After setting celsius - Celsius: {temp.celsius}°C, Fahrenheit: {temp.fahrenheit}°F")

# Changing temperature using fahrenheit property
temp.fahrenheit = 68
print(f"After setting fahrenheit - Celsius: {temp.celsius}°C, Fahrenheit: {temp.fahrenheit}°F")

# Validation prevents impossible temperatures
try:
    print("\nTrying to set temperature below absolute zero:")
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

# =====================================================
# 4. PRACTICAL EXAMPLE: USER PROFILE
# =====================================================
print("\n" + "=" * 50)
print("4. PRACTICAL EXAMPLE: USER PROFILE")
print("=" * 50)

import re  # For email validation

class UserProfile:
    def __init__(self, username, email, age=None):
        self.username = username
        self._email = None  # Set via property
        self.email = email  # Uses the email.setter
        self._age = None    # Set via property
        self.age = age      # Uses the age.setter

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Simple email validation using regex
        if value and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value is not None and (value < 0 or value > 120):
            raise ValueError("Age must be between 0 and 120")
        self._age = value

    def display_info(self):
        age_info = f", Age: {self.age}" if self.age else ""
        return f"Username: {self.username}, Email: {self.email}{age_info}"

# Create a valid user profile
try:
    print("Creating valid user:")
    user1 = UserProfile("johndoe", "john@example.com", 30)
    print(user1.display_info())
except ValueError as e:
    print(f"Error: {e}")

# Invalid email
try:
    print("\nTrying to create user with invalid email:")
    user2 = UserProfile("janedoe", "not-an-email", 25)
except ValueError as e:
    print(f"Error: {e}")

# Invalid age
try:
    print("\nTrying to create user with invalid age:")
    user3 = UserProfile("bobsmith", "bob@example.com", 150)
except ValueError as e:
    print(f"Error: {e}")

# Update profile with properties
try:
    print("\nUpdating user profile:")
    user1.email = "john.doe@company.com"
    user1.age = 31
    print(user1.display_info())
except ValueError as e:
    print(f"Error: {e}")

print("\nEncapsulation helps create robust classes that maintain data integrity")
