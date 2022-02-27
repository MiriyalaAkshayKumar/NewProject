print("This is a Auction Program")
from art import logo
print(logo)

bids={}
bidding_finished = False

while not bidding_finished:
    name = input("Enter your Name : \n")
    bid_price = input("Enter the Bid amount $: \n")
    bids[name]=bid_price
    should_continue= input("Are any other bidders ? Type 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True



