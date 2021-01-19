dice = [1, 3, 2, 2, 2]

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


# calculate top half of scorecard
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




#calculate three of a kind
choice_1 = "three of a kind"
score_1 = 0

if choice_1 == "three of a kind":

    for die in dice:
        if dice.count(die) >= 3:
            scorecard["three of a kind"] = sum(dice)
            break


#calculate four of a kind
choice_2 = "four of a kind"
score_2 = 0

if choice_2 == "four of a kind":

    for die in dice:
        if dice.count(die) >= 4:
            scorecard["four of a kind"] = sum(dice)
            break


# calculate score for full house
choice_3 = "full house"
check = [0, 0]

if choice_3 == "full house":
    for die in dice:
        if dice.count(die) == 2:
            check[0] = 2
        elif dice.count(die) == 3:
            check[1] = 3

    if check == [2, 3]:
        scorecard["full house"] = 25


dice_2 = [6, 3, 2, 4, 1]
dice_4 = [2, 4, 3, 3, 5]


dice_4.sort()
check = [dice_4[0]]
print(dice_4)
i = 0
ind = 0

while ind < (len(dice_4) - 1):
    print(ind, "test")
    
    if dice[ind] == (check[i] + 1):
        print(i, ind , "loop")
        check.append(dice_4[ind])
        i += 1
        ind += 1
    else: 
        ind += 1
        i += 1
        print(i , ind , "loop2")
        continue
    
    
    


print(check)