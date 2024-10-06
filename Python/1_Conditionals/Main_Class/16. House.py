name = input("What is your name? ")

match name:
    case "Sanjeeb":
        print("Kodoth")
    case "Adith":
        print("Kodoth")
    case "Abhi":
        print("Erumakulam")
    # _ means anything other than above, from my understating
    case _:
        print("Who?")