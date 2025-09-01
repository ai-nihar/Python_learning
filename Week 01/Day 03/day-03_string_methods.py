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
print("Original:", repr(text))
print("lower():", text.lower())
print("upper():", text.upper())
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())
print("replace():", text.replace("Python", "Java"))
print("split():", text.split())
print("find('Python'):", text.find("Python"))
print("count('o'):", text.count('o'))
print("startswith('  Hello'):", text.startswith("  Hello"))
print("endswith('!  '):", text.endswith("!  "))
print("capitalize():", text.capitalize())
print("title():", text.title())
print("isalpha() on 'Hello':", "Hello".isalpha())
print("isdigit() on '123':", "123".isdigit())
print("isalnum() on 'abc123':", "abc123".isalnum())
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
# 1. Take a string input and print it reversed.
user_str = input("Enter a string to reverse: ")
print("Reversed:", user_str[::-1])

# 2. Count vowels in a string.
vowels = "aeiouAEIOU"
count = 0
for char in user_str:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# 3. Check if a string is a palindrome.
if user_str == user_str[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# 4. Split a sentence into words and join with '-'.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Joined with '-':", '-'.join(words))

# 5. Replace spaces with underscores in a string.
print("With underscores:", sentence.replace(' ', '_'))

