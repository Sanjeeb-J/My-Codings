# Sum of 1 + (1+2) + (1+2+3) + ..... (1+2+3+...n)

n = int(input("Enter a positive integer n: "))
total_sum = 0
for i in range(1,n+1):
    partial_sum = 0
    for j in range(1, i+1):
        partial_sum +=j
    total_sum += partial_sum
print(f"The sum of the sequence 1 + (1+2) + (1+2+3) + ..... (1+2+3+...n) is: {total_sum}")