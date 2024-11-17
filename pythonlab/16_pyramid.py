 #pyramid-4 
n = 10 
for i in range(1,n+1): 
   for j in range(1, n-i+1): 
       print(" ",end = "") 
   for k in range(1,i+1): 
       print(k,end = "") 
   for m in range(i-1,0,-1): 
       print(m,end = "") 
    
   print()

n = 10 
# Outer loop for each row of the pyramid 
for i in range(n, 0, -1): 
    
   # Inner loop to print leading spaces 
   for j in range(n - i): 
       print(" ", end="")  # Adds spaces to shift numbers to the right 
   # Inner loop to print increasing numbers in the current row 
   for k in range(1, i + 1): 
       print(k, end="")  # Prints increasing numbers starting from 1 up to i 
    
   # Inner loop to print decreasing numbers in the current row 
   for m in range(i - 1, 0, -1): 
       print(m, end="")  # Prints decreasing numbers starting from i-1 down to 1 
   # Move to the next line after completing a row 
   print()