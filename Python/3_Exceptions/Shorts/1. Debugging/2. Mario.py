def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i, end=" ")
        print("#" * i)

if __name__ == "__main__":
    main()

"""
Care full because here i starts from 0
"""