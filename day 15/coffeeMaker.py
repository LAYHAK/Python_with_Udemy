from menu import MENU
from method import check_resources, process_coins, make_coffee, print_report

print("Welcome to the Coffee Maker!")
while True:
    print("Please select from the following menu:")
    print("espresso: $1.50")
    print("latte: $2.50")
    print("cappuccino: $3.00")
    print("off: turn off the coffee maker")
    print("report: print a report of the coffee maker's resources")
    user_input = input("What would you like? ").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        if check_resources(user_input):
            if process_coins(user_input):
                make_coffee(user_input)
    else:
        print("Sorry, I don't understand.")
