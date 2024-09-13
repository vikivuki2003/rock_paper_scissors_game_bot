import random

def get_bot_choice():
    return random.choice(['Rock', 'Scissors', 'Paper'])

def get_winner(user_choice: str, bot_choice: str) -> str:
    rules = {'Paper': 'Rock',
             'Rock': 'Scissors',
             'Scissors': 'Paper'}
    if user_choice == bot_choice:
        return 'Nobody won'
    elif rules[user_choice] == bot_choice:
        return 'You won! Congratulations!'
    else:
        return 'I won!'
    
print(get_winner('Rock', 'Scissors'))