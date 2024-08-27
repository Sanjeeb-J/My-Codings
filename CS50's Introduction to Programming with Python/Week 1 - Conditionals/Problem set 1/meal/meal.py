def main():
    ans = input("What time is it? ")
    time = convert(ans)
    if time>= 7 and time<= 8:
        print("breakfast time")
    elif time>=12 and time<=13:
        print("lunch time")
    elif time>=18 and time<=19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes)/60
    # return result to main function
    return float(hours) + new_minutes

if __name__ == "__main__":
    main()