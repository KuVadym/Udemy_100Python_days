import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "pear", "melon"]
chosen_word = random.choice(word_list)
display = []
end_of_game = False
lives = 6

for letter in chosen_word:
    display.append("_")


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for letter_id in range(len(chosen_word)):
        if chosen_word[letter_id] == guess:
            display[letter_id] = guess

    if guess in chosen_word:
        print(stages[lives])
    else:
        lives -= 1
        print(stages[lives])

    print(display)

    if lives < 1:
        print("You lose.")
        end_of_game = True
    if not "_" in display:
        print('You win!')
        end_of_game = True
