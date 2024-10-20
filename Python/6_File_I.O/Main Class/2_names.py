name = input("What is your name? ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()

# You hove to close the file at the end otherwise gets corrupted
# Or you can use with