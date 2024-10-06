def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check 1st and 2nd character are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    has_digit = False

    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] == "0" and not has_digit:
                return False
            has_digit = True
        elif has_digit:  # If a letter appears after a digit
            return False
        elif not s[i].isalpha():  # Check for invalid characters
            return False

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in [' ', ',', '.', '?', '!']:
            return False

    # If we pass all the tests, return True
    return True

main()
