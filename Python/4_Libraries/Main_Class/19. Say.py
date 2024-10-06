import sys

from saying import hello

if len(sys.argv) ==2:
    hello(sys.argv[1])


# You have to use ( if __name__ == "__main__": ) in the file