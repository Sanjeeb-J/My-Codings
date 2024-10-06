import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)

# Here it print the the 0 also, so that is a problem
# Use Slice [1:]