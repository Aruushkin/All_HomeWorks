import configparser
import random
from decouple import config

def get_initial_money():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return int(config['DEFAULT']['MY_MONEY'])


def play_game():
    while True:
        # initial_capital = config("MY_MONEY")
        initial_capital = get_initial_money()
        slots = list(range(1, 31))
        bet = int(input(f'Ваш нынешний капитал {initial_capital} Делайте ставку;'))
        winning_slot = random.choice(slots)
        if bet == winning_slot:
            print(f'Поздравляю! Вы выйграли: {bet * 2}')
            initial_capital += bet * 2
            print(f'Игра окончена. Ваш итоговый баланс: {bet}')
        else:
            print(f'Сожалею, вы проиграли: {bet}')
            initial_capital -= bet
            print(f'Игра окончена. Ваш итоговый баланс: {bet}')
            choice = input("Хотите сыграть еще? (да/нет): ")
            if choice == "да":
                continue





