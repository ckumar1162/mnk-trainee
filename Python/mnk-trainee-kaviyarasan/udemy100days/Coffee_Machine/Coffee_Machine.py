MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}
profit = 0

# check weather resources is available
def check_resources(ingredients):
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            print(f"Sorry, not enough {item}.")
            return False
    return True

# process the cost of the coffee
def process_payment(cost):
    print("Insert coins:")
    total = (int(input("Quarters: ")) * 0.25 +
             int(input("Dimes: ")) * 0.10 +
             int(input("Nickels: ")) * 0.05 +
             int(input("Pennies: ")) * 0.01)
    if total >= cost:
        change = round(total - cost, 2)
        print(f"Change: ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Not enough money. Refunding.")
        return False

# make drink and reduce the items of resources
def make_drink(drink_name, ingredients):
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} Enjoy")

# report the user, resources left ?
def report():
    for item, amount in resources.items():
        print(f"{item.capitalize()}: {amount}")
    print(f"Profit: ${profit}")


# loop until no resource left or user choice off
while True:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if choice == "off":
        print("Turning off Good bye")
        break
    elif choice == "report":
        report() # calls the report function
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]): # calls check_resources function
            if process_payment(drink["cost"]): # calls payment function
                make_drink(choice, drink["ingredients"]) # calls make drink function
    else:
        print("Invalid choice. Please select again.")
