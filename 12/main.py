#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

EASY_LEVEL = 10 
HARD_LEVEL = 5
print(logo)
print("Welcome to the Number Guessing Game!")

def diff():
    difficulty = input("Choose a difficulty. Type easy or hard.: ")
    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL

def compare(guess, number):
    if guess == number:
        return f"You win! Correct answer {guess}"
    elif guess > number:
        return "Too hight."
    elif guess < number:
        return "Too low."


def game():
    attemts = diff()
    number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100")
    lives = True
    while lives:
        print(f"You have {attemts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = compare(guess, number)
        print(result)
        attemts -= 1
        if result == f"You win! Correct answer {guess}":
            lives = False
        elif attemts == 0 and lives == True:
            print("Game over You lose")
            lives = False


game()
