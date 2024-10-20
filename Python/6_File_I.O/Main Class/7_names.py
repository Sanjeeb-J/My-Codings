# If you want to read a file you don't want to put r 
# file is a variable
with open("name.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())
