name = input("What is your name? ")

"""
str
docs.python.org/3/library/stdtypes.html#string-methods
"""

# Remove white space from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

print(f"Hello, {name}")