data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if i == str(i):
        letters.extend(i)
    else:
        numbers.append(i)

print(f"Строка1: {letters}")
print(f"Числа, бул1: {numbers}")

del numbers[0]
letters.insert(0, numbers[0])
numbers.insert(2, 2)
numbers.pop(0)
numbers.sort()
letters.reverse()
letters.insert(0, letters[8])
letters.pop(9)
letters[1] = 'G'
letters[7] = 'c'
numbers[1] = numbers[1]**2
numbers[2] = numbers[2]**2

letters = tuple(letters)
numbers = tuple(numbers)


print("-------")
print(f"Строка2: {letters}")
print(f"Числа, бул2: {numbers}")


