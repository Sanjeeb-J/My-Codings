# Create list with the name of all months
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Loop forever
while True:
    # Get user input and remove leading/trailing whitespace
    date = input("Date: ").strip()

    try:
        # Try splitting the date by /
        month, day, year = date.split("/")
        month, day, year = month.strip(), day.strip(), year.strip()

        # Check if month is between 1 and 12 and day between 1 and 31
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        try:
            # Try splitting the date by space
            old_month, old_day, year = date.split(" ")
            old_month, old_day, year = old_month.strip(), old_day.strip(), year.strip()

            # Ensure that the day ends with a comma
            if not old_day.endswith(","):
                raise ValueError("Missing comma after day")

            # Find the number of the month
            month = None
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
                    break

            # Remove comma from day variable
            day = old_day.replace(",", "")

            # Check if month is between 1 and 12 and day between 1 and 31
            if (month is not None) and (1 <= int(day) <= 31):
                break
        except:
            # If the format is wrong, continue looping
            print("Invalid format. Please try again.")
            pass

# Ensure the month and day are in two-digit format
month = f"{int(month):02}"
day = f"{int(day):02}"

# Print the result in YYYY-MM-DD format
print(f"{year}-{month}-{day}")
