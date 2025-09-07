#Strings are immutable, that means they cannot be changed after they are created.
#Strings can be defined using single quotes, double quotes or triple quotes. 
string = "Hello, World!"
string1 = '!Hello, World!!'
string3 = """Hello, World!D B X 
bbjnA ;L
 ASDBASNDL
 BNj
 SJsaV


"""
string3 = '''Hello, World!D B X 
bbjnA ;L
 ASDBASNDL
 BNj
 SJsaV

'''
print (string)
print(len(string))
print (string[0])  # First character
print (string[2:5])  # Characters from position 2 to 4 
print (string[2:len(string)-1 ])  # Characters from position 2 to end of the string 
print (string[2:])  # Characters from position 2 to end
print (string * 2)  # String repetition (string will be printed twice)
print(string1.strip("!"))    # Remove leading/trailing characters
print(string.lstrip("H"))  # Remove leading characters
print(string.rstrip("!"))  # Remove trailing characters
print(string.lower())  # Convert to lowercase
print(string.upper())  # Convert to uppercase   
print(string.replace("!", "?"))  # Replace substring
print(string.split(","))  # Split string into a list
print(capitalize(string))  # Capitalize first character
print(string3.center(50))  # Center string with padding
print(string3.count("A"))  # Count occurrences of substring
print(string3.encode())  # Encode string to bytes
print(string3.endswith("V"))  # Check if string ends with substring 
print(string.startswith("H"))  # Check if string starts with substring
print(string3.find("World"))  # Find substring index
print(string3.index("World"))  # Find substring index (raises error if not found(stops program), while find() returns -1 and poceeds) 
print(string3.isalnum())  # Check if all characters are alphanumeric
print(string3.isalpha())  # Check if all characters are alphabetic
print(string3.isdigit())  # Check if all characters are digits
print(string3.isspace())  # Check if all characters are whitespace
print(string3.istitle())  # Check if string is titlecased
print(string3.isupper())  # Check if all characters are uppercase
print(string3.islower())  # Check if all characters are lowercase
print(string3.startswith("Hello"))  # Check if string starts with substring 
print(string3.swapcase())  # Swap case of characters lower to upper and vice versa
print(string3.title())  # Convert to title case 
print(string3.zfill(100))  # Pad string with zeros on the left to a total width

print(string3)  # Original string remains unchanged