from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1.Print report

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

is_on=True

while is_on:
    # get items name from menu
    options=menu.get_items()
    choice=input(f"what would you like ? {options}: ")
    # printing choice entered by user
    print(choice)

    if choice=="off":
        is_on=False
    elif choice=="report":
        # used to report
        coffee_maker.report()
        money_machine.report()
    else:
        # check for item entered by user choice and return items if its present else return false
        drink=menu.find_drink(choice)
        # check for sufficient of resources
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)