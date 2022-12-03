# read data from input.txt
with open("input.txt", "r") as f:
    data = f.read()

rounds = data.split("\n")
total_score = 0
for round in rounds:
    round_score = 0

    if round.split(" ")[0] == "A":
        opponent = "rock"
    elif round.split(" ")[0] == "B":
        opponent = "paper"
    elif round.split(" ")[0] == "C":
        opponent = "scissors"

    ending = round.split(" ")[1]

    if ending == "X":
        if opponent == "rock":
            round_score += 3
        elif opponent == "paper":
            round_score += 1
        elif opponent == "scissors":
            round_score += 2
    elif ending == "Y":
        round_score += 3
        if opponent == "rock":
            round_score += 1
        elif opponent == "paper":
            round_score += 2
        elif opponent == "scissors":
            round_score += 3
    elif ending == "Z":
        round_score += 6
        if opponent == "rock":
            round_score += 2
        elif opponent == "paper":
            round_score += 3
        elif opponent == "scissors":
            round_score += 1

    total_score += round_score

print(total_score)
