import random

cards = ["jack", "queen", "king"]

def main():
    card = random.choices(cards, weights=[75, 25, 5], k=2)
    print(card)

main()

# You can change the priority of each cards over here