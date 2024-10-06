print("What is 100/2?")
def get_guess():
    guess = input("Enter your guess:")
    return guess

def main():
    guess = get_guess()
    if guess == 'fifty':
        print("Congratulations! You guessed the correct number.", end=" ")
    else:
        print("Sorry, you guessed incorrectly.")
        print("The correct number is fifty.")

main()

#When you put that into ' ' it is a string
