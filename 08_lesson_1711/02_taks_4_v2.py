n = input('Введите число: ')
mult = 1

for digit in n:
    print(f'{mult} * {digit} = {mult * int(digit)}')
    mult *= int(digit)

