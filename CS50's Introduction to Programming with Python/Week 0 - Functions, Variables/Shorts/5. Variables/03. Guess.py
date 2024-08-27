print("What is 100/2? ", end="")
def get_guess():
    guess = int(input("Enter your guess:"))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Congratulations! You guessed the correct number.",end=" ")
    else:
        print("Sorry, you guessed incorrectly.")
        print("The correct number is 50.")
    print(guess)

main()
