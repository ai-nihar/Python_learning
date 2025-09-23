"""
======================================================
Python Learning - Week 02 Day 04 (Day 11 Overall)
TOPIC: OBSERVER PATTERN AND CONTEXT MANAGERS
======================================================

DESCRIPTION:
This file explores the Observer design pattern and Context Managers in Python.
The Observer pattern establishes a one-to-many relationship between objects,
while Context Managers provide a clean way to manage resources.

TOPICS COVERED:
1. Observer Pattern
2. Implementation in Python
3. Context Managers
4. Custom Context Managers
5. Practical applications

LEARNING OUTCOMES:
- Understand and implement the Observer pattern
- Create event notification systems
- Use context managers for resource management
- Create custom context managers
- Apply these concepts to real-world problems

======================================================
"""

# =====================================================
# 1. OBSERVER PATTERN
# =====================================================
print("=" * 50)
print("1. OBSERVER PATTERN")
print("=" * 50)

"""
The Observer Pattern defines a one-to-many dependency between objects.
When one object (the subject) changes state, all its dependents (observers)
are notified and updated automatically.

Uses:
- Event handling systems
- MVC architecture
- Notification services
"""

class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class Observer:
    def __init__(self, name):
        self.name = name

    def notify(self, subject, *args, **kwargs):
        print(f"Observer {self.name} received: {args}, {kwargs}")

# Example: Weather Station (Subject) and Displays (Observers)
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if self._temperature != value:
            self._temperature = value
            self.notify_all("temperature", new_value=value)

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        if self._humidity != value:
            self._humidity = value
            self.notify_all("humidity", new_value=value)

# Specialized observers
class PhoneDisplay(Observer):
    def notify(self, subject, *args, **kwargs):
        if args[0] == "temperature":
            print(f"Phone App: Temperature updated to {kwargs['new_value']}°F")
        elif args[0] == "humidity":
            print(f"Phone App: Humidity updated to {kwargs['new_value']}%")

class SmartHomeController(Observer):
    def __init__(self, name):
        super().__init__(name)
        self.ac_on = False

    def notify(self, subject, *args, **kwargs):
        if args[0] == "temperature":
            temp = kwargs['new_value']
            if temp > 78 and not self.ac_on:
                self.ac_on = True
                print(f"Smart Home: Turning AC ON (temp={temp}°F)")
            elif temp < 70 and self.ac_on:
                self.ac_on = False
                print(f"Smart Home: Turning AC OFF (temp={temp}°F)")

# Create observers
phone_display = PhoneDisplay("Phone App")
weather_channel = Observer("Weather Channel")
smart_home = SmartHomeController("Smart Home")

# Create subject
weather_station = WeatherStation()

# Register observers
weather_station.register(phone_display)
weather_station.register(weather_channel)
weather_station.register(smart_home)

# Change temperature - should notify all observers
print("Setting temperature to 75°F")
weather_station.temperature = 75

# Change humidity
print("\nSetting humidity to 60%")
weather_station.humidity = 60

# Change temperature to trigger AC
print("\nSetting temperature to 80°F")
weather_station.temperature = 80

# Change temperature again to turn off AC
print("\nSetting temperature to 68°F")
weather_station.temperature = 68

# Unregister an observer
print("\nUnregistering Weather Channel")
weather_station.unregister(weather_channel)

# Update again - should not notify Weather Channel
print("Setting temperature to 72°F")
weather_station.temperature = 72

# =====================================================
# 2. PRACTICAL OBSERVER PATTERN EXAMPLE
# =====================================================
print("\n" + "=" * 50)
print("2. PRACTICAL OBSERVER PATTERN EXAMPLE")
print("=" * 50)

"""
Let's implement a more practical example of the Observer pattern with
a stock market price tracking system.
"""

class StockMarket(Subject):
    def __init__(self):
        super().__init__()
        self._stock_prices = {}

    def set_price(self, symbol, price):
        old_price = self._stock_prices.get(symbol)
        self._stock_prices[symbol] = price
        self.notify_all("price_update", symbol=symbol, price=price, old_price=old_price)

class StockTrader(Observer):
    def __init__(self, name, watch_list):
        super().__init__(name)
        self.watch_list = watch_list

    def notify(self, subject, *args, **kwargs):
        if args[0] == "price_update" and kwargs["symbol"] in self.watch_list:
            symbol = kwargs["symbol"]
            price = kwargs["price"]
            old_price = kwargs["old_price"]

            if old_price is None:
                print(f"Trader {self.name}: Initial price for {symbol} is ${price}")
            else:
                change = price - old_price
                percent = (change / old_price) * 100
                direction = "up" if change > 0 else "down"
                print(f"Trader {self.name}: {symbol} is {direction} to ${price:.2f} ({percent:.2f}%)")

class AutoTrader(Observer):
    def __init__(self, name, buy_threshold, sell_threshold):
        super().__init__(name)
        self.buy_threshold = buy_threshold  # Buy if price drops by this %
        self.sell_threshold = sell_threshold  # Sell if price increases by this %
        self.portfolio = {}  # symbol -> (shares, purchase_price)
        self.cash = 10000  # Initial cash

    def notify(self, subject, *args, **kwargs):
        if args[0] == "price_update":
            symbol = kwargs["symbol"]
            price = kwargs["price"]
            old_price = kwargs["old_price"]

            if old_price is None:
                return

            # Calculate percent change
            percent_change = ((price - old_price) / old_price) * 100

            # Check for sell opportunities in current portfolio
            if symbol in self.portfolio and percent_change >= self.sell_threshold:
                shares, purchase_price = self.portfolio[symbol]
                profit = shares * (price - purchase_price)
                self.cash += shares * price
                print(f"AutoTrader {self.name}: SELLING {shares} shares of {symbol} at ${price:.2f}")
                print(f"Profit: ${profit:.2f}, New cash balance: ${self.cash:.2f}")
                del self.portfolio[symbol]

            # Check for buying opportunity
            elif symbol not in self.portfolio and percent_change <= -self.buy_threshold:
                shares_to_buy = int(self.cash * 0.1 / price)  # Use 10% of cash
                if shares_to_buy > 0:
                    cost = shares_to_buy * price
                    self.cash -= cost
                    self.portfolio[symbol] = (shares_to_buy, price)
                    print(f"AutoTrader {self.name}: BUYING {shares_to_buy} shares of {symbol} at ${price:.2f}")
                    print(f"Cost: ${cost:.2f}, New cash balance: ${self.cash:.2f}")

# Create stock market
market = StockMarket()

# Create traders
human_trader = StockTrader("John", ["AAPL", "GOOG", "MSFT"])
bot_trader = AutoTrader("RoboTrader", buy_threshold=5, sell_threshold=7)

# Register with market
market.register(human_trader)
market.register(bot_trader)

# Set initial prices
print("\nSetting initial stock prices:")
market.set_price("AAPL", 150.0)
market.set_price("GOOG", 2800.0)
market.set_price("MSFT", 300.0)
market.set_price("AMZN", 3300.0)

# Simulate price changes
print("\nSimulating market activity:")
# AAPL drops 6%
market.set_price("AAPL", 141.0)  # Bot should buy

# GOOG rises 8%
market.set_price("GOOG", 3024.0)  # Bot should sell if it bought

# MSFT rises 3%
market.set_price("MSFT", 309.0)  # No action from bot

# AAPL recovers 10%
market.set_price("AAPL", 155.1)  # Bot should sell if it bought

print("\nThe Observer pattern allows objects to react to changes in other objects!")

# =====================================================
# 3. CONTEXT MANAGERS
# =====================================================
print("\n" + "=" * 50)
print("3. CONTEXT MANAGERS")
print("=" * 50)

"""
Context managers are used to allocate and release resources precisely
when you want to. The most common example is opening and closing files.

They implement the __enter__ and __exit__ methods (context management protocol).
"""

# Built-in context managers
print("Using built-in context manager for file handling:")
with open("example_file.txt", "w") as f:
    f.write("Hello, context manager world!")
    print("File written inside context")

print("Context exited, file should be closed")

# Check if the file was created and closed
import os
if os.path.exists("example_file.txt"):
    print(f"File exists: {os.path.abspath('example_file.txt')}")

    # Try to read the closed file to verify it was closed
    try:
        f.write("This should fail")
    except ValueError as e:
        print(f"File is closed: {e}")

# Read the file with another context manager
with open("example_file.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

# =====================================================
# 4. CUSTOM CONTEXT MANAGERS
# =====================================================
print("\n" + "=" * 50)
print("4. CUSTOM CONTEXT MANAGERS")
print("=" * 50)

# Context manager using class
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"Opening connection to {self.db_name}")
        self.connected = True
        # In a real case, we'd connect to the DB here
        self.dummy_data = {"users": ["Alice", "Bob"]}
        return self  # Return self as the context object

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connected = False
        # In a real case, we'd close the connection here

        # Handle exceptions that occurred inside the context
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
            return False  # Re-raise the exception

    def query(self, table):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        if table in self.dummy_data:
            return self.dummy_data[table]
        else:
            raise ValueError(f"Table '{table}' not found")

# Using the context manager
print("Using class-based context manager:")
try:
    with DatabaseConnection("users_db") as conn:
        print("Connection is open inside the context")
        users = conn.query("users")
        print(f"Users: {users}")

        # Let's cause an exception
        nonexistent = conn.query("products")
except ValueError as e:
    print(f"Caught exception outside context: {e}")

print("\nConnection should be closed now regardless of exception")

# Context manager using decorator and generator
from contextlib import contextmanager

@contextmanager
def file_opener(filename, mode="r"):
    try:
        # Setup - resource acquisition
        print(f"Opening file {filename} in {mode} mode")
        file = open(filename, mode)
        yield file  # Yield control back to the with block
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        yield None  # Still yield something to avoid breaking the with block
    finally:
        # Teardown - resource release
        if 'file' in locals() and file is not None:
            print(f"Closing file {filename}")
            file.close()

# Using the generator-based context manager
print("\nUsing generator-based context manager:")
with file_opener("example_file.txt") as file:
    if file:
        content = file.read()
        print(f"Read from file: {content}")

# With a non-existent file
print("\nTrying with a non-existent file:")
with file_opener("non_existent_file.txt") as file:
    if file:
        print("This won't execute because file is None")
    else:
        print("File is None - handled gracefully")

# =====================================================
# 5. PRACTICAL CONTEXT MANAGERS
# =====================================================
print("\n" + "=" * 50)
print("5. PRACTICAL CONTEXT MANAGERS")
print("=" * 50)

# Timing context manager
@contextmanager
def timer(description):
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{description}: {elapsed:.5f} seconds")

# Using the timer
with timer("Calculating sum of 1M numbers"):
    sum(range(1_000_000))

with timer("List comprehension"):
    [i*i for i in range(100_000)]

# Indentation context manager
@contextmanager
def indented_block(indent=4):
    try:
        # Remember the current indentation setting
        import sys
        old_stdout = sys.stdout

        class IndentedStream:
            def __init__(self, stream, indent_level):
                self.stream = stream
                self.indent = " " * indent_level
                self.new_line = True

            def write(self, text):
                if self.new_line:
                    text = self.indent + text
                self.new_line = text.endswith('\n')
                # Replace internal newlines with indented newlines
                text = text.replace('\n', '\n' + self.indent)
                self.stream.write(text)

            def __getattr__(self, name):
                return getattr(self.stream, name)

        sys.stdout = IndentedStream(sys.stdout, indent)
        yield
    finally:
        sys.stdout = old_stdout

print("Without indentation:")
print("Line 1")
print("Line 2")

print("\nWith indentation:")
with indented_block(4):
    print("Line 1")
    print("Line 2")
    with indented_block(4):  # Additional indentation
        print("Nested line 1")
        print("Nested line 2")
    print("Back to first level")

print("Outside indentation again")

# =====================================================
# 6. RESOURCE MANAGEMENT WITH CONTEXT MANAGERS
# =====================================================
print("\n" + "=" * 50)
print("6. RESOURCE MANAGEMENT WITH CONTEXT MANAGERS")
print("=" * 50)

"""
Context managers are particularly useful for managing resources like
files, network connections, locks, and database connections.
"""

# Multiple context managers
@contextmanager
def temporary_file(content):
    import tempfile
    import os

    # Create a temporary file
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        print(f"Created temporary file: {path}")
        yield path
    finally:
        os.close(fd)
        os.remove(path)
        print(f"Removed temporary file: {path}")

# Using both context managers together
with temporary_file("Hello, world!") as temp_path:
    with open(temp_path, 'r') as f:
        content = f.read()
        print(f"Read from temporary file: {content}")
    print("File still exists here")
print("File should be gone now")

# Cleanup
import os
if os.path.exists("example_file.txt"):
    os.remove("example_file.txt")
    print("Cleaned up example_file.txt")
