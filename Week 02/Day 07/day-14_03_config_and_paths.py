"""
======================================================
Python Learning - Week 02 Day 07 (Day 14 Overall)
TOPIC: CONFIGURATION FILES & PATH HANDLING
======================================================

DESCRIPTION:
This file explores working with configuration files and modern path
handling in Python. Configuration files are essential for application
settings, while pathlib provides a powerful object-oriented approach
to managing file paths across platforms.

TOPICS COVERED:
1. INI Configuration Files
2. Environment Variables
3. YAML Configuration
4. Path Handling with pathlib (Modern Approach)

LEARNING OUTCOMES:
- Work with INI configuration files using configparser
- Use environment variables for configuration
- Understand YAML configuration options
- Master modern path handling with pathlib

======================================================
"""

import os
import configparser
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
# 1) INI Configuration Files
# ======================================================
"""
INI files are a common format for configuration files with a simple
structure of sections, keys, and values.
"""
print("\n" + "="*50)
print("1. INI CONFIGURATION FILES")
print("="*50)

# Create a configuration parser
config = configparser.ConfigParser()

# Add sections and values
config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9'
}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
server = config['topsecret.server.com']
server['Port'] = '50022'
server['ForwardX11'] = 'no'
server['Host'] = 'topsecret.server.com'

# Write the configuration to a file
ini_file = EXAMPLE_DIR / "example.ini"
with open(ini_file, 'w') as configfile:
    config.write(configfile)
print(f"Created INI configuration file at {ini_file}")

# Display the contents of the INI file
print("\nINI file contents:")
with open(ini_file, 'r') as file:
    print(file.read())

# Read configuration from file
print("\nReading configuration from INI file:")
config = configparser.ConfigParser()
config.read(ini_file)

# Access configuration values
print(f"Sections: {config.sections()}")
print(f"Server port: {config['topsecret.server.com']['Port']}")
print(f"Compression enabled: {config['DEFAULT']['Compression']}")

# Check if values exist
if 'bitbucket.org' in config and 'User' in config['bitbucket.org']:
    print(f"Bitbucket user: {config['bitbucket.org']['User']}")

# Convert types (all values are stored as strings)
compression_level = config['DEFAULT'].getint('CompressionLevel')
print(f"Compression level (as integer): {compression_level}")

# Demonstration of different type converters
print("\nType conversion methods:")
print("getint() - Convert value to integer")
print("getfloat() - Convert value to float")
print("getboolean() - Convert value to boolean (accepts yes/no, on/off, true/false, 1/0)")

# Modifying and saving configuration
print("\nModifying configuration:")
config['topsecret.server.com']['Port'] = '55555'  # Change port
config['DEFAULT']['NewSetting'] = 'value'  # Add new setting

# Add a new section
config['new_section'] = {}
config['new_section']['Name'] = 'New Section'
config['new_section']['Value'] = '42'

# Save the modified configuration
with open(EXAMPLE_DIR / "modified.ini", 'w') as configfile:
    config.write(configfile)
print(f"Modified configuration saved to {EXAMPLE_DIR / 'modified.ini'}")


# ======================================================
# 2) Environment Variables
# ======================================================
"""
Environment variables are another common way to configure applications,
especially for sensitive data that shouldn't be in configuration files.
"""
print("\n" + "="*50)
print("2. ENVIRONMENT VARIABLES")
print("="*50)

# Reading environment variables
print("Some common environment variables:")
print(f"HOME: {os.environ.get('HOME', 'Not set')}")
print(f"USER: {os.environ.get('USER', 'Not set')}")
print(f"PATH: {os.environ.get('PATH', 'Not set')[:50]}... (truncated)")

# Setting environment variables
print("\nSetting environment variables in Python:")
os.environ['APP_ENV'] = 'development'
os.environ['APP_DEBUG'] = 'true'
os.environ['DB_CONNECTION'] = 'sqlite:///:memory:'

print("Newly set environment variables:")
print(f"APP_ENV: {os.environ.get('APP_ENV')}")
print(f"APP_DEBUG: {os.environ.get('APP_DEBUG')}")
print(f"DB_CONNECTION: {os.environ.get('DB_CONNECTION')}")

# Best practices for environment variables
print("\nBest practices for environment variables:")
print("1. Use for configuration that varies between environments")
print("2. Store sensitive information like API keys and passwords")
print("3. Never commit .env files to version control")
print("4. Provide a .env.example file with sample values")
print("5. Set sensible defaults when getting environment variables")


# ======================================================
# 3) YAML Configuration
# ======================================================
"""
YAML is a human-friendly data serialization standard commonly
used for configuration files in modern applications.
"""
print("\n" + "="*50)
print("3. YAML CONFIGURATION")
print("="*50)

print("YAML requires the 'PyYAML' package:")
print("pip install pyyaml")

# Example YAML configuration
print("\nExample YAML configuration:")
yaml_example = """
# Server Configuration
server:
  host: example.com
  port: 8080
  debug: true

# Database Settings
database:
  url: postgresql://user:pass@localhost/db
  pool_size: 5
  
# Features
features:
  - user_management
  - reporting
  - api_access

# Environment-specific settings
environments:
  development:
    debug: true
    log_level: DEBUG
  production:
    debug: false
    log_level: ERROR
"""

print(yaml_example)

# Advantages of YAML
print("\nAdvantages of YAML for configuration:")
print("1. Human-readable format with clear structure")
print("2. Support for complex data structures")
print("3. Less verbose than JSON (no quotes or braces required)")
print("4. Support for comments")
print("5. Easy to edit manually")


# ======================================================
# 4) Path Handling with pathlib
# ======================================================
"""
The pathlib module provides an object-oriented interface to file paths,
which is more powerful and convenient than os.path functions.
"""
print("\n" + "="*50)
print("4. PATH HANDLING WITH PATHLIB")
print("="*50)

print("Pathlib is a modern alternative to os.path for handling file paths")
print("It's been part of the standard library since Python 3.4")

# Basic path operations
print("\n4.1 Basic path operations:")

# Create a path object
file_path = Path(EXAMPLE_DIR) / "example" / "data.txt"
print(f"Path object: {file_path}")
print(f"Parent directory: {file_path.parent}")
print(f"Filename: {file_path.name}")
print(f"Stem (filename without extension): {file_path.stem}")
print(f"Extension: {file_path.suffix}")

# Creating directories
if not file_path.parent.exists():
    file_path.parent.mkdir(parents=True)
    print(f"Created directory: {file_path.parent}")

# Writing to a file
file_path.write_text("This file was created using pathlib.\nIt's much cleaner syntax!")
print(f"Wrote text to {file_path}")

# Reading from a file
content = file_path.read_text()
print(f"File content:\n{content}")

# File operations
stats = file_path.stat()
print(f"File size: {stats.st_size} bytes")
print(f"Modified: {datetime.fromtimestamp(stats.st_mtime)}")

# Iterating through directories
print("\n4.2 Listing files in directory:")
for item in EXAMPLE_DIR.iterdir():
    if item.is_file():
        print(f"FILE: {item.name} ({item.stat().st_size} bytes)")
    elif item.is_dir():
        print(f"DIR:  {item.name} ({len(list(item.iterdir()))} items)")

# Finding files with glob pattern
print("\n4.3 Finding files with glob pattern:")

# Find all text files recursively
print("Text files in directory tree:")
for text_file in EXAMPLE_DIR.glob("**/*.txt"):
    print(f"- {text_file.relative_to(EXAMPLE_DIR)}")

# Working with file paths
print("\n4.4 Working with file paths:")

# Resolving paths (absolute paths)
print(f"Absolute path: {file_path.resolve()}")

# Joining paths
data_dir = Path(EXAMPLE_DIR) / "data_files"
data_dir.mkdir(exist_ok=True)
config_file = data_dir / "config.ini"
print(f"Joined path: {config_file}")

# Changing file extensions
py_file = Path("script.py")
print(f"Original: {py_file}")
print(f"New extension: {py_file.with_suffix('.backup.py')}")

# Platform-independent path handling
print("\n4.5 Platform-independent path handling:")
print("Pathlib handles path separators correctly per platform")

# Home directory (platform independent)
home = Path.home()
print(f"Home directory: {home}")

# Current working directory
cwd = Path.cwd()
print(f"Current working directory: {cwd}")


print("\n" + "="*50)
print("SUMMARY OF CONFIGURATION FILES & PATH HANDLING")
print("="*50)

print("""
Key takeaways from this module:

1. INI files provide a simple format for configuration with sections
   and key-value pairs, easily handled with Python's configparser.

2. Environment variables are useful for configuration that varies
   between environments or for storing sensitive data.

3. YAML offers a more flexible and readable configuration format
   that supports complex data structures and comments.

4. Pathlib provides a modern, object-oriented approach to working
   with file paths, offering cleaner syntax and more functionality
   than traditional os.path functions.

These techniques help you manage application configuration and
file paths more effectively, leading to more maintainable and
platform-independent code.
""")
