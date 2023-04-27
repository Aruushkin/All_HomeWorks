ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, ten))
square = list(map(lambda n: n ** 2, evens))
print(f"Целые числа списка ten: {ten}")
print(f"Четныее числа списка ten: {list(evens)}")
print(f"Возденные в квадрат из списка evens: {list(square)}")

def ten(the_numbers=ten):
    while True:
        try:
            index = input('enter index: ')
            if index == 'exit':
                print('выход')
                break
            else:
                print(the_numbers(int(index)))
        except Exception:
            print(f" Индекс: от 0 до {len(the_numbers) -1} ")

ten()
