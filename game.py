import random
number = random.randint(1, 9)
gameOver = False
chances = 5

while chances < 5 & gameOver == False:
    guess = int(input("enter a number between 1 and 9"))

    if guess == number:
        compareAnswer = "Right"
        gameOver = True
    elif guess > number:
        compareAnswer = "High"
    elif guess < number:
        compareAnswer = "Low"

    if compareAnswer == "Right":
        print("Congratulations, You Win!")
    elif compareAnswer == "High":
        print("Your answer is too high, try again!")
    elif compareAnswer == "Low":
        print("Your answer is too low, try again!")

    if chances > 5:
        print("Game Over!")
        gameOver = True
