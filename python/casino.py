#import libraries or packages
import os
from random import randint
#declare and initialize variables and/or constants
lives = 3
dice1 = 0
dice2 = 0  
roll_count = 0
equal_count = 0
dices_add = 0
acum_dices = 0
status = True
player_lives = 3


#functions
def rollDices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2




#main
print(":::::welcome to the casino:::::")
press_key = input("\npress any key to strart the game :::")
while status:
    os.system("cls")
    dices = rollDices()
    roll_count += 1
    dices_add = 0
    print("#" * 20)
    print(f"roll dices N°: {roll_count}")
    print("#" * 20)
    print(f"player lives: {player_lives}")

    if acum_dices >14:
        dicex = dices[randint(0, 1)]
        print(f"dice: {dicesx}")
        acum_dices += dicex
    else:
        print(f"dice 1: {dices[0]}")
        print(f"dice 2: {dices[1]}")
        dices_add = dices[0] + dices[1]
        acum_dices += dices_add

    if acum_dices >=20:
        print("::: congratulations you´ve win the game :::")
        break
    
    if dices_add%2 != 0:
        player_lives -= 1
        print(f"you lose a life, you have {player_lives} lives ")
        if player_lives == 0:
            print(":::game over:::")
            break

    
    if (dices[0] == 6 and dices[1] == 6) or (dices[0] == 1 and dices[1] == 1):
        player_lives += 1
        print(":::you´ve win a life:::")

    print(f"dices addition (current roll): {dices_add}")
    print(f"dices acum: {acum_dices}")


    print(f"dices addition: {dices_add}")

    
    if player_lives == 0:
        print(":::game over:::")
        print(f"total roll count: {roll_count}")
        break
    else:
        press_key = input("\npress any key to roll the dices again")