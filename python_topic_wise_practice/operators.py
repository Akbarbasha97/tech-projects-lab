# ARITHMETIC OPERATORS IN PYTHON

print("=== ARITHMETIC OPERATORS ===\n")

# Sample numbers for demonstration
a = 20
b = 6

print(f"Using a = {a} and b = {b}:\n")

# 1. ADDITION (+)
print("1. ADDITION (+)")
result = a + b
print(f"   {a} + {b} = {result}")
print()

# 2. SUBTRACTION (-)
print("2. SUBTRACTION (-)")
result = a - b
print(f"   {a} - {b} = {result}")
print()

# 3. MULTIPLICATION (*)
print("3. MULTIPLICATION (*)")
result = a * b
print(f"   {a} * {b} = {result}")
print()

# 4. DIVISION (/)
print("4. DIVISION (/) - Returns float")
result = a / b
print(f"   {a} / {b} = {result}")
print()

# 5. FLOOR DIVISION (//)
print("5. FLOOR DIVISION (//) - Returns integer (rounded down)")
result = a // b
print(f"   {a} // {b} = {result}")
print(f"   25 // 4 = {25 // 4}")  # Additional example
print()

# 6. MODULUS (%)
print("6. MODULUS (%) - Returns remainder")
result = a % b
print(f"   {a} % {b} = {result}")
print(f"   17 % 5 = {17 % 5}")  # Additional example
print()

# 7. EXPONENTIATION (**)
print("7. EXPONENTIATION (**) - Power")
result = a**b
print(f"   {a} ** {b} = {result}")
print(f"   2 ** 3 = {2 ** 3}")  # Additional example
print()

# OPERATOR PRECEDENCE
print("=== OPERATOR PRECEDENCE ===")
print("Order of operations (highest to lowest priority):")
print("1. Parentheses ()")
print("2. Exponentiation **")
print("3. Multiplication *, Division /, Floor Division //, Modulus %")
print("4. Addition +, Subtraction -")
print()

# Examples of precedence
print("Precedence Examples:")
expr1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {expr1} (multiplication first)")

expr2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {expr2} (parentheses first)")

expr3 = 2**3**2
print(f"2 ** 3 ** 2 = {expr3} (right to left for **)")

expr4 = 10 - 6 + 2
print(f"10 - 6 + 2 = {expr4} (left to right for same precedence)")
print()

# ASSIGNMENT OPERATORS
print("=== ASSIGNMENT OPERATORS ===")
x = 10
print(f"Initial x = {x}")

x += 5  # x = x + 5
print(f"x += 5  -> x = {x}")

x -= 3  # x = x - 3
print(f"x -= 3  -> x = {x}")

x *= 2  # x = x * 2
print(f"x *= 2  -> x = {x}")

x /= 4  # x = x / 4
print(f"x /= 4  -> x = {x}")

x **= 2  # x = x ** 2
print(f"x **= 2 -> x = {x}")

x //= 3  # x = x // 3
print(f"x //= 3 -> x = {x}")

x %= 5  # x = x % 5
print(f"x %= 5  -> x = {x}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Calculate area of rectangle
length = 15
width = 8
area = length * width
print(f"Rectangle area: {length} * {width} = {area} square units")

# Calculate compound interest
principal = 1000
rate = 0.05  # 5%
time = 3  # years
amount = principal * (1 + rate)**time
print(
    f"Compound Interest: ${principal} at {rate*100}% for {time} years = ${amount:.2f}"
)

# Check if number is even or odd
number = 17
remainder = number % 2
if remainder == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Convert temperature
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Calculate average
num1, num2, num3 = 85, 92, 78
average = (num1 + num2 + num3) / 3
print(f"Average of {num1}, {num2}, {num3} = {average:.2f}")
print()

# WORKING WITH DIFFERENT DATA TYPES
print("=== ARITHMETIC WITH DIFFERENT TYPES ===")

# Integer and float
int_num = 10
float_num = 3.5
result = int_num + float_num
print(
    f"Integer + Float: {int_num} + {float_num} = {result} (type: {type(result).__name__})"
)

# String repetition with *
text = "Hello "
repeated = text * 3
print(f"String repetition: '{text}' * 3 = '{repeated}'")

# List repetition with *
my_list = [1, 2]
repeated_list = my_list * 3
print(f"List repetition: {my_list} * 3 = {repeated_list}")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


def power(x, y):
    return x**y


def calculator():
    print("=== SIMPLE CALCULATOR ===")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    while True:
        choice = input("\nEnter choice (1-6): ")

        if choice == '10':
            print("Thank you for using the calculator!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")

                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")

                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")

                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

                elif choice == '5':
                    result = power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}")

            except ValueError:
                print("Error: Please enter valid numbers!")

        else:
            print("Invalid input! Please enter a number between 1-6.")


# Advanced calculator with more operations
def advanced_calculator():
    import math

    print("\n=== ADVANCED CALCULATOR ===")
    print("Available operations:")
    print("Basic: +, -, *, /, ** (power)")
    print("Advanced: sqrt, sin, cos, tan, log, factorial")
    print("Type 'exit' to quit")

    while True:
        expression = input(
            "\nEnter calculation (e.g., '5 + 3' or 'sqrt(16)'): ")

        if expression.lower() == 'exit':
            break

        try:
            # Replace common math functions
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log')
            expression = expression.replace('factorial', 'math.factorial')

            # Evaluate the expression
            result = eval(expression)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("Choose calculator mode:")
    print("1. Simple Calculator")
    print("2. Advanced Calculator")

    mode = input("Enter choice (1 or 2): ")

    if mode == '1':
        calculator()
    elif mode == '2':
        advanced_calculator()
    else:
        print("Invalid choice! Running simple calculator...")
        calculator()
