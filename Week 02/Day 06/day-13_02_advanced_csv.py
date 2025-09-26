"""
======================================================
Python Learning - Week 02 Day 06 (Day 13 Overall)
TOPIC: ADVANCED CSV OPERATIONS
======================================================

DESCRIPTION:
This file explores advanced techniques for working with CSV
(Comma-Separated Values) files in Python. We'll cover handling
complex data, custom dialects, error handling, and performance
considerations when working with CSV files.

TOPICS COVERED:
1. Working with complex CSV data
2. Custom CSV dialects
3. Handling malformed CSV data
4. CSV performance optimization

LEARNING OUTCOMES:
- Process complex CSV data with various data types
- Create custom CSV formats with dialects
- Handle errors in malformed CSV files
- Optimize CSV processing for better performance

======================================================
"""

import os
import csv
from pathlib import Path
from datetime import datetime

"""
Before we begin, let's create a directory to store our example files.
This keeps our workspace organized and prevents file clutter.
"""
# Create a directory for our file examples using pathlib (modern approach)
EXAMPLE_DIR = Path("file_examples_advanced")
EXAMPLE_DIR.mkdir(exist_ok=True)
print(f"Working directory: {EXAMPLE_DIR}")


# ======================================================
# 1) Working with Complex CSV Data
# ======================================================
"""
CSV files often contain a variety of data types and complex data
that needs special handling when reading and writing.
"""
print("\n" + "="*50)
print("1. WORKING WITH COMPLEX CSV DATA")
print("="*50)

# Create a more complex CSV file with various data types
complex_csv_file = EXAMPLE_DIR / "complex_data.csv"
with open(complex_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['ID', 'Name', 'Date', 'Values', 'Active'])
    # Write data rows with different types
    writer.writerow([1, 'Product A', '2025-01-15', '10,20,30', 'True'])
    writer.writerow([2, 'Product, with comma', '2025-02-28', '5,15', 'False'])
    writer.writerow([3, 'Product "quoted"', '2025-03-10', '', 'True'])
    writer.writerow([4, 'Multi\nline\nproduct', '2025-04-01', '42', 'True'])
print(f"Created complex CSV file at {complex_csv_file}")

# Reading complex CSV with appropriate handling
print("\nReading complex CSV data with proper handling:")
with open(complex_csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read header row first
    print(f"Headers: {header}")

    for row in reader:
        print(f"\nRow data: {row}")

        # Process and convert data appropriately
        id_num = int(row[0])
        name = row[1]
        date_str = row[2]

        # Handle empty values in lists
        values_str = row[3]
        if values_str:
            values = [int(x) for x in values_str.split(',')]
        else:
            values = []

        # Convert string to boolean
        active = row[4].lower() == 'true'

        print(f"  Processed ID: {id_num} (type: {type(id_num)})")
        print(f"  Processed Name: {name} (type: {type(name)})")
        print(f"  Processed Date: {date_str} (type: {type(date_str)})")
        print(f"  Processed Values: {values} (type: {type(values)})")
        print(f"  Processed Active: {active} (type: {type(active)})")


# ======================================================
# 2) Custom CSV Dialects
# ======================================================
"""
CSV dialects allow you to customize the formatting of CSV files,
such as using different delimiters or handling special characters.
"""
print("\n" + "="*50)
print("2. CUSTOM CSV DIALECTS")
print("="*50)

# Create a custom CSV dialect for specific formatting needs
csv.register_dialect('semicolon', delimiter=';', quotechar='"', escapechar='\\',
                    doublequote=False, quoting=csv.QUOTE_MINIMAL)

# Write CSV using our custom dialect
custom_dialect_file = EXAMPLE_DIR / "custom_dialect.csv"
with open(custom_dialect_file, 'w', newline='') as file:
    writer = csv.writer(file, dialect='semicolon')
    writer.writerow(['Name', 'Country', 'Notes'])
    writer.writerow(['Alice', 'USA', 'Some "quoted" text'])
    writer.writerow(['Bob', 'Canada', 'Text with ; semicolons'])
    writer.writerow(['Charlie', 'UK', 'Multiple\\lines\\here'])
print(f"Created CSV with custom dialect at {custom_dialect_file}")

# Read it back using the same dialect
print("\nReading CSV with custom dialect:")
with open(custom_dialect_file, 'r', newline='') as file:
    reader = csv.reader(file, dialect='semicolon')
    for row in reader:
        print(row)

print("\nExploring available dialects:")
print("Built-in dialects: ", csv.list_dialects())

# Show the properties of our custom dialect
dialect = csv.get_dialect('semicolon')
print("\nProperties of our 'semicolon' dialect:")
print(f"Delimiter: '{dialect.delimiter}'")
print(f"Quote character: '{dialect.quotechar}'")
print(f"Escape character: '{dialect.escapechar}'")
print(f"Double quote behavior: {dialect.doublequote}")


# ======================================================
# 3) Handling Malformed CSV Data
# ======================================================
"""
Real-world CSV files can contain errors, inconsistencies, or malformed 
data. Robust applications need to handle these issues gracefully.
"""
print("\n" + "="*50)
print("3. HANDLING MALFORMED CSV DATA")
print("="*50)

# Create a malformed CSV file to demonstrate error handling
malformed_csv = EXAMPLE_DIR / "malformed.csv"
with open(malformed_csv, 'w', newline='') as file:
    file.write('ID,Name,Value\n')
    file.write('1,Good row,100\n')
    file.write('2,"Unclosed quote,200\n')  # Missing closing quote
    file.write('3,Extra,Comma,300\n')      # Extra column
    file.write('4,Missing column\n')       # Missing column
    file.write('5,Good row,500\n')
print(f"Created malformed CSV file at {malformed_csv}")

# Method 1: Skip errors using error_bad_lines parameter
print("\nMethod 1: Using error handling with QUOTE_MINIMAL:")
try:
    with open(malformed_csv, 'r', newline='') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(reader):
            try:
                print(f"Row {i}: {row}")
            except csv.Error as e:
                print(f"Error in row {i}: {e}")
except csv.Error as e:
    print(f"Critical error: {e}")

# Method 2: Handle field count issues manually
print("\nMethod 2: Handle field count issues manually:")
with open(malformed_csv, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    expected_fields = len(header)
    print(f"Expected {expected_fields} fields based on header")

    for i, row in enumerate(reader, 1):
        try:
            if len(row) != expected_fields:
                print(f"Row {i} has wrong field count: {len(row)} vs expected {expected_fields}")
                # Handle missing or extra fields
                if len(row) < expected_fields:
                    # Pad with None for missing fields
                    row = row + [None] * (expected_fields - len(row))
                else:
                    # Truncate extra fields
                    row = row[:expected_fields]
            print(f"  Processed: {row}")
        except csv.Error as e:
            print(f"  Error in row {i}: {e}")


# ======================================================
# 4) CSV Performance Optimization
# ======================================================
"""
When working with large CSV files, performance considerations
become important for efficient processing.
"""
print("\n" + "="*50)
print("4. CSV PERFORMANCE OPTIMIZATION")
print("="*50)

# Create a larger CSV file
large_csv_file = EXAMPLE_DIR / "large_data.csv"
with open(large_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'value1', 'value2'])  # header
    for i in range(100_000):  # 100k rows for this demo
        writer.writerow([i, f"data_{i}", i * 2])
print(f"Created large CSV with 100,000 rows for performance testing")

# Standard approach timing
start_time = datetime.now()
row_count = 0
with open(large_csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        # Simple processing
        row_count += 1
        if row_count % 50000 == 0:
            print(f"Processed {row_count} rows...")
end_time = datetime.now()
print(f"Standard approach: Processed {row_count} rows in {(end_time - start_time).total_seconds():.4f} seconds")

# Using csv.DictReader for more readable code (slightly slower but more maintainable)
start_time = datetime.now()
row_count = 0
with open(large_csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Access by column name
        row_count += 1
        if row_count % 50000 == 0:
            print(f"Processed {row_count} rows...")
end_time = datetime.now()
print(f"DictReader approach: Processed {row_count} rows in {(end_time - start_time).total_seconds():.4f} seconds")

# Tips for CSV performance
print("\nPerformance Tips for CSV Processing:")
print("1. Always use 'newline=''` parameter when opening CSV files")
print("2. For very large files, process row-by-row instead of loading all at once")
print("3. Use standard csv.reader over DictReader when performance is critical")
print("4. Consider using pandas for very complex CSV operations if available")
print("5. Batch process and write in chunks for large output files")


print("\n" + "="*50)
print("SUMMARY OF ADVANCED CSV OPERATIONS")
print("="*50)

print("""
Key takeaways from this module:

1. CSV files can contain complex data requiring conversion between
   string representation and Python data types.

2. Custom dialects allow you to work with various CSV formats,
   including files using different delimiters or quoting styles.

3. Real-world CSV files often contain errors that need to be handled
   gracefully with appropriate error handling strategies.

4. For large CSV files, consider performance implications and use
   appropriate techniques for efficient processing.

These techniques provide a solid foundation for working with CSV files
in real-world applications, from simple data processing to complex
data integration scenarios.
""")
