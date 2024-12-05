# TODO-1: Ask the user for
import art
print(art.logo)
#name = str(input("what is your name?\n"))
#bit = int(input("what is your bit?\n"))
# TODO-2: Save data into dictionary {name: price}
dict={}

def winner(dict):
    bit =0
    winner1 = ''
    for key in dict:
        if dict[key] > bit:
            bit = dict[key]
            winner1 = key
    print(f"winner is {winner1} bit is {bit}")

# TODO-3: Whether if new bids need to be added
new_bit = True
while new_bit:
    name = str(input("what is your name? :\n"))
    price = int(input("what is your bit?: \n"))
    dict[name] = price
    new = input("if there are other user want to bit? type yes or no\n").lower()
    if new == "no":
        new_bit = False
        winner(dict)
        #print(f"winner is " + max(dict, key=dict.get) +" bit is "+str(dict[max(dict, key=dict.get)]))
    elif new == "yes":
        print("\n" * 20)


# TODO-4: Compare bids in dictionary

'''bit =0
winner = ''
for key in dict:
    if dict[key] > bit:
        bit = dict[key]
        winner = key
print(f"winner is {winner}")'''

