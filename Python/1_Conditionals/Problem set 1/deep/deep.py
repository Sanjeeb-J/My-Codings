def main():
    deep = input("What is the answer to the Great Question of life, the Universe, and Everything? ")
    if deep.strip() == "42":
        print("Yes")
    elif deep.lower().strip() == "forty-two":
        print("Yes")
    elif deep.lower().strip() == "forty two":
        print("Yes")
    else:
        print("No")
main()
