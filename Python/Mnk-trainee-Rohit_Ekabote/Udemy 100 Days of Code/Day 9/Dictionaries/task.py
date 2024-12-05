programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
colours = {"apple": "red", "pear": "green", "banana": "yellow"}
print(colours["apple"])
colours["peach"] = "pink"
colours["apple"] = "green"
print(colours["apple"])
colours[1] = "green"

for key in colours:
    print(key)

for key in colours:
    print(colours[key])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])