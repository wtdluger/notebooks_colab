'''
2 dice piggy game 
[["Player 1" total_score round_score ]
 ["Player 2" total_score round_score ]
 ...
 ["Player n" total_score round_score ]]
 
Rules
* Two standard dice are rolled. If neither shows a 1, their sum is added to the turn total.
* If a single 1 is rolled, the player scores nothing and the turn ends.
* If two 1s are rolled, the player’s entire score is lost, and the turn ends.
* If a double is rolled, the point total is added to the turn total as with any roll but the player is obligated to roll again (possible sub-variation of the two-dice game)

'''
import math
import random
import numpy

# Initial Setup
print("Welcome to this 2-Dice Piggy Game.")
num_players = int(input("How many players?"))
theMatrix = numpy.empty((num_players + 1, 3), dtype = object)
theMatrix[0] = ["Names", "Total Score", "Round Score"]
for i in range (1, num_players + 1):
    theMatrix[i][0] = input("What is the name of player " + str(i) + "? ") # Player's Name
    theMatrix[i][1] = 0 # Player's Total Score
    theMatrix[i][2] = 0 # Player's Turn Score

print(" ")
print("Let's Begin")
its_on = True
j = 1
while its_on == True:
    roll = [int(math.floor( 6*random.random() + 1 )), int(math.floor( 6*random.random() + 1 ))] # roll 2D6, store rolls as a list of 2 integers
    print(theMatrix[j][0] + " rolled a: ")
    print(roll)

    if roll[0] == 1 and roll[1] == 1:
        theMatrix[j][2] = 0 # Set Turn Score to 0
        theMatrix[j][1] = 0 # Set Total Score to 0
        print("The standings are now: ")
        print(theMatrix)
        input(theMatrix[j][0] + ", your turn is over. Press any key to let the next player roll...")
        j +=1
        choice = "N"
    elif roll[0] == 1 or roll[1] == 1:
        theMatrix[j][2] = 0 # Set Turn Score to 0
        print("The standings are now: ")
        print(theMatrix)
        input(theMatrix[j][0] + ", your turn is over. Press any key to let the next player roll...")
        j += 1
        choice = "N"
    else:
        theMatrix[j][2] = int(theMatrix[j][2]) + roll[0] + roll[1] # Add rolls to turn score    
        print("The standings are now: ")
        print(theMatrix)
        choice = input(theMatrix[j][0] + ", would you like to roll again, 'Y' or 'N'?")
        if choice == "N": #End Turn
            theMatrix[j][1] = int(theMatrix[j][1]) + int(theMatrix[j][2])
            theMatrix[j][2] = 0
            j += 1
        elif choice == "Y":
            print(" ")
        else:
            print("You are rolling again.")

    if j == num_players + 1:
        # check if any Player reached the maximum score
        for i in range(1, num_players + 1):
            if int(theMatrix[i][1]) >= 10:
                print(theMatrix[i][0] + " has won the game.")
                its_on = False
        # reset turn counter to 0 to begin another round of turns
        j = 1


# https://en.wikipedia.org/wiki/Pig_(dice_game)