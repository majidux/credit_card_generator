# Write your code here
from random import randint
import functools


def create_account_identifier():
    return randint(10000, 99999)


def create_bin_number():
    return randint(1000, 9999)


def luhn_algorithm(entry_number):
    separated_number = list(entry_number)
    new_list = []
    final_new_list = []
    for index, item in enumerate(separated_number):
        if (index + 1) % 2 == 0:
            item = item
            new_list.append(int(item))
        else:
            item = 2 * int(item)
            new_list.append(int(item))
    for index, item in enumerate(new_list):
        if item > 9:
            item = int(item) - 9
            final_new_list.append(int(item))
        else:
            item = item
            final_new_list.append(int(item))
    return functools.reduce(lambda a, b: a + b, final_new_list)


class CreateCard:
    def __init__(self):
        self.account_identifier = create_account_identifier()
        self.bin_number = create_bin_number()
        self.card_number = f"{self.account_identifier}{self.bin_number}"
        self.card_pin = randint(1000, 9999)
        self.sum_new_list = luhn_algorithm(f"400000{self.card_number}")
        self.card_number_generated = f"400000{self.card_number}"
        self.items = {
            "card_number": int(self.card_number_generated),
            "pin_number": self.card_pin
        }

    def create_card(self):
        if self.sum_new_list % 10 > 0:
            check_sum = 10 - self.sum_new_list % 10
        else:
            check_sum = 0
        created_card = {
            "card_number": f"{int(self.card_number_generated)}{int(check_sum)}",
            "pin_number": self.card_pin
        }
        self.items = created_card


def handle_func():
    entry_number = int(input())
    global card
    if entry_number == 1:
        card = CreateCard()
        card.create_card()
        carder = card.items
        card_number = carder.get('card_number')
        pin_number = carder.get('pin_number')
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin_number)
        handle_func()
    elif entry_number == 2:
        carder = card.items
        card_number = carder.get('card_number')
        pin_number = carder.get('pin_number')
        print("Enter your card number:")
        card_number_input = int(input())
        print("Enter your PIN:")
        pin_number_input = int(input())
        print(f"type {card_number}")
        if int(pin_number) != pin_number_input or int(card_number) != card_number_input:
            print("Wrong card number or PIN!")
            handle_func()
        else:
            print("You have successfully logged in!")
            again = int(input())
            handle_func_entered(again)
    else:
        print('Bye!')


def handle_func_entered(entry_arg):
    if entry_arg == 1:
        print(0)
        balance = int(input())
        handle_func_entered(balance)
    elif entry_arg == 2:
        print("You have successfully logged out!")
        return
    else:
        print('Bye!')


handle_func()
