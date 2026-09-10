# Training Progress

## 2026-09-10

### What I Learned

#### Pandas Project

- Implemented a small **Pandas data analysis project** using a CSV dataset.
- Learned to load data using `pd.read_csv()`.
- Practiced DataFrame inspection, filtering, sorting, grouping, and basic analysis.
- Exported processed results to a CSV file.

#### Django Basics

- Installed **Django** inside the Python 3.13 virtual environment.
- Created the first Django project and explored its basic file structure.
- Learned the difference between a **Django project** and a **Django app**.
- Learned the basics of **MVT (Model-View-Template)** architecture.
- Understood the basic request flow between URLs, Views, Models, Templates, and the database.

### Tasks / Activities

- Completed the Pandas dataset analysis project.
- Installed Django and verified the installation.
- Created and ran a basic Django project.
- Explored the Django project structure and important files such as `manage.py`, `settings.py`, and `urls.py`.
- Practiced understanding the MVT architecture.

### Challenges

- Understanding Django's project structure and the role of different files.
- Understanding how MVT differs from the architecture of frameworks such as NestJS and Next.js.

### Key Takeaways

- Pandas provides useful tools for processing and analyzing structured data.
- Django is a Python web framework for building web applications.
- MVT separates data, application logic, and presentation.
- Django projects are organized into reusable applications.
- `manage.py` is used to manage and run Django projects.

### Progress / Updates

- Completed the practical **Pandas** task.
- Installed and configured **Django** in the virtual environment.
- Created the first Django project.
- Learned the Django project structure and basics of **MVT architecture**.

## 2026-09-08

### What I Learned

#### Logging and Debugging

- Learned the basics of Python's **`logging`** module.
- Learned logging levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- Learned how to write logs to a file with timestamps and log levels.
- Learned how `logging.exception()` records errors with traceback information.
- Learned the basics of debugging using the **Python debugger in VSCodium**.
- Learned how to use breakpoints and step through code.
- Learned the basic debugger controls: Continue, Step Over, Step Into, and Step Out.

### Tasks / Activities

- Implemented a logging program with different log levels.
- Created an `app.log` file to record application events and errors.
- Implemented error logging using `logging.exception()`.
- Practiced debugging a Python program using breakpoints and variable inspection.

### Challenges

- Understanding the difference between `print()` and proper logging.
- Understanding when to use different logging levels.
- Practicing step-by-step debugging and inspecting variable values.

### Key Takeaways

- **Logging** records what is happening in an application.
- **Debugging** helps find where and why unexpected behavior occurs.
- Logging is useful for tracking application behavior and errors.
- Debuggers are useful for inspecting program execution and variable states.

### Progress / Updates

- Completed the basics of **Python Logging and Debugging**.
- Practiced using the **`logging` module** and Python debugger.
- Completed practical implementations for logging, error tracking, breakpoints, and step-by-step debugging.

## 2026-09-07

### What I Learned

#### Pandas for Data Analysis

- Learned the basics of **Pandas** for working with structured data.
- Learned how to create **DataFrames** from Python data.
- Learned basic operations such as filtering, sorting, counting, and analyzing data.
- Learned how to save processed data to CSV files.

#### Working with APIs

- Learned how **RESTful APIs** work with HTTP methods.
- Practiced **CRUD operations** using:
  - `GET` for reading data.
  - `POST` for creating data.
  - `PUT` for updating data.
  - `PATCH` for partial updates.
  - `DELETE` for deleting data.
- Learned how to use the `requests` library for API communication.
- Learned how JSON data is converted to Python objects using `response.json()`.
- Learned how Python dictionaries can be sent as JSON using `requests`.

### Tasks / Activities

- Used my own **MockAPI** endpoint for practical API operations.
- Implemented complete CRUD operations using `requests`.
- Retrieved API data and converted it into a Pandas DataFrame.
- Practiced filtering, sorting, counting, and analyzing user data with Pandas.
- Exported processed API data to a CSV file.

### Challenges

- Understanding the difference between `PUT` and `PATCH`.
- Understanding the flow between REST API, JSON, Python objects, and Pandas.
- Combining API operations with Pandas data analysis.

### Key Takeaways

- `requests` is used to communicate with APIs.
- JSON is commonly used to exchange data between applications.
- REST APIs use HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
- Pandas makes it easier to process and analyze structured API data.
- API data can be collected, analyzed, and exported using Python.

### Progress / Updates

- Completed the basics of **Pandas for Data Analysis**.
- Practiced **Requests, JSON, and RESTful APIs**.
- Implemented complete **CRUD operations** using my MockAPI.
- Combined API data with **Pandas** for analysis and CSV export.

## 2026-09-03

### What I Learned

#### Advanced Python Concepts

- Learned the basics of **Decorators** for adding reusable behavior to functions.
- Learned **Context Managers** and the `with` statement for resource management and automatic cleanup.
- Learned **AsyncIO** for handling multiple I/O-bound tasks efficiently.
- Learned **Generators** and `yield` for producing values one at a time.
- Learned **Coroutines** using `async` and `await` for asynchronous programming.
- Learned the difference between **Multithreading** and **Multiprocessing**.
- Learned that multithreading is useful for **I/O-bound tasks**, while multiprocessing is useful for **CPU-bound tasks**.

### Tasks / Activities

- Implemented a decorator to measure function execution time.
- Implemented a custom context manager using `__enter__()` and `__exit__()`.
- Implemented asynchronous tasks using `asyncio`, `async`, `await`, and `asyncio.gather()`.
- Implemented a generator using `yield`.
- Implemented coroutines and practiced running them concurrently.
- Implemented basic multithreading using `threading.Thread`.
- Implemented basic multiprocessing using `multiprocessing.Process`.

### Challenges

- Understanding how decorators wrap and modify functions.
- Understanding how context managers handle setup and cleanup automatically.
- Understanding the difference between `async`, `await`, generators, and coroutines.
- Understanding when to use threads versus processes.

### Key Takeaways

- Decorators provide reusable behavior around functions.
- Context managers make resource handling safer and cleaner.
- AsyncIO is useful for concurrent I/O-bound operations.
- Generators help process large data efficiently with less memory.
- Coroutines allow asynchronous tasks to pause and resume.
- Multithreading is suitable for I/O-bound work, while multiprocessing is better suited for CPU-bound work.
- These concepts can help improve performance and resource usage in larger applications.

### Progress / Updates

- Completed the basics of **Decorators**, **Context Managers**, **AsyncIO**, **Generators**, **Coroutines**, **Multithreading**, and **Multiprocessing**.
- Completed practical implementations for all major topics covered today.

## 2026-09-02

### What I Learned

#### Unit Testing

- Learned the purpose of **unit testing** and automated testing.
- Learned how testing helps detect **regressions** after code changes.
- Learned the basics of `unittest` and `pytest`.
- Learned `unittest.TestCase`, assertions, and `unittest.main()`.
- Learned how `__name__ == "__main__"` works.
- Learned how the `unittest` framework automatically creates test objects and runs test methods.
- Learned **mocking and patching** using `unittest.mock`.
- Learned how to test API-related code without making real network requests.
- Learned basic **debugger** features such as breakpoints and step execution.

### Tasks / Activities

- Implemented and tested a calculator using `unittest`.
- Implemented the same tests using `pytest`.
- Implemented API testing using `Mock` and `patch()`.
- Practiced debugging with breakpoints and variable inspection.

### Challenges

- Understanding inheritance with `unittest.TestCase`.
- Understanding automatic test object creation and test execution.
- Understanding the difference between `unittest` and `pytest`.
- Understanding how mocking and patching replace real dependencies during tests.

### Key Takeaways

- Automated testing saves time as applications grow.
- Tests help ensure existing functionality continues to behave as expected.
- `pytest` is simpler to write, while `unittest` is important to understand.
- Mocking isolates code from external dependencies.
- Debugging helps inspect program execution step by step.

### Progress / Updates

- Completed the basics of **Unit Testing**.
- Practiced **`unittest`**, **`pytest`**, **mocking**, **patching**, and **debugging**.
- Completed practical implementations for all major topics covered today.

## 2026-08-31

### What I Learned

#### Working with Databases

- Learned the basics of **SQL** and relational databases.
- Learned the basic **CRUD operations**: Create, Read, Update, and Delete.
- Learned how to create database tables using SQL.
- Learned how to insert, retrieve, update, and delete records.
- Learned how **SQLite** works as a lightweight relational database.
- Learned how to use Python's built-in `sqlite3` module.
- Learned how to connect Python applications to a SQLite database.
- Learned how to create tables and execute SQL queries from Python.
- Learned how to use cursors for executing SQL statements.
- Learned how to retrieve query results using `fetchone()` and `fetchall()`.
- Learned how to use `commit()` to save database changes.
- Learned the importance of **parameterized SQL queries** using `?` placeholders.

#### Web Scraping

- Learned the basics of the `requests` library for making HTTP requests.
- Learned how to inspect HTTP status codes, headers, and response content using `requests`.
- Learned how to process JSON responses using `response.json()`.
- Learned the basics of **BeautifulSoup** for parsing HTML.
- Learned how to find and extract HTML elements using `find()` and `find_all()`.
- Learned the difference between downloading webpage content with `requests` and parsing it with BeautifulSoup.
- Learned the basics of **Selenium** for browser automation.
- Learned how to open webpages using Selenium WebDriver.
- Learned how to find webpage elements using Selenium locators.
- Learned how to retrieve text from browser elements.
- Learned how to close the browser using `driver.quit()`.

### Tasks / Activities

- Implemented a small SQLite database program using Python.
- Created a SQLite table and performed basic CRUD operations.
- Practiced executing SQL queries through Python's `sqlite3` module.
- Implemented a basic `requests` program using a public API.
- Implemented a basic BeautifulSoup program to parse webpage HTML.
- Implemented a basic Selenium program for browser automation.
- Practiced the basic differences and use cases of `requests`, BeautifulSoup, and Selenium.

### Key Takeaways

- SQL is used to communicate with relational databases.
- SQLite provides a simple database solution without requiring a separate database server.
- Python can interact directly with SQLite using the built-in `sqlite3` module.
- `requests` is suitable for making HTTP requests and retrieving web resources.
- BeautifulSoup is useful for parsing and extracting information from HTML.
- Selenium is useful when browser interaction and automation are required.
- `requests` and BeautifulSoup are commonly used together for static webpage scraping.
- Selenium controls an actual browser and is useful for interactive or dynamically rendered webpages.
- Parameterized SQL queries should be used when passing external values into SQL statements.

### Progress / Updates

- Completed the **Introduction to SQL** topic.
- Completed the basics of **SQLite with Python**.
- Completed the basic implementation of the `requests` library.
- Completed the basic implementation of **BeautifulSoup**.
- Completed the basic implementation of **Selenium**.
- Practiced combining previously learned Python concepts with databases and web-related libraries.

## 2026-08-26

### What I Learned

#### Databases

- Learned the fundamentals of **SQL** and relational databases.
- Learned basic SQL concepts for working with structured data.
- Learned how to create and interact with database tables.
- Learned basic SQL operations for inserting, retrieving, updating, and deleting data.
- Learned how to use **SQLite with Python**.
- Learned how Python can connect to and interact with a SQLite database.
- Learned how to execute SQL queries from Python.
- Learned how to create tables and manage database records using Python.
- Learned the basics of using Python's built-in `sqlite3` module.

### Tasks / Activities

- Practiced basic SQL queries.
- Created and interacted with SQLite database tables.
- Connected Python applications to SQLite databases.
- Executed SQL queries using Python.
- Practiced inserting, retrieving, updating, and deleting records using Python and SQLite.

### Key Takeaways

- SQL provides a standard way to interact with relational databases.
- SQLite is a lightweight relational database that does not require a separate database server.
- Python provides built-in SQLite support through the `sqlite3` module.
- Python applications can use SQL queries to persist and manage structured data.
- Database storage provides a more structured and scalable approach to persistent data compared with simple files such as JSON.

### Progress / Updates

- Completed the Introduction to SQL topic.
- Completed the fundamentals of using SQLite with Python.

## 2026-08-25

### What I Learned

#### Advanced Python Modules
- Learned `itertools` and how to handle advanced iterators like combinations and permutations.
- Learned `functools` and its role in higher-order functions and operations.
- Learned the purpose of `functools.partial` to pre-fill or freeze arguments of a function.
- Learned the purpose of `functools.reduce` for applying rolling computations to sequences.
- Learned the purpose of `functools.lru_cache` for memoization and optimizing repetitive function calls.

#### Advanced File Operations
- Learned how to handle complex data formats beyond standard text and CSV.
- Learned JSON and XML parsing for structured data exchange.
- Learned Config File Handling to manage application settings.
- Learned how to read, write, and manage configuration data using INI and YAML formats.

### Tasks / Activities
- Practiced generating combinations and permutations using the `itertools` module.
- Implemented examples using `partial`, `reduce`, and `lru_cache`.
- Practiced parsing, reading, and writing structured data using JSON and XML files.
- Implemented configuration file handling by reading and writing INI and YAML files.

### Key Takeaways
- `itertools` provides memory-efficient, fast tools for creating complex iterators.
- `functools` offers powerful utilities for functional programming and performance optimization (`lru_cache`).
- JSON and XML are essential standards for parsing and structuring data across different systems.
- INI and YAML provide clean, human-readable ways to manage application configurations and settings.

### Progress / Updates
- Completed the `itertools` (combinations, permutations) and `functools` (`partial`, `reduce`, `lru_cache`) topics.
- Learned Advanced File Operations.
- Covered JSON and XML parsing.
- Covered Config File Handling using INI and YAML.

## 2026-08-24

### What I Learned

#### Object-Oriented Programming

- Learned the fundamentals of **Mixins** and how they can provide reusable functionality to classes.
- Learned **Multiple Inheritance** and how a class can inherit functionality from multiple parent classes.
- Learned **Special/Magic Methods** and their role in defining how Python objects behave.
- Learned the `__init__()` magic method for initializing objects.
- Learned the `__str__()` magic method for defining the human-readable string representation of an object.
- Learned about other commonly used magic methods and how Python calls them automatically in specific situations.
- Learned about **Access Modifiers** and Python's approach to public, internal, and name-mangled attributes.
- Learned about Python's underscore conventions such as `_attribute` and `__attribute`.
- Learned about **escape characters** and their use in strings.

#### Python Standard Library

- Started learning the `collections` module from Python's standard library.
- Learned the purpose of `Counter` for counting occurrences of elements.
- Learned the purpose of `defaultdict` for dictionaries with default values.
- Learned the purpose of `deque` for efficient insertion and removal from both ends of a sequence.

### Tasks / Activities

- Practiced creating classes using multiple inheritance.
- Explored the concept of Mixins and reusable class functionality.
- Implemented and experimented with special methods such as `__init__()` and `__str__()`.
- Practiced Python's access modifier conventions and name mangling.
- Practiced using escape characters in strings.
- Implemented examples using `Counter`.
- Implemented examples using `defaultdict`.
- Implemented examples using `deque`.

### Key Takeaways

- Mixins provide a way to add reusable behavior to classes without representing a standalone entity.
- Multiple inheritance allows a class to inherit behavior from more than one parent class.
- Magic methods allow Python classes to integrate with built-in language operations and behaviors.
- Python uses naming conventions and name mangling rather than Java-style strict access modifiers.
- Escape characters allow special characters and formatting to be represented inside strings.
- `Counter`, `defaultdict`, and `deque` provide specialized data structures that can simplify common programming tasks.

### Progress / Updates

- Completed the Mixins and Multiple Inheritance topics.
- Learned commonly used Special/Magic Methods.
- Learned Python Access Modifiers and escape characters.
- Started the Python Standard Library `collections` module.
- Covered `Counter`, `defaultdict`, and `deque`.

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



