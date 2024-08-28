from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True


while is_on:
    customerOrder = input(f"What would you like? (espress/latte/cappuccino):").lower()
    if customerOrder == "off":
        is_on = False
    elif customerOrder == "report":
        print(coffee.report())
        print(money.report())
    else:
        drink = menu.find_drink(customerOrder)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)


