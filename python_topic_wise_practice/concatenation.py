
# String Concatenation in Python

# 1. USING THE + OPERATOR
print("1. Using + Operator:")
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# With numbers (convert to string first)
age = 25
message = "I am " + str(age) + " years old"
print(message)
print()

# 2. USING f-STRINGS (FORMATTED STRING LITERALS) - RECOMMENDED
print("2. Using f-strings (Python 3.6+):")
name = "Alice"
age = 30
city = "New York"
intro = f"Hi, I'm {name}, {age} years old, and I live in {city}."
print(intro)

# With expressions
num1 = 10
num2 = 20
result = f"The sum of {num1} and {num2} is {num1 + num2}"
print(result)
print()

# 3. USING .format() METHOD
print("3. Using .format() method:")
template = "Hello {}, you are {} years old"
formatted = template.format("Bob", 35)
print(formatted)

# Named placeholders
template2 = "Hello {name}, you are {age} years old"
formatted2 = template2.format(name="Charlie", age=40)
print(formatted2)
print()

# 4. USING % FORMATTING (OLD STYLE)
print("4. Using % formatting (older style):")
name = "David"
age = 45
message = "Hello %s, you are %d years old" % (name, age)
print(message)
print()

# 5. JOIN METHOD FOR MULTIPLE STRINGS
print("5. Using join() method:")
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)

# Join with different separators
fruits = ["apple", "banana", "orange"]
fruit_list = ", ".join(fruits)
print(f"Fruits: {fruit_list}")
print()

# 6. CONCATENATING WITH DIFFERENT DATA TYPES
print("6. Mixing different data types:")
product = "Laptop"
price = 999.99
quantity = 2
is_available = True

# Using f-strings (best practice)
description = f"Product: {product}, Price: ${price}, Quantity: {quantity}, Available: {is_available}"
print(description)

# Mathematical operations in f-strings
total = f"Total cost: ${price * quantity}"
print(total)
print()

# 7. MULTILINE STRING CONCATENATION
print("7. Multiline concatenation:")
long_text = ("This is a very long string that "
             "spans multiple lines and gets "
             "concatenated automatically")
print(long_text)

# Using triple quotes for multiline
multiline = f"""
Name: {first_name}
Age: {age}
City: {city}
"""
print(multiline)

# 8. PERFORMANCE COMPARISON
print("8. Performance notes:")
print("- f-strings are fastest and most readable")
print("- + operator is simple but can be slow for many concatenations")
print("- join() is best for concatenating many strings")
print("- .format() is more flexible but slower than f-strings")

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
