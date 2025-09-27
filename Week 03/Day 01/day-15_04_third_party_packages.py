"""
===============================================================================
PYTHON THIRD-PARTY PACKAGES
===============================================================================

While Python's standard library is extensive, the Python ecosystem includes thousands
of third-party packages that extend Python's functionality for specialized tasks.
These packages are developed by the community and can be installed and managed using tools
like pip, the Python Package Installer.

IN THIS LESSON:
  1. Introduction to PyPI (Python Package Index)
  2. Installing packages with pip
  3. Managing packages with virtual environments
  4. Creating and using requirements files
  5. Building and sharing your own packages

===============================================================================
"""

#==============================================================================
# 1. INTRODUCTION TO PyPI
#==============================================================================
"""
PyPI (Python Package Index) is the official repository for third-party Python packages.
It hosts over 400,000 projects and is the main source for downloading Python packages.

Website: https://pypi.org/
"""

print("=" * 50)
print("PYTHON PACKAGE INDEX (PyPI)")
print("=" * 50)

print("PyPI is to Python what npm is to JavaScript or Maven is to Java.")
print("It hosts thousands of packages for various purposes, including:")
print("- Data science: pandas, numpy, scipy, matplotlib")
print("- Web development: Django, Flask, FastAPI")
print("- Machine learning: TensorFlow, PyTorch, scikit-learn")
print("- Automation: Selenium, BeautifulSoup, Scrapy")
print("- And many more specialized domains")

print("\n" + "=" * 50)
print("INSTALLING PACKAGES WITH PIP")
print("=" * 50)

#==============================================================================
# 2. INSTALLING PACKAGES WITH PIP
#==============================================================================
"""
pip is the package installer for Python. It comes pre-installed with Python 3.4+ and
allows you to install and manage additional packages that aren't in the standard library.
"""

print("Basic pip commands:")
print("- pip install package_name")
print("- pip install package_name==1.2.3  # Install specific version")
print("- pip install 'package_name>=1.2.3'  # Install minimum version")
print("- pip install package_name1 package_name2  # Install multiple packages")
print("- pip uninstall package_name")
print("- pip list  # List installed packages")
print("- pip show package_name  # Show information about a package")
print("- pip search query  # Search for packages (Note: may be disabled)")

print("\nExample of installing a popular package:")
print("pip install requests")
print("""
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
""")

print("\nInstalling specific versions:")
print("pip install requests==2.25.1  # Exact version")
print("pip install 'requests>=2.25.1'  # Minimum version")
print("pip install 'requests>=2.25.1,<2.26.0'  # Version range")

print("\nUpgrading packages:")
print("pip install --upgrade requests")
print("pip install -U requests  # Shorthand")

print("\n" + "=" * 50)
print("MANAGING VIRTUAL ENVIRONMENTS")
print("=" * 50)

#==============================================================================
# 3. MANAGING VIRTUAL ENVIRONMENTS
#==============================================================================
"""
Virtual environments are isolated Python environments that allow you to install packages
for a specific project without affecting other projects or the system-wide Python installation.
"""

print("Why use virtual environments:")
print("1. Isolate dependencies between projects")
print("2. Avoid version conflicts between packages")
print("3. Ensure reproducibility of your project")
print("4. Make it easy to share project requirements")

print("\nCreating and using virtual environments with venv:")
print("# Create a virtual environment")
print("python -m venv myenv")
print("")
print("# Activate the virtual environment")
print("# On Windows:")
print("myenv\\Scripts\\activate")
print("# On macOS/Linux:")
print("source myenv/bin/activate")
print("")
print("# Install packages in the virtual environment")
print("pip install requests")
print("")
print("# Deactivate when done")
print("deactivate")

print("\nPopular virtual environment tools:")
print("1. venv - built into Python 3.3+ (recommended)")
print("2. virtualenv - works with older Python versions")
print("3. conda - popular in data science, manages non-Python dependencies too")
print("4. pipenv - combines pip and virtualenv functionality")
print("5. poetry - modern dependency management and packaging")

print("\n" + "=" * 50)
print("REQUIREMENTS FILES")
print("=" * 50)

#==============================================================================
# 4. CREATING AND USING REQUIREMENTS FILES
#==============================================================================
"""
Requirements files list all the dependencies for a project, making it easy to recreate
the environment on another machine or share with collaborators.
"""

print("Creating a requirements file:")
print("pip freeze > requirements.txt")

print("\nExample requirements.txt file:")
print("""
requests==2.28.1
numpy==1.23.3
pandas==1.4.4
matplotlib==3.6.0
""")

print("\nInstalling from a requirements file:")
print("pip install -r requirements.txt")

print("\nPinning vs. Flexible Requirements:")
print("# Pinned (exact versions):")
print("requests==2.28.1")
print("")
print("# Flexible (minimum versions):")
print("requests>=2.28.1")
print("")
print("# Constrained (version range):")
print("requests>=2.28.1,<2.29.0")

print("\nBest practices for requirements files:")
print("1. Pin versions for reproducible builds")
print("2. Keep development and production requirements separate")
print("3. Include comments for clarity")
print("4. Group related packages together")
print("5. Regularly update dependencies for security")

print("\n" + "=" * 50)
print("BUILDING AND SHARING YOUR OWN PACKAGES")
print("=" * 50)

#==============================================================================
# 5. BUILDING AND SHARING YOUR OWN PACKAGES
#==============================================================================
"""
Once you've created useful modules, you might want to share them with others
by packaging them and uploading to PyPI.
"""

print("Basic structure of a Python package for distribution:")
print("""
mypackage/
    |-- setup.py              # Package metadata and dependencies
    |-- README.md             # Documentation
    |-- LICENSE               # License information
    `-- mypackage/
        |-- __init__.py       # Makes it a package
        |-- module1.py        # Your code
        `-- module2.py        # More code
""")

print("\nSimple setup.py example:")
print("""
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.20.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of the package",
    keywords="sample, setuptools, development",
    url="https://github.com/yourusername/mypackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
""")

print("\nBuilding and uploading to PyPI:")
print("# Install build tools")
print("pip install setuptools wheel twine")
print("")
print("# Build the package")
print("python setup.py sdist bdist_wheel")
print("")
print("# Upload to PyPI")
print("twine upload dist/*")

print("\nModern Python packaging with pyproject.toml:")
print("""
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
description = "A short description of the package"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.20.0",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/mypackage"
"Bug Tracker" = "https://github.com/yourusername/mypackage/issues"
""")

print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)

"""
KEY TAKEAWAYS:

1. PyPI hosts thousands of third-party packages that extend Python's capabilities
2. pip is the standard tool for installing and managing Python packages
3. Virtual environments isolate project dependencies for better maintainability
4. Requirements files ensure reproducible environments across different systems
5. You can build and share your own packages through PyPI
6. Modern Python packaging uses pyproject.toml for configuration

With these tools, you can leverage the vast Python ecosystem to build powerful applications
without reinventing the wheel.
"""
