from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print(f"Choice not found. Try again!")