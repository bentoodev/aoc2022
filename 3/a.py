# read data from input.txt
with open("input.txt", "r") as f:
    data = f.read()

rucksacks = data.split("\n")

priority = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
dupe_items = []

for rucksack in rucksacks:
    compartment_length = int(len(rucksack) / 2)
    compartments = [rucksack[compartment_length:], rucksack[:compartment_length]]
    # find character that appears in both compartments
    for char in compartments[0]:
        if char in compartments[1]:
            dupe_items.append(char)
            break

sum_of_priorities = 0
for item in dupe_items:
    # find the index of the item in the priority list
    sum_of_priorities += priority.index(item) + 1

print(sum_of_priorities)
