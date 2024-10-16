def main():
    name = input("What is your name? ")
    print(hello(name))

def hello(to="world"):
    """
    if you put like this 
    print("hello,",to)
    it is not returning anything
    """
    return f"hello, {to}"

if __name__ == "__main__":
    main()