# Get user input
camelCase = input("camelCase: ")

# Loop through every letter
for letter in camelCase:

    # Check if letter is upper case
    if letter.isupper():
        # Print underscores and the letter in lowercase
        print("_" + letter.lower(), end="")

    # Otherwise, print letter
    else:
        print(letter, end="")
# Print space in the end
print()
