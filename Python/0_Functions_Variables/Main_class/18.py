def main():
    Hello()
    name = input("What is your name? ")
    Hello(name)

def Hello(to="World"):
    print("Hello,", to)

main()

"""
first you define the main function, but you are not printed
inside main you put the hello but hello is not function over there
so in next line you define the hello function
and finally printed the main function
"""