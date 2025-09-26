"""
======================================================
Python Learning - Week 02 Day 01 (Day 8 Overall)
TOPIC: FILE HANDLING IN PYTHON
======================================================

DESCRIPTION:
This file demonstrates how to work with files in Python, an essential
skill for data processing, configuration management, and many other
programming tasks. We'll explore different file formats and methods
for reading, writing, and managing files.

TOPICS COVERED:
1. Basic Text File Operations
2. Working with File Paths
3. Binary File Handling
4. CSV File Processing
5. JSON Data Handling
6. File System Operations
7. Best Practices

LEARNING OUTCOMES:
- Open, read, write, and close files safely
- Navigate and manipulate file paths across platforms
- Process structured data formats like CSV and JSON
- Perform common file system operations
- Follow best practices for file handling

======================================================
"""

import os
import csv
import json
from datetime import datetime

"""
Before we begin, let's create a directory to store our example files.
This keeps our workspace organized and prevents file clutter.
"""
# Create a directory for our file examples
EXAMPLE_DIR = "file_examples"
if not os.path.exists(EXAMPLE_DIR):
    os.makedirs(EXAMPLE_DIR)
    print(f"Created directory: {EXAMPLE_DIR}")


# ======================================================
# 1) Basic File Operations (Text Files)
# ======================================================
"""
Text files are the most common type of files to work with.
Python provides several ways to read and write text files.
"""
print("\n1. BASIC FILE OPERATIONS (TEXT FILES)")
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
print("\n1.2. Using 'with' statement (context manager):")
with open(f"{EXAMPLE_DIR}/sample2.txt", "w") as file:
    file.write("Hello from the context manager!\n")
    file.write("This file will be automatically closed.\n")
    file.write("Even if errors happen.\n")
print("File written using 'with' statement")
print("(The 'with' statement automatically closes the file when the block ends)")

# 1.3 Reading from a text file
print("\n1.3. Reading from a text file:")

# Reading the whole file at once
print("\nReading entire file:")
with open(f"{EXAMPLE_DIR}/sample1.txt", "r") as file:  # 'r' is read mode (default)
    content = file.read()  # Reads entire file into a single string
    print(f"File contents ({len(content)} characters):")
    print(content)

# Reading line by line (memory efficient for large files)
print("\nReading line by line:")
with open(f"{EXAMPLE_DIR}/sample2.txt", "r") as file:
    for i, line in enumerate(file, 1):  # start=1 for 1-based line numbering
        print(f"Line {i}: {line.strip()}")  # strip() removes trailing newline

# Reading all lines into a list
print("\nReading all lines into a list:")
with open(f"{EXAMPLE_DIR}/sample1.txt", "r") as file:
    lines = file.readlines()  # Returns a list where each element is a line
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# 1.4 Appending to a file
print("\n1.4. Appending to a file:")
with open(f"{EXAMPLE_DIR}/sample1.txt", "a") as file:  # 'a' is append mode - adds to end
    file.write(f"Appended at: {datetime.now()}\n")
    file.write("This text is added to the end of the file.\n")
print("Content appended to sample1.txt")

# Let's read it to verify
with open(f"{EXAMPLE_DIR}/sample1.txt", "r") as file:
    print("\nUpdated file contents:")
    print(file.read())

# 1.5 Different file modes
print("\n1.5. Common file modes:")
print("'r'  - Read (default) - Opens file for reading")
print("'w'  - Write - Creates new file or truncates existing file")
print("'a'  - Append - Opens for writing, appending to end of file")
print("'r+' - Read and write - Opens file for both reading and writing")
print("'b'  - Binary mode - Add to other modes (e.g., 'rb', 'wb')")
print("'t'  - Text mode (default) - File handled as text")
print("'x'  - Exclusive creation - Fails if file already exists")


# ======================================================
# 2) Working with File Paths
# ======================================================
"""
Working with file paths correctly is crucial for creating
cross-platform code. Python's os.path module provides
tools for safe path manipulation.
"""
print("\n2. WORKING WITH FILE PATHS")
print("-" * 40)

# 2.1 Getting the current working directory
print(f"2.1. Current working directory: {os.getcwd()}")
# The working directory is where Python looks for files when
# relative paths are used

# 2.2 Joining paths the right way (cross-platform)
data_dir = os.path.join(EXAMPLE_DIR, "data")  # Joins paths using correct separator for OS
if not os.path.exists(data_dir):
    os.makedirs(data_dir)  # Creates nested directories if needed
    print(f"\n2.2. Created directory: {data_dir}")

# 2.3 Path operations
file_path = os.path.join(data_dir, "test_file.txt")
with open(file_path, "w") as f:
    f.write("Testing path operations")

print("\n2.3. Path operations:")
print(f"Full path: {file_path}")
print(f"Directory name: {os.path.dirname(file_path)}")  # Get directory portion
print(f"File name: {os.path.basename(file_path)}")  # Get filename portion
print(f"File name without extension: {os.path.splitext(os.path.basename(file_path))[0]}")
print(f"File extension: {os.path.splitext(file_path)[1]}")

# 2.4 Checking if paths exist
print("\n2.4. Path existence checks:")
print(f"Does {file_path} exist? {os.path.exists(file_path)}")
print(f"Is {data_dir} a directory? {os.path.isdir(data_dir)}")
print(f"Is {file_path} a file? {os.path.isfile(file_path)}")
# These checks are important before performing operations on files/directories

# 2.5 Listing directory contents
print("\n2.5. Directory contents:")
print(f"Contents of {EXAMPLE_DIR}:")
for item in os.listdir(EXAMPLE_DIR):  # List all items in directory
    item_path = os.path.join(EXAMPLE_DIR, item)
    if os.path.isdir(item_path):
        print(f"  📁 {item} (Directory)")
    else:
        size = os.path.getsize(item_path)  # Get file size in bytes
        print(f"  📄 {item} ({size} bytes)")


# ======================================================
# 3) Binary File Handling
# ======================================================
"""
Binary files contain data that isn't formatted as text.
This includes images, audio files, compiled programs, etc.
Python can read and write binary data using the 'b' mode.
"""
print("\n3. BINARY FILE HANDLING")
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
    print(f"Decoded as ASCII: {binary_content.decode('ascii')}")  # Convert bytes to string


# ======================================================
# 4) Working with CSV Files
# ======================================================
"""
CSV (Comma-Separated Values) is a common format for storing
tabular data. Python's csv module makes it easy to read and
write CSV files without manually handling the formatting.
"""
print("\n4. WORKING WITH CSV FILES")
print("-" * 40)

# 4.1 Writing CSV data
print("4.1. Writing CSV data:")
csv_file = os.path.join(EXAMPLE_DIR, "data.csv")
data = [
    ['Name', 'Age', 'City'],               # Header row
    ['Alice', 28, 'New York'],             # Data rows
    ['Bob', 35, 'Los Angeles'],
    ['Charlie', 22, 'Chicago'],
    ['Diana', 41, 'Boston']
]

with open(csv_file, 'w', newline='') as file:  # newline='' prevents extra line breaks
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once
print(f"CSV data written to {csv_file}")

# 4.2 Reading CSV data
print("\n4.2. Reading CSV data:")
with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)  # Creates a reader object
    for i, row in enumerate(reader):
        if i == 0:
            print(f"Headers: {', '.join(row)}")
        else:
            print(f"Row {i}: {row}")

# 4.3 Using CSV DictReader and DictWriter
print("\n4.3. Using CSV DictReader and DictWriter:")
dict_csv_file = os.path.join(EXAMPLE_DIR, "dict_data.csv")

# Writing with DictWriter - uses dictionaries instead of lists
dict_data = [
    {'Name': 'Emily', 'Age': '24', 'City': 'Seattle'},
    {'Name': 'Frank', 'Age': '31', 'City': 'Portland'},
    {'Name': 'Grace', 'Age': '29', 'City': 'Austin'}
]

with open(dict_csv_file, 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header row
    writer.writerows(dict_data)  # Write all data rows
print(f"Dictionary data written to {dict_csv_file}")

# Reading with DictReader - reads each row as a dictionary
print("\nReading with DictReader:")
with open(dict_csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)  # Creates a reader that returns dictionaries
    for row in reader:
        # Access fields by name rather than position
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}")


# ======================================================
# 5) Working with JSON Files
# ======================================================
"""
JSON (JavaScript Object Notation) is a lightweight data format
that's easy for humans to read and write and easy for machines
to parse and generate. It's commonly used for web APIs and
configuration files.
"""
print("\n5. WORKING WITH JSON FILES")
print("-" * 40)

# 5.1 Writing JSON data
print("5.1. Writing JSON data:")
json_file = os.path.join(EXAMPLE_DIR, "data.json")

# Create a nested data structure
person = {
    'name': 'John Doe',
    'age': 30,
    'address': {  # Nested dictionary
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345'
    },
    'phone_numbers': [  # List of dictionaries
        {'type': 'home', 'number': '555-1234'},
        {'type': 'work', 'number': '555-5678'}
    ],
    'is_active': True,   # Boolean
    'balance': 125.45    # Float
}

with open(json_file, 'w') as file:
    # indent=2 makes the output pretty and readable
    json.dump(person, file, indent=2)
print(f"JSON data written to {json_file}")

# 5.2 Reading JSON data
print("\n5.2. Reading JSON data:")
with open(json_file, 'r') as file:
    loaded_data = json.load(file)  # Parse JSON into Python objects
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


# ======================================================
# 6) File System Operations
# ======================================================
"""
Python's os module provides many functions for interacting
with the file system. These let you create, move, rename,
and remove files and directories.
"""
print("\n6. FILE SYSTEM OPERATIONS")
print("-" * 40)

# 6.1 Creating a new directory
new_dir = os.path.join(EXAMPLE_DIR, "new_folder")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)  # Creates a single directory
    print(f"6.1. Created directory: {new_dir}")

# 6.2 Creating temporary file
temp_file = os.path.join(new_dir, "temp.txt")
with open(temp_file, 'w') as file:
    file.write("This is a temporary file.")
print(f"\n6.2. Created temporary file: {temp_file}")

# 6.3 Renaming a file
renamed_file = os.path.join(new_dir, "renamed.txt")
os.rename(temp_file, renamed_file)  # Move/rename the file
print(f"\n6.3. Renamed file to: {renamed_file}")

# 6.4 Getting file information
print("\n6.4. File information:")
file_stats = os.stat(renamed_file)  # Get file statistics
print(f"Size: {file_stats.st_size} bytes")
print(f"Last modified: {datetime.fromtimestamp(file_stats.st_mtime)}")
print(f"Last accessed: {datetime.fromtimestamp(file_stats.st_atime)}")

# 6.5 Removing files and directories
print("\n6.5. Removing files and directories:")
os.remove(renamed_file)  # Delete a file
print(f"Removed file: {renamed_file}")
os.rmdir(new_dir)  # Delete an empty directory
print(f"Removed directory: {new_dir}")


# ======================================================
# 7) Best Practices
# ======================================================
"""
Following these best practices will help you write safer,
more reliable code when working with files.
"""
print("\n7. BEST PRACTICES")
print("-" * 40)

print("1. Always use the 'with' statement for file operations")
print("   - Automatically closes files even if exceptions occur")
print("2. Check if files/directories exist before operations")
print("   - Prevents errors from trying to access non-existent files")
print("3. Use proper encoding (e.g., UTF-8) for text files")
print("   - Ensures correct handling of international characters")
print("4. Handle exceptions appropriately")
print("   - File operations can fail for many reasons (permissions, disk space)")
print("5. Close files explicitly if not using 'with'")
print("   - Prevents resource leaks and data corruption")
print("6. Use the 'os.path' module for cross-platform compatibility")
print("   - Handles different path formats between Windows, Linux, etc.")
print("7. For large files, read/write in chunks")
print("   - Prevents memory issues when dealing with huge files")
print("8. Validate user input before writing to files")
print("   - Prevents injection attacks and corrupted data")
print("9. Keep file paths relative when possible")
print("   - Makes code more portable between systems")
print("10. Backup important files before overwriting")
print("    - Prevents data loss in case of errors")

print("\n" + "=" * 50)
print("End of File Handling Examples")
print("=" * 50)

"""
SUMMARY:
- Python provides simple and powerful ways to work with files
- The 'with' statement ensures files are properly closed
- Different file formats (text, binary, CSV, JSON) require different techniques
- The os module provides tools for working with files and directories
- Following best practices prevents common file-handling issues
"""
