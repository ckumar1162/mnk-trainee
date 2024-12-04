menu={
    "espresso":
        {
        "ingredient":
            {
            "water":50,
            "coffee":18,
            },
        "cost":1.5
    },
    "latte":
        {
            "ingredient":
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
            "cost": 2.5
        },
    "cappuccino":
        {
            "ingredient":
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
            "cost": 3.0
        }
}

resources={
    "water":300,
    "milk": 200,
    "coffee": 100
}
def is_resource_sufficient(ingredient):
    """Check for resource sufficients"""
    for items in ingredient:
        if resources[items] >= ingredient[items]:
            print("sufficient")
            return True
        else:
            print(f"Sorry. there is not enough {items}.")
            return False

def process_coins():
    """Return total amount of coins to buy coffee"""
    print("Please insert coins")
    total = int(input("How many quoters? : ")) * 0.25
    total += int(input("How many dimes?  : ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_money_enough(money_received, drink_cost):
    """Check for money entered by user is enough for order drink"""
    if money_received >= drink_cost:
        change=round(money_received - drink_cost, 2)
        print(f"Here is {change} dollars in change.")

        global profit
        profit += round(money_received, 2)
        return True
    else:
        print("sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name,order_ingredient):
    """Deduct resources from orders coffee"""
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]

    print(f"Here is your {drink_name} ☕, Enjoy.")



profit=0
is_on=True

while is_on:
    # 1.ask your user for drink choice
    choice=input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    # 2.Turn off coffee machine
    if choice=="off":
        is_on=False
    # 3. Print report of resources
    elif choice=="report":
        print(f"water  : {resources["water"]}ml")
        print(f"milk   : {resources["milk"]}ml")
        print(f"coffee : {resources["coffee"]}g")
        print(f"Money  : ${profit}")
    else:
        # getting  drink name
        drink=menu[choice]
        # check resource sufficient
        if is_resource_sufficient(drink["ingredient"]):
            # ask for insert coins
            amount=process_coins()
            # check if money is enough to buy a coffee
            if is_money_enough(amount,drink["cost"]):
                # make coffee if money is enough and deduct resource ingredient
                make_coffee(choice,drink["ingredient"])
