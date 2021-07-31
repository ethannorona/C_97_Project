correctNumber = 21
chances = 5
print("Number Guessing Game")
print("Guess a number (between 1 and 35)")
while(chances != 0):
    guessedNumber = input("Enter Your Guess: ")
    if(int(guessedNumber) == 21):
        print("Congrates You Win")
        break
    elif(int(guessedNumber) <= 21):
        print("It's a number higher than " + guessedNumber)
        chances = chances - 1
    elif(int(guessedNumber) >= 21):
        print("It's a number lower than " + guessedNumber)
        chances = chances - 1
if(chances == 0):
    print("Game Over")
    print("You Lose")