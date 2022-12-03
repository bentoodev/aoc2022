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

    if round.split(" ")[1] == "X":
        me = "rock"
    elif round.split(" ")[1] == "Y":
        me = "paper"
    elif round.split(" ")[1] == "Z":
        me = "scissors"

    if me == "paper":
        round_score += 2
        if opponent == "paper":
            round_score += 3
        elif opponent == "rock":
            round_score += 6
    elif me == "rock":
        round_score += 1
        if opponent == "rock":
            round_score += 3
        elif opponent == "scissors":
            round_score += 6
    elif me == "scissors":
        round_score += 3
        if opponent == "scissors":
            round_score += 3
        elif opponent == "paper":
            round_score += 6

    total_score += round_score

print(total_score)
