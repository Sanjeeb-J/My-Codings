names = []

# If you want to read a file you don't want to put r 
# file is a variable
with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("Hello,", name)

"""
Here we are sorting the name in a list before printing 
"""