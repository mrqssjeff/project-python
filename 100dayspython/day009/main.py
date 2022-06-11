auction = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print("Welcome to the Secret Auction Program!")
end_game = False
while not end_game:
    name = str(input("What is your name?: ")).strip().capitalize()
    bid = int(input("What's your bid?: "))
    auction[name] = bid
    response = str(input("Are there any other bidders? Type 'yes' or 'no': ")).strip().lower()
    if response == 'no':
        find_highest_bidder(auction)
        end_game = True
