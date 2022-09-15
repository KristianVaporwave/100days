from replit import clear
from art import logo


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} they won with a bid amount of ${highest_bid}")

print(logo)
print("Welcome to the auction house.")

while not bidding_finished:
    bidder_name = input("Type your name: ")
    bid_amount = input("Input your bid: $")
    bids[bidder_name] = bid_amount
    should_continue = input("Are there any other bidders: yes or no \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()



