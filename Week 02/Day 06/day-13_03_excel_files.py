"""
======================================================
Python Learning - Week 02 Day 06 (Day 13 Overall)
TOPIC: WORKING WITH EXCEL FILES
======================================================

DESCRIPTION:
This file demonstrates how to work with Excel files in Python using
the pandas library with openpyxl as the backend. Excel files are
commonly used in business environments, and Python provides powerful
tools for reading, writing, and manipulating Excel data.

TOPICS COVERED:
1. Creating Excel files with pandas
2. Reading Excel files
3. Working with multiple sheets
4. Formatting and styling Excel files

LEARNING OUTCOMES:
- Read and write Excel files using pandas
- Work with multiple sheets in a workbook
- Apply basic formatting to Excel files
- Handle Excel data efficiently

Note: This module requires the pandas and openpyxl libraries.
      Install with: pip install pandas openpyxl

======================================================
"""

import os
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
# 1) Creating Excel Files with Pandas
# ======================================================
"""
Pandas provides a convenient interface for creating Excel files
through its DataFrame object and to_excel method.
"""
print("\n" + "="*50)
print("1. CREATING EXCEL FILES WITH PANDAS")
print("="*50)

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Pandas library not available. Excel operations will be skipped.")
    print("To install pandas: pip install pandas openpyxl")
    print("Openpyxl is used by pandas as the Excel engine.")

if PANDAS_AVAILABLE:
    # Create a simple DataFrame
    print("Creating a pandas DataFrame:")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 32, 18, 47, 22],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston'],
        'Salary': [75000, 82000, 45000, 98000, 65000]
    }
    df = pd.DataFrame(data)
    print(df)

    # Write to Excel file
    excel_file = EXAMPLE_DIR / "employee_data.xlsx"
    df.to_excel(excel_file, sheet_name='Employees', index=False)
    print(f"\nDataFrame written to Excel file: {excel_file}")

    print("\nKey parameters for to_excel():")
    print("- sheet_name: Name of the sheet (default is 'Sheet1')")
    print("- index: Whether to write row names (default True)")
    print("- header: Whether to write column names (default True)")
    print("- startrow/startcol: Where to start writing data")
    print("- engine: Excel engine to use ('openpyxl', 'xlsxwriter')")
else:
    print("\nSkipping Excel creation example due to missing pandas library.")


# ======================================================
# 2) Reading Excel Files
# ======================================================
"""
Pandas makes it easy to read Excel files into DataFrames, which
provides powerful data manipulation capabilities.
"""
print("\n" + "="*50)
print("2. READING EXCEL FILES")
print("="*50)

if PANDAS_AVAILABLE and os.path.exists(EXAMPLE_DIR / "employee_data.xlsx"):
    # Read the Excel file we just created
    print("Reading Excel file into DataFrame:")
    read_df = pd.read_excel(EXAMPLE_DIR / "employee_data.xlsx")
    print(read_df)

    # Display information about the DataFrame
    print("\nDataFrame information:")
    print(f"Shape: {read_df.shape} (rows, columns)")
    print(f"Column names: {read_df.columns.tolist()}")
    print(f"Data types:\n{read_df.dtypes}")

    # Basic data analysis
    print("\nBasic data analysis:")
    print(f"Average age: {read_df['Age'].mean():.1f} years")
    print(f"Salary statistics:\n{read_df['Salary'].describe()}")

    # Filtering data
    print("\nFiltering data (employees younger than 30):")
    young_employees = read_df[read_df['Age'] < 30]
    print(young_employees)

    print("\nKey parameters for read_excel():")
    print("- sheet_name: Sheet to read (name, index, or list of these)")
    print("- header: Row to use as column names")
    print("- skiprows: Number of rows to skip at the start")
    print("- usecols: Columns to read (e.g., 'A:C' or [0, 1, 2])")
    print("- nrows: Number of rows to read")
else:
    print("\nSkipping Excel reading example due to missing file or pandas library.")


# ======================================================
# 3) Working with Multiple Sheets
# ======================================================
"""
Excel workbooks often contain multiple sheets. Pandas allows you to
work with multiple sheets in a single workbook.
"""
print("\n" + "="*50)
print("3. WORKING WITH MULTIPLE SHEETS")
print("="*50)

if PANDAS_AVAILABLE:
    # Create a multi-sheet Excel file
    multi_sheet_excel = EXAMPLE_DIR / "multi_sheet_data.xlsx"

    # Create a writer object to write multiple sheets
    with pd.ExcelWriter(multi_sheet_excel) as writer:
        # Employees sheet (reusing data from earlier)
        df.to_excel(writer, sheet_name='Employees', index=False)

        # Departments sheet
        departments = pd.DataFrame({
            'Department': ['HR', 'Engineering', 'Marketing', 'Finance'],
            'Manager': ['Alice', 'David', 'Eva', 'Bob'],
            'Budget': [150000, 500000, 300000, 1000000]
        })
        departments.to_excel(writer, sheet_name='Departments', index=False)

        # Projects sheet
        projects = pd.DataFrame({
            'Project': ['Website Redesign', 'Mobile App', 'Data Migration'],
            'Lead': ['Charlie', 'David', 'Bob'],
            'Deadline': ['2025-10-15', '2025-11-30', '2025-09-01']
        })
        projects.to_excel(writer, sheet_name='Projects', index=False)

    print(f"Created multi-sheet Excel file at {multi_sheet_excel}")

    # Reading specific sheets
    print("\nReading specific sheets:")
    departments_df = pd.read_excel(multi_sheet_excel, sheet_name='Departments')
    print("Departments sheet:")
    print(departments_df)

    # Reading all sheets at once
    print("\nReading all sheets at once:")
    all_sheets = pd.read_excel(multi_sheet_excel, sheet_name=None)  # Returns a dict of DataFrames
    for sheet_name, sheet_data in all_sheets.items():
        print(f"\nSheet: {sheet_name}")
        print(sheet_data)

    # Sheet information
    print("\nGetting sheet names without loading data:")
    import openpyxl
    wb = openpyxl.load_workbook(multi_sheet_excel)
    print(f"Sheet names: {wb.sheetnames}")
else:
    print("\nSkipping multi-sheet Excel example due to missing pandas library.")


# ======================================================
# 4) Formatting and Styling Excel Files
# ======================================================
"""
For more advanced formatting, you can use the XlsxWriter engine
with pandas, or use openpyxl directly for even more control.
"""
print("\n" + "="*50)
print("4. FORMATTING AND STYLING EXCEL FILES")
print("="*50)

if PANDAS_AVAILABLE:
    try:
        # Check if XlsxWriter is available
        import xlsxwriter
        XLSXWRITER_AVAILABLE = True
    except ImportError:
        XLSXWRITER_AVAILABLE = False
        print("XlsxWriter library not available for advanced formatting.")
        print("To install: pip install xlsxwriter")

    if XLSXWRITER_AVAILABLE:
        # Create a styled Excel file
        styled_excel = EXAMPLE_DIR / "styled_excel.xlsx"

        # Sample sales data
        sales_data = {
            'Region': ['North', 'South', 'East', 'West', 'Central'],
            'Q1': [10000, 12000, 8000, 15000, 9000],
            'Q2': [12000, 13000, 9000, 14000, 8000],
            'Q3': [15000, 14000, 10000, 13000, 9000],
            'Q4': [18000, 16000, 12000, 15000, 10000]
        }
        sales_df = pd.DataFrame(sales_data)

        # Add totals row and column
        sales_df['Total'] = sales_df[['Q1', 'Q2', 'Q3', 'Q4']].sum(axis=1)
        totals = sales_df[['Q1', 'Q2', 'Q3', 'Q4', 'Total']].sum().tolist()
        totals.insert(0, 'Total')
        sales_df.loc[len(sales_df)] = totals

        print("Sales data with totals:")
        print(sales_df)

        # Create a Pandas Excel writer using XlsxWriter as the engine
        with pd.ExcelWriter(styled_excel, engine='xlsxwriter') as writer:
            # Write the DataFrame to an Excel sheet
            sales_df.to_excel(writer, sheet_name='Sales', index=False)

            # Get the workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Sales']

            # Define formats
            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'fg_color': '#D7E4BC',
                'border': 1
            })

            total_format = workbook.add_format({
                'bold': True,
                'fg_color': '#FFD700',
                'border': 1
            })

            currency_format = workbook.add_format({
                'num_format': '$#,##0',
                'border': 1
            })

            # Apply formats
            for col_num, col_name in enumerate(sales_df.columns):
                worksheet.write(0, col_num, col_name, header_format)

            # Format totals row and column
            for col in range(1, len(sales_df.columns)):
                for row in range(1, len(sales_df)):
                    worksheet.write(row, col, sales_df.iloc[row-1, col], currency_format)

            # Format total row
            last_row = len(sales_df)
            for col in range(len(sales_df.columns)):
                worksheet.write(last_row, col, sales_df.iloc[last_row-1, col], total_format)

            # Format total column
            last_col = len(sales_df.columns) - 1
            for row in range(1, last_row + 1):
                worksheet.write(row, last_col, sales_df.iloc[row-1, last_col], total_format)

            # Add a chart
            chart = workbook.add_chart({'type': 'column'})

            # Configure the series for the first 5 rows (excluding totals)
            for i in range(1, 5):  # Q1 to Q4
                chart.add_series({
                    'name': [f'Sales', 0, i],
                    'categories': [f'Sales', 1, 0, 5, 0],  # Region names
                    'values': [f'Sales', 1, i, 5, i],
                    'data_labels': {'value': True}
                })

            # Add chart title and labels
            chart.set_title({'name': 'Quarterly Sales by Region'})
            chart.set_x_axis({'name': 'Region'})
            chart.set_y_axis({'name': 'Sales ($)'})

            # Insert the chart into the worksheet
            worksheet.insert_chart('H2', chart, {'x_scale': 1.5, 'y_scale': 1.5})

            # Auto-fit columns
            worksheet.set_column(0, 0, 10)  # Region column
            worksheet.set_column(1, 5, 12)  # Data columns

        print(f"\nCreated styled Excel file with chart at {styled_excel}")
    else:
        print("\nSkipping styled Excel example due to missing XlsxWriter library.")

    print("\nOther Excel formatting options:")
    print("- Direct use of openpyxl for maximum formatting control")
    print("- Conditional formatting for dynamic styling")
    print("- Cell merging for complex layouts")
    print("- Custom formulas for dynamic calculations")
    print("- Data validation for controlled input")
else:
    print("\nSkipping Excel formatting example due to missing pandas library.")


print("\n" + "="*50)
print("SUMMARY OF WORKING WITH EXCEL FILES")
print("="*50)

print("""
Key takeaways from this module:

1. Pandas provides a powerful interface for working with Excel files
   through its DataFrame object and excel I/O methods.

2. Reading Excel files into DataFrames allows you to leverage pandas'
   data manipulation capabilities on Excel data.

3. Multiple sheets can be handled in a single workbook, enabling
   complex data organization similar to traditional Excel usage.

4. Advanced formatting and styling can be applied using XlsxWriter
   or openpyxl for professional-looking reports and dashboards.

Note that working with Excel files in Python requires additional
libraries like pandas, openpyxl or xlsxwriter that need to be installed
separately from the standard library.
""")
