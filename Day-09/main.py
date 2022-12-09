from art import logo
import os

print(logo)

print("Welcome to the secret auction program.")

bid_dic = {}

def highest_bid(dic):
    highest = 0
    winner = ""
    for key in dic:
        bid_amount = dic[key]
        if bid_amount > highest:
            highest = bid_amount
            winner = key
    
    print(f"The winner is {winner} with a bid of ${highest}")

while(True):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    bid_dic[name] = bid
    
    option = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if option == "no":  
        highest_bid(bid_dic)    
        break
    elif option != "yes":
        print("Entrada inválida!")
        break
    else:
        os.system('cls')
