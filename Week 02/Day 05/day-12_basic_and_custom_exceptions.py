"""
======================================================
Python Learning - Week 02 Day 05 (Day 12 Overall)
TOPIC: BASIC & CUSTOM EXCEPTIONS
======================================================

DESCRIPTION:
This file explores exception hierarchy, best practices for handling errors,
and creating custom exception classes using object-oriented programming.
These fundamentals help build more robust applications with better error handling.

TOPICS COVERED:
1. Exception Hierarchy in Python
2. Best Practices for Exception Handling
3. Custom Exception Classes with OOP
4. Creating Exception Hierarchies

LEARNING OUTCOMES:
- Understand Python's exception structure
- Apply exception handling best practices
- Create domain-specific exception classes
- Design effective exception hierarchies

======================================================
"""

# ======================================================
# 1) Exception Hierarchy in Python
# ======================================================
"""
Python's exception classes form a hierarchy with BaseException at the root.
Understanding this hierarchy helps you catch exceptions at the appropriate level.

Exception hierarchy (simplified):
BaseException
 ├── SystemExit, KeyboardInterrupt, GeneratorExit
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      └── TypeError, ValueError
"""

print("\n1. EXCEPTION HIERARCHY IN PYTHON")
print("=" * 50)

# 1.1 Exception Hierarchy in Action
print("\n1.1 Handling exceptions at appropriate levels:")

try:
    numbers = [10, 20, 30]

    # This will cause an IndexError
    value = numbers[10]

    # This code will not run due to the error above
    result = value / 0   # Would cause ZeroDivisionError

except IndexError as e:
    print(f"Specific error caught: {e}")
    print(f"Type of exception: {type(e).__name__}")

except LookupError as e:
    # This wouldn't run in this case because IndexError is caught first
    # LookupError is a parent class of IndexError
    print(f"More general error caught: {e}")

except Exception as e:
    # Most general error handler - catches all exceptions derived from Exception
    print(f"Caught a general exception: {e}")

# 1.2 Exploring the Exception Hierarchy
print("\n1.2 Exploring the exception hierarchy:")

def show_exception_hierarchy(exception_class, level=0):
    """Display an exception class and its direct subclasses."""
    indent = "  " * level
    print(f"{indent}├── {exception_class.__name__}")

    # Show direct subclasses
    for subclass in exception_class.__subclasses__():
        show_exception_hierarchy(subclass, level + 1)

# Display a portion of the exception hierarchy
print("\nCommon exceptions in the hierarchy:")
print("BaseException")
show_exception_hierarchy(Exception, 1)  # Start from Exception, level 1 indentation

# ======================================================
# 2) Best Practices for Exception Handling
# ======================================================
"""
Following best practices for exception handling makes your code more robust,
easier to debug, and helps prevent common pitfalls.
"""

print("\n\n2. BEST PRACTICES FOR EXCEPTION HANDLING")
print("=" * 50)

# PRACTICE 1: Be specific with exception types
print("\n2.1 Be specific with exception types:")
try:
    # Some code that might raise different errors
    value = int("abc")  # ValueError
except ValueError:
    print("✓ Specifically handling ValueError - good practice")
except Exception:
    print("✗ Catching all exceptions - avoid unless necessary")

# PRACTICE 2: Don't silence exceptions without handling
print("\n2.2 Don't silence exceptions without proper handling:")
try:
    value = 10 / 0
except ZeroDivisionError:
    print("✓ Caught ZeroDivisionError and handling it properly")
    # Bad practice (commented out):
    # pass  # ✗ Silently ignoring the exception

# PRACTICE 3: Clean up resources properly
print("\n2.3 Clean up resources properly:")
try:
    file = open("nonexistent_file.txt")
    content = file.read()
except FileNotFoundError:
    print("✓ Handled file not found error")
finally:
    # Always executed, whether exception occurs or not
    print("✓ This is where you'd close resources (e.g., file.close())")

# PRACTICE 4: Don't catch exceptions you can't handle meaningfully
print("\n2.4 Don't catch exceptions you can't handle:")
def example_function():
    try:
        # Some code that might fail
        result = 10 / 0
    except ZeroDivisionError:
        print("✓ Handle locally if you can address the issue here")
        return "Default value"

print(example_function())

# PRACTICE 5: Use context managers where applicable
print("\n2.5 Use context managers where applicable:")
try:
    # Using context manager ('with' statement) ensures the file is closed
    with open("test_context_manager.txt", "w") as f:
        f.write("Context managers handle cleanup automatically")
    print("✓ File automatically closed after 'with' block")
except IOError as e:
    print(f"Error: {e}")

# ======================================================
# 3) Custom Exception Classes with OOP
# ======================================================
"""
Creating custom exceptions allows you to:
1. Make your code more readable and self-documenting
2. Create a hierarchy of application-specific exceptions
3. Include additional information relevant to your application
4. Handle different error cases in more specific ways
"""

print("\n\n3. CUSTOM EXCEPTION CLASSES WITH OOP")
print("=" * 50)

# 3.1 Basic Custom Exception
print("\n3.1 Creating a basic custom exception:")

class InsufficientFundsError(Exception):
    """Exception raised when a withdrawal exceeds the available balance."""
    pass  # Even with no additional code, this is a valid custom exception

# Using the basic custom exception
try:
    balance = 100
    withdrawal = 150
    if withdrawal > balance:
        raise InsufficientFundsError("Not enough funds to complete withdrawal")
except InsufficientFundsError as e:
    print(f"Error: {e}")

# 3.2 Adding Information to Custom Exceptions
print("\n3.2 Adding information to custom exceptions:")

class WithdrawalError(Exception):
    """Exception raised for errors in the withdrawal operation."""

    def __init__(self, balance, amount, message="Insufficient funds"):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        self.message = message
        # Call the base class constructor with the message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: tried to withdraw ${self.amount} but balance is ${self.balance} (deficit: ${self.deficit})"

# Using the custom exception with additional information
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            # Raise our custom exception with details
            raise WithdrawalError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Testing the custom exception
account = BankAccount("John Doe", 100)
try:
    account.withdraw(150)
except WithdrawalError as e:
    print(f"Error: {e}")
    print(f"Current balance: ${e.balance}")
    print(f"Attempted withdrawal: ${e.amount}")
    print(f"Amount needed: ${e.deficit}")

# ======================================================
# 4) Creating Exception Hierarchies
# ======================================================
"""
For complex applications, creating an exception hierarchy helps:
1. Organize errors by category
2. Allow for both specific and general error handling
3. Make the codebase more maintainable
4. Provide clearer error diagnostics
"""

print("\n\n4. CREATING EXCEPTION HIERARCHIES")
print("=" * 50)

class BankError(Exception):
    """Base exception class for banking operations."""
    pass

class AccountError(BankError):
    """Exceptions related to account operations."""
    pass

class TransactionError(BankError):
    """Exceptions related to transactions."""
    pass

class InsufficientBalanceError(TransactionError):
    """Raised when withdrawal amount exceeds balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient balance: {balance} < {amount}")

class AccountLockedError(AccountError):
    """Raised when operations are attempted on a locked account."""
    pass

class DailyLimitExceededError(TransactionError):
    """Raised when daily withdrawal limit is exceeded."""
    def __init__(self, limit, attempted_amount):
        self.limit = limit
        self.attempted_amount = attempted_amount
        super().__init__(f"Daily limit of ${limit} exceeded with ${attempted_amount} withdrawal")

# Example of a banking system using the exception hierarchy
class EnhancedBankAccount:
    def __init__(self, owner, balance=0, daily_limit=1000):
        self.owner = owner
        self.balance = balance
        self.daily_limit = daily_limit
        self.today_withdrawals = 0
        self.locked = False

    def withdraw(self, amount):
        """Withdraw money with multiple possible errors."""
        # Check if account is locked
        if self.locked:
            raise AccountLockedError(f"Account for {self.owner} is locked")

        # Check daily withdrawal limit
        if self.today_withdrawals + amount > self.daily_limit:
            raise DailyLimitExceededError(self.daily_limit, amount)

        # Check sufficient balance
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)

        # Process withdrawal
        self.balance -= amount
        self.today_withdrawals += amount
        return self.balance

# Example usage of exception hierarchy
print("\nExample of using exception hierarchy in a banking system:")
account = EnhancedBankAccount("Jane Smith", 500, daily_limit=1000)

# Test various error scenarios
try:
    # Lock the account first
    account.locked = True
    account.withdraw(100)
except AccountLockedError as e:
    print(f"Account error: {e}")
    # Unlock for next tests
    account.locked = False

try:
    # Try exceeding daily limit
    account.withdraw(1200)
except DailyLimitExceededError as e:
    print(f"Transaction error: {e}")

try:
    # Try exceeding balance
    account.withdraw(600)
except InsufficientBalanceError as e:
    print(f"Balance error: {e}")

try:
    # This should succeed
    new_balance = account.withdraw(200)
    print(f"Withdrawal successful. New balance: ${new_balance}")
except BankError as e:
    # This is a catch-all for any bank-related error
    print(f"Bank error: {e}")

print("\n\nCustom exceptions make your code more readable and provide better error information.")
print("They help structure your error handling in a way that's natural to your application domain.")
