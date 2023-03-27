from art import logo, vs
from game_data import data
import random
import os





def compare(a, b):
  if a['follower_count'] > b['follower_count']:
      return 'a'
  else:
      return 'b'
    

a = random.choice(data)
b = random.choice(data)
print(a["name"])


score = 0
game_continue = True
while game_continue:
    if a == b:
        b = random.choice(data)
    print(logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}')
    choose = input("Who has more followers? Type 'A' or 'B': ")
    if choose.lower() == compare(a, b):
        score += 1
        print(f"You're right! Current score: {score}.")
        a = b
        b = random.choice(data)
        os.system('clear') # for Linux
        # os.system('cls') # for Windows
    else:
        print(f"Sorry, that's wrong.Final score {score}")
        game_continue = False
    
