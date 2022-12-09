# Rules 

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    sum_cards = sum(cards)

    if sum_cards == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum_cards > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum_cards

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif player_score == 0:
        return "Win with a Blackjack "
    elif player_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win "
    elif player_score > computer_score:
        return "You win "
    else:
        return "You lose "

def play_game():
    print(logo)

    player_hand = []
    computer_hand = []
    
    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while True:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        
        print(f"\tYour cards: {player_hand}, current score: {player_score}")
        print(f"\tComputer's first card: {computer_hand[0]}")

        if computer_score == 0 or player_score == 0 or player_score > 21:
            break
        
        option = input("Type 'y' to get another card, type 'n' to pass: ")
        if option == 'n':
            break
        elif option == 'y':
            player_hand.append(deal_card())
        
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"\tYour final hand: {player_hand}, final score: {player_score}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))
    
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
