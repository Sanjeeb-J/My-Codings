"""
docs.python.org/3/library/functions.html#round

round(number, ndigits=None)
round(number[, ndigits])
"""

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

z = round(x + y)
#for printing comma on the numbers 

print(f"{z:,}")

