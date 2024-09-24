from multiprocessing.forkserver import connect_to_new_process

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0

def get_order() -> str:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order

def print_report():
    global profit
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Profit: $ {profit}")


def process_coins() -> float:
    total = float(0)
    quarter = input("Quarters: ")
    dime = input("Dimes: ")
    nickel = input("Nickel: ")
    penny = input("Penny: ")

    if quarter != "":
        total += 0.25 * int(quarter)
    if dime != "":
        total += 0.1 * int(dime)
    if nickel != "":
        total += 0.05 * int(nickel)
    if penny != "":
        total += 0.01 * int(penny)

    return round(total,2)


def check_stock(order: str) -> bool:
    # check resources
    if order == "espresso":
        if resources["water"] >= MENU[order]["ingredients"]["water"] \
                and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            return True
    elif order == "latte" or order == "cappuccino":
        if resources["water"] >= MENU[order]["ingredients"]["water"] \
                and resources["coffee"] >= MENU[order]["ingredients"]["coffee"] \
                and resources["milk"] >= MENU[order]["ingredients"]["milk"]:
            return True

    return False

def process_order(order, coins):
    global profit
    if coins >= MENU[order]["cost"]:
        # update money
        profit += MENU[order]["cost"]
        change = round(coins - MENU[order]["cost"], 2)
        print(f"Change: {change}")
        # update stock
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        if order != "espresso":
            resources["milk"] -= MENU[order]["ingredients"]["milk"]
        # serve drink
        print(f"Here is your {order}, enjoy!")
    else:
        print("Not enough coins, refunded")


def run():
    while True:
        order = get_order()
        if order == "off":
            quit()
        elif order == "report":
            print_report()
        else:
            if check_stock(order):
                coins = process_coins()
                print(f"Coins: {coins} Cost: {MENU[order]["cost"]}")
                process_order(order, coins)
            else:
                print("Sorry, out of stock for that order")


run()