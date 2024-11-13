# Prime number or not (while loop with else)

num = int(input("Enter a number: "))
if num > 1:
  divisor=2
  while divisor <= int(num**0.5):
    if num % divisor == 0:
      print(num, "is not a prime number.")
      break
    divisor +=1
  else:
    print(num, "is a prime number.")
else:
  print(num, "is not a prime number.")