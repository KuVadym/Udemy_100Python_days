############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random

print(logo)
print('Welcome to the 21 game!')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card():
    return int(random.choice(cards))


def end_game(more_game):
    if more_game == 'y':
        return start_game()
    else:
        return print("Goodbuy!")
      

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose! Computer  has Blackjack!"
    elif user_score == 0:
        return "You win with Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif computer_score > user_score:
        return "Computer win!"
    else:
        return "You win"

    

def start_game():
    computer_cards = [random_card(), random_card()]
    game = True
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random_card())
    print(f'computer first card {computer_cards[0]}')
    gamer_cards = [random_card(), random_card()]
    print(f'You have {gamer_cards}')
    azart = True
    while azart == True:
        more_card = input('Do you want get one more card? y/n\n')
        if more_card == 'y':
            gamer_cards.append(random_card())
            print(f'You have {gamer_cards}')
            if calculate_score(gamer_cards) > 21:
              azart = False
        else:
            azart = False
    result = compare(calculate_score(gamer_cards), calculate_score(computer_cards))
    print(result)
    one_more_game = input("Do you wnt play one more time? y/n\n")
    if one_more_game == "y":
        start_game()
    else:
        print("goodbay!")

start_game()
