date = int(input('Введите день: '))
month = str(input('Введите месяц: '))

if date >= 21 and date <= 31 and month == 'март' or date >= 1 and date <= 20 and month == 'апрель':
    print('овен')
elif date >= 21 and date <= 31 and month == 'апрель' or date >= 1 and date <= 21 and month == 'май':
    print('телец')
elif date >= 22 and date <= 31 and month == 'май' or date >= 1 and date <= 21 and month == 'июня':
    print('близнец')
elif date >= 22 and date <= 31 and month == 'июня' or date >= 1 and date <= 22 and month == 'июля':
    print('рак')
elif date >= 23 and date <= 31 and month == 'июля' or date >= 1 and date <= 21 and month == 'август':
    print('лев')
elif date >= 22 and date <= 31 and month == 'август' or date >= 1 and date <= 23 and month == 'сентябрь':
    print('дева')
elif date >= 24 and date <= 31 and month == 'сентябрь' or date >= 1 and date <= 23 and month == 'октябрь':
    print('весы')
elif date >= 24 and date <= 31 and month == 'октябрь' or date >= 1 and date <= 22 and month == 'ноябрь':
    print('скорпион')
elif date >= 23 and date <= 31 and month == 'ноябрь' or date >= 1 and date <= 22 and month == 'декабрь':
    print('стрелец')
elif date >= 23 and date <= 31 and month == 'декабрь' or date >= 1 and date <= 20 and month == 'январь':
    print('козерог')
elif date >= 21 and date <= 31 and month == 'январь' or date >= 1 and date <= 19 and month == 'февраль':
    print('водолей')
elif date >= 20 and date <= 31 and month == 'февраль' or date >= 1 and date <= 21 and month == 'март':
    print('рыбы')
else:
    print('не правильно ввели месяц или день!')

