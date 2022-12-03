with open("input.txt", "r") as f:
    data = f.read()

# split data into list by line breaks
elfs = data.split("\n\n")

calories_per_elf = []

for elf in elfs:
    food_items = elf.split("\n")
    total_calorie = 0
    for food in food_items:
        total_calorie += int(food)
    calories_per_elf.append(total_calorie)

calories_per_elf_sorted = sorted(calories_per_elf)
top_3_elfs = calories_per_elf_sorted[-3:]
print(sum(top_3_elfs))
