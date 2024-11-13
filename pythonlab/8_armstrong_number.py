# Generate Armstrong Numbers

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Armstrong numbers between {start} and {end} are: ")
for num in range (start, end+1):
    num_of_digits = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_of_digits
        temp //= 10
    if sum == num:
        print(num, end=" ")