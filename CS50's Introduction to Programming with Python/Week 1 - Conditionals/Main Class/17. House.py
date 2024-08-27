name = input("What is your name?")

match name:
    case "Sajeeb" | "Adith" | "Akashy":
        print("Kodoth")
    case "Abhi":
        print("Erumakulam")
    case _:
        print("Who?")