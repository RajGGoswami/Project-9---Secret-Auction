# Day 9 – Secret Auction
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Working with dictionaries to store dynamic data
# - Using functions to process dictionary values
# - Looping through dictionaries to find maximum values
# - Managing program flow with while loops
# - Clearing the console for a better user experience
# - Separating logic into reusable functions
#
# This project simulates a real-world sealed-bid auction
# where bidders cannot see each other’s bids.

import os
from art import logo

# Secret Auction

# Dictionary to store bidder names and their bids
bid_dict = {}

continue_bidding = True
print(logo)


def find_highest_bidder(bidding_dict):
    # Initialize variables to track highest bid
    highest_bidder = ""
    highest_bid = 0

    # Loop through each bidder in the dictionary
    for bidder in bidding_dict:
        if bidding_dict[bidder] > highest_bid:
            highest_bidder = bidder
            highest_bid = bidding_dict[bidder]

    # Display the winner
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


# Main bidding loop
while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid_value = int(input("What is your bid?: $"))

    # Store bidder name and bid amount
    bid_dict[bidder_name] = bid_value

    # Ask if there are more bidders
    more_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

    if more_bidders == "yes":
        # Clear screen so next bidder cannot see previous bids
        os.system('cls')
    else:
        os.system('cls')
        continue_bidding = False
        find_highest_bidder(bid_dict)
