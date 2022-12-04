# read data from input.txt
with open("input.txt", "r") as f:
    data = f.read()

rucksacks = data.split("\n")
# each group is 3 lines long
groups = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

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
badges = []

for group in groups:
    # find character that appears in all three strings in the group
    for char in group[0]:
        if char in group[1] and char in group[2]:
            badges.append(char)
            break


sum_of_priorities = 0
for badge in badges:
    # find the index of the item in the priority list
    sum_of_priorities += priority.index(badge) + 1

print(sum_of_priorities)
