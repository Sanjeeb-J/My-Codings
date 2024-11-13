# GCD of Two numbers

print("Enter two numbers")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
while (b>0):
    r = a % b
    a = b
    b = r
print("GCD=", a)