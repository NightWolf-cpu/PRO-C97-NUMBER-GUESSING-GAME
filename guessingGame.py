import random
guess=random.randint(1,9)
chance=1

while chance<=5:
    userGuess=int(input("Guess Any Number Between (1-9): "))
    if(guess==userGuess):
        print("YOU WON")
        break
    elif(chance<5):
        print("Try Again")
        chance=chance+1
    else:
        break

if(guess!=userGuess):
    print("You Lost The Number is: ",guess)
