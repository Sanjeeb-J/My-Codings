import random

cards = ["jack", "queen", "king"]

def main():
    card = random.sample(cards, k=2)
    print(card)

main()

# Here we get 2 distinct cards