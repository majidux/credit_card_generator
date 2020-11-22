# Write your code here
from random import randint


def handle_func():
    card = CreateCard()
    entry_number = int(input())
    global carder
    if entry_number == 1:
        carder = card.create_card()
        # print("Press 2 if you want to login")
        handle_func()
    elif entry_number == 2:
        card_number = carder.get('card_number')
        pin_number = carder.get('pin_number')
        print("Enter your card number:")
        card_number_input = int(input())
        print("Enter your PIN:")
        pin_number_input = int(input())
        if pin_number != pin_number_input or card_number != card_number_input:
            print("Wrong card number or PIN!")
            again = int(input())
            handle_func_entered(again)
            return
        else:
            print("You have successfully logged in!")
            again = int(input())
            handle_func_entered(again)
            # print('Press 1 for balance')
    else:
        print('Bye!')


def handle_func_entered(entry_arg):
    print("Press 1 or 2")
    if entry_arg == 1:
        print(entry_arg * 235)
        balance = int(input())
        handle_func_entered(balance)
    elif entry_arg == 2:
        print("You have successfully logged out!")
        return
    else:
        print('Bye!')


class CreateCard:
    def __init__(self):
        self.mii_number = randint(0, 9)
        self.bin_number = randint(10000, 99999)
        self.account_identifier = randint(1000000000, 9999999999)
        self.check_sum = randint(0, 9)
        self.card_number = self.mii_number + self.bin_number + self.account_identifier + self.check_sum
        self.card_pin = randint(0000, 9999)

    def create_card(self):
        card_number_generated = f"400000{self.card_number}"
        print("Your card has been created")
        print("Your card number:")
        print(card_number_generated)
        print("Your card PIN:")
        print(self.card_pin)
        created_card = {
            "card_number": int(card_number_generated),
            "pin_number": self.card_pin
        }
        return created_card


# print("Press 1 for creating card")
handle_func()
