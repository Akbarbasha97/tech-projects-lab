
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
        expression = input("\nEnter calculation (e.g., '5 + 3' or 'sqrt(16)'): ")

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
