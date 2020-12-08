# Write your code here
from random import randint
import functools
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS card')
conn.commit()


def open_connection():
    return sqlite3.connect("card.s3db")


def handle_enumerate(arg, e):
    for index, item in enumerate(arg):
        return arg[index]


def write_query(query):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()


def create_table():
    conn = open_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            f'CREATE TABLE IF NOT EXISTS card ( id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


create_table()


def fetch_one(query):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchone()


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
        conn = sqlite3.connect("card.s3db")
        cur = conn.cursor()
        cur.execute(f'INSERT INTO card (number, pin) VALUES ({card_number}, {pin_number})')
        conn.commit()
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin_number)
        handle_func()
    elif entry_number == 2:
        print("Enter your card number:")
        card_number_input = int(input())
        print("Enter your PIN:")
        pin_number_input = int(input())
        card_number = fetch_one(f'SELECT number FROM card WHERE number = {int(card_number_input)}')
        pin_number = fetch_one(f'SELECT pin FROM card WHERE pin = {int(pin_number_input)}')
        print(f"pin_number {handle_enumerate(pin_number, pin_number_input)}")
        print(f"card_number {handle_enumerate(card_number, card_number_input)}")
        if int(handle_enumerate(pin_number, pin_number_input)) != pin_number_input \
                or \
                int(handle_enumerate(card_number, card_number_input)) != card_number_input:
            print("Wrong card number or PIN!")
            handle_func()
        else:
            print("You have successfully logged in!")
            again = int(input())
            handle_func_entered(again, card_number)
    else:
        print('Bye!')


def handle_func_entered(entry_arg, card_number_arg=''):
    balance_query = fetch_one('SELECT balance FROM card')
    item_enumerate = handle_enumerate(balance_query)
    if entry_arg == 1:
        print(f"Balance: {int(item_enumerate)}")
        handle_func_entered(int(input()))
    elif entry_arg == 2:
        print('Enter income:')
        income_entry = input()
        sum_balance = int(income_entry) + int(item_enumerate)
        write_query(f'UPDATE card SET balance = {int(sum_balance)} WHERE number = {card_number_arg}')
        print("Income was added!")
        handle_func_entered(int(input()))
    elif entry_arg == 3:
        do_transfer(card_number_arg)
    elif entry_arg == 4:
        close_account(card_number_arg)
    elif entry_arg == 5:
        print("You have successfully logged out!")
        return
    else:
        print('Bye!')


def do_transfer(arg):
    # enter_
    # if
    print('do_transfer')


def close_account(arg):
    query = f"DELETE FROM card WHERE number = {handle_enumerate(arg)}"
    write_query(query)
    print(query)


handle_func()
