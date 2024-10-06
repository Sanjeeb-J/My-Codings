def main():
    name = input("What is your name? ")
    Hello()

def Hello():
    print("Hello,", name)

main()

"""
This is scope which means the name input is only defined in the main function
name is not defined in hello function
"""