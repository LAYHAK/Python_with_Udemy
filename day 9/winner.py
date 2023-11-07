def find_winner(auction):
    highest_bid = 0
    winner = ""
    for bidder in auction:
        if auction[bidder] > highest_bid:
            highest_bid = auction[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

