# 
# 


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
money = 0

def report():
    print(f"Water {resources['water']}ml")
    print(f"Milk {resources['milk']}ml")
    print(f"Coffee {resources['coffee']}g")
    print(f"Money ${money}")


def insert_money():
    total = int(input("How many quarters?: "))
    total += int(input("How many dimes?: "))
    total += int(input("How many nickles?: "))
    total += int(input("How many pennies?: "))
    return total

def check_resources(choice):
    requirment_resource = MENU[choice]["ingredients"]
    for resorce in resources:
        if resources[resorce] < requirment_resource[resorce]:
            return resorce
        else:
            return 0

def recount_resources(choice):
    requirment_resource = MENU[choice]["ingredients"]
    for resorce in resources:
        if resorce in requirment_resource:
            resources[resorce] = resources[resorce] - requirment_resource[resorce]


def make_a_coffe():
    coffe_machine_on = True
    while coffe_machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino: ")
        if choice == 'report':
            report()
        elif choice in MENU:
            posibility = check_resources(choice)
            if posibility == 0:
                cash = insert_money()
                coffe_price = MENU[choice]["cost"]
                change = cash - coffe_price*100
                print(change)
                print(type(change))
                if cash >= coffe_price*100:
                    global money
                    resources = recount_resources(choice)
                    money += coffe_price
                    print(f"Here is your {choice} Enjoy!")
                    if change > 0:
                        print(f"Here is ${change/100} in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {posibility}.")
        elif choice == 'off':
            coffe_machine_on = False


make_a_coffe()
