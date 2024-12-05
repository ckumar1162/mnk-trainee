
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def my_function():
    my_local_var = 2


# This will cause a NameErrorr
#print(my_local_var)

my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
my_function()

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()


player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()
game()
