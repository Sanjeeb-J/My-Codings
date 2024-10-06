name = input("What is your name? ").strip().title()

#Split users name in to first and last name
first, last = name.split()

print(f"Hello, {first}")