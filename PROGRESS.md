# Training Progress

## 2026-08-17

### What I Learned

- Set up and configured the GitHub CLI (`gh`) on Garuda Linux.
- Learned the difference between Git and GitHub CLI and when CLI-based GitHub operations are useful.
- Configured GitHub CLI authentication using a Personal Access Token (PAT).
- Learned about fine-grained Personal Access Tokens and the principle of least privilege.
- Understood the difference between fine-grained and classic PATs and restricted the training repository token to the required permissions.
- Verified GitHub SSH authentication and configured the repository to use SSH for Git operations.
- Created and organized the `ScaleTech-Training` GitHub repository.
- Learned about Git repository structure, branches, remotes, commits, and repository synchronization.
- Created a basic folder structure for Stage 1 training.
- Learned about multiple Python installations on Linux and how `PATH` determines which Python executable is used.
- Identified Python 3.14.7 and Python 3.11.16 installations on the system.
- Created an isolated Python 3.11.16 virtual environment using `venv`.
- Learned the purpose and structure of `.venv`, including `bin`, `lib`, `include`, and `pyvenv.cfg`.
- Learned how to verify the Python interpreter used by a virtual environment.
- Learned how `pip` works inside a virtual environment.
- Installed the `requests` package and observed its dependencies.
- Learned about dependency management and created `requirements.txt` using `pip freeze`.
- Configured `.gitignore` to exclude the virtual environment and company-provided training roadmap from Git.

### Tasks / Activities

- Installed and configured GitHub CLI.
- Authenticated GitHub CLI using a fine-grained PAT.
- Verified SSH authentication with GitHub.
- Created and renamed the training repository.
- Configured the Git remote using SSH.
- Created the initial Stage 1 repository structure.
- Created a Python 3.11 virtual environment.
- Activated and verified the virtual environment using Fish.
- Installed `requests` using `pip`.
- Generated `requirements.txt`.
- Started configuring `.gitignore`.

### Key Takeaways / Challenges

- Git and GitHub are related but serve different purposes: Git handles version control, while GitHub provides hosting and collaboration features.
- GitHub CLI provides command-line access to GitHub functionality, while Git itself handles version-control operations.
- SSH keys and Personal Access Tokens serve different authentication purposes and can be used together.
- Fine-grained PATs provide more restrictive repository and permission control than classic PATs.
- Virtual environments allow project dependencies to remain isolated from system-wide Python packages.
- Multiple Python versions can coexist on Linux without changing the system default Python.
- `python3.11 -m venv .venv` allows the project to explicitly use Python 3.11 instead of the system Python 3.14.
- `requirements.txt` allows project dependencies to be recorded and recreated on another system.
- Learned that Git does not track empty directories and that `.gitignore` prevents files such as `.venv` from being tracked.

### Progress / Updates

- Initial GitHub repository and local development environment are configured.
- Python 3.11.16 virtual environment is ready for the training.
- Package management and dependency tracking have been introduced.
- Python programming concepts have not been started yet; they will begin in the next training session.

## 2026-08-18

### What I Learned

#### Python Fundamentals

- Learned Python data types and how different types represent different kinds of values.
- Learned variables and variable assignment.
- Learned Python operators, including arithmetic, comparison, logical, assignment, and other commonly used operators.
- Learned input and output operations using `input()` and `print()`.
- Learned control flow using conditional statements such as `if`, `elif`, and `else`.
- Learned loops and how iteration is used to repeatedly execute code.
- Learned functions and how functions help organize reusable logic.
- Learned positional and keyword arguments.
- Learned `*args` for handling a variable number of positional arguments.
- Learned `**kwargs` for handling a variable number of keyword arguments.
- Learned Python variable scope and how local and global variables behave.
- Learned built-in Python functions and their practical usage.
- Learned lambda functions for creating small anonymous functions.
- Learned the use of `break`, `continue`, and `pass` in control flow.
- Learned the `range()` function for generating sequences of numbers, particularly for iteration.

#### Core Data Structures

- Learned Lists and their use for ordered, mutable collections.
- Learned Tuples and their use for ordered, immutable collections.
- Learned Sets and their use for collections of unique elements.
- Learned Dictionaries and key-value based data storage.
- Learned list comprehensions for concise list creation and transformation.
- Learned dictionary comprehensions for concise dictionary creation and transformation.
- Learned string manipulation techniques.
- Learned string formatting and how formatted strings can be used to construct readable output.

### Tasks / Activities

- Practiced Python variables, data types, and operators.
- Implemented input/output examples.
- Practiced conditional statements and loops.
- Implemented functions using regular arguments, `*args`, and `**kwargs`.
- Practiced variable scope.
- Used built-in functions and lambda functions.
- Practiced `break`, `continue`, `pass`, and `range()`.
- Implemented examples using Lists, Tuples, Sets, and Dictionaries.
- Practiced list and dictionary comprehensions.
- Practiced string manipulation and formatting.

### Key Takeaways

- Python provides dynamic typing, allowing variables to reference values of different data types without explicitly declaring their type.
- Control flow determines which parts of a program execute and how many times they execute.
- Functions provide reusable and organized units of logic.
- `*args` and `**kwargs` allow functions to accept flexible numbers of positional and keyword arguments.
- Python's built-in data structures provide different trade-offs depending on whether ordering, mutability, uniqueness, or key-value access is required.
- Comprehensions provide a concise way to create collections from existing iterables.
- String formatting provides a structured way to construct readable and dynamic text.

### Progress / Updates

- Completed the core Python fundamentals covered in the current training section.
- Started working with Python's core built-in data structures.
- Ready to continue with the remaining Stage 1 Python topics.

## 2026-08-19

### What I Learned

#### Modules and Packages

- Learned how to use Python's built-in `math` module for mathematical operations.
- Learned how to use the `random` module for generating random values and making random selections.
- Learned how to use the `os` module for interacting with the operating system and filesystem.
- Learned how to use the `datetime` module for working with dates and times.
- Learned how to create custom Python modules and import functionality from them.
- Learned the basics of organizing reusable code into modules.
- Learned the `re` (Regular Expression) library for pattern matching and text processing.

#### Error Handling

- Learned how `try-except` blocks handle runtime exceptions.
- Learned how to catch specific exception types.
- Learned how to use `raise` to explicitly raise exceptions when a condition is invalid.

### Tasks / Activities

- Practiced importing and using built-in Python modules.
- Implemented examples using `math`, `random`, `os`, and `datetime`.
- Created and imported custom Python modules.
- Practiced regular expressions using the `re` library.
- Implemented `try-except` blocks for handling exceptions.
- Practiced raising exceptions using the `raise` statement.

### Key Takeaways

- Modules allow functionality to be organized into reusable Python files.
- Python's standard library provides many modules for common programming tasks without requiring external packages.
- Custom modules help separate application logic and improve code organization.
- Regular expressions provide a way to search, validate, and extract structured information from text.
- Exception handling allows programs to handle unexpected runtime conditions gracefully.
- Explicitly raising exceptions allows a program to enforce validation rules and communicate invalid states.

### Progress / Updates

- Completed the Modules and Packages topics for the current Stage 1 training section.
- Completed the Error Handling topics covering `try-except` and `raise`.
- Ready to continue with the next Stage 1 topics.

## 2026-08-20

### What I Learned

#### File Handling

- Learned basic file handling in Python.
- Learned how to open, read, write, and append files.
- Learned different file modes such as `r`, `w`, `a`, and `x`.
- Learned how to use the `with` statement for safe file handling.
- Learned how to work with file encodings using UTF-8.
- Learned how to handle file-related exceptions such as `FileNotFoundError` and `PermissionError`.
- Learned how to read and write CSV files using Python's built-in `csv` module.
- Learned `csv.reader()` and `csv.writer()`.
- Learned `csv.DictReader()` and `csv.DictWriter()` for working with structured CSV data.

#### CLI Calculator

- Started building a basic command-line calculator.
- Implemented arithmetic operations using separate functions.
- Added user input and operator selection.
- Added continuous calculation using a `while` loop.
- Added error handling using `try-except`.
- Used `raise ValueError` for division by zero.
- Used `break` and `continue` to control the calculator loop.

### Tasks / Activities

- Implemented a basic file read/write program.
- Implemented a CSV read/write program.
- Created a basic CLI calculator.
- Added continuous calculation support.
- Added exception handling to the calculator.
- Practiced combining previously learned Python concepts into a practical project.

### Key Takeaways

- File handling allows Python programs to persist and retrieve data.
- The `with` statement provides safer resource management when working with files.
- The `csv` module should be used instead of manually splitting CSV lines.
- Exceptions can be raised inside functions and handled at a higher level.
- Loops, functions, conditions, and exception handling can be combined to build useful CLI applications.

### Progress / Updates

- Completed the basic File Handling topics.
- Completed the CSV File Handling topics.
- Started the CLI Calculator project.
- CLI Calculator currently supports basic arithmetic operations, continuous execution, and error handling.
- Tomorrow's focus will be the **CLI To-Do List project**, including filesystem-based data storage.

## 2026-08-21

### What I Learned

#### CLI To-Do List

- Built a command-line To-Do List application using Python.
- Implemented task creation, viewing, updating, completion, and deletion.
- Used lists and dictionaries to represent and manage task data.
- Used functions to separate different task operations.
- Created a custom `todo.py` module for helper functions and application logic.
- Used `main.py` as the entry point and CLI interface.
- Implemented persistent task storage using a JSON file.
- Used the `json` module to read and write task data.
- Used `pathlib` to manage the application data file path.
- Used `datetime` to store task creation timestamps.
- Applied `try-except` and `raise` for input validation and error handling.
- Practiced separation of concerns by separating the CLI interface from task management logic.

#### Object-Oriented Programming Fundamentals

- Started learning **Classes and Objects**.
- Learned the purpose of classes as blueprints for creating objects.
- Learned how objects represent instances of classes.
- Started understanding **Inheritance** and how classes can reuse and extend functionality from other classes.
- Started understanding **Polymorphism** and how different objects can provide different implementations of the same interface or method.
- Started understanding **Encapsulation** and how data and behavior can be organized and controlled within a class.

### Tasks / Activities

- Created the CLI To-Do List project structure.
- Implemented task CRUD operations.
- Added JSON-based persistent storage.
- Separated helper functions into a custom Python module.
- Practiced importing and using a custom module from `main.py`.
- Studied the fundamentals of classes and objects.
- Studied the fundamentals of inheritance, polymorphism, and encapsulation.

### Key Takeaways

- CLI applications can combine multiple Python concepts into a practical project.
- JSON provides a convenient way to persist structured Python data.
- Separating application logic into modules makes the code easier to maintain and extend.
- Classes provide a way to model real-world entities and group related data and behavior.
- Inheritance allows classes to reuse and extend existing functionality.
- Polymorphism allows different objects to respond to the same operation in different ways.
- Encapsulation helps control how an object's internal data and behavior are accessed.

### Progress / Updates

- Completed the CLI To-Do List project with JSON-based persistent storage.
- Completed the basic implementation of task CRUD operations.
- Started learning Object-Oriented Programming fundamentals.
- Covered the fundamentals of Classes, Objects, Inheritance, Polymorphism, and Encapsulation.
- Ready to continue with practical Object-Oriented Programming concepts and implementation.
