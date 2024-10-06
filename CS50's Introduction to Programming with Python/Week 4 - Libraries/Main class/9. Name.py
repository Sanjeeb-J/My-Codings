import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("Hello, my name is", arg)

# Here it print the the 0 also, so that is a problem
# In order to solve that you can slice the arg/sys (check it out in next page)