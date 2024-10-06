# Now you can add names into you don't need to copy and paste again and again

def main():
    name = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(name)):
        print(write_letter(name[i], "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},
    
    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
"""

main()