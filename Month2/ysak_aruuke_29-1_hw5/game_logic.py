import random
from decouple import config



def play_game():
    initial_money = int(config("MY_MONEY"))
    money = initial_money

    numbers = list(range(1, 31))

    while True:
        print("Ваш текущий капитал:", money)

        bet = int(input("Введите сумму ставки: "))

        winning_number = random.choice(numbers)

        selected_number = int(input("Введите номер слота (от 1 до 30): "))

        if selected_number == winning_number:
            money += bet * 2
            print("Вы выиграли!")
        else:
            money -= bet
            print("Вы проиграли!")

        choice = input("Хотите продолжить игру? (да/нет): ")
        if choice.lower() != "да":
            break

    if money > initial_money:
        print("Поздравляем! Вы в выигрыше.")
    elif money < initial_money:
        print("К сожалению, вы в проигрыше.")
    else:
        print("Вы закончили игру с тем же капиталом, с которого начали.")