from menu import MENU, resources

def maintenance(value):
    if value == "off":
        return False
    else:
        return True

def report():
    for i in resources:
        print(f"{i}: {resources[i]}")

def choose_a_drink():
    drink_of_choice = input("What would you like! (espresso/latte/cappuccino): ").lower()
    while drink_of_choice != "espresso" or drink_of_choice != "latte" or drink_of_choice != "cappuccino":
        if drink_of_choice == "report":
            report()
            drink_of_choice = input("What would you like! (espresso/latte/cappuccino): ").lower()
        elif drink_of_choice == "off":
            return drink_of_choice
        elif drink_of_choice == "espresso" or drink_of_choice == "latte" or drink_of_choice == "cappuccino":
            return drink_of_choice
        else:
            print("Sorry!! That type of drink is not available... Please choose something from the options listed.")
            drink_of_choice = input("What would you like! (espresso/latte/cappuccino): ").lower()
    return drink_of_choice

def pay():
    print(f"Please insert coins. (Cost: ${MENU[drink_choice]["cost"]})")
    quarters = int(input("how many quarters?($0.25): "))
    dimes = int(input("how many dimes?($0,10): "))
    nickles = int(input("how many nickles?($0.05): "))
    pennies = int(input("how many pennies?($0.01): "))
    payment1 = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return float(payment1)

def payment_check(drink_choice1):
    payment = pay()
    if payment < MENU[drink_choice1]["cost"]:
        while payment < MENU[drink_choice1]["cost"]:
            if payment >= MENU[drink_choice1]["cost"]:
                return float(payment)
            elif payment < MENU[drink_choice1]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                drink_choice1 = choose_a_drink()
                if drink_choice1 == "off":
                    return drink_choice1
                payment = pay()
                if payment >= MENU[drink_choice1]["cost"]:
                    return float(payment)
    elif payment >= MENU[drink_choice1]["cost"]:
        return float(payment)


drink_choice = choose_a_drink()
on = maintenance(drink_choice)
while on:
    payment2 = payment_check(drink_choice)
    on = maintenance(payment2)
    if on:
        cost_of_drink = MENU[drink_choice]["cost"]
        change = payment2 - cost_of_drink
        print(f"Here is ${change} in change.")
        resources["money"] += cost_of_drink
        resources["water"] -= MENU[drink_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink_choice]["ingredients"]["coffee"]
        if 'milk' in MENU[drink_choice]["ingredients"]:
            resources["milk"] -= MENU[drink_choice]["ingredients"]["milk"]
        print(f"Here is your {drink_choice}☕. Enjoy!")
    drink_choice = choose_a_drink()
    on = maintenance(drink_choice)
    while on and resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
        print("Sorry there isn't enough water")
        drink_choice = choose_a_drink()
        on = maintenance(drink_choice)
    while on and resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
        print("Sorry there isn't enough coffee")
        drink_choice = choose_a_drink()
        on = maintenance(drink_choice)
    if on and 'milk' in MENU[drink_choice]["ingredients"]:
        while on and resources["milk"] < MENU[drink_choice]["ingredients"]["milk"]:
            print("Sorry there isn't enough milk")
            drink_choice = choose_a_drink()
            on = maintenance(drink_choice)