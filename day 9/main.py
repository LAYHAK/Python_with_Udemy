from logo import logo
from clearConsole import clear
from winner import find_winner

print(logo)
print("Welcome to the secret auction program.")
auction = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bid = float(input("How much do you want to bid?: $"))
    auction[name] = bid
    print("are there any other bidders? Type 'yes' or 'no'")
    answer = input().lower()
    if answer == 'no':
        find_winner(auction)
        bidding_finished = True
    elif answer == 'yes':
        clear()
        continue
    else:
        print("Invalid input. Please try again.")
        continue

