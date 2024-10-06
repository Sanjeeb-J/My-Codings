try:
    x = int(input("What is x ? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

"""
Here we have a NameError
"""