"""
REGULAR EXPRESSIONS BASICS IN PYTHON

Regular expressions (regex) are powerful patterns used to match character combinations in strings.
This module covers regex fundamentals, syntax, and basic pattern matching operations in Python.

Key concepts:
1. Basic pattern matching
2. Character classes and special sequences
3. Quantifiers and repetition
4. Anchors and boundaries
5. The re module in Python

Regular expressions are essential for text processing, data validation, and pattern matching tasks.
"""

# =====================================================
# 1. INTRODUCTION TO REGULAR EXPRESSIONS
# =====================================================
print("=" * 50)
print("1. INTRODUCTION TO REGULAR EXPRESSIONS")
print("=" * 50)

import re  # Import Python's regex module

# Simple pattern matching
text = "Python programming is fun and Python is powerful."

# Search for the word "Python" in the text
match = re.search("Python", text)
print(f"Found '{match.group()}' at position {match.start()}-{match.end()}")

# Find all occurrences of "Python"
all_matches = re.findall("Python", text)
print(f"All matches: {all_matches}, Count: {len(all_matches)}")

# Replace all occurrences of "Python" with "Java"
new_text = re.sub("Python", "Java", text)
print(f"After replacement: {new_text}")

# Case insensitive search
case_insensitive = re.findall("python", text, re.IGNORECASE)
print(f"Case insensitive matches: {case_insensitive}, Count: {len(case_insensitive)}")

# =====================================================
# 2. CHARACTER CLASSES AND SPECIAL SEQUENCES
# =====================================================
print("\n" + "=" * 50)
print("2. CHARACTER CLASSES AND SPECIAL SEQUENCES")
print("=" * 50)

# Example text for demonstration
sample = "Python 3.9 was released on October 5th, 2020. Contact: info@python.org"

# Character classes
print("\nCharacter Classes:")
print("-" * 20)

# Match any digit
digits = re.findall(r"\d", sample)
print(f"Digits: {digits}")

# Match any non-digit
non_digits = re.findall(r"\D", sample)
print(f"Non-digits (first 10): {non_digits[:10]}...")

# Match any whitespace
whitespace = re.findall(r"\s", sample)
print(f"Whitespace characters: {whitespace}")

# Match any word character (alphanumeric + underscore)
word_chars = re.findall(r"\w", sample)
print(f"Word characters (first 10): {word_chars[:10]}...")

# Match any non-word character
non_word = re.findall(r"\W", sample)
print(f"Non-word characters: {non_word}")

# Custom character classes
print("\nCustom Character Classes:")
print("-" * 20)

# Match vowels
vowels = re.findall(r"[aeiou]", sample.lower())
print(f"Vowels: {vowels}, Count: {len(vowels)}")

# Match consonants (non-vowels among letters)
consonants = re.findall(r"[b-df-hj-np-tv-z]", sample.lower())
print(f"Consonants: {consonants}, Count: {len(consonants)}")

# Match characters in a range
alphanumeric = re.findall(r"[a-zA-Z0-9]", sample)
print(f"Alphanumeric (first 10): {alphanumeric[:10]}...")

# Negated character class (match anything NOT in the brackets)
not_letters = re.findall(r"[^a-zA-Z]", sample)
print(f"Non-letters: {not_letters}")

# =====================================================
# 3. QUANTIFIERS AND REPETITION
# =====================================================
print("\n" + "=" * 50)
print("3. QUANTIFIERS AND REPETITION")
print("=" * 50)

# Zero or more repetitions (*)
print("\nZero or More (*):")
star_pattern = re.findall(r"py.*n", "python typhoon pyn pen", re.IGNORECASE)
print(f"'py.*n' matches: {star_pattern}")  # Greedy - matches longest possible string

# One or more repetitions (+)
print("\nOne or More (+):")
plus_pattern = re.findall(r"py.+n", "python typhoon pyn pen", re.IGNORECASE)
print(f"'py.+n' matches: {plus_pattern}")  # Requires at least one character between py and n

# Zero or one repetition (?)
print("\nZero or One (?):")
optional = re.findall(r"https?://", "http://example.com https://secure.com")
print(f"'https?' matches: {optional}")  # Matches both http:// and https://

# Exact number of repetitions ({n})
print("\nExact Repetition ({n}):")
exact = re.findall(r"\d{4}", "Year 2020, card 1234, code 567")
print(f"'\\d{{4}}' matches: {exact}")  # Matches exactly 4 digits

# Range of repetitions ({m,n})
print("\nRange of Repetitions ({m,n}):")
range_pattern = re.findall(r"\d{2,4}", "Year 2020, card 1234, code 567")
print(f"'\\d{{2,4}}' matches: {range_pattern}")  # Matches 2, 3 or 4 digits

# Non-greedy matching
print("\nNon-greedy Matching:")
greedy = re.findall(r"<.+>", "<tag>content</tag>")
print(f"Greedy '<.+>' matches: {greedy}")  # Matches entire string

non_greedy = re.findall(r"<.+?>", "<tag>content</tag>")
print(f"Non-greedy '<.+?>' matches: {non_greedy}")  # Matches each tag separately

# =====================================================
# 4. ANCHORS AND BOUNDARIES
# =====================================================
print("\n" + "=" * 50)
print("4. ANCHORS AND BOUNDARIES")
print("=" * 50)

# Start of string (^)
print("\nStart of String (^):")
starts_with = re.findall(r"^Python", "Python is great\nPython is awesome", re.MULTILINE)
print(f"'^Python' matches: {starts_with}")  # Matches Python at the start of each line with MULTILINE flag

# End of string ($)
print("\nEnd of String ($):")
ends_with = re.findall(r"great$", "Python is great\nJava is great", re.MULTILINE)
print(f"'great$' matches: {ends_with}")  # Matches great at the end of each line with MULTILINE flag

# Word boundary (\b)
print("\nWord Boundary (\\b):")
whole_words = re.findall(r"\bpy\b", "py python py3 ipy", re.IGNORECASE)
print(f"'\\bpy\\b' matches: {whole_words}")  # Matches 'py' as a whole word

non_boundary = re.findall(r"\Bpy\B", "python spying copy", re.IGNORECASE)
print(f"'\\Bpy\\B' matches: {non_boundary}")  # Matches 'py' not at a boundary

# =====================================================
# 5. RE MODULE USAGE
# =====================================================
print("\n" + "=" * 50)
print("5. RE MODULE USAGE")
print("=" * 50)

# Compile regex for better performance
print("\nCompiling Regular Expressions:")
email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

test_text = "Contact us at info@example.com or support@company.co.uk for assistance."
emails = email_pattern.findall(test_text)
print(f"Emails found: {emails}")

# Match object exploration
print("\nMatch Object Methods:")
match_obj = email_pattern.search(test_text)
if match_obj:
    print(f"Found email: {match_obj.group()}")
    print(f"Position: {match_obj.start()}-{match_obj.end()}")
    print(f"Span: {match_obj.span()}")

# match vs search
print("\nmatch() vs search():")
# match checks only at the beginning of the string
match_result = re.match(r"contact", test_text, re.IGNORECASE)
print(f"match() result: {match_result}")  # None because string doesn't start with 'contact'

# search looks throughout the string
search_result = re.search(r"contact", test_text, re.IGNORECASE)
print(f"search() result: {'Found' if search_result else 'Not found'}")

# finditer for iteration
print("\nUsing finditer():")
for match in email_pattern.finditer(test_text):
    print(f"Email {match.group()} found at position {match.span()}")

# Split using regex
print("\nSplitting with regex:")
split_result = re.split(r"@|\.|-", emails[0])
print(f"Split result of {emails[0]}: {split_result}")

# =====================================================
# PRACTICE EXERCISES
# =====================================================
print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

print("\nExercise 1: Extract all dates in format DD/MM/YYYY")
text_with_dates = "Important dates: 25/12/2023, 01/01/2024 and 14/02/2024."
date_pattern = r"\d{2}/\d{2}/\d{4}"
dates = re.findall(date_pattern, text_with_dates)
print(f"Dates found: {dates}")

print("\nExercise 2: Validate phone numbers (simple pattern)")
phone_numbers = ["123-456-7890", "123.456.7890", "(123) 456-7890", "123 456 7890", "1234567890"]
valid_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

for phone in phone_numbers:
    is_valid = re.fullmatch(valid_pattern, phone) is not None
    print(f"{phone}: {'Valid' if is_valid else 'Invalid'}")

print("\nExercise 3: Replace HTML tags with their content")
html_text = "<h1>Title</h1><p>This is a <b>bold</b> paragraph.</p>"
text_only = re.sub(r"<[^>]+>", "", html_text)
print(f"Text without HTML tags: {text_only}")

# =====================================================
# SUMMARY
# =====================================================
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

"""
Regular Expressions Basics:

1. Basic Pattern Matching:
   - Use re.search() to find first match
   - Use re.findall() to find all matches
   - Use re.sub() for substitution

2. Character Classes:
   - \d: digits, \D: non-digits
   - \w: word characters, \W: non-word characters
   - \s: whitespace, \S: non-whitespace
   - Custom classes: [aeiou], [a-z], [^0-9]

3. Quantifiers:
   - *: zero or more
   - +: one or more
   - ?: zero or one
   - {n}: exactly n
   - {m,n}: between m and n

4. Anchors and Boundaries:
   - ^: start of string/line
   - $: end of string/line
   - \b: word boundary
   - \B: non-word boundary

5. re Module Functions:
   - compile(): create pattern object
   - search(): find first match
   - match(): match at beginning only
   - findall(): find all matches
   - finditer(): iterator over matches
   - split(): split string by pattern
   - sub(): substitute matches
"""

# Common use cases for regular expressions:
# - Form validation (emails, phone numbers, etc.)
# - Data extraction from unstructured text
# - Search and replace operations
# - Tokenizing text for natural language processing
# - Parsing and processing log files
