# Escape Sequence Characters in Python

print("=== ESCAPE SEQUENCE CHARACTERS ===")
print()

# 1. NEWLINE (\n)
print("1. Newline (\\n):")
print("First line\nSecond line\nThird line")
print()

# 2. TAB (\t)
print("2. Tab (\\t):")
print("Name:\tJohn")
print("Age:\t25")
print("City:\tNew York")
print()

# 3. BACKSLASH (\\)
print("3. Backslash (\\\\):")
print("This is a backslash: \\")
print("File path: C:\\Users\\Documents\\file.txt")
print()

# 4. SINGLE QUOTE (\')
print("4. Single Quote (\\'):")
print('It\'s a beautiful day!')
print("She said, 'Hello there!'")
print()

# 5. DOUBLE QUOTE (\")
print("5. Double Quote (\\\"):")
print("He said, \"How are you?\"")
print('The book title is "Python Programming"')
print()

# 6. CARRIAGE RETURN (\r)
print("6. Carriage Return (\\r):")
print("Loading", end="")
for i in range(5):
    print(f"\rLoading{'.' * (i + 1)}", end="")
print("\rComplete!     ")
# The f-string formats the output as "Loading" followed by the dots.
# \r is a carriage return, which moves the cursor back to the beginning of the line, so each output overwrites the previous one on the same
print()

# 7. BACKSPACE (\b)
print("7. Backspace (\\b):")
print("Hello\b World")  # Removes 'o' before 'W'
print()

# 8. FORM FEED (\f)
print("8. Form Feed (\\f):")
print("Before form feed\fAfter form feed")
print()

# 9. VERTICAL TAB (\v)
print("9. Vertical Tab (\\v):")
print("Before vertical tab\vAfter vertical tab")
print()

# 10. NULL CHARACTER (\0)
print("10. Null Character (\\0):")
print("Text with null\0character")
print()

# 11. OCTAL REPRESENTATION (\ooo)
print("11. Octal representation (\\ooo):")
print("\101\102\103")  # ABC in octal
print()

# 12. HEXADECIMAL REPRESENTATION (\xhh)
print("12. Hexadecimal representation (\\xhh):")
print("\x41\x42\x43")  # ABC in hexadecimal
print()

# 13. UNICODE REPRESENTATION (\uxxxx and \Uxxxxxxxx)
print("13. Unicode representation:")
print("Heart: \u2764")  # ❤
print("Smiley: \u263A")  # ☺
print("Copyright: \u00A9")  # ©
print("Star: \U00002B50")  # ⭐
print()

# 14. RAW STRINGS (r"" or r'')
print("14. Raw strings (no escape processing):")
regular_string = "C:\\Users\\Documents\\file.txt"
raw_string = r"C:\Users\Documents\file.txt"
print(f"Regular: {regular_string}")
print(f"Raw: {raw_string}")
print()

# 15. TRIPLE QUOTES FOR MULTILINE STRINGS
print("15. Triple quotes (multiline strings):")
multiline = """This is a multiline string
that can contain "quotes" and 'apostrophes'
without escaping them."""
print(multiline)
print()

# 16. PRACTICAL EXAMPLES
print("16. Practical Examples:")

# JSON-like string
json_data = "{\"name\": \"John\", \"age\": 30}"
print(f"JSON string: {json_data}")

# HTML content
html = "<div class=\"container\">\n\t<h1>Welcome</h1>\n</div>"
print(f"HTML:\n{html}")

# File path handling
windows_path = "C:\\Program Files\\Python\\python.exe"
unix_path = "/usr/local/bin/python"
print(f"Windows path: {windows_path}")
print(f"Unix path: {unix_path}")

# Special characters in output
print("Creating a box:")
print("┌─────────────┐")
print("│ Hello World │")
print("└─────────────┘")
print()

# 17. ESCAPE SEQUENCE REFERENCE TABLE
print("17. Escape Sequence Reference:")
print("\\n  - Newline")
print("\\t  - Tab")
print("\\\\  - Backslash")
print("\\'  - Single quote")
print("\\\"  - Double quote")
print("\\r  - Carriage return")
print("\\b  - Backspace")
print("\\f  - Form feed")
print("\\v  - Vertical tab")
print("\\0  - Null character")
print("\\ooo - Octal value")
print("\\xhh - Hexadecimal value")
print("\\uxxxx - Unicode 16-bit")
print("\\Uxxxxxxxx - Unicode 32-bit")