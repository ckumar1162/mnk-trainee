#Secret auction program
print("""
                  __
               (_()  \
          \__/  ||    \  \__/
          (oo)  /)       (oo)
         //~~\\//       //~~\\
         \\__/\/   _____\\__//_____
          |/\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|____jro

""")

print("Welcome to secret auction")
bidding_details = {}
continue_looping = True

while continue_looping:

    name = input("What is ur name ?\n")
    bid = int(input("Enter the amount?\n"))
    people = input("Are there any other bidders?Type 'yes' or 'no'\n")  
    bidding_details[name] = bid

    if people == "no":
        continue_looping = False
        
    elif people == "yes":
        print("\n" * 20)
    winner = max(bidding_details, key=bidding_details.get)        
print(f"The winner of the bidding is {winner}")    