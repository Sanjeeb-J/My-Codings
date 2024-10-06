def main():
    mood = input()
    if ":)" in mood:
        mood = mood.replace(":)", "🙂")
    if ":(" in mood:
        mood = mood.replace(":(", "🙁")
    print(mood)
main()
