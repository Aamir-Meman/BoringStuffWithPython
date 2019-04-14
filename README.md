# Boring Stuff With Python
This is a repository only for learning python and automate boring stuff in daily life.

**You'll remember the things you do much better than the things you only read.**

## Expressions
- 2 + 2

Expressions consist of **values** (such as 2) and **operators** (such as +), and they can evaluate down to a single value.

## Precedence

The ** operator is evaluated first; the ***, /, //, and %** are evaluted next, from left to right; and the + and - operators are evaluated last (also from left to right). You can use parentheses to override the usual precedence if you need to.

## The Integer, Floating-Point, and String Data Types

- A data type is a category for values, and every value belongs to exactly one data type.
- The integer (or int) data type indicates values that are whole numbers.
- Numbers with a decimal point, such as 3.14 are called floating point numbers (or floats).
- Always surround your string in **single quote (')**
- You can even have a string with no characters in it. **''** called a **blank string**.

## String Concatenation and Replication

- **+** is the addition operator when it operates on two integers or floating-point values. However, when + is used on two string values, it joins the strings as the **string concatenation operator**.
- The * operator is used for multiplication when it operates on two integer or floating point values.But when the * operator is used on one string value and one integer value, it becomes the **string replication** operator.

## Storing Values in Variables
- A **variable** is like a box in the computer's memory where you can store a single value. 
- If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.
- **Assignment Statements**
  - You'll store values in variables with an assignment statement. An assignment statement consists of a variable name, an equal sign (called the assignment operator), and the value to be stored.
  - If you enter the assignment statement spam = 42, then a variable named spam will have the integer value 42 stored in it.
 
## A Collection of Modules

- Packages are nothing more than a folder of Python module files.
- In the package folder, a file named __init__.py should be present,it can be empty
  - This file can be used for package initialization
- When Python sees this file, it treats the folder as a package, and it modules can be imported
- The folder name is the package name, and can be thought of as a namespace

## Publicly Distributed Packages 

- The **Python Package Index** is the official public package repository for Python.
- The packages are simply shared code libraries which save developers lots of time by not requiring them to reinvent the wheel for each task they need to accomplish.
- To use the repository to download and install packages, the program pip is used.
- **Pip** is distributed with Python.
- https://pypi.python.org/pypi

## Installing Packages

- Packages can be installed globally or for the user.
- To install a package globally, open a terminal, and run the following command:
-       pip install <package name>
- To install the package for the current user only, run the following command:
-       pip install --user <package name>

## Removing Packages

- To remove a package run:
-       pip uninstall <package name>
- If a package is installed locally (with --user) and globally, the local version will be installed first.
- Run the command again to uninstall the package globally.

## Listing Packages

- To list all installed packages:
-       pip list
- To see a list of outdated packages:
-       pip list --outdated
- To upgrade a package:
-       pip install --upgrade <package name>
- To see more details of a package:
-       pip show <package name>

## Requirements File

- To ensure packages are installed for a given application, a "requirements.txt" can be created.
- To initially create the "requirements.txt" file, the **pip** "freeze" command can be used
-       pip freeze > requirements.txt
- The "requirements.txt" can be used by **pip** to install the packages listed inside of it
-       pip install -r requirements.txt 
