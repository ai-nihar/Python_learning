"""
======================================================
Python Learning - Week 02 Day 07 (Day 14 Overall)
TOPIC: WORKING WITH ZIP AND ARCHIVE FILES
======================================================

DESCRIPTION:
This file demonstrates how to work with ZIP and other archive files
in Python. Archive files are commonly used for distributing software,
backing up data, and efficiently storing multiple files. We'll explore
Python's built-in zipfile module and other archiving capabilities.

TOPICS COVERED:
1. Creating and extracting ZIP files
2. Working with password-protected archives
3. Creating multi-file archives with different formats
4. Best practices for archive handling

LEARNING OUTCOMES:
- Create and extract ZIP files using Python's zipfile module
- Work with password-protected archives
- Use different archive formats (ZIP, TAR, GZTAR)
- Apply best practices for efficient archive management

======================================================
"""

import os
import zipfile
import shutil
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
# 1) Creating and Extracting ZIP Files
# ======================================================
"""
The zipfile module in Python's standard library provides tools for
creating, reading, writing, and extracting ZIP files.
"""
print("\n" + "="*50)
print("1. CREATING AND EXTRACTING ZIP FILES")
print("="*50)

# Create some example files to archive
print("Creating example files to archive...")
text_file_path = EXAMPLE_DIR / "sample.txt"
with open(text_file_path, 'w') as file:
    file.write("This is a sample text file for ZIP demonstration.\n" * 10)

python_file_path = EXAMPLE_DIR / "example.py"
with open(python_file_path, 'w') as file:
    file.write("""
print("Hello from a zipped Python file!")

def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print(f"10 + 20 = {result}")
""")

# Create subdirectory with files
subdir_path = EXAMPLE_DIR / "subdir"
subdir_path.mkdir(exist_ok=True)

for i in range(3):
    with open(subdir_path / f"file{i}.txt", 'w') as file:
        file.write(f"This is file {i} in the subdirectory.\n" * 3)

print(f"Created example files in {EXAMPLE_DIR} and {subdir_path}")

# Basic ZIP file creation
basic_zip_path = EXAMPLE_DIR / "basic_archive.zip"
with zipfile.ZipFile(basic_zip_path, 'w') as zip_file:
    # Add individual files to the ZIP
    zip_file.write(text_file_path, arcname="sample.txt")
    zip_file.write(python_file_path, arcname="example.py")

    # Print info about the ZIP file
    print(f"\nCreated ZIP file: {basic_zip_path}")
    print(f"Contains {len(zip_file.namelist())} files")
    print(f"Files: {', '.join(zip_file.namelist())}")

# Create a ZIP with compression
compressed_zip_path = EXAMPLE_DIR / "compressed_archive.zip"
with zipfile.ZipFile(compressed_zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
    # Add individual files with compression
    zip_file.write(text_file_path, arcname="sample.txt")
    zip_file.write(python_file_path, arcname="example.py")

    # Add all files from subdirectory
    for file_path in subdir_path.glob("*.txt"):
        zip_file.write(file_path, arcname=f"subdir/{file_path.name}")

    print(f"\nCreated compressed ZIP file: {compressed_zip_path}")
    print(f"Contains {len(zip_file.namelist())} files")
    print(f"Files: {', '.join(zip_file.namelist())}")

# Comparison of file sizes
basic_size = os.path.getsize(basic_zip_path)
compressed_size = os.path.getsize(compressed_zip_path)
original_size = os.path.getsize(text_file_path) + os.path.getsize(python_file_path)

print(f"\nOriginal files size: {original_size} bytes")
print(f"Basic ZIP size: {basic_size} bytes")
print(f"Compressed ZIP size: {compressed_size} bytes")
print(f"Compression ratio: {compressed_size/original_size:.2%}")

# Extract ZIP contents
extract_dir = EXAMPLE_DIR / "extracted"
extract_dir.mkdir(exist_ok=True)

with zipfile.ZipFile(compressed_zip_path, 'r') as zip_ref:
    # Extract all files to directory
    zip_ref.extractall(extract_dir)

    # Print the extracted files
    print(f"\nExtracted files to {extract_dir}")
    extracted_files = list(extract_dir.glob("**/*"))
    print(f"Extracted {len(extracted_files)} files/directories")

    # List ZIP contents without extracting
    print("\nListing ZIP contents without extracting:")
    for info in zip_ref.infolist():
        print(f"- {info.filename} ({info.file_size} bytes, "
              f"compressed: {info.compress_size} bytes, "
              f"ratio: {info.compress_size/info.file_size if info.file_size else 1:.2%})")


# ======================================================
# 2) Working with Password-Protected Archives
# ======================================================
"""
ZIP files can be password-protected for sensitive information.
Python's zipfile module supports working with encrypted archives.
"""
print("\n" + "="*50)
print("2. WORKING WITH PASSWORD-PROTECTED ARCHIVES")
print("="*50)

# Create a password-protected ZIP
encrypted_zip_path = EXAMPLE_DIR / "encrypted_archive.zip"
password = b"SecretPassword123"  # Password must be bytes

print("\nCreating password-protected ZIP file...")
try:
    with zipfile.ZipFile(encrypted_zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        # Add files with encryption
        zip_file.setpassword(password)

        # Note: For encryption, we need to use writestr instead of write
        # and manually set the encryption flag
        with open(text_file_path, 'r') as f:
            content = f.read()
            zip_info = zipfile.ZipInfo("secure_sample.txt")
            zip_info.compress_type = zipfile.ZIP_DEFLATED
            zip_info.flag_bits |= 0x1  # Set encryption flag
            zip_file.writestr(zip_info, content, password)

        print(f"Created encrypted ZIP file: {encrypted_zip_path}")
except Exception as e:
    print(f"Error creating encrypted ZIP: {e}")
    print("Note: Some ZIP encryption features require additional packages like 'pyzipper'")
    print("Consider: pip install pyzipper")

# Demonstrate using pyzipper for password-protected ZIPs
print("\nCode example for using pyzipper for encrypted ZIPs:")
print('''
# Using pyzipper for better encryption support
import pyzipper

# Create encrypted ZIP
with pyzipper.AESZipFile('encrypted.zip', 'w', compression=pyzipper.ZIP_LZMA) as zf:
    zf.setpassword(b'password123')
    zf.setencryption(pyzipper.WZ_AES, nbits=256)
    
    with open('secret.txt', 'rb') as f:
        zf.writestr('secret.txt', f.read())

# Extract from encrypted ZIP
with pyzipper.AESZipFile('encrypted.zip', 'r') as zf:
    zf.setpassword(b'password123')
    data = zf.read('secret.txt')
    print(data.decode('utf-8'))
''')

print("\nImportant notes on ZIP encryption:")
print("1. Standard ZIP encryption (ZipCrypto) is not highly secure")
print("2. For better security, use AES encryption with third-party libraries")
print("3. Never use ZIP encryption as the only security measure for sensitive data")
print("4. Modern tools like 7-Zip offer stronger encryption options")


# ======================================================
# 3) Creating Multi-File Archives with Different Formats
# ======================================================
"""
Python's shutil module provides high-level functions for creating
archives in various formats like ZIP, TAR, GZTAR, and more.
"""
print("\n" + "="*50)
print("3. CREATING MULTI-FILE ARCHIVES WITH DIFFERENT FORMATS")
print("="*50)

# Create directory with multiple files for archiving
archive_source_dir = EXAMPLE_DIR / "multiple_files"
archive_source_dir.mkdir(exist_ok=True)

for i in range(5):
    with open(archive_source_dir / f"document_{i}.txt", 'w') as file:
        file.write(f"This is document {i}\n" * 20)

# Create a small image-like binary file
with open(archive_source_dir / "sample.bin", 'wb') as file:
    file.write(os.urandom(1024))  # 1KB of random data

print(f"Created example directory with multiple files: {archive_source_dir}")

# List available archive formats
print("\nAvailable archive formats in shutil:")
for format_name in shutil.get_archive_formats():
    print(f"- {format_name[0]}: {format_name[1]}")

# Create archives in different formats
formats_to_try = ['zip', 'tar', 'gztar', 'bztar', 'xztar']
created_archives = []

for format_name in formats_to_try:
    try:
        # Archive path without extension (shutil adds the appropriate one)
        archive_path = str(EXAMPLE_DIR / f"multi_archive_{format_name}")

        # Create the archive
        result_path = shutil.make_archive(
            base_name=archive_path,
            format=format_name,
            root_dir=str(EXAMPLE_DIR),
            base_dir="multiple_files"
        )

        created_archives.append((format_name, result_path))
        print(f"\nCreated {format_name} archive: {result_path}")
        print(f"Size: {os.path.getsize(result_path)} bytes")
    except Exception as e:
        print(f"Error creating {format_name} archive: {e}")

# Compare archive sizes
if created_archives:
    print("\nArchive size comparison:")
    for format_name, path in created_archives:
        size = os.path.getsize(path)
        print(f"- {format_name}: {size} bytes")

    # Calculate source directory total size
    source_size = sum(os.path.getsize(os.path.join(dirpath, filename))
                  for dirpath, dirnames, filenames in os.walk(archive_source_dir)
                  for filename in filenames)

    print(f"\nOriginal files total size: {source_size} bytes")
    print(f"Best compression ratio: {min(os.path.getsize(path) for _, path in created_archives) / source_size:.2%}")

# Unpacking archives
print("\nUnpacking archives example:")
for format_name, archive_path in created_archives[:1]:  # Just demo with the first archive
    extract_path = EXAMPLE_DIR / f"extracted_{format_name}"
    try:
        shutil.unpack_archive(archive_path, extract_path)
        print(f"Unpacked {format_name} archive to {extract_path}")

        # Count extracted files
        extracted_count = sum(1 for _ in Path(extract_path).glob("**/*") if _.is_file())
        print(f"Extracted {extracted_count} files")
    except Exception as e:
        print(f"Error unpacking {format_name} archive: {e}")


# ======================================================
# 4) Best Practices for Archive Handling
# ======================================================
"""
Working with archives effectively requires following some best
practices to avoid common issues and security vulnerabilities.
"""
print("\n" + "="*50)
print("4. BEST PRACTICES FOR ARCHIVE HANDLING")
print("="*50)

print("""
1. Security Considerations:
   - Always validate archive contents before extraction
   - Be cautious with archives from untrusted sources
   - Watch out for path traversal attacks ("zip slip")
   - Avoid extracting archives with absolute paths

2. Efficient Archive Creation:
   - Choose appropriate compression format based on needs
   - For text files: ZIP with DEFLATE or GZTAR are good choices
   - For already compressed files (images, videos): use uncompressed storage
   - For mixed content: ZIP or TAR formats offer good balance

3. Memory Management:
   - For large archives, extract files individually rather than all at once
   - Use streaming extraction for very large files
   - Consider using temporary directories for extraction

4. Error Handling:
   - Always handle exceptions when working with archives
   - Verify archive integrity before extraction
   - Implement retry mechanisms for network-based archives

5. Cross-Platform Considerations:
   - Be aware of path separator differences (/ vs \\)
   - Consider filename encoding issues between platforms
   - Use pathlib for path manipulations to ensure cross-platform compatibility
""")

# Demonstrate safe extraction (avoiding path traversal)
print("\nDemonstration of safe archive extraction (preventing path traversal):")
print('''
def safe_extract(zip_path, extract_path):
    """Safely extract a ZIP file, preventing path traversal attacks."""
    extract_path = Path(extract_path)
    extract_path.mkdir(exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Validate file paths before extraction
        for file_info in zip_ref.infolist():
            # Convert to Path object for safe path manipulation
            target_path = extract_path / file_info.filename
            
            # Check for path traversal
            if not str(target_path).startswith(str(extract_path)):
                print(f"WARNING: Blocked extraction of {file_info.filename} - path traversal detected")
                continue
                
            # Check for absolute paths
            if Path(file_info.filename).is_absolute():
                print(f"WARNING: Blocked extraction of {file_info.filename} - absolute path detected")
                continue
                
            # Safe to extract this file
            zip_ref.extract(file_info, extract_path)
            print(f"Safely extracted: {file_info.filename}")
''')

# Create a problematic ZIP with path traversal for demonstration
print("\nCreating demonstration of path traversal vulnerability:")
malicious_zip_path = EXAMPLE_DIR / "malicious_demo.zip"

with zipfile.ZipFile(malicious_zip_path, 'w') as zip_file:
    # Regular file
    zip_file.writestr("regular.txt", "This is a normal file")

    # Problematic path (path traversal)
    zip_file.writestr("../traversal_attempt.txt", "This file attempts path traversal")

    # Problematic absolute path
    if os.name == 'nt':  # Windows
        zip_file.writestr("C:/Windows/bad_idea.txt", "This attempts to write to system directory")
    else:  # Unix-like
        zip_file.writestr("/etc/bad_idea.txt", "This attempts to write to system directory")

print(f"Created demonstration ZIP file: {malicious_zip_path}")
print("IMPORTANT: This is for educational purposes only")
print("In real applications, always implement proper security checks")


print("\n" + "="*50)
print("SUMMARY OF ARCHIVE FILE HANDLING")
print("="*50)

print("""
Key takeaways from this module:

1. Python's zipfile module provides comprehensive tools for working
   with ZIP archives, including compression and encryption.

2. For better security, consider third-party libraries like pyzipper
   that support stronger encryption methods.

3. The shutil module offers convenient functions for creating archives
   in various formats like ZIP, TAR, GZTAR, and more.

4. Always implement security measures when working with archives,
   especially from untrusted sources, to prevent path traversal attacks.

5. Choose the appropriate archive format and compression level based
   on your specific needs (file types, size, compression ratio).

These skills will help you efficiently work with archived data in your
Python applications, whether for data backup, distribution, or storage.
""")
