# 1. Makes 3 hot flavours
# Espresso (50ml Water 18g Coffee) => $1.50
# Latte (200ml Water 24g Coffee 150ml Milk) => $2.50
# Cappuccino (250ml Water 24g Coffee 100ml Milk) => $3.00
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Machine resource => 300ml Water, 200ml Milk, 100g Coffee

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 2. Coin Operated
# Penny => 1 cent
# Nickel => 5 cent
# Dime => 10 cent
# Quarter => 25 cent

# Program requirements
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee


def check_resource(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry that is not enough {ingredient}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total


def check_money(coffee_cost, coins_sum):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if coins_sum < coffee_cost:
        print("Sorry that's not enough money. Money refunded")
        return False

    change = round(coins_sum - coffee_cost, 2)
    print(f"Here is ${change} in change.")
    global money
    money += coffee_cost
    return True


def make_coffee(coffee_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    return f"Here is your {coffee_name} ☕. Enjoy!"


os.system('cls' if os.name == 'nt' else 'clear')
money = 0
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${money}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if check_money(drink["cost"], payment):
                make_coffee(choice, drink["ingredients"])
    else:
        print(f"Choice not found. Try again!")
