"""
Your module description

my psudocode
OUTPUT Welcome to Guess the Number!
OUTPUT The rules are simple. I will think of a number, and you will try to guess it.
number = RANDOM RANDINT 1-10

isguessright EQUALS FALSE

WHILE isguessright ISNOT EQUAL TRUE
    guess = INPUT Guess a number between 1 and 10: 
    IF guess EQUALS number
        OUTPUT You guessed {}. That is correct! You win!
        isguessright EQUALS TRUE
    ELSE
        OUTPUT You guessed {}. Sorry, that isn’t it. Try again.
"""
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))