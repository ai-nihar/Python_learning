"""
======================================================
Python Learning - Week 02 Day 07 (Day 14 Overall)
TOPIC: MEMORY-EFFICIENT FILE PROCESSING & ENCODINGS
======================================================

DESCRIPTION:
This file explores advanced techniques for efficient file processing
and handling different text encodings in Python. These skills are
crucial when working with large files or international text data.

TOPICS COVERED:
1. Memory-Efficient File Processing
2. Working with File Encodings
3. Temporary Files and Directories
4. Best Practices for Large Files

LEARNING OUTCOMES:
- Process large files efficiently without memory issues
- Handle text files with various encodings correctly
- Use temporary files and directories effectively
- Apply best practices for file processing

======================================================
"""

import os
import tempfile
from pathlib import Path
from datetime import datetime
from io import StringIO, BytesIO

"""
Before we begin, let's create a directory to store our example files.
This keeps our workspace organized and prevents file clutter.
"""
# Create a directory for our file examples using pathlib (modern approach)
EXAMPLE_DIR = Path("file_examples_advanced")
EXAMPLE_DIR.mkdir(exist_ok=True)
print(f"Working directory: {EXAMPLE_DIR}")


# ======================================================
# 1) Memory-Efficient File Processing
# ======================================================
"""
Processing large files efficiently is a common requirement.
Here we'll explore techniques to handle large files without
loading everything into memory.
"""
print("\n" + "="*50)
print("1. MEMORY-EFFICIENT FILE PROCESSING")
print("="*50)

# Create a moderately large file for demonstration
print("Creating a sample large file...")
large_file_path = EXAMPLE_DIR / "large_sample.txt"
with open(large_file_path, 'w') as file:
    for i in range(100000):
        file.write(f"This is line {i} of our large sample file.\n")
print(f"Created file with 100,000 lines at {large_file_path}")
print(f"File size: {os.path.getsize(large_file_path) / (1024*1024):.2f} MB")

# The wrong way - loading entire file into memory
print("\nInefficient approach (loading entire file):")
start_time = datetime.now()
try:
    with open(large_file_path, 'r') as file:
        # Loading entire content into memory - AVOID THIS FOR LARGE FILES!
        content = file.read()
        print(f"Total characters: {len(content)}")
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"Elapsed time: {elapsed:.3f} seconds")
    print(f"Memory usage: Approximately {len(content) / (1024*1024):.2f} MB")
except MemoryError:
    print("Memory error - file too large to load entirely!")

# Better approach - read line by line
print("\nEfficient approach (line by line):")
start_time = datetime.now()
line_count = 0
total_chars = 0
with open(large_file_path, 'r') as file:
    for line in file:  # This iterates through lines without loading all at once
        line_count += 1
        total_chars += len(line)
        # Process each line individually
        # (Just counting in this example)
elapsed = (datetime.now() - start_time).total_seconds()
print(f"Lines processed: {line_count}")
print(f"Total characters: {total_chars}")
print(f"Elapsed time: {elapsed:.3f} seconds")
print(f"Memory usage: Minimal (just one line at a time)")

# Using context managers for automatic file closing
print("\nUsing context managers:")
with open(large_file_path, 'r') as file:
    first_line = file.readline()
    print(f"First line: {first_line.strip()}")

    # File is automatically closed after the with block
print("File is now closed (automatically by context manager)")


# ======================================================
# 2) Working with File Encodings
# ======================================================
"""
Understanding file encodings is crucial when working with text files,
especially those containing non-ASCII characters.
"""
print("\n" + "="*50)
print("2. WORKING WITH FILE ENCODINGS")
print("="*50)

# Create a string with characters from different languages
multilingual_text = """
Unicode Text Examples:
English: Hello, world!
Spanish: ¡Hola, mundo!
French: Bonjour, monde!
German: Hallo, Welt!
Russian: Привет, мир!
Japanese: こんにちは世界！
Chinese: 你好，世界！
Arabic: مرحبا بالعالم!
Greek: Γειά σου, κόσμε!
"""

# Common encodings used for text files
encodings = ["utf-8", "latin-1", "utf-16", "ascii"]

# Testing different encodings
print("Writing and reading with different encodings:")
for enc in encodings:
    encoding_file = EXAMPLE_DIR / f"encoding_{enc}.txt"
    try:
        # Try to write with this encoding
        with open(encoding_file, 'w', encoding=enc) as file:
            file.write(multilingual_text)

        # Try to read it back
        with open(encoding_file, 'r', encoding=enc) as file:
            content = file.read()

        print(f"✅ {enc}: Successfully wrote and read {len(content)} characters")
    except UnicodeEncodeError as e:
        print(f"❌ {enc}: Encoding error - {str(e)}")
    except UnicodeDecodeError as e:
        print(f"❌ {enc}: Decoding error - {str(e)}")

# The importance of specifying encoding
print("\nWhy specifying encoding is important:")
print("1. Different systems use different default encodings")
print("2. Windows often uses cp1252, macOS and Linux typically use UTF-8")
print("3. When sharing files between systems, encoding issues can arise")
print("4. Always specify encoding when opening files to avoid surprises")
print("5. UTF-8 is generally recommended as it supports all languages")

# Handling encoding errors
print("\nHandling encoding errors:")
test_file = EXAMPLE_DIR / "error_handling.txt"
error_handling_modes = [
    "strict",    # Default: raises an error for encoding issues
    "replace",   # Replace problematic characters with a replacement marker
    "ignore",    # Skip problematic characters
    "xmlcharrefreplace"  # Replace with XML character references
]

# Write a file with non-ASCII characters
with open(test_file, 'w', encoding='utf-8') as file:
    file.write(multilingual_text)

print("Reading file with restricted encoding and different error modes:")
for mode in error_handling_modes:
    try:
        with open(test_file, 'r', encoding='ascii', errors=mode) as file:
            content = file.read()
            print(f"- {mode}: Read {len(content)} characters")
            if len(content) < 50:  # Show only if content is short
                print(f"  Result: {content[:50]}")
            else:
                print(f"  Result preview: {content[:50]}...")
    except Exception as e:
        print(f"- {mode}: Error - {str(e)}")


# ======================================================
# 3) Temporary Files and Directories
# ======================================================
"""
Temporary files and directories are useful for storing intermediate
data that doesn't need to be kept permanently.
"""
print("\n" + "="*50)
print("3. TEMPORARY FILES AND DIRECTORIES")
print("="*50)

# Creating a temporary file
print("Creating a temporary file:")
with tempfile.TemporaryFile(mode='w+t') as temp_file:
    # Write to the temporary file
    temp_file.write("This is temporary data that will be automatically deleted.\n")
    temp_file.write("Temporary files are useful for intermediate processing steps.\n")

    # Go back to the beginning of the file
    temp_file.seek(0)

    # Read from the file
    content = temp_file.read()
    print(f"Temporary file contents ({len(content)} chars):")
    print(content)
print("Temporary file is automatically deleted when closed")

# Creating a named temporary file
print("\nCreating a named temporary file:")
with tempfile.NamedTemporaryFile(suffix='.txt', prefix='python_demo_', delete=False) as named_temp:
    temp_path = named_temp.name
    named_temp.write(b"This is a named temporary file.\n")
    named_temp.write(b"It has a name that we can see: " + temp_path.encode() + b"\n")

print(f"Named temporary file created at: {temp_path}")
print("Content:")
with open(temp_path, 'r') as file:
    print(file.read())

# Clean up the named temporary file
os.unlink(temp_path)
print(f"Deleted the named temporary file")

# Creating a temporary directory
print("\nCreating a temporary directory:")
with tempfile.TemporaryDirectory(prefix='python_demo_') as temp_dir:
    print(f"Temporary directory created at: {temp_dir}")

    # Create some files in the temporary directory
    for i in range(3):
        temp_file_path = Path(temp_dir) / f"tempfile_{i}.txt"
        with open(temp_file_path, 'w') as file:
            file.write(f"This is temporary file {i}.\n")

    # List the contents of the temporary directory
    print("Files in the temporary directory:")
    for item in Path(temp_dir).iterdir():
        print(f"- {item.name}")

print("Temporary directory is automatically deleted when the context manager exits")


# ======================================================
# 4) Best Practices for Large Files
# ======================================================
"""
Working with very large files requires special techniques to avoid
memory issues and ensure efficient processing.
"""
print("\n" + "="*50)
print("4. BEST PRACTICES FOR LARGE FILES")
print("="*50)

# Create another large sample file for chunked reading
print("Creating another large sample file for demonstrations...")
chunk_file_path = EXAMPLE_DIR / "chunk_sample.txt"
with open(chunk_file_path, 'w') as file:
    for i in range(100000):
        file.write(f"Line {i}: " + "A" * 50 + "\n")
print(f"Created large file at {chunk_file_path}")

# Reading in chunks (buffer size)
print("\n4.1 Reading files in chunks:")
buffer_size = 4096  # 4KB buffer
total_bytes = 0
chunk_count = 0

start_time = datetime.now()
with open(chunk_file_path, 'rb') as file:
    while True:
        chunk = file.read(buffer_size)  # Read a chunk of specified size
        if not chunk:  # End of file
            break

        # Process the chunk (just counting in this example)
        total_bytes += len(chunk)
        chunk_count += 1

elapsed = (datetime.now() - start_time).total_seconds()
print(f"Read {total_bytes} bytes in {chunk_count} chunks of {buffer_size} bytes each")
print(f"Elapsed time: {elapsed:.3f} seconds")

# Example of processing a large file by generating output incrementally
print("\n4.2 Processing a large file incrementally:")
source_file = chunk_file_path
output_file = EXAMPLE_DIR / "processed_output.txt"

start_time = datetime.now()
lines_processed = 0
# Process a large file line by line and write output incrementally
with open(source_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        # Simple transformation: uppercase and add a timestamp
        transformed = line.upper().strip() + f" [Processed: {datetime.now()}]\n"
        out_file.write(transformed)
        lines_processed += 1

        # Status update every 25,000 lines
        if lines_processed % 25000 == 0:
            print(f"Processed {lines_processed} lines...")

elapsed = (datetime.now() - start_time).total_seconds()
print(f"Processed {lines_processed} lines in {elapsed:.3f} seconds")
print(f"Output written to {output_file}")

# Using generators for memory-efficient processing
print("\n4.3 Using generators for memory-efficient processing:")

def line_processor(filename):
    """Generator that yields processed lines from a file."""
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            # Process the line (simple example: extract line number and length)
            yield line_number, len(line.strip()), line.strip()[:20]

print("Processing file using a generator (first 5 lines):")
count = 0
for line_num, length, preview in line_processor(chunk_file_path):
    print(f"Line {line_num}: length={length}, preview='{preview}...'")
    count += 1
    if count >= 5:  # Just show first 5 results
        print("... (and many more)")
        break

# Memory-efficient line counting (without loading entire file)
print("\n4.4 Memory-efficient line counting:")
start_time = datetime.now()

def count_lines(filename):
    """Count lines in a file efficiently."""
    count = 0
    with open(filename, 'rb') as file:
        for _ in file:
            count += 1
    return count

total_lines = count_lines(chunk_file_path)
elapsed = (datetime.now() - start_time).total_seconds()
print(f"File contains {total_lines} lines (counted in {elapsed:.3f} seconds)")

# Working with streaming I/O in memory
print("\n4.5 Memory stream I/O:")
print("StringIO allows string manipulation through file-like interface")

# Create an in-memory text stream
with StringIO() as mem_text:
    # Write to the in-memory stream
    mem_text.write("This is line 1\n")
    mem_text.write("This is line 2\n")
    mem_text.write("This is line 3\n")

    # Get current position
    print(f"Current position: {mem_text.tell()}")

    # Go back to beginning
    mem_text.seek(0)

    # Read from the beginning
    content = mem_text.read()
    print(f"StringIO content ({len(content)} chars):")
    print(content)

print("\nByteIO allows binary data manipulation through file-like interface")
# Create an in-memory binary stream
with BytesIO() as mem_binary:
    # Write bytes to the in-memory stream
    mem_binary.write(b"Binary data: ")
    mem_binary.write(b"\x00\x01\x02\x03\x04")

    # Go back to beginning
    mem_binary.seek(0)

    # Read as bytes
    binary_data = mem_binary.read()
    print(f"BytesIO content ({len(binary_data)} bytes):")
    print(f"Raw: {binary_data}")
    print(f"Hex: {binary_data.hex()}")


print("\n" + "="*50)
print("SUMMARY OF MEMORY-EFFICIENT FILE PROCESSING & ENCODINGS")
print("="*50)

print("""
Key takeaways from this module:

1. When processing large files, read line-by-line or in chunks
   instead of loading the entire file into memory.

2. Always specify the correct encoding when working with text files,
   especially those containing non-ASCII characters.

3. Temporary files and directories are useful for intermediate
   processing steps and are automatically cleaned up.

4. Use generators and iterators for memory-efficient processing
   of large datasets.

5. In-memory streams (StringIO and BytesIO) provide file-like
   interfaces for manipulating strings and binary data.

These techniques will help you work with files more efficiently,
especially when dealing with large datasets or memory constraints.
""")
