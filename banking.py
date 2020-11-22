# Write your code here
from random import randint


def handle_func(entry_number, entry_card_detail=None):
    if entry_number == 1:
        carder = card.create_card()
        print("Press 2 if you want to login")
        return carder
    elif entry_number == 2:
        print(entry_card_detail)
        print("Enter card number")
    else:
        print('Exit')


class CreateCard:
    def __init__(self):
        self.mii_number = randint(0, 9)
        self.bin_number = randint(10000, 99999)
        self.account_identifier = randint(100000000, 999999999)
        self.check_sum = randint(0, 9)
        self.card_number = self.mii_number + self.bin_number + self.account_identifier + self.check_sum
        self.card_pin = randint(0000, 9999)

    def create_card(self):
        created_card = {
            "card_number": self.card_number,
            "pin_number": self.card_pin
        }
        return created_card


card = CreateCard()

print("Press 1 for creating card")
task = int(input())
card_detail = handle_func(task)
task2 = int(input())
handle_func(task2, card_detail)
