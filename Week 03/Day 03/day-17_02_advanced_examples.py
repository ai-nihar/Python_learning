"""
====================================================
ADVANCED FUNCTIONAL PROGRAMMING EXAMPLES - DAY 17
====================================================

This file provides practical, real-world examples of advanced functional
programming techniques in Python to demonstrate their real-world applications.

Examples include:
- Function composition for data processing
- Curried functions in API design
- Immutable data structures for concurrent processing
- Functional error handling in a real application
- Recursion for solving complex problems
"""

print("ADVANCED FUNCTIONAL PROGRAMMING EXAMPLES")
print("=" * 50)

# =====================================================
# Example 1: Advanced Data Pipeline with Function Composition
# =====================================================
# Building a sophisticated data processing pipeline using function composition

print("\nEXAMPLE 1: ADVANCED DATA PIPELINE WITH FUNCTION COMPOSITION")
print("-" * 30)

# Import necessary modules
import functools
import datetime
import re
from collections import namedtuple

# Sample dataset: weather measurements from multiple stations
WeatherData = namedtuple('WeatherData', ['station_id', 'timestamp', 'temperature',
                                        'humidity', 'pressure', 'wind_speed', 'rain'])

raw_data = [
    {'station': 'A1', 'time': '2025-09-26 08:00:00', 'temp': '22.5', 'hum': '65.2',
     'pres': '1012.3', 'wind': '12.5', 'rain': '0.0'},
    {'station': 'B2', 'time': '2025-09-26 08:00:00', 'temp': '21.8', 'hum': '70.1',
     'pres': '1011.5', 'wind': '10.2', 'rain': '0.2'},
    {'station': 'A1', 'time': '2025-09-26 09:00:00', 'temp': 'error', 'hum': '68.3',
     'pres': '1012.1', 'wind': '13.1', 'rain': '0.0'},
    {'station': 'C3', 'time': '2025-09-26 08:00:00', 'temp': '20.2', 'hum': '72.5',
     'pres': '1010.9', 'wind': '8.5', 'rain': '1.5'},
    {'station': 'B2', 'time': '2025-09-26 09:00:00', 'temp': '22.1', 'hum': '69.5',
     'pres': '1011.2', 'wind': '11.3', 'rain': '0.1'},
    {'station': 'C3', 'time': 'invalid', 'temp': '20.5', 'hum': '73.1',
     'pres': 'error', 'wind': '9.1', 'rain': '1.2'},
]

print("Original raw weather data:")
for item in raw_data:
    print(f"  {item}")

# Define functions for data transformation

def parse_timestamp(record):
    """Parse the timestamp string into a datetime object."""
    try:
        record['timestamp'] = datetime.datetime.strptime(
            record['time'], '%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        record['timestamp'] = None
    return record

def parse_float_field(field_name, default=None):
    """Create a function that parses a specific field as float."""
    def parser(record):
        try:
            record[field_name] = float(record[field_name])
        except (ValueError, TypeError, KeyError):
            record[field_name] = default
        return record
    return parser

def rename_fields(record):
    """Rename fields to standard format."""
    field_mapping = {
        'station': 'station_id',
        'temp': 'temperature',
        'hum': 'humidity',
        'pres': 'pressure',
        'wind': 'wind_speed',
    }

    for old_name, new_name in field_mapping.items():
        if old_name in record:
            record[new_name] = record.pop(old_name)

    return record

def validate_record(record):
    """Mark if record has all required valid fields."""
    required_fields = ['station_id', 'timestamp', 'temperature',
                     'humidity', 'pressure', 'wind_speed', 'rain']

    record['is_valid'] = all(
        field in record and record[field] is not None
        for field in required_fields
    )

    return record

def convert_to_namedtuple(record):
    """Convert dictionary record to a WeatherData namedtuple if valid."""
    if record.get('is_valid', False):
        return WeatherData(
            station_id=record['station_id'],
            timestamp=record['timestamp'],
            temperature=record['temperature'],
            humidity=record['humidity'],
            pressure=record['pressure'],
            wind_speed=record['wind_speed'],
            rain=record['rain']
        )
    return None

# Function composition helper
def compose(*functions):
    """Compose multiple functions right-to-left (last function is applied first)."""
    def compose_two(f, g):
        return lambda x: f(g(x))

    if not functions:
        return lambda x: x  # Identity function

    return functools.reduce(compose_two, functions)

# Build the data transformation pipeline using function composition
process_weather_data = compose(
    convert_to_namedtuple,
    validate_record,
    parse_timestamp,
    parse_float_field('temperature'),
    parse_float_field('humidity'),
    parse_float_field('pressure'),
    parse_float_field('wind_speed'),
    parse_float_field('rain'),
    rename_fields
)

# Apply the pipeline to all records
valid_weather_data = list(filter(None, map(process_weather_data, raw_data)))

print("\nProcessed valid weather data:")
for data in valid_weather_data:
    print(f"  {data}")

# Calculate average temperature and rainfall by station
from collections import defaultdict

# Group by station
stations = defaultdict(list)
for data in valid_weather_data:
    stations[data.station_id].append(data)

# Calculate statistics
station_stats = {}
for station_id, measurements in stations.items():
    avg_temp = sum(m.temperature for m in measurements) / len(measurements)
    total_rain = sum(m.rain for m in measurements)
    station_stats[station_id] = {
        'measurements': len(measurements),
        'avg_temperature': avg_temp,
        'total_rainfall': total_rain
    }

print("\nStation statistics:")
for station, stats in station_stats.items():
    print(f"  Station {station}: {stats['measurements']} valid measurements")
    print(f"    Average temperature: {stats['avg_temperature']:.1f}°C")
    print(f"    Total rainfall: {stats['total_rainfall']:.1f}mm")

# =====================================================
# Example 2: Currying and Partial Application in API Client
# =====================================================
print("\nEXAMPLE 2: CURRYING AND PARTIAL APPLICATION IN API CLIENT")
print("-" * 30)

from functools import partial

# Simulate an API client with authentication and different endpoints
class ApiClient:
    """Demonstration of a functional approach to API client design."""

    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key

    def make_request(self, method, endpoint, params=None, headers=None):
        """Simulate making an HTTP request."""
        # In a real client, this would use requests or similar library
        full_url = f"{self.base_url}/{endpoint}"

        # Merge default headers with provided headers
        all_headers = {'Content-Type': 'application/json'}
        if self.api_key:
            all_headers['Authorization'] = f"Bearer {self.api_key}"

        if headers:
            all_headers.update(headers)

        # For this example, we'll just return a simulated response
        return {
            'url': full_url,
            'method': method,
            'params': params or {},
            'headers': all_headers,
            'simulated': True
        }

# Create a base client
api = ApiClient('https://api.example.com/v1', api_key='my_secret_key')

# Create curried request functions
def curried_request(method):
    """Return a function that applies the method to our API client."""
    def with_endpoint(endpoint):
        """Return a function that applies the endpoint."""
        def with_params(params=None):
            """Return a function that applies the parameters."""
            return api.make_request(method, endpoint, params)
        return with_params
    return with_endpoint

# Create specialized request functions using currying
get = curried_request('GET')
post = curried_request('POST')
put = curried_request('PUT')
delete = curried_request('DELETE')

# Create endpoint-specific functions using partial application
get_users = get('users')
get_user_by_id = lambda user_id: get(f'users/{user_id}')()
create_user = post('users')
update_user = lambda user_id: put(f'users/{user_id}')

# Demonstrate the API usage
print("Making API requests using curried functions:")

# Get all users
all_users_request = get_users({'page': 1, 'limit': 10})
print(f"\n1. Get all users:")
print(f"   URL: {all_users_request['url']}")
print(f"   Method: {all_users_request['method']}")
print(f"   Params: {all_users_request['params']}")

# Get specific user
user_request = get_user_by_id(123)
print(f"\n2. Get user by ID:")
print(f"   URL: {user_request['url']}")
print(f"   Method: {user_request['method']}")

# Create a new user
new_user = {'name': 'John Doe', 'email': 'john@example.com'}
create_request = create_user(new_user)
print(f"\n3. Create new user:")
print(f"   URL: {create_request['url']}")
print(f"   Method: {create_request['method']}")
print(f"   Params: {create_request['params']}")

# Update a user
update_request = update_user(123)({'status': 'active'})
print(f"\n4. Update user:")
print(f"   URL: {update_request['url']}")
print(f"   Method: {update_request['method']}")
print(f"   Params: {update_request['params']}")

# =====================================================
# Example 3: Immutable Data Structures for Concurrent Processing
# =====================================================
print("\nEXAMPLE 3: IMMUTABLE DATA STRUCTURES")
print("-" * 30)

from collections import namedtuple
import copy
import threading
import time
import random

# Define immutable data structures using namedtuples
User = namedtuple('User', ['id', 'name', 'email', 'role', 'active'])
Transaction = namedtuple('Transaction', ['id', 'user_id', 'amount', 'timestamp', 'status'])

# Create sample data
users = [
    User(1, 'Alice Smith', 'alice@example.com', 'admin', True),
    User(2, 'Bob Johnson', 'bob@example.com', 'user', True),
    User(3, 'Charlie Brown', 'charlie@example.com', 'user', False),
    User(4, 'Diana Miller', 'diana@example.com', 'manager', True),
    User(5, 'Edward Davis', 'edward@example.com', 'user', True),
]

transactions = [
    Transaction(101, 2, 125.50, datetime.datetime(2025, 9, 25, 10, 30), 'completed'),
    Transaction(102, 5, 89.99, datetime.datetime(2025, 9, 25, 11, 45), 'completed'),
    Transaction(103, 1, 250.00, datetime.datetime(2025, 9, 26, 9, 15), 'pending'),
    Transaction(104, 4, 175.25, datetime.datetime(2025, 9, 26, 14, 20), 'completed'),
    Transaction(105, 2, 49.99, datetime.datetime(2025, 9, 27, 16, 10), 'failed'),
    Transaction(106, 3, 120.00, datetime.datetime(2025, 9, 27, 17, 30), 'pending'),
]

print("Initial data structures:")
print(f"Users: {len(users)}")
print(f"Transactions: {len(transactions)}")

# Demonstrate transformations that create new data rather than modifying
def activate_user(users, user_id):
    """Return a new list of users with the specified user activated."""
    return [
        User(u.id, u.name, u.email, u.role, True) if u.id == user_id else u
        for u in users
    ]

def process_pending_transaction(transactions, transaction_id):
    """Return a new list of transactions with the specified one marked as completed."""
    return [
        Transaction(t.id, t.user_id, t.amount, t.timestamp, 'completed')
        if t.id == transaction_id and t.status == 'pending' else t
        for t in transactions
    ]

# Demonstrate thread safety with immutable data
shared_users = users
shared_transactions = transactions

def simulate_user_updates(thread_id):
    """Simulate a thread that updates users."""
    global shared_users
    print(f"Thread {thread_id} starting user updates")

    # Simulate multiple updates
    for _ in range(3):
        user_id = random.randint(1, 5)
        old_users = shared_users  # Capture current state

        # Create new state (this is an atomic operation)
        new_users = activate_user(old_users, user_id)

        # Update global state
        shared_users = new_users

        print(f"Thread {thread_id}: Activated user {user_id}")
        time.sleep(random.random() * 0.1)  # Short random delay

    print(f"Thread {thread_id} finished user updates")

def simulate_transaction_processing(thread_id):
    """Simulate a thread that processes transactions."""
    global shared_transactions
    print(f"Thread {thread_id} starting transaction processing")

    # Get pending transaction IDs
    pending_ids = [t.id for t in shared_transactions if t.status == 'pending']

    # Process each pending transaction
    for tx_id in pending_ids:
        old_transactions = shared_transactions  # Capture current state

        # Create new state
        new_transactions = process_pending_transaction(old_transactions, tx_id)

        # Update global state
        shared_transactions = new_transactions

        print(f"Thread {thread_id}: Processed transaction {tx_id}")
        time.sleep(random.random() * 0.2)  # Short random delay

    print(f"Thread {thread_id} finished transaction processing")

# Create and start threads
threads = []
for i in range(1, 4):
    # Alternate between user updates and transaction processing
    if i % 2 == 0:
        t = threading.Thread(target=simulate_user_updates, args=(i,))
    else:
        t = threading.Thread(target=simulate_transaction_processing, args=(i,))

    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("\nFinal data structures after concurrent processing:")
print("Users:")
for user in shared_users:
    print(f"  {user.name}: {'Active' if user.active else 'Inactive'}")

print("\nTransactions:")
for tx in shared_transactions:
    print(f"  ID: {tx.id}, Amount: ${tx.amount}, Status: {tx.status}")

# =====================================================
# Example 4: Functional Error Handling in Data Processing
# =====================================================
print("\nEXAMPLE 4: FUNCTIONAL ERROR HANDLING")
print("-" * 30)

# Define a Maybe monad-like class for handling potential errors
class Maybe:
    """
    A simple Maybe monad implementation.

    Represents a computation that might return a value or nothing.
    """
    def __init__(self, value=None):
        self.value = value
        self.is_nothing = value is None

    def map(self, func):
        """Apply function if value exists, otherwise return Nothing."""
        if self.is_nothing:
            return self  # Nothing
        try:
            return Maybe(func(self.value))
        except Exception as e:
            print(f"Error in operation: {e}")
            return Maybe(None)  # Convert exceptions to Nothing

    def get_or_else(self, default):
        """Return the value or a default if Nothing."""
        return self.value if not self.is_nothing else default

    def __str__(self):
        if self.is_nothing:
            return "Nothing"
        return f"Just {self.value}"

# Sample data: financial transactions with potential issues
financial_data = [
    {'account': '12345', 'amount': '520.45', 'date': '2025-09-20'},
    {'account': '67890', 'amount': 'error', 'date': '2025-09-21'},
    {'account': '24680', 'amount': '120.00', 'date': '2025-09-22'},
    {'account': '13579', 'amount': '215.75', 'date': 'invalid-date'},
    {'account': '98765', 'amount': '-50.25', 'date': '2025-09-24'},
]

print("Processing financial transactions with error handling:")

# Define functions for data validation and transformation
def parse_amount(transaction_dict):
    """Parse the amount string to float."""
    try:
        amount = float(transaction_dict['amount'])
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid amount: {e}")

def parse_date(transaction_dict):
    """Parse the date string to a datetime object."""
    try:
        return datetime.datetime.strptime(transaction_dict['date'], '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

def apply_fee(amount):
    """Apply a 2% processing fee to the amount."""
    fee = amount * 0.02
    return amount - fee

def format_transaction(transaction_dict, amount, date):
    """Format the transaction with parsed values."""
    return {
        'account': transaction_dict['account'],
        'original_amount': amount,
        'fee': amount * 0.02,
        'net_amount': amount * 0.98,
        'processed_date': date,
        'status': 'processed'
    }

# Process transactions using functional error handling
processed_transactions = []

for tx in financial_data:
    print(f"\nProcessing transaction for account {tx['account']}:")

    # Use Maybe to handle potential errors in the processing pipeline
    result = (Maybe(tx)
              .map(lambda t: (t, parse_amount(t)))  # Return tuple of (tx, amount)
              .map(lambda t_a: (t_a[0], t_a[1], parse_date(t_a[0])))  # Add date
              .map(lambda t_a_d: format_transaction(
                  t_a_d[0], apply_fee(t_a_d[1]), t_a_d[2]))  # Format final result
             )

    if result.is_nothing:
        print(f"  Failed to process transaction for account {tx['account']}")
        # In a real system, we might log the error or add to a retry queue
        processed_transactions.append({
            'account': tx['account'],
            'status': 'failed',
            'original_data': tx
        })
    else:
        print(f"  Successfully processed: {result.value['status']}")
        print(f"  Amount: ${result.value['original_amount']:.2f}")
        print(f"  Fee: ${result.value['fee']:.2f}")
        print(f"  Net amount: ${result.value['net_amount']:.2f}")
        processed_transactions.append(result.value)

# Summarize results
successful = sum(1 for tx in processed_transactions if tx['status'] == 'processed')
failed = sum(1 for tx in processed_transactions if tx['status'] == 'failed')

print("\nProcessing summary:")
print(f"Total transactions: {len(processed_transactions)}")
print(f"Successful: {successful}")
print(f"Failed: {failed}")

if successful > 0:
    total_processed = sum(tx['net_amount'] for tx in processed_transactions
                        if tx['status'] == 'processed')
    print(f"Total amount processed: ${total_processed:.2f}")

# =====================================================
# Example 5: Recursive Algorithms for Complex Problems
# =====================================================
print("\nEXAMPLE 5: RECURSIVE ALGORITHMS FOR COMPLEX PROBLEMS")
print("-" * 30)

# Problem 1: Directory tree traversal using recursion
print("RECURSIVE DIRECTORY TRAVERSAL EXAMPLE")

# Define a mock file system structure for demonstration
class FileSystemNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []
        self.content = "" if not is_directory else None
        self.size = 0

    def add_child(self, child):
        if self.is_directory:
            self.children.append(child)
        else:
            raise ValueError("Cannot add child to a file")
        return child

    def set_content(self, content):
        if not self.is_directory:
            self.content = content
            self.size = len(content)
        else:
            raise ValueError("Cannot set content for a directory")

# Create a mock file system
def create_mock_filesystem():
    root = FileSystemNode("root", True)

    docs = root.add_child(FileSystemNode("documents", True))
    pics = root.add_child(FileSystemNode("pictures", True))

    # Add files to documents
    report = docs.add_child(FileSystemNode("report.txt"))
    report.set_content("This is the annual report content...")

    notes = docs.add_child(FileSystemNode("notes.txt"))
    notes.set_content("Meeting notes from yesterday...")

    project = docs.add_child(FileSystemNode("project", True))
    readme = project.add_child(FileSystemNode("readme.md"))
    readme.set_content("# Project Documentation\n\nThis project is...")

    code = project.add_child(FileSystemNode("code.py"))
    code.set_content("def hello_world():\n    print('Hello, world!')")

    # Add files to pictures
    pic1 = pics.add_child(FileSystemNode("vacation.jpg"))
    pic1.set_content("Binary content of image")  # Simplified for demo

    pic2 = pics.add_child(FileSystemNode("family.jpg"))
    pic2.set_content("Binary content of another image")  # Simplified for demo

    return root

# Create the file system
fs_root = create_mock_filesystem()

# Recursive function to list all files and directories
def list_directory(node, indent=0):
    """Print the directory structure recursively."""
    prefix = "  " * indent
    if node.is_directory:
        print(f"{prefix}{node.name}/ (directory)")
        for child in node.children:
            list_directory(child, indent + 1)
    else:
        print(f"{prefix}{node.name} ({node.size} bytes)")

# Recursive function to find files by extension
def find_files_by_extension(node, extension, path=""):
    """Find all files with the given extension."""
    current_path = f"{path}/{node.name}" if path else node.name

    if node.is_directory:
        # Use list comprehension with a nested function call for recursion
        return [
            file_path
            for child in node.children
            for file_path in find_files_by_extension(child, extension, current_path)
        ]
    elif node.name.endswith(extension):
        return [current_path]
    else:
        return []

# Recursive function to calculate directory sizes
def calculate_directory_size(node):
    """Calculate the total size of a directory or file."""
    if not node.is_directory:
        return node.size

    # Use functional approach to sum child sizes
    return sum(calculate_directory_size(child) for child in node.children)

# Display directory tree
print("\nFile system structure:")
list_directory(fs_root)

# Find files by extension
py_files = find_files_by_extension(fs_root, ".py")
print("\nPython files found:")
for file_path in py_files:
    print(f"  {file_path}")

txt_files = find_files_by_extension(fs_root, ".txt")
print("\nText files found:")
for file_path in txt_files:
    print(f"  {file_path}")

# Calculate directory sizes
total_size = calculate_directory_size(fs_root)
print(f"\nTotal file system size: {total_size} bytes")

# Get size of specific directories
for child in fs_root.children:
    dir_size = calculate_directory_size(child)
    print(f"Size of '{child.name}' directory: {dir_size} bytes")

# Problem 2: Tree-based data processing with recursion
print("\nRECURSIVE TREE-BASED DATA PROCESSING")

# Define a tree structure for organizational hierarchy
class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)
        return employee

    def __str__(self):
        return f"{self.name} ({self.position})"

# Create a sample organization structure
def create_org_chart():
    # Executive level
    ceo = Employee(1, "John Smith", "CEO", 250000)

    # Management level
    cto = ceo.add_subordinate(Employee(2, "Emma Johnson", "CTO", 180000))
    cfo = ceo.add_subordinate(Employee(3, "Michael Brown", "CFO", 190000))
    cmo = ceo.add_subordinate(Employee(4, "Sarah Davis", "CMO", 175000))

    # IT Department
    lead_dev = cto.add_subordinate(Employee(5, "David Wilson", "Lead Developer", 120000))
    lead_dev.add_subordinate(Employee(6, "Lisa Miller", "Senior Developer", 100000))
    lead_dev.add_subordinate(Employee(7, "Robert Taylor", "Senior Developer", 100000))
    lead_dev.add_subordinate(Employee(8, "Jennifer Garcia", "Developer", 85000))

    sysadmin = cto.add_subordinate(Employee(9, "Kevin Martinez", "System Administrator", 95000))
    sysadmin.add_subordinate(Employee(10, "Laura Anderson", "Network Specialist", 82000))

    # Finance Department
    controller = cfo.add_subordinate(Employee(11, "Thomas Robinson", "Controller", 115000))
    controller.add_subordinate(Employee(12, "Patricia White", "Senior Accountant", 90000))
    controller.add_subordinate(Employee(13, "James Lee", "Accountant", 75000))

    # Marketing Department
    marketing_director = cmo.add_subordinate(Employee(14, "Christopher Harris", "Marketing Director", 110000))
    marketing_director.add_subordinate(Employee(15, "Barbara Clark", "Marketing Specialist", 80000))
    marketing_director.add_subordinate(Employee(16, "Daniel Lewis", "Social Media Manager", 78000))

    return ceo

# Create the organization chart
org_root = create_org_chart()

# Recursive function to print organization hierarchy
def print_org_chart(employee, level=0):
    """Print the organizational chart with hierarchy."""
    indent = "  " * level
    print(f"{indent}- {employee.name} ({employee.position})")

    for subordinate in employee.subordinates:
        print_org_chart(subordinate, level + 1)

# Recursive function to calculate department salary totals
def calculate_department_salary(manager):
    """Calculate total salary for a manager and all subordinates."""
    # Base salary is the manager's salary
    total = manager.salary

    # Add salaries of all subordinates recursively
    for subordinate in manager.subordinates:
        total += calculate_department_salary(subordinate)

    return total

# Recursive function to find employees by criteria
def find_employees_by_criteria(employee, predicate):
    """Find all employees that match the given predicate."""
    # Check if the current employee matches
    matches = [employee] if predicate(employee) else []

    # Recursively check all subordinates
    for subordinate in employee.subordinates:
        matches.extend(find_employees_by_criteria(subordinate, predicate))

    return matches

# Print the organization chart
print("\nOrganization Chart:")
print_org_chart(org_root)

# Calculate department salary totals
print("\nDepartment Salary Totals:")
print(f"Total company payroll: ${calculate_department_salary(org_root):,.2f}")

# Calculate each department's payroll
for executive in org_root.subordinates:
    dept_total = calculate_department_salary(executive)
    print(f"{executive.position} department: ${dept_total:,.2f}")

# Find employees by criteria
high_salary_employees = find_employees_by_criteria(
    org_root, lambda e: e.salary > 100000)
print(f"\nEmployees with salary over $100,000: {len(high_salary_employees)}")
for emp in high_salary_employees:
    print(f"  {emp.name}: ${emp.salary:,.2f}")

developers = find_employees_by_criteria(
    org_root, lambda e: "Developer" in e.position)
print(f"\nAll developers: {len(developers)}")
for dev in developers:
    print(f"  {dev.name}: {dev.position}")

print("\n" + "=" * 50)
