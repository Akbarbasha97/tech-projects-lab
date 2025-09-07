# TYPECASTING IN PYTHON

print("=== TYPECASTING (TYPE CONVERSION) ===\n")

# IMPLICIT TYPECASTING (Automatic)
print("1. IMPLICIT TYPECASTING")
print("Python automatically converts data types when needed:")

int_num = 10
float_num = 3.5
result = int_num + float_num  # int automatically converted to float
print(f"int + float: {int_num} + {float_num} = {result} (type: {type(result).__name__})")

bool_val = True
result2 = bool_val + int_num  # bool converted to int (True = 1)
print(f"bool + int: {bool_val} + {int_num} = {result2} (type: {type(result2).__name__})")
print()

# EXPLICIT TYPECASTING (Manual)
print("2. EXPLICIT TYPECASTING")
print("Manual conversion using built-in functions:\n")

# STRING TO INTEGER
print("A) STRING TO INTEGER - int()")
str_number = "42"
int_converted = int(str_number)
print(f"int('{str_number}') = {int_converted} (type: {type(int_converted).__name__})")

# String with decimal to int (removes decimal part)
str_decimal = "42.8"
try:
    int_from_decimal = int(float(str_decimal))  # Convert to float first, then int
    print(f"int(float('{str_decimal}')) = {int_from_decimal}")
except ValueError as e:
    print(f"Error: {e}")
print()

# STRING TO FLOAT
print("B) STRING TO FLOAT - float()")
str_float = "3.14159"
float_converted = float(str_float)
print(f"float('{str_float}') = {float_converted} (type: {type(float_converted).__name__})")

str_int = "100"
float_from_int = float(str_int)
print(f"float('{str_int}') = {float_from_int} (type: {type(float_from_int).__name__})")
print()

# INTEGER/FLOAT TO STRING
print("C) NUMBER TO STRING - str()")
number = 123
str_converted = str(number)
print(f"str({number}) = '{str_converted}' (type: {type(str_converted).__name__})")

pi = 3.14159
str_pi = str(pi)
print(f"str({pi}) = '{str_pi}' (type: {type(str_pi).__name__})")
print()

# STRING TO BOOLEAN
print("D) STRING TO BOOLEAN - bool()")
print("Note: Empty string = False, Non-empty string = True")
empty_str = ""
non_empty_str = "Hello"
print(f"bool('') = {bool(empty_str)}")
print(f"bool('Hello') = {bool(non_empty_str)}")
print()

# NUMBER TO BOOLEAN
print("E) NUMBER TO BOOLEAN - bool()")
print("Note: 0 = False, Any other number = True")
zero = 0
non_zero = 42
print(f"bool(0) = {bool(zero)}")
print(f"bool(42) = {bool(non_zero)}")
print()

# LIST/TUPLE CONVERSIONS
print("F) LIST AND TUPLE CONVERSIONS")
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(f"tuple({my_list}) = {my_tuple} (type: {type(my_tuple).__name__})")

back_to_list = list(my_tuple)
print(f"list({my_tuple}) = {back_to_list} (type: {type(back_to_list).__name__})")
print()

# STRING TO LIST
print("G) STRING TO LIST")
text = "Hello"
char_list = list(text)
print(f"list('{text}') = {char_list}")

# Join list back to string
joined = ''.join(char_list)
print(f"''.join({char_list}) = '{joined}'")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: User input (always string) to number
print("Example 1: Converting user input")
user_age = "25"  # Simulating input()
age = int(user_age)
print(f"User entered: '{user_age}' -> Converted to: {age}")
next_year = age + 1
print(f"Next year you'll be: {next_year}")
print()

# Example 2: Calculating average from string inputs
print("Example 2: Grade calculator")
grade1_str = "85"
grade2_str = "92"
grade3_str = "78"

grade1 = int(grade1_str)
grade2 = int(grade2_str)
grade3 = int(grade3_str)

average = (grade1 + grade2 + grade3) / 3
print(f"Grades: {grade1}, {grade2}, {grade3}")
print(f"Average: {average:.2f}")
print()

# Example 3: Formatting numbers for display
print("Example 3: Number formatting")
price = 19.99
quantity = 3
total = price * quantity

# Convert to strings for formatted display
formatted_output = f"Price: ${str(price)} x {str(quantity)} = ${str(total)}"
print(formatted_output)
print()

# ERROR HANDLING
print("=== ERROR HANDLING ===\n")
print("Common typecasting errors:")

# Invalid string to int
try:
    invalid_conversion = int("abc")
except ValueError as e:
    print(f"Error converting 'abc' to int: {e}")

# Float string with int()
try:
    float_str_to_int = int("3.14")
except ValueError as e:
    print(f"Error converting '3.14' to int: {e}")
    print("Solution: Use int(float('3.14')) = ", int(float("3.14")))

# Division by zero after conversion
try:
    zero_str = "0"
    zero_num = int(zero_str)
    result = 10 / zero_num
except ZeroDivisionError as e:
    print(f"Error: {e}")
print()

# CHECKING DATA TYPES
print("=== CHECKING DATA TYPES ===\n")

def check_and_convert(value):
    print(f"Value: {value}")
    print(f"Type: {type(value).__name__}")
    print(f"Is string? {isinstance(value, str)}")
    print(f"Is integer? {isinstance(value, int)}")
    print(f"Is float? {isinstance(value, float)}")
    print(f"Is numeric string? {str(value).isdigit() if isinstance(value, str) else 'N/A'}")
    print()

check_and_convert("123")
check_and_convert(123)
check_and_convert(123.45)
check_and_convert(True)

# SAFE CONVERSION FUNCTION
print("=== SAFE CONVERSION FUNCTION ===\n")

def safe_int_conversion(value):
    """Safely convert a value to integer with error handling"""
    try:
        return int(value)
    except ValueError:
        try:
            # Try converting float string to int
            return int(float(value))
        except ValueError:
            print(f"Cannot convert '{value}' to integer")
            return None

# Test safe conversion
test_values = ["42", "42.8", "abc", "3.14", True, 100]
for val in test_values:
    result = safe_int_conversion(val)
    print(f"safe_int_conversion({val}) = {result}")

def add(x, y):
    return x + y