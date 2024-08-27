distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    # .keys helps to return all the keys in our dictionary
    for name in distances.keys():
        print(f"{name} is {distances[name]} Au from the Earth")

main()