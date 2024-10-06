while True:
    try:
        x = int(input("What is x ? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")