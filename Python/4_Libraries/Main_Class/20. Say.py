import sys

from saying import goodbye

if len(sys.argv) ==2:
    goodbye(sys.argv[1])


# You have to use ( if __name__ == "__main__": ) in the file