from random import randint

#functions
def roll_dice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2


dices = roll_dice()
print(f"dice 1: {dices[0]}")
print(f"dice 2: {dices[1]}")


if dices[0] == dices[1]:
    print("you´ve win")
else:
    print("try again !!!")
