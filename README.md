# Project-9---Secret-Auction

This is a beginner Python project built as part of my 100 Days of Code challenge.

The goal of this project is to simulate a secret auction, where multiple users can place bids without seeing each other’s values.

**Project Overview**

This project is a command-line based auction system.

Each bidder:

Enters their name

Enters their bid amount

Does not see previous bids

At the end of the auction:

The program determines the highest bidder

Announces the winner and winning bid

**Project File Structure**

main.py
Contains the auction logic, user input handling, and winner calculation.

art.py
Stores the ASCII art logo displayed at program start.

**Why this project exists**

This project helped me understand how to manage and process dynamic user data.

It simulates a real-world sealed-bid auction and reinforces the use of dictionaries for storing key-value pairs.

**What I learned**

How to store and update values in dictionaries

How to loop through dictionary keys and values

How to compare values to find a maximum

How to separate logic into functions

How to control program flow with while loops

How to clear the console for better user experience

**How the code works (step-by-step)**

Display the auction logo

Create an empty dictionary to store bids

Ask each bidder for their name and bid amount

Store the data in the dictionary

Clear the screen so bids remain secret

Repeat until there are no more bidders

Loop through all bids to find the highest value

Print the auction winner

**Example Output**

What is your name?:
Alex


What is your bid?: $
250


Are there any other bidders? Type 'yes' or 'no'.
yes


What is your name?:
Jamie


What is your bid?: $

300

Are there any other bidders? Type 'yes' or 'no'.

no

The winner is Jamie with a bid of $300
