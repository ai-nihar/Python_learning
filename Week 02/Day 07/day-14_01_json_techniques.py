"""
======================================================
Python Learning - Week 02 Day 07 (Day 14 Overall)
TOPIC: PRACTICAL JSON TECHNIQUES
======================================================

DESCRIPTION:
This file explores practical techniques for working with JSON (JavaScript
Object Notation) data in Python. JSON is a lightweight data format widely
used for web APIs, configuration files, and data storage. We'll cover
advanced techniques for handling complex JSON structures efficiently.

TOPICS COVERED:
1. Working with nested JSON structures
2. JSON schema validation
3. Working with JSON in memory
4. Performance techniques for large JSON files

LEARNING OUTCOMES:
- Navigate and extract data from complex nested JSON structures
- Validate JSON data against schemas
- Efficiently process and modify JSON data in memory
- Handle large JSON files without memory issues

======================================================
"""

import os
import json
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
# 1) Working with Nested JSON Structures
# ======================================================
"""
Real-world JSON data often contains deeply nested structures that
can be challenging to navigate and extract data from.
"""
print("\n" + "="*50)
print("1. WORKING WITH NESTED JSON STRUCTURES")
print("="*50)

# Create complex nested JSON data
complex_json = {
    "company": "Tech Innovations Inc.",
    "founded": 2015,
    "active": True,
    "address": {
        "street": "123 Innovation Way",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94107",
        "coordinates": {
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    "employees": [
        {
            "id": 1,
            "name": "John Smith",
            "position": "CEO",
            "skills": ["leadership", "strategy", "programming"],
            "contact": {
                "email": "john@techinnovations.com",
                "phone": "555-1234"
            }
        },
        {
            "id": 2,
            "name": "Lisa Wong",
            "position": "CTO",
            "skills": ["architecture", "python", "databases"],
            "contact": {
                "email": "lisa@techinnovations.com",
                "phone": "555-5678"
            }
        }
    ],
    "products": [
        {"name": "AI Assistant", "category": "software", "price": 499.99},
        {"name": "Data Analyzer", "category": "software", "price": 299.99},
        {"name": "Smart Hub", "category": "hardware", "price": 149.99}
    ]
}

# Save the complex JSON to a file
complex_json_file = EXAMPLE_DIR / "complex_data.json"
with open(complex_json_file, 'w') as file:
    json.dump(complex_json, file, indent=2)
print(f"Complex JSON data saved to {complex_json_file}")

# Extract data from nested JSON - safe extraction patterns
print("\nExtracting data from nested JSON:")

# Method 1: Direct access (risky if structure might change)
try:
    ceo_name = complex_json["employees"][0]["name"]
    print(f"CEO name (direct access): {ceo_name}")
except (KeyError, IndexError) as e:
    print(f"Error with direct access: {e}")

# Method 2: Safe extraction with get() method
cto_name = complex_json.get("employees", [])  # Default to empty list if key doesn't exist
if len(cto_name) > 1:
    cto_name = cto_name[1].get("name", "Unknown")
else:
    cto_name = "Unknown"
print(f"CTO name (safe access): {cto_name}")

# Method 3: Using a helper function for deep access
def get_nested(data, path, default=None):
    """Safely access nested dictionary values with a path list"""
    current = data
    for key in path:
        if isinstance(current, dict):
            current = current.get(key, {})
        elif isinstance(current, list) and isinstance(key, int) and 0 <= key < len(current):
            current = current[key]
        else:
            return default
    return current if current != {} else default

# Use the helper function for deep access
latitude = get_nested(complex_json, ["address", "coordinates", "latitude"], "Unknown")
print(f"Office latitude (helper function): {latitude}")

# Missing data returns default value
missing_value = get_nested(complex_json, ["address", "country"], "Unknown")
print(f"Country (missing, should show default): {missing_value}")

print("\nAdvantages of helper function approach:")
print("1. One consistent pattern for all nested access")
print("2. No risk of KeyError or IndexError exceptions")
print("3. Default values for missing data")
print("4. Works with any depth of nesting")
print("5. Handles both dictionaries and lists")


# ======================================================
# 2) JSON Schema Validation
# ======================================================
"""
When working with JSON data from external sources, it's important
to validate the data against an expected schema to ensure it has
the required structure and data types.
"""
print("\n" + "="*50)
print("2. JSON SCHEMA VALIDATION")
print("="*50)

print("JSON Schema validation requires the 'jsonschema' library.")
print("You can install it with: pip install jsonschema")

# Demonstrate schema validation with inline code example
print("\nExample JSON Schema validation code:")
print('''
from jsonschema import validate, ValidationError

# Define a schema for our employee data
employee_schema = {
    "type": "object",
    "required": ["id", "name", "position"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "position": {"type": "string"},
        "skills": {
            "type": "array",
            "items": {"type": "string"}
        },
        "contact": {
            "type": "object",
            "required": ["email"],
            "properties": {
                "email": {"type": "string", "format": "email"},
                "phone": {"type": "string"}
            }
        }
    }
}

# Validate data against schema
try:
    # Valid data
    validate(instance=complex_json["employees"][0], schema=employee_schema)
    print("Employee data is valid!")
    
    # Invalid data (missing required field)
    invalid_employee = {"id": 3, "name": "Jane Doe"}  # Missing "position"
    validate(instance=invalid_employee, schema=employee_schema)
except ValidationError as e:
    print(f"Validation error: {e}")
''')

print("\nCommon JSON Schema validation features:")
print("- Required properties")
print("- Type checking (string, number, boolean, object, array, etc.)")
print("- String formats (date, email, URI, etc.)")
print("- Numeric constraints (minimum, maximum, etc.)")
print("- Array constraints (minItems, maxItems, uniqueItems, etc.)")
print("- Pattern matching with regular expressions")


# ======================================================
# 3) Working with JSON in Memory
# ======================================================
"""
Python makes it easy to work with JSON data in memory through
the loads() and dumps() functions.
"""
print("\n" + "="*50)
print("3. WORKING WITH JSON IN MEMORY")
print("="*50)

# Create JSON from a string
json_string = '''
{
    "name": "Python Workshop",
    "date": "2025-09-25",
    "attendees": 25,
    "topics": ["file handling", "JSON processing", "data analysis"]
}
'''

# Parse JSON from string
workshop_data = json.loads(json_string)
print("Parsed JSON from string:")
print(f"Workshop name: {workshop_data['name']}")
print(f"Date: {workshop_data['date']}")
print(f"Attendees: {workshop_data['attendees']}")
print(f"Topics: {', '.join(workshop_data['topics'])}")

# Modify the data in memory
workshop_data["attendees"] += 5
workshop_data["topics"].append("advanced techniques")

# Convert back to JSON string
updated_json_string = json.dumps(workshop_data, indent=2)
print("\nModified and converted back to JSON string:")
print(updated_json_string)

# Customizing JSON serialization
print("\nCustomizing JSON serialization:")

# Format options
print("\nFormatting options:")
compact = json.dumps(workshop_data)
pretty = json.dumps(workshop_data, indent=2)
sorted_keys = json.dumps(workshop_data, sort_keys=True, indent=2)

print(f"Compact: {len(compact)} characters")
print(f"Pretty: {len(pretty)} characters")
print("Pretty-printed JSON with sorted keys:")
print(sorted_keys)

# Custom serialization
print("\nHandling non-JSON serializable types:")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define a custom JSON encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age, "_type": "Person"}
        elif isinstance(obj, datetime):
            return {"_type": "datetime", "value": obj.isoformat()}
        # Let the base class handle other types or raise TypeError
        return super().default(obj)

# Create data with custom objects
instructor = Person("Dr. Smith", 45)
session_data = {
    "title": "Advanced Python",
    "instructor": instructor,
    "date": datetime.now()
}

# Serialize with custom encoder
try:
    custom_json = json.dumps(session_data, cls=CustomEncoder, indent=2)
    print("\nCustom serialization result:")
    print(custom_json)
except TypeError as e:
    print(f"Error: {e}")
    print("Use a custom JSONEncoder to handle non-JSON serializable objects")


# ======================================================
# 4) Performance Techniques for Large JSON Files
# ======================================================
"""
When working with very large JSON files, it's important to use
memory-efficient approaches to avoid loading everything at once.
"""
print("\n" + "="*50)
print("4. PERFORMANCE TECHNIQUES FOR LARGE JSON FILES")
print("="*50)

# Generate a larger JSON file for demonstration
large_json_file = EXAMPLE_DIR / "large_data.json"

# Function to generate large JSON data
def generate_large_json(num_records=1000):
    """Generate a large JSON file with many records"""
    data = {
        "metadata": {
            "created": datetime.now().isoformat(),
            "version": "1.0",
            "record_count": num_records
        },
        "records": []
    }

    for i in range(num_records):
        record = {
            "id": i,
            "value": f"Record #{i}",
            "timestamp": (datetime.now().timestamp() + i),
            "active": i % 3 == 0,  # Every 3rd record is active
            "tags": [f"tag_{j}" for j in range(i % 5 + 1)]  # 1-5 tags
        }
        data["records"].append(record)

    return data

# Create the large JSON file
large_data = generate_large_json(1000)  # 1000 records
with open(large_json_file, 'w') as file:
    json.dump(large_data, file)
print(f"Created large JSON file with {len(large_data['records'])} records at {large_json_file}")

# Inefficient approach: loading the entire file
print("\nInefficient approach (loading entire file):")
start_time = datetime.now()
with open(large_json_file, 'r') as file:
    data = json.load(file)
    # Count active records
    active_records = sum(1 for record in data["records"] if record["active"])
end_time = datetime.now()
print(f"Found {active_records} active records in {(end_time - start_time).total_seconds():.4f} seconds")

# More efficient approach using streaming
print("\nFor very large JSON files, consider using the 'ijson' package for streaming:")
print("pip install ijson")
print('''
import ijson

# Process JSON file as a stream
with open('huge_data.json', 'rb') as file:
    # This only loads one object at a time into memory
    for record in ijson.items(file, 'records.item'):
        if record.get('active'):
            # Process just this record
            pass
''')

print("\nAlternative chunking approach:")
print('''
def process_large_json_in_chunks(filename, chunk_size=1000):
    """Process a large JSON file by loading chunks of records at a time"""
    with open(filename, 'r') as f:
        # Read opening bracket and metadata
        data_str = f.read(1024)  # Read initial chunk with metadata
        metadata_end = data_str.find('"records"') + 10
        
        # Position file after the records opening bracket
        f.seek(metadata_end)
        
        # Process records in chunks
        buffer = ""
        record_count = 0
        in_string = False
        escape_char = False
        bracket_count = 1  # We're inside the first [
        
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
                
            buffer += chunk
            records = []
            
            # Extract complete JSON objects
            i = 0
            while i < len(buffer):
                char = buffer[i]
                
                # Handle string literals
                if char == '"' and not escape_char:
                    in_string = not in_string
                elif char == '\\' and not escape_char:
                    escape_char = True
                    i += 1
                    continue
                
                # Only count brackets outside strings
                if not in_string:
                    if char == '{':
                        bracket_count += 1
                    elif char == '}':
                        bracket_count -= 1
                        if bracket_count == 1:  # End of object within array
                            # Extract complete record
                            record_str = buffer[:i+1]
                            try:
                                record = json.loads(record_str)
                                records.append(record)
                            except json.JSONDecodeError:
                                pass
                            
                            # Remove processed record from buffer
                            buffer = buffer[i+1:]
                            i = 0
                            continue
                
                escape_char = False
                i += 1
            
            # Process extracted records
            for record in records:
                # Do something with each record
                record_count += 1
            
        return record_count
''')


print("\n" + "="*50)
print("SUMMARY OF PRACTICAL JSON TECHNIQUES")
print("="*50)

print("""
Key takeaways from this module:

1. When working with nested JSON structures, use safe extraction 
   patterns to avoid errors when dealing with missing data.

2. JSON schema validation ensures that data conforms to expected
   structure and types, especially important for external data.

3. Python's json module provides convenient functions for parsing
   and generating JSON in memory with full control over formatting.

4. For large JSON files, consider streaming approaches to avoid
   loading the entire file into memory at once.

These techniques will help you work with JSON data more effectively
in your Python applications, from simple configuration files to
complex web API integrations.
""")
