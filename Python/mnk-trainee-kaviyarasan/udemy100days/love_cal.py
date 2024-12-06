
def love_calculator(name1, name2):

    names = name1 + name2

    count_true = sum(names.count(char) for char in "true")

    count_love = sum(names.count(char) for char in "love")

    print(str(count_true) + str(count_love))
love_calculator("true", "love")