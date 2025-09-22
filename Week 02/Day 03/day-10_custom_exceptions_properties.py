"""
======================================================
Python Learning - Week 02 Day 03 (Day 10 Overall)
TOPIC: CUSTOM EXCEPTIONS AND PROPERTIES
======================================================

DESCRIPTION:
This file explores two important OOP concepts in Python: custom exception
classes and property decorators. Custom exceptions help create more meaningful
error handling, while property decorators provide a clean syntax for controlled
attribute access.

TOPICS COVERED:
1. Creating custom exception classes
2. Exception hierarchies
3. Property decorators
4. Getters, setters, and deleters
5. Combining exceptions and properties

LEARNING OUTCOMES:
- Design and implement custom exception classes
- Create exception hierarchies for better error handling
- Use property decorators for clean attribute access
- Implement data validation with properties
- Combine properties and exceptions for robust classes

======================================================
"""

# =====================================================
# 1. CUSTOM EXCEPTION CLASSES
# =====================================================
print("=" * 50)
print("1. CUSTOM EXCEPTION CLASSES")
print("=" * 50)

"""
Custom exceptions help make your code more readable and maintainable
by providing specific error types for different error conditions.
"""

# Creating custom exception classes by inheriting from Exception
class InsufficientFundsError(Exception):
    """Exception raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        # Call the base class constructor with a custom message
        super().__init__(
            f"Cannot withdraw ${amount}. "
            f"Balance is ${balance}. "
            f"You need ${self.deficit} more."
        )

class AccountLockedError(Exception):
    """Exception raised when operating on a locked account."""
    pass

# A more complex bank account using custom exceptions
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = balance
        self._is_locked = False

    def lock(self):
        self._is_locked = True
        return f"{self.owner}'s account is now locked"

    def unlock(self):
        self._is_locked = False
        return f"{self.owner}'s account is now unlocked"

    def get_balance(self):
        if self._is_locked:
            raise AccountLockedError(f"Cannot check balance: {self.owner}'s account is locked")
        return self._balance

    def deposit(self, amount):
        if self._is_locked:
            raise AccountLockedError(f"Cannot deposit: {self.owner}'s account is locked")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"

    def withdraw(self, amount):
        if self._is_locked:
            raise AccountLockedError(f"Cannot withdraw: {self.owner}'s account is locked")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            # Raise our custom exception
            raise InsufficientFundsError(self._balance, amount)

        self._balance -= amount
        return f"Withdrew ${amount}. New balance: ${self._balance}"

# Create account and test our custom exceptions
improved_account = BankAccount("Jane Doe", 500)
print(f"Account owner: {improved_account.owner}")
print(f"Account balance: ${improved_account.get_balance()}")

# Test deposits and withdrawals
try:
    print(improved_account.deposit(300))
    print(improved_account.withdraw(200))

    # Lock the account
    print(improved_account.lock())

    # Try to withdraw while locked
    print(improved_account.withdraw(100))

except InsufficientFundsError as e:
    print(f"Insufficient funds: {e}")
except AccountLockedError as e:
    print(f"Account locked: {e}")
except ValueError as e:
    print(f"Value error: {e}")

# Unlock and try a withdrawal that's too large
print(improved_account.unlock())
try:
    print(improved_account.withdraw(1000))  # Too much!
except InsufficientFundsError as e:
    print(f"Insufficient funds: {e}")

# =====================================================
# 2. EXCEPTION HIERARCHIES
# =====================================================
print("\n" + "=" * 50)
print("2. EXCEPTION HIERARCHIES")
print("=" * 50)

"""
Creating a hierarchy of custom exceptions can make error handling more
organized and flexible. This connects to what you learned about inheritance.
"""

# Base exception for all database errors
class DatabaseError(Exception):
    """Base class for all database-related exceptions."""
    pass

# More specific exceptions
class ConnectionError(DatabaseError):
    """Raised when a connection to the database fails."""
    pass

class QueryError(DatabaseError):
    """Raised when a query fails."""
    def __init__(self, query, message):
        self.query = query
        self.message = message
        super().__init__(f"Query '{query}' failed: {message}")

class TableNotFoundError(QueryError):
    """Raised when a query references a non-existent table."""
    def __init__(self, query, table_name):
        self.table_name = table_name
        super().__init__(query, f"Table '{table_name}' not found")

# A simple database simulator class
class DatabaseSimulator:
    def __init__(self):
        self.connected = False
        self.data = {"users": ["Alice", "Bob", "Charlie"]}

    def connect(self, password):
        if password != "correct_password":
            raise ConnectionError("Invalid database password")
        self.connected = True
        print("Connected to database")

    def disconnect(self):
        if not self.connected:
            print("Not connected")
            return
        self.connected = False
        print("Disconnected from database")

    def execute_query(self, query):
        if not self.connected:
            raise ConnectionError("Not connected to database")

        # Simulate query execution
        parts = query.lower().split()
        if parts[0] == "select" and len(parts) >= 4 and parts[2] == "from":
            table = parts[3]
            if table in self.data:
                print(f"Query results: {self.data[table]}")
                return self.data[table]
            else:
                raise TableNotFoundError(query, table)
        else:
            raise QueryError(query, "Invalid query format")

# Using the database with try-except blocks
db = DatabaseSimulator()

# Connection handling
try:
    # Try with wrong password first
    try:
        db.connect("wrong_password")
    except ConnectionError as e:
        print(f"Connection failed: {e}")
        print("Retrying with correct password...")

    # Connect with correct password
    db.connect("correct_password")

    # Query handling
    try:
        # Valid query
        results = db.execute_query("SELECT * FROM users")

        # Invalid table query
        db.execute_query("SELECT * FROM products")
    except TableNotFoundError as e:
        print(f"Table not found: {e}")
        print(f"Missing table: {e.table_name}")
    except QueryError as e:
        print(f"Query error: {e}")

    # Invalid query format
    try:
        db.execute_query("INVALID QUERY")
    except QueryError as e:
        print(f"Another query error: {e}")

    # Catching at different levels of the hierarchy
    try:
        db.execute_query("SELECT * FROM nonexistent")
    except ConnectionError:
        print("Connection lost!")
    except TableNotFoundError:
        print("Specifically caught as TableNotFoundError")
    except QueryError as e:
        print(f"Caught as QueryError: {e}")
    except DatabaseError:
        print("Caught as DatabaseError")

finally:
    # This will run regardless of exceptions
    db.disconnect()

print("\nExceptions hierarchies let us catch errors at different levels of specificity!")

# =====================================================
# 3. PROPERTY DECORATORS
# =====================================================
print("\n" + "=" * 50)
print("3. PROPERTY DECORATORS")
print("=" * 50)

"""
Properties provide a clean syntax for getters and setters, allowing
you to use attributes in a Pythonic way while still controlling access.
"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age  # Protected attribute

    # Getter property
    @property
    def age(self):
        return self._age

    # Setter property
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self._age = value

    # Computed property
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Deleter property (rarely used)
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

# Create a person
person = Person("John", "Doe", 30)

# Access properties
print(f"Full name: {person.full_name}")  # Using computed property
print(f"Age: {person.age}")  # Using getter

# Use setter
try:
    person.age = 35  # Using setter
    print(f"New age: {person.age}")

    # These will raise exceptions:
    person.age = -5
except ValueError as e:
    print(f"ValueError: {e}")

try:
    person.age = "forty"  # Wrong type
except TypeError as e:
    print(f"TypeError: {e}")

# Use deleter (rarely needed)
print("\nDeleting age...")
del person.age

try:
    print(f"Age: {person.age}")
except AttributeError as e:
    print(f"AttributeError: {e}")

# =====================================================
# 4. PROPERTY VS TRADITIONAL GETTERS/SETTERS
# =====================================================
print("\n" + "=" * 50)
print("4. PROPERTY VS TRADITIONAL GETTERS/SETTERS")
print("=" * 50)

# Traditional style
class CircleTraditional:
    def __init__(self, radius):
        self._radius = radius  # Protected attribute

    # Getter
    def get_radius(self):
        return self._radius

    # Setter
    def set_radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Calculated attribute
    def get_area(self):
        return 3.14159 * self._radius ** 2

    def get_diameter(self):
        return 2 * self._radius

# Property style
class CircleProperty:
    def __init__(self, radius):
        self._radius = radius  # Will be validated by the setter
        # OR use the setter directly:
        # self.radius = radius  # This calls the radius.setter

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def diameter(self):
        return 2 * self._radius

# Using traditional style
circle1 = CircleTraditional(5)
print("Traditional style:")
print(f"Radius: {circle1.get_radius()}")
print(f"Area: {circle1.get_area()}")
print(f"Diameter: {circle1.get_diameter()}")

# Update radius
circle1.set_radius(7)
print(f"New radius: {circle1.get_radius()}")
print(f"New area: {circle1.get_area()}")

# Using property style
circle2 = CircleProperty(5)
print("\nProperty style:")
print(f"Radius: {circle2.radius}")
print(f"Area: {circle2.area}")
print(f"Diameter: {circle2.diameter}")

# Update radius
circle2.radius = 7
print(f"New radius: {circle2.radius}")
print(f"New area: {circle2.area}")

# Try invalid radius
try:
    circle2.radius = -2
except ValueError as e:
    print(f"Error: {e}")

print("\nAdvantages of properties:")
print("1. More Pythonic syntax - looks like direct attribute access")
print("2. Can start with direct access and add validation later")
print("3. Cleaner code with less boilerplate")
print("4. Computed properties look like regular attributes")

# =====================================================
# 5. COMBINING EXCEPTIONS AND PROPERTIES
# =====================================================
print("\n" + "=" * 50)
print("5. COMBINING EXCEPTIONS AND PROPERTIES")
print("=" * 50)

"""
Combining custom exceptions with properties creates robust classes
with controlled access and meaningful error messages.
"""

# Custom exceptions for the Product class
class ProductError(Exception):
    """Base class for product-related exceptions."""
    pass

class InvalidPriceError(ProductError):
    """Raised when setting an invalid price."""
    pass

class OutOfStockError(ProductError):
    """Raised when trying to purchase out-of-stock items."""
    pass

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._price = None
        self._stock = None

        # Use properties to validate initial values
        self.price = price
        self.stock = stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise InvalidPriceError("Price must be a number")
        if value < 0:
            raise InvalidPriceError("Price cannot be negative")
        self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if not isinstance(value, int):
            raise TypeError("Stock must be an integer")
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value

    @property
    def is_available(self):
        return self._stock > 0

    def purchase(self, quantity=1):
        if not self.is_available:
            raise OutOfStockError(f"{self.name} is out of stock")

        if quantity > self._stock:
            raise OutOfStockError(
                f"Cannot purchase {quantity} units. Only {self._stock} available."
            )

        self._stock -= quantity
        return f"Purchased {quantity} {self.name}(s) for ${self._price * quantity:.2f}"

# Create and use a product
try:
    laptop = Product("Laptop", 999.99, 5)
    print(f"Product: {laptop.name}, Price: ${laptop.price}, Stock: {laptop.stock}")
    print(f"Available? {laptop.is_available}")

    # Purchase some laptops
    print(laptop.purchase(2))
    print(f"Remaining stock: {laptop.stock}")

    # Try to purchase too many
    print(laptop.purchase(4))

except OutOfStockError as e:
    print(f"Stock error: {e}")
except InvalidPriceError as e:
    print(f"Price error: {e}")
except ProductError as e:
    print(f"General product error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

# Try to create a product with invalid values
try:
    invalid_product = Product("Invalid", -50, 10)
except InvalidPriceError as e:
    print(f"\nCouldn't create product: {e}")

print("\nCombining properties with custom exceptions creates robust, self-validating classes!")
