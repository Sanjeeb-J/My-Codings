import random

cards = ["jack", "queen", "king"]

def main():
    card = random.choices(cards, k=2)
    print(card)

main()

# You have to change choice to choices
# The problem over here is 1st time select a card and put the card back in the same set
# So you get same card 2 times