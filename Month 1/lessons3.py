attempts = 5

while attempts > 0:
    temperature = input(f'enter degree {attempts} попыток' )
    if temperature == 'exit':
        print('goodbay!')
        break
    temperature = int(temperature)

    if temperature >= -40 and temperature <= 10:
        print('холодно')
    elif temperature >= 11 and temperature <= 20:
        print('прохладно')
    elif temperature >= 21 and temperature <= 27:
        print('тепло')
    elif temperature >= 28 and temperature <= 52:
        print('жарко')
    else:
        print('че за погода, ваа!')
    attempts -= 1