results = ["Mario", "Luigi","Princess","Yoshi", "Koopa Troopa", "Toad", "Browser", "Donkey Kong Jr"]

# If you want remove any element from your list use ".remove"
results.remove("Browser")
# When you use ".append" you're adding the element at the end of the list
# Use ".insert" if you want to add a particular element at a particular position
results.insert(0, "Browser")
# If you want to flip the whole list use ".reverse"
results.reverse()

print(results)