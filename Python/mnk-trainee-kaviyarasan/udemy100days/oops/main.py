from pandas import options

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()
menu = Menu()
coffee_maker.report()


while True:
    menu_of_coffee = menu.get_items()
    user_choice = input(f"what would you like? ({menu_of_coffee}): ").lower()
    if user_choice == "off":
        print("Thankyou good bye")
        break
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            print(coffee_maker.make_coffee(drink))

