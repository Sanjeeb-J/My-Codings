results = ["Mario", "Luigi"]

# If you want to add an element at the end of the list
# use ".append"

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# Add a list to a list don't use ".append" use ".extend"
results.append(["Browser", "Donkey Kong Jr"])
results.remove(["Browser", "Donkey Kong Jr"])
results.extend(["Browser", "Donkey Kong Jr"])

print(results)