# Number Guessing Game
# Guess the number within 10 attempts to win using the hints given after every wrong attempts.

import random
print("")
print("GUESS THE NUMBER BETWEEN 1 & 100")
print("You have 5 attempts to Guess")
print("------------------------------------")
print("")

r= random.randint(1,100)
#print(r)     #Remove This Line after program testing

for i in range(1,7):

    if i<6:
        print("|| This is your attempt no.",i,"||")
        a= int(input("Guess Any Number: "))

        if a<r:
            print("Guess Higher")
        elif a>r:
            print("Guess lower")
        else:
            print("Right Guess")
            print("COngrats! You Successfully Guessed in",i,"Attempts.")
            break
    else:
        print("")
        print("SOORY, The number is",r)
        print("You Lost all your Attempts")
        print("  |||=  GAME OVER  =|||  ")

input("\nPress ENTER to Continue...")
