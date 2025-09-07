# USER INPUT IN PYTHON

print("=== USER INPUT IN PYTHON ===\n")

# BASIC INPUT
print("1. BASIC INPUT - input() function")
print("The input() function always returns a string\n")

## default input  will be string, even if you enter a number, please convert it to int or float if needed


# Example 1: Simple input
name = input("Enter your name: ")
print(f"Hello, {name}! Nice to meet you.")
print(f"Type of input: {type(name).__name__}")
print()

# Example 2: Input with prompt
age_str = input("How old are you? ")
print(f"You entered: '{age_str}' (type: {type(age_str).__name__})")
print()

# CONVERTING INPUT TO NUMBERS
print("2. CONVERTING INPUT TO NUMBERS")
print("Since input() returns string, we need to convert to numbers:\n")

# Integer input
try:
    age = int(input("Enter your age as a number: "))
    print(f"Age: {age} (type: {type(age).__name__})")
    years_to_100 = 100 - age
    print(f"Years until you're 100: {years_to_100}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
print()

# Float input
try:
    height = float(input("Enter your height in meters: "))
    print(f"Height: {height}m (type: {type(height).__name__})")
    height_cm = height * 100
    print(f"Height in centimeters: {height_cm}cm")
except ValueError:
    print("Invalid input! Please enter a valid decimal number.")
print()

# MULTIPLE INPUTS
print("3. MULTIPLE INPUTS")
print("Getting multiple values from user:\n")

# Method 1: Separate inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print()

# Method 2: Split single input
print("Enter three numbers separated by spaces:")
numbers_input = input().split()
try:
    num1 = int(numbers_input[0])
    num2 = int(numbers_input[1]) 
    num3 = int(numbers_input[2])
    total = num1 + num2 + num3
    print(f"Numbers: {num1}, {num2}, {num3}")
    print(f"Sum: {total}")
except (ValueError, IndexError):
    print("Please enter exactly three valid numbers separated by spaces.")
print()

# SAFE INPUT FUNCTIONS
print("4. SAFE INPUT FUNCTIONS")
print("Functions to handle input validation:\n")

def get_integer_input(prompt):
    """Get integer input with validation"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_float_input(prompt):
    """Get float input with validation"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no_input(prompt):
    """Get yes/no input with validation"""
    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'y', '1', 'true']:
            return True
        elif response in ['no', 'n', '0', 'false']:
            return False
        else:
            print("Please enter yes/no, y/n, or 1/0.")

# Using safe input functions
print("Using safe input functions:")
user_age = get_integer_input("Enter your age (integer): ")
user_height = get_float_input("Enter your height in meters (decimal): ")
likes_python = get_yes_no_input("Do you like Python? (yes/no): ")

print(f"\nAge: {user_age}")
print(f"Height: {user_height}m")
print(f"Likes Python: {likes_python}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Simple Calculator
print("Example 1: Simple Calculator")
def simple_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        else:
            print("Invalid operation!")
            return

        print(f"Result: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

simple_calculator()
print()

# Example 2: User Profile
print("Example 2: User Profile Creator")
def create_user_profile():
    print("Creating your profile...")
    profile = {}

    profile['name'] = input("Full name: ")
    profile['age'] = get_integer_input("Age: ")
    profile['city'] = input("City: ")
    profile['occupation'] = input("Occupation: ")

    print("\n--- USER PROFILE ---")
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"City: {profile['city']}")
    print(f"Occupation: {profile['occupation']}")
    return profile

user_profile = create_user_profile()
print()

# Example 3: Number Guessing Game
print("Example 3: Number Guessing Game")
import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("I'm thinking of a number between 1 and 100!")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.")

        except ValueError:
            print("Please enter a valid number!")

    print(f"Game over! The number was {secret_number}")

number_guessing_game()
print()

# INPUT VALIDATION TECHNIQUES
print("=== INPUT VALIDATION TECHNIQUES ===\n")

def validate_email(email):
    """Simple email validation"""
    return '@' in email and '.' in email

def validate_phone(phone):
    """Simple phone validation"""
    return phone.replace('-', '').replace(' ', '').isdigit()

def get_validated_input(prompt, validator, error_message):
    """Generic validation function"""
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        print(error_message)

# Using validation
print("Input Validation Examples:")
email = get_validated_input(
    "Enter your email: ",
    validate_email,
    "Please enter a valid email address (must contain @ and .)"
)

phone = get_validated_input(
    "Enter your phone number: ",
    validate_phone,
    "Please enter a valid phone number (digits only, spaces/hyphens ok)"
)

print(f"Email: {email}")
print(f"Phone: {phone}")
print()

# MENU SYSTEM
print("=== MENU SYSTEM EXAMPLE ===\n")

def display_menu():
    print("--- MAIN MENU ---")
    print("1. Calculate area of rectangle")
    print("2. Calculate area of circle")
    print("3. Convert temperature")
    print("4. Exit")

def menu_system():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            length = get_float_input("Enter length: ")
            width = get_float_input("Enter width: ")
            area = length * width
            print(f"Rectangle area: {area}")

        elif choice == '2':
            radius = get_float_input("Enter radius: ")
            area = 3.14159 * radius ** 2
            print(f"Circle area: {area:.2f}")

        elif choice == '3':
            temp = get_float_input("Enter temperature in Celsius: ")
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp}°C = {fahrenheit}°F")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-4.")

        input("\nPress Enter to continue...")
        print()

menu_system()

# TIPS AND BEST PRACTICES
print("\n=== TIPS AND BEST PRACTICES ===")
print("1. Always validate user input")
print("2. Use try-except for type conversions")
print("3. Provide clear prompts and error messages")
print("4. Strip whitespace with .strip()")
print("5. Convert to appropriate case with .lower() or .upper()")
print("6. Use functions for reusable input validation")
print("7. Consider using loops for repeated input requests")
print("8. Handle edge cases (empty input, special characters)")
print()

# COMMON INPUT PATTERNS
print("=== COMMON INPUT PATTERNS ===")

# Pattern 1: Input with default value
def input_with_default(prompt, default):
    user_input = input(f"{prompt} [default: {default}]: ").strip()
    return user_input if user_input else default

country = input_with_default("Enter your country", "Unknown")
print(f"Country: {country}")

# Pattern 2: Input from list of options
def input_from_options(prompt, options):
    while True:
        print(f"{prompt}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter choice number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")

favorite_color = input_from_options(
    "Choose your favorite color:",
    ["Red", "Blue", "Green", "Yellow", "Purple"]
)
print(f"Favorite color: {favorite_color}")

print("\n=== INPUT TUTORIAL COMPLETE ===")
print("You now know how to handle user input in Python!")