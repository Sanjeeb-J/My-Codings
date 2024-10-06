# If you want create a loop that only break when it is True
while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")