try:
    x = int(input("What is x ? "))
except ValueError:
    print("x is not an integer")

# Debug name error
else:
    print(f"x is {x}")