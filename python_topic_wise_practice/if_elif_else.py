print("Try if else condition")

# Basic if-else example
number = 5

if number > 10:
    print("Number is greater than 10")
elif number > 0:
    print("Number is positive but not greater than 10")
    if number == 5:
        print("Number is zero")
else:
    print("Number is zero or negative")

# Another example with different conditions
age = 25

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
