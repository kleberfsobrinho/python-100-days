from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    elif b_followers > a_followers:
        return guess == "B"

score = 0

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
B = random.choice(data)

while True:
    A = B
    B = random.choice(data)
    while A == B:
        B = random.choice(data)

    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")

    guess = input("Who was more followers? Type 'A' or 'B': ").upper()

    a_follower_count = A['follower_count']
    b_follower_count = B['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    

