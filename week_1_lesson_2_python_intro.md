# Week 1: Introduction to Python and Basic Concepts

## Setting up the Environment

### Using Conda Environments in VS Code

Visual Studio Code has excellent integration with Python and Conda.

1.  **Open your project folder** in VS Code.
2.  **Select the Python interpreter:** Open the Command Palette (`Ctrl+Shift+P`) and search for `Python: Select Interpreter`. You should see your `ds_env` conda environment in the list. Select it.
3.  **Create a new Jupyter Notebook:** You can now create a `.ipynb` file in VS Code. When you run a cell for the first time, VS Code will use the selected interpreter (`ds_env`) and its packages.

### Navigating Jupyter Notebooks

Jupyter Notebooks are interactive documents that allow you to write and run code, add explanatory text, and create visualizations all in one place.

*   **Launch:** Open your terminal (or Anaconda Prompt on Windows) and type:
    ```bash
    jupyter notebook
    ```
*   **Interface:** Your web browser will open the Jupyter dashboard, showing files in the current directory.
*   **Create a Notebook:** Click "New" in the top-right corner and select "Python 3" (or similar).
*   **Cells:** Notebooks are composed of cells.
    *   **Code Cells:** Where you write and execute Python code.
    *   **Markdown Cells:** Where you can write formatted text, like this document.
*   **Run a Cell:** To execute a cell, select it and press `Shift + Enter`.

#### Modes and Shortcuts

Jupyter has two main modes:

*   **Command Mode (blue cell border):** Press `Esc` to enter. Allows you to edit the notebook as a whole, but not type in individual cells.
*   **Edit Mode (green cell border):** Press `Enter` to enter. Allows you to type code or text into a cell.

Here are some essential shortcuts:

| Shortcut              | Action (in Command Mode)                                  |
| :-------------------- | :-------------------------------------------------------- |
| `A`                   | Insert a new cell above the current cell.                 |
| `B`                   | Insert a new cell below the current cell.                 |
| `M`                   | Change the current cell to a Markdown cell.               |
| `Y`                   | Change the current cell to a Code cell.                   |
| `D`, `D` (press twice)  | Delete the current cell.                                  |
| `Z`                   | Undo the last cell deletion.                              |
| `Shift + Up/Down`     | Select multiple cells.                                    |
| `Ctrl + Enter`        | Run the selected cell(s).                                 |
| `Shift + Enter`       | Run the current cell and select the one below.            |
| `Alt + Enter`         | Run the current cell and insert a new one below.          |

## First Python Program

The "Hello, World!" program is a tradition in programming. It's a simple program that outputs "Hello, World!".

In a code cell in your Jupyter Notebook, type the following and run it:

```python
print("Hello, World!")
```

The `print()` function is a built-in Python function that displays the specified message to the screen.

## Variables and Data Types

Variables are containers for storing data values.

### Variable Naming Rules

When naming variables in Python, you must follow these rules:

*   A variable name must start with a letter or the underscore character (`_`).
*   A variable name cannot start with a number.
*   A variable name can only contain alpha-numeric characters and underscores (`A-z`, `0-9`, and `_`).
*   Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables).
*   Avoid using Python keywords (like `if`, `for`, `while`, `str`, `int`) as variable names.

**Good Examples:**
```python
my_variable = 10
user_name = "JohnDoe"
_value = 42
```

**Bad Examples:**
```python
2nd_variable = 5  # Cannot start with a number
my-variable = 20  # Cannot contain hyphens
for = "loop"      # "for" is a keyword
```

*   **Integer (`int`):** Whole numbers.
    ```python
    age = 25
    ```
*   **Float (`float`):** Numbers with a decimal point.
    ```python
    price = 19.99
    ```
*   **String (`str`):** A sequence of characters, enclosed in single (`'`) or double (`"`) quotes.
    ```python
    name = "Alice"
    ```
*   **Boolean (`bool`):** Represents one of two values: `True` or `False`.
    ```python
    is_student = True
    ```

You can find out the data type of a variable using the `type()` function:
```python
print(type(name))
# Output: <class 'str'>
```

### The Importance of Data Types: `1` vs `"1"`

It's crucial to understand that Python treats data of different types differently, even if they look similar to us.

*   **Number vs. Text:** The integer `1` is a number that you can perform mathematical calculations on. The string `"1"` is a piece of text, a single character.

    ```python
    # Mathematical addition
    print(1 + 1)
    # Output: 2

    # String concatenation
    print("1" + "1")
    # Output: "11"
    ```
    Trying to perform math with a string will result in an error: `1 + "1"` would crash your program.

*   **Boolean vs. Text:** Similarly, `True` is a special boolean value representing truth. `"True"` is just a four-character string.

    ```python
    if True:
        print("This will always run.")

    # This also runs, but for a different reason!
    # Any non-empty string is considered "truthy" in Python.
    if "True":
        print("This runs because the string is not empty.")
    ```

**Why does this matter?**

Data types tell the computer what kind of data it is working with and what operations are allowed. By enforcing these rules, Python helps prevent errors and ensures that our code behaves predictably. Using the correct data type is fundamental to writing correct and efficient programs.

### Summary of Basic Data Types

| Data Type | Description                   | Example              | Key Characteristics                                    |
| :-------- | :---------------------------- | :------------------- | :----------------------------------------------------- |
| `int`     | Integer numbers               | `age = 25`           | Whole numbers, positive or negative, without decimals. |
| `float`   | Floating-point numbers        | `price = 19.99`      | Numbers with a decimal point.                          |
| `str`     | String (sequence of characters) | `name = "Alice"`     | Textual data, enclosed in single or double quotes.     |
| `bool`    | Boolean                       | `is_student = True`  | Represents `True` or `False`. Used in conditional logic. |

## Basic Operators

### Arithmetic Operators
Used to perform mathematical operations.

| Operator | Description    | Example     | Result |
| :------- | :------------- | :---------- | :----- |
| `+`      | Addition       | `5 + 2`     | `7`    |
| `-`      | Subtraction    | `5 - 2`     | `3`    |
| `*`      | Multiplication | `5 * 2`     | `10`   |
| `/`      | Division       | `5 / 2`     | `2.5`  |
| `//`     | Floor Division | `5 // 2`    | `2`    |
| `%`      | Modulus        | `5 % 2`     | `1`    |
| `**`     | Exponentiation | `5 ** 2`    | `25`   |

### Assignment Operators
Used to assign values to variables.

| Operator | Example   | Equivalent to |
| :------- | :-------- | :------------ |
| `=`      | `x = 5`   | `x = 5`       |
| `+=`     | `x += 3`  | `x = x + 3`   |
| `-=`     | `x -= 3`  | `x = x - 3`   |

### Comparison Operators
Used to compare two values. They return a Boolean (`True` or `False`).

| Operator | Description              | Example     | Result |
| :------- | :----------------------- | :---------- | :----- |
| `==`     | Equal to                 | `5 == 2`    | `False`|
| `!=`     | Not equal to             | `5 != 2`    | `True` |
| `>`      | Greater than             | `5 > 2`     | `True` |
| `<`      | Less than                | `5 < 2`     | `False`|
| `>=`     | Greater than or equal to | `5 >= 5`    | `True` |
| `<=`     | Less than or equal to    | `5 <= 2`    | `False`|

## Basic Input and Output

### Output
As we've seen, the `print()` function is used for output. You can also use f-strings (formatted string literals) for more readable and convenient formatting.

```python
name = "Bob"
age = 40
print(f"{name} is {age} years old.")
# Output: Bob is 40 years old.
```

### Input
The `input()` function allows you to get input from the user. It always returns the data as a string.

```python
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
```

If you need to perform mathematical operations, you'll need to convert the input string to a number (`int` or `float`).

```python
user_age_str = input("Enter your age: ")
user_age_int = int(user_age_str)
print(f"Next year, you will be {user_age_int + 1} years old.")
```

## Introduction to Data Structures

Data structures are a way of organizing and storing data in a computer so that it can be accessed and used efficiently. Python has several built-in data structures, and in this section, we will focus on lists and tuples.

## Lists

A list is an ordered and mutable (changeable) collection of items. Lists can contain items of different data types.

### Creating Lists

You create a list by placing items inside square brackets `[]`, separated by commas.

```python
# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list with mixed data types
mixed_list = ["hello", 3.14, True, 42]
```

### Indexing and Slicing

You can access elements in lists and other sequence types (like strings and tuples) using indexing and slicing.

*   **Indexing:** Access individual items using their index. Python is zero-indexed, meaning the first item is at index 0.

    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0])  # Output: apple
    print(fruits[2])  # Output: cherry
    ```

*   **Negative Indexing:** You can also use negative indices to access items from the end of the list. `-1` refers to the last item, `-2` to the second-to-last, and so on.

    ```python
    print(fruits[-1]) # Output: cherry
    print(fruits[-2]) # Output: banana
    ```

*   **Slicing:** Access a range of items by specifying a `start` and `end` index (`start:end`). The slice will include the element at the `start` index but **exclude** the element at the `end` index.

    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers[1:5])  # Output: [1, 2, 3, 4]
    print(numbers[:4])   # Output: [0, 1, 2, 3] (from the beginning up to index 4)
    print(numbers[5:])   # Output: [5, 6, 7, 8, 9] (from index 5 to the end)
    ```

*   **Slicing with a Step:** You can also provide a "step" value to your slice (`start:end:step`). This allows you to skip elements.

    ```python
    print(numbers[0:10:2]) # Output: [0, 2, 4, 6, 8] (every second element)
    ```

*   **Reversing a List with Slicing:** A common trick is to use a step of `-1` to reverse a list.

    ```python
    print(numbers[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ```

### Modifying Lists

Since lists are mutable, you can change their content.

*   **Change an item:**
    ```python
    fruits[1] = "blueberry"
    print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
    ```
*   **Add items:**
    *   `append()`: Adds an item to the end of the list.
        ```python
        fruits.append("orange")
        print(fruits) # Output: ['apple', 'blueberry', 'cherry', 'orange']
        ```
    *   `insert()`: Adds an item at a specified index.
        ```python
        fruits.insert(1, "grape")
        print(fruits) # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']
        ```
*   **Remove items:**
    *   `remove()`: Removes the first occurrence of a specified value.
        ```python
        fruits.remove("cherry")
        ```
    *   `pop()`: Removes an item at a specified index (or the last item if the index is not provided).
        ```python
        fruits.pop(1)
        ```

## Tuples

A tuple is an ordered and **immutable** (unchangeable) collection of items. Once a tuple is created, you cannot change its values.

### Creating Tuples

You create a tuple by placing items inside parentheses `()`, separated by commas.

```python
# A tuple of numbers
point = (10, 20)

# A tuple of strings
colors = ("red", "green", "blue")
```

### When to use Tuples?

Use tuples when you have data that should not change, such as coordinates, dates, or configuration settings. Their immutability makes your code safer from accidental changes.

## Conditional Statements

Conditional statements allow you to execute certain blocks of code based on whether a condition is true or false.

### `if`, `elif`, and `else`

*   `if`: The block of code under `if` is executed if the condition is `True`.
*   `elif` (else if): If the first `if` condition is `False`, Python checks the `elif` condition.
*   `else`: If all preceding conditions are `False`, the `else` block is executed.

```python
age = 18

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
# Output: You are a teenager.
```
