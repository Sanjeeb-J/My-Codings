# Sum of factorials from 1 to n!

n = int(input("Enter a positive integer n: "))
sum = 0
for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    sum += factorial
print(f"The sum of factorials from 1! to {n}! is: {sum}")