import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear
paint_calc(height, width, cover):
    number_of_cans = (height*width)/cover
    print(f'You\'ll need {number_of_cans} cans of   paint.')

chosen_word = random.choice(word_list)
display = []
end_of_game = False
lives = 6

for letter in chosen_word:
    display.append("_")

print(logo)
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f'You\'ve already guessed {guess}')
    else:
        for letter_id in range(len(chosen_word)):
            if chosen_word[letter_id] == guess:
                display[letter_id] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f'The letter {guess} isn\'t in the word')
        print(stages[lives])

    print(display)

    if lives < 1:
        print("You lose.")
        end_of_game = True
    if not "_" in display:
        print('You win!')
        end_of_game = True
