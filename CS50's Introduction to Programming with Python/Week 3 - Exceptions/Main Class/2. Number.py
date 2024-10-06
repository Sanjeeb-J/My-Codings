try:
    x = int(input("What is x ? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

"""
try & except - If you want to try to do something in python you can literally use this key word and you can check whether or not exceptional
               ie, You can try to do something except there something goes wrong do something else instead
"""