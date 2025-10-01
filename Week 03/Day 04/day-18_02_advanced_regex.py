"""
ADVANCED REGEX PATTERNS AND TECHNIQUES

This module covers advanced regular expression techniques in Python, building on the
basics covered previously. We'll explore complex pattern constructs, groups, and
practical applications of regex in real-world scenarios.

Key concepts:
1. Groups and capturing
2. Lookahead and lookbehind assertions
3. Advanced pattern techniques
4. Performance optimization
5. Real-world applications
"""

# =====================================================
# 1. GROUPS AND CAPTURING
# =====================================================
print("=" * 50)
print("1. GROUPS AND CAPTURING")
print("=" * 50)

import re

# Basic capturing groups
text = "Python version 3.9.5 was released in 2021"

# Capturing version number
version_match = re.search(r"Python version (\d+\.\d+\.\d+)", text)
if version_match:
    print(f"Version captured: {version_match.group(1)}")  # Access first group
    print(f"Full match: {version_match.group(0)}")  # Full match

# Multiple capturing groups
date_text = "Date: 2023-10-01"
date_match = re.search(r"Date: (\d{4})-(\d{2})-(\d{2})", date_text)
if date_match:
    year, month, day = date_match.group(1), date_match.group(2), date_match.group(3)
    print(f"Date components: Year={year}, Month={month}, Day={day}")
    print(f"All groups: {date_match.groups()}")  # Returns tuple of all groups

# Named groups
print("\nNamed Groups:")
named_match = re.search(r"Date: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date_text)
if named_match:
    print(f"Using named groups: Year={named_match.group('year')}, "
          f"Month={named_match.group('month')}, Day={named_match.group('day')}")
    print(f"Named groups dictionary: {named_match.groupdict()}")

# Non-capturing groups (?:...)
print("\nNon-capturing Groups:")
phone = "Call me at 555-123-4567 or (555) 987-6543"
# Using non-capturing group for the area code format options
numbers = re.findall(r"(?:\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}", phone)
print(f"Phone numbers: {numbers}")

# Backreferences
print("\nBackreferences:")
repeated_words = "The the quick brown fox jumps over the lazy dog dog."
# Find repeated words using backreference \1
duplicates = re.findall(r"\b(\w+)\s+\1\b", repeated_words, re.IGNORECASE)
print(f"Repeated words: {duplicates}")

# Complex example with groups
html = '<a href="https://python.org">Python Website</a>'
link_pattern = re.compile(r'<a href="([^"]+)">([^<]+)</a>')
link_match = link_pattern.search(html)
if link_match:
    url, text = link_match.groups()
    print(f"Link URL: {url}, Link Text: {text}")

# =====================================================
# 2. LOOKAHEAD AND LOOKBEHIND ASSERTIONS
# =====================================================
print("\n" + "=" * 50)
print("2. LOOKAHEAD AND LOOKBEHIND ASSERTIONS")
print("=" * 50)

# Positive lookahead (?=...)
print("\nPositive Lookahead:")
# Find all words followed by a number
words_before_numbers = re.findall(r"\b\w+\b(?=\s+\d+)", "Item1 25 Item2 30 Item3 15")
print(f"Words before numbers: {words_before_numbers}")

# Negative lookahead (?!...)
print("\nNegative Lookahead:")
# Find all words NOT followed by a number
words_not_before_numbers = re.findall(r"\b\w+\b(?!\s+\d+\b)", "Item1 25 Item2 30 Final Item")
print(f"Words not before numbers: {words_not_before_numbers}")

# Positive lookbehind (?<=...)
print("\nPositive Lookbehind:")
# Find all numbers preceded by "$"
prices = re.findall(r"(?<=\$)\d+", "Item1 $25 Item2 $30 Item3 15")
print(f"Prices (numbers after $ sign): {prices}")

# Negative lookbehind (?<!...)
print("\nNegative Lookbehind:")
# Find all numbers NOT preceded by "$"
non_prices = re.findall(r"(?<!\$)\d+", "Item1 $25 Item2 $30 Item3 15")
print(f"Non-prices (numbers not after $ sign): {non_prices}")
# Note: This will match all digits, even in $25 (the '5'). Let's fix that:
non_prices_fixed = re.findall(r"(?<!\$)\b\d+\b", "Item1 $25 Item2 $30 Item3 15")
print(f"Non-prices (fixed): {non_prices_fixed}")

# Combined lookahead and lookbehind
print("\nCombined Assertions:")
# Find words between specific words
between_words = re.findall(r"(?<=start: ).+?(?= :end)", "start: middle content :end")
print(f"Content between 'start:' and ':end': {between_words}")

# Password validation example
print("\nPassword Validation with Lookahead:")
passwords = ["weak", "strong123", "Strong123", "Strong123!", "A1b2C3d4"]

# Complex password pattern with multiple lookaheads
# Must contain:
# - At least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character
pattern = re.compile(r"""
    ^                   # Start of string
    (?=.*[A-Z])         # Lookahead for at least one uppercase letter
    (?=.*[a-z])         # Lookahead for at least one lowercase letter
    (?=.*\d)            # Lookahead for at least one digit
    (?=.*[!@#$%^&*()])  # Lookahead for at least one special character
    .{8,}               # Match at least 8 characters
    $                   # End of string
""", re.VERBOSE)

for password in passwords:
    is_valid = bool(pattern.match(password))
    print(f"Password '{password}': {'Valid' if is_valid else 'Invalid'}")

# =====================================================
# 3. ADVANCED PATTERN TECHNIQUES
# =====================================================
print("\n" + "=" * 50)
print("3. ADVANCED PATTERN TECHNIQUES")
print("=" * 50)

# Using verbose mode (re.VERBOSE)
print("\nVerbose Mode:")
# Phone pattern with comments
phone_pattern = re.compile(r"""
    \(?\d{3}\)?      # Area code (optional parentheses)
    [-.\s]?          # Optional separator
    \d{3}            # Exchange code
    [-.\s]?          # Optional separator
    \d{4}            # Local number
""", re.VERBOSE)

test_phones = ["123-456-7890", "(123) 456-7890", "123.456.7890", "123 456 7890"]
for phone in test_phones:
    if phone_pattern.match(phone):
        print(f"Phone {phone} matches the pattern")

# Conditional patterns
print("\nConditional Patterns:")
# Match 'color' or 'colour'
text_samples = ["I prefer the color blue.", "I prefer the colour blue."]
for sample in text_samples:
    # (?:ou|o) means match 'ou' or 'o'
    match = re.search(r"colou?r", sample)
    if match:
        print(f"Found '{match.group()}' in '{sample}'")

# Word boundaries and alternatives
print("\nWord Boundaries and Alternatives:")
language_text = "I code in Python, Java, and JavaScript. python is my favorite."
languages = re.findall(r"\b(?:Python|Java|JavaScript)\b", language_text, re.IGNORECASE)
print(f"Programming languages mentioned: {languages}")

# Greedy vs. non-greedy matching (deeper look)
print("\nGreedy vs. Non-greedy Matching:")
html_text = "<div>Content 1</div><div>Content 2</div>"
greedy = re.findall(r"<div>.*</div>", html_text)
print(f"Greedy match: {greedy}")

non_greedy = re.findall(r"<div>.*?</div>", html_text)
print(f"Non-greedy match: {non_greedy}")

# Character class subtraction (Python 3.7+)
print("\nCharacter Class Operations:")
# All lowercase except vowels
consonants = re.findall(r"[a-z--[aeiou]]", "python programming")
print(f"Consonants: {consonants}")

# =====================================================
# 4. PERFORMANCE OPTIMIZATION
# =====================================================
print("\n" + "=" * 50)
print("4. PERFORMANCE OPTIMIZATION")
print("=" * 50)

import time

text_to_search = "Python" * 1000 + "Java" * 1000

# Compare performance of different approaches
print("\nPerformance Comparison:")

# 1. Using pre-compiled regex
start = time.time()
pattern = re.compile(r"Python")
for _ in range(100):
    matches = pattern.findall(text_to_search)
compiled_time = time.time() - start
print(f"Pre-compiled regex: {compiled_time:.6f} seconds")

# 2. Inline regex
start = time.time()
for _ in range(100):
    matches = re.findall(r"Python", text_to_search)
inline_time = time.time() - start
print(f"Inline regex: {inline_time:.6f} seconds")

# 3. Simple string methods
start = time.time()
for _ in range(100):
    count = text_to_search.count("Python")
string_time = time.time() - start
print(f"String method: {string_time:.6f} seconds")

print(f"\nCompiled regex is {inline_time/compiled_time:.2f}x faster than inline regex")
print(f"String method is {inline_time/string_time:.2f}x faster than inline regex")
print("Use string methods when possible for simple patterns!")

# Optimization tips
print("\nOptimization Tips:")
print("1. Compile patterns you'll reuse")
print("2. Use specific patterns - avoid .* when possible")
print("3. Anchor patterns with ^ and $ when appropriate")
print("4. Use string methods for simple cases (str.startswith, str.endswith, etc.)")
print("5. Consider alternative non-regex approaches for very large datasets")

# =====================================================
# 5. REAL-WORLD APPLICATIONS
# =====================================================
print("\n" + "=" * 50)
print("5. REAL-WORLD APPLICATIONS")
print("=" * 50)

# Email validation
print("\nEmail Validation:")
emails = [
    "user@example.com",
    "user.name@example.co.uk",
    "user+tag@example.org",
    "invalid@.com",
    "@example.com",
    "user@example.",
    "user@.example.com"
]

# RFC 5322 compliant email pattern (simplified)
email_pattern = re.compile(r"""
    ^[a-zA-Z0-9._%+-]+      # Local part
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # Domain name
    \.[a-zA-Z]{2,}$         # Domain suffix (at least 2 chars)
""", re.VERBOSE)

for email in emails:
    is_valid = bool(email_pattern.match(email))
    print(f"{email}: {'Valid' if is_valid else 'Invalid'}")

# URL extraction
print("\nURL Extraction:")
web_text = """
Visit our website at https://www.example.com or http://example.org.
For secure connections, use https://secure.example.net.
Invalid URLs: http:/example ftp://wrong
"""

# URL pattern
url_pattern = re.compile(r"""
    (https?://)?            # Protocol (optional)
    (www\.)?                # www. prefix (optional)
    ([a-zA-Z0-9-]+)         # Domain name
    (\.[a-zA-Z0-9-]+)+      # Domain suffix(es)
    (/[a-zA-Z0-9./?=_&%-]*)?  # Path (optional)
""", re.VERBOSE)

urls = url_pattern.findall(web_text)
print("Extracted URLs:")
for url_parts in urls:
    # Reconstruct the full URL from the captured groups
    full_url = ''.join(url_parts)
    if full_url:  # Filter out empty matches
        print(f"- {full_url}")

# Log file parsing
print("\nLog File Parsing:")
log_entries = [
    "192.168.1.1 - - [01/Oct/2023:10:32:15 +0000] \"GET /index.html HTTP/1.1\" 200 1234",
    "192.168.1.2 - - [01/Oct/2023:10:33:20 +0000] \"POST /submit HTTP/1.1\" 302 0",
    "192.168.1.1 - - [01/Oct/2023:10:35:08 +0000] \"GET /images/logo.png HTTP/1.1\" 404 0"
]

log_pattern = re.compile(r"""
    ^(\S+)                  # IP address
    \s+-\s+-\s+             # Ignored fields
    \[([^\]]+)\]            # Date and time
    \s+"(\w+)\s+            # HTTP method
    ([^ ]+)\s+              # Requested URL
    HTTP/[0-9.]+"\s+        # HTTP version
    (\d+)\s+                # Status code
    (\d+)                   # Response size
""", re.VERBOSE)

print("Parsed Log Entries:")
for log in log_entries:
    match = log_pattern.search(log)
    if match:
        ip, date, method, url, status, size = match.groups()
        print(f"IP: {ip}, Date: {date}, Method: {method}, URL: {url}, Status: {status}, Size: {size}")

# Data extraction and transformation
print("\nData Extraction and Transformation:")
address = "John Smith, 123 Main St., Apt 4B, Boston, MA 02108"

# Extract components using named groups
address_pattern = re.compile(r"""
    (?P<name>[^,]+),\s+
    (?P<street>[^,]+),\s+
    (?P<unit>[^,]+),\s+
    (?P<city>[^,]+),\s+
    (?P<state>[A-Z]{2})\s+
    (?P<zip>\d{5})
""", re.VERBOSE)

match = address_pattern.search(address)
if match:
    data = match.groupdict()
    print("Address Components:")
    for key, value in data.items():
        print(f"  {key.capitalize()}: {value}")

    # Transform to different format
    formatted = f"{data['name']}\n{data['street']}, {data['unit']}\n{data['city']}, {data['state']} {data['zip']}"
    print("\nReformatted Address:")
    print(formatted)

# =====================================================
# PRACTICE EXERCISES
# =====================================================
print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

print("\nExercise 1: Extract all dates with named groups")
text = "Meeting on 2023-10-01, deadline on 2023-12-31"
date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
for match in re.finditer(date_pattern, text):
    date_info = match.groupdict()
    print(f"Found date: {date_info['day']}/{date_info['month']}/{date_info['year']}")

print("\nExercise 2: Validate strong passwords")
passwords = ["Abc123$!", "weakpass", "NoDigits!", "nouppercase123$", "NOLOWERCASE123$"]
for password in passwords:
    # Check for 8+ chars with at least 1 uppercase, 1 lowercase, 1 digit, 1 special
    is_strong = bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$", password))
    print(f"Password '{password}' is {'strong' if is_strong else 'weak'}")

print("\nExercise 3: Parse CSV data with regex")
csv_data = """
name,age,email
"Smith, John",34,john.smith@example.com
"Doe, Jane",28,jane.doe@example.org
"""
# Complex pattern to handle quoted fields with commas
pattern = r'"([^"]*)"[^,]*,|([^,]+),'
for line in csv_data.strip().split("\n")[1:]:  # Skip header
    fields = re.findall(pattern, line + ",")  # Add trailing comma for last field
    values = [group[0] if group[0] else group[1] for group in fields]
    print(f"Parsed: {values}")

# =====================================================
# SUMMARY
# =====================================================
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

"""
Advanced Regular Expression Techniques:

1. Groups and Capturing:
   - (pattern) - Capturing group
   - (?P<name>pattern) - Named group
   - (?:pattern) - Non-capturing group
   - \1, \2, etc. - Backreferences

2. Assertions:
   - (?=...) - Positive lookahead
   - (?!...) - Negative lookahead
   - (?<=...) - Positive lookbehind
   - (?<!...) - Negative lookbehind

3. Advanced Patterns:
   - re.VERBOSE for readable patterns
   - Character class operations (Python 3.7+)
   - Alternation with non-capturing groups

4. Performance Tips:
   - Compile regex you use repeatedly
   - Use specific patterns rather than general ones
   - Consider string methods for simple cases
   - Anchor patterns when appropriate

5. Real-world Applications:
   - Data validation (emails, passwords, etc.)
   - Log parsing and analysis
   - Data extraction and transformation
   - Text preprocessing for NLP
"""

# Common pitfalls with regular expressions:
# - Overreliance: Using regex for parsing structured formats (HTML, XML) is error-prone
# - Performance: Poorly optimized regex can lead to catastrophic backtracking
# - Maintainability: Complex regex can be difficult to understand and modify
# - Correctness: Easy to write patterns that match more/less than intended
