score = int(input("Score: "))

if score > 100:
    print("Please enter your mark out of 100")
elif score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
elif score >=60:
    print("Grade: D")
elif score <60:
    print("Grade: F")