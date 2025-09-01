
# Variables and Data Types in Python

# 1. VARIABLES
# Variables are containers that store data values
# Python has no command for declaring a variable - it's created when you assign a value

name = "John"           # String variable
age = 25               # Integer variable
height = 5.9           # Float variable
is_student = True      # Boolean variable

print("Variables:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")
print()

# 2. DATA TYPES
print("Data Types:")

# String (str) - Text data
text = "Hello World"
print(f"String: {text} - Type: {type(text)}")

# Integer (int) - Whole numbers
number = 42
print(f"Integer: {number} - Type: {type(number)}")

# Float (float) - Decimal numbers
decimal = 3.14159
print(f"Float: {decimal} - Type: {type(decimal)}")

# Boolean (bool) - True or False
is_valid = True
print(f"Boolean: {is_valid} - Type: {type(is_valid)}")

# List - Ordered collection of items
fruits = ["apple", "banana", "orange"]
print(f"List: {fruits} - Type: {type(fruits)}")

# Tuple - Ordered, unchangeable collection
coordinates = (10, 20)
print(f"Tuple: {coordinates} - Type: {type(coordinates)}")

# Dictionary - Key-value pairs
person = {"name": "Alice", "age": 30}
print(f"Dictionary: {person} - Type: {type(person)}")

# Set - Unordered collection of unique items
unique_numbers = {1, 2, 3, 4, 5}
print(f"Set: {unique_numbers} - Type: {type(unique_numbers)}")

# NoneType - Represents absence of value
nothing = None
print(f"None: {nothing} - Type: {type(nothing)}")
print()

# 3. TYPE CONVERSION
print("Type Conversion:")
str_number = "123"
int_number = int(str_number)      # String to integer
float_number = float(str_number)   # String to float
bool_value = bool(str_number)      # String to boolean

print(f"Original: '{str_number}' ({type(str_number)})")
print(f"To int: {int_number} ({type(int_number)})")
print(f"To float: {float_number} ({type(float_number)})")
print(f"To bool: {bool_value} ({type(bool_value)})")
print()

# 4. VARIABLE NAMING RULES
print("Variable Naming Rules:")
# Valid variable names
first_name = "John"       # Use underscores
lastName = "Doe"          # CamelCase (less common in Python)
age2 = 25                 # Numbers allowed (not at start)
_private = "hidden"       # Underscore prefix

print("Valid names: first_name, lastName, age2, _private")

# Invalid examples (commented out to avoid errors):
# 2age = 25              # Cannot start with number
# first-name = "John"    # Cannot use hyphens
# class = "Python"       # Cannot use reserved keywords

# 5. CHECKING DATA TYPES
print("\nChecking Data Types:")
value = 42
print(f"Is {value} an integer? {isinstance(value, int)}")
print(f"Is {value} a string? {isinstance(value, str)}")

# 6. MUTABLE vs IMMUTABLE
print("\nMutable vs Immutable:")
# Immutable - cannot be changed after creation
immutable_string = "Hello"
print(f"Original string: {immutable_string}")

# Mutable - can be changed after creation
mutable_list = [1, 2, 3]
print(f"Original list: {mutable_list}")
mutable_list.append(4)
print(f"Modified list: {mutable_list}")
