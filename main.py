from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


new_money_machine = MoneyMachine()
new_coffee_maker = CoffeeMaker()
new_menu = Menu()


def run_coffee_machine():
    is_working = True
    while is_working:
        user_choice = input(f"What would you like? {new_menu.get_items()}?")

        if user_choice == "espresso" or user_choice == "cappuccino" or user_choice == "latte":
            user_choice_menu_item = new_menu.find_drink(user_choice)
            resources_status = new_coffee_maker.is_resource_sufficient(user_choice_menu_item)

            if resources_status:
                new_coffee_maker.make_coffee(user_choice_menu_item)
                payment_result = new_money_machine.make_payment(user_choice_menu_item.cost)

                if payment_result:
                    print(f"Here is your {user_choice_menu_item.name}. Enjoy!")

        elif user_choice == "report":
            new_coffee_maker.report()
        elif user_choice == "off":
            is_working = False
        else:
            print("Something went wrong. ")


run_coffee_machine()

