# 1. Programming with Python

## 1.1: Introduction to Python and Basic Concepts
*   Introduction to Python and Data Science
*   Setting up the Environment
*   Basic Operators
    *   Arithmetic Operators
    *   Operator Precedence
    *   Comparison Operators
*   Variables and Data Types
    *   Reassignment
    *   Assignment Operators
    *   Variable Naming Rules
    *   Basic Data Types
    *   Assigning Differet Data Types to Variables
    *   Type Conversion Functions
*   Strings in Detail
    *   String Concatenation
    *   String Replication
    *   Escape Characters
    *   String Indexing and Slicing
    *   String Properties
    *   String Functions
    *   String Methods
*   Basic Input and Output
    *   Output
    *   Formatting Options
    *   Input

## 1.2. Data Structures and Control Flow
*   Introduction to Data Structures
*   Lists
    *   Creating Lists
    *   List Membership
    *   Indexing and Slicing
    *   Modifying Lists
    *   List Methods
    *   Nested Lists
*   Tuples
    *   Creating Tuples
    *   When to use Tuples?
*   Logical Operators
    *   Chained Comparison Operators
*   Conditional Statements
    *   `if`, `elif`, and `else`
    *   Nested Conditional Statements
    *   Single-line Conditional Statements
    *   Match Statement
*   Loops 
    *   `for` Loops
    *   `while` Loops
    *   `break`, `continue`, `pass`
    *   Nested Loops
*   List Comprehensions
    *   The Basic Syntax
    *   Adding a Condition
    *   `if-else` in List Comprehensions
    *   Nested List Comprehensions

## 1.3. Advanced Data Structures and Functions
*   Dictionaries 
    *   Creating Dictionaries
    *   Accessing Values
    *   Modifying Dictionaries
    *   More complex Dictionaries
    *   Operations on Dictionaries
*   Sets 
    *   Creating Sets
    *   Set Operations
*   Introduction to Functions 
    *   Writing and Calling Functions
*   Function Arguments 
    *   Positional Arguments
    *   Keyword Arguments
    *   Using return statement
    *   Adding logic to functions
*   Scope of Variables 
<!-- *   Basic Data Transformation  -->

## 1.4. Advanced Functions and Functional Programming for Data Processing
*   What is Functional Programming?
*   Lambda Functions
*   `map`, `filter`, and `reduce`
    *   `map`
    *   `filter`
    *   `reduce`
*   List Comprehensions
    *   Basic Syntax
    *   Adding a Condition
    *   `if-else` in List Comprehensions
*   Dictionary and Set Comprehensions
    *   Dictionary Comprehensions
    *   Set Comprehensions
*   Error Handling (`try...except`)
    *   Basic Syntax
    *   Handling Multiple Exceptions
    *   `else` and `finally` clauses
*   Raising Exceptions (`raise`)
*   Assertions

## 1.5. Object-Oriented Programming (OOP)
*   Introduction to OOP
*   Creating Classes
    *   Defining a Class
    *   Creating an Instance (Object)
    *   A different example
*   Inheritance
*   Polymorphism
*   Encapsulation
*   Special Methods
*   Data Classes

## 1.6. Advanced Data Structures and Iterators
*   Args and Kwargs
    *   `*args`
    *   `**kwargs`
    *   Using `*args` and `**kwargs` together
*   Generators
*   Iterators
*   Decorators
*   Reading and Writing Files 
*   Introduction to Python's Standard Library 
    *   Pathlib Module
    *   Collections Module
    *   Itertools Module

<!-- ## 1.7. Working with Data and APIs
*   JSON and XML
*   Working with APIs
*   Introduction to Regular Expressions
*   Data Validation and Cleaning -->

# 2. Data Analysis and Statistics

## 2.1. Numerical Computing with NumPy
*   Introduction to NumPy
*   NumPy Arrays (ndarrays)
    *   Creating NumPy Arrays
    *   Array Attributes
*   Array Indexing and Slicing
*   Array Operations
    *   Vectorized Operations
    *   Broadcasting
*   Mathematical and Statistical Functions
*   Linear Algebra with NumPy

## 2.2. Data Manipulation with Pandas
*   Introduction to Pandas
*   Pandas Data Structures
    *   Series
    *   DataFrame
*   Reading and Writing Data (CSV, Excel, etc.)
*   Indexing and Selecting Data
    *   `loc` and `iloc`
    *   Conditional Selection
*   Data Cleaning and Preparation
    *   Handling Missing Data
    *   Handling Duplicated Data
    *   Data type conversions
    *   Outlier detection
    *   Data validation
    *   Inconsistent formatting
*   Data Transformation
    *   Aggregating and Grouping Data
    *   Merging, Joining, and Concatenating DataFrames
*   Date/Time Manipulation
    *   Time Series Basics

## 2.3. SQL for Data Analysis
*   Introduction to Relational Databases and SQL
    *   Comments
    *   Data Types
    *   Constraints
*   Basic Queries: 
    *   `SELECT` 
    *   `FROM` 
    *   `WHERE`
    *   Aliases
*   Filtering and Sorting: 
    *   `ORDER BY` 
    *   `LIMIT` 
    *   `DISTINCT`
    *   `LIKE`
    *   `AND`, `OR`, `NOT`
    *   `IN`, `NOT IN`
    *   `BETWEEN`
    *   `IS NULL`, `IS NOT NULL`
*   Row Level Operations: 
    *   String Functions
        *   `CONCAT`
        *   `UPPER`
        *   `LOWER`
        *   `TRIM`
        *   `REPLACE`
        *   `LEN`
        *   `LEFT`
        *   `RIGHT`
        *   `SUBSTRING`
    *   Numerical Functions
        *   `ABS`
        *   `CEIL`
        *   `FLOOR`
        *   `ROUND`
        *   `TRUNC`
        *   `SQRT`
        *   `POWER`
        *   `LOG`
    *   Date Functions
    *   `CASE` 
    *   `CAST`
*   Aggregate Functions: 
    *   `COUNT` 
    *   `SUM` 
    *   `AVG` 
    *   `MIN` 
    *   `MAX`
*   Grouping Data: 
    *   `GROUP BY`
    *   `HAVING`
*   Joining Multiple Tables: 
    *   Keys
    *   `INNER` 
    *   `LEFT` 
    *   `RIGHT` 
    *   `FULL OUTER JOIN`
    *   Self Joins
    *   Cross Join
    *   `UNION`, `UNION ALL`
    *   `INTERSECT`, `EXCEPT`
*   Subqueries
*   Common Table Expressions (CTEs) using `WITH`
*   Window Functions: 
    *   `ROW_NUMBER` 
    *   `RANK` 
    *   `LEAD` 
    *   `LAG`
*   Data Cleaning and Transformation: 
*   Advanced Topics:
    *   Indexes
    *   Triggers
    *   Views
    *   Stored Procedures
    *   Transactions
    *   Connectors (python)
    *   ORMs (python)

## 2.4. Visualization with Python
*   Introduction to Data Visualization
*   Matplotlib
    *   Creating Basic Plots (Line, Bar, Scatter, Histogram)
    *   Customizing Plots (Labels, Titles, Colors)
    *   Subplots
*   Seaborn
    *   Introduction to Statistical Visualization
    *   Advanced Plots (Box Plots, Violin Plots, Heatmaps)
    *   Styling and Themes
*   Plotly
*   Streamlit

## 2.5. PowerBI
*   Introduction to PowerBI
*   Data Sources
*   Data Modeling
*   Data Visualization
*   Dashboards
*   Reports

# 5. Statistics

# 6. Machine Learning
## Scikit-learn
## PyTorch