import time
run = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0.0
}


def menu():
    global run
    command = input('What ☕ would you like? (espresso/latte/cappuccino):  ').lower()
    if command == 'off':
        print('Turning off...')
        time.sleep(2)
        run = False
    if command == 'report':
        report()
    if command in ['espresso', 'latte', 'cappuccino']:
        if coffee(command):
            bill(command)


def report():
    print('Water: ', resources["water"], 'ml')
    print('Milk: ', resources["milk"], 'ml')
    print('Coffee: ', resources["coffee"], 'g')
    print('Cash: ', resources["money"], '$')


def coffee(x):
    if resources['water'] < MENU[x]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    if resources['milk'] < MENU[x]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return False
    if resources['coffee'] < MENU[x]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    return True


def bill(x):
    print(x, 'cost:', str(MENU[x]['cost']) + '$  Please insert coins.')
    quarters = int(input('How many Quarters ?? : '))
    dimes = int(input('How many Dimes ?? : '))
    nickles = int(input('How many nickles ?? : '))
    cents = int(input('How many cents ?? : '))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (cents * 0.01)
    change = round(total - MENU[x]['cost'], 2)
    if total < MENU[x]['cost']:
        print("Sorry that's is not enough money. Money refunded.")
    else:
        print("It's ok. Please enjoy your ☕", x, "☕", end='')
        resources['water'] -= MENU[x]['ingredients']['water']
        resources['milk'] -= MENU[x]['ingredients']['milk']
        resources['coffee'] -= MENU[x]['ingredients']['coffee']
        resources['money'] += MENU[x]['cost']
        if change > 0:
            print('Here is', change, '$ in change.\n')


while run:
    menu()
