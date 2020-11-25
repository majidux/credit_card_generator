# Write your code here
from random import randint
import functools


def create_account_identifier():
    return randint(10000, 99999)


def create_bin_number():
    return randint(1000, 9999)


def create_check_sum():
    return randint(0, 9)


def luhn_algorithm(entry_number, check_sum):
    separated_number = list(entry_number)
    new_list = []
    for i, j in enumerate(separated_number):
        if i % 2 == 1:
            new_list.append(int(j))
        else:
            new_list.append(int(j) * 2)
    return functools.reduce(lambda a, b: a + b, new_list) + check_sum


class CreateCard:
    def __init__(self):
        self.account_identifier = create_account_identifier()
        self.bin_number = create_bin_number()
        self.check_sum = create_check_sum()
        self.card_number = f"{self.account_identifier}{self.bin_number}{self.check_sum}"
        self.card_pin = randint(1000, 9999)
        self.sum_new_list = luhn_algorithm(f"400000{self.card_number}", self.check_sum)
        self.card_number_generated = f"400000{self.card_number}"
        self.items = {
            "card_number": int(self.card_number_generated),
            "pin_number": self.card_pin
        }

    def create_card(self):
        if not self.sum_new_list % 10 == 0:
            while not self.sum_new_list % 10 == 0:
                self.account_identifier = create_account_identifier()
                self.bin_number = create_bin_number()
                self.check_sum = create_check_sum()
                self.sum_new_list = luhn_algorithm(f"400000{self.card_number}", self.check_sum)
                self.card_number_generated = f"400000{self.card_number}"
                self.create_card()
                self.items = {
                    "card_number": int(self.card_number_generated),
                    "pin_number": self.card_pin
                }
        else:
            created_card = {
                "card_number": int(self.card_number_generated),
                "pin_number": self.card_pin
            }
            self.items = created_card


card = CreateCard()


def handle_func():
    entry_number = int(input())
    carder = card.items
    if entry_number == 1:
        card2 = CreateCard()
        card2.create_card()
        carder = card2.items
        card_number = carder.get('card_number')
        pin_number = carder.get('pin_number')
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin_number)
        handle_func()
    elif entry_number == 2:
        card_number = carder.get('card_number')
        pin_number = carder.get('pin_number')
        print("Enter your card number:")
        card_number_input = int(input())
        print("Enter your PIN:")
        pin_number_input = int(input())
        print(pin_number)
        if pin_number != pin_number_input or card_number != card_number_input:
            print("Wrong card number or PIN!")
            again = int(input())
            handle_func_entered(again)
        else:
            print("You have successfully logged in!")
            again = int(input())
            handle_func_entered(again)
    else:
        print('Bye!')


def handle_func_entered(entry_arg):
    print("Press 1 or 2")
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
