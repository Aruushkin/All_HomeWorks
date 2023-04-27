while True:
    word = input('Введите слово (exit) : ')
    if word == 'exit':
        print('goodbay!')
        break

    counter_glas = 0
    counter_sogl = 0
    counter = 0
    consonants1 = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyzБВГДЖЭЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPRSTVWYZ'
    for i in word:
        if i in consonants1:
            counter_sogl += 1

    consonants2 = 'ауоыиэяюёеaeiouАУОЫИЭЯЁЕAEIOU'
    for i in word:
        if i in consonants2:
            counter_glas += 1

    for i in word:
        if i in consonants1 or consonants2:
            counter += 1

    print(f'Слово: {word}')
    print(f'Количество букв: {counter}')
    print(f'Согласных букв: {counter_sogl}')
    print(f'Гласных букв: {counter_glas}')
    print(f'Гласные: {round(counter_glas / len(word) * 100, 2)}%')
    print(f'Согласные: {round(counter_sogl / len(word) * 100, 2)}%')