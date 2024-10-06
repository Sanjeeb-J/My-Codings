answer = input("Greeting: ").lower()

def main():
    #Check answer has hello
    if "hello" in answer:
        print("$0")
    #Check answer has h
    elif answer[0] == "h":
        print("$20")
    #Otherwise
    else:
        print("$100")
main()
