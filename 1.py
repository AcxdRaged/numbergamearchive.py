#By SpaceAxolotl and AcxdRaged
#Import needed stuffs
import random
import time

#Define needed stuffs
Infinite = 999999999999999999
playAgain = "Y"
myName = 'None'
playerGuess = 0
playerGuesses = 10
guessesUsed = 0
myNumber = random.randint(1,101)

#Start the game
print('What is your name')
myName = input()
time.sleep(1)
print('Well', myName, 'I am thinking of a number between 1 and 100')
time.sleep(1)
print('Can you guess what it is?')

def Game():
    while Infinite >= 1:
        print("")
        global guessesUsed
        global myNumber
        playerGuess = input()
        guessesUsed = guessesUsed + 1

	    #tells the player if the number is too high
        if int(playerGuess) > myNumber:
            print("Too high, try again")

        #or too low
        elif int(playerGuess) < myNumber:
	        print('Too low, try again')

	    #or correct
        elif int(playerGuess) == myNumber :
            print('Good Job!')
            break

        if guessesUsed > playerGuesses:
            print('Your bad at this')
            break


    playAgain = input('Would you like to play again Y/N')
    if playAgain == 'Y':
        myNumber = random.randint(1,101)
        guessesUsed = 0
        Game()

Game()
