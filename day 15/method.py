from menu import MENU, resources


def check_resources(drink):
    """Check if there are enough resources to make the drink."""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins(drink):
    """Process the coins inserted by the user."""
    print("Please insert coins.")
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    quarters = int(input("How many quarters?: (espresso/latte/cappuccino):"))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total > MENU[drink]["cost"]:
        resources["money"] += MENU[drink]["cost"]
        print(f"Here is ${round(total - MENU[drink]['cost'], 2)} in change.")
    return True


def make_coffee(drink):
    """Make the drink."""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")


def print_report():
    """Print a report of the coffee maker's resources."""
    print("Report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
