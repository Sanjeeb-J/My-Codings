# "len" function - show the length of list
# [] is an empty list
# "dict" function (Dictionary)
# {} is an empty dictionary
# None - literally means nothing

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None },
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")