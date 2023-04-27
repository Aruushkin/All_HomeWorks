import random
from random import randint
random_number = 0
attempts = 3
while True:

    number = random.randint(1, 100)
    print(number)
    print(attempts)
    random_number = int(input("Введите число: "))
    if random_number > 100:
        print("Не больше 100")
    elif random_number < 0:
        print("Нельзя отрицательное число")
    elif number != random_number:
        attempts -= 1

    if random_number == number and attempts > 0:
        print("Я угадал число")
        with open("results.txt", "a") as file:
            file.write(f"Угаданное число {number}\n")
            file.write(f"Пoпытки {attempts}\n")
            break

    elif attempts == 0:
        print("Попытки закончились")
        break










