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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(items):
    for item in items:
        if resources[item] < items[item]:
            print(f"Sorry there is not enough{item}")
            return False
    return True


def coins():
    print(" insert coins")
    quarters = float(input("quarters: ")) * 0.25
    dimes = float(input(' dimes: ')) * 0.10
    nickles = float(input(" nickles: ")) * 0.05
    pennies = float(input("pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_transtion(payment, drinks):
    if drinks['cost'] <= payment:
        change = round((payment - drinks['cost']), 2)
        print(f" your change is: {change}")
        global profit
        profit += drinks['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(drinks, user):
    for item in drinks['ingredients']:
        resources[item] -= drinks['ingredients'][item]
    print(f"Here is your {user}. Enjoy!")




profit = 0
turn_off = False
while not turn_off:

    user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user == "off":
        turn_off = True
    elif user == 'report':
        print(f"water : {resources['water']}ml.")
        print(f"milk : {resources['milk']}ml.")
        print(f"coffee : {resources['coffee']}g.")
        print(f"money : ${profit}.")
    else:
        drinks = MENU[user]
        if check_resource(drinks['ingredients']):
            payment = coins()
            if check_transtion(payment, drinks):
                make_coffee(drinks, user)

