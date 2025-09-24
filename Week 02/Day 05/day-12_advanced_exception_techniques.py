"""
======================================================
Python Learning - Week 02 Day 05 (Day 12 Overall)
TOPIC: ADVANCED EXCEPTION TECHNIQUES
======================================================

DESCRIPTION:
This file explores advanced exception handling techniques including
exception chaining, context preservation, and design patterns for
robust error handling in complex applications.

TOPICS COVERED:
1. Exception Chaining and Context Preservation
2. Exception Handling Design Patterns
3. Exception Documentation and API Design
4. Real-world Exception Handling Scenarios

LEARNING OUTCOMES:
- Implement exception chaining for better debugging
- Apply design patterns for systematic error handling
- Document exceptions properly in libraries and APIs
- Handle errors gracefully in complex scenarios

======================================================
"""

# ======================================================
# 1) Exception Chaining and Context Preservation
# ======================================================
"""
Exception chaining allows you to preserve the original cause of an exception
when you need to raise a new one. This is crucial for debugging complex applications.
"""

print("\n1. EXCEPTION CHAINING AND CONTEXT PRESERVATION")
print("=" * 50)

# 1.1 Basic Exception Chaining
print("\n1.1 Basic exception chaining with 'raise from':")

try:
    try:
        # Original exception
        result = int("abc")  # Raises ValueError
    except ValueError as e:
        # Raise a new exception while preserving the original one
        raise RuntimeError("Failed to parse input") from e
except RuntimeError as e:
    print(f"Runtime error: {e}")
    print(f"Original cause: {e.__cause__}")
    print(f"Type of original cause: {type(e.__cause__).__name__}")

# 1.2 Implicit Exception Chaining
print("\n1.2 Implicit exception chaining:")

def process_data(data):
    try:
        return int(data)
    except ValueError:
        # Raising a new exception within an except block
        # automatically chains it with the original exception
        raise TypeError("Expected a numeric string")

try:
    process_data("hello")
except TypeError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__context__}")
    print(f"Type of original cause: {type(e.__context__).__name__}")

# 1.3 Suppressing Exception Chaining
print("\n1.3 Suppressing exception chaining:")

try:
    try:
        # Original exception
        result = int("xyz")
    except ValueError:
        # Explicitly suppress chaining with "from None"
        raise RuntimeError("Failed to process input") from None
except RuntimeError as e:
    print(f"Error message: {e}")
    print(f"Original cause: {e.__cause__}")  # Will be None

# 1.4 Tracing Multiple Exception Levels
print("\n1.4 Tracing multiple exception levels:")

def level3_function(value):
    # Lowest level function
    return int(value)  # May raise ValueError

def level2_function(value):
    # Mid-level function
    try:
        return level3_function(value)
    except ValueError as e:
        raise ValueError("Invalid value format") from e

def level1_function(value):
    # Top-level function
    try:
        return level2_function(value)
    except ValueError as e:
        raise RuntimeError("Processing error") from e

# Test the chain of exceptions
try:
    level1_function("not-a-number")
except RuntimeError as e:
    print("\nException chain (from high to low level):")
    print(f"1. {type(e).__name__}: {e}")

    if e.__cause__:
        print(f"2. {type(e.__cause__).__name__}: {e.__cause__}")

        if e.__cause__.__cause__:
            print(f"3. {type(e.__cause__.__cause__).__name__}: {e.__cause__.__cause__}")

# ======================================================
# 2) Exception Handling Design Patterns
# ======================================================
"""
Design patterns for exception handling help structure error-handling
in more complex applications. These patterns make code more maintainable
and error-handling more consistent.
"""

print("\n\n2. EXCEPTION HANDLING DESIGN PATTERNS")
print("=" * 50)

import random
import time

# 2.1 Retry Pattern
print("\n2.1 Retry pattern:")

def unstable_operation():
    """Simulates an operation that sometimes fails."""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network connection failed")
    return "Operation successful"

def retry_operation(operation, max_attempts=3, delay=1):
    """Retry pattern implementation."""
    attempts = 0
    last_exception = None

    while attempts < max_attempts:
        try:
            return operation()
        except Exception as e:
            attempts += 1
            last_exception = e
            print(f"Attempt {attempts} failed: {e}")
            if attempts < max_attempts:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)

    # If we reach here, all attempts failed
    raise RuntimeError(f"Failed after {max_attempts} attempts") from last_exception

# Try the retry pattern
try:
    result = retry_operation(unstable_operation)
    print(f"Result: {result}")
except RuntimeError as e:
    print(f"Final error: {e}")

# 2.2 Exception Translation Pattern
print("\n2.2 Exception translation pattern:")

class DatabaseError(Exception):
    """Base class for database-related exceptions."""
    pass

class QueryError(DatabaseError):
    """Raised for SQL query errors."""
    pass

class ConnectionError(DatabaseError):
    """Raised for database connection errors."""
    pass

def execute_query(query):
    """Simulates executing a database query."""
    try:
        # Simulate different types of errors
        if "SELECT" not in query:
            raise ValueError("Invalid SQL: SELECT statement missing")
        if "FROM" not in query:
            raise SyntaxError("Invalid SQL syntax: FROM clause missing")

        # Simulate successful query
        return ["result1", "result2"]

    except ValueError as e:
        # Translate generic ValueError to domain-specific QueryError
        raise QueryError(f"Query validation failed: {str(e)}") from e

    except Exception as e:
        # Translate any other exception to generic DatabaseError
        raise DatabaseError(f"Database operation failed: {str(e)}") from e

# Test the exception translation pattern
try:
    results = execute_query("SELECT * WHERE id = 1")  # Missing FROM clause
except QueryError as e:
    print(f"Query error: {e}")
except DatabaseError as e:
    print(f"Database error: {e}")

# 2.3 Fallback Pattern
print("\n2.3 Fallback pattern:")

def get_user_data(user_id):
    """Simulate fetching user data with fallback options."""
    # Try primary data source
    try:
        print(f"Attempting to fetch user {user_id} from primary database...")
        if random.random() < 0.5:  # 50% chance of primary source failing
            raise ConnectionError("Primary database connection failed")
        return {"id": user_id, "name": "John Doe", "source": "primary_db"}

    # Try backup data source
    except ConnectionError:
        print("Primary source failed, trying backup database...")
        try:
            if random.random() < 0.3:  # 30% chance of backup source failing
                raise TimeoutError("Backup database timeout")
            return {"id": user_id, "name": "John Doe", "source": "backup_db"}

        # Try cache as last resort
        except Exception:
            print("Backup source failed, using cached data...")
            # Cache should never fail (fallback of last resort)
            return {"id": user_id, "name": "John Doe", "source": "cache", "note": "might be stale"}

# Test the fallback pattern
user_data = get_user_data(123)
print(f"Retrieved user data: {user_data}")

# 2.4 Circuit Breaker Pattern
print("\n2.4 Circuit breaker pattern:")

class CircuitBreaker:
    """Implementation of the circuit breaker pattern."""

    def __init__(self, max_failures=3, reset_timeout=10):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failures = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN
        self.last_failure_time = 0

    def execute(self, function, *args, **kwargs):
        """Execute a function with circuit breaker protection."""
        # Check if circuit is OPEN
        if self.state == "OPEN":
            # Check if reset timeout has expired
            if time.time() - self.last_failure_time > self.reset_timeout:
                print("Circuit breaker: Moving from OPEN to HALF-OPEN")
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError(f"Circuit breaker is OPEN until {self.last_failure_time + self.reset_timeout}")

        # Try to execute the function
        try:
            result = function(*args, **kwargs)

            # If HALF-OPEN and successful, reset circuit breaker
            if self.state == "HALF-OPEN":
                print("Circuit breaker: Moving from HALF-OPEN to CLOSED")
                self.state = "CLOSED"
                self.failures = 0

            return result

        except Exception as e:
            # Record the failure
            self.failures += 1
            self.last_failure_time = time.time()

            # If too many failures, open the circuit
            if self.failures >= self.max_failures:
                print(f"Circuit breaker: Moving to OPEN (after {self.failures} failures)")
                self.state = "OPEN"

            # Re-raise the exception
            raise e

# Function to test with the circuit breaker
def unreliable_service():
    """Simulates an unreliable service that fails most of the time."""
    if random.random() < 0.8:  # 80% chance of failure
        raise ConnectionError("Service unavailable")
    return "Service response data"

# Test the circuit breaker
circuit_breaker = CircuitBreaker(max_failures=3, reset_timeout=5)

# Make several calls to demonstrate circuit breaker state changes
print("\nTesting circuit breaker with multiple calls:")
for i in range(5):
    try:
        print(f"\nCall {i+1}:")
        result = circuit_breaker.execute(unreliable_service)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Failed: {e}")
        print(f"Circuit state: {circuit_breaker.state}")
        print(f"Failure count: {circuit_breaker.failures}")

# ======================================================
# 3) Exception Documentation and API Design
# ======================================================
"""
Documenting exceptions properly is critical for API design. It helps users
of your code understand what can go wrong and how to handle errors.
"""

print("\n\n3. EXCEPTION DOCUMENTATION AND API DESIGN")
print("=" * 50)

# 3.1 Documenting Exceptions
print("\n3.1 Documenting exceptions in docstrings:")

def transfer_money(from_account, to_account, amount):
    """Transfer money between two accounts.

    Args:
        from_account: The source account object
        to_account: The destination account object
        amount: The amount to transfer (must be positive)

    Returns:
        dict: Transaction details including confirmation ID

    Raises:
        ValueError: If amount is negative or zero
        InsufficientFundsError: If source account has insufficient balance
        AccountLockedError: If either account is locked
        TransactionError: For other transaction processing errors
    """
    print("Example of well-documented function that specifies its exceptions")
    # Implementation would go here
    pass

# 3.2 Exception Handling in API Design
print("\n3.2 Exception handling in API design:")

class PaymentAPI:
    """Example API class demonstrating exception handling principles."""

    def process_payment(self, payment_details):
        """Process a payment through the payment gateway.

        This method demonstrates several API design principles:
        1. Document all possible exceptions
        2. Use domain-specific exceptions
        3. Include relevant error information
        4. Keep internals separate from the public interface
        """
        try:
            # Internal implementation with potential low-level errors
            self._validate_payment(payment_details)
            self._connect_to_gateway()
            self._send_payment_request(payment_details)
            return {"status": "success", "confirmation_code": "ABC123"}

        except ValueError as e:
            # Translate to domain-specific exception
            raise PaymentValidationError(str(e)) from e

        except ConnectionError as e:
            # Add context and retry information
            raise PaymentGatewayError("Unable to connect to payment service. Please try again later.") from e

        except Exception as e:
            # Generic handler with logging
            print(f"Would log error: {e}")
            raise PaymentProcessingError("An unexpected error occurred during payment processing.") from e

    # Internal methods
    def _validate_payment(self, details):
        if "amount" not in details:
            raise ValueError("Payment amount is required")

    def _connect_to_gateway(self):
        if random.random() < 0.3:
            raise ConnectionError("Gateway connection failed")

    def _send_payment_request(self, details):
        pass

# Define domain-specific exceptions for the API
class PaymentError(Exception):
    """Base class for payment-related errors."""
    pass

class PaymentValidationError(PaymentError):
    """Raised when payment details fail validation."""
    pass

class PaymentGatewayError(PaymentError):
    """Raised when there's an issue with the payment gateway."""
    pass

class PaymentProcessingError(PaymentError):
    """Raised when payment processing fails."""
    pass

# Example usage of the API
payment_api = PaymentAPI()
try:
    result = payment_api.process_payment({"card_number": "1234-5678-9012-3456"})
    print(f"Payment result: {result}")
except PaymentValidationError as e:
    print(f"Invalid payment details: {e}")
except PaymentGatewayError as e:
    print(f"Gateway error: {e}")
except PaymentError as e:
    print(f"Payment error: {e}")

# ======================================================
# 4) Real-world Exception Handling Scenarios
# ======================================================
"""
Real-world applications often combine multiple exception handling techniques
to create robust, fault-tolerant systems.
"""

print("\n\n4. REAL-WORLD EXCEPTION HANDLING SCENARIOS")
print("=" * 50)

# 4.1 Web API Client with Robust Error Handling
print("\n4.1 Web API client with robust error handling:")

class APIClient:
    """Example API client with comprehensive error handling."""

    def __init__(self, base_url, max_retries=3):
        self.base_url = base_url
        self.max_retries = max_retries
        self.circuit_breaker = CircuitBreaker(max_failures=5, reset_timeout=60)

    def get_data(self, endpoint, params=None):
        """Get data from the API with robust error handling."""

        # Define the operation to perform with retries
        def fetch_operation():
            # This would be a real HTTP request in a real client
            print(f"Fetching data from {self.base_url}/{endpoint}")

            # Simulate various potential errors
            rand = random.random()
            if rand < 0.2:
                raise ConnectionError("Network connection error")
            elif rand < 0.4:
                raise TimeoutError("Request timed out")
            elif rand < 0.6:
                # Simulate HTTP error with status code
                status_code = random.choice([400, 403, 404, 500, 503])
                raise Exception(f"HTTP Error: {status_code}")

            # Successful response
            return {
                "data": [{"id": 1, "name": "Example"}, {"id": 2, "name": "Sample"}],
                "meta": {"total": 2}
            }

        try:
            # Apply circuit breaker pattern
            return self.circuit_breaker.execute(
                # Apply retry pattern
                lambda: retry_operation(
                    fetch_operation,
                    max_attempts=self.max_retries,
                    delay=2
                )
            )

        except ConnectionError as e:
            # Network errors
            print(f"Connection error: {e}")
            # Apply fallback pattern - return cached data
            return self._get_cached_data(endpoint)

        except TimeoutError as e:
            # Timeout errors
            print(f"Request timed out: {e}")
            # Apply fallback pattern
            return self._get_cached_data(endpoint)

        except Exception as e:
            # Unexpected errors
            print(f"API request failed: {e}")
            # Here you might log the error, notify admins, etc.
            return {"error": str(e), "data": []}

    def _get_cached_data(self, endpoint):
        """Fallback method to get cached data when live data is unavailable."""
        print(f"Returning cached data for {endpoint}")
        return {
            "data": [{"id": 1, "name": "Cached Example"}],
            "meta": {"total": 1, "cached": True}
        }

# Test the API client
api_client = APIClient("https://api.example.com")
result = api_client.get_data("users")
print(f"Final API result: {result}")

print("\n\nAdvanced exception handling techniques provide powerful tools for robust applications.")
print("By combining these patterns, you can build systems that gracefully handle failures!")
