# Pyramid 5

n = 10
for i in range(n, 0, -1):
  for j in range(1, n-i+1):
    print(" ", end="")
  for k in range(1, i+1):
    print(k, end="")
  for m in range(i-1, 0, -1):
    print(m, end="")
  print()