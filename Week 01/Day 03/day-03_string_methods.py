"""
Day 3: Deep Dive into Strings & Useful Functions - Master Guide
Date: 2025-09-01

This file covers advanced string operations, methods, and some extra Python basics.
"""

# ======================================================
# 1. String Indexing and Slicing
# ======================================================
# Strings are sequences. You can access characters by index.

s = "Python Programming"
print("s[0]:", s[0])        # First character
print("s[-1]:", s[-1])      # Last character
print("s[0:6]:", s[0:6])    # 'Python'
print("s[7:]:", s[7:])      # 'Programming'
print("s[:6]:", s[:6])      # 'Python'
print("s[::2]:", s[::2])    # Every 2nd char
print("s[::-1]:", s[::-1])  # Reversed string
print()

# ======================================================
# 2. Common String Methods
# ======================================================
text = "  Hello, Python World!  "

print("Original:", repr(text))  # Shows the string with whitespace and escape characters

# --- Case Conversion ---
print("lower():", text.lower())      # All characters to lowercase -> '  hello, python world!  '
print("upper():", text.upper())      # All characters to uppercase -> '  HELLO, PYTHON WORLD!  '

# --- Whitespace Removal ---
print("strip():", text.strip())      # Remove leading/trailing whitespace -> 'Hello, Python World!'
print("lstrip():", text.lstrip())    # Remove leading whitespace -> 'Hello, Python World!  '
print("rstrip():", text.rstrip())    # Remove trailing whitespace -> '  Hello, Python World!'

# --- Replace & Split ---
print("replace('Python', 'Java'):", text.replace("Python", "Java"))  # Replace 'Python' with 'Java' -> '  Hello, Java World!  '
print("split():", text.split())      # Split into list of words (by whitespace) -> ['Hello,', 'Python', 'World!']

# --- Search & Count ---
print("find('Python'):", text.find("Python"))  # Index of 'Python' (returns -1 if not found) -> 9
print("count('o'):", text.count('o'))          # Number of 'o' in string -> 3

# --- Start/End Checks ---
print("startswith('  Hello'):", text.startswith("  Hello"))  # True if string starts with '  Hello' -> True
print("endswith('!  '):", text.endswith("!  "))              # True if string ends with '!  ' -> True

# --- Capitalization ---
print("capitalize():", text.capitalize())      # First letter uppercase, rest lowercase -> '  hello, python world!  '
print("title():", text.title())              # First letter of each word uppercase -> '  Hello, Python World!  '

# --- Character Checks ---
print("isalpha() on 'Hello':", "Hello".isalpha())      # True if all chars are letters -> True
print("isdigit() on '123':", "123".isdigit())          # True if all chars are digits -> True
print("isalnum() on 'abc123':", "abc123".isalnum())    # True if all chars are alphanumeric -> True
print()

# ======================================================
# 3. Escape Characters and Raw Strings
# ======================================================
print("Line1\nLine2")
print("Tab\tSeparated")
print(r"C:\\Users\\Name")  # Raw string, no escape
print()

# ======================================================
# 4. String Concatenation and Repetition
# ======================================================
a = "Hello"
b = "World"
print(a + " " + b)      # Concatenation
print(a * 3)            # Repetition
print()

# ======================================================
# 5. String Formatting Recap
# ======================================================
name = "Nihar"
age = 18
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))
print()

# ======================================================
# 6. Useful Built-in Functions (Extra)
# ======================================================
numbers = [3, 7, 2, 9, 4]
print("abs(-5):", abs(-5))
print("round(3.14159, 2):", round(3.14159, 2))
print("min(numbers):", min(numbers))
print("max(numbers):", max(numbers))
print("sum(numbers):", sum(numbers))
print()

# ======================================================
# 7. Practice Exercises
# ======================================================
# 1. Reverse a string input by the user
user_str = input("Enter a string to reverse: ")
print("Reversed:", user_str[::-1])  # Slicing with [::-1] reverses the string

# 2. Count vowels in the string
vowels = "aeiouAEIOU"
count = sum(1 for char in user_str if char in vowels)  # Generator expression for clarity
print("Number of vowels:", count)

# 3. Check if the string is a palindrome
if user_str == user_str[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# 4. Split a sentence and join with '-'
sentence = input("Enter a sentence: ")
words = sentence.split()  # Splits by whitespace
print("Joined with '-':", '-'.join(words))

# 5. Replace spaces with underscores
print("With underscores:", sentence.replace(' ', '_'))
