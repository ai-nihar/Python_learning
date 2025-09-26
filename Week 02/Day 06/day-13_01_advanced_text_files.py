"""
======================================================
Python Learning - Week 02 Day 06 (Day 13 Overall)
TOPIC: ADVANCED TEXT FILE HANDLING
======================================================

DESCRIPTION:
This file builds upon our basic text file handling knowledge,
diving deeper into advanced techniques for working with text files
in Python. We'll explore encodings, file navigation, context managers,
and efficient techniques for handling large files.

TOPICS COVERED:
1. Working with different text encodings
2. Advanced file operations (seeking and navigation)
3. Custom context managers for file operations
4. Memory-efficient approaches for large files

LEARNING OUTCOMES:
- Handle text files with various encodings correctly
- Navigate within files using seek and tell operations
- Create custom context managers for file handling
- Process large files without memory issues

======================================================
"""

import os
from pathlib import Path
from datetime import datetime
import time

"""
Before we begin, let's create a directory to store our example files.
This keeps our workspace organized and prevents file clutter.
"""
# Create a directory for our file examples using pathlib (modern approach)
EXAMPLE_DIR = Path("file_examples_advanced")
EXAMPLE_DIR.mkdir(exist_ok=True)
print(f"Working directory: {EXAMPLE_DIR}")


# ======================================================
# 1) Working with Different Text Encodings
# ======================================================
"""
Text files may use different encodings to represent characters.
UTF-8 is the most common and recommended encoding, but you might
encounter files with other encodings.
"""
print("\n" + "="*50)
print("1. WORKING WITH DIFFERENT TEXT ENCODINGS")
print("="*50)

# Create a string with non-ASCII characters
text_with_special_chars = """
Hello in different languages:
English: Hello!
Spanish: ¡Hola!
French: Bonjour!
German: Guten Tag!
Japanese: こんにちは
Chinese: 你好
Russian: Привет
Arabic: مرحبا
"""

# Write with UTF-8 encoding (recommended for most applications)
utf8_file = EXAMPLE_DIR / "text_utf8.txt"
with open(utf8_file, 'w', encoding='utf-8') as file:
    file.write(text_with_special_chars)
print(f"✅ Text written with UTF-8 encoding to {utf8_file}")

# Try with different encodings
encodings = ['utf-8', 'latin-1', 'utf-16', 'ascii']
for encoding in encodings:
    test_file = EXAMPLE_DIR / f"text_{encoding}.txt"
    try:
        with open(test_file, 'w', encoding=encoding) as file:
            file.write(text_with_special_chars)
        print(f"✅ Successfully written with {encoding} encoding")

        # Try reading it back
        with open(test_file, 'r', encoding=encoding) as file:
            content = file.read()
        print(f"   Read back {len(content)} characters")
    except UnicodeEncodeError:
        print(f"❌ Failed to write with {encoding} encoding (some characters not supported)")
    except Exception as e:
        print(f"❌ Error with {encoding}: {str(e)}")

print("\nNOTE: Always specify encoding when working with text files!")
print("UTF-8 is the recommended encoding for most applications.")


# ======================================================
# 2) Advanced File Operations - Seeking and Navigation
# ======================================================
"""
Python provides methods to navigate within files, allowing you to
jump to specific positions and read from those points.
"""
print("\n" + "="*50)
print("2. ADVANCED FILE OPERATIONS - SEEKING AND NAVIGATION")
print("="*50)

# Create a simple file with line numbers
numbered_file = EXAMPLE_DIR / "numbered_lines.txt"
with open(numbered_file, 'w') as file:
    for i in range(1, 21):
        file.write(f"Line {i}: This is content for line number {i}\n")

# Demonstrate file seeking operations
with open(numbered_file, 'r') as file:
    # Read first line
    first_line = file.readline()
    print(f"First line: {first_line.strip()}")

    # Get current position
    position = file.tell()
    print(f"Current position in file: {position} bytes")

    # Skip to specific position (beginning of 5th line)
    file.seek(0)  # Go back to beginning
    for _ in range(4):  # Skip 4 lines
        file.readline()
    print(f"5th line: {file.readline().strip()}")

    # Go back to beginning and read specific lines
    file.seek(0)
    lines = file.readlines()  # Read all lines into a list
    print(f"Line 10: {lines[9].strip()}")  # 0-indexed
    print(f"Last line: {lines[-1].strip()}")


# ======================================================
# 3) Using Context Managers for Custom File Operations
# ======================================================
"""
Custom context managers allow you to extend the functionality
of the 'with' statement for more specialized file operations.
"""
print("\n" + "="*50)
print("3. USING CONTEXT MANAGERS FOR CUSTOM FILE OPERATIONS")
print("="*50)

class TimedFileReader:
    """Custom context manager that times file reading operations"""

    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        print(f"Opening file at {self.start_time}")
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        end_time = datetime.now()
        duration = end_time - self.start_time
        print(f"File operation completed in {duration.total_seconds():.4f} seconds")
        # Return False to propagate exceptions, True to suppress them
        return False

# Use our custom context manager
try:
    with TimedFileReader(numbered_file) as file:
        content = file.read()
        print(f"Read {len(content)} characters from file")
        # Simulate some processing time
        time.sleep(0.1)
except Exception as e:
    print(f"Error: {e}")


# ======================================================
# 4) Handling Very Large Files Efficiently
# ======================================================
"""
When working with large files, it's important to use memory-efficient
approaches to avoid loading the entire file into memory.
"""
print("\n" + "="*50)
print("4. HANDLING VERY LARGE FILES EFFICIENTLY")
print("="*50)

# Create a "large" demo file
large_file = EXAMPLE_DIR / "large_demo.txt"
with open(large_file, 'w') as file:
    # Write 10,000 lines (not truly large, but demonstrates the technique)
    for i in range(10_000):
        file.write(f"This is line {i+1} with some repeated content to take up space.\n")
print(f"Created demo file with 10,000 lines")

# Inefficient way (DON'T DO THIS for truly large files)
print("\nDemonstrating inefficient vs efficient approaches:")
print("Inefficient way (loading entire file into memory):")
start_time = datetime.now()
with open(large_file, 'r') as file:
    all_content = file.read()  # Reads entire file into memory
    line_count = all_content.count('\n')
end_time = datetime.now()
print(f"Counted {line_count} lines in {(end_time - start_time).total_seconds():.4f} seconds")

# Efficient way - process line by line
print("\nEfficient way (streaming line by line):")
start_time = datetime.now()
line_count = 0
with open(large_file, 'r') as file:
    for line in file:  # File object is an iterator - reads one line at a time
        line_count += 1
end_time = datetime.now()
print(f"Counted {line_count} lines in {(end_time - start_time).total_seconds():.4f} seconds")

# Efficient way 2 - using a generator to process chunks
print("\nEfficient way 2 (processing in chunks):")
def process_file_in_chunks(filename, chunk_size=1024*8):  # 8KB chunks
    """Process a file in chunks to avoid memory issues with large files"""
    with open(filename, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:  # End of file
                break
            yield chunk

start_time = datetime.now()
total_chars = 0
line_count = 0
for chunk in process_file_in_chunks(large_file):
    total_chars += len(chunk)
    line_count += chunk.count('\n')
end_time = datetime.now()
print(f"Processed {total_chars} characters, found {line_count} lines")
print(f"Time taken: {(end_time - start_time).total_seconds():.4f} seconds")


print("\n" + "="*50)
print("SUMMARY OF ADVANCED TEXT FILE HANDLING")
print("="*50)

print("""
Key takeaways from this module:

1. Always specify encodings when working with text files,
   with UTF-8 being the recommended default.

2. File objects provide seek() and tell() methods for navigating
   within files and reading from specific positions.

3. Custom context managers can extend file handling with specialized
   behaviors like timing operations, logging, or error handling.

4. For large files, use line-by-line iteration or chunk-based 
   processing to avoid memory issues.

These techniques will help you work with text files more effectively
in your Python applications, especially when dealing with special
character sets or large data files.
""")
