name = input("What is your name? ")

# file is a variable

with open("name.txt", "a") as file:
    file.write(f"{name}\n")