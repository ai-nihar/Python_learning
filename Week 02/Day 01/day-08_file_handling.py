"""
======================================================
Python Learning - Week 02 Day 01 (Day 8 Overall)
TOPIC: File Handling
======================================================
This file covers file handling in Python:
- Opening and closing files
- Reading from files (text and binary)
- Writing to files
- Working with file paths
- Context managers (with statement)
- CSV, JSON, and Pickle data handling
======================================================
"""

print("=" * 50)
print("DAY 8: FILE HANDLING")
print("=" * 50)
print()

import os
import csv
import json
import pickle
from datetime import datetime

# First, let's create a directory for our file examples
EXAMPLE_DIR = "file_examples"
if not os.path.exists(EXAMPLE_DIR):
    os.makedirs(EXAMPLE_DIR)
    print(f"Created directory: {EXAMPLE_DIR}")

# ======================================================
# 1) Basic File Operations (Text Files)
# ======================================================
print("1. BASIC FILE OPERATIONS (TEXT FILES)")
print("-" * 40)

# 1.1 Writing to a text file
print("1.1. Writing to a text file:")

# The old way (not recommended - requires manual close)
file = open(f"{EXAMPLE_DIR}/sample1.txt", "w")  # 'w' mode creates a new file or overwrites existing
file.write("Hello, Python file handling!\n")
file.write("This is line 2.\n")
file.write("This is line 3.\n")
file.close()  # Always remember to close files!
print("File written using traditional open()")

# The better way - using context manager (with statement)
# Automatically handles closing the file, even if exceptions occur
print("\n1.2. Using 'with' statement (context manager):")
with open(f"{EXAMPLE_DIR}/sample2.txt", "w") as file:
    file.write("Hello from the context manager!\n")
    file.write("This file will be automatically closed.\n")
    file.write("Even if errors happen.\n")
print("File written using 'with' statement")

# 1.3 Reading from a text file
print("\n1.3. Reading from a text file:")

# Reading the whole file at once
print("\nReading entire file:")
with open(f"{EXAMPLE_DIR}/sample1.txt", "r") as file:  # 'r' is read mode (default)
    content = file.read()
    print(f"File contents ({len(content)} characters):")
    print(content)

# Reading line by line
print("\nReading line by line:")
with open(f"{EXAMPLE_DIR}/sample2.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")  # strip() removes trailing newline

# Reading all lines into a list
print("\nReading all lines into a list:")
with open(f"{EXAMPLE_DIR}/sample1.txt", "r") as file:
    lines = file.readlines()  # Returns a list of lines
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# 1.4 Appending to a file
print("\n1.4. Appending to a file:")
with open(f"{EXAMPLE_DIR}/sample1.txt", "a") as file:  # 'a' is append mode
    file.write(f"Appended at: {datetime.now()}\n")
    file.write("This text is added to the end of the file.\n")
print("Content appended to sample1.txt")

# Let's read it to verify
with open(f"{EXAMPLE_DIR}/sample1.txt", "r") as file:
    print("\nUpdated file contents:")
    print(file.read())

# 1.5 Different file modes
print("\n1.5. Common file modes:")
print("'r'  - Read (default)")
print("'w'  - Write (creates new/truncates)")
print("'a'  - Append (adds to end)")
print("'r+' - Read and write")
print("'b'  - Binary mode (add to others: 'rb', 'wb')")
print("'t'  - Text mode (default)")

print()

# ======================================================
# 2) Working with File Paths
# ======================================================
print("2. WORKING WITH FILE PATHS")
print("-" * 40)

# 2.1 Getting the current working directory
print(f"2.1. Current working directory: {os.getcwd()}")

# 2.2 Joining paths the right way (cross-platform)
data_dir = os.path.join(EXAMPLE_DIR, "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"\n2.2. Created directory: {data_dir}")

# 2.3 Path operations
file_path = os.path.join(data_dir, "test_file.txt")
with open(file_path, "w") as f:
    f.write("Testing path operations")

print("\n2.3. Path operations:")
print(f"Full path: {file_path}")
print(f"Directory name: {os.path.dirname(file_path)}")
print(f"File name: {os.path.basename(file_path)}")
print(f"File name without extension: {os.path.splitext(os.path.basename(file_path))[0]}")
print(f"File extension: {os.path.splitext(file_path)[1]}")

# 2.4 Checking if paths exist
print("\n2.4. Path existence checks:")
print(f"Does {file_path} exist? {os.path.exists(file_path)}")
print(f"Is {data_dir} a directory? {os.path.isdir(data_dir)}")
print(f"Is {file_path} a file? {os.path.isfile(file_path)}")

# 2.5 Listing directory contents
print("\n2.5. Directory contents:")
print(f"Contents of {EXAMPLE_DIR}:")
for item in os.listdir(EXAMPLE_DIR):
    item_path = os.path.join(EXAMPLE_DIR, item)
    if os.path.isdir(item_path):
        print(f"  📁 {item} (Directory)")
    else:
        size = os.path.getsize(item_path)
        print(f"  📄 {item} ({size} bytes)")

print()

# ======================================================
# 3) Binary File Handling
# ======================================================
print("3. BINARY FILE HANDLING")
print("-" * 40)

# 3.1 Writing binary data
print("3.1. Writing binary data:")
binary_file = os.path.join(EXAMPLE_DIR, "binary_data.bin")
data = bytes([65, 66, 67, 68, 69])  # ASCII values for ABCDE
with open(binary_file, "wb") as file:  # 'wb' - write binary
    file.write(data)
print(f"Binary data written to {binary_file}")

# 3.2 Reading binary data
print("\n3.2. Reading binary data:")
with open(binary_file, "rb") as file:  # 'rb' - read binary
    binary_content = file.read()
    print(f"Raw bytes: {binary_content}")
    print(f"Decoded as ASCII: {binary_content.decode('ascii')}")

print()

# ======================================================
# 4) Working with CSV Files
# ======================================================
print("4. WORKING WITH CSV FILES")
print("-" * 40)

# 4.1 Writing CSV data
print("4.1. Writing CSV data:")
csv_file = os.path.join(EXAMPLE_DIR, "data.csv")
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 28, 'New York'],
    ['Bob', 35, 'Los Angeles'],
    ['Charlie', 22, 'Chicago'],
    ['Diana', 41, 'Boston']
]

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print(f"CSV data written to {csv_file}")

# 4.2 Reading CSV data
print("\n4.2. Reading CSV data:")
with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            print(f"Headers: {', '.join(row)}")
        else:
            print(f"Row {i}: {row}")

# 4.3 Using CSV DictReader and DictWriter
print("\n4.3. Using CSV DictReader and DictWriter:")
dict_csv_file = os.path.join(EXAMPLE_DIR, "dict_data.csv")

# Writing with DictWriter
dict_data = [
    {'Name': 'Emily', 'Age': 24, 'City': 'Seattle'},
    {'Name': 'Frank', 'Age': 31, 'City': 'Portland'},
    {'Name': 'Grace', 'Age': 29, 'City': 'Austin'}
]

with open(dict_csv_file, 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_data)
print(f"Dictionary data written to {dict_csv_file}")

# Reading with DictReader
print("\nReading with DictReader:")
with open(dict_csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}")

print()

# ======================================================
# 5) Working with JSON Files
# ======================================================
print("5. WORKING WITH JSON FILES")
print("-" * 40)

# 5.1 Writing JSON data
print("5.1. Writing JSON data:")
json_file = os.path.join(EXAMPLE_DIR, "data.json")

person = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345'
    },
    'phone_numbers': [
        {'type': 'home', 'number': '555-1234'},
        {'type': 'work', 'number': '555-5678'}
    ],
    'is_active': True,
    'balance': 125.45
}

with open(json_file, 'w') as file:
    # indent=2 makes the output pretty and readable
    json.dump(person, file, indent=2)
print(f"JSON data written to {json_file}")

# 5.2 Reading JSON data
print("\n5.2. Reading JSON data:")
with open(json_file, 'r') as file:
    loaded_data = json.load(file)
print(f"Loaded person: {loaded_data['name']}, {loaded_data['age']} years old")
print(f"Lives in: {loaded_data['address']['city']}, {loaded_data['address']['state']}")
print(f"Phone numbers: {len(loaded_data['phone_numbers'])}")
for phone in loaded_data['phone_numbers']:
    print(f"  {phone['type']}: {phone['number']}")

# 5.3 JSON string operations
print("\n5.3. JSON string operations:")
# Convert Python object to JSON string
json_string = json.dumps({"name": "Python", "year": 1991, "awesome": True}, indent=2)
print("JSON string:")
print(json_string)

# Parse JSON string to Python object
parsed_data = json.loads('{"language": "Python", "typing": "Dynamic"}')
print("\nParsed JSON string:")
print(f"Language: {parsed_data['language']}, Typing: {parsed_data['typing']}")

print()

# ======================================================
# 6) Using Pickle for Python Object Serialization
# ======================================================
print("6. USING PICKLE FOR PYTHON OBJECT SERIALIZATION")
print("-" * 40)

# Warning about pickle
print("⚠️ Warning: Only unpickle data from trusted sources! ⚠️")
print("Pickle can execute arbitrary code during unpickling.\n")

# 6.1 Creating a complex Python object
print("6.1. Creating and pickling a Python object:")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created_at = datetime.now()

    def greet(self):
        return f"Hello, my name is {self.name}!"

# Create an instance
person = Person("Alex", 30)
print(f"Created person object: {person.name}, {person.age} years old")
print(f"Greeting: {person.greet()}")

# 6.2 Pickle (serialize) the object
pickle_file = os.path.join(EXAMPLE_DIR, "person.pickle")
with open(pickle_file, 'wb') as file:
    pickle.dump(person, file)
print(f"\nPerson object pickled to {pickle_file}")

# 6.3 Unpickle (deserialize) the object
print("\n6.3. Unpickling the object:")
with open(pickle_file, 'rb') as file:
    loaded_person = pickle.load(file)
print(f"Loaded person: {loaded_person.name}, {loaded_person.age} years old")
print(f"Greeting: {loaded_person.greet()}")
print(f"Creation time: {loaded_person.created_at}")

print()

# ======================================================
# 7) File System Operations
# ======================================================
print("7. FILE SYSTEM OPERATIONS")
print("-" * 40)

# 7.1 Creating a new directory
new_dir = os.path.join(EXAMPLE_DIR, "new_folder")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"7.1. Created directory: {new_dir}")

# 7.2 Creating temporary file
temp_file = os.path.join(new_dir, "temp.txt")
with open(temp_file, 'w') as file:
    file.write("This is a temporary file.")
print(f"\n7.2. Created temporary file: {temp_file}")

# 7.3 Renaming a file
renamed_file = os.path.join(new_dir, "renamed.txt")
os.rename(temp_file, renamed_file)
print(f"\n7.3. Renamed file to: {renamed_file}")

# 7.4 Getting file info
print("\n7.4. File information:")
file_stats = os.stat(renamed_file)
print(f"Size: {file_stats.st_size} bytes")
print(f"Last modified: {datetime.fromtimestamp(file_stats.st_mtime)}")
print(f"Last accessed: {datetime.fromtimestamp(file_stats.st_atime)}")

# 7.5 Removing files and directories
print("\n7.5. Removing files and directories:")
os.remove(renamed_file)
print(f"Removed file: {renamed_file}")
os.rmdir(new_dir)
print(f"Removed directory: {new_dir}")

print()

# ======================================================
# 8) Best Practices
# ======================================================
print("8. BEST PRACTICES")
print("-" * 40)

print("1. Always use the 'with' statement for file operations")
print("2. Check if files/directories exist before operations")
print("3. Use proper encoding (e.g., UTF-8) for text files")
print("4. Handle exceptions appropriately")
print("5. Close files explicitly if not using 'with'")
print("6. Use the 'os.path' module for cross-platform compatibility")
print("7. For large files, read/write in chunks")
print("8. Validate user input before writing to files")
print("9. Keep file paths relative when possible")
print("10. Backup important files before overwriting")

print("\n" + "=" * 50)
print("End of File Handling Examples")
print("=" * 50)
