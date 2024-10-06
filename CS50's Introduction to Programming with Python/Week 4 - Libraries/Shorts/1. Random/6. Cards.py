import random

cards = ["jack", "queen", "king"]

def main():
    random.seed(0)
    card = random.choices(cards, k=2)
    print(card)

main()

# Using seed give consistent randomness
# You can use seed to debug you program