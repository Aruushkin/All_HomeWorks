def multiply_numbers(*args):
    result = 1
    for i in args:
        result *= i
    return print(result)

multiply_numbers(5, 5, 5)

def mirror(hello, hi='unknown'):
    if hello == hi:
        return print(True)
    else:
        return print(False)

mirror("fff", "fff")

def calculator():
    operator = input('operator: ')
    number1 = float(input('number1:'))
    number2 = float(input('number2: '))

    if operator == '+':
        print(number1 + number2)
    elif operator == '-':
        print(number1 - number2)
    elif operator == '*':
        print(number1 * number2)
    elif operator == '**':
        print(number1 ** number2)
    elif operator == '/':
        print(number1 / number2)
    elif operator == '//':
        print(number1 // number2)
    elif operator == '%':
        print(number1 % number2)
    else:
        return print(operator)

calculator()






