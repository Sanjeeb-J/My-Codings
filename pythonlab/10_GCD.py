# GCD of Two numbers

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
while b:
    a,b = b, a%b
print("GCD=", a)