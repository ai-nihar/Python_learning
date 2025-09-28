"""
====================================================
PRACTICAL FUNCTIONAL PROGRAMMING EXAMPLES - DAY 16
====================================================

This file provides practical, real-world examples of functional programming
techniques in Python to help solidify the concepts covered in the basics file.

Examples include:
- Data transformation pipelines
- Text processing with functional tools
- Functional approaches to data analysis
- Working with JSON data functionally
- Web scraping with functional programming
"""

print("PRACTICAL FUNCTIONAL PROGRAMMING EXAMPLES")
print("=" * 50)

# =====================================================
# Example 1: Data Transformation Pipeline
# =====================================================
# Building a data processing pipeline to clean and transform data
print("\nEXAMPLE 1: DATA TRANSFORMATION PIPELINE")
print("-" * 30)

# Sample data: sales records with some data quality issues
sales_data = [
    {'id': '1', 'product': 'Laptop', 'price': '999.99', 'quantity': '2', 'date': '2025-05-15'},
    {'id': '2', 'product': 'Mouse', 'price': '24.50', 'quantity': '5', 'date': '2025-05-16'},
    {'id': '3', 'product': 'Keyboard', 'price': 'unknown', 'quantity': '3', 'date': '2025-05-16'},
    {'id': '4', 'product': 'Monitor', 'price': '149.99', 'quantity': '0', 'date': '2025-05-17'},
    {'id': '5', 'product': 'Headphones', 'price': '59.99', 'quantity': '-1', 'date': 'invalid'},
    {'id': '6', 'product': 'USB Drive', 'price': '19.99', 'quantity': '10', 'date': '2025-05-18'},
]

print("Original sales data:")
for item in sales_data:
    print(f"  {item}")

# Step 1: Define transformation functions
def clean_price(record):
    """Convert price to float or set to 0.0 if invalid."""
    try:
        record['price'] = float(record['price'])
    except (ValueError, TypeError):
        record['price'] = 0.0
    return record

def clean_quantity(record):
    """Convert quantity to int and ensure it's non-negative."""
    try:
        quantity = int(record['quantity'])
        record['quantity'] = max(0, quantity)  # Ensure non-negative
    except (ValueError, TypeError):
        record['quantity'] = 0
    return record

def validate_date(record):
    """Check if the date format is valid (YYYY-MM-DD)."""
    import re
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', record['date']):
        record['date'] = 'unknown'
    return record

def calculate_total(record):
    """Add total value (price * quantity) to the record."""
    record['total'] = record['price'] * record['quantity']
    return record

def filter_valid_items(record):
    """Only include records with price > 0 and quantity > 0."""
    return record['price'] > 0 and record['quantity'] > 0

# Step 2: Apply the pipeline using functional programming
from functools import reduce

# Apply multiple transformations to each record
def process_record(record):
    """Apply all transformations to a single record."""
    # Create a copy to avoid modifying the original
    import copy
    record_copy = copy.deepcopy(record)

    # Apply transformations in sequence
    transformations = [clean_price, clean_quantity, validate_date, calculate_total]
    return reduce(lambda r, transform: transform(r), transformations, record_copy)

# Process all records and filter valid ones
processed_data = list(filter(
    filter_valid_items,
    map(process_record, sales_data)
))

print("\nProcessed and filtered sales data:")
for item in processed_data:
    print(f"  {item}")

# Step 3: Calculate summary statistics
total_revenue = sum(map(lambda x: x['total'], processed_data))
avg_price = sum(map(lambda x: x['price'], processed_data)) / len(processed_data)
total_items_sold = sum(map(lambda x: x['quantity'], processed_data))

print("\nSummary statistics:")
print(f"Total revenue: ${total_revenue:.2f}")
print(f"Average price: ${avg_price:.2f}")
print(f"Total items sold: {total_items_sold}")

# =====================================================
# Example 2: Text Processing with Functional Programming
# =====================================================
print("\nEXAMPLE 2: TEXT PROCESSING")
print("-" * 30)

# Sample text: excerpt from a famous speech
text = """
Four score and seven years ago our fathers brought forth on this continent, 
a new nation, conceived in Liberty, and dedicated to the proposition that 
all men are created equal. Now we are engaged in a great civil war, testing 
whether that nation, or any nation so conceived and so dedicated, can long 
endure. We are met on a great battle-field of that war. We have come to 
dedicate a portion of that field, as a final resting place for those who 
here gave their lives that that nation might live. It is altogether fitting 
and proper that we should do this.
"""

print(f"Original text length: {len(text)} characters")

# Text processing pipeline
import re

# Step 1: Define text processing functions
def remove_punctuation(text):
    """Remove punctuation from text."""
    return re.sub(r'[^\w\s]', '', text)

def lowercase(text):
    """Convert text to lowercase."""
    return text.lower()

def tokenize(text):
    """Split text into words."""
    return text.split()

def remove_stopwords(words):
    """Remove common English stopwords."""
    stopwords = {'a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'on', 'in',
                 'to', 'for', 'of', 'that', 'this', 'it', 'we', 'as', 'who'}
    return [word for word in words if word not in stopwords]

# Step 2: Apply text processing pipeline
processed_text = remove_stopwords(
    tokenize(
        lowercase(
            remove_punctuation(text)
        )
    )
)

print(f"Number of words after processing: {len(processed_text)}")

# Step 3: Word frequency analysis
word_freq = {}
for word in processed_text:
    word_freq[word] = word_freq.get(word, 0) + 1

# Sort words by frequency (descending)
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 most frequent words:")
for word, freq in sorted_words[:10]:
    print(f"  {word}: {freq}")

# Alternative using Counter from collections (more functional)
from collections import Counter
word_counter = Counter(processed_text)
print("\nTop 10 most frequent words (using Counter):")
for word, count in word_counter.most_common(10):
    print(f"  {word}: {count}")

# =====================================================
# Example 3: Functional Data Analysis
# =====================================================
print("\nEXAMPLE 3: FUNCTIONAL DATA ANALYSIS")
print("-" * 30)

# Sample dataset: student test scores across different subjects
students = [
    {'name': 'Alice', 'scores': {'math': 95, 'science': 88, 'history': 92, 'english': 85}},
    {'name': 'Bob', 'scores': {'math': 80, 'science': 93, 'history': 75, 'english': 82}},
    {'name': 'Charlie', 'scores': {'math': 90, 'science': 78, 'history': 85, 'english': 93}},
    {'name': 'David', 'scores': {'math': 75, 'science': 82, 'history': 79, 'english': 88}},
    {'name': 'Eva', 'scores': {'math': 88, 'science': 91, 'history': 87, 'english': 90}},
    {'name': 'Frank', 'scores': {'math': 72, 'science': 68, 'history': 80, 'english': 73}},
    {'name': 'Grace', 'scores': {'math': 93, 'science': 85, 'history': 91, 'english': 89}},
]

# Calculate average score for each student
def calculate_average(student):
    """Calculate average score across all subjects for a student."""
    scores = student['scores'].values()
    avg = sum(scores) / len(scores)
    return {'name': student['name'], 'average': avg}

student_averages = list(map(calculate_average, students))
print("Student average scores:")
for student in student_averages:
    print(f"  {student['name']}: {student['average']:.2f}")

# Find students with average >= 85 (high performers)
high_performers = list(filter(lambda s: s['average'] >= 85, student_averages))
print("\nHigh performing students:")
for student in high_performers:
    print(f"  {student['name']}: {student['average']:.2f}")

# Calculate subject averages across all students
subjects = ['math', 'science', 'history', 'english']

def get_subject_average(subject):
    """Calculate average score for a specific subject across all students."""
    scores = [student['scores'][subject] for student in students]
    return {'subject': subject, 'average': sum(scores) / len(scores)}

subject_averages = list(map(get_subject_average, subjects))
print("\nSubject averages:")
for subject in subject_averages:
    print(f"  {subject['subject']}: {subject['average']:.2f}")

# Find the highest scoring student in each subject
def get_highest_scorer(subject):
    """Find the student with the highest score in a specific subject."""
    highest_student = max(students, key=lambda s: s['scores'][subject])
    return {
        'subject': subject,
        'student': highest_student['name'],
        'score': highest_student['scores'][subject]
    }

top_performers = list(map(get_highest_scorer, subjects))
print("\nTop performer in each subject:")
for result in top_performers:
    print(f"  {result['subject']}: {result['student']} ({result['score']})")

# =====================================================
# Example 4: Working with JSON Data
# =====================================================
print("\nEXAMPLE 4: WORKING WITH JSON DATA")
print("-" * 30)

# Sample JSON-like data (list of dictionaries)
import json

# Simulated API response data
api_response = """
[
    {
        "id": 1,
        "title": "Python Programming",
        "author": "John Smith",
        "year": 2022,
        "rating": 4.7,
        "tags": ["programming", "python", "beginner"]
    },
    {
        "id": 2,
        "title": "Advanced Data Analysis",
        "author": "Jane Doe",
        "year": 2023,
        "rating": 4.9,
        "tags": ["data science", "statistics", "python", "advanced"]
    },
    {
        "id": 3,
        "title": "Web Development Basics",
        "author": "Mike Johnson",
        "year": 2021,
        "rating": 4.2,
        "tags": ["web", "html", "css", "javascript", "beginner"]
    },
    {
        "id": 4,
        "title": "Machine Learning Fundamentals",
        "author": "Sarah Williams",
        "year": 2023,
        "rating": 4.8,
        "tags": ["machine learning", "python", "data science", "intermediate"]
    },
    {
        "id": 5,
        "title": "Database Design Principles",
        "author": "Robert Brown",
        "year": 2022,
        "rating": 4.5,
        "tags": ["database", "sql", "design", "intermediate"]
    }
]
"""

# Parse JSON
books = json.loads(api_response)
print(f"Loaded {len(books)} books from JSON")

# Filter books by rating threshold
min_rating = 4.5
highly_rated_books = list(filter(lambda book: book['rating'] >= min_rating, books))
print(f"\nBooks with rating >= {min_rating}:")
for book in highly_rated_books:
    print(f"  {book['title']} by {book['author']} - {book['rating']}")

# Find all unique tags
def extract_tags(books):
    """Extract all unique tags from the book collection."""
    # Flatten list of tag lists and create a set
    all_tags = set()
    for book in books:
        all_tags.update(book['tags'])
    return all_tags

unique_tags = extract_tags(books)
print(f"\nUnique tags ({len(unique_tags)}):")
print(f"  {', '.join(sorted(unique_tags))}")

# Find books by tag using functional approach
tag_to_find = "python"
books_with_tag = list(filter(lambda book: tag_to_find in book['tags'], books))
print(f"\nBooks with tag '{tag_to_find}':")
for book in books_with_tag:
    print(f"  {book['title']} ({book['year']})")

# Get list of recent books (functional pipeline)
current_year = 2023
recent_books = list(map(
    lambda book: f"{book['title']} by {book['author']}",
    filter(lambda book: book['year'] == current_year, books)
))
print(f"\nBooks published in {current_year}:")
for title in recent_books:
    print(f"  {title}")

# Calculate average rating by publication year
from collections import defaultdict

def group_by_year(books):
    """Group books by publication year."""
    result = defaultdict(list)
    for book in books:
        result[book['year']].append(book)
    return result

books_by_year = group_by_year(books)
avg_rating_by_year = {
    year: sum(book['rating'] for book in year_books) / len(year_books)
    for year, year_books in books_by_year.items()
}

print("\nAverage rating by publication year:")
for year, avg_rating in sorted(avg_rating_by_year.items()):
    print(f"  {year}: {avg_rating:.2f}")

# =====================================================
# Example 5: Simple Web Page Analysis
# =====================================================
print("\nEXAMPLE 5: WEB PAGE ANALYSIS SIMULATION")
print("-" * 30)
print("(Note: This example simulates web content without making actual requests)")

# Simulated HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Programming Resources</title>
</head>
<body>
    <header>
        <h1>Python Programming Resources</h1>
        <nav>
            <ul>
                <li><a href="/tutorials">Tutorials</a></li>
                <li><a href="/examples">Examples</a></li>
                <li><a href="/documentation">Documentation</a></li>
                <li><a href="/community">Community</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="featured">
            <h2>Featured Tutorials</h2>
            <article>
                <h3><a href="/tutorials/beginner">Python for Beginners</a></h3>
                <p>Learn the basics of Python programming in this comprehensive guide.</p>
                <span class="tag">Beginner</span>
                <span class="tag">Fundamentals</span>
            </article>
            <article>
                <h3><a href="/tutorials/intermediate">Intermediate Python</a></h3>
                <p>Take your Python skills to the next level with these intermediate topics.</p>
                <span class="tag">Intermediate</span>
                <span class="tag">Advanced Features</span>
            </article>
            <article>
                <h3><a href="/tutorials/advanced">Advanced Python Techniques</a></h3>
                <p>Master advanced Python concepts like metaclasses, descriptors, and more.</p>
                <span class="tag">Advanced</span>
                <span class="tag">Expert</span>
            </article>
        </section>
        <section class="examples">
            <h2>Code Examples</h2>
            <ul>
                <li><a href="/examples/data-analysis">Data Analysis with Pandas</a></li>
                <li><a href="/examples/web-scraping">Web Scraping with BeautifulSoup</a></li>
                <li><a href="/examples/machine-learning">Machine Learning with scikit-learn</a></li>
                <li><a href="/examples/web-dev">Web Development with Flask</a></li>
                <li><a href="/examples/automation">Automation Scripts</a></li>
            </ul>
        </section>
    </main>
    <footer>
        <p>Copyright © 2025 Python Resources</p>
        <p>Contact: <a href="mailto:info@pythonresources.com">info@pythonresources.com</a></p>
    </footer>
</body>
</html>
"""

# Extract information from HTML using regular expressions (simulating BeautifulSoup)
import re

def extract_title(html):
    """Extract page title from HTML."""
    match = re.search(r'<title>(.*?)</title>', html)
    return match.group(1) if match else "No title found"

def extract_links(html):
    """Extract all links from HTML."""
    return re.findall(r'<a href="([^"]+)">(.*?)</a>', html)

def extract_headers(html):
    """Extract all headers (h1-h3) from HTML."""
    headers = []
    for level in range(1, 4):
        pattern = f'<h{level}>(.*?)</h{level}>'
        headers.extend([(level, text) for text in re.findall(pattern, html)])
    return headers

# Process HTML content using functional programming
title = extract_title(html_content)
all_links = extract_links(html_content)
all_headers = extract_headers(html_content)

print(f"Page title: {title}")

# Process links
print(f"\nFound {len(all_links)} links:")
for href, text in all_links[:5]:  # Show first 5 links
    print(f"  '{text}' -> {href}")

if len(all_links) > 5:
    print(f"  ... and {len(all_links) - 5} more")

# Analyze links by type/section
internal_links = list(filter(lambda link: link[0].startswith('/'), all_links))
external_links = list(filter(lambda link: not link[0].startswith('/'), all_links))

print(f"\nInternal links: {len(internal_links)}")
print(f"External links: {len(external_links)}")

# Group links by section
tutorial_links = list(filter(lambda link: 'tutorial' in link[0].lower(), all_links))
example_links = list(filter(lambda link: 'example' in link[0].lower(), all_links))

print(f"\nTutorial links: {len(tutorial_links)}")
for href, text in tutorial_links:
    print(f"  '{text}' -> {href}")

print(f"\nExample links: {len(example_links)}")
for href, text in example_links:
    print(f"  '{text}' -> {href}")

# Process headers
print("\nHeaders by level:")
for level in range(1, 4):
    headers_at_level = list(filter(lambda h: h[0] == level, all_headers))
    print(f"  H{level} ({len(headers_at_level)}): {', '.join(h[1] for h in headers_at_level)}")

print("\n" + "=" * 50)
