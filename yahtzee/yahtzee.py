dice = [1,3,3,2,5]

scorecard = {
    "ones": 0,
    "twos": 0,
    "threes": 0,
    "fours": 0,
    "fives": 0,
    "sixes": 0,
    "three of a kind": 0,
    "four of a kind": 0,
    "full house": 0,
    "small straight": 0,
    "large straight": 0,
    "chance": 0
}

score = 0

choice = 3

for die in dice:
    if die == choice:
        score += die

    if choice == 1:
        scorecard["ones"] = score
    elif choice == 2:
        scorecard["twos"] = score
    elif choice == 3:
        scorecard["threes"] = score
    elif choice == 4:
        scorecard["fours"] = score
    elif choice == 5:
        scorecard["fives"] = score
    elif choice == 6:
        scorecard["sixes"] = score

print(scorecard)