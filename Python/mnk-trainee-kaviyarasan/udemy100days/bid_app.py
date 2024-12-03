# TODO-1: Ask the user for input
bids = {}
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bid(bid_dict):
    highest_bid = 0
    bid_winner_name = ""
    for bidder in bid_dict:
        bid_price = bid_dict[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            bid_winner_name = bidder
    print(f"\nhighest bid amount ${highest_bid}, the winner is {bid_winner_name}")

highest_bids = True

while highest_bids:

    name = input("enter your name : ")
    bid = int(input("enter bid amount:"))
    bids[name] = bid
    make_bid = input("does any other want to make bid if you want yes or no : ").lower()
    if make_bid == "no":
        highest_bids = False
        find_highest_bid(bids)
    elif make_bid == "yes":
        print("\n" * 20)

