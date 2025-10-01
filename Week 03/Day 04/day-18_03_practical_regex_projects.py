"""
REGEX PRACTICAL PROJECTS AND APPLICATIONS

This module demonstrates practical applications of regular expressions through mini-projects
that showcase how regex can be used to solve real-world text processing challenges.

Key projects:
1. Text analyzer tool
2. Log file parser
3. Web scraper helper
4. Custom data validator
5. Code formatter
"""

# =====================================================
# 1. TEXT ANALYZER TOOL
# =====================================================
print("=" * 50)
print("1. TEXT ANALYZER TOOL")
print("=" * 50)

import re
import collections

def analyze_text(text):
    """Analyze text using regex patterns to extract useful information."""
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Word count (excluding punctuation)
    words = re.findall(r'\b[A-Za-z0-9\']+\b', text)
    word_count = len(words)

    # Sentence count
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Find most common words
    word_freq = collections.Counter(word.lower() for word in words)
    most_common = word_freq.most_common(5)

    # Find all email addresses
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    # Find all URLs
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w=&%+-]*)?', text)

    # Find hashtags
    hashtags = re.findall(r'#\w+', text)

    # Extract dates (multiple formats)
    dates = re.findall(r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b', text)

    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'most_common_words': most_common,
        'emails': emails,
        'urls': urls,
        'hashtags': hashtags,
        'dates': dates
    }

# Example text to analyze
sample_text = """
This is a sample text for our Text Analyzer tool. It was created on Oct 1, 2023.
You can contact us at support@example.com or visit https://example.com/contact.
Follow us on social media with hashtags #Python, #RegEx, and #DataScience.
Another meeting is scheduled for 10/15/2023. The previous meeting was on 5-5-2023.
This is a sample text. This text is just an example. Sample examples help us learn.
"""

# Run the analyzer
results = analyze_text(sample_text)

# Display results
print("\nText Analysis Results:")
print(f"Word count: {results['word_count']}")
print(f"Sentence count: {results['sentence_count']}")
print("\nMost common words:")
for word, count in results['most_common_words']:
    print(f"  {word}: {count}")
print("\nEmails found:", results['emails'])
print("URLs found:", results['urls'])
print("Hashtags found:", results['hashtags'])
print("Dates found:", results['dates'])

# =====================================================
# 2. LOG FILE PARSER
# =====================================================
print("\n" + "=" * 50)
print("2. LOG FILE PARSER")
print("=" * 50)

# Sample log entries
log_entries = [
    "192.168.1.1 - - [01/Oct/2023:10:32:15 +0000] \"GET /index.html HTTP/1.1\" 200 1234",
    "192.168.1.2 - - [01/Oct/2023:10:33:20 +0000] \"POST /submit HTTP/1.1\" 302 0",
    "192.168.1.1 - - [01/Oct/2023:10:35:08 +0000] \"GET /images/logo.png HTTP/1.1\" 404 0",
    "192.168.1.3 - - [01/Oct/2023:10:36:12 +0000] \"GET /about HTTP/1.1\" 200 5678",
    "192.168.1.4 - - [01/Oct/2023:10:40:32 +0000] \"GET /api/data HTTP/1.1\" 500 230",
    "192.168.1.1 - - [01/Oct/2023:10:41:55 +0000] \"GET /contact HTTP/1.1\" 200 3456"
]

def parse_apache_logs(logs):
    """Parse Apache-style log entries using regex."""
    # Define the regex pattern for Apache Common Log Format
    pattern = re.compile(r"""
        ^(\S+)                      # IP address
        \s+-\s+-\s+                 # Ignored fields
        \[([^\]]+)\]                # Date and time
        \s+"(\w+)\s+                # HTTP method
        ([^ ]+)\s+                  # Requested URL
        HTTP/[0-9.]+"\s+            # HTTP version
        (\d+)\s+                    # Status code
        (\d+)                       # Response size
    """, re.VERBOSE)

    parsed_logs = []

    for log in logs:
        match = pattern.search(log)
        if match:
            ip, date, method, url, status, size = match.groups()

            # Further parse the date
            date_pattern = re.compile(r'(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+)')
            date_match = date_pattern.search(date)
            if date_match:
                day, month, year, hour, minute, second = date_match.groups()

            parsed_logs.append({
                'ip': ip,
                'date': date,
                'method': method,
                'url': url,
                'status': int(status),
                'size': int(size),
                'day': day,
                'month': month,
                'year': year,
                'time': f"{hour}:{minute}:{second}"
            })

    return parsed_logs

# Parse the logs
parsed_logs = parse_apache_logs(log_entries)

# Analyze the parsed logs
def analyze_logs(logs):
    """Analyze parsed logs for useful patterns and statistics."""
    # Group by IP address
    ips = collections.Counter(log['ip'] for log in logs)

    # Group by status code
    status_codes = collections.Counter(log['status'] for log in logs)

    # Group by URL
    urls = collections.Counter(log['url'] for log in logs)

    # Find all 404 (not found) errors
    not_found = [log for log in logs if log['status'] == 404]

    # Find all 500 (server error) entries
    server_errors = [log for log in logs if log['status'] >= 500]

    return {
        'total_requests': len(logs),
        'unique_ips': len(ips),
        'ips': ips,
        'status_distribution': status_codes,
        'top_urls': urls.most_common(3),
        'not_found_errors': not_found,
        'server_errors': server_errors
    }

# Run the analysis
log_analysis = analyze_logs(parsed_logs)

# Display results
print("\nLog Analysis Results:")
print(f"Total requests: {log_analysis['total_requests']}")
print(f"Unique IP addresses: {log_analysis['unique_ips']}")
print("\nRequests by IP:")
for ip, count in log_analysis['ips'].items():
    print(f"  {ip}: {count}")
print("\nStatus code distribution:")
for status, count in log_analysis['status_distribution'].items():
    print(f"  {status}: {count}")
print("\nTop requested URLs:")
for url, count in log_analysis['top_urls']:
    print(f"  {url}: {count}")
print("\nNot found errors (404):")
for error in log_analysis['not_found_errors']:
    print(f"  {error['url']} requested by {error['ip']}")
print("\nServer errors (5xx):")
for error in log_analysis['server_errors']:
    print(f"  {error['url']} returned {error['status']} to {error['ip']}")

# =====================================================
# 3. WEB SCRAPER HELPER
# =====================================================
print("\n" + "=" * 50)
print("3. WEB SCRAPER HELPER")
print("=" * 50)

# Sample HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
    <meta name="description" content="A sample website for regex practice">
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/products">Products</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="featured">
            <h2>Featured Products</h2>
            <div class="product" id="prod-1">
                <h3>Premium Widget</h3>
                <p>Price: $99.99</p>
                <p>Rating: 4.5/5</p>
            </div>
            <div class="product" id="prod-2">
                <h3>Deluxe Gadget</h3>
                <p>Price: $149.99</p>
                <p>Rating: 4.8/5</p>
            </div>
        </section>
        <section class="testimonials">
            <h2>Customer Testimonials</h2>
            <blockquote>
                <p>This product changed my life!</p>
                <cite>John Smith</cite>
            </blockquote>
            <blockquote>
                <p>Best purchase I've ever made.</p>
                <cite>Jane Doe</cite>
            </blockquote>
        </section>
    </main>
    <footer>
        <p>Contact us at: <a href="mailto:info@example.com">info@example.com</a></p>
        <p>© 2023 Sample Company</p>
    </footer>
</body>
</html>
"""

def extract_from_html(html):
    """Extract useful information from HTML using regex."""
    results = {}

    # Extract the title
    title_match = re.search(r'<title>(.*?)</title>', html)
    results['title'] = title_match.group(1) if title_match else "No title found"

    # Extract meta description
    desc_match = re.search(r'<meta name="description" content="(.*?)"', html)
    results['description'] = desc_match.group(1) if desc_match else "No description found"

    # Extract all links
    results['links'] = re.findall(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', html)

    # Extract headings
    results['h1'] = re.findall(r'<h1>(.*?)</h1>', html)
    results['h2'] = re.findall(r'<h2>(.*?)</h2>', html)

    # Extract product information
    products = []
    product_sections = re.finditer(r'<div class="product"[^>]*>(.*?)</div>', html, re.DOTALL)
    for prod_match in product_sections:
        prod_html = prod_match.group(1)

        # Extract product name
        name_match = re.search(r'<h3>(.*?)</h3>', prod_html)
        name = name_match.group(1) if name_match else "Unknown"

        # Extract price
        price_match = re.search(r'Price:\s+\$([\d.]+)', prod_html)
        price = price_match.group(1) if price_match else "Unknown"

        # Extract rating
        rating_match = re.search(r'Rating:\s+([\d.]+)/5', prod_html)
        rating = rating_match.group(1) if rating_match else "Unknown"

        products.append({
            'name': name,
            'price': price,
            'rating': rating
        })

    results['products'] = products

    # Extract testimonials
    testimonials = []
    testimonial_blocks = re.finditer(r'<blockquote>(.*?)</blockquote>', html, re.DOTALL)
    for block_match in testimonial_blocks:
        block_html = block_match.group(1)

        # Extract testimonial text
        text_match = re.search(r'<p>(.*?)</p>', block_html)
        text = text_match.group(1) if text_match else ""

        # Extract author
        author_match = re.search(r'<cite>(.*?)</cite>', block_html)
        author = author_match.group(1) if author_match else "Anonymous"

        testimonials.append({
            'text': text,
            'author': author
        })

    results['testimonials'] = testimonials

    return results

# Extract data from HTML
extracted_data = extract_from_html(html_content)

# Display results
print("\nExtracted HTML Data:")
print(f"Title: {extracted_data['title']}")
print(f"Description: {extracted_data['description']}")
print("\nHeadings:")
print(f"H1: {extracted_data['h1']}")
print(f"H2: {extracted_data['h2']}")

print("\nLinks:")
for href, text in extracted_data['links']:
    print(f"  {text} -> {href}")

print("\nProducts:")
for product in extracted_data['products']:
    print(f"  {product['name']} - ${product['price']} - Rating: {product['rating']}/5")

print("\nTestimonials:")
for testimonial in extracted_data['testimonials']:
    print(f"  \"{testimonial['text']}\" - {testimonial['author']}")

print("\nWarning: Regular expressions have limitations for parsing HTML. For production code,")
print("consider using dedicated HTML parsing libraries like BeautifulSoup or lxml.")

# =====================================================
# 4. CUSTOM DATA VALIDATOR
# =====================================================
print("\n" + "=" * 50)
print("4. CUSTOM DATA VALIDATOR")
print("=" * 50)

def create_validator(pattern, error_message, transform_func=None):
    """Create a custom validator function based on regex pattern."""
    compiled_pattern = re.compile(pattern)

    def validator(value):
        if not value:
            return False, "Value cannot be empty"

        if compiled_pattern.fullmatch(value):
            if transform_func:
                transformed = transform_func(value)
                return True, transformed
            return True, value
        return False, error_message

    return validator

# Create various validators
validators = {
    'email': create_validator(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        "Invalid email format"
    ),
    'phone': create_validator(
        r'^(\+\d{1,3})?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
        "Invalid phone number format",
        lambda x: re.sub(r'[^\d+]', '', x)  # Normalize by removing non-digits
    ),
    'username': create_validator(
        r'^[a-zA-Z][a-zA-Z0-9_]{3,15}$',
        "Username must start with a letter and be 4-16 characters long"
    ),
    'password': create_validator(
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()-_=+]).{8,}$',
        "Password must have at least 8 characters with uppercase, lowercase, digit, and special char"
    ),
    'date': create_validator(
        r'^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(19|20)\d{2}$',
        "Date must be in format MM/DD/YYYY",
        lambda x: x  # Could convert to Date object in a real application
    ),
    'zipcode': create_validator(
        r'^\d{5}(-\d{4})?$',
        "Invalid US ZIP code format"
    ),
    'credit_card': create_validator(
        r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})$',
        "Invalid credit card number",
        lambda x: x[-4:].rjust(len(x), '*')  # Mask all but last 4 digits
    )
}

# Sample data for validation
data_to_validate = {
    'email': ['user@example.com', 'invalid.email', 'missing@domain.', '@nodomain.com'],
    'phone': ['(123) 456-7890', '123.456.7890', '123-456-7890', '12345'],
    'username': ['user123', '123user', 'ab', 'valid_username', 'too_long_username12345'],
    'password': ['weak', 'Stronger1', 'Strong!1', 'nodigit!A', 'NOLOWER123!'],
    'date': ['01/01/2023', '13/01/2023', '01/32/2023', '01/01/23'],
    'zipcode': ['12345', '12345-6789', '1234', '123456'],
    'credit_card': ['4111111111111111', '5555555555554444', '1234567812345678', '41111']
}

# Validate the data
print("\nValidation Results:")
for field, values in data_to_validate.items():
    print(f"\n{field.upper()} VALIDATION:")
    for value in values:
        is_valid, result = validators[field](value)
        print(f"  '{value}': {'✓ Valid' if is_valid else '✗ Invalid'}, Result: {result}")

# =====================================================
# 5. CODE FORMATTER/ANALYZER
# =====================================================
print("\n" + "=" * 50)
print("5. CODE FORMATTER/ANALYZER")
print("=" * 50)

# Sample Python code for analysis
python_code = """
def calculate_total(items):
    total=0  # Initialize total
    for item in items:
        total+=item['price']*item['quantity']    # Calculate item total
    
    # Apply tax
    tax_rate = 0.08
    total = total * (1 + tax_rate)
    
    return total

# Test function
items = [
    {'name': 'Widget', 'price': 9.99, 'quantity': 3},
    {'name': 'Gadget', 'price': 15.99, 'quantity': 1}
]
grand_total = calculate_total(items)
print(f"Grand total: ${grand_total:.2f}")
"""

def analyze_python_code(code):
    """Analyze Python code using regex to find potential issues and metrics."""
    results = {}

    # Normalize line endings
    code = code.replace('\r\n', '\n')

    # Count lines of code (excluding empty lines)
    lines = code.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    results['total_lines'] = len(lines)
    results['code_lines'] = len(non_empty_lines)

    # Count functions
    function_defs = re.findall(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code)
    results['functions'] = function_defs
    results['function_count'] = len(function_defs)

    # Find potential style issues
    style_issues = []

    # No space around operators
    operator_issues = re.findall(r'[a-zA-Z0-9_]([-+*/=])[a-zA-Z0-9_]', code)
    if operator_issues:
        style_issues.append(f"Missing spaces around operators: {operator_issues}")

    # Trailing whitespace
    trailing_spaces = re.findall(r'[ \t]+$', code, re.MULTILINE)
    if trailing_spaces:
        style_issues.append(f"Found {len(trailing_spaces)} lines with trailing whitespace")

    # Too many blank lines
    too_many_blanks = re.findall(r'\n{4,}', code)
    if too_many_blanks:
        style_issues.append(f"Found {len(too_many_blanks)} instances of 3+ consecutive blank lines")

    # Line too long (>79 characters)
    long_lines = [line for line in lines if len(line) > 79]
    if long_lines:
        style_issues.append(f"Found {len(long_lines)} lines longer than 79 characters")

    results['style_issues'] = style_issues

    # Find TODO comments
    todos = re.findall(r'#\s*TODO:?\s*(.*?)$', code, re.MULTILINE | re.IGNORECASE)
    results['todos'] = todos

    # Find potential variable naming issues
    bad_names = re.findall(r'\b(i|j|k|x|y|z|a|b|c|foo|bar|baz)\b\s*=', code)
    if bad_names:
        results['naming_issues'] = f"Potentially non-descriptive variable names: {set(bad_names)}"

    # Format code
    formatted_code = code

    # Add spaces around operators
    formatted_code = re.sub(r'([a-zA-Z0-9_])([+\-*/=])([a-zA-Z0-9_])', r'\1 \2 \3', formatted_code)

    # Remove trailing whitespace
    formatted_code = re.sub(r'[ \t]+$', '', formatted_code, flags=re.MULTILINE)

    # Limit consecutive blank lines to 2
    formatted_code = re.sub(r'\n{3,}', '\n\n', formatted_code)

    results['formatted_code'] = formatted_code

    return results

# Analyze the code
code_analysis = analyze_python_code(python_code)

# Display results
print("\nCode Analysis Results:")
print(f"Total lines: {code_analysis['total_lines']}")
print(f"Code lines (non-empty): {code_analysis['code_lines']}")
print(f"Functions: {code_analysis['functions']} (count: {code_analysis['function_count']})")

print("\nStyle Issues:")
if code_analysis['style_issues']:
    for issue in code_analysis['style_issues']:
        print(f"- {issue}")
else:
    print("- No style issues found")

print("\nTODOs:")
if code_analysis.get('todos'):
    for todo in code_analysis['todos']:
        print(f"- TODO: {todo}")
else:
    print("- No TODOs found")

if code_analysis.get('naming_issues'):
    print(f"\n{code_analysis['naming_issues']}")

print("\nOriginal vs. Formatted Code:")
print("\n--- Original Code ---")
print(python_code)
print("\n--- Formatted Code ---")
print(code_analysis['formatted_code'])

# =====================================================
# SUMMARY
# =====================================================
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

"""
Practical Regular Expression Applications:

1. Text Analyzer Tool:
   - Extract metadata from text (word count, entities, etc.)
   - Use Counter to find patterns and frequencies
   - Combine multiple regex patterns for comprehensive analysis

2. Log File Parser:
   - Extract structured data from semi-structured logs
   - Use capturing groups to isolate important components
   - Analyze patterns across multiple log entries

3. Web Scraper Helper:
   - Extract content from HTML markup
   - Use regex with caution for HTML parsing
   - Know when to switch to dedicated parsing libraries

4. Custom Data Validator:
   - Create reusable validation functions with descriptive errors
   - Use regex for data format validation
   - Transform and normalize data during validation

5. Code Formatter/Analyzer:
   - Identify style issues in code
   - Use regex to improve code formatting
   - Extract metrics and patterns from codebases

Key Takeaways:
- Regular expressions are extremely powerful for text processing tasks
- Combining regex with Python's standard libraries creates robust tools
- For production use, consider performance and maintainability
- Know the limitations of regex (e.g., HTML parsing, recursion)
- Practice and testing are essential for mastering complex patterns
"""

# Next steps for learning:
# - Explore regex engines differences between languages
# - Study performance optimization for large-scale text processing
# - Learn advanced techniques like recursive patterns
# - Practice with more complex real-world data sources
