names = []

with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print("Hello,", name)

"""
sorted (iterable, /, *, key=None, reverse=Fa1se)
"""